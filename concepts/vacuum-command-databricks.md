---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9a3428e008511de0960d20bfc4a2c06e9cdfa88c08eba0d92e4a09308bc21408
  pageDirectory: concepts
  sources:
    - vacuum-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - vacuum-command-databricks
    - VC(
    - VACUUM Command
    - VACUUM command
    - Vacuum command
  citations:
    - file: vacuum-databricks-on-aws.md
title: VACUUM Command (Databricks)
description: A Databricks SQL command that removes unused data files from Delta, Iceberg, and other table directories to free storage space.
tags:
  - databricks
  - sql
  - table-maintenance
timestamp: "2026-06-19T23:24:12.222Z"
---

# VACUUM Command (Databricks)

**VACUUM** is a SQL command on Databricks that removes unused files from a table directory. Its behavior differs depending on whether the target table is a [Delta Lake](/concepts/delta-lake.md) table, an [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) table, or another type of table. ^[vacuum-databricks-on-aws.md]

## Vacuuming a Delta table

`VACUUM` recursively cleans directories associated with a Delta table. It removes all files that are not managed by [Delta Lake](/concepts/delta-lake.md), as well as data files that are no longer in the latest state of the table's transaction log and are older than a retention threshold. The command skips all directories that begin with an underscore (`_`), which includes the `_delta_log` directory. If the table is partitioned on a column that starts with an underscore, `VACUUM` scans all valid partitions in the target table. ^[vacuum-databricks-on-aws.md]

Delta table data files are deleted according to the time they were logically removed from the transaction log plus the retention hours, not based on their file modification timestamps on the storage system. The default retention threshold is 7 days. Running `VACUUM` on a Delta table removes the ability to [time travel](/concepts/delta-lake-time-travel.md) back to a version older than the specified data retention period. ^[vacuum-databricks-on-aws.md]

If [predictive optimization](/concepts/delta-lake-predictive-optimization.md) is enabled, Databricks automatically triggers `VACUUM` as part of its optimization process. In most cases, manual execution of `VACUUM` is not needed. ^[vacuum-databricks-on-aws.md]

## Vacuuming an Apache Iceberg table

For Apache Iceberg tables, `VACUUM` recursively removes unreferenced files from the table directories. The retention period is fixed at 7 days. As with Delta tables, predictive optimization automatically triggers `VACUUM` when enabled. ^[vacuum-databricks-on-aws.md]

## Vacuuming other tables

For tables that are neither Delta nor Iceberg, `VACUUM` recursively cleans associated directories by removing uncommitted files older than a retention threshold (default 7 days). Databricks automatically triggers these `VACUUM` operations as data is written. ^[vacuum-databricks-on-aws.md]

## Syntax and parameters

```
VACUUM table_name { { FULL | LITE } | DRY RUN } [...]
```

- `table_name`: Identifies an existing table. For Delta tables, the name must not include a temporal specification or options specification.
- `DRY RUN`: Returns a list of up to 1,000 files that would be deleted, without performing the deletion.
- `FULL` (default): Runs a full vacuum which deletes data files outside the retention duration and all files in the table directory not referenced by the table.
- `LITE`: (Applies to Databricks Runtime 16.1 and above on Delta tables) Uses the [Delta transaction log](/concepts/delta-transaction-log.md) to identify and remove files no longer referenced by any table version within the retention duration. If the Delta log has been pruned, a `DELTA_CANNOT_VACUUM_LITE` exception is raised. ^[vacuum-databricks-on-aws.md]

## Retention configuration

The retention window for `VACUUM` on Delta tables is determined by the `delta.deletedFileRetentionDuration` table property, which defaults to 7 days. This property controls how long data files that are no longer referenced by a Delta table version are retained. To support time travel for longer durations, set this property to a higher value. For example:

```sql
ALTER TABLE table_name SET TBLPROPERTIES ('delta.deletedFileRetentionDuration' = '30 days');
```

Iceberg and other tables have a fixed retention threshold of 7 days. ^[vacuum-databricks-on-aws.md]

## Safety considerations

Databricks strongly recommends a retention interval of at least 7 days. Long-running jobs may write files that are not yet committed; if the retention period is too short, `VACUUM` could delete these uncommitted files before the job completes. [Delta Lake](/concepts/delta-lake.md) includes a safety check that prevents running a `VACUUM` with a dangerously short retention interval. To disable this check, set the Spark configuration property `spark.databricks.delta.retentionDurationCheck.enabled` to `false`. This should only be done when absolutely certain that no operations are running on the table that take longer than the specified retention interval. ^[vacuum-databricks-on-aws.md]

## Related concepts

- [Delta Lake](/concepts/delta-lake.md)
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md)
- [Time travel](/concepts/delta-lake-time-travel.md)
- [Predictive optimization](/concepts/predictive-optimization-for-delta-lake.md)
- [Delta transaction log](/concepts/delta-transaction-log.md)
- Spark configuration properties

## Sources

- vacuum-databricks-on-aws.md

# Citations

1. [vacuum-databricks-on-aws.md](/references/vacuum-databricks-on-aws-9d87fed3.md)
