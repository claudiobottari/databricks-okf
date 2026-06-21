---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1688bd03f9fb495e033fcd0b5864dee353e0d7c7eb0b115f81097bd126586f5f
  pageDirectory: concepts
  sources:
    - read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - structured-streaming-on-shared-tables
    - SSOST
    - Structured Streaming
  citations:
    - file: read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md
title: Structured Streaming on Shared Tables
description: Using Spark Structured Streaming with OpenSharing shared tables as a source for incremental processing, requiring history sharing to be enabled.
tags:
  - streaming
  - apache-spark
  - data-sharing
  - databricks
timestamp: "2026-06-19T20:12:03.833Z"
---

# Structured Streaming on Shared Tables

**Structured Streaming on Shared Tables** refers to the use of [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) to incrementally process data from tables shared via [OpenSharing](/concepts/opensharing.md) (formerly Delta Sharing). This enables real-time or near-real-time ingestion of shared data without manual batch refreshes.

## Overview

OpenSharing allows data providers to share Delta tables with recipients. Recipients can read shared tables using Apache Spark DataFrames with the `deltasharing` format. For incremental processing, Structured Streaming can be used as the reading mechanism, provided the shared table has history sharing enabled. ^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]

## Prerequisites

To use Structured Streaming on a shared table:

- The provider must enable **history sharing** on the share using `ALTER SHARE` (see [Delta Sharing](/concepts/delta-sharing.md)). ^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]
- The recipient must use **Databricks Runtime 12.2 LTS or above**. ^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]
- The table must be accessible via an OpenSharing profile path in the form `<profile-path>#<share-name>.<schema-name>.<table-name>`. ^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]

## Reading with Structured Streaming

You can read a shared table as a streaming source by using `spark.readStream` with the `.format("deltasharing")` option and providing the full path to the shared table. The following example sets up a streaming DataFrame that reads all new data from the shared table:

```python
streaming_df = (spark.readStream
  .format("deltasharing")
  .load("<profile-path>#<share-name>.<schema-name>.<table-name>"))
```

^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]

The stream processes records incrementally as they become available in the shared table.

## Reading Change Data Feed with Structured Streaming

If the source Delta table has [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) (CDF) enabled **and** history sharing is enabled on the share, you can read change data feed records directly from the shared table using Structured Streaming. This allows you to capture inserts, updates, and deletes. ^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]

To read CDF in a streaming manner, use the `readChangeFeed` option and optionally specify a starting timestamp:

```python
streaming_cdf_df = (spark.readStream
  .format("deltasharing")
  .option("readChangeFeed", "true")
  .option("startingTimestamp", "2021-04-21 05:45:46")
  .load("<profile-path>#<share-name>.<schema-name>.<table-name>"))
```

^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]

The same CDF option works for batch reads using `spark.read`; the streaming example above shows the incremental variant.

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) – The protocol for sharing Delta tables between Databricks workspaces.
- [Delta Sharing](/concepts/delta-sharing.md) – The underlying sharing technology.
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) – Enables capture of row-level changes on Delta tables.
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) – The Databricks engine for incremental stream processing.
- Databricks Runtime – The runtime version required for history sharing support.
- Profile Path – The identifier used to locate a shared table in OpenSharing.

## Sources

- read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md

# Citations

1. [read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md](/references/read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws-a44c61ff.md)
