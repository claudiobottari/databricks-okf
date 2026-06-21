---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6ae5f582c3af16bb353f1732516bfdb6b7efa4ebf044287be7d685652822678e
  pageDirectory: concepts
  sources:
    - fsck-repair-table-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - verify-all-files-verification
    - VAFV
  citations:
    - file: fsck-repair-table-databricks-on-aws.md
title: VERIFY ALL FILES verification
description: A comprehensive verification mode for FSCK REPAIR TABLE that checks both metadata and actual data file contents, including data file readability and deletion vector integrity.
tags:
  - delta-lake
  - verification
  - data-integrity
timestamp: "2026-06-18T12:26:40.895Z"
---

# VERIFY ALL FILES Verification

**VERIFY ALL FILES verification** is an advanced mode of the `FSCK REPAIR TABLE` command in [Delta Lake](/concepts/delta-lake.md) on Databricks that performs a deep integrity scan of every data file in a Delta table. It detects a broader set of file-level corruptions than the default `FSCK REPAIR TABLE` operation, which only checks for missing files referenced in the transaction log. ^[fsck-repair-table-databricks-on-aws.md]

## What It Checks

When run with the `VERIFY ALL FILES` option, the command inspects each data file and its associated [deletion vector](/concepts/deletion-vectors.md) (if present) for the following types of corruption: ^[fsck-repair-table-databricks-on-aws.md]

| Column in output | Corruption detected |
|------------------|---------------------|
| `dataFileMissing` | The data file does not exist on disk |
| `fileCrcCorrupt` | The CRC checksum of the data file does not match its recorded value |
| `fileUnreadable` | The data file exists but cannot be read (e.g., format corruption) |
| `fileMetadataHasInvalidPartitionValues` | The file's partition values violate the table's partition column constraints (e.g., `NULL` in a `NOT NULL` column) |
| `deletionVectorFileMissing` | The deletion vector file referenced by the data file is missing |
| `deletionVectorCorrupt` | The deletion vector file exists but its contents are corrupt |

The command outputs a row for each file that exhibits at least one of these issues. If no issues are found, the command returns an empty result set. ^[fsck-repair-table-databricks-on-aws.md]

## Dry Run Mode

Adding `DRY RUN` to the `FSCK REPAIR TABLE ... VERIFY ALL FILES` command reports all detected problems without performing any repair. This is useful for previewing the scope of corruption before deciding whether to fix it. ^[fsck-repair-table-databricks-on-aws.md]

**Example:**
```sql
FSCK REPAIR TABLE t VERIFY ALL FILES DRY RUN;
```

Output:

| dataFilePath  | dataFileMissing | deletionVectorPath | deletionVectorFileMissing | checkpointFilePath | fileCrcCorrupt | fileUnreadable | fileMetadataHasInvalidPartitionValues | deletionVectorCorrupt |
|---------------|-----------------|--------------------|---------------------------|--------------------|----------------|----------------|---------------------------------------|-----------------------|
| file1.parquet | false           | null               | false                     | null               | false          | true           | false                                 | false                 |
| file2.parquet | false           | dv2.bin            | false                     | null               | null           | null           | false                                 | true                  |

In this example, `file1.parquet` is unreadable and `file2.parquet` has a corrupt deletion vector `dv2.bin`. ^[fsck-repair-table-databricks-on-aws.md]

## Comparison with Other FSCK Modes

- **`FSCK REPAIR TABLE`** (no modifier): Checks only for missing data files and deletion vectors by comparing the transaction log against the file system. ^[fsck-repair-table-databricks-on-aws.md]
- **`FSCK REPAIR TABLE METADATA ONLY`**: Checks metadata files (checkpoints) for CRC corruption and missing files. ^[fsck-repair-table-databricks-on-aws.md]
- **`FSCK REPAIR TABLE VERIFY ALL FILES`**: Performs the most thorough check, including reading the full content of every data file and deletion vector to detect unreadable data, CRC mismatches, invalid partition values, and deletion vector corruption. ^[fsck-repair-table-databricks-on-aws.md]

## Use Cases

- **Data integrity validation** after a storage outage or replication failure.
- **Pre‑upgrade health check** before updating to a new Delta Lake version.
- **Troubleshooting** query failures caused by corrupt or missing files.

## Related Concepts

- [Delta Lake FSCK REPAIR TABLE](/concepts/fsck-repair-table.md) — The full command syntax and repair options
- [Deletion Vectors](/concepts/deletion-vectors.md) — Metadata files that track logically deleted rows
- Checkpoint Files — Aggregated state snapshots used for fast recovery
- Table Maintenance on Databricks — Best practices for keeping Delta tables healthy

## Sources

- fsck-repair-table-databricks-on-aws.md

# Citations

1. [fsck-repair-table-databricks-on-aws.md](/references/fsck-repair-table-databricks-on-aws-0ce9a31c.md)
