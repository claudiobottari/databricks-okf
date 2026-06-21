---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f224e092a8eb36f1d1f8d4d697cd0c53db1f63dbceb254c99bb0026ed0e3a29d
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-as-a-streaming-sink
    - DLAASS
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: Delta Lake as a Streaming Sink
description: Using Delta Lake tables as sinks for Spark Structured Streaming with exactly-once processing guarantees
tags:
  - streaming
  - delta-lake
  - spark-structured-streaming
timestamp: "2026-06-18T15:15:40.196Z"
---

```yaml
---
title: Delta Lake as a Streaming Sink
summary: Using Delta Lake tables as sinks for Spark Structured Streaming with append and complete output modes, leveraging the transaction log for exactly-once processing guarantees.
sources:
  - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:49:00.987Z"
updatedAt: "2026-06-18T11:49:00.987Z"
tags:
  - streaming
  - delta-lake
  - structured-streaming
aliases:
  - delta-lake-as-a-streaming-sink
  - DLAASS
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Delta Lake as a Streaming Sink

**Delta Lake as a Streaming Sink** refers to using a [[Delta Lake]] table as the output target for Spark Structured Streaming queries via `writeStream`. The Delta Lake transaction log guarantees exactly-once processing, even when other streams or batch queries run concurrently against the same table. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Append Mode

By default, streams run in append mode and only add new records to the table. Use the `toTable` method when streaming to tables: ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

```python
(events.writeStream
   .outputMode("append")
   .option("checkpointLocation", "/tmp/delta/events/_checkpoints/")
   .toTable("events"))
```

## Complete Mode

Use Structured Streaming with complete mode to replace the entire table after every batch. For example, you can continuously update an aggregated summary table of events by customer: ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

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

For applications without strict latency requirements, you can save computing resources and costs with one-time triggers such as `AvailableNow`. See Structured Streaming Triggers. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Empty Commits

When you write to a [[delta-lake-table|Delta Lake Table]] using a Structured Streaming sink, you might see empty commits with `epochId = -1`. These are expected and typically occur: ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

- On the first batch of each run of the streaming query (this happens every batch for `Trigger.AvailableNow`).
- When a schema is changed (such as adding a column).

These empty commits are intentional and do not indicate an error. They do not affect the correctness or performance of the query in any significant way. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Checkpoint Storage

The Delta Lake `VACUUM` function removes all files not managed by Delta Lake but skips any directories that begin with `_`. You can safely store checkpoints alongside other data and metadata for a [[delta-lake-table|Delta Lake Table]] using a directory structure such as `<table-name>/_checkpoints`. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Monitor Backlog with Metrics

Use the following metrics to monitor the backlog of a streaming query process: ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

- `numBytesOutstanding`: Number of bytes yet to be processed in the backlog.
- `numFilesOutstanding`: Number of files yet to be processed in the backlog.
- `numNewListedFiles`: Number of Delta Lake files listed to calculate the backlog for this batch.
- `backlogEndOffset`: The [[delta-lake-table|Delta Lake Table]] version used to calculate the backlog.

In a notebook, view these metrics under the **Raw Data** tab in the streaming query progress dashboard. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Idempotent Writes with `foreachBatch`

Delta Lake tables support the following `DataFrameWriter` options to make writes to multiple tables within `foreachBatch` idempotent: ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

- `txnAppId`: A unique string that you can pass on each DataFrame write. For example, you can use the StreamingQuery ID as `txnAppId`. `txnAppId` can be any user-generated unique string and does not have to be related to the stream ID.
- `txnVersion`: A monotonically increasing number that acts as transaction version.

Delta Lake uses `txnAppId` and `txnVersion` to identify and ignore duplicate writes. After a failure interrupts a batch write, you can re-run the batch with the same `txnAppId` and `txnVersion` to correctly identify and ignore duplicates. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

> **Warning:** If you delete the streaming checkpoint and restart the query with a new checkpoint, you must provide a different `txnAppId`. New checkpoints start with a batch ID of `0`. Delta Lake uses the batch ID and `txnAppId` as a unique key, and skips batches with already seen values. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

The following code example demonstrates this pattern: ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

```python
app_id = ... # A unique string that is used as an application ID.

def writeToDeltaLakeTableIdempotent(batch_df, batch_id):
  batch_df.write.format(...).option("txnVersion", batch_id).option("txnAppId", app_id).save(...) # location 1
  batch_df.write.format(...).option("txnVersion", batch_id).option("txnAppId", app_id).save(...) # location 2

streamingDF.writeStream.foreachBatch(writeToDeltaLakeTableIdempotent).start()
```

> **Note:** Databricks recommends configuring a separate streaming write for each sink you want to update instead of using `foreachBatch`. Writes to multiple sinks in `foreachBatch` reduces parallelization and increases overall latency because writes to multiple tables are serialized in `foreachBatch`. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Upsert from Streaming Queries Using `foreachBatch`

You can use `merge` and `foreachBatch` to write complex upserts from a streaming query into a [[delta-lake-table|Delta Lake Table]]. See foreachBatch for Arbitrary Data Sinks. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

This approach has many applications: ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

- Improve write performance with `update` output mode, whereas `complete` output mode requires rewriting the entire result table for each microbatch.
- Continuously apply a stream of changes to a [[delta-lake-table|Delta Lake Table]] by using a merge query to write change data in `foreachBatch`. See Slowly Changing Data (SCD) and Change Data Capture (CDC) with Delta Lake.
- Handle deduplication during stream processing. You can use an insert-only merge query in `foreachBatch` to continuously write data to a [[delta-lake-table|Delta Lake Table]] with automatic deduplication. See Data Deduplication When Writing into Delta Lake Tables.

> **Note:** Verify that your `merge` statement inside `foreachBatch` is idempotent. Otherwise, restarts of the streaming query can apply the operation on the same batch of data multiple times. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

For example, you can use `MERGE` SQL statements within `foreachBatch`: ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

```python
# Function to upsert microBatchOutputDF into [Delta Lake Table](/concepts/delta-lake-table.md) using merge
def upsertToDelta(microBatchOutputDF, batchId):
  # Set the dataframe to view name
  microBatchOutputDF.createOrReplaceTempView("updates")
  # Use the view name to apply MERGE
  # NOTE: You have to use the SparkSession that has been used to define the `updates` dataframe
  microBatchOutputDF.sparkSession.sql("""
    MERGE INTO aggregates t
    USING updates s
    ON s.key = t.key
    WHEN MATCHED THEN UPDATE SET *
    WHEN NOT MATCHED THEN INSERT *
  """)

# Write the output of a streaming aggregation query into [Delta Lake Table](/concepts/delta-lake-table.md)
streamingAggregatesDF.writeStream \
  .foreachBatch(upsertToDelta) \
  .outputMode("update") \
  .start()
```

## Related Concepts

- [Delta Lake as a Streaming Source](/concepts/delta-lake-as-a-streaming-source-and-sink.md) — Using Delta Lake tables as input for streaming queries
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) — The Spark framework for stream processing
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — The mechanism that guarantees exactly-once processing
- foreachBatch — The API for writing custom batch logic in streaming queries
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) — Row-level change tracking for Delta Lake tables
- Structured Streaming Triggers — Trigger modes for controlling stream execution
- Streaming Query Monitoring — Tools for tracking streaming query progress

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
