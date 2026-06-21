---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cff49a67cb6d475eda92b1e111add19de8c996856702b351c28a2513cc80e6ef
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - upsert-from-streaming-queries-using-foreachbatch-and-merge
    - MERGE and Upsert from Streaming Queries using foreachBatch
    - UFSQUFAM
    - Upsert from streaming queries using foreachBatch
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: Upsert from Streaming Queries using foreachBatch and MERGE
description: Combining foreachBatch with Delta Lake MERGE operations to perform upserts (inserts and updates) from streaming queries, enabling SCD/CDC patterns and deduplication.
tags:
  - streaming
  - delta-lake
  - structured-streaming
timestamp: "2026-06-18T11:49:13.138Z"
---

# Upsert from Streaming Queries using foreachBatch and MERGE

**Upsert from Streaming Queries using `foreachBatch` and `MERGE`** is a pattern in [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) that allows you to continuously apply upserts (insert-or-update logic) from a streaming micro-batch into a [Delta Lake](/concepts/delta-lake.md) table. By combining the `foreachBatch` sink with a `MERGE` statement, you can write complex stateful operations that are not directly supported by the built-in streaming output modes. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Overview

The standard `append` and `complete` output modes for streaming queries have limitations. `append` only adds new rows; `complete` replaces the entire result table every micro-batch, which is expensive for large aggregations. Using `foreachBatch`, you can execute arbitrary DataFrame operations on each micro-batch, including a `MERGE` (also known as an upsert) into a [Delta Lake Table](/concepts/delta-lake-table.md). This approach lets you maintain a target table that is continuously updated with the latest changes from the stream. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## How it Works

Inside the `foreachBatch` function, you create a temporary view of the micro-batch DataFrame and then issue a `MERGE` SQL statement. Alternatively, you can use the Delta Lake API (`DeltaTable.merge()`). The merge condition typically matches on a key column: when a match is found, the existing row is updated; when no match is found, a new row is inserted. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### Example using SQL

```scala
def upsertToDelta(microBatchOutputDF: DataFrame, batchId: Long): Unit = {
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

### Example using Delta Lake API

```scala
import io.delta.tables._

val deltaTable = DeltaTable.forName(spark, "table_name")

def upsertToDelta(microBatchOutputDF: DataFrame, batchId: Long): Unit = {
  deltaTable.as("t")
    .merge(microBatchOutputDF.as("s"), "s.key = t.key")
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

## Applications

The pattern supports several common use cases: ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

- **Improve write performance with `update` output mode** – instead of rewriting the entire aggregation result each batch (as `complete` mode does), you only apply the incremental changes via merge, reducing I/O and cost.
- **Slowly Changing Data (SCD) and Change Data Capture (CDC)** – you can continuously apply a stream of changes (inserts, updates, deletes) to a [Delta Lake Table](/concepts/delta-lake-table.md) using a merge query inside `foreachBatch`. For details, see Slowly changing data and change data capture with Delta Lake.
- **Deduplication** – you can use an insert-only merge (e.g., `WHEN NOT MATCHED THEN INSERT`) inside `foreachBatch` to continuously write data to a [Delta Lake Table](/concepts/delta-lake-table.md) with automatic deduplication, since the merge condition prevents inserting duplicate rows. See Data deduplication when writing into Delta Lake tables.

## Idempotency Considerations

The `merge` statement inside `foreachBatch` must be idempotent. If the streaming query restarts after a failure, the same batch may be reprocessed. Without idempotency, the merge could apply the same changes multiple times, leading to incorrect results. To make the write idempotent, you can use the `txnAppId` and `txnVersion` options on the DataFrame write inside `foreachBatch`. For a full discussion, see [Use foreachBatch for idempotent table writes](/concepts/foreachbatch-for-idempotent-and-upsert-writes.md). ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Metric Multiplication

When `merge` is used inside `foreachBatch`, the input data rate metric reported by Structured Streaming may return a multiple of the actual source rate. This happens because `merge` reads input data multiple times (once for the join/condition evaluation). To prevent metric multiplication, cache the batch DataFrame before executing the merge and uncache it afterward. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Best Practices

- **Cache the batch DataFrame** – as noted, this avoids skewing streaming progress metrics.
- **Use `outputMode("update")`** – this output mode works naturally with merge because only updated or inserted rows need to be passed to foreachBatch; the stream does not need to maintain a complete result state.
- **Consider using multiple separate streams** – Databricks recommends configuring a separate streaming write for each sink rather than writing to multiple tables inside a single `foreachBatch`, because doing so serializes the writes and reduces parallelism. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Related Concepts

- foreachBatch – The sink that enables custom per-batch logic in Structured Streaming.
- [MERGE INTO](/concepts/merge-into-delta-lake.md) – The Delta Lake SQL command for upsert operations.
- [Delta Lake](/concepts/delta-lake.md) – The ACID storage layer that supports merge operations.
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) – The stream processing engine in Apache Spark.
- Change Data Capture (CDC) – Using merge in foreachBatch to apply change streams.
- Data Deduplication – Using insert-only merge for deduplication.
- Idempotent Writes – Techniques for ensuring exactly-once semantics in streaming.

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
