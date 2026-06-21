---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2f26cf6a92cc43f630a95aaa8ef81c4a904e60b9d61c7b6a9b2610db7d827749
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - skipchangecommits-for-handling-source-table-modifications
    - SFHSTM
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: skipChangeCommits for handling source table modifications
description: Option to skip transactions that modify/delete records in a Delta source table during streaming, processing only appends; replaces legacy options ignoreChanges and ignoreDeletes.
tags:
  - streaming
  - delta-lake
  - configuration
timestamp: "2026-06-19T10:00:21.981Z"
---

# skipChangeCommits for Handling Source Table Modifications

**skipChangeCommits** is a configuration option for Delta Lake streaming reads that allows a Structured Streaming query to ignore transactions that delete or modify existing records in a source [Delta Lake Table](/concepts/delta-lake-table.md), processing only append-only changes.

## Overview

When a streaming query reads from a [Delta Lake Table](/concepts/delta-lake-table.md), it incrementally processes new commits as they occur. However, certain operations such as `UPDATE`, `DELETE`, `MERGE INTO`, or `OVERWRITE` modify existing data in the source table. By default, Structured Streaming throws an exception if any modifications occur on the source [Delta Lake Table](/concepts/delta-lake-table.md) because it only accepts append inputs. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

Setting `skipChangeCommits` to `true` allows the stream to ignore these modification commits and continue processing only new append-only data. This is useful when changes to existing data do not need to be propagated through the stream, or when you prefer to implement separate logic to handle those changes. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Syntax

You enable `skipChangeCommits` as an option when configuring a streaming read from a [Delta Lake Table](/concepts/delta-lake-table.md):

```python
(spark.readStream
  .option("skipChangeCommits", "true")
  .table("source_table"))
```
^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Behavior

When `skipChangeCommits` is enabled:

- **Append-only operations** are processed as usual through the stream.
- **Modification operations** (`UPDATE`, `DELETE`, `MERGE INTO`, `OVERWRITE`) are completely ignored. Rewritten data files in the source table due to these operations are not re-emitted to the stream.
- **Deletes are not propagated downstream.** The stream simply skips over the commits that contain modifications.
- **Downstream consumers do not receive duplicates** from unchanged rows that were rewritten as part of a modification operation. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Comparison with Legacy Options

`skipChangeCommits` replaces the legacy option `ignoreChanges` in Databricks Runtime 12.2 LTS and above. The key difference is in how each option handles modified data files:

| Option | Behavior on Modification Operations | 
|--------|-------------------------------------|
| `skipChangeCommits` | Ignores rewritten data files entirely. Modified data is not re-emitted. |
| `ignoreChanges` (legacy) | Re-emits rewritten data files, potentially including unchanged rows alongside modified rows. Downstream consumers must handle duplicates. |

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

A separate legacy option, `ignoreDeletes`, only handles transactions that delete data at partition boundaries (full partition drops) but does not handle non-partition deletes, updates, or other modifications. Databricks recommends using `skipChangeCommits` instead of `ignoreDeletes` unless you are certain that deletes are always full partition drops. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Toggling Behavior

You can turn `skipChangeCommits` on and off if you need to temporarily ignore one-time changes to the source table. This flexibility allows you to selectively skip modification commits during specific periods without permanently altering the streaming configuration. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Schema Change Handling

If the schema for a [Delta Lake Table](/concepts/delta-lake-table.md) changes after a streaming read begins against the table, the query fails regardless of `skipChangeCommits`. For most schema changes, you can restart the stream to resolve schema mismatch and continue processing. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Recommendations

Databricks recommends using `skipChangeCommits` for most workloads that do not use [change data feed](/concepts/delta-change-data-feed-cdf.md). If you need to reflect changes (updates and deletes) in stream source tables, you must implement separate logic to propagate these changes, or use the change data feed approach for more robust handling. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

For workloads that process all types of changes (inserts, updates, and deletes), the [Delta Lake change data feed](/concepts/delta-lake-change-data-feed-cdf.md) is the most robust approach because your code explicitly handles every type of change event. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Related Concepts

- Structured Streaming with Delta Lake
- [Delta Lake Change Data Feed](/concepts/delta-lake-change-data-feed-cdf.md)
- Spark Structured Streaming
- Delta Lake Table History

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
