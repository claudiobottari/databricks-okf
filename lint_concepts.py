#!/usr/bin/env python3
"""
lint_concepts.py
================
Find and merge near-duplicate OKF concept files.

Strategy
--------
1. Load precomputed vector embeddings from dbokf-index/ (no API calls needed)
2. Compute pairwise cosine similarity between all 6 000+ concepts (numpy, O(n²))
3. Union-Find clusters: concepts with cosine_sim >= threshold AND related names
4. For each cluster: pick canonical (shortest ID), absorb aliases from duplicates
5. Update every cross-reference in all .md files across the repo
6. Delete duplicate files; update meta.json + vectors.bin
7. Stage + commit

Usage
-----
    python lint_concepts.py --dry-run          # preview, no changes
    python lint_concepts.py                    # apply + commit
    python lint_concepts.py --no-commit        # apply, stage, but do NOT commit
    python lint_concepts.py --threshold 0.96   # lower similarity bar (more merges)
"""

import argparse
import json
import os
import struct
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False
    sys.exit("numpy is required. Install it: pip install numpy")

OKF_DIR = Path(__file__).parent.resolve()
CONCEPTS_DIR = OKF_DIR / "concepts"
INDEX_DIR = OKF_DIR / "dbokf-index"
META_PATH = INDEX_DIR / "meta.json"
VECTORS_PATH = INDEX_DIR / "vectors.bin"
CONFIG_PATH = INDEX_DIR / "config.json"
EXCLUDE_DIRS = {".venv", "node_modules", ".git", "dbokf-index"}


# ---------------------------------------------------------------------------
# Index I/O
# ---------------------------------------------------------------------------

def load_meta():
    with open(META_PATH, encoding="utf-8") as f:
        return json.load(f)


def load_config():
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return json.load(f)


def load_vectors(n, d):
    with open(VECTORS_PATH, "rb") as f:
        n_stored, d_stored = struct.unpack_from("<II", f.read(8))
        if n_stored != n or d_stored != d:
            raise ValueError(
                f"vectors.bin header mismatch: expected ({n},{d}), got ({n_stored},{d_stored})"
            )
        return np.frombuffer(f.read(), dtype=np.float32).reshape(n, d)


def save_vectors(arr, path):
    n, d = arr.shape
    buf = bytearray(8)
    struct.pack_into("<II", buf, 0, n, d)
    with open(path, "wb") as f:
        f.write(buf)
        f.write(arr.astype(np.float32).tobytes())


# ---------------------------------------------------------------------------
# Similarity + clustering
# ---------------------------------------------------------------------------

def cosine_sim_matrix(vectors):
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    v = vectors / norms
    return (v @ v.T).astype(np.float32)


def edit_distance(a, b):
    m, n = len(a), len(b)
    if m < n:
        a, b, m, n = b, a, n, m
    prev = list(range(n + 1))
    for i in range(1, m + 1):
        curr = [i] + [0] * n
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(prev[j - 1], prev[j], curr[j - 1])
        prev = curr
    return prev[n]


STOPWORDS = {
    'a', 'an', 'the', 'of', 'in', 'on', 'for', 'to', 'and', 'or', 'is',
    'are', 'that', 'which', 'it', 'its', 'this', 'with', 'from', 'by', 'as',
    'at', 'be', 'can', 'has', 'have', 'how', 'not', 'use', 'used', 'using',
    'when', 'where', 'whether', 'also', 'each', 'other', 'they', 'their',
}


def name_token_overlap(a, b):
    """Fraction of common name tokens (split by -), relative to the smaller set."""
    ta = set(a.split('-'))
    tb = set(b.split('-'))
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / min(len(ta), len(tb))


def desc_jaccard(da, db):
    """Jaccard similarity of content words in two description strings."""
    wa = set(da.lower().split()) - STOPWORDS
    wb = set(db.lower().split()) - STOPWORDS
    if not wa or not wb:
        return 0.0
    return len(wa & wb) / len(wa | wb)


def names_are_structurally_related(a, b):
    """
    True when names are structurally near-identical:
    one is a prefix of the other, OR edit distance <= 35 % of the longer name,
    AND length ratio >= 0.40.
    """
    if a.startswith(b) or b.startswith(a):
        return True
    lo = min(len(a), len(b))
    hi = max(len(a), len(b))
    if hi == 0 or lo / hi < 0.40:
        return False
    return edit_distance(a, b) / hi <= 0.35


