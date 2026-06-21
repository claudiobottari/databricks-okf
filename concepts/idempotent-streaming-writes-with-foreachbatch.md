---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3804c72402bb79d489696dc539a767c890541aa46690e38dbde32093f8c982c2
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - idempotent-streaming-writes-with-foreachbatch
    - ISWWF
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: Idempotent Streaming Writes with foreachBatch
description: Using txnAppId and txnVersion to make foreachBatch writes idempotent when writing to Delta Lake from streams
tags:
  - streaming
  - delta-lake
  - idempotency
timestamp: "2026-06-18T15:15:33.073Z"
---

# Idempotent Streaming Writes with foreachBatch

**Idempotent Streaming Writes with foreachBatch** is a pattern for safely writing streaming data to multiple sinks from a single Spark Structured Streaming query using the `foreachBatch` sink. By making writes idempotent — meaning repeated executions of the same batch produce the same result without duplicating data — you can recover from failures without data corruption or duplication.

## Overview

The `foreachBatch` operation in Spark Structured Streaming allows you to apply arbitrary DataFrame operations on the output of each micro-batch. When writing to multiple sinks from within `foreachBatch`, writes are serialized, which can increase latency. For this reason, Databricks recommends configuring a separate streaming write for each sink instead of using `foreachBatch` when possible. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

However, when `foreachBatch` is necessary — for example, when you need to write to multiple Delta Lake tables or apply custom transformations per sink — you must ensure writes are idempotent to handle failure and restart scenarios correctly. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## How Idempotent Writes Work

Delta Lake provides two DataFrameWriter options to make writes within `foreachBatch` idempotent: ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

- **`txnAppId`**: A unique string that identifies the application or streaming query. For example, you can use the StreamingQuery ID as `txnAppId`. This can be any user-generated unique string and does not have to be related to the stream ID. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]
- **`txnVersion`**: A monotonically increasing number that acts as a transaction version. Typically, you use the `batchId` provided by `foreachBatch`. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

Delta Lake uses the combination of `txnAppId` and `txnVersion` to identify and ignore duplicate writes. If a failure interrupts a batch write, re-running the batch with the same `txnAppId` and `txnVersion` correctly identifies the duplicates and skips them. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Implementing Idempotent Writes

The following code example demonstrates the pattern for idempotent writes to multiple locations: ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

```python
app_id = ... # A unique string used as an application ID.

def writeToDeltaLakeTableIdempotent(batch_df, batch_id):
  batch_df.write.format(...).option("txnVersion", batch_id).option("txnAppId", app_id).save(...) # location 1
  batch_df.write.format(...).option("txnVersion", batch_id).option("txnAppId", app_id).save(...) # location 2

streamingDF.writeStream.foreachBatch(writeToDeltaLakeTableIdempotent).start()
```

In this pattern, each write call passes the same `txnAppId` and `txnVersion` (the `batch_id`). If the query fails mid-batch and restarts, the same batch ID is used, allowing Delta Lake to recognize and skip the already-written data. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Important Considerations

### Checkpoint Restarts

If you delete the streaming checkpoint and restart the query with a new checkpoint, you **must** provide a different `txnAppId`. New checkpoints start with a batch ID of `0`. Delta Lake uses the batch ID and `txnAppId` as a unique key and skips batches with already seen values. Using the same `txnAppId` with a new checkpoint would cause the first batch (batch ID `0`) to be incorrectly skipped. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### Upsert Operations in foreachBatch

When using Merge statements inside `foreachBatch` for upserts, you must verify that the merge operation itself is idempotent. Otherwise, restarts of the streaming query can apply the operation on the same batch of data multiple times. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### Metric Multipliation

When using `merge` in `foreachBatch`, the input data rate metric might return a multiple of the actual rate at which data is generated at the source. This occurs because `merge` reads input data multiple times, which multiplies the metrics. To prevent metric multiplication, cache the batch DataFrame before the `merge` operation and uncache it after. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### Performance Implications

Writes to multiple sinks within `foreachBatch` are serialized, which reduces parallelization and increases overall latency. Each target sink is written sequentially within the same micro-batch processing, so if you need to update multiple sinks, evaluate whether separate streaming queries for each sink would provide better performance. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Related Concepts

- [ForeachBatch Sink](/concepts/idempotent-foreachbatch-writes.md) — The general mechanism for applying custom logic per micro-batch
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — How Delta Lake tracks writes and ensures atomicity
- Streaming Checkpoints — How Structured Streaming tracks progress for recovery
- [MERGE INTO (Delta Lake)](/concepts/merge-into-delta-lake.md) — Using upsert operations in streaming workflows
- Change Data Capture with Delta Lake — Processing row-level changes from streaming sources
- Spark Structured Streaming — The underlying streaming engine

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
