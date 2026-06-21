---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8062065a3b9b96849ef745453fc76c2d37e4d7a4a0df17100dcddbce5b5c83f3
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - skipchangecommits-for-streaming-sources
    - SFSS
    - Skip Change Commits for Delta Streaming
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: skipChangeCommits for Streaming Sources
description: An option to ignore transactions that delete or modify existing records when streaming from a Delta Lake source
tags:
  - streaming
  - delta-lake
  - change-handling
timestamp: "2026-06-18T15:15:44.183Z"
---

# skipChangeCommits for Streaming Sources

**skipChangeCommits** is a streaming source option for [Delta Lake](/concepts/delta-lake.md) tables that instructs Spark Structured Streaming queries to ignore transactions that delete or modify existing records, processing only appended data. This option helps streaming queries continue running without failure when the source table undergoes non-append operations like `UPDATE`, `DELETE`, `MERGE INTO`, or `OVERWRITE`.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Overview

By default, when a streaming query reads from a [Delta Lake Table](/concepts/delta-lake-table.md), it only accepts append inputs. If any modification operation occurs on the source table — such as `UPDATE`, `DELETE`, `MERGE INTO`, or `OVERWRITE` — the stream fails with an error. `skipChangeCommits` allows the stream to disregard these change operations and continue processing only new appended data.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Usage

Enable `skipChangeCommits` as an option on the streaming source:

* Python
* Scala

Python

```python
(spark.readStream
  .option("skipChangeCommits", "true")
  .table("source_table"))
```

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### Turning On and Off

You can dynamically enable and disable `skipChangeCommits` as needed. This flexibility is useful when you need to temporarily ignore one-time changes to the source table without restarting the stream.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Schema Changes

If the schema for a [Delta Lake Table](/concepts/delta-lake-table.md) changes after a streaming read has begun against the table, the query fails regardless of `skipChangeCommits` settings. For most schema changes, you can resolve the issue by restarting the stream to reconcile schema mismatches.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Implementation Details

When `skipChangeCommits` is enabled, the streaming source completely disregards file-changing operations. This means that rewritten data files in the source table due to data modification operations such as `UPDATE`, `MERGE INTO`, `DELETE`, and `OVERWRITE` are ignored entirely. Deletes are not propagated downstream, and modified records are not re-emitted.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

For workloads that need to reflect changes in stream source tables, you must implement separate logic to propagate these changes.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Comparison with Legacy Options

### Replacement for `ignoreChanges`

In Databricks Runtime 12.2 LTS and above, `skipChangeCommits` replaces the legacy `ignoreChanges` option. In Databricks Runtime 11.3 LTS and lower, `ignoreChanges` is the only supported option.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

Key differences:

- **`ignoreChanges`**: Rewritten data files from modification operations are re-emitted downstream. Unchanged rows are often emitted alongside new rows, so downstream consumers must handle potential duplicates. Deletes are not propagated.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]
- **`skipChangeCommits`**: Disregards file-changing operations entirely. No re-emission of rewritten data occurs. This provides cleaner semantics but means changes in the source table are not reflected in the stream output.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

Databricks recommends using `skipChangeCommits` for all new workloads. To migrate from `ignoreChanges` to `skipChangeCommits`, refactor your streaming logic.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### Relationship with `ignoreDeletes`

`ignoreDeletes` is a legacy option that only handles transactions deleting data at partition boundaries (full partition drops). `skipChangeCommits` provides broader coverage by handling all types of changes, including non-partition deletes, updates, and other modifications. Databricks recommends using `skipChangeCommits` instead of `ignoreDeletes` unless you are certain that deletes are always full partition drops.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Example: Handling GDPR Deletes

Suppose you have a table `user_events` partitioned by `date` with columns `user_email` and `action`. You stream from this table and need to delete data due to GDPR compliance requirements targeting specific `user_email` values across multiple partitions:

```scala
spark.readStream
  .option("skipChangeCommits", "true")
  .table("user_events")
```

With `skipChangeCommits` enabled, you can perform `DELETE` operations on the source table (filtering by `user_email`) without causing the streaming query to fail. Similarly, if you update a `user_email` using the `UPDATE` statement, the rewritten data files are ignored by the stream.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## When to Use Alternative Approaches

While `skipChangeCommits` is suitable for many workloads, consider these alternatives when your requirements differ:

### Change Data Feed

For workloads that need to process all types of changes (inserts, updates, and deletes), use the [Delta Lake Change Data Feed](/concepts/delta-lake-change-data-feed-cdf.md). This records row-level changes and allows you to write logic for each change type in downstream tables. This is the most robust approach for handling every type of change event.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### Full Refresh

If upstream changes are rare and the data is small enough to reprocess, you can delete the streaming checkpoint and output table, then restart the stream from the beginning. This causes the stream to reprocess all data from the source table.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### Materialized Views

Materialized views automatically handle upstream changes by recomputing results when source data changes. This approach simplifies architecture when you do not require the lowest possible latency.^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Table Streaming Reads and Writes](/concepts/delta-lake-as-a-streaming-source-and-sink.md) — Comprehensive guide for streaming with Delta Lake
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) — Row-level change tracking for Delta Lake tables
- Streaming Checkpoints — Managing streaming query state and recovery
- VACUUM Retention Windows — Understanding retention limits for streaming sources
- [Initial Snapshot Processing](/concepts/event-time-ordered-initial-snapshot-processing.md) — Handling the first read of existing data in a [Delta Lake Table](/concepts/delta-lake-table.md)

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
