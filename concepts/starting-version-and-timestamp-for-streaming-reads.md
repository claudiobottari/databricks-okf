---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c9a35d8781dc4deae29f3c7b11904574ee8d9390ea35e79e57d5f3795a9a6a7a
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - starting-version-and-timestamp-for-streaming-reads
    - Timestamp for Streaming Reads and Starting Version
    - SVATFSR
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: Starting Version and Timestamp for Streaming Reads
description: Options (startingVersion, startingTimestamp) to control the initial table version from which a Delta Lake streaming source begins processing changes.
tags:
  - structured-streaming
  - delta-lake
  - configuration
timestamp: "2026-06-19T18:20:55.454Z"
---

#Starting Version and Timestamp for Streaming Reads

**Starting Version and Timestamp for Streaming Reads** are optional parameters that allow a [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) query consuming a [Delta Lake Table](/concepts/delta-lake-table.md) to begin processing from a specific point in the table’s history rather than from the latest snapshot. By default, a streaming read starts from the most recent [Delta Lake Table](/concepts/delta-lake-table.md) version, capturing a full snapshot of the table at that moment and all future changes. Databricks recommends using this default for most workloads. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## `startingVersion`

The `startingVersion` option specifies the [Delta Lake Table](/concepts/delta-lake-table.md) version from which to begin reading. The stream processes all table changes committed at or after that version. If the specified version is not available in the table’s history, the stream fails to start. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

To find available commit versions, run `DESCRIBE HISTORY` and inspect the `version` column. To read only the most recent changes without processing the full history, specify `latest` as the value. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## `startingTimestamp`

The `startingTimestamp` option specifies a timestamp from which to begin reading. The stream processes all table changes committed at or after that timestamp. If the provided timestamp precedes all table commits, the streaming read begins with the earliest available timestamp. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

Supported values include a timestamp string (for example, `"2019-01-01T00:00:00.000Z"`) or a date string (for example, `"2019-01-01"`). ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Constraints and Compatibility

You **cannot** set both `startingVersion` and `startingTimestamp` at the same time. These options apply only to new streaming queries; once a query has started and its progress has been recorded in a check¬point, these settings are ignored. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

Because the schema of the streaming source is always the latest schema of the [Delta Lake Table](/concepts/delta-lake-table.md), you must ensure that no incompatible schema changes have occurred after the specified version or timestamp. Otherwise, the stream might return incorrect results. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Examples

To read changes since version 5 of a [Delta Lake Table](/concepts/delta-lake-table.md) named `user_events`:

```scala
spark.readStream
  .option("startingVersion", "5")
  .table("user_events")
```

To read changes since October 18, 2018:

```scala
spark.readStream
  .option("startingTimestamp", "2018-10-18")
  .table("user_events")
```

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Related Concepts

- Delta Lake streaming — Overview of using Delta Lake as a streaming source and sink.
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) — Spark’s stream processing engine.
- Checkpointing — Mechanism that records stream progress and enables recovery.
- [Table history](/concepts/table-history-sharing.md) — How to query Delta Lake version history with `DESCRIBE HISTORY`.
- Data retention — Impact of `VACUUM` and log retention on stream availability.
- failOnDataLoss — Option to control behavior when source data is removed.

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
