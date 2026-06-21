---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d7c3b2b994bb1120bef690c0346a50d3fe7a70409c7718d016f85b004fa39456
  pageDirectory: concepts
  sources:
    - vacuum-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - vacuum-full-vs-vacuum-lite
    - VFVVL
    - Vacuum|VACUUMed
  citations:
    - file: vacuum-databricks-on-aws.md
title: VACUUM FULL vs VACUUM LITE
description: "Two modes of VACUUM operation on Delta tables: FULL scans all files in the table directory, while LITE uses the transaction log to identify deletable files more efficiently."
tags:
  - databricks
  - delta-lake
  - optimization
timestamp: "2026-06-19T23:24:11.548Z"
---

# VACUUM FULL vs VACUUM LITE

**VACUUM FULL** and **VACUUM LITE** are two modes of the `VACUUM` command on Databricks that remove unused files from a [Delta Lake](/concepts/delta-lake.md) table directory. Both modes are available in Databricks Runtime 16.1 and above. The default mode is `FULL`. ^[vacuum-databricks-on-aws.md]

## VACUUM FULL

`VACUUM FULL` runs the vacuum operation in *Full* mode. It deletes data files that are outside the retention duration and all files in the table directory that are not referenced by the table. This is the traditional vacuum behavior: it scans the entire table directory to find files not managed by Delta, as well as data files no longer in the latest state of the transaction log and older than the retention threshold. ^[vacuum-databricks-on-aws.md]

## VACUUM LITE

`VACUUM LITE` runs the vacuum operation in *Lite* mode. Instead of finding all files in the table directory, it uses the [Delta transaction log](/concepts/delta-transaction-log.md) to identify and remove files no longer referenced by any table versions within the retention duration. This approach is more efficient because it avoids a full directory scan. ^[vacuum-databricks-on-aws.md]

However, `VACUUM LITE` can fail if the Delta log has been pruned. In that case, a `DELTA_CANNOT_VACUUM_LITE` exception is raised, and the operation cannot complete. ^[vacuum-databricks-on-aws.md]

## Key Differences

| Feature | VACUUM FULL | VACUUM LITE |
|---|---|---|
| Scan scope | Scans the entire table directory | Uses the [Delta transaction log](/concepts/delta-transaction-log.md) only |
| Efficiency | Slower for large directories | Faster, as it skips directory scan |
| Failure condition | None specific to log pruning | Raises `DELTA_CANNOT_VACUUM_LITE` if the log is pruned |
| Default | Yes | No (must be specified explicitly) |

Both modes respect the same retention threshold, which defaults to 7 days and can be controlled via the `delta.deletedFileRetentionDuration` table property. ^[vacuum-databricks-on-aws.md]

## Retention Threshold

The retention window for `VACUUM` is determined by the `delta.deletedFileRetentionDuration` table property, which defaults to 7 days. This means `VACUUM` removes data files that are no longer referenced by a Delta table version in the last 7 days. To support longer [time travel](/concepts/delta-lake-time-travel.md) windows, set this property to a higher value. For example:

```sql
ALTER TABLE table_name SET TBLPROPERTIES ('delta.deletedFileRetentionDuration' = '30 days');
```

^[vacuum-databricks-on-aws.md]

## Automatic Operation

If [predictive optimization](/concepts/delta-lake-predictive-optimization.md) is enabled, Databricks automatically triggers `VACUUM` as part of its optimization process. In most cases, you do not need to run `VACUUM` manually. ^[vacuum-databricks-on-aws.md]

## Safety Considerations

Databricks strongly recommends a retention interval of at least 7 days. Long-running jobs may write files that are not yet committed; if the retention period is too short, `VACUUM` could delete these uncommitted files before the job completes. [Delta Lake](/concepts/delta-lake.md) includes a safety check to prevent dangerous vacuum operations. You can disable this check by setting `spark.databricks.delta.retentionDurationCheck.enabled` to `false`, but only if you are certain no operations on the table take longer than the specified retention interval. ^[vacuum-databricks-on-aws.md]

## Syntax

```sql
VACUUM table_name { FULL | LITE } [DRY RUN] [...]
```

- `FULL` — Full mode (default).
- `LITE` — Lite mode.
- `DRY RUN` — Returns a list of up to 1000 files that would be deleted without actually deleting them.

^[vacuum-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md)
- [Time Travel](/concepts/delta-lake-time-travel.md)
- [Delta transaction log](/concepts/delta-transaction-log.md)
- Predictive Optimization
- Delta table properties
- [VACUUM command](/concepts/vacuum-command-databricks.md)

## Sources

- vacuum-databricks-on-aws.md

# Citations

1. [vacuum-databricks-on-aws.md](/references/vacuum-databricks-on-aws-9d87fed3.md)
