---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4f5663a482ec6a6d1e61f840ab5a6e69188aa78dec49e8e323bf2f8086339119
  pageDirectory: concepts
  sources:
    - restore-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - restore-table-command
    - RTC
    - RESTORE Command
    - RESTORE Table
  citations:
    - file: restore-databricks-on-aws.md
title: RESTORE TABLE Command
description: Delta Lake SQL command to restore a table to a previous state using timestamp or version
tags:
  - delta-lake
  - sql-command
  - data-management
timestamp: "2026-06-19T20:14:17.938Z"
---

# RESTORE TABLE Command

The **RESTORE TABLE Command** is a Delta Lake SQL statement that rolls back a Delta table to a previous state, specified either by a timestamp or by a version number. This command allows users to recover from accidental modifications, data corruption, or to inspect and revert to a known good state of the table. ^[restore-databricks-on-aws.md]

## Syntax

```sql
RESTORE TABLE table_name TO TIMESTAMP AS OF timestamp_expression;

RESTORE TABLE table_name TO VERSION AS OF version_number;
```

Each form instructs Delta Lake to restore the table to the state it was in at the given timestamp or version. ^[restore-databricks-on-aws.md]

## Parameters

- **`table_name`**: The name of the Delta table to restore. This can be a fully qualified table name (e.g., `catalog.schema.table`).
- **`timestamp_expression`**: A timestamp string (e.g., `'2022-08-02 00:00:00'`) or a timestamp function like `current_timestamp() - INTERVAL '1' HOUR`.
- **`version_number`**: An integer version number retrieved from the table history, typically obtained using `DESCRIBE HISTORY employee`. ^[restore-databricks-on-aws.md]

## Output

The RESTORE TABLE command returns a result set with the following columns:

| Column | Description |
|--------|-------------|
| `table_size_after_restore` | Size of the table in bytes after the restore |
| `num_of_files_after_restore` | Number of files in the table after the restore |
| `num_removed_files` | Number of files removed during the restore |
| `num_restored_files` | Number of files brought back from history |
| `removed_files_size` | Total size in bytes of files removed |
| `restored_files_size` | Total size in bytes of files restored |

^[restore-databricks-on-aws.md]

## Examples

### Restore to a Specific Timestamp

```sql
RESTORE TABLE employee TO TIMESTAMP AS OF '2022-08-02 00:00:00';
```

This restores the `employee` table to its state as of midnight on August 2, 2022. ^[restore-databricks-on-aws.md]

### Restore to a Specific Version

```sql
RESTORE TABLE employee TO VERSION AS OF 1;
```

This restores the `employee` table to version 1, as listed by the `DESCRIBE HISTORY` command. ^[restore-databricks-on-aws.md]

### Restore to a Relative Time

```sql
RESTORE TABLE employee TO TIMESTAMP AS OF current_timestamp() - INTERVAL '1' HOUR;
```

This restores the `employee` table to the state it was in one hour ago. ^[restore-databricks-on-aws.md]

## Important Considerations

- The RESTORE command requires that the target state still exists in the Delta table's transaction log and data files. If files have been VACUUMed (permanently deleted) or if the transaction log has been truncated, the restore may fail or produce incomplete results.
- Restoring a table creates a new version in the table's history. The original state that was overwritten by the restore is still accessible via version history (as long as the underlying data files have not been vacuumed).
- The command uses `DESCRIBE HISTORY` to enumerate available versions and timestamps for reference. ^[restore-databricks-on-aws.md]

## Related Concepts

- [DESCRIBE HISTORY](/concepts/describe-history.md) – Command to view the version history of a Delta table, including timestamps and operations.
- VACUUM – Command that permanently removes old data files, which can affect the ability to restore.
- [Delta Lake](/concepts/delta-lake.md) – The underlying storage layer that enables time travel and restore operations.
- [Time Travel](/concepts/delta-lake-time-travel.md) – The general capability in Delta Lake to query and restore data from previous versions.

## Sources

- restore-databricks-on-aws.md

# Citations

1. [restore-databricks-on-aws.md](/references/restore-databricks-on-aws-b92cad28.md)
