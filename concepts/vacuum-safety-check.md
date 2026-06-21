---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7081a7eb0ee1b05f17619b975d81e8061f95d2d1082caf1374752320d83c6646
  pageDirectory: concepts
  sources:
    - vacuum-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - vacuum-safety-check
    - VSC
  citations:
    - file: vacuum-databricks-on-aws.md
title: VACUUM Safety Check
description: A Delta Lake safety mechanism that prevents dangerous VACUUM operations with too-short retention intervals, controllable via spark.databricks.delta.retentionDurationCheck.enabled.
tags:
  - databricks
  - safety
  - configuration
timestamp: "2026-06-19T23:24:46.930Z"
---

# VACUUM Safety Check

The **VACUUM Safety Check** is a built-in protection mechanism in [Delta Lake](/concepts/delta-lake.md) that prevents users from running a dangerous `VACUUM` command with a retention interval that is too short. Its purpose is to safeguard against accidental data loss, particularly when long-running jobs may have uncommitted files in the table directory that are not yet referenced by the transaction log. ^[vacuum-databricks-on-aws.md]

## How It Works

[Delta Lake](/concepts/delta-lake.md)'s `VACUUM` operation removes data files that are no longer in the latest state of the transaction log and are older than a specified retention threshold. The VACUUM Safety Check prevents you from specifying a retention interval that could lead to the deletion of files that are still needed by active or incomplete operations. This is especially important because `VACUUM` deletes files based on how long they have been logically removed from Delta's transaction log plus the retention hours, not their modification timestamps on the storage system. ^[vacuum-databricks-on-aws.md]

## Risk of Short Retention Intervals

If you have jobs that run for several days, those long-running jobs might write files that are not yet committed to the transaction log. If the retention period is too short, `VACUUM` could delete these uncommitted files before the job completes, causing job failures or data corruption. ^[vacuum-databricks-on-aws.md]

Databricks strongly recommends setting a retention interval of at least 7 days. ^[vacuum-databricks-on-aws.md]

## Disabling the Safety Check

If you are certain that there are no operations being performed on a table that take longer than the retention interval you plan to specify, you can turn off this safety check. To disable it, set the Spark configuration property `spark.databricks.delta.retentionDurationCheck.enabled` to `false`. ^[vacuum-databricks-on-aws.md]

## Relationship to Retention Configuration

The retention window for the `VACUUM` command is determined by the `delta.deletedFileRetentionDuration` table property, which defaults to 7 days. This property controls how long data files are retained after they are no longer referenced by any table version. To retain data for a longer period — such as to support [time travel](/concepts/delta-lake-time-travel.md) for longer durations — you can set this table property to a higher value. ^[vacuum-databricks-on-aws.md]

## Related Concepts

- VACUUM — The command for removing unused files from Delta, Iceberg, and other tables.
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — The mechanism [Delta Lake](/concepts/delta-lake.md) uses to track table versions and file references.
- [Time Travel](/concepts/delta-lake-time-travel.md) — The ability to access previous versions of a Delta table, which is affected by `VACUUM` operations.
- Predictive Optimization — A Databricks feature that can automatically trigger `VACUUM` operations.
- Table Properties — Configuration options for Delta tables, including retention duration settings.

## Sources

- vacuum-databricks-on-aws.md

# Citations

1. [vacuum-databricks-on-aws.md](/references/vacuum-databricks-on-aws-9d87fed3.md)
