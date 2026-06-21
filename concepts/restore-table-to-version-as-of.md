---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5dba325634a2d019fd4adb223b8aba59f959f6fe6167eb70e4387f5d3fdc3ade
  pageDirectory: concepts
  sources:
    - restore-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - restore-table-to-version-as-of
    - RTTVAO
  citations:
    - file: restore-databricks-on-aws.md
title: RESTORE TABLE TO VERSION AS OF
description: Restoring a Delta table to a specific version number obtained from DESCRIBE HISTORY
tags:
  - delta-lake
  - versioning
  - restore
timestamp: "2026-06-19T20:14:20.689Z"
---

# RESTORE TABLE TO VERSION AS OF

**RESTORE TABLE TO VERSION AS OF** is a Delta Lake SQL command that restores a Delta table to a specific historical version, identified by its version number. This command enables users to roll back a table to a previous state, undoing changes that occurred after the specified version.

## Syntax

```sql
RESTORE TABLE table_name TO VERSION AS OF version_number;
```

^[restore-databricks-on-aws.md]

## Description

The `RESTORE TABLE TO VERSION AS OF` command restores a Delta table to the state it was in at a specific version number. The version number can be obtained from the output of `DESCRIBE HISTORY table_name`, which lists all the versions of the table along with their associated metadata. ^[restore-databricks-on-aws.md]

This command is part of the [Delta Lake](/concepts/delta-lake.md) time travel capabilities, which allow users to access and restore previous versions of a table. Unlike `RESTORE TABLE TO TIMESTAMP AS OF`, which restores based on a timestamp, this variant uses the explicit version number from the table's history. ^[restore-databricks-on-aws.md]

## Output

The command returns a result set with the following columns:

| Column | Description |
|--------|-------------|
| `table_size_after_restore` | Size of the table after the restore operation |
| `num_of_files_after_restore` | Number of data files after the restore |
| `num_removed_files` | Number of files removed during the restore |
| `num_restored_files` | Number of files restored (added back) |
| `removed_files_size` | Size of the removed files |
| `restored_files_size` | Size of the restored files |

^[restore-databricks-on-aws.md]

## Example

The following example demonstrates restoring the `employee` table to version 1:

```sql
> RESTORE TABLE employee TO VERSION AS OF 1;

table_size_after_restore  num_of_files_after_restore  num_removed_files  num_restored_files  removed_files_size  restored_files_size
100                       3                           1                  0                   574                 0
```

In this example, the restore operation removes one file (574 bytes) and results in a table with 3 files totaling 100 bytes. No files needed to be restored because the target state was achieved by removing newer files. ^[restore-databricks-on-aws.md]

## Related Commands

- [RESTORE TABLE TO TIMESTAMP AS OF](/concepts/restore-table-to-timestamp-as-of.md) — Restores a table to a specific point in time rather than a version number
- [DESCRIBE HISTORY](/concepts/describe-history.md) — Lists the version history of a Delta table, used to find version numbers for restoration
- [TIME TRAVEL](/concepts/delta-lake-time-travel.md) — The broader Delta Lake feature for accessing historical versions of a table

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that provides ACID transactions and time travel capabilities
- [Table Versioning](/concepts/delta-table-versioning.md) — How Delta Lake tracks changes to tables through sequential versions
- Data Recovery — Using restore operations to recover from accidental data modifications or deletions

## Sources

- restore-databricks-on-aws.md

# Citations

1. [restore-databricks-on-aws.md](/references/restore-databricks-on-aws-b92cad28.md)
