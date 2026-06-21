---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0b53a17b9db16827a43cff9949c0be20081028d58193f3f8192a9c8ed9142d60
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - witheventtimeorder-for-initial-snapshots
    - WFIS
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: withEventTimeOrder for Initial Snapshots
description: An option to preserve event-time ordering during initial snapshot processing in stateful streaming queries on Delta tables
tags:
  - streaming
  - delta-lake
  - event-time
  - watermark
timestamp: "2026-06-18T15:16:19.372Z"
---

# withEventTimeOrder for Initial Snapshots

**withEventTimeOrder** is a configuration option for [Delta Lake](/concepts/delta-lake.md) [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) that controls how initial snapshot data is processed during the first micro-batches of a streaming query. When enabled, it divides the event time range of the initial snapshot into time buckets, processing records in event time order rather than file modification time order, which prevents data loss in stateful streaming queries with watermarks.

## Overview

When a streaming query starts reading from a [Delta Lake Table](/concepts/delta-lake-table.md), it first processes all existing data in the table, creating a version called the _initial snapshot_. By default, the data files in the initial snapshot are processed based on which file was last modified. However, the last modification time does not necessarily represent the record event time order. This can cause problems when the streaming query has a defined watermark and uses stateful operations. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

Processing files by modification time can process records in the wrong order relative to their event time. This causes the watermark to incorrectly mark records as late events and drop them. This can only occur when the initial Delta snapshot is processed in the default order. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## How It Works

When `withEventTimeOrder` is enabled, the system:

1. Divides the event time range of initial snapshot data into time buckets.
2. Each micro-batch processes one bucket by filtering data within the corresponding time range.
3. The `maxFilesPerTrigger` and `maxBytesPerTrigger` options still apply to control micro-batch size, but only approximately due to the filtering approach. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

The following diagram illustrates this process:

![Initial Snapshot](https://docs.databricks.com/aws/en/assets/images/delta-initial-snapshot-data-drop-22bccd2312254a9f9e853389e49f13eb.png)

## Usage

### Enabling in Source Configuration

To enable `withEventTimeOrder` for a specific streaming query, set the option when configuring the read stream:

```python
(spark.readStream
  .option("withEventTimeOrder", "true")
  .table("user_events")
  .withWatermark("event_time", "10 seconds"))
```

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### Enabling Globally

You can also set `withEventTimeOrder` with a Spark configuration on the cluster to apply it to all streaming queries:

```
spark.databricks.delta.withEventTimeOrder.enabled true
```

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Availability

This feature is available on Databricks Runtime 11.3 LTS and above. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Constraints

The following constraints apply when using `withEventTimeOrder`: ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

- **Cannot change during active processing:** If the stream query has started and the initial snapshot is actively processing, you cannot change the `withEventTimeOrder` setting. To restart with a changed setting, you must delete the checkpoint.
- **Downgrade restriction:** If `withEventTimeOrder` is enabled, you cannot downgrade a stream to a Databricks Runtime version that does not support this feature until the initial snapshot processing completes. To downgrade, wait for the initial snapshot to finish, or delete the checkpoint and restart the query.
- **Unsupported scenarios:** This feature is not supported in the following cases:
  - The event time column is a generated column and there are non-projection transformations between the Delta source and watermark.
  - There is a watermark that has more than one Delta source in the stream query.

## Performance Considerations

If `withEventTimeOrder` is enabled, initial snapshot processing performance might be slower. Each micro-batch scans the initial snapshot to filter data within the corresponding event time range. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

To improve filtering performance: ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

- Use a Delta source column as the event time so that data skipping can be applied.
- Partition the table along the event time column.

Use the Spark UI to see how many Delta files are scanned for a specific micro-batch.

## Example

Suppose you have a table `user_events` with an `event_time` column. Your streaming query is an aggregation query. If you want to ensure no data drop during the initial snapshot processing, you can use:

```python
(spark.readStream
  .option("withEventTimeOrder", "true")
  .table("user_events")
  .withWatermark("event_time", "10 seconds"))
```

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Related Concepts

- Watermarking in Structured Streaming — How watermarks determine late event handling.
- [Initial Snapshot Processing](/concepts/event-time-ordered-initial-snapshot-processing.md) — The first phase of streaming from a Delta table.
- [Delta Lake Table Streaming Reads and Writes](/concepts/delta-lake-as-a-streaming-source-and-sink.md) — General guidance on streaming with Delta Lake.
- Data Skipping — Performance optimization for Delta table scans.

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
