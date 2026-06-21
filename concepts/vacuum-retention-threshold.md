---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 49966d40a73531a78150ef2bc79f07dee343db0842134be0343585e430e849a5
  pageDirectory: concepts
  sources:
    - vacuum-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - vacuum-retention-threshold
    - VRT
  citations:
    - file: vacuum-databricks-on-aws.md
title: VACUUM Retention Threshold
description: The configurable time window (default 7 days) that determines which data files are safe to delete; files modified or logically removed within this window are retained.
tags:
  - databricks
  - delta-lake
  - configuration
timestamp: "2026-06-19T23:24:14.589Z"
---

# VACUUM Retention Threshold

The **VACUUM Retention Threshold** is the time period used by the VACUUM command to determine which unused data files in a Delta, Iceberg, or other table directory should be deleted. VACUUM removes files that are no longer part of the latest state of the table and are older than this retention threshold. The default retention threshold is **7 days** across all supported table types on Databricks. ^[vacuum-databricks-on-aws.md]

## Retention Threshold by Table Type

### Delta Tables

For [Delta Lake](/concepts/delta-lake.md) tables, the retention threshold is controlled by the table property `delta.deletedFileRetentionDuration`. This property defaults to 7 days if not explicitly set. Delta table data files are deleted according to the time they have been logically removed from the [Delta transaction log](/concepts/delta-transaction-log.md) plus the retention hours, not their modification timestamps on the storage system. ^[vacuum-databricks-on-aws.md]

If `VACUUM FULL` is used (the default mode), all data files outside the retention duration and all files in the table directory not referenced by the table are removed. The `VACUUM LITE` mode (available in Databricks Runtime 16.1+) uses the [Delta transaction log](/concepts/delta-transaction-log.md) to identify and remove files no longer referenced by any table versions within the retention duration, but may raise a `DELTA_CANNOT_VACUUM_LITE` exception if the log has been pruned. ^[vacuum-databricks-on-aws.md]

Running VACUUM on a Delta table results in the loss of the ability to [time travel](/concepts/delta-lake-time-travel.md) back to any version older than the specified data retention period. ^[vacuum-databricks-on-aws.md]

### Apache Iceberg Tables

For [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) tables, the retention period is fixed at **7 days** and cannot be modified via a table property. Databricks automatically triggers VACUUM as data is written if [predictive optimization](/concepts/delta-lake-predictive-optimization.md) is enabled. ^[vacuum-databricks-on-aws.md]

### Other Tables (Non-Delta, Non-Iceberg)

For tables that are not Delta or Iceberg, VACUUM recursively removes uncommitted files older than a retention threshold, which defaults to **7 days**. Databricks automatically triggers VACUUM operations on these tables as data is written. ^[vacuum-databricks-on-aws.md]

## Recommendations and Safety Checks

Databricks **strongly recommends** setting a retention interval of at least 7 days. If long-running jobs write files that are not yet committed, a retention period that is too short could cause VACUUM to delete those uncommitted files before the job completes. ^[vacuum-databricks-on-aws.md]

[Delta Lake](/concepts/delta-lake.md) includes a safety check to prevent running a dangerous VACUUM command. If you are certain that no operations on the table take longer than the retention interval you plan to specify, you can disable this safety check by setting the Spark configuration property `spark.databricks.delta.retentionDurationCheck.enabled` to `false`. ^[vacuum-databricks-on-aws.md]

## Customizing the Retention Threshold for Delta Tables

To retain data for a longer period—for example, to support time travel for longer durations—set the `delta.deletedFileRetentionDuration` table property to a higher value. The following example sets the threshold to 30 days:

```sql
ALTER TABLE table_name SET TBLPROPERTIES ('delta.deletedFileRetentionDuration' = '30 days');
```

^[vacuum-databricks-on-aws.md]

## Automatic Management via Predictive Optimization

If [predictive optimization](/concepts/delta-lake-predictive-optimization.md) is enabled on a workspace, Databricks automatically triggers the VACUUM operation as part of its optimization process. In most cases, manual VACUUM is not required when this feature is active. ^[vacuum-databricks-on-aws.md]

## Related Concepts

- VACUUM — The full SQL command syntax and behavior.
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that VACUUM operates on.
- [Time Travel](/concepts/delta-lake-time-travel.md) — Ability to access previous versions of a Delta table.
- Predictive Optimization — Automatic maintenance that includes VACUUM.
- [Delta transaction log](/concepts/delta-transaction-log.md) — The record of changes that VACUUM uses for identification of unreferenced files.
- Spark configuration properties — Settings that control safety checks for VACUUM.

## Sources

- vacuum-databricks-on-aws.md

# Citations

1. [vacuum-databricks-on-aws.md](/references/vacuum-databricks-on-aws-9d87fed3.md)
