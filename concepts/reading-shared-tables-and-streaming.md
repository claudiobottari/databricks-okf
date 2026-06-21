---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea7c378dca94c1251c9d97b45823f8cce123ce19c58cf8c1286f128d9aab5c4a
  pageDirectory: concepts
  sources:
    - read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md
  confidence: 0.94
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - reading-shared-tables-and-streaming
    - Streaming and Reading Shared Tables
    - RSTAS
  citations:
    - file: read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md
title: Reading Shared Tables and Streaming
description: Technical operations for querying shared tables including batch reads, time-travel queries, change data feed (CDF), and Apache Spark Structured Streaming, with specific version and option requirements.
tags:
  - delta-sharing
  - streaming
  - data-querying
timestamp: "2026-06-19T20:08:35.779Z"
---

# Reading Shared Tables and Streaming

This page describes how to read data shared with you through the Databricks-to-Databricks OpenSharing protocol, focusing on reading shared tables and using streaming queries on them. As a recipient, you access shared data using Unity Catalog syntax after a privileged user creates a catalog from the share. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Reading Shared Tables

You can read data in a shared table using any Databricks tool: Catalog Explorer, notebooks, SQL queries, the Databricks CLI, or REST APIs. You must have the `SELECT` privilege on the table. Shared tables are read-only. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

If the provider shares the table `WITH HISTORY`, you can run time-travel queries using version or timestamp, and access the change data feed (CDF). For example: `SELECT * FROM table VERSION AS OF 3;` or `SELECT * FROM table_changes('table', 0, 3);`. History queries require Databricks Runtime 12.2 LTS or above. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Streaming on Shared Tables

If a table is shared with history, you can use it as the source for Spark Structured Streaming. This requires Databricks Runtime 12.2 LTS or above. Supported options include `ignoreDeletes`, `ignoreChanges`, `startingVersion`, `startingTimestamp`, `maxFilesPerTrigger`, `maxBytesPerTrigger`, and `readChangeFeed`. The `Trigger.availableNow` option is not supported. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

### Sample Streaming Queries

For Scala, a typical streaming read on a shared table looks like:
```scala
spark.readStream.format("deltaSharing")
  .option("startingVersion", 0)
  .option("ignoreChanges", true)
  .option("maxFilesPerTrigger", 10)
  .table("catalog.schema.table")
```

To stream the change data feed (CDF):
```scala
spark.readStream.format("deltaSharing")
  .option("readChangeFeed", "true")
  .table("catalog.schema.table")
```
^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Reading Shared Streaming Tables and Materialized Views

Reading shared streaming tables and materialized views follows the same pattern as reading shared tables, but has additional restrictions:

- **History**: You cannot query history of materialized views.
- **Refresh**: You cannot access the refresh status or schedule of a materialized view.
- **Transactions**: Supported, but see the transaction limitations page.
- **SQL limitations**: `current_recipient` function and `DESCRIBE EXTENDED` are not supported.
- **Column mapping**: If using classic compute across accounts, you must set `responseFormat=delta`; serverless or same‑account querying has no restriction.
- **Cost**: Sharing costs apply; see the sharing costs documentation. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

For streaming tables specifically, you cannot create streaming tables on shared materialized views. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Reading Tables with Deletion Vectors or Column Mapping

If the provider enables deletion vectors or column mapping on a shared Delta table, you can perform batch reads using a SQL warehouse or cluster running Databricks Runtime 14.1 or above. CDF and streaming queries require Databricks Runtime 14.2 or above. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

For CDF and streaming on such tables, you must set the additional option `responseFormat=delta`. Example:
```scala
spark.readStream.format("deltaSharing")
  .option("responseFormat", "delta")
  .table(<tableName>)
```
^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for sharing data across platforms
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that enables Databricks-to-Databricks sharing
- Structured Streaming on Databricks — General streaming guidance
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) — Capturing row-level changes for incremental processing
- [Deletion Vectors](/concepts/deletion-vectors.md) — Storage optimization affecting read semantics

## Sources

- read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md

# Citations

1. [read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md](/references/read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws-21150d4f.md)
