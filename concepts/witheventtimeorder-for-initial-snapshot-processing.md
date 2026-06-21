---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5e310984373fcd861398bbbe72c82c6359d3e0c3b485b9a5a6ec0d4bc240502e
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - witheventtimeorder-for-initial-snapshot-processing
    - WFISP
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: withEventTimeOrder for Initial Snapshot Processing
description: Feature to avoid data drops during initial snapshot processing by ordering data by event time instead of file modification time, using time bucket filtering.
tags:
  - structured-streaming
  - delta-lake
  - watermark
  - exactly-once
timestamp: "2026-06-19T18:20:50.653Z"
---

# withEventTimeOrder for Initial Snapshot Processing

**withEventTimeOrder** is a Delta Lake streaming option that prevents data loss during the initial snapshot processing of a stateful streaming query. When enabled, it processes the initial snapshot data in event-time order rather than the default file-modification-time order, ensuring that records with later event times are not incorrectly marked as late and dropped. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Overview

When a streaming query with a defined watermark starts reading from a [Delta Lake](/concepts/delta-lake.md) table, it first processes all existing data in the table. This initial data is called the INITIAL_SNAPSHOT|initial snapshot. By default, Delta Lake's streaming source processes data files based on which file was last modified. However, the last modification time of a file does not necessarily represent the order of the events within that file. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

In a stateful streaming query, the watermark tracks the maximum event time seen so far. If the initial snapshot processes files in modification-time order, the query might see a record with a later event time, advance the watermark based on that time, and then later see a record with an earlier event time (because it was in a file modified earlier). The watermark would then incorrectly mark the earlier record as a late event and potentially drop it. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## How `withEventTimeOrder` Works

When `withEventTimeOrder` is enabled, the streaming source divides the event time range of the initial snapshot data into time buckets. Each micro-batch processes one bucket by filtering the data to only include records within that specific event-time range. This ensures that the watermarks advance in a consistent, event-time-aligned manner and that no records are incorrectly dropped due to out-of-order file processing. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

The `maxFilesPerTrigger` and `maxBytesPerTrigger` options still apply to control micro-batch size, but they are only approximate when `withEventTimeOrder` is enabled because the primary constraint is the event-time bucket. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Constraints

- You cannot change `withEventTimeOrder` if the stream query has started and the initial snapshot is actively processing. To restart with `withEventTimeOrder` changed, you must delete the [checkpoint](/concepts/checkpoint-v2-requirement.md) and restart the query. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]
- If `withEventTimeOrder` is enabled, you cannot downgrade a stream to a Databricks Runtime version that does not support this feature until the initial snapshot processing completes. To downgrade, wait for the initial snapshot to finish, or delete the checkpoint and restart the query. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]
- This feature is not supported in the following scenarios: ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]
  - The event time column is a generated column and there are non-projection transformations between the Delta source and watermark.
  - There is a watermark that has more than one Delta source in the stream query.

## Performance Considerations

Enabling `withEventTimeOrder` can reduce initial snapshot processing performance because each micro-batch must scan the entire initial snapshot to filter data within the corresponding event-time range. To improve filtering performance: ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

- Use a Delta source column as the event time so that data skipping can be applied.
- Partition the table along the event time column.

Use the Spark UI to see how many Delta files are scanned for a specific micro-batch. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Example Usage

```scala
spark.readStream
  .option("withEventTimeOrder", "true")
  .table("user_events")
  .withWatermark("event_time", "10 seconds")
```

You can also set `withEventTimeOrder` with a Spark configuration on the cluster to apply it to all streaming queries: ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

```
spark.databricks.delta.withEventTimeOrder.enabled true
```

## Related Concepts

- INITIAL_SNAPSHOT|Initial Snapshot – The complete dataset processed at the start of a streaming query.
- Watermark – A mechanism in [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) to track event time and handle late data.
- Data Skipping – A Delta Lake optimization that can reduce the files scanned for a query.
- Generated Column – A column whose value is automatically computed from other columns.
- Streaming Query – A continuous data-processing pipeline using Spark Structured Streaming.

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