def should_merge(meta_a, meta_b, cos_sim):
    """
    Structural merge decision — two rules:

    Rule 1a (prefix): one ID is a prefix of the other AND cosine >= 0.85.
    Covers: concept-X vs concept-X-suffix-detail (highest confidence).

    Rule 1b (edit): structurally near-identical names (edit_ratio <= 35% of
    longer name, length ratio >= 40%) AND cosine >= 0.88.
    Covers: singular/plural, preposition swap, word insertion/deletion.

    No description-content rule — too many false positives in a single-domain
    corpus where every concept shares vocabulary.
    """
    a, b = meta_a["id"], meta_b["id"]

    # Rule 1a: prefix match (very high confidence at lower threshold)
    if cos_sim >= 0.85 and (a.startswith(b) or b.startswith(a)):
        return True

    # Rule 1b: structural edit similarity
    if cos_sim >= 0.88:
        lo = min(len(a), len(b))
        hi = max(len(a), len(b))
        if hi > 0 and lo / hi >= 0.40 and edit_distance(a, b) / hi <= 0.35:
            return True

    return False


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1


def find_clusters(metas, vectors, threshold):
    """
    threshold is kept as a CLI arg for --dry-run exploration but the
    real merge logic is inside should_merge() (dual-rule: structural + semantic).
    """
    n = len(metas)
    print(f"  Computing {n}x{n} cosine similarity matrix...")
    sim = cosine_sim_matrix(vectors)

    print("  Building clusters via Union-Find (structural >= 0.88 | semantic >= 0.80)...")
    uf = UnionFind(n)
    n_pairs = 0

    # Only examine pairs above the lower bound to keep it fast
    rows, cols = np.where(sim >= 0.85)
    for i, j in zip(rows.tolist(), cols.tolist()):
        if i >= j:
            continue
        if should_merge(metas[i], metas[j], float(sim[i, j])):
            uf.union(i, j)
            n_pairs += 1

    print(f"  Found {n_pairs} mergeable pairs")

    groups = defaultdict(list)
    for i in range(n):
        groups[uf.find(i)].append(i)

    return {root: members for root, members in groups.items() if len(members) > 1}


# ---------------------------------------------------------------------------
# Canonical selection
# ---------------------------------------------------------------------------

def choose_canonical(metas, cluster):
    """
    Pick the canonical: shortest ID wins (most generic name).
    Tie-break: most file content (richer source stays).
    """
    def score(i):
        path = CONCEPTS_DIR / f"{metas[i]['id']}.md"
        size = path.stat().st_size if path.exists() else 0
        return (len(metas[i]["id"]), -size, metas[i]["id"])

    return min(cluster, key=score)


# ---------------------------------------------------------------------------
# Frontmatter manipulation (line-by-line, no YAML round-trip)
# ---------------------------------------------------------------------------

def parse_fm_lines(content):
    """
    Split content into (fm_end_lineno, lines).
    lines[0] == '---', lines[fm_end_lineno] == '---'.
    Returns (None, lines) when no frontmatter is found.
    """
    lines = content.split("\n")
    if not lines or lines[0].rstrip() != "---":
        return None, lines
    for i in range(1, len(lines)):
        if lines[i].rstrip() == "---":
            return i, lines
    return None, lines


def get_xllmwiki_aliases(lines, fm_end):
    """Return the list of existing aliases under x-llmwiki.aliases."""
    in_xllm = False
    in_aliases = False
    aliases = []
    for line in lines[1:fm_end]:
        stripped = line.strip()
        if stripped == "x-llmwiki:":
            in_xllm = True
        elif in_xllm and not line.startswith(" "):
            in_xllm = False
            in_aliases = False
        if in_xllm and stripped == "aliases:":
            in_aliases = True
        elif in_aliases and line.startswith("    - "):
            aliases.append(line[6:].rstrip())
        elif in_aliases and not line.startswith("    - "):
            in_aliases = False
    return aliases


