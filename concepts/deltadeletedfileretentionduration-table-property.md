---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3ee117484c169b01fefa40154982d9059297a75fc9e5ceab99592c5f6dc33ba2
  pageDirectory: concepts
  sources:
    - vacuum-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deltadeletedfileretentionduration-table-property
    - DTP
  citations:
    - file: vacuum-databricks-on-aws.md
title: delta.deletedFileRetentionDuration Table Property
description: A Delta table property that controls the retention window for VACUUM, overriding the default 7-day threshold to support longer time travel capabilities.
tags:
  - databricks
  - delta-lake
  - table-properties
timestamp: "2026-06-19T23:24:24.521Z"
---

# delta.deletedFileRetentionDuration Table Property

The `delta.deletedFileRetentionDuration` table property controls how long data files that have been logically removed from a Delta table’s transaction log are kept before the VACUUM command can physically delete them. ^[vacuum-databricks-on-aws.md]

## Default

The default value for `delta.deletedFileRetentionDuration` is **7 days**. This means that by default, `VACUUM` will only remove data files that are no longer referenced by any Delta table version in the last 7 days. ^[vacuum-databricks-on-aws.md]

## Effect on VACUUM

The retention window for the `VACUUM` command is entirely determined by this table property. `VACUUM` uses the [Delta transaction log](/concepts/delta-transaction-log.md) to identify files that are no longer referenced by any table versions within the retention duration. Files that have been logically removed but are still within the retention window are kept, even if they are older than the modification timestamps on the storage system. ^[vacuum-databricks-on-aws.md]

If you set the property to a higher value, `VACUUM` will preserve those files for a longer period. Conversely, setting it to a lower value will cause files to be deleted sooner, which can free up storage more aggressively but may break concurrent write operations if the retention interval is too short. ^[vacuum-databricks-on-aws.md]

## Effect on Time Travel

Because `VACUUM` physically removes data files, running it on a Delta table means you lose the ability to [time travel](/concepts/delta-lake-time-travel.md) back to a version older than the specified data retention period. If you need to time travel to older versions, set `delta.deletedFileRetentionDuration` to a value equal to or greater than the desired time-travel horizon. ^[vacuum-databricks-on-aws.md]

## Configuration

You can set this table property using the `ALTER TABLE SET TBLPROPERTIES` command. The value must be a string that specifies a duration, such as `'30 days'` or `'7 days'`.

Example: ^[vacuum-databricks-on-aws.md]

```sql
ALTER TABLE table_name SET TBLPROPERTIES ('delta.deletedFileRetentionDuration' = '30 days');
```

This example extends the retention to 30 days, allowing time travel back to any version within the last 30 days and preventing `VACUUM` from deleting those files before the extended window. ^[vacuum-databricks-on-aws.md]

## Related Concepts

- VACUUM – The command that uses this property to determine which files to delete.
- [Time Travel](/concepts/delta-lake-time-travel.md) – The ability to query previous versions of a Delta table; limited by the retention duration.
- [Delta Lake](/concepts/delta-lake.md) – The storage layer that manages the transaction log and file lifecycle.
- Table Properties – General configuration for Delta tables.
- Predictive Optimization – An automated process that can trigger `VACUUM` without manual intervention.

## Sources

- vacuum-databricks-on-aws.md

# Citations

1. [vacuum-databricks-on-aws.md](/references/vacuum-databricks-on-aws-9d87fed3.md)
