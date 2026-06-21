---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b870f1cd7d7e05fd31d405136096bd6eccf9b4869dbd38194290404b88c3e4e8
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-streaming-sink-modes
    - DLSSM
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: Delta Lake Streaming Sink Modes
description: Using Delta Lake tables as streaming sinks with append mode (adding new records) and complete mode (replacing the entire table each batch)
tags:
  - delta-lake
  - streaming
  - structured-streaming
timestamp: "2026-06-19T14:59:59.989Z"
---

# Delta Lake Streaming Sink Modes

**Delta Lake Streaming Sink Modes** refer to the output modes available when using a [Delta Lake](/concepts/delta-lake.md) table as the destination for a Spark Structured Streaming query. Delta Lake’s transaction log guarantees exactly-once processing, even when other streams or batch queries run concurrently against the same table. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

When writing to a [Delta Lake Table](/concepts/delta-lake-table.md) via `writeStream`, you may observe empty commits with `epochId = -1`. These are expected and occur on the first batch of each streaming query run (or every batch with `Trigger.AvailableNow`) and when a schema is changed. They do not affect correctness or performance. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

The Delta Lake `VACUUM` function removes files not managed by Delta Lake but skips directories beginning with `_`. You can safely store checkpoints alongside table data using a directory structure like `<table-name>/_checkpoints`. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Append Mode

**Append mode** is the default output mode. It adds only new records to the table in each micro‑batch. The typical usage is:

```python
(events.writeStream
   .outputMode("append")
   .option("checkpointLocation", "/tmp/delta/events/_checkpoints/")
   .toTable("events"))
```

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

The `toTable` method is the recommended way to stream to a [Delta Lake Table](/concepts/delta-lake-table.md).

## Complete Mode

**Complete mode** replaces the entire table after every batch. It is used when you want to continuously rewrite an aggregated summary. For example:

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

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

For applications without strict latency requirements, you can use one‑time triggers such as `AvailableNow` to save resources. See Structured Streaming triggers. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Using `foreachBatch` for Upserts

The `foreachBatch` operation allows you to apply custom logic per micro‑batch. This is commonly used to perform upserts via `MERGE INTO` on a [Delta Lake Table](/concepts/delta-lake-table.md), enabling you to continuously apply changes from a stream.

Databricks recommends configuring a separate streaming write for each sink rather than using `foreachBatch` for multiple sinks, because serialized writes within `foreachBatch` reduce parallelization and increase latency. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

Example using Delta Lake’s `merge` API:

```scala
import io.delta.tables._

val deltaTable = DeltaTable.forName(spark, "table_name")

def upsertToDelta(microBatchOutputDF: DataFrame, batchId: Long): Unit = {
  deltaTable.as("t")
    .merge(
      microBatchOutputDF.as("s"),
      "s.key = t.key")
    .whenMatched().updateAll()
    .whenNotMatched().insertAll()
    .execute()
}

streamingAggregatesDF.writeStream
  .foreachBatch(upsertToDelta _)
  .outputMode("update")
  .start()
```

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

When using `merge` inside `foreachBatch`, the input data rate metric may be multiplied because `merge` reads input data multiple times. Cache the batch DataFrame before `merge` and uncache afterwards to prevent this. The merge statement must be idempotent to handle restarts correctly. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Idempotent Writes with `foreachBatch`

Delta Lake provides two options to make `foreachBatch` writes idempotent:

- **`txnAppId`**: A unique string identifying the application (e.g., the `StreamingQuery` ID).
- **`txnVersion`**: A monotonically increasing number (e.g., the batch ID).

Delta Lake uses these together to detect and ignore duplicate writes. If a checkpoint is deleted and the query restarts with a new checkpoint, you must provide a different `txnAppId`. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

Example:

```python
app_id = ...  # unique string

def writeToDeltaLakeTableIdempotent(batch_df, batch_id):
    batch_df.write.format(...) \
        .option("txnVersion", batch_id) \
        .option("txnAppId", app_id) \
        .save(...)

streamingDF.writeStream.foreachBatch(writeToDeltaLakeTableIdempotent).start()
```

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Table](/concepts/delta-lake-table.md)
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md)
- foreachBatch
- [MERGE INTO](/concepts/merge-into-delta-lake.md)
- Idempotent write
- txnAppId and txnVersion
- Checkpoint location
- VACUUM
- [Change data feed](/concepts/delta-change-data-feed-cdf.md)
- [Materialized views](/concepts/materialized-views-in-databricks.md)

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
