---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a806224c6e5ec1e42437d8b9247a988ddb1048798dad78ec7754ed9ecd708c9e
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - event-time-ordered-initial-snapshot-processing
    - EOISP
    - Event time processing
    - Initial Snapshot Processing
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: Event-Time Ordered Initial Snapshot Processing
description: The withEventTimeOrder option processes initial Delta snapshot data in event-time order buckets to prevent watermark-based data drops in stateful streaming queries.
tags:
  - streaming
  - delta-lake
  - structured-streaming
timestamp: "2026-06-18T11:49:18.738Z"
---

# Event-Time Ordered Initial Snapshot Processing

**Event-Time Ordered Initial Snapshot Processing** is a feature in Spark Structured Streaming with [Delta Lake](/concepts/delta-lake.md) that reorders the processing of the initial snapshot of a Delta source table so that records are grouped by their event time rather than file modification time. This prevents a stateful streaming query from incorrectly dropping late-arriving data during initial snapshot processing when a watermark is defined.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Background

When a streaming query reads from a [Delta Lake Table](/concepts/delta-lake-table.md), it first processes all data present in the table — this is called the *initial snapshot*. By default, Delta Lake processes data files in order of their last modification time. However, the file modification time does not necessarily correspond to the event time of the records inside those files. If a stateful query (such as an aggregation) uses a watermark to handle late events, the default ordering can cause records with a later event time to be processed before records with an earlier event time. The watermark may then mark the earlier records as late and drop them, leading to data loss.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## How It Works

Enabling the `withEventTimeOrder` option (available in Databricks Runtime 11.3 LTS and above) instructs the streaming source to divide the event time range of the initial snapshot data into time buckets. Each micro-batch processes one bucket by filtering data within that specific event time range. This ensures that records are output in ascending event-time order, so the watermark advances correctly and late records are not incorrectly discarded.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

The existing `maxFilesPerTrigger` and `maxBytesPerTrigger` options still control micro-batch size, but only approximately, because the bucket-based approach may override the precise limits intended by those settings.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

The following diagram illustrates the concept:

![Diagram showing initial snapshot data drop prevention by using event-time ordered processing](https://docs.databricks.com/aws/en/assets/images/delta-initial-snapshot-data-drop-22bccd2312254a9f9e853389e49f13eb.png)

## Constraints

The feature has several important limitations:

- Once a streaming query has started processing the initial snapshot with `withEventTimeOrder`, you cannot change the setting. To restart with a different value, you must delete the checkpoint and restart the query from scratch.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]
- If `withEventTimeOrder` is enabled, you cannot downgrade the stream to a Databricks Runtime version that does not support the feature until initial snapshot processing completes. To downgrade, wait for the snapshot to finish, or delete the checkpoint and restart the query.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]
- The feature is not supported in the following scenarios:
  - The event time column is a generated column **and** there are non-projection transformations between the Delta source and the watermark.
  - The stream query has a watermark that involves more than one Delta source.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Performance Considerations

Enabling `withEventTimeOrder` may slow down initial snapshot processing. Each micro-batch must scan the initial snapshot to filter data within the corresponding event time range, rather than simply reading files in their natural order. To improve filtering performance:^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

- Use a Delta source column as the event time so that data skipping can be applied.
- Partition the table along the event time column.

You can monitor the number of Delta files scanned per micro-batch using the Spark UI.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Example

Suppose you have a table `user_events` with an `event_time` column and you want to perform a streaming aggregation with a 10-second watermark. To avoid data loss during initial snapshot processing, enable `withEventTimeOrder`:

```scala
spark.readStream
  .option("withEventTimeOrder", "true")
  .table("user_events")
  .withWatermark("event_time", "10 seconds")
```

You can also set the option globally on the cluster with the Spark configuration:

```
spark.databricks.delta.withEventTimeOrder.enabled true
```

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer providing transactional guarantees for streaming sources
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) — The Apache Spark streaming engine used with Delta tables
- Stateful Streaming — Streaming queries that maintain state (e.g., aggregations, joins)
- Watermark — Mechanism to control late-data handling in stateful streams
- Data Skipping — Optimisation that reduces file scans for filtered queries
- INITIAL_SNAPSHOT|Initial Snapshot — The complete set of data present in a Delta table when a streaming query starts
- maxFilesPerTrigger — Option to limit files processed per micro-batch
- maxBytesPerTrigger — Option to limit data size processed per micro-batch

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
