---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1e41cfb00078f701d6eb55cb66a11c0052e4db15ee932a6e43b3fca687ba0850
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - change-data-feed-for-delta-streaming
    - CDFFDS
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: Change Data Feed for Delta Streaming
description: Approach to use Delta Lake change data feed to capture inserts, updates, and deletes from source tables in streaming queries for robust change data capture (CDC).
tags:
  - structured-streaming
  - delta-lake
  - cdc
  - change-data-feed
timestamp: "2026-06-19T18:21:32.208Z"
---

# Change Data Feed for Delta Streaming

**Change Data Feed (CDF)** is a feature of Delta Lake that captures row-level changes (inserts, updates, and deletes) made to a Delta table. When enabled, it provides a structured way to stream these changes from a source table to downstream consumers, enabling robust change data capture (CDC) workflows.

## Overview

The Change Data Feed records every change event at the row level, including metadata about the type of change (insert, update, or delete). This allows streaming queries to process all types of modifications, not just appends. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Use Case

CDF is the most robust approach for handling upstream changes to [Delta Lake](/concepts/delta-lake.md) tables when used as streaming sources. It is the recommended solution for workloads that need to process all change types—inserts, updates, and deletes—and propagate them to downstream tables with explicit logic for each event type. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## How It Works

When CDF is enabled on a [Delta Lake](/concepts/delta-lake.md) table, every write operation (including `UPDATE`, `DELETE`, `MERGE INTO`, and `OVERWRITE`) generates a change data feed record. Streaming readers can then consume this feed to process row-level changes. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Enabling Change Data Feed

To use CDF for streaming, the source table must have the change data feed feature enabled. This is typically done using the `delta.enableChangeDataFeed` table property or by setting `spark.databricks.delta.changeDataFeed` to `true` in the Spark session configuration. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Streaming with CDF

When streaming from a Delta table with CDF enabled:

1. The stream reads all row-level changes, including those from `UPDATE`, `DELETE`, and `MERGE INTO` operations.
2. Each change record includes the operation type (insert, update, or delete).
3. Downstream consumers can implement custom logic for each change type.

This contrasts with `skipChangeCommits`, which ignores all modification operations. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Comparison with Other Approaches

| Approach | Change Type Handling | Recommended For |
|----------|---------------------|-----------------|
| **Change Data Feed** | All changes (inserts, updates, deletes) | Robust CDC with explicit change handling |
| **skipChangeCommits** | Ignores all modifications | Append-only workloads, one-time changes |
| **ignoreChanges** | Re-emits modified files (legacy) | Older Databricks Runtime versions |
| **Full refresh** | Reprocess all data | Small datasets, infrequent changes |

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Column Mapping and Streaming

In Databricks Runtime 12.2 LTS and below, you cannot stream from the change data feed for a [Delta Lake Table](/concepts/delta-lake-table.md) with column mapping enabled that has undergone non-additive schema evolution (such as renaming or dropping columns). See Column mapping and streaming for details. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Related Concepts

- Change Data Capture (CDC) – The broader pattern of capturing and propagating data changes
- [Delta Lake](/concepts/delta-lake.md) – The storage layer that provides CDF functionality
- Streaming reads and writes – The underlying streaming mechanism for Delta tables
- Auto CDC APIs – Lakeflow Spark Declarative Pipelines for simplified CDC
- [Materialized views](/concepts/materialized-views-in-databricks.md) – An alternative for handling upstream changes without streaming complexity

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
