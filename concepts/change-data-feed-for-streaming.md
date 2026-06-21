---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d56a9731350fda021a29491d368fb41a94120f6c44f13d50d586185578af8858
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - change-data-feed-for-streaming
    - CDFFS
    - change-data-feed-for-delta-streaming
    - CDFFDS
    - change-data-feed-for-streaming-all-change-types
    - CDFFSACT
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: Change Data Feed for Streaming
description: Using Delta Lake change data feed to stream all change types (inserts, updates, deletes) and handle them explicitly in downstream tables
tags:
  - delta-lake
  - streaming
  - cdc
  - change-data-feed
timestamp: "2026-06-19T15:00:07.226Z"
---

# Change Data Feed for Streaming

**Change Data Feed for Streaming** refers to the use of Delta Lake's built-in change data feed as a streaming source in Spark Structured Streaming. The change data feed records row-level changes (inserts, updates, and deletes) made to a [Delta Lake Table](/concepts/delta-lake-table.md). By consuming the change data feed with `readStream`, a streaming query can process all types of changes and apply custom logic in downstream tables for each change event. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Overview

When a [Delta Lake Table](/concepts/delta-lake-table.md) is modified by operations such as `INSERT`, `UPDATE`, `DELETE`, or `MERGE INTO`, the change data feed captures the before and after images of the affected rows. A streaming query that reads from the change data feed is able to see each committed change as a new record in the feed. This approach is the most robust way to handle full change data capture (CDC) workloads with [Delta Lake](/concepts/delta-lake.md), because the application code explicitly handles every type of change event and can propagate deletions, updates, and inserts to downstream tables. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## When to Use the Change Data Feed

The change data feed is designed for workloads that require processing all types of changes—not just appends. Alternative approaches include:

- **`skipChangeCommits`**: Ignores transactions that delete or modify existing records; only processes appends. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]
- **Full refresh**: Delete checkpoint and output table, then restart from scratch; best for small datasets or infrequent changes. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]
- **Materialized views**: Automatically recompute results when source data changes; suitable when lowest latency is not required. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

For workloads that must handle all row-level changes in near-real-time, the change data feed is the recommended path. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Limitations

In Databricks Runtime 12.2 LTS and below, you cannot stream from the change data feed for a [Delta Lake Table](/concepts/delta-lake-table.md) that has [column mapping](/concepts/column-mapping-in-delta-lake.md) enabled and has undergone non-additive schema evolution, such as renaming or dropping columns. For details, see the column mapping documentation. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Related Concepts

- [Delta Lake table streaming reads and writes](/concepts/delta-lake-as-a-streaming-source-and-sink.md)
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md)
- Change data capture (CDC)
- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md)
- [Column mapping](/concepts/column-mapping-in-delta-lake.md)
- Use change data feed on Databricks

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
