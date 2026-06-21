---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9d7112ea63a629de341811fb8a247dff42fbdfa793b8f946dc0c8963dc551e9a
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - initial-table-version-for-delta-streaming
    - ITVFDS
    - Setting initial table version for streaming
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: Initial Table Version for Delta Streaming
description: Setting startingVersion or startingTimestamp to control where a Delta Lake streaming source begins reading
tags:
  - streaming
  - delta-lake
  - checkpointing
timestamp: "2026-06-18T15:15:59.426Z"
---

# Initial Table Version for Delta Streaming

**Initial Table Version for Delta Streaming** refers to the optional configuration in Spark Structured Streaming that allows you to specify a starting point for reading from a [Delta Lake](/concepts/delta-lake.md) table source, rather than processing the full table history.

## Overview

By default, when a streaming query reads from a [Delta Lake Table](/concepts/delta-lake-table.md), it begins with the latest available table version and processes all future changes. This includes a complete snapshot of the table at that moment and all subsequent commits. Databricks recommends using this default behavior for most workloads. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

However, there are scenarios where you may want to start processing from a specific point in the table's history rather than from the latest version. Delta Lake provides two options for controlling the starting position: `startingVersion` and `startingTimestamp`. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Options for Setting Initial Table Version

### `startingVersion`

The `startingVersion` option specifies the [Delta Lake Table](/concepts/delta-lake-table.md) version to begin reading from. The stream reads all table changes committed at or after the specified version. If the specified version is not available in the table's history, the stream fails to start. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

To find available commit versions, run `DESCRIBE HISTORY` on the table and check the `version` column. To return only the latest changes, specify the value `latest`. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### `startingTimestamp`

The `startingTimestamp` option specifies a timestamp to start reading from. All table changes committed at or after the specified timestamp are read by the stream. If the provided timestamp precedes all table commits, the streaming read begins with the earliest available timestamp. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

Accepted formats include:
- A timestamp string, for example `"2019-01-01T00:00:00.000Z"`
- A date string, for example `"2019-01-01"`

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Constraints

You cannot set both `startingVersion` and `startingTimestamp` at the same time. These settings apply only to new streaming queries. If a streaming query has already started and progress has been recorded in its checkpoint, these settings are ignored. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### Schema Compatibility

Although you can start the streaming source from a specified version or timestamp, the schema of the streaming source is always the latest schema of the [Delta Lake Table](/concepts/delta-lake-table.md). You must ensure there is no incompatible schema change to the [Delta Lake Table](/concepts/delta-lake-table.md) after the specified version or timestamp. Otherwise, the streaming source might return incorrect results when reading the data with an incorrect schema. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Example Usage

The following example reads changes from a `user_events` table starting from version 5:

```scala
spark.readStream
  .option("startingVersion", "5")
  .table("user_events")
```

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

The following example reads changes starting from October 18, 2018:

```scala
spark.readStream
  .option("startingTimestamp", "2018-10-18")
  .table("user_events")
```

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Related Concepts

- Delta Lake Table History — Viewing available table versions using `DESCRIBE HISTORY`
- Structured Streaming Checkpoints — How checkpoint data affects initial version options
- [Skip Change Commits for Delta Streaming](/concepts/skipchangecommits-for-streaming-sources.md) — Handling modifications in source tables
- Delta Lake Retention Windows — How VACUUM and log retention affect available versions
- INITIAL_SNAPSHOT Subcondition|Process Initial Snapshot Without Dropping Data — Using `withEventTimeOrder` for stateful queries

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
