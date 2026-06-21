---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0932f4d670c01f64f59562c82d769156291dc4c3e58b0e491b40d5f02ec4d750
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - change-data-feed-for-streaming-all-change-types
    - CDFFSACT
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
      start: 93
      end: 95
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
      start: 95
      end: 96
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
      start: 95
      end: 97
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
      start: 93
      end: 97
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
      start: 103
      end: 107
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
      start: 93
      end: 96
title: Change Data Feed for streaming all change types
description: Using Delta Lake change data feed to stream inserts, updates, and deletes from a source table, providing row-level change tracking for robust downstream processing.
tags:
  - streaming
  - delta-lake
  - cdc
timestamp: "2026-06-19T10:00:50.142Z"
---

# Change Data Feed for Streaming All Change Types

**Change Data Feed for streaming all change types** refers to using the [Delta Lake change data feed](/concepts/delta-lake-change-data-feed-cdf.md) feature to capture and process row-level changes — inserts, updates, and deletes — from a [Delta Lake Table](/concepts/delta-lake-table.md) as a streaming source in Spark Structured Streaming.

## Overview

When a streaming query reads from a [Delta Lake Table](/concepts/delta-lake-table.md), it normally only processes new appends and fails if any `UPDATE`, `DELETE`, `MERGE INTO`, or `OVERWRITE` operation modifies the source table. For workloads that must handle all types of changes, the change data feed records every row-level change and makes those change events available to the stream. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md#L93-L95]

This is the most robust approach for propagating upstream changes downstream, because the streaming logic explicitly consumes each change type. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md#L95-L96]

## How It Works

The Delta Lake change data feed logs a row-level change for every insert, update, or delete committed to the table. By configuring the source table to enable the change data feed (`delta.enableChangeDataFeed = true`) and reading from it using the `readChangeFeed` API or the `cdf` option in `readStream`, a streaming query receives a stream of change events that include metadata such as the change type (`insert`, `update_preimage`, `update_postimage`, `delete`) and the version of the change. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md#L93-L95]

The stream reads from the change data feed as a continuous source, processing each change event in the order the table versions were committed. Downstream logic can inspect the change type column and decide how to apply each change — for example, merging updates into a target table, removing deleted rows, or inserting new rows. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md#L95-L97]

## Usage

To stream all change types from a [Delta Lake Table](/concepts/delta-lake-table.md), the table must first have the change data feed enabled. Then you read from it using the `readStream` option `readChangeFeed` or `startingVersion`/`startingTimestamp` with the `cdf` source option. The resulting DataFrame contains additional columns such as `_change_type`, `_commit_version`, and `_commit_timestamp`.

```python
(spark.readStream
  .option("readChangeFeed", "true")
  .table("source_table")
)
```

Each micro-batch delivers both pre‑image and post‑image rows for updates, allowing the streaming logic to implement any desired transformation. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md#L93-L97]

## Considerations

- **Column mapping limitation**: In Databricks Runtime 12.2 LTS and below, you cannot stream from the change data feed for a [Delta Lake Table](/concepts/delta-lake-table.md) with [column mapping](/concepts/column-mapping-in-delta-lake.md) enabled that has undergone non‑additive schema evolution (e.g., renaming or dropping columns). See Column mapping and streaming. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md#L103-L107]
- **Schema changes**: If the source table’s schema changes after the stream begins, the query may fail. For most schema changes, restarting the stream resolves the mismatch. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md#L103-L107]
- **Retention windows**: The change data feed is subject to the same retention as the transaction log (`logRetentionDuration`, default 30 days). If the stream falls behind, it may miss change records and fail. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md#L103-L107]
- **Cost**: The change data feed generates additional metadata and may increase storage cost for the table. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md#L103-L107]

## When to Use

Use the change data feed for streaming when you need to propagate deletes and updates (not just appends) to downstream systems. It is the recommended approach over `skipChangeCommits` when your workload requires handling every type of change event. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md#L93-L96]

## Related Concepts

- [Delta Lake change data feed](/concepts/delta-lake-change-data-feed-cdf.md) – The underlying feature that records row-level changes.
- [skipChangeCommits](/concepts/skipchangecommits.md) – A simpler option for ignoring change transactions.
- ignoreChanges – Legacy option that re‑emits rewritten data files.
- Spark Structured Streaming with Delta Lake – General guidance on streaming reads/writes.
- Column mapping and streaming – Limitations when using CDF with schema evolution.

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md (lines 93–107)

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md:93-95](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
2. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md:95-96](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
3. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md:95-97](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
4. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md:93-97](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
5. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md:103-107](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
6. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md:93-96](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
