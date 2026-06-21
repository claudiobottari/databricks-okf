---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2edee1b0d2c71de3dc464d34338fa7b0ce6f5a7574a26efa8aad9cf9b0ecb352
  pageDirectory: concepts
  sources:
    - vacuum-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - vacuum-dry-run
    - VDR
  citations:
    - file: vacuum-databricks-on-aws.md
title: VACUUM DRY RUN
description: A preview mode for VACUUM that returns up to 1000 files that would be deleted without actually removing them.
tags:
  - databricks
  - sql
  - safety
timestamp: "2026-06-19T23:24:16.127Z"
---

## VACUUM DRY RUN

**VACUUM DRY RUN** is a parameter of the `VACUUM` command that returns a preview list of files that would be deleted by the operation without actually removing them. It is a safe way to inspect which files are eligible for cleanup before executing the full `VACUUM`. ^[vacuum-databricks-on-aws.md]

### Syntax

```sql
VACUUM table_name DRY RUN [ FULL | LITE ]
```

The `FULL` and `LITE` qualifiers are optional and apply only to Delta tables on Databricks Runtime 16.1 and above. If omitted, the default vacuum mode is `FULL`. ^[vacuum-databricks-on-aws.md]

### Parameters

- **`DRY RUN`** – Returns a list of up to 1000 files that would be deleted by the `VACUUM` operation. This list is a preview only; no files are actually removed. ^[vacuum-databricks-on-aws.md]
- **`FULL`** – Runs the vacuum operation in "Full" mode, which deletes data files outside the retention duration and all files in the table directory not referenced by the table. This is the default mode. ^[vacuum-databricks-on-aws.md]
- **`LITE`** – Runs the vacuum operation in "Lite" mode, which uses the [Delta transaction log](/concepts/delta-transaction-log.md) to identify and remove files no longer referenced by any table versions within the retention duration. If the Delta log has been pruned, `VACUUM LITE` raises a `DELTA_CANNOT_VACUUM_LITE` exception. ^[vacuum-databricks-on-aws.md]

### Behavior by Table Type

#### Delta Tables

When used on a Delta table, `VACUUM ... DRY RUN` previews files that are no longer managed by Delta—those not in the latest state of the transaction log and older than the retention threshold (default 7 days). The command skips directories starting with an underscore (`_`), except for valid partitions that begin with an underscore. Deletion eligibility is based on the time a file was logically removed from Delta's transaction log, not its modification timestamp on storage. ^[vacuum-databricks-on-aws.md]

Running `VACUUM` (even with `DRY RUN` does not affect time travel, but the actual deletion loses the ability to [time travel](/concepts/delta-lake-time-travel.md) to versions older than the retention period. If [predictive optimization](/concepts/delta-lake-predictive-optimization.md) is enabled, Databricks automatically triggers `VACUUM` as part of its optimization process; manual runs are usually unnecessary. ^[vacuum-databricks-on-aws.md]

#### Iceberg Tables

For Apache Iceberg tables, `VACUUM ... DRY RUN` previews unreferenced files. The retention period for Iceberg tables is fixed at 7 days. ^[vacuum-databricks-on-aws.md]

#### Other Tables

For non-Delta, non-Iceberg tables, `VACUUM ... DRY RUN` previews uncommitted files older than the retention threshold (default 7 days). Databricks automatically triggers `VACUUM` operations as data is written on these tables. ^[vacuum-databricks-on-aws.md]

### Retention and Safety Considerations

The retention window for `VACUUM` on Delta tables is controlled by the `delta.deletedFileRetentionDuration` table property, which defaults to 7 days. To support longer time travel, this property can be increased, for example:

```sql
ALTER TABLE table_name SET TBLPROPERTIES ('delta.deletedFileRetentionDuration' = '30 days');
```

Databricks strongly recommends a retention interval of at least 7 days to prevent `VACUUM` from deleting uncommitted files from long-running jobs. [Delta Lake](/concepts/delta-lake.md) includes a safety check to prevent dangerous `VACUUM` commands. If you are certain that no operations on the table take longer than your specified retention interval, you can disable this check by setting `spark.databricks.delta.retentionDurationCheck.enabled` to `false`. ^[vacuum-databricks-on-aws.md]

### Related Concepts

- VACUUM – The full command for removing unused files from table directories.
- [Delta tables](/concepts/delta-lake-table.md) – The primary table format for which `VACUUM` with `DRY RUN` is most often used.
- Iceberg tables – An alternative table format with its own `VACUUM` behavior.
- [Predictive optimization](/concepts/predictive-optimization-for-delta-lake.md) – An automatic trigger for `VACUUM` operations.
- [Time travel](/concepts/delta-lake-time-travel.md) – A [Delta Lake](/concepts/delta-lake.md) feature that is affected by the retention duration used by `VACUUM`.
- Table properties – Including `delta.deletedFileRetentionDuration` for configuring retention.

### Sources

- vacuum-databricks-on-aws.md

# Citations

1. [vacuum-databricks-on-aws.md](/references/vacuum-databricks-on-aws-9d87fed3.md)
