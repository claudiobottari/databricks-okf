---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4791a56b8cd394bfecc91d0c5804057fb32411ece41c3642f29b013d76171c81
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - idempotent-writes-with-foreachbatch-and-transaction-identifiers
    - Transaction Identifiers and Idempotent Writes with foreachBatch
    - IWWFATI
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: Idempotent Writes with foreachBatch and Transaction Identifiers
description: Using txnAppId and txnVersion options with foreachBatch to make multi-table writes idempotent, allowing safe retry after failures without duplicating data.
tags:
  - streaming
  - delta-lake
  - structured-streaming
timestamp: "2026-06-18T11:48:58.682Z"
---

# Idempotent Writes with `foreachBatch` and Transaction Identifiers

**Idempotent Writes with `foreachBatch` and Transaction Identifiers** is a pattern that uses Delta Lake’s `txnAppId` and `txnVersion` options inside the `foreachBatch` sink to guarantee that each micro-batch is written exactly once, even when failures cause the same batch to be replayed. This prevents duplicate records when a streaming query restarts after an interruption. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Overview

When a [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) query writes to a [Delta Lake](/concepts/delta-lake.md) table using `foreachBatch`, the underlying micro-batch may be re-executed if the query fails and resumes from a checkpoint. Without an idempotent write mechanism, the same data could be written multiple times, producing duplicates. Delta Lake provides two `DataFrameWriter` options — `txnAppId` and `txnVersion` — that allow `foreachBatch` writers to record a unique transaction identifier for each batch. Delta Lake uses these identifiers to detect and skip already-processed batches, making the write idempotent. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## How It Works

The idempotent write mechanism relies on two options:

* **`txnAppId`**: A user-defined string that uniquely identifies the application or streaming query. For example, you can use the streaming query’s ID (`StreamingQuery.id`) or any globally unique string. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]
* **`txnVersion`**: A monotonically increasing number that acts as a transaction version. The batch ID (provided as the second argument to the `foreachBatch` function) is a natural choice because it increments sequentially for each micro-batch. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

When writing, Delta Lake stores a record of the `(txnAppId, txnVersion)` pair. If the same pair is submitted again (e.g., because a failure caused the same batch to be re-processed), Delta Lake ignores the write, ensuring exactly-once semantics. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Example

The following code demonstrates how to apply `txnAppId` and `txnVersion` to make writes to multiple Delta Lake tables idempotent within a `foreachBatch` callback:

```python
app_id = ...  # A unique string used as an application ID, e.g., streamingQuery.id

def writeToDeltaLakeTableIdempotent(batch_df, batch_id):
    batch_df.write \
        .format("delta") \
        .option("txnVersion", batch_id) \
        .option("txnAppId", app_id) \
        .save("/path/to/location1")

    batch_df.write \
        .format("delta") \
        .option("txnVersion", batch_id) \
        .option("txnAppId", app_id) \
        .save("/path/to/location2")

streamingDF.writeStream \
    .foreachBatch(writeToDeltaLakeTableIdempotent) \
    .start()
```

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Important Considerations

### Checkpoint Resets Require a New `txnAppId`

If you delete the streaming checkpoint and restart the query with a new checkpoint, you **must** provide a different `txnAppId`. A new checkpoint starts with batch ID `0`, which may conflict with previously recorded `(txnAppId, txnVersion)` pairs. Using a new `txnAppId` prevents Delta Lake from incorrectly skipping batches that should be reprocessed. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### Alternative Approach: Separate Streaming Sinks

For most use cases, Databricks recommends configuring a separate streaming write for each sink instead of using `foreachBatch` to write to multiple tables. Multiple writes inside `foreachBatch` are serialized, which reduces parallelism and can increase latency. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Related Concepts

- foreachBatch — The streaming sink that applies a custom function to each micro-batch
- [Delta Lake](/concepts/delta-lake.md) — The storage layer providing transactional guarantees
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) — The stream processing engine on Spark
- Spark Structured Streaming Checkpoints — Mechanism for fault tolerance and exactly-once delivery
- Duplicate Data Deduplication — Strategies for removing duplicates in streaming pipelines

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
