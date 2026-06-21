---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3e01b2f264c4867f72956e8368f01516640b25f2950abe7a414609e4fb41f8e9
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - idempotent-writes-with-foreachbatch-using-txnappid-and-txnversion
    - txnVersion and Idempotent writes with foreachBatch using txnAppId
    - IWWFUTAT
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: Idempotent writes with foreachBatch using txnAppId and txnVersion
description: Pattern for idempotent multi-sink writes within foreachBatch using Delta Lake's transaction app ID and version to identify and ignore duplicate writes after failures.
tags:
  - streaming
  - delta-lake
  - exactly-once
timestamp: "2026-06-19T10:00:37.927Z"
---

# Idempotent Writes with `foreachBatch` Using `txnAppId` and `txnVersion`

**Idempotent writes with `foreachBatch` using `txnAppId` and `txnVersion`** refers to a pattern in Spark Structured Streaming that allows a streaming query to write the same micro-batch to one or more [Delta Lake](/concepts/delta-lake.md) tables safely, without risk of data duplication when the batch is retried after a failure. This is achieved by passing two special DataFrame writer options—`txnAppId` and `txnVersion`—to each write operation inside the `foreachBatch` callback.

## Overview

When a streaming query uses `foreachBatch` to write to multiple sinks, Databricks recommends configuring a separate streaming query for each sink instead of using `foreachBatch`, because `foreachBatch` serializes writes and increases latency. However, when `foreachBatch` is necessary, Delta Lake provides the `txnAppId` and `txnVersion` options to make writes idempotent.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

- **`txnAppId`** – A unique string that identifies the application or streaming query. It can be any user-generated unique string; for example, the StreamingQuery ID can be used.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]
- **`txnVersion`** – A monotonically increasing number that acts as a transaction version. In the `foreachBatch` callback, the `batchId` parameter is a natural choice.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

Delta Lake uses the combination of `txnAppId` and `txnVersion` as a unique key to detect and ignore duplicate writes. After a failure interrupts a batch write, re-running the batch with the same values ensures that any partially‑written data is not duplicated.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Usage

The following code example demonstrates writing the same micro‑batch to two Delta Lake locations idempotently:

```python
app_id = ... # A unique string used as an application ID.

def writeToDeltaLakeTableIdempotent(batch_df, batch_id):
    batch_df.write.format(...).option("txnVersion", batch_id)\
        .option("txnAppId", app_id).save(...) # location 1
    batch_df.write.format(...).option("txnVersion", batch_id)\
        .option("txnAppId", app_id).save(...) # location 2

streamingDF.writeStream.foreachBatch(writeToDeltaLakeTableIdempotent).start()
```

In this pattern, every batch write carries the same `txnAppId` and the batch’s unique `batch_id` as the version. If a write fails and is retried, Delta Lake checks whether a transaction with the same (`txnAppId`, `txnVersion`) already exists and silently skips the duplicate.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Important Considerations

- **Checkpoint deletion** – If you delete the streaming checkpoint and restart the query with a new checkpoint, you **must** provide a different `txnAppId`. This is because new checkpoints start with a batch ID of `0`, and Delta Lake uses the (`batchId`, `txnAppId`) pair as a unique key. If the same `txnAppId` and batch ID pair has already been recorded, the write is incorrectly skipped.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]
- **Upsert patterns** – When using `foreachBatch` for upserts with merge, ensure that the merge statement itself is idempotent. Restarts of the streaming query can re‑apply the same batch of data; `txnAppId` and `txnVersion` protect the batch‑level commit, but the merge logic must also handle re‑execution safely. See Upsert from streaming queries using foreachBatch.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Related Concepts

- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) – The underlying streaming engine.
- [Delta Lake table streaming reads and writes](/concepts/delta-lake-as-a-streaming-source-and-sink.md) – Broad guide on streaming with Delta Lake.
- foreachBatch – The `DataStreamWriter` method for custom micro‑batch sinks.
- Streaming checkpoint – Location where stream progress is recorded.
- Exactly-once processing – The guarantee that `txnAppId`/`txnVersion` helps enforce.
- Upsert from streaming queries using foreachBatch – How to combine `merge` with `foreachBatch`.

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