def add_aliases_to_content(content, new_aliases):
    """
    Insert new_aliases into x-llmwiki.aliases in the first frontmatter block.
    Preserves all original formatting; only inserts new lines.
    """
    if not new_aliases:
        return content

    fm_end, lines = parse_fm_lines(content)
    if fm_end is None:
        return content

    existing = set(get_xllmwiki_aliases(lines, fm_end))
    to_add = [a for a in new_aliases if a not in existing]
    if not to_add:
        return content

    # Locate the insertion point: after the last alias item (or after "aliases:" header)
    in_xllm = False
    in_aliases = False
    last_alias_line = None
    aliases_header_line = None

    for i, line in enumerate(lines[1:fm_end], 1):
        stripped = line.strip()
        if stripped == "x-llmwiki:":
            in_xllm = True
        elif in_xllm and not line.startswith(" "):
            in_xllm = False
            in_aliases = False
        if in_xllm and stripped == "aliases:":
            in_aliases = True
            aliases_header_line = i
        elif in_aliases and line.startswith("    - "):
            last_alias_line = i
        elif in_aliases and not line.startswith("    - "):
            in_aliases = False

    new_alias_lines = [f"    - {a}" for a in to_add]

    if last_alias_line is not None:
        insert_after = last_alias_line
    elif aliases_header_line is not None:
        insert_after = aliases_header_line
    else:
        # No aliases section — add one right after x-llmwiki:
        for i, line in enumerate(lines[1:fm_end], 1):
            if line.strip() == "x-llmwiki:":
                header = ["  aliases:"] + new_alias_lines
                new_lines = lines[: i + 1] + header + lines[i + 1 :]
                return "\n".join(new_lines)
        return content  # x-llmwiki not found; leave untouched

    new_lines = lines[: insert_after + 1] + new_alias_lines + lines[insert_after + 1 :]
    return "\n".join(new_lines)


# ---------------------------------------------------------------------------
# Reference updating
# ---------------------------------------------------------------------------

def find_all_md_files():
    result = []
    for dirpath, dirnames, filenames in os.walk(OKF_DIR):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        for fname in filenames:
            if fname.endswith(".md"):
                result.append(Path(dirpath) / fname)
    return result


def batch_update_refs(all_md, replacements):
    """
    Apply ALL {old_id -> new_id} replacements in a single pass per file
    (instead of scanning every file for every replacement — much faster at scale).
    Returns set of modified file paths.
    """
    pattern_pairs = []
    for old_id, new_id in replacements.items():
        pattern_pairs.extend([
            (f"/concepts/{old_id}.md",  f"/concepts/{new_id}.md"),
            (f"/concepts/{old_id})",    f"/concepts/{new_id})"),
            (f"/concepts/{old_id}#",    f"/concepts/{new_id}#"),
            (f"concepts/{old_id}.md",   f"concepts/{new_id}.md"),
        ])

    modified = set()
    for md_file in all_md:
        try:
            with open(md_file, encoding="utf-8") as f:
                content = f.read()
        except (OSError, UnicodeDecodeError):
            continue

        new_content = content
        for old_pat, new_pat in pattern_pairs:
            if old_pat in new_content:
                new_content = new_content.replace(old_pat, new_pat)

        if new_content != content:
            with open(md_file, "w", encoding="utf-8") as f:
                f.write(new_content)
            modified.add(md_file)

    return modified


# ---------------------------------------------------------------------------
# Index update (removes stale entries for deleted concepts)
# ---------------------------------------------------------------------------

def update_index(metas, vectors, deleted_ids):
    deleted_set = set(deleted_ids)
    keep = [i for i, m in enumerate(metas) if m["id"] not in deleted_set]

    new_metas = [metas[i] for i in keep]
    new_vectors = vectors[np.array(keep)]

    print(f"  Index: {len(metas)} -> {len(new_metas)} entries")

    with open(META_PATH, "w", encoding="utf-8") as f:
        json.dump(new_metas, f, separators=(",", ":"))

    save_vectors(new_vectors, VECTORS_PATH)

    config = load_config()
    config["count"] = len(new_metas)
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)


# ---------------------------------------------------------------------------
# Git helpers
# ---------------------------------------------------------------------------

def git_add(paths):
    if paths:
        subprocess.run(
            ["git", "add", "--"] + [str(p) for p in paths],
            cwd=OKF_DIR, check=True, capture_output=True,
        )


def git_rm(paths):
    """Remove files from git index AND disk. Silently skip if not tracked."""
    for p in paths:
        if not p.exists():
            continue
        try:
            subprocess.run(
                ["git", "rm", "-f", str(p)],
                cwd=OKF_DIR, check=True, capture_output=True,
            )
        except subprocess.CalledProcessError:
            p.unlink(missing_ok=True)  # not tracked; just delete from disk


