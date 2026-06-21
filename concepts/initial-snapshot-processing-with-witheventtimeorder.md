---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 488a3daab60f7c49a60e98482ae4c8fc80d22badffd50d5c9658b5f5aa41e4d3
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - initial-snapshot-processing-with-witheventtimeorder
    - ISPWW
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: Initial snapshot processing with withEventTimeOrder
description: Feature to prevent data drops during initial Delta snapshot processing in stateful streaming queries by ordering data by event time into time-bucketed micro-batches.
tags:
  - streaming
  - delta-lake
  - watermark
timestamp: "2026-06-19T10:00:31.870Z"
---

# Initial Snapshot Processing with `withEventTimeOrder`

**Initial snapshot processing with `withEventTimeOrder`** is an option available in Databricks Runtime 11.3 LTS and above that prevents data loss during the initial snapshot phase of a stateful streaming query reading from a [Delta Lake](/concepts/delta-lake.md) source. It ensures that records are not incorrectly dropped as late events when the file modification order does not match the event-time order. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Problem

In a stateful streaming query that uses a defined watermark, the default behavior processes the initial snapshot (all data present in the Delta table when the stream starts) based on the **last modification time** of each data file. Because file modification times do not necessarily reflect the actual event time of the records inside the files, the watermark may incorrectly classify records as “late” and drop them. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## How It Works

When `withEventTimeOrder` is enabled, the streaming query divides the event time range of the initial snapshot data into time buckets. Each micro-batch processes one bucket by filtering the data within that bucket’s time range. The existing rate‑limiting options `maxFilesPerTrigger` and `maxBytesPerTrigger` still apply, but only approximately because of the time‑bucket‑based processing approach. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

The following diagram illustrates the process (image from the Databricks documentation):

![Initial Snapshot processing with withEventTimeOrder](https://docs.databricks.com/aws/en/assets/images/delta-initial-snapshot-data-drop-22bccd2312254a9f9e853389e49f13eb.png)

## Constraints

- You **cannot** change the `withEventTimeOrder` setting after the streaming query has started and the initial snapshot is actively being processed. To change it, delete the checkpoint and restart the query. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]
- You **cannot** downgrade the stream to a Databricks Runtime version that does not support this feature until the initial snapshot processing has completed. To downgrade, either wait for completion or delete the checkpoint and restart. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]
- The feature is **not supported** in the following scenarios:
  - The event time column is a generated column and there are non‑projection transformations between the Delta source and the watermark.
  - The stream query contains more than one Delta source with a watermark. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Performance Considerations

Enabling `withEventTimeOrder` can slow down initial snapshot processing because each micro‑batch must scan the snapshot to filter data within the corresponding event time bucket. To improve filtering performance:

- Use a Delta source column as the event time column so that data skipping can be applied.
- Partition the table along the event time column.

Use the Spark UI to inspect how many Delta files are scanned for a specific micro‑batch. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Example

The following Scala example reads from a Delta table `user_events` with an `event_time` column and enables `withEventTimeOrder`:

```scala
spark.readStream
  .option("withEventTimeOrder", "true")
  .table("user_events")
  .withWatermark("event_time", "10 seconds")
```

To apply the setting cluster‑wide (for all streaming queries), set the Spark configuration:

```conf
spark.databricks.delta.withEventTimeOrder.enabled true
```

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Related Concepts

- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md)
- [Delta Lake streaming reads and writes](/concepts/delta-lake-as-a-streaming-source-and-sink.md)
- Watermark in Structured Streaming
- Stateful streaming queries
- [Event time processing](/concepts/event-time-ordered-initial-snapshot-processing.md)
- Data skipping
- [Setting initial table version for streaming](/concepts/initial-table-version-for-delta-streaming.md)

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
