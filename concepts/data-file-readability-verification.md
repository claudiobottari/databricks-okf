---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 692df29c81287196b1fc9c46f9c4b98fabc3d4597a9cf75d1c24004cdd8b9db4
  pageDirectory: concepts
  sources:
    - fsck-repair-table-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-file-readability-verification
    - DFRV
  citations:
    - file: fsck-repair-table-databricks-on-aws.md
title: Data File Readability Verification
description: Direct read validation of data files to detect corruption or unreadable files in Delta Lake tables, performed by VERIFY ALL FILES mode.
tags:
  - delta-lake
  - data-integrity
  - file-validation
timestamp: "2026-06-19T18:56:13.294Z"
---

# Data File Readability Verification

**Data File Readability Verification** is a feature of the Delta Lake `FSCK REPAIR TABLE` command that checks whether the data files tracked in the table’s transaction log are physically readable and free of corruption. It is part of a broader set of metadata‑ and file‑level integrity checks that help administrators detect and diagnose storage‑level issues. ^[fsck-repair-table-databricks-on-aws.md]

## What the Verification Checks

When run with the `VERIFY ALL FILES` option, the command performs a full scan of every data file listed in the table’s metadata. The output includes columns that report specific problems: ^[fsck-repair-table-databricks-on-aws.md]

| Column | Description |
|--------|-------------|
| `fileUnreadable` | The data file exists but cannot be read (e.g., corrupt or truncated). |
| `fileCrcCorrupt` | The checkpoint file’s CRC checksum does not match, indicating corruption of the checkpoint itself. |
| `fileMetadataHasInvalidPartitionValues` | A partition column’s stored value violates the column’s nullability or type constraints. |
| `deletionVectorCorrupt` | A deletion vector file associated with a data file is corrupt and cannot be parsed. |
| `dataFileMissing` | A data file that the metadata expects is not present on storage. |
| `deletionVectorFileMissing` | A deletion vector file referenced by a data file is missing. |

These checks are performed only for the files that are relevant to the specific scan mode. For example, `fileCrcCorrupt` is only populated when a checkpoint file is examined, and `deletionVectorCorrupt` is only set when a deletion vector is present and is corrupted. ^[fsck-repair-table-databricks-on-aws.md]

## DRY RUN Mode

The `DRY RUN` clause can be added to `FSCK REPAIR TABLE` to report findings without making any changes. For instance, the command reports missing files or corrupt deletion vectors but does not repair them. This mode is useful for auditing table health before deciding on a fix. ^[fsck-repair-table-databricks-on-aws.md]

## Example Outputs

The following examples illustrate typical output rows from `VERIFY ALL FILES DRY RUN`. ^[fsck-repair-table-databricks-on-aws.md]

**Checkpoint CRC corruption**  
When `005.checkpoint.parquet` has a CRC checksum mismatch:

```
dataFilePath = null
dataFileMissing = false
deletionVectorPath = null
deletionVectorFileMissing = false
checkpointFilePath = "_delta_log/005.checkpoint.parquet"
fileCrcCorrupt = true
fileUnreadable = false
fileMetadataHasInvalidPartitionValues = false
deletionVectorCorrupt = false
```

**Missing data file and missing deletion vector**  
When `file1.parquet` is missing and its associated deletion vector `dv1.bin` is also missing:

```
dataFilePath = "file2.parquet"
dataFileMissing = true
deletionVectorPath = "dv1.bin"
deletionVectorFileMissing = true
checkpointFilePath = null
fileCrcCorrupt = false
fileUnreadable = false
fileMetadataHasInvalidPartitionValues = false
deletionVectorCorrupt = false
```

*Note*: The example output shows a row where `dataFilePath` is `"file2.parquet"`. The text explains the scenario: `file1.parquet` is missing along with its deletion vector. The row shown in the source corresponds to a second file `file2.parquet` that has a partition value violation.

**Invalid partition value**  
When `file2.parquet` has a partition value of `NULL` but the partition column is defined as `NOT NULL`:

```
dataFilePath = "file2.parquet"
dataFileMissing = false
deletionVectorPath = null
deletionVectorFileMissing = false
checkpointFilePath = null
fileCrcCorrupt = null
fileUnreadable = null
fileMetadataHasInvalidPartitionValues = true
deletionVectorCorrupt = false
```

**Unreadable data file and corrupt deletion vector**  
When `file1.parquet` is corrupt and unreadable, and `file2.parquet` has a corrupt deletion vector `dv2.bin`:

```
dataFilePath = "file1.parquet"
dataFileMissing = false
deletionVectorPath = null
deletionVectorFileMissing = false
checkpointFilePath = null
fileCrcCorrupt = false
fileUnreadable = true
fileMetadataHasInvalidPartitionValues = false
deletionVectorCorrupt = false

dataFilePath = "file2.parquet"
dataFileMissing = false
deletionVectorPath = "dv2.bin"
deletionVectorFileMissing = false
checkpointFilePath = null
fileCrcCorrupt = null
fileUnreadable = null
fileMetadataHasInvalidPartitionValues = false
deletionVectorCorrupt = true
```

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The storage layer that uses a transaction log and supports `FSCK REPAIR`.
- [FSCK REPAIR TABLE](/concepts/fsck-repair-table.md) – The command that performs readability and consistency checks.
- [Data File Corruption](/concepts/deletion-vector-corruption-detection.md) – General topic of file‑level bitrot, truncation, or CRC mismatch.
- [Deletion Vectors](/concepts/deletion-vectors.md) – Data structures that mark rows as deleted without rewriting files.
- Table Maintenance – Routine operations like compaction, vacuum, and file repair.

## Sources

- fsck-repair-table-databricks-on-aws.md

# Citations

1. [fsck-repair-table-databricks-on-aws.md](/references/fsck-repair-table-databricks-on-aws-0ce9a31c.md)
