---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a88145138b2e3c9cea828e18c65db8a05058dbc29aeb26d067c77a5ef8413d38
  pageDirectory: concepts
  sources:
    - vacuum-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-time-travel-and-vacuum
    - VACUUM and Delta Lake Time Travel
    - DLTTAV
    - VACUUM (Delta Lake)
  citations:
    - file: vacuum-databricks-on-aws.md
title: Delta Lake Time Travel and VACUUM
description: Running VACUUM on a Delta table removes the ability to time travel to versions older than the specified data retention period.
tags:
  - databricks
  - delta-lake
  - time-travel
timestamp: "2026-06-19T23:24:28.717Z"
---

# [Delta Lake Time Travel](/concepts/delta-lake-time-travel.md) and VACUUM

**Delta Lake Time Travel** is a feature that allows users to access and query previous versions of a Delta table. **VACUUM** is a cleanup operation that removes unused data files from the table directory, which directly impacts the ability to time travel to older versions. Understanding the interplay between these two features is essential for managing data retention and storage costs.

## Time Travel Overview

[Delta Lake](/concepts/delta-lake.md)'s transaction log records every change made to a table, creating a version history. Time Travel enables you to query, restore, or compare data at any point in this version history. This capability is useful for auditing, reproducing analyses, rolling back accidental changes, and debugging. ^[vacuum-databricks-on-aws.md]

## VACUUM Operation

The `VACUUM` command recursively removes all files from the table directory that are not managed by [Delta Lake](/concepts/delta-lake.md), as well as data files that are no longer in the latest state of the transaction log and are older than a retention threshold. ^[vacuum-databricks-on-aws.md]

### Default Retention Period

The default retention threshold for `VACUUM` is **7 days**. This threshold is controlled by the `delta.deletedFileRetentionDuration` table property. When you run `VACUUM`, it removes data files that have been logically deleted from the transaction log for more than this retention period. ^[vacuum-databricks-on-aws.md]

### Impact on Time Travel

Running `VACUUM` on a Delta table removes the ability to time travel back to versions older than the specified retention period. Once `VACUUM` deletes data files for old versions, those versions become unrecoverable. To retain the ability to time travel for a longer duration, you must increase the `delta.deletedFileRetentionDuration` table property. For example:
```
ALTER TABLE table_name SET TBLPROPERTIES ('delta.deletedFileRetentionDuration' = '30 days');
```

^[vacuum-databricks-on-aws.md]

### VACUUM Modes

In Databricks Runtime 16.1 and above, `VACUUM` supports two modes: ^[vacuum-databricks-on-aws.md]

- **FULL** (default): Deletes data files outside the retention duration and all files in the table directory not referenced by the table.
- **LITE**: Uses the [Delta transaction log](/concepts/delta-transaction-log.md) to identify and remove files no longer referenced by any table versions within the retention duration. This mode is more efficient but requires the transaction log to be intact. If the log has been pruned, a `DELTA_CANNOT_VACUUM_LITE` exception is raised.

### Safety Considerations

Databricks strongly recommends setting a retention interval of at least 7 days. Long-running jobs might write files that are not yet committed, and a short retention period could cause `VACUUM` to delete these uncommitted files before the job completes. ^[vacuum-databricks-on-aws.md]

[Delta Lake](/concepts/delta-lake.md) includes a safety check to prevent running a dangerous `VACUUM` command. In Databricks Runtime, you can turn off this safety check by setting the Spark configuration property `spark.databricks.delta.retentionDurationCheck.enabled` to `false`, but only if you are certain that no operations on the table take longer than the specified retention interval. ^[vacuum-databricks-on-aws.md]

### Automatic VACUUM

If [predictive optimization](/concepts/delta-lake-predictive-optimization.md) is enabled, Databricks automatically triggers the `VACUUM` operation as part of its optimization process. In most cases, you do not need to run `VACUUM` manually. ^[vacuum-databricks-on-aws.md]

## DRY RUN

Before running `VACUUM`, you can use the `DRY RUN` option to return a list of up to 1000 files that would be deleted. This helps verify the impact of the operation before executing it. ^[vacuum-databricks-on-aws.md]

## Syntax

```sql
VACUUM table_name { { FULL | LITE } | DRY RUN } [...]
```

The table name must not include a [temporal specification or options specification](/concepts/temporal-specification-restriction-on-describe-history.md). ^[vacuum-databricks-on-aws.md]

## Best Practices

- Set the retention interval based on your time travel requirements. If you need to access data from 30 days ago, configure `delta.deletedFileRetentionDuration` to at least 30 days.
- Use the `DRY RUN` option to preview which files will be deleted before performing the actual cleanup.
- Consider relying on [predictive optimization](/concepts/delta-lake-predictive-optimization.md) for automatic `VACUUM` management.
- Be aware that `VACUUM` removes files based on their logical deletion time in the transaction log, not their file modification timestamps.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that provides ACID transactions and time travel.
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — The ordered record of every change made to a Delta table.
- Predictive Optimization — Automated optimization that can trigger VACUUM.

## Sources

- vacuum-databricks-on-aws.md

# Citations

1. [vacuum-databricks-on-aws.md](/references/vacuum-databricks-on-aws-9d87fed3.md)
