---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 980bdb70f1db221473fdd4c23797aa5af6a6ffd6ad2c8c1c2ddbbe05b13da252
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-as-a-streaming-source-and-sink
    - Sink and Delta Lake as a Streaming Source
    - DLAASSAS
    - Delta Lake as a Streaming Source
    - Delta Lake Table Streaming Reads and Writes
    - Delta Lake streaming reads and writes
    - Delta Lake table streaming reads and writes
    - Streaming Source
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: Delta Lake as a Streaming Source and Sink
description: Overview of using Delta Lake tables with Spark Structured Streaming readStream/writeStream, including exactly-once guarantees and performance benefits.
tags:
  - structured-streaming
  - delta-lake
  - real-time-processing
timestamp: "2026-06-19T18:20:37.131Z"
---

# Delta Lake as a Streaming Source and Sink

**Delta Lake as a streaming source and sink** refers to using [Delta Lake](/concepts/delta-lake.md) tables with Spark Structured Streaming's `readStream` and `writeStream` APIs for real-time and incremental data processing. Delta Lake provides reliability and performance benefits for streaming workloads, including exactly-once processing guarantees, efficient file management, and robust transaction semantics. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Using Delta Lake as a Streaming Sink

### Append Mode

By default, streams run in append mode, adding only new records to the table. Use the `toTable` method when streaming to tables: ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

```python
(events.writeStream
   .outputMode("append")
   .option("checkpointLocation", "/tmp/delta/events/_checkpoints/")
   .toTable("events"))
```

### Complete Mode

Use complete mode to replace the entire table after every batch. This is useful for continuously updating aggregated summary tables: ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

```python
(spark.readStream
  .table("events")
  .groupBy("customerId")
  .count()
  .writeStream
  .outputMode("complete")
  .option("checkpointLocation", "/tmp/delta/eventsByCustomer/_checkpoints/")
  .toTable("events_by_customer"))
```

### Empty Commits

When writing to a [Delta Lake Table](/concepts/delta-lake-table.md) using a Structured Streaming sink, you might see empty commits with `epochId = -1`. These are expected and typically occur on the first batch of each run or when a schema changes. They do not affect correctness or performance. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Using Delta Lake as a Streaming Source

### Retention Window Requirements

If you use a [Delta Lake Table](/concepts/delta-lake-table.md) as a streaming source, the streaming query must run at least once within the source table's retention window. The default retention windows are 7 days for `VACUUM`-removed data files and 30 days for the transaction log (`logRetentionDuration`). If a query falls behind these windows, it fails with `DELTA_FILE_NOT_FOUND_DETAILED` and must be reset with a full refresh. Do **not** set `spark.sql.files.ignoreMissingFiles` to `true` as a workaround, as this silently produces incorrect results. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### Setting Initial Table Version

By default, streams begin with the latest available [Delta Lake Table](/concepts/delta-lake-table.md) version. You can optionally specify a starting point using: ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

- **`startingVersion`**: The [Delta Lake Table](/concepts/delta-lake-table.md) version to start reading from. All changes committed at or after the specified version are read.
- **`startingTimestamp`**: The timestamp to start reading from. All changes committed at or after the specified timestamp are read.

You cannot set both options simultaneously. These settings apply only to new streaming queries; once a query has started and recorded progress in its checkpoint, these settings are ignored. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

```scala
spark.readStream
  .option("startingVersion", "5")
  .table("user_events")
```

### Limiting Input Rate

To manage memory usage, stabilize latency, or reduce cloud storage costs, use the following options: ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

- **`maxFilesPerTrigger`**: The number of new files to consider in every micro-batch (default is 1000).
- **`maxBytesPerTrigger`**: The amount of data processed in each micro-batch (soft max, not set by default).

If both options are used, the micro-batch processes data until either limit is reached. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Handling Changes to Source Tables

Structured Streaming only accepts append inputs and throws an exception if modifications occur on the source [Delta Lake Table](/concepts/delta-lake-table.md). There are four typical approaches for handling upstream changes: ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### Skip Change Commits

Set `skipChangeCommits` to ignore transactions that delete or modify existing records and process only appends. This is recommended for most workloads that do not use change data feeds: ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

```python
(spark.readStream
  .option("skipChangeCommits", "true")
  .table("source_table"))
```

### Full Refresh of Downstream Tables

If upstream changes are rare and data is small enough to reprocess, delete the streaming checkpoint and output table, then restart the stream from the beginning. This approach is best suited for smaller datasets or infrequent changes. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### Use Change Data Feed

For workloads that process all types of changes (inserts, updates, and deletes), use the [Delta Lake change data feed](/concepts/delta-lake-change-data-feed-cdf.md). This records row-level changes and allows you to stream those changes with explicit logic for each change type. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### Use Materialized Views

Materialized views automatically handle upstream changes by recomputing results when source data changes. This approach simplifies architecture when you do not need the lowest possible latency. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Idempotent Writes with `foreachBatch`

Delta Lake tables support `txnAppId` and `txnVersion` DataFrameWriter options to make writes within `foreachBatch` idempotent. Delta Lake uses these to identify and ignore duplicate writes after failures: ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

```python
app_id = ... # A unique string used as an application ID.

def writeToDeltaLakeTableIdempotent(batch_df, batch_id):
  batch_df.write.format(...).option("txnVersion", batch_id).option("txnAppId", app_id).save(...)

streamingDF.writeStream.foreachBatch(writeToDeltaLakeTableIdempotent).start()
```

If you delete the streaming checkpoint and restart with a new checkpoint, you must provide a different `txnAppId`. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Upserts from Streaming Queries

Use `merge` and `foreachBatch` to write complex upserts from a streaming query into a [Delta Lake Table](/concepts/delta-lake-table.md). This approach has several applications: ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

- Improve write performance with `update` output mode instead of `complete` mode.
- Continuously apply a stream of changes using merge queries for slowly changing data (SCD) and change data capture (CDC).
- Handle deduplication during stream processing with insert-only merge queries.

Verify that your `merge` statement inside `foreachBatch` is idempotent to prevent duplicate operations on restarts. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Processing Initial Snapshot with Event Time Order

Available on Databricks Runtime 11.3 LTS and above, the `withEventTimeOrder` option prevents data drops during initial snapshot processing in stateful streaming queries with defined watermarks. It divides the event time range into time buckets, processing each bucket in order to ensure records are not incorrectly marked as late events. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

```scala
spark.readStream
  .option("withEventTimeOrder", "true")
  .table("user_events")
  .withWatermark("event_time", "10 seconds")
```

Performance may be slower with this option enabled. To improve filtering performance, use a Delta source column as the event time for data skipping, or partition the table along the event time column. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Monitoring Backlog

Use the following metrics to monitor the backlog of a streaming query: ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

- **`numBytesOutstanding`**: Number of bytes yet to be processed.
- **`numFilesOutstanding`**: Number of files yet to be processed.
- **`numNewListedFiles`**: Number of Delta Lake files listed for this batch.
- **`backlogEndOffset`**: The [Delta Lake Table](/concepts/delta-lake-table.md) version used to calculate the backlog.

## Checkpoint Storage

The Delta Lake `VACUUM` function removes all files not managed by Delta Lake but skips directories that begin with `_`. You can safely store checkpoints alongside other data and metadata using a directory structure such as `<table-name>/_checkpoints`. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Related Concepts

- Spark Structured Streaming
- [Delta Lake](/concepts/delta-lake.md)
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md)
- foreachBatch
- Slowly Changing Data (SCD)
- Change Data Capture (CDC)
- Data Deduplication
- Stream-Static Joins

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
