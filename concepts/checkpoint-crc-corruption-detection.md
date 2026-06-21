---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: afe7775f20b702b819f708150f12b160bb2ddb1c70ffff6071d5921070feddcf
  pageDirectory: concepts
  sources:
    - fsck-repair-table-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - checkpoint-crc-corruption-detection
    - CCCD
  citations:
    - file: fsck-repair-table-databricks-on-aws.md
title: Checkpoint CRC Corruption Detection
description: Detection of CRC checksum corruption in Delta Lake checkpoint files, identified by the fileCrcCorrupt column in FSCK REPAIR TABLE output.
tags:
  - delta-lake
  - data-integrity
  - checkpoints
timestamp: "2026-06-19T18:55:58.385Z"
---

# Checkpoint CRC Corruption Detection

**Checkpoint CRC Corruption Detection** refers to the ability of Delta Lake's `FSCK REPAIR TABLE` command to identify checkpoints that have Cyclic Redundancy Check (CRC) checksum corruption. CRC corruption occurs when the integrity checksum of a checkpoint file does not match its actual contents, indicating data corruption in the Delta log. ^[fsck-repair-table-databricks-on-aws.md]

## Overview

When running `FSCK REPAIR TABLE` with the appropriate options, Delta Lake can detect checkpoint files where the CRC checksum is corrupt. The command reports this corruption through the `fileCrcCorrupt` column in its output, which is set to `true` for affected checkpoint files. ^[fsck-repair-table-databricks-on-aws.md]

## Detection Methods

The `FSCK REPAIR TABLE` command supports different modes for detecting CRC corruption in checkpoint files:

### METADATA ONLY Mode

The `METADATA ONLY DRY RUN` mode scans only the Delta transaction log metadata to identify corrupted checkpoint files. This mode is faster than full file verification but is limited to detecting issues in the metadata layer. ^[fsck-repair-table-databricks-on-aws.md]

Example command and output:
```sql
FSCK REPAIR TABLE t METADATA ONLY DRY RUN;
```

| checkpointFilePath | fileCrcCorrupt |
|--------------------|----------------|
| `_delta_log/005.checkpoint.parquet` | true |

### VERIFY ALL FILES Mode

The `VERIFY ALL FILES DRY RUN` mode performs a comprehensive scan that checks both metadata and actual data files. In addition to detecting CRC corruption in checkpoints, it can identify corrupt data files and deletion vectors. ^[fsck-repair-table-databricks-on-aws.md]

## Identified Corruption Types

When a CRC corruption is detected, the `fileCrcCorrupt` field is set to `true` for that checkpoint file. The following types of corruption can be detected:

- **CRC checksum corruption**: The checkpoint file's CRC checksum does not match its content, indicating data integrity issues. ^[fsck-repair-table-databricks-on-aws.md]
- **File unreadability**: The checkpoint file is corrupt and cannot be read (`fileUnreadable: true`). ^[fsck-repair-table-databricks-on-aws.md]
- **File metadata issues**: Invalid partition values in the file metadata. ^[fsck-repair-table-databricks-on-aws.md]
- **Deletion vector corruption**: Corruption in associated deletion vectors alongside checkpoint corruption. ^[fsck-repair-table-databricks-on-aws.md]

## Repairing CRC Corruption

When CRC corruption is detected in checkpoint files, you can run `FSCK REPAIR TABLE` without the `DRY RUN` option to attempt repairs. The repair process is table-specific and affects only the Delta table's transaction log. ^[fsck-repair-table-databricks-on-aws.md]

## Other Detected Issues

The `FSCK REPAIR TABLE` command can detect additional issues beyond CRC corruption, including:
- **Missing data files** (`dataFileMissing: true`): Data files referenced in the log that no longer exist. ^[fsck-repair-table-databricks-on-aws.md]
- **Missing deletion vectors** (`deletionVectorFileMissing: true`): Deletion vector files referenced in the log that are missing. ^[fsck-repair-table-databricks-on-aws.md]
- **Invalid partition values** (`fileMetadataHasInvalidPartitionValues: true`): Partition values that violate column constraints (e.g., a `NULL` value in a `NOT NULL` partition column). ^[fsck-repair-table-databricks-on-aws.md]

## Related Concepts

- [Delta Lake FSCK REPAIR TABLE](/concepts/fsck-repair-table.md) — The command used for detecting and repairing Delta table metadata issues.
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — The transaction log where checkpoint files reside.
- Delta Lake Checkpoint — Checkpoint files that aggregate transaction log entries.
- Data Integrity in Delta Lake — Broader topic of maintaining data integrity in Delta tables.
- [Deletion Vector corruption detection](/concepts/deletion-vector-corruption-detection.md) — Detection of corruption in deletion vector files.

## Sources

- fsck-repair-table-databricks-on-aws.md

# Citations

1. [fsck-repair-table-databricks-on-aws.md](/references/fsck-repair-table-databricks-on-aws-0ce9a31c.md)
