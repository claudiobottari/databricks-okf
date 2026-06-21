---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5faeeda107b84dc83f91c72d3a725874843cd82da584eeb4c337ff648919800e
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-change-data-feed-for-streaming
    - DCDFFS
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: Delta Change Data Feed for Streaming
description: Using the Delta Lake change data feed to capture and stream all types of row-level changes (inserts, updates, deletes) from a source table, providing the most robust approach for handling upstream modifications.
tags:
  - streaming
  - delta-lake
  - change-data-capture
timestamp: "2026-06-18T11:49:19.697Z"
---

# Delta Change Data Feed for Streaming

**Delta Change Data Feed (CDF) for streaming** enables row-level change tracking on Delta Lake tables, allowing streaming queries to process inserts, updates, and deletes as distinct event types. This capability is essential for maintaining downstream consistency when source tables undergo modifications such as `UPDATE`, `DELETE`, `MERGE INTO`, or `OVERWRITE` operations. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Overview

[Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) incrementally reads Delta Lake tables by processing new table versions as they commit. By default, streaming queries only accept append inputs and fail if any modification operations occur on the source table. The change data feed provides a robust mechanism to handle all change types by recording row-level changes and making them available to downstream consumers. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Enabling Change Data Feed

To use change data feed for streaming, you must enable it on the [Delta Lake Table](/concepts/delta-lake-table.md). When enabled, the feed captures changes at the row level, including which rows were inserted, updated, or deleted. This allows you to write explicit handling logic for each change type in downstream tables. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

The change data feed is the most robust approach for handling upstream changes because your code explicitly processes every change event. See Enable change data feed on Delta tables for configuration details. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Reading Change Data Feed in Streams

### Using `readChangeFeed`

The `readChangeFeed` DataFrame reader provides a structured way to consume changes from a Delta table. It returns the following columns for each change:

- `_change_type`: The type of change (`insert`, `update_preimage`, `update_postimage`, `delete`)
- `_commit_version`: The table version at which the change was committed
- `_commit_timestamp`: The timestamp of the commit

### Using `readStream` with Change Data Feed Options

For streaming workloads, you can use `readStream` with the `readChangeFeed` option:

```python
(spark.readStream
  .option("readChangeFeed", "true")
  .table("source_table"))
```

This reads all changes as they are committed to the source table, including insert, update, and delete events. The streaming query processes each change type distinctly, allowing downstream logic to handle each type appropriately. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Handling Update and Delete Events

When you stream from a change data feed, the stream processes each type of change as a separate row in the output. For example, an `UPDATE` operation produces two rows: the pre-update image and the post-update image. Your downstream logic can then determine how to propagate those changes to target tables. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Alternative Approaches Without Change Data Feed

### Using `skipChangeCommits`

For workloads that do not require change data feed, the `skipChangeCommits` option (available in Databricks Runtime 12.2 LTS and above) allows streaming queries to ignore transactions that modify existing records, processing only appends. This is useful when changes to existing data do not need to be propagated through the stream. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### Legacy Options

- `ignoreChanges` (Databricks Runtime 11.3 LTS and below): Re-emits rewritten data files after modification operations, often causing duplicate rows in the output.
- `ignoreDeletes`: Only handles transactions that delete data at partition boundaries (full partition drops).

Databricks recommends using `skipChangeCommits` for all new workloads instead of these legacy options. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Best Practices

- **Use change data feed for production-grade pipelines** that must handle all change types accurately.
- **Consider materialized views** (via Lakeflow Spark Declarative Pipelines) as an alternative when you do not need the lowest possible latency and want to avoid managing streaming complexity.
- **Implement upsert logic in `foreachBatch`** when combining change data feed with streaming writes to target tables, using `merge` statements for idempotent handling.

## Limitations

- In Databricks Runtime 12.2 LTS and below, you cannot stream from the change data feed for a [Delta Lake Table](/concepts/delta-lake-table.md) with [column mapping](/concepts/column-mapping-in-delta-lake.md) enabled that has undergone non-additive schema evolution, such as renaming or dropping columns.
- The change data feed records row-level changes but does not propagate schema changes; schema evolution must be handled separately.

## Related Concepts

- [Delta Lake Change Data Feed](/concepts/delta-lake-change-data-feed-cdf.md) — The underlying mechanism for row-level change tracking
- Streaming from Delta Tables — Basic streaming patterns and options
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) — The Apache Spark streaming engine
- [ForeachBatch](/concepts/idempotent-foreachbatch-writes.md) — Writing custom logic per micro-batch
- [Merge Into Delta](/concepts/merge-into-delta-lake.md) — Combining streaming and merge operations
- Column Mapping and Streaming — Schema evolution compatibility with change data feed

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
