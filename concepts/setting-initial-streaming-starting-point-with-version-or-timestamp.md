---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fdbd27e0c9b71517246360d377be9a541687e411531a5d02959a70593256847a
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - setting-initial-streaming-starting-point-with-version-or-timestamp
    - Timestamp or Setting Initial Streaming Starting Point with Version
    - SISSPWVOT
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: Setting Initial Streaming Starting Point with Version or Timestamp
description: Using startingVersion or startingTimestamp options to begin a Delta Lake streaming read from a specific table version or point in time, skipping the full table snapshot.
tags:
  - streaming
  - delta-lake
  - structured-streaming
timestamp: "2026-06-18T11:48:59.383Z"
---

# Setting Initial Streaming Starting Point with Version or Timestamp

When using [Delta Lake](/concepts/delta-lake.md) tables as a streaming source with Spark Structured Streaming, you can control where the stream begins processing data by specifying an initial starting point. By default, streams start from the latest available [Delta Lake Table](/concepts/delta-lake-table.md) version, which includes a complete snapshot of the table at that moment and all future changes. Databricks recommends using the default initial table version for most workloads. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Starting Point Options

You can optionally use the following options to specify the starting point of the Delta Lake streaming source without processing the entire table:

- **`startingVersion`**: The [Delta Lake Table](/concepts/delta-lake-table.md) version to start reading from. All table changes committed at or after the specified version are read by the stream. If the specified version is not available, the stream fails to start. To find available commit versions, run `DESCRIBE HISTORY` and check the `version` column. To return only the latest changes, specify `latest`. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

- **`startingTimestamp`**: The timestamp to start reading from. All table changes committed at or after the specified timestamp are read by the stream. If the provided timestamp precedes all table commits, the streaming read begins with the earliest available timestamp. You can set either a timestamp string (for example, `"2019-01-01T00:00:00.000Z"`) or a date string (for example, `"2019-01-01"`). ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

You cannot set both `startingVersion` and `startingTimestamp` at the same time. These settings apply to new streaming queries only. If a streaming query has started and the progress has been recorded in its checkpoint, these settings are ignored. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Schema Considerations

Although you can start the streaming source from a specified version or timestamp, the schema of the streaming source is always the latest schema of the [Delta Lake Table](/concepts/delta-lake-table.md). You must ensure there is no incompatible schema change to the [Delta Lake Table](/concepts/delta-lake-table.md) after the specified version or timestamp. Otherwise, the streaming source might return incorrect results when reading the data with an incorrect schema. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Examples

### Starting from a Specific Version

To read changes since version 5 of a table named `user_events`:

```scala
spark.readStream
  .option("startingVersion", "5")
  .table("user_events")
```

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### Starting from a Specific Timestamp

To read changes since October 18, 2018:

```scala
spark.readStream
  .option("startingTimestamp", "2018-10-18")
  .table("user_events")
```

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Related Concepts

- [Delta Lake table streaming reads and writes](/concepts/delta-lake-as-a-streaming-source-and-sink.md) — General guidance on using Delta Lake as a streaming source and sink
- Delta Lake table history — Working with table versions and the `DESCRIBE HISTORY` command
- Spark Structured Streaming — The streaming framework that powers Delta Lake streaming
- Streaming checkpoint management — How checkpoints track streaming progress
- Delta Lake retention windows — Understanding `VACUUM` and `logRetentionDuration` defaults that affect stream availability

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