def git_commit(message):
    subprocess.run(["git", "commit", "-m", message], cwd=OKF_DIR, check=True)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Merge near-duplicate OKF concepts")
    parser.add_argument("--dry-run", action="store_true", help="Preview merges, no file changes")
    parser.add_argument("--threshold", type=float, default=0.97,
                        help="Cosine similarity threshold (default: 0.97)")
    parser.add_argument("--no-commit", action="store_true",
                        help="Apply changes and stage but do NOT commit")
    args = parser.parse_args()

    # --- Load index ---
    print("Loading meta.json …")
    metas = load_meta()
    n = len(metas)
    config = load_config()
    d = config["dim"]
    print(f"  {n} concepts, embedding dim={d}")

    print("Loading vectors.bin …")
    vectors = load_vectors(n, d)

    # --- Cluster ---
    print(f"Clustering (threshold={args.threshold}) …")
    clusters = find_clusters(metas, vectors, args.threshold)

    # --- Report ---
    label = "DRY RUN — " if args.dry_run else ""
    print(f"\n{label}Found {len(clusters)} merge group(s):\n")
    all_merges = []  # [(canonical_idx, [dup_idx, ...])]

    for root, members in sorted(clusters.items()):
        canonical_idx = choose_canonical(metas, members)
        dup_indices = [i for i in members if i != canonical_idx]
        canonical_id = metas[canonical_idx]["id"]
        dup_ids = [metas[i]["id"] for i in dup_indices]
        print(f"  KEEP  {canonical_id}")
        for did in dup_ids:
            print(f"  DROP  {did}")
        print()
        all_merges.append((canonical_idx, dup_indices))

    n_drops = sum(len(d) for _, d in all_merges)
    print(f"Total: {n_drops} files to delete across {len(all_merges)} group(s).")

    if args.dry_run:
        print("\nDry run complete — no changes made. Remove --dry-run to apply.")
        return

    if not all_merges:
        print("Nothing to merge.")
        return

    # --- Apply ---
    print("\nScanning all .md files …")
    all_md = find_all_md_files()
    print(f"  {len(all_md)} .md files found")

    modified: set = set()
    deleted_ids: list = []
    replacements: dict = {}   # {old_id: canonical_id}

    for canonical_idx, dup_indices in all_merges:
        canonical_id = metas[canonical_idx]["id"]
        canonical_path = CONCEPTS_DIR / f"{canonical_id}.md"

        if not canonical_path.exists():
            print(f"  WARN: canonical missing on disk: {canonical_path.name}")
            continue

        # Collect aliases to absorb from all duplicates
        new_aliases = []
        for dup_idx in dup_indices:
            dup_id = metas[dup_idx]["id"]
            new_aliases.append(dup_id)
            replacements[dup_id] = canonical_id

            dup_path = CONCEPTS_DIR / f"{dup_id}.md"
            if dup_path.exists():
                with open(dup_path, encoding="utf-8") as f:
                    dup_content = f.read()
                fm_end, lines = parse_fm_lines(dup_content)
                if fm_end is not None:
                    new_aliases.extend(get_xllmwiki_aliases(lines, fm_end))

        # Deduplicate aliases, skip canonical's own ID
        seen_aliases: set = set()
        unique_new = []
        for a in new_aliases:
            if a != canonical_id and a not in seen_aliases:
                seen_aliases.add(a)
                unique_new.append(a)

        # Patch canonical file with absorbed aliases
        with open(canonical_path, encoding="utf-8") as f:
            old = f.read()
        patched = add_aliases_to_content(old, unique_new)
        if patched != old:
            with open(canonical_path, "w", encoding="utf-8") as f:
                f.write(patched)
            modified.add(canonical_path)

        for dup_idx in dup_indices:
            deleted_ids.append(metas[dup_idx]["id"])

    # Single-pass reference update across all files
    print(f"  Updating cross-references ({len(replacements)} replacements)...")
    ref_modified = batch_update_refs(all_md, replacements)
    modified |= ref_modified

    # --- Update index (gitignored, not staged) ---
    print("Updating dbokf-index …")
    update_index(metas, vectors, deleted_ids)

    # --- Git ---
    to_delete = [CONCEPTS_DIR / f"{did}.md" for did in deleted_ids]
    print(f"\nStaging {len(modified)} modified + {len(to_delete)} deleted files …")
    git_add(list(modified))
    git_rm(to_delete)

    if args.no_commit:
        print("Staged. Run `git commit` manually.")
        return

    msg = (
        f"lint: merge {len(deleted_ids)} duplicate concepts into {len(all_merges)} canonical file(s)\n\n"
        f"Near-duplicate concept files merged (structural similarity cos>=0.85/0.88).\n"
        f"names structurally related). Absorbed aliases preserved in canonical\n"
        f"frontmatter. All cross-references updated. dbokf-index pruned.\n\n"
        f"Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
    )
    git_commit(msg)
    print("Done!")


if __name__ == "__main__":
    main()
