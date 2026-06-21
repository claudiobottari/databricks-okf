---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 70b2b1baaf04b8781750f0c8982aed8beb316a348d322638bdfc44de694b93a0
  pageDirectory: concepts
  sources:
    - restore-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - restore-operation-metrics
    - ROM
  citations:
    - file: restore-databricks-on-aws.md
title: RESTORE Operation Metrics
description: Output columns returned by a RESTORE operation showing table size, file counts, and files changed during the restore
tags:
  - delta-lake
  - monitoring
  - operations
timestamp: "2026-06-19T20:14:26.679Z"
---

# RESTORE Operation Metrics

**RESTORE Operation Metrics** are the six values returned by the `RESTORE TABLE` command on [Delta Lake](/concepts/delta-lake.md) tables. These metrics describe the state of the table after the restore (size and number of files) and the effects of the restore (number of files removed or restored, and their sizes). ^[restore-databricks-on-aws.md]

## Metrics Returned

When a `RESTORE TABLE` command completes, it outputs a single row with the following columns:

- **`table_size_after_restore`** – The total size (in bytes) of the table after the restore operation.
- **`num_of_files_after_restore`** – The number of data files in the table after the restore.
- **`num_removed_files`** – The number of files that were removed from the table as a result of the restore.
- **`num_restored_files`** – The number of files that were restored (i.e., reinstated from a previous version) to reach the target state.
- **`removed_files_size`** – The total size (in bytes) of the files that were removed.
- **`restored_files_size`** – The total size (in bytes) of the files that were restored.

^[restore-databricks-on-aws.md]

## Example Output

The following examples show the metrics returned for a table named `employee`:

```sql
RESTORE TABLE employee TO TIMESTAMP AS OF '2022-08-02 00:00:00';

table_size_after_restore  num_of_files_after_restore  num_removed_files  num_restored_files  removed_files_size  restored_files_size
                     100                          3                  1                   0                 574                   0
```

```sql
RESTORE TABLE employee TO VERSION AS OF 1;

table_size_after_restore  num_of_files_after_restore  num_removed_files  num_restored_files  removed_files_size  restored_files_size
                     100                          3                  1                   0                 574                   0
```

```sql
RESTORE TABLE employee TO TIMESTAMP AS OF current_timestamp() - INTERVAL '1' HOUR;

table_size_after_restore  num_of_files_after_restore  num_removed_files  num_restored_files  removed_files_size  restored_files_size
                     100                          3                  1                   0                 574                   0
```

^[restore-databricks-on-aws.md]

## Interpretation

The metrics allow users to understand the impact of a restore operation:

- A non-zero **`num_removed_files`** indicates that some files from the current state were removed to revert to the target version.
- A non-zero **`num_restored_files`** indicates that files from an earlier state were added back.
- The **`table_size_after_restore`** and **`num_of_files_after_restore`** describe the final state of the table.
- The **`removed_files_size`** and **`restored_files_size`** provide the total byte sizes of the files affected in each direction.

In the examples above, the restore removed 1 file (574 bytes) and restored 0 files, leaving a table of 100 bytes across 3 files.

## Related Concepts

- [RESTORE TABLE Command](/concepts/restore-table-command.md) – The SQL command that returns these metrics.
- [Delta Lake Time Travel](/concepts/delta-lake-time-travel.md) – The mechanism used to specify the target version or timestamp.
- [DESCRIBE HISTORY](/concepts/describe-history.md) – Used to retrieve table version history and version numbers for `RESTORE TABLE TO VERSION AS OF`.
- Delta Lake File Management – How Delta manages data files and transaction logs.

## Sources

- restore-databricks-on-aws.md

# Citations

1. [restore-databricks-on-aws.md](/references/restore-databricks-on-aws-b92cad28.md)
