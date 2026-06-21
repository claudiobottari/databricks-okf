---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 026ce6537ce0f8e9c143754ef2ab3d1f332e619ec813c4b8911211e6bd79fa1a
  pageDirectory: concepts
  sources:
    - restore-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - restore-table-to-timestamp-as-of
    - RTTTAO
  citations:
    - file: restore-databricks-on-aws.md
title: RESTORE TABLE TO TIMESTAMP AS OF
description: Restoring a Delta table to the state it was in at a specific point in time
tags:
  - delta-lake
  - time-travel
  - restore
timestamp: "2026-06-19T20:14:20.622Z"
---

# RESTORE TABLE TO TIMESTAMP AS OF

The **RESTORE TABLE TO TIMESTAMP AS OF** command restores a [Delta Lake](/concepts/delta-lake.md) table to the state it was in at a specified point in time. This enables time travel–based rollback to recover from accidental changes or to inspect historical data states without manually recreating the table from old snapshots. ^[restore-databricks-on-aws.md]

## Syntax

```sql
RESTORE TABLE table_name TO TIMESTAMP AS OF timestamp_expression;
```

The `timestamp_expression` can be a specific timestamp string, a function like `current_timestamp() - INTERVAL '1' HOUR`, or any expression that resolves to a timestamp. ^[restore-databricks-on-aws.md]

## Examples

Restore the `employee` table to a specific point in time:

```sql
RESTORE TABLE employee TO TIMESTAMP AS OF '2022-08-02 00:00:00';
```

Restore the `employee` table to the state it was in one hour ago:

```sql
RESTORE TABLE employee TO TIMESTAMP AS OF current_timestamp() - INTERVAL '1' HOUR;
```

These commands return a summary of the restoration, including the number of files added and removed, and the size changes. ^[restore-databricks-on-aws.md]

## Related Command: RESTORE TABLE TO VERSION AS OF

The `RESTORE` command also supports restoring by version number. The version number is retrieved from the output of `DESCRIBE HISTORY employee`. For example:

```sql
RESTORE TABLE employee TO VERSION AS OF 1;
```

Both forms perform the same logical operation but use different identification methods: timestamp or version number. ^[restore-databricks-on-aws.md]

## Output Columns

When the restore completes, a result set with the following columns is returned:

| Column | Description |
|--------|-------------|
| `table_size_after_restore` | Size of the table after restoration (in bytes). |
| `num_of_files_after_restore` | Number of files in the table after restoration. |
| `num_removed_files` | Number of files removed during the restore operation. |
| `num_restored_files` | Number of files restored from an earlier version. |
| `removed_files_size` | Total size of the removed files (in bytes). |
| `restored_files_size` | Total size of the restored files (in bytes). |

^[restore-databricks-on-aws.md]

## Considerations

- The command relies on the Delta transaction log and the underlying data files being available for the requested timestamp. If the data has been [Vacuum|VACUUMed](/concepts/vacuum-full-vs-vacuum-lite.md) beyond the retention period, the restore may fail.
- Using `current_timestamp() - INTERVAL '1' HOUR` restores the table to the most recent snapshot that is at least one hour old, which is useful for quickly undoing recent unintended modifications.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md)
- [Time Travel](/concepts/delta-lake-time-travel.md)
- [DESCRIBE HISTORY](/concepts/describe-history.md)
- VACUUM
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md)

## Sources

- restore-databricks-on-aws.md

# Citations

1. [restore-databricks-on-aws.md](/references/restore-databricks-on-aws-b92cad28.md)
