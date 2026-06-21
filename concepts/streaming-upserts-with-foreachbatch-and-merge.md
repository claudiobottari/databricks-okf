---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ca1b846345868750f5e72ebf3f4890ac7011b9175045bd17932b3a5b6a8a76cb
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - streaming-upserts-with-foreachbatch-and-merge
    - MERGE and Streaming Upserts with foreachBatch
    - SUWFAM
    - Streaming foreachBatch
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: Streaming Upserts with foreachBatch and MERGE
description: Using MERGE operations inside foreachBatch to continuously apply streaming changes (upserts) to Delta Lake tables with idempotency guarantees
tags:
  - delta-lake
  - streaming
  - upsert
  - cdc
timestamp: "2026-06-19T15:00:02.265Z"
---

```markdown
---
title: Streaming upserts with foreachBatch and MERGE
summary: Using merge operations inside foreachBatch to perform complex upserts from streaming queries into Delta tables, enabling SCD/CDC patterns and deduplication.
sources:
  - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T15:16:10.817Z"
updatedAt: "2026-06-19T10:00:48.470Z"
tags:
  - streaming
  - delta-lake
  - upsert
  - merge
aliases:
  - streaming-upserts-with-foreachbatch-and-merge
  - MERGE and Streaming upserts with foreachBatch
  - SUWFAM
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Streaming Upserts with `foreachBatch` and MERGE

**Streaming Upserts with `foreachBatch` and MERGE** is a pattern for applying change data capture (CDC) or upsert operations from a Spark Structured Streaming query into a [[Delta Lake]] table. By combining the `foreachBatch` sink with a Delta Lake `MERGE` statement, you can handle inserts, updates, and deletes within each micro‑batch, avoiding the full table rewrite required by `complete` output mode. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Overview

The standard streaming sink writes only appends. For use cases that require updating or deleting existing rows — such as Slowly Changing Data (SCD) or Change Data Capture (CDC) — you can use `foreachBatch` to call a `MERGE` statement for every micro‑batch. This approach also supports deduplication because an insert‑only merge can skip rows that already exist. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## How It Works

1. **Write a function** that receives the micro‑batch `DataFrame` and the batch ID.
2. Inside the function, register the `DataFrame` as a temporary view or use the Delta Lake API.
3. Execute a `MERGE` statement that upserts the micro‑batch into the target Delta table.
4. Pass the function to `writeStream.foreachBatch()`.

Because `foreachBatch` can be restarted, the `MERGE` operation must be **idempotent**. Delta Lake supports this by using the `txnAppId` and `txnVersion` options on each write, which allow Delta to detect and skip duplicate batch writes. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Example

The following Scala example uses the Delta Lake API to upsert streaming aggregation results into a table:

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

The same pattern can be expressed with SQL by creating a temporary view from the micro‑batch:

```scala
def upsertToDelta(microBatchOutputDF: DataFrame, batchId: Long): Unit = {
  microBatchOutputDF.createOrReplaceTempView("updates")
  microBatchOutputDF.sparkSession.sql(
    """MERGE INTO aggregates t
      USING updates s
      ON s.key = t.key
      WHEN MATCHED THEN UPDATE SET *
      WHEN NOT MATCHED THEN INSERT *""")
}
```

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Important Considerations

### Idempotency

Restarts of the streaming query can re‑run a batch. To prevent duplicate upserts, always use the `txnAppId` and `txnVersion` options when writing inside `foreachBatch`:

```scala
batchDF.write
  .format("delta")
  .option("txnAppId", appId)
  .option("txnVersion", batchId)
  .save("/path/to/target")
```

If the checkpoint is deleted and the query restarted, you **must** change the `txnAppId` to a new value; otherwise Delta may incorrectly skip valid batches. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### Metric Multiplication and Caching

When `MERGE` is used inside `foreachBatch`, the input data rate metric reported by `StreamingQueryProgress` can be a multiple of the actual source rate because `MERGE` reads the input data multiple times. To prevent this, **cache** the batch `DataFrame` before the merge and uncache it afterwards:

```scala
def upsertToDelta(batchDF: DataFrame, batchId: Long): Unit = {
  batchDF.cache()
  // perform merge
  batchDF.unpersist()
}
```

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### Use a Dedicated Stream per Sink

Databricks recommends configuring a separate streaming write for each sink rather than writing to multiple tables inside a single `foreachBatch`. Writes to multiple sinks within `foreachBatch` are serialized, reducing parallelism and increasing latency. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Use Cases

- **Slowly Changing Data (SCD) and CDC** – Continuously apply a stream of changes to a Delta table using merge.  
- **Deduplication** – Use an insert‑only merge (e.g., `WHEN NOT MATCHED THEN INSERT`) to automatically skip duplicate records.  

Both patterns are documented in Delta Lake’s MERGE documentation. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Related Concepts

- [[Idempotent foreachBatch Writes|foreachBatch sink]] – The general pattern for custom processing of streaming micro‑batches.
- Delta Lake MERGE – The SQL and API syntax for upserts, deletes, and updates.
- [[Delta Change Data Feed (CDF)|Change Data Feed]] – Stream all row‑level changes including updates and deletes.
- Streaming Deduplication – Deduplicating data streams with `dropDuplicates` or merge.
- [[Idempotent foreachBatch Writes|Idempotent Writes in Delta]] – Using `txnAppId` and `txnVersion` for exactly‑once semantics.

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
```

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
