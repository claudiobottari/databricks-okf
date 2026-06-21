---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8d562eb3f578b4b7e7b3d88daee708c71eaf5730da31abcf83b0e1a0a21f7b20
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - idempotent-foreachbatch-writes
    - IFW
    - ForeachBatch
    - ForeachBatch Sink
    - Idempotent Writes in Delta
    - foreachBatch sink
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: Idempotent foreachBatch Writes
description: Pattern using txnAppId and txnVersion to make writes to multiple sinks within foreachBatch idempotent, preventing duplicate writes on failure recovery
tags:
  - delta-lake
  - streaming
  - exactly-once
  - structured-streaming
timestamp: "2026-06-19T14:59:49.734Z"
---

# Idempotent foreachBatch Writes

**Idempotent foreachBatch Writes** is a pattern for writing data from Spark Structured Streaming queries to multiple [Delta Lake](/concepts/delta-lake.md) tables within a `foreachBatch` operation while guaranteeing that duplicate writes are safely ignored. This pattern is essential for maintaining exactly-once semantics when a streaming query restarts after a failure.

## Overview

When using `foreachBatch` to write to multiple sinks, a batch may be re-executed after a failure. Without idempotency guarantees, this can result in duplicate data being written to downstream tables. Delta Lake provides built-in support for idempotent writes through transaction identifiers that allow the system to detect and skip already-processed batches. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Transaction Identifiers

Delta Lake supports two `DataFrameWriter` options to make writes within `foreachBatch` idempotent: ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

- **`txnAppId`**: A unique string that identifies the application or streaming query. For example, you can use the `StreamingQuery` ID as the `txnAppId`. This value can be any user-generated unique string and does not have to be related to the stream ID. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]
- **`txnVersion`**: A monotonically increasing number that acts as a transaction version. Typically, you use the streaming batch ID for this value. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

Delta Lake uses the combination of `txnAppId` and `txnVersion` to identify and ignore duplicate writes. After a failure interrupts a batch write, re-running the batch with the same `txnAppId` and `txnVersion` correctly identifies and skips duplicates. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Implementation

The following code example demonstrates the idempotent write pattern: ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

```python
app_id = ... # A unique string that is used as an application ID.

def writeToDeltaLakeTableIdempotent(batch_df, batch_id):
  batch_df.write.format(...).option("txnVersion", batch_id).option("txnAppId", app_id).save(...) # location 1
  batch_df.write.format(...).option("txnVersion", batch_id).option("txnAppId", app_id).save(...) # location 2

streamingDF.writeStream.foreachBatch(writeToDeltaLakeTableIdempotent).start()
```

## Important Considerations

### Checkpoint Restarts

If you delete the streaming checkpoint and restart the query with a new checkpoint, you must provide a different `txnAppId`. New checkpoints start with a batch ID of `0`. Delta Lake uses the batch ID and `txnAppId` as a unique key and skips batches with already-seen values. Using the same `txnAppId` after a checkpoint reset would cause the system to incorrectly skip the first batch of the new query. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### Alternative Recommendation

Databricks recommends configuring a separate streaming write for each sink instead of using `foreachBatch`. Writes to multiple sinks in `foreachBatch` reduce parallelization and increase overall latency because writes to multiple tables are serialized within the `foreachBatch` operation. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Related Concepts

- [Delta Lake table streaming reads and writes](/concepts/delta-lake-as-a-streaming-source-and-sink.md) — General guidance on using Delta Lake with Structured Streaming
- foreachBatch — The mechanism for applying arbitrary operations to streaming micro-batches
- Structured Streaming checkpointing — How checkpoints track streaming progress
- Exactly-once semantics in Delta Lake — How Delta Lake guarantees exactly-once processing
- Upsert from streaming queries using foreachBatch — Using merge operations within foreachBatch

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
