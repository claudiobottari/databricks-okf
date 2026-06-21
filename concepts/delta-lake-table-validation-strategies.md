---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cbc63dca719e52d52ea74689f643138fb92ba4d92a5636a0614a25e3be03911e
  pageDirectory: concepts
  sources:
    - fsck-repair-table-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-table-validation-strategies
    - DLTVS
  citations:
    - file: fsck-repair-table-databricks-on-aws.md
title: Delta Lake Table Validation Strategies
description: "Three modes of table validation: METADATA ONLY (lightweight CRC check), DRY RUN (file existence checks), and VERIFY ALL FILES (deep data validation including file readability and deletion vector integrity)."
tags:
  - delta-lake
  - validation
  - table-maintenance
timestamp: "2026-06-19T18:55:35.970Z"
---

# [Delta Lake Table](/concepts/delta-lake-table.md) Validation Strategies

**Delta Lake Table Validation Strategies** refer to the set of commands and approaches used to detect and repair inconsistencies in [Delta Lake](/concepts/delta-lake.md) tables. These strategies help maintain data integrity by identifying missing data files, corrupt files, invalid partition values, and corrupted [Deletion Vectors](/concepts/deletion-vectors.md) or Checkpoint files.

## Overview

Delta Lake tables can develop inconsistencies over time due to file system issues, incomplete operations, or storage failures. The `FSCK REPAIR TABLE` command provides a mechanism to validate table metadata against the actual state of the underlying storage and repair detected issues. ^[fsck-repair-table-databricks-on-aws.md]

## Validation Modes

### DRY RUN

The `DRY RUN` mode reports detected issues without making any changes to the table. This is useful for auditing table health before performing repairs. The command returns a detailed report of all inconsistencies found. ^[fsck-repair-table-databricks-on-aws.md]

### METADATA ONLY

The `METADATA ONLY` option limits validation to checkpoint files only, checking for CRC checksum corruption. This is a faster validation that does not scan data files or deletion vectors. ^[fsck-repair-table-databricks-on-aws.md]

### VERIFY ALL FILES

The `VERIFY ALL FILES` option performs a comprehensive validation that checks:
- Data file existence and readability
- Deletion vector file existence and integrity
- Partition value validity
- Checkpoint file CRC integrity

^[fsck-repair-table-databricks-on-aws.md]

## Detected Issues

The validation report includes the following columns that indicate specific types of issues:

| Column | Description |
|--------|-------------|
| `dataFileMissing` | The referenced data file does not exist in storage |
| `fileCrcCorrupt` | The checkpoint file has CRC checksum corruption |
| `fileUnreadable` | The data file exists but cannot be read |
| `fileMetadataHasInvalidPartitionValues` | The file's partition values violate the table schema (e.g., NULL in a NOT NULL partition column) |
| `deletionVectorFileMissing` | The deletion vector file referenced by a data file is missing |
| `deletionVectorCorrupt` | The deletion vector file exists but is corrupted |

^[fsck-repair-table-databricks-on-aws.md]

## Example Scenarios

### Checkpoint CRC Corruption

When a checkpoint file has CRC checksum corruption, the `METADATA ONLY DRY RUN` mode detects it:

```sql
FSCK REPAIR TABLE t METADATA ONLY DRY RUN;
```

This reports `fileCrcCorrupt = true` for the affected checkpoint file. ^[fsck-repair-table-databricks-on-aws.md]

### Missing Data and Deletion Vector Files

When a data file and its associated deletion vector are both missing, the `DRY RUN` mode reports both issues:

```sql
FSCK REPAIR TABLE t DRY RUN;
```

This shows `dataFileMissing = true` and `deletionVectorFileMissing = true` for the affected file. ^[fsck-repair-table-databricks-on-aws.md]

### Invalid Partition Values

When a data file has a NULL partition value in a column defined as NOT NULL, the `DRY RUN` mode detects it:

```sql
FSCK REPAIR TABLE t DRY RUN;
```

This reports `fileMetadataHasInvalidPartitionValues = true` for the affected file. ^[fsck-repair-table-databricks-on-aws.md]

### Unreadable Files and Corrupt Deletion Vectors

When a data file is corrupt and unreadable, or a deletion vector is corrupted, the `VERIFY ALL FILES DRY RUN` mode detects both issues:

```sql
FSCK REPAIR TABLE t VERIFY ALL FILES DRY RUN;
```

This reports `fileUnreadable = true` for corrupt data files and `deletionVectorCorrupt = true` for corrupted deletion vectors. ^[fsck-repair-table-databricks-on-aws.md]

## Best Practices

1. **Run DRY RUN first**: Always validate with `DRY RUN` before performing actual repairs to understand the scope of issues.
2. **Use METADATA ONLY for quick checks**: When only checkpoint integrity is a concern, use `METADATA ONLY` for faster validation.
3. **Use VERIFY ALL FILES for comprehensive checks**: When data integrity is critical, use `VERIFY ALL FILES` to catch all possible issues.
4. **Schedule regular validation**: Incorporate table validation into routine maintenance workflows to catch issues early.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that provides ACID transactions and scalable metadata handling
- [Deletion Vectors](/concepts/deletion-vectors.md) — Files that mark rows as deleted without rewriting data files
- Checkpoint — Snapshot files that compact the transaction log for faster reads
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — The ordered record of every change made to a Delta table
- Table Maintenance — Regular operations to keep Delta tables healthy and performant

## Sources

- fsck-repair-table-databricks-on-aws.md

# Citations

1. [fsck-repair-table-databricks-on-aws.md](/references/fsck-repair-table-databricks-on-aws-0ce9a31c.md)
