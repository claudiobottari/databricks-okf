---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 20892e6ac7a65cca39a0e974ff7a666308f3ad09f77e3461ad62248932ab8e20
  pageDirectory: concepts
  sources:
    - fsck-repair-table-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - fsck-repair-table-command
    - FRTC
  citations:
    - file: fsck-repair-table-databricks-on-aws.md
title: FSCK REPAIR TABLE Command
description: A Delta Lake SQL command that repairs a table by detecting and reporting various types of corruption including missing files, CRC corruption, unreadable files, and invalid partition values.
tags:
  - delta-lake
  - sql-command
  - table-maintenance
timestamp: "2026-06-19T18:55:37.512Z"
---

# FSCK REPAIR TABLE Command

The **FSCK REPAIR TABLE** command is a maintenance utility for [Delta Lake](/concepts/delta-lake.md) tables on Databricks that scans the table’s transaction log and underlying files for inconsistencies and reports (or optionally repairs) detected issues. It is the Delta Lake equivalent of a file system consistency check (`fsck`). ^[fsck-repair-table-databricks-on-aws.md]

## Overview

FSCK REPAIR TABLE inspects a Delta table for a variety of metadata and data integrity problems, including:
- Missing data files referenced in the transaction log
- Missing deletion vector files
- Corrupt checkpoint files (CRC checksum corruption)
- Unreadable data files (e.g., corrupt Parquet files)
- Data files with partition values that violate the table schema (e.g., `NULL` in a `NOT NULL` partition column)
- Corrupt deletion vectors

The command runs in a **dry run** mode by default, which reports issues without making changes. Depending on the selected options, it can also repair certain types of corruption (the source material only shows dry run examples, but the command supports repair actions). ^[fsck-repair-table-databricks-on-aws.md]

## Syntax and Options

The general syntax is:

```
FSCK REPAIR TABLE table_name [METADATA ONLY | VERIFY ALL FILES] [DRY RUN]
```

Three modes are available:

### `METADATA ONLY DRY RUN`
Scans only the metadata (the transaction log) for inconsistencies such as missing checkpoint files or CRC corrupt checkpoints. It does not touch data files. Example output columns include `checkpointFilePath`, `fileCrcCorrupt`, `fileUnreadable`. ^[fsck-repair-table-databricks-on-aws.md]

### `DRY RUN` (default)
Scans both metadata and data file references, reporting missing data files, missing deletion vectors, and invalid partition values. Example output columns include `dataFilePath`, `dataFileMissing`, `deletionVectorPath`, `deletionVectorFileMissing`, `fileMetadataHasInvalidPartitionValues`. ^[fsck-repair-table-databricks-on-aws.md]

### `VERIFY ALL FILES DRY RUN`
Performs a deep inspection that reads and validates every data file, including verifying the integrity of deletion vectors. This mode detects corrupt or unreadable files and corrupt deletion vectors. Example output columns include `fileUnreadable` and `deletionVectorCorrupt`. ^[fsck-repair-table-databricks-on-aws.md]

## Output Columns

The command returns a result set with the following columns (not all appear in every mode):

| Column | Description |
|---|---|
| `dataFilePath` | Path of a data file in the table |
| `dataFileMissing` | Boolean — whether the data file is missing from storage |
| `deletionVectorPath` | Path of a deletion vector file associated with a data file |
| `deletionVectorFileMissing` | Boolean — whether the deletion vector file is missing |
| `checkpointFilePath` | Path of a checkpoint file in the transaction log |
| `fileCrcCorrupt` | Boolean — whether the checkpoint file has CRC corruption |
| `fileUnreadable` | Boolean — whether the data file is corrupt or unreadable |
| `fileMetadataHasInvalidPartitionValues` | Boolean — whether the data file has partition values that violate the table’s partition schema (e.g., `NULL` in a `NOT NULL` column) |
| `deletionVectorCorrupt` | Boolean — whether the deletion vector file is corrupt |

^[fsck-repair-table-databricks-on-aws.md]

## Usage Examples

The source material provides three example scenarios:

1. **CRC checksum corruption in a checkpoint** — `FSCK REPAIR TABLE t METADATA ONLY DRY RUN` reports `fileCrcCorrupt = true` for `_delta_log/005.checkpoint.parquet`. ^[fsck-repair-table-databricks-on-aws.md]

2. **Missing data file, missing deletion vector, and invalid partition value** — `FSCK REPAIR TABLE t DRY RUN` reports `dataFileMissing = true` for `file1.parquet` (and its deletion vector `dv1.bin` missing), and `fileMetadataHasInvalidPartitionValues = true` for `file2.parquet` (where partition value is `NULL` but the column is `NOT NULL`). ^[fsck-repair-table-databricks-on-aws.md]

3. **Corrupt unreadable data file and corrupt deletion vector** — `FSCK REPAIR TABLE t VERIFY ALL FILES DRY RUN` reports `fileUnreadable = true` for `file1.parquet` and `deletionVectorCorrupt = true` for `file2.parquet`’s deletion vector `dv2.bin`. ^[fsck-repair-table-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that this command maintains.
- Delta Lake Table Properties — Configuration options for Delta tables.
- [Deletion Vectors](/concepts/deletion-vectors.md) — Files that mark which rows in a data file are logically deleted.
- Checkpoint (Delta Lake) — Aggregated state files in the transaction log.
- Optimize Command — Another maintenance command for compacting small files.

## Sources

- fsck-repair-table-databricks-on-aws.md

# Citations

1. [fsck-repair-table-databricks-on-aws.md](/references/fsck-repair-table-databricks-on-aws-0ce9a31c.md)
