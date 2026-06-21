---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2705db76b7617e4d4a147cae5802ead9bc6e96505d4dd55c0143ea2d4c495985
  pageDirectory: concepts
  sources:
    - fsck-repair-table-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deletion-vector-integrity-checking
    - DVIC
    - Data Integrity Checks
  citations:
    - file: fsck-repair-table-databricks-on-aws.md
title: Deletion Vector Integrity Checking
description: Detection of missing or corrupted deletion vector files associated with data files in Delta Lake tables, surfaced by FSCK REPAIR TABLE commands.
tags:
  - delta-lake
  - data-integrity
  - deletion-vectors
timestamp: "2026-06-19T18:55:49.060Z"
---

# Deletion Vector Integrity Checking

**Deletion Vector Integrity Checking** is a diagnostic operation available through the `FSCK REPAIR TABLE` command on Delta Lake tables. It validates that deletion vectors referenced by data files exist and are readable, helping maintain the logical consistency of data files that have been modified via deletion vectors rather than full rewrites.

## Overview

Deletion vectors are files that track which rows within a data file have been logically deleted without rewriting the entire file. When a data file references a deletion vector, the system expects the corresponding deletion vector file to exist and be structurally valid. Deletion Vector Integrity Checking scans the table metadata to identify any referenced deletion vector files that are missing (non-existent) or corrupt (unreadable or containing invalid data). ^[fsck-repair-table-databricks-on-aws.md]

## Checks Performed

The integrity check inspects each data file's metadata and reports two conditions for each referenced deletion vector:

- **deletionVectorFileMissing** — The deletion vector file does not exist at the expected path in cloud storage. This can occur if the deletion vector was manually deleted, the data file was moved without its companion deletion vector, or a storage operation removed the file independently of the Delta transaction log. ^[fsck-repair-table-databricks-on-aws.md]
- **deletionVectorCorrupt** — The deletion vector file exists but its contents are unreadable, corrupt, or fail CRC checksum validation. This can happen due to partial writes, storage corruption, or software bugs that produce malformed deletion vector files. ^[fsck-repair-table-databricks-on-aws.md]

## FSCK REPAIR TABLE Modes

The `FSCK REPAIR TABLE` command supports several modes that affect which files are inspected:

- **METADATA ONLY** — Checks only metadata files in the `_delta_log` directory (checkpoint files and commit JSON files). When deletion vector checks are enabled, this mode also reports deletion vector files referenced from checkpoint files. If a checkpoint file has CRC corruption, the deletion vectors referenced within that checkpoint are considered suspect. ^[fsck-repair-table-databricks-on-aws.md]
- **DRY RUN** — (Default mode) Reports all issues without fixing them. Scans both metadata and data files, checking for missing or corrupt deletion vectors. ^[fsck-repair-table-databricks-on-aws.md]
- **VERIFY ALL FILES DRY RUN** — Performs a deep inspection that reads every data file in the table, attempting to open and parse each one. This mode can detect deletion vector corruption inside data files that was not evident from metadata alone. ^[fsck-repair-table-databricks-on-aws.md]

## Output Columns

The diagnostic output includes the following columns relevant to deletion vector integrity:

| Column | Description |
|--------|-------------|
| `dataFilePath` | Path to the data file that references a deletion vector. |
| `dataFileMissing` | Whether the data file itself is missing (may be true independently of deletion vector status). |
| `deletionVectorPath` | Path to the deletion vector file referenced by the data file. |
| `deletionVectorFileMissing` | Whether the deletion vector file does not exist. |
| `deletionVectorCorrupt` | Whether the deletion vector file exists but is corrupt or unreadable. |

^[fsck-repair-table-databricks-on-aws.md]

## Example Output

Given a table `t` where:
- `file1.parquet` references deletion vector `dv1.bin`, which is missing.
- `file2.parquet` references deletion vector `dv2.bin`, which exists but is corrupt.

Running:
```sql
FSCK REPAIR TABLE t VERIFY ALL FILES DRY RUN;
```

Produces:
```
dataFilePath  dataFileMissing deletionVectorPath deletionVectorFileMissing deletionVectorCorrupt
------------- --------------- ------------------ ------------------------- ---------------------
file1.parquet false           null               false                     false
file2.parquet false           dv2.bin            false                     true
```

Note that `file1.parquet` does not report `deletionVectorCorrupt = true` even though its deletion vector is missing; instead, the missing state is reported via the `dataFileMissing` column. The corruption column applies only when the file exists but is unreadable. ^[fsck-repair-table-databricks-on-aws.md]

## Related Concepts

- [Delta Lake FSCK REPAIR TABLE](/concepts/fsck-repair-table.md) — The full command syntax and available options.
- [Deletion Vectors](/concepts/deletion-vectors.md) — The mechanism for tracking logically deleted rows without rewriting data files.
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — The `_delta_log` directory where checkpoint and commit files reside.
- CRC Checksum Validation — The integrity check applied to checkpoint files to detect corruption.
- Table Maintenance on Delta Lake — Overview of routine maintenance operations including repair.

## Sources

- fsck-repair-table-databricks-on-aws.md

# Citations

1. [fsck-repair-table-databricks-on-aws.md](/references/fsck-repair-table-databricks-on-aws-0ce9a31c.md)
