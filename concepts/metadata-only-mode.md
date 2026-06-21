---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 731d6e078bf52ff1b87e2fa3ca343244343e55e9998dc6268dcebe0d1447416a
  pageDirectory: concepts
  sources:
    - fsck-repair-table-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metadata-only-mode
    - MOM
  citations:
    - file: fsck-repair-table-databricks-on-aws.md
title: METADATA ONLY mode
description: FSCK REPAIR TABLE mode that only checks metadata integrity without verifying actual data file contents
tags:
  - delta-lake
  - databricks
  - metadata
  - optimization
timestamp: "2026-06-19T10:40:10.117Z"
---

# METADATA ONLY mode

**METADATA ONLY mode** is a run mode for the [FSCK REPAIR TABLE](/concepts/fsck-repair-table.md) command in [Delta Lake](/concepts/delta-lake.md) that restricts integrity checks to the table’s metadata rather than scanning all data files. It is useful for quickly identifying metadata-specific corruption without the cost of a full file scan. ^[fsck-repair-table-databricks-on-aws.md]

## Purpose

When you specify `METADATA ONLY` in an `FSCK REPAIR TABLE` statement, the command restricts its verification to metadata integrity—primarily the CRC (cyclic redundancy check) correctness of checkpoint files in the `_delta_log` directory. Data file integrity, deletion vector status, and partition value validity are not checked. ^[fsck-repair-table-databricks-on-aws.md]

## Usage

The mode is typically combined with `DRY RUN` to report issues without performing any repairs. The syntax is:

```sql
FSCK REPAIR TABLE <table-name> METADATA ONLY DRY RUN;
```

## What It Reports

In `METADATA ONLY DRY RUN`, the command outputs a row for each checkpoint file that has a CRC checksum corruption. The output columns related to metadata are:

| Column | Meaning |
|--------|---------|
| `checkpointFilePath` | Path to the checkpoint file |
| `fileCrcCorrupt` | `true` if the CRC checksum is corrupted |

Other columns (`dataFilePath`, `dataFileMissing`, `deletionVectorPath`, etc.) are set to `null` or `false` because the command does not inspect data files or deletion vectors. ^[fsck-repair-table-databricks-on-aws.md]

### Example

Assuming a checkpoint file `005.checkpoint.parquet` has a CRC checksum corruption:

```sql
FSCK REPAIR TABLE t METADATA ONLY DRY RUN;
```

Output:

```
dataFilePath  dataFileMissing  deletionVectorPath  deletionVectorFileMissing  checkpointFilePath              fileCrcCorrupt  fileUnreadable  fileMetadataHasInvalidPartitionValues  deletionVectorCorrupt
------------  ---------------  ------------------  -------------------------  ------------------------------  --------------  --------------  -------------------------------------  ---------------------
null          false            null                false                      _delta_log/005.checkpoint.parquet true            false           false                                   false
```

^[fsck-repair-table-databricks-on-aws.md]

## Comparison with Other Modes

- **Default `DRY RUN` (without `METADATA ONLY`)**: Checks data file existence, deletion vectors, and partition value validity, in addition to metadata. ^[fsck-repair-table-databricks-on-aws.md]
- **`VERIFY ALL FILES DRY RUN`**: Also checks every data file for readability and deletion vector corruption, which is the most thorough (and slowest) mode. ^[fsck-repair-table-databricks-on-aws.md]

`METADATA ONLY` is the lightest-weight mode, suitable for quick health checks of the transactional log.

## Related Concepts

- [FSCK REPAIR TABLE](/concepts/fsck-repair-table.md) – The full command and its options.
- [Delta Lake](/concepts/delta-lake.md) – The underlying storage format.
- Checkpoint files – The condensed log files whose CRC is validated.
- [DRY RUN](/concepts/dry-run-mode.md) – The preview mode used with `METADATA ONLY`.

## Sources

- fsck-repair-table-databricks-on-aws.md

# Citations

1. [fsck-repair-table-databricks-on-aws.md](/references/fsck-repair-table-databricks-on-aws-0ce9a31c.md)
