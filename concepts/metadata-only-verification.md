---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c2b9d771e1a3ad1e722bce891bc6a1c60d5edf2038212858f51c0e58638b5c4d
  pageDirectory: concepts
  sources:
    - fsck-repair-table-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metadata-only-verification
    - MOV
  citations:
    - file: fsck-repair-table-databricks-on-aws.md
title: METADATA ONLY verification
description: A verification mode for FSCK REPAIR TABLE that checks only the Delta transaction log metadata (checkpoint CRCs, file listings) without examining actual data file contents.
tags:
  - delta-lake
  - verification
  - performance
timestamp: "2026-06-18T12:26:36.922Z"
---

# METADATA ONLY Verification

**METADATA ONLY verification** is a mode of the `FSCK REPAIR TABLE` command that performs a lightweight check of a Delta table's metadata without reading the actual data files. It is used to detect file metadata issues such as corruption in checkpoint files, CRC checksum corruption, or invalid partition values.

## Overview

When you run `FSCK REPAIR TABLE` with the `METADATA ONLY` option, the command only verifies the file metadata recorded in the Delta transaction log, rather than scanning the actual data files on disk. This makes it faster than a full verification, as it avoids reading the data content of each file. ^[fsck-repair-table-databricks-on-aws.md]

## Capabilities

METADATA ONLY verification can detect the following types of issues:

- **Checkpoint file CRC corruption** — If a checkpoint `.parquet` file has CRC checksum corruption, the command reports it under `fileCrcCorrupt`.
- **File metadata with invalid partition values** — When a file's metadata contains partition values that violate the table's partition schema (e.g., a `NOT NULL` partition column has a `null` value), the command reports it under `fileMetadataHasInvalidPartitionValues`.
- **File unreadable** — If a data file is corrupt and cannot be read, the command reports it under `fileUnreadable`.

## Comparison with Full Verification

| Check Type | METADATA ONLY | Full Verification (VERIFY ALL FILES) |
|------------|----------------|----------------------------------------|
| Checks file metadata only | Yes | Yes |
| Reads data file content | No | Yes |
| Detects missing data files | No | Yes |
| Detects missing deletion vectors | No | Yes |
| Detects deletion vector file corruption | No | Yes |
| Detects data file corruption | Partial (only if file metadata is also corrupt) | Yes |

## Syntax

```sql
FSCK REPAIR TABLE table_name METADATA ONLY DRY RUN;
```

The `DRY RUN` option is required with `METADATA ONLY` to report issues without repairing them.

## Output Columns

When run with `METADATA ONLY`, the command reports the following columns:

| Column | Description |
|--------|-------------|
| `dataFilePath` | Path to the data file |
| `dataFileMissing` | Whether the data file is missing |
| `deletionVectorPath` | Path to the deletion vector |
| `deletionVectorFileMissing` | Whether the deletion vector is missing |
| `checkpointFilePath` | Path to the checkpoint file |
| `fileCrcCorrupt` | Whether the file's CRC is corrupt |
| `fileUnreadable` | Whether the file is unreadable |
| `fileMetadataHasInvalidPartitionValues` | Whether the file metadata has invalid partition values |
| `deletionVectorCorrupt` | Whether the deletion vector is corrupt |

## Examples

### Detecting checkpoint CRC corruption

```sql
FSCK REPAIR TABLE t METADATA ONLY DRY RUN;
```

**Result**: Reports `fileCrcCorrupt: true` for `_delta_log/005.checkpoint.parquet` when CRC checksum corruption is detected.

### Detecting invalid partition values

```sql
FSCK REPAIR TABLE t METADATA ONLY DRY RUN;
```

**Result**: Reports `fileMetadataHasInvalidPartitionValues: true` for `file2.parquet` when a partition column with `NOT NULL` constraint contains a `null` value.

### Detecting unreadable files

```sql
FSCK REPAIR TABLE t METADATA ONLY DRY RUN;
```

**Result**: Reports `fileUnreadable: true` for `file1.parquet` when the file is corrupt and cannot be read.

## Use Cases

METADATA ONLY verification is useful for:
- **Fast health checks** of Delta table metadata without reading data files
- **Validating table schema** and partition value constraints
- **Checking checkpoint file integrity** for CRC corruption
- **Pre-deployment validation** before committing to a full repair

## Related Concepts

- [FSCK REPAIR TABLE](/concepts/fsck-repair-table.md) — The full command for verifying and repairing Delta tables
- FSCK REPAIR TABLE DRY RUN — Dry run mode for reporting issues without repair
- [Delta Lake](/concepts/delta-lake.md) — The storage layer for Delta tables
- [Transaction Log](/concepts/delta-transaction-log.md) — The metadata that tracks table changes in Delta
- Checkpoint File — A snapshot of the transaction log state
- [Deletion Vector](/concepts/deletion-vectors.md) — A data structure for tracking soft-deleted rows
- CRC Checksum — Used to validate file integrity

## Sources

- fsck-repair-table-databricks-on-aws.md

# Citations

1. [fsck-repair-table-databricks-on-aws.md](/references/fsck-repair-table-databricks-on-aws-0ce9a31c.md)
