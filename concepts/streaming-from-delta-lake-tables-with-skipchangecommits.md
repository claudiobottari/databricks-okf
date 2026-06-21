---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cbee8f16e0d8f995b0084bef61f6aecce50972f3f2be8312991f7d055385967b
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - streaming-from-delta-lake-tables-with-skipchangecommits
    - SFDLTWS
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: Streaming from Delta Lake Tables with skipChangeCommits
description: The skipChangeCommits option allows streaming queries to ignore upstream modifications (UPDATE, DELETE, MERGE, OVERWRITE) on a source Delta table, processing only append transactions.
tags:
  - streaming
  - delta-lake
  - structured-streaming
timestamp: "2026-06-18T11:49:14.234Z"
---

# Streaming from Delta Lake Tables with skipChangeCommits

**Streaming from Delta Lake Tables with `skipChangeCommits`** is a configuration option for Spark Structured Streaming queries that read from [Delta Lake](/concepts/delta-lake.md) tables as a streaming source. When enabled, the streaming query ignores transactions that delete or modify existing records, processing only append-only data. This is useful when changes to existing data do not need to be propagated through the stream, or when you prefer to implement separate logic to handle those changes. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Overview

Structured Streaming incrementally reads Delta Lake tables by processing new records as new table versions commit to the source. By default, structured streaming only accepts append inputs and throws an exception if any modifications — such as `UPDATE`, `DELETE`, `MERGE INTO`, or `OVERWRITE` — occur on the source [Delta Lake Table](/concepts/delta-lake-table.md). ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

Setting `skipChangeCommits` allows the stream to ignore data modification operations entirely. Rewritten data files in the source table due to operations like `UPDATE`, `MERGE INTO`, `DELETE`, and `OVERWRITE` are disregarded. Deletes are not propagated downstream, and the stream continues processing only new appended data. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## When to Use skipChangeCommits

Databricks recommends using `skipChangeCommits` for most workloads that do not use [change data feed](/concepts/delta-change-data-feed-cdf.md) (CDF). ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

This option is particularly well-suited for:

- **GDPR or data privacy compliance** — when you need to delete data from a source table without breaking downstream streaming queries that only need to process new events
- **Temporary data cleanup** — when you need to perform one-time data modifications and can turn the option on temporarily, then turn it off after the change is complete
- **Workloads where upstream changes are rare** — and separate logic handles those changes at the point of consumption

If the schema for a [Delta Lake Table](/concepts/delta-lake-table.md) changes after a streaming read begins against the table, the query fails. For most schema changes, you can restart the stream to resolve schema mismatch and continue processing. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Configuration

Enable `skipChangeCommits` using the `.option()` method on the `DataStreamReader`:

*   Python
*   Scala

```python
(spark.readStream
  .option("skipChangeCommits", "true")
  .table("source_table"))
```

```scala
spark.readStream
  .option("skipChangeCommits", "true")
  .table("source_table")
```

You can turn `skipChangeCommits` on and off as needed — for example, to temporarily ignore one-time changes while continuing to process new data. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Behavior with Different Operations

| Operation | Behavior with `skipChangeCommits` |
|-----------|-----------------------------------|
| `APPEND` | New records are processed normally |
| `UPDATE` | Rewritten data files are ignored; unchanged rows are not re-emitted |
| `DELETE` | Deleted records are not propagated downstream |
| `MERGE INTO` | Changed files are ignored |
| `OVERWRITE` | Rewritten data files are not re-processed |

In contrast to the legacy `ignoreChanges` option, which re-emitted rewritten data files after modification operations, `skipChangeCommits` disregards file-changing operations entirely. Legacy `ignoreChanges` also often emitted unchanged rows alongside new rows, requiring downstream consumers to handle duplicates. `skipChangeCommits` does not re-emit any data, eliminating this duplication issue. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Legacy Options

### `ignoreDeletes`

`ignoreDeletes` is a legacy option that only handles transactions that delete data at partition boundaries (full partition drops). If you need to handle non-partition deletes, updates, or other modifications, use `skipChangeCommits` instead. Databricks recommends using `skipChangeCommits` instead of `ignoreDeletes` unless you are certain that deletes are always full partition drops. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### `ignoreChanges`

In Databricks Runtime 11.3 LTS and lower, `ignoreChanges` is the only supported option. In Databricks Runtime 12.2 LTS and above, `skipChangeCommits` replaces `ignoreChanges`. Databricks recommends using `skipChangeCommits` for all new workloads. To migrate a workload from `ignoreChanges` to `skipChangeCommits`, refactor your streaming logic. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md, delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Alternative Approaches

When changes to the source table must be reflected in downstream consumers, consider these alternatives:

- **[Change Data Feed](/concepts/delta-change-data-feed-cdf.md)** — records row-level changes (inserts, updates, deletes) so your code can handle each type of change explicitly. This is the most robust approach.
- **[Materialized Views](/concepts/materialized-views-in-databricks.md)** — automatically recompute results when source data changes, suitable when low latency is not required.
- **Full refresh** — delete the streaming checkpoint and output table, then restart the stream from the beginning to reprocess all data. Best for smaller datasets where the cost of a full refresh is acceptable. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Requirements and Limitations

- In Databricks Runtime 12.2 LTS and above, `skipChangeCommits` is the supported option. In Databricks Runtime 11.3 LTS and lower, `ignoreChanges` is the only supported option. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]
- If you use a [Delta Lake Table](/concepts/delta-lake-table.md) as a streaming source, the streaming query must run at least one time within the source table's retention window. The default retention windows are 7 days for `VACUUM`-removed data files and 30 days for the transaction log. If a query falls behind these windows, it fails with `DELTA_FILE_NOT_FOUND_DETAILED` and must be reset with a full refresh. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that powers streaming reads and writes
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) — The Spark streaming engine used with `readStream` and `writeStream`
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) — The alternative for processing all types of table changes
- Spark Structured Streaming — The underlying framework for incrementally processing data
- [Delta Lake Source Retention Windows](/concepts/delta-lake-streaming-retention-window-and-failure-handling.md) — The time limits for VACUUM and transaction log retention

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
