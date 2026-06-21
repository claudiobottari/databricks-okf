---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 49a767a3ad0a83bf80970ee03526c67b945cfecb123ee1593ae01559104a96b2
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-table-streaming-start-position
    - DTSSP
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: Delta Table Streaming Start Position
description: Using startingVersion and startingTimestamp options to define the initial read position for a streaming query on a Delta table
tags:
  - delta-lake
  - streaming
  - structured-streaming
timestamp: "2026-06-19T15:00:02.517Z"
---

# Delta Table Streaming Start Position

**Delta Table Streaming Start Position** refers to the configurable starting point for a Spark Structured Streaming query that reads from a [Delta Lake](/concepts/delta-lake.md) table source. By default, streams begin with the latest available [Delta Lake Table](/concepts/delta-lake-table.md) version, which includes a complete snapshot of the table at that moment and all future changes. Optional parameters allow you to specify an explicit version or timestamp to begin processing changes from a particular point in the table's history. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Default Behavior

Unless otherwise specified, a streaming query on a [Delta Lake Table](/concepts/delta-lake-table.md) starts from the current state of the table. The stream first processes the complete snapshot of the table at the time the query starts, and then incrementally processes all subsequent changes as new table versions commit. For most workloads, Databricks recommends using this default behavior. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Configuring a Starting Position

You can override the default starting position using the following read options, which apply only to new streaming queries. Once a query has started and its progress has been recorded in its checkpoint, these settings are ignored. You cannot set both `startingVersion` and `startingTimestamp` simultaneously. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### `startingVersion`

The `startingVersion` option specifies the [Delta Lake Table](/concepts/delta-lake-table.md) version to begin reading from. All table changes committed at or after the specified version are read by the stream. If the specified version is not available, the stream fails to start. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

To find available commit versions, run `DESCRIBE HISTORY` and check the `version` column. To return only the latest changes, specify the value `latest`. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

```python
(spark.readStream
  .option("startingVersion", "5")
  .table("user_events"))
```

```scala
spark.readStream
  .option("startingVersion", "5")
  .table("user_events")
```

### `startingTimestamp`

The `startingTimestamp` option specifies a timestamp to begin reading from. All table changes committed at or after the specified timestamp are read by the stream. If the provided timestamp precedes all table commits, the streaming read begins with the earliest available timestamp. You can set either: ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

- A timestamp string, for example `"2019-01-01T00:00:00.000Z"`.
- A date string, for example `"2019-01-01"`.

```python
(spark.readStream
  .option("startingTimestamp", "2018-10-18")
  .table("user_events"))
```

```scala
spark.readStream
  .option("startingTimestamp", "2018-10-18")
  .table("user_events")
```

## Schema Considerations

Although you can start the streaming source from a specified version or timestamp, the schema of the streaming source is always the **latest schema** of the [Delta Lake Table](/concepts/delta-lake-table.md). You must ensure there is no incompatible schema change to the [Delta Lake Table](/concepts/delta-lake-table.md) after the specified version or timestamp; otherwise, the streaming source might return incorrect results when reading the data with an incorrect schema. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Retention Window Impact

If you use a [Delta Lake Table](/concepts/delta-lake-table.md) as a streaming source, the streaming query must run at least one time within the source table's retention window. The default retention windows are 7 days for `VACUUM`-removed data files and 30 days for the transaction log (`logRetentionDuration`). If a query falls behind these windows, it fails with `DELTA_FILE_NOT_FOUND_DETAILED` and must be reset with a full refresh. Do _not_ set `spark.sql.files.ignoreMissingFiles` to `true` as a workaround because this configuration silently produces incorrect results. If a stream's schedule cannot keep up with the default retention windows, increase the source table's retention instead. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Related Concepts

- Delta Lake Table History — How to inspect and manage table version history.
- Delta Lake Retention — Configuration for data and transaction log retention.
- Spark Structured Streaming — The core streaming framework used for reading Delta Lake tables.
- [Delta Lake Change Data Feed](/concepts/delta-lake-change-data-feed-cdf.md) — An alternative approach for processing all types of changes (inserts, updates, deletes).
- Checkpoint-based Streaming — How streaming progress is tracked and why it affects starting position options.

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
