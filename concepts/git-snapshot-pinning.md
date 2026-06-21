---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a2d62d62530cf590480c4e2c53268afa41e3a0b95a982ac88d817b6a367571f0
  pageDirectory: concepts
  sources:
    - workload-yaml-reference-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - git-snapshot-pinning
    - GSP
  citations:
    - file: workload-yaml-reference-databricks-on-aws.md
title: Git Snapshot Pinning
description: Pin code versions in training jobs by git branch or commit SHA using the `git:` block inside `code_source`, with optional remote HEAD fetching via `git.remote`.
tags:
  - git
  - versioning
  - reproducibility
timestamp: "2026-06-19T23:27:06.204Z"
---

# Git Snapshot Pinning

**Git Snapshot Pinning** refers to the practice of fixing the version of training code to a specific git branch or commit SHA when submitting a workload with the [AI Runtime CLI](/concepts/ai-runtime-cli.md). This ensures exact reproducibility by making the remote execution environment use a known revision of the code rather than the current working tree. ^[workload-yaml-reference-databricks-on-aws.md]

## Overview

In the [AI Runtime CLI](/concepts/ai-runtime-cli.md) (`air run`), the `code_source` block defines how local training code is packaged and made available on the compute node. When the `type` is set to `snapshot`, the CLI can either package the working tree as-is (including uncommitted changes) or, if a `git:` block is provided, pin the snapshot to a specific git revision. Pinning enables version-aware caching and uses `git archive` to create the tarball, reducing upload time and guaranteeing the same code is used across runs. ^[workload-yaml-reference-databricks-on-aws.md]

## Configuration

Pinning is configured inside the `snapshot` sub-block under `code_source`. The `git:` block accepts two mutually exclusive fields: `branch` or `commit`. A third optional field, `remote`, can be used with `branch` to fetch the remote HEAD instead of the local one.

### Pin by Branch

Using `git.branch` pins the snapshot to the local HEAD of the specified branch. The CLI does not perform a remote fetch; it uses the local checked-out state of that branch.

```yaml
code_source:
  type: snapshot
  snapshot:
    root_path: /home/username/repo
    git:
      branch: main
command: train.sh
```

^[workload-yaml-reference-databricks-on-aws.md]

### Pin by Commit

Using `git.commit` pins the snapshot to a specific commit SHA, providing exact reproducibility regardless of the current branch.

```yaml
code_source:
  type: snapshot
  snapshot:
    root_path: /home/username/repo
    git:
      commit: abc1234567
command: train.sh
```

^[workload-yaml-reference-databricks-on-aws.md]

### Use a Remote HEAD

The optional `git.remote` field is valid only when `git.branch` is set. Setting it to `true` automatically fetches the remote tracking branch’s HEAD from the default remote. Alternatively, you can specify a remote name (e.g., `upstream`) to fetch from that particular remote. This is useful for collaborating across forks or ensuring the latest remote version is used.

```yaml
code_source:
  type: snapshot
  snapshot:
    root_path: /home/username/repo
    git:
      branch: main
      remote: true
command: train.sh
```

```yaml
code_source:
  type: snapshot
  snapshot:
    root_path: /home/username/repo
    git:
      branch: feature-x
      remote: upstream
command: train.sh
```

^[workload-yaml-reference-databricks-on-aws.md]

## Behavior Without a `git:` Block

If the `git:` block is omitted entirely (and `root_path` is not required to be a git repository), the CLI packages the working tree as a plain tarball, including any uncommitted changes. No version caching is applied, meaning a fresh tarball is uploaded for every run. This method is simpler but does not guarantee reproducibility across runs because the working directory may change. ^[workload-yaml-reference-databricks-on-aws.md]

## Best Practices

- **Always pin by commit SHA** for production or long-running experiments to ensure that the same code version is used even if the branch moves forward.
- **Use `git.branch` with `remote: true`** when you want to use the latest upstream version from a shared repository without manually updating your local clone.
- **Set `root_path`** to the root of your git repository. The `git:` block requires `root_path` to be a git repository.
- **Avoid mixing `branch` and `commit`** – they are mutually exclusive. Specify exactly one within the `git:` block. ^[workload-yaml-reference-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – The command-line tool that consumes workload YAML configurations.
- [Workload YAML Reference](/concepts/workload-yaml-configuration.md) – Full reference for all configuration fields.
- Code Snapshot Type – The `snapshot` `type` in `code_source`.
- Dependency Pinning – Pinning Python package versions for reproducibility.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – The typical context in which Git snapshot pinning is used.

## Sources

- workload-yaml-reference-databricks-on-aws.md

# Citations

1. [workload-yaml-reference-databricks-on-aws.md](/references/workload-yaml-reference-databricks-on-aws-d459ba00.md)
