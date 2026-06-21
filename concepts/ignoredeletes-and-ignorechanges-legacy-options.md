---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f1de3fe8512b9dc8dfde9931e87158366cb7fbde0c4dd9aa4cdfdcfa963db3c5
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ignoredeletes-and-ignorechanges-legacy-options
    - ignoreChanges Legacy Options and ignoreDeletes
    - IAILO
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: ignoreDeletes and ignoreChanges Legacy Options
description: Legacy streaming source options for Delta Lake that handle delete/change operations differently than skipChangeCommits, with specific behaviors for file re-emission and duplicate handling.
tags:
  - structured-streaming
  - delta-lake
  - legacy
timestamp: "2026-06-19T18:20:39.432Z"
---

# ignoreDeletes and ignoreChanges Legacy Options

The **`ignoreDeletes`** and **`ignoreChanges`** options are legacy configuration parameters for Spark Structured Streaming when reading from [Delta Lake](/concepts/delta-lake.md) tables. They control how streaming queries handle data modification operations (such as `DELETE`, `UPDATE`, `MERGE INTO`, and `OVERWRITE`) on source Delta Lake tables. These options have been superseded by the `skipChangeCommits` option in Databricks Runtime 12.2 LTS and above. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Overview

By default, [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) only accepts append inputs when reading from a [Delta Lake Table](/concepts/delta-lake-table.md). If any modification operation (such as `UPDATE`, `DELETE`, `MERGE INTO`, or `OVERWRITE`) modifies a source [Delta Lake Table](/concepts/delta-lake-table.md) that a streaming query reads from, the stream fails with an error. The legacy `ignoreDeletes` and `ignoreChanges` options provide mechanisms to handle these operations without failing the stream. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## `ignoreDeletes`

The `ignoreDeletes` option is a legacy option that only handles transactions that delete data at partition boundaries (that is, full partition drops). It does not handle non-partition deletes, updates, or other modification operations. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

If you need to handle non-partition deletes, updates, or other modifications, use `skipChangeCommits` instead. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### Syntax

```python
spark.readStream \
  .option("ignoreDeletes", "true") \
  .table("user_events")
```

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## `ignoreChanges`

The `ignoreChanges` option is available in Databricks Runtime 11.3 LTS and lower. In Databricks Runtime 12.2 LTS and above, it is replaced by `skipChangeCommits`. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

With `ignoreChanges` enabled, rewritten data files in the source table are re-emitted after a data modification operation such as `UPDATE`, `MERGE INTO`, `DELETE` (within partitions), or `OVERWRITE`. Unchanged rows are often emitted alongside new rows, so downstream consumers must be able to handle duplicates. Deletes are not propagated downstream. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

`ignoreChanges` takes precedence over `ignoreDeletes`. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Comparison with `skipChangeCommits`

In contrast to `ignoreChanges`, `skipChangeCommits` disregards file-changing operations entirely. Rewritten data files in the source table due to data modification operations such as `UPDATE`, `MERGE INTO`, `DELETE`, and `OVERWRITE` are ignored entirely. To reflect changes in stream source tables, you must implement separate logic to propagate these changes. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

Databricks recommends using `skipChangeCommits` for all new workloads. To migrate a workload from `ignoreChanges` to `skipChangeCommits`, refactor your streaming logic. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Summary of Recommendations

| Option | Best For | Status |
|--------|----------|--------|
| `skipChangeCommits` | Most workloads that do not use change data feeds | Current (Databricks Runtime 12.2 LTS+) |
| `ignoreChanges` | Legacy workloads on Databricks Runtime 11.3 LTS and lower | Superseded by `skipChangeCommits` |
| `ignoreDeletes` | Scenarios where deletes are always full partition drops | Limited; use `skipChangeCommits` instead |

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Related Concepts

- [skipChangeCommits](/concepts/skipchangecommits.md) — The modern replacement for these legacy options
- [Delta Lake change data feed](/concepts/delta-lake-change-data-feed-cdf.md) — Row-level change tracking for robust change processing
- [Delta Lake streaming reads and writes](/concepts/delta-lake-as-a-streaming-source-and-sink.md) — General patterns for streaming with Delta Lake
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) — The streaming engine that processes Delta Lake tables
- Data modification operations on Delta Lake — How UPDATE, DELETE, MERGE, and OVERWRITE affect streaming sources

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
