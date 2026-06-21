---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3012ef0909e9bd4e742e77bcf52eceaf53d813a5161efb5539b802023aef926a
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - foreachbatch-for-idempotent-and-upsert-writes
    - Upsert Writes and foreachBatch for Idempotent
    - FFIAUW
    - Use foreachBatch for idempotent table writes
    - foreachBatch for Idempotent and Upsert Writes#Idempotent Writes
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: foreachBatch for Idempotent and Upsert Writes
description: Using foreachBatch with txnAppId/txnVersion for idempotent writes to multiple Delta tables, and employing MERGE within foreachBatch for continuous upserts from streaming queries.
tags:
  - structured-streaming
  - delta-lake
  - merge
  - upsert
timestamp: "2026-06-19T18:20:57.985Z"
---

# foreachBatch for Idempotent and Upsert Writes

**foreachBatch for Idempotent and Upsert Writes** is a pattern in Spark Structured Streaming that allows you to apply custom batch processing logic, including idempotent writes and upserts, to each micro-batch output from a streaming query. This pattern is commonly used with [Delta Lake](/concepts/delta-lake.md) tables to achieve exactly-once semantics and handle complex data modification operations in streaming workflows.

## Idempotent Writes with `foreachBatch`

Delta Lake tables support `DataFrameWriter` options that make writes within `foreachBatch` idempotent, meaning duplicate writes are safely ignored. This is critical for handling streaming query restarts after failures. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

To implement idempotent writes, you pass two options on each DataFrame write:

- **`txnAppId`**: A unique string that identifies the application or streaming query. For example, you can use the `StreamingQuery` ID. `txnAppId` can be any user-generated unique string and does not have to be related to the stream ID.
- **`txnVersion`**: A monotonically increasing number that acts as a transaction version. Delta Lake uses `txnVersion` and `txnAppId` together to identify and ignore duplicate writes.

If a failure interrupts a batch write, re-running the batch with the same `txnAppId` and `txnVersion` correctly identifies and ignores duplicates.

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### Important Warning

If you delete the streaming checkpoint and restart the query with a new checkpoint, you must provide a different `txnAppId`. New checkpoints start with a batch ID of `0`. Delta Lake uses the batch ID and `txnAppId` as a unique key and skips batches with already seen values. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### Code Example

The following example demonstrates idempotent writes to multiple Delta Lake tables within `foreachBatch`:

```python
app_id = ... # A unique string used as an application ID.

def writeToDeltaLakeTableIdempotent(batch_df, batch_id):
    batch_df.write.format(...).option("txnVersion", batch_id).option("txnAppId", app_id).save(...) # location 1
    batch_df.write.format(...).option("txnVersion", batch_id).option("txnAppId", app_id).save(...) # location 2

streamingDF.writeStream.foreachBatch(writeToDeltaLakeTableIdempotent).start()
```

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Upsert from Streaming Queries Using `foreachBatch`

You can use Delta Lake merge (`MERGE` statement) inside `foreachBatch` to write complex upserts from a streaming query into a [Delta Lake Table](/concepts/delta-lake-table.md). This approach has several applications:

- Improve write performance with `update` output mode (whereas `complete` output mode requires rewriting the entire result table for each micro-batch).
- Continuously apply a stream of changes to a [Delta Lake Table](/concepts/delta-lake-table.md) using a merge query.
- Handle deduplication during stream processing using an insert-only merge query.

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### Important Considerations

- Verify that your `MERGE` statement inside `foreachBatch` is idempotent. Otherwise, restarts of the streaming query can apply the operation on the same batch of data multiple times. See [foreachBatch for Idempotent and Upsert Writes#Idempotent Writes](/concepts/foreachbatch-for-idempotent-and-upsert-writes.md).
- When `MERGE` is used in `foreachBatch`, the input data rate metric might return a multiple of the actual rate. `MERGE` reads input data multiple times, which multiplies the metrics. To prevent metric multiplication, cache the batch DataFrame before `MERGE` and then uncache it after `MERGE`.

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### SQL-Based Example

The following example uses `MERGE` SQL statements within `foreachBatch`:

```scala
def upsertToDelta(microBatchOutputDF: DataFrame, batchId: Long) {
    microBatchOutputDF.createOrReplaceTempView("updates")
    microBatchOutputDF.sparkSession.sql(s"""
        MERGE INTO aggregates t
        USING updates s
        ON s.key = t.key
        WHEN MATCHED THEN UPDATE SET *
        WHEN NOT MATCHED THEN INSERT *
    """)
}

streamingAggregatesDF.writeStream
    .foreachBatch(upsertToDelta _)
    .outputMode("update")
    .start()
```

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### Delta Lake API Example

You can also use the Delta Lake APIs for streaming upserts:

```scala
import io.delta.tables._

val deltaTable = DeltaTable.forName(spark, "table_name")

def upsertToDelta(microBatchOutputDF: DataFrame, batchId: Long) {
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

## Performance Consideration

Databricks recommends configuring a separate streaming write for each sink you want to update, rather than using `foreachBatch` for writing to multiple sinks. Writes to multiple sinks in `foreachBatch` reduces parallelization and increases overall latency because writes to multiple tables are serialized. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Related Concepts

- Delta Lake merge — The upsert operation used within `foreachBatch` for change data capture.
- Change Data Capture (CDC) — A use case for streaming upserts with Delta Lake.
- Spark Structured Streaming — The streaming framework that provides `foreachBatch`.
- Data deduplication — An application of insert-only merge in `foreachBatch`.
- Streaming checkpoints — Checkpoint management considerations for idempotent writes.
- Slowly Changing Data (SCD) — A pattern implemented using streaming upserts.

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
