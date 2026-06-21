---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9fc28f66811b0a20e7997ed6c8c47a3c5a7a91f7178b0035ea5b416748898fdf
  pageDirectory: concepts
  sources:
    - read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - change-data-feed-with-opensharing
    - CDFWO
  citations:
    - file: read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md
title: Change Data Feed with OpenSharing
description: Reading incremental change data from OpenSharing tables using the readChangeFeed option in Spark DataFrames and Structured Streaming.
tags:
  - change-data-capture
  - streaming
  - data-sharing
  - delta-lake
timestamp: "2026-06-19T20:12:00.008Z"
---

# Change Data Feed with OpenSharing

**Change Data Feed with OpenSharing** refers to the ability to read row-level change records (inserts, updates, deletes) from tables shared via [OpenSharing](/concepts/opensharing.md) (also known as [Delta Sharing](/concepts/delta-sharing.md)) when the underlying source [Delta Lake](/concepts/delta-lake.md) table has the change data feed (CDF) feature enabled and the share has history sharing enabled. This allows recipients to consume incremental changes from shared tables using both batch and [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) operations. ^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]

## Prerequisites

To use change data feed with OpenSharing, two conditions must be met:

1. The source Delta table must have change data feed enabled (see Use change data feed on Databricks).
2. The share must have history sharing enabled (using `ALTER SHARE`).

Additionally, reading change data feed through OpenSharing requires **Databricks Runtime 12.2 LTS or above**. ^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]

## Reading change data feed with Apache Spark DataFrames (batch)

For tables that meet the prerequisites, you can read change data feed records in batch using the `deltasharing` format with the `readChangeFeed`, `startingTimestamp`, and `endingTimestamp` options.

```python
df = (spark.read
  .format("deltasharing")
  .option("readChangeFeed", "true")
  .option("startingTimestamp", "2021-04-21 05:45:46")
  .option("endingTimestamp", "2021-05-21 12:00:00")
  .load("<profile-path>#<share-name>.<schema-name>.<table-name>"))
```

The `startingTimestamp` and `endingTimestamp` define the time range of change records to retrieve. ^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]

## Reading change data feed with Structured Streaming (streaming)

You can also use a shared table with history sharing as a source for Structured Streaming. If change data feed is additionally enabled on the source table, you can specify `readChangeFeed` and `startingTimestamp` options to stream changes from a given point in time.

```python
# Basic streaming without CDF:
streaming_df = (spark.readStream
  .format("deltasharing")
  .load("<profile-path>#<share-name>.<schema-name>.<table-name>"))

# Streaming with CDF:
streaming_cdf_df = (spark.readStream
  .format("deltasharing")
  .option("readChangeFeed", "true")
  .option("startingTimestamp", "2021-04-21 05:45:46")
  .load("<profile-path>#<share-name>.<schema-name>.<table-name>"))
```

Note that `endingTimestamp` is **not** used in streaming; changes are consumed continuously from the starting timestamp. ^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]

## Related concepts

- [OpenSharing](/concepts/opensharing.md) – The protocol for sharing Delta tables across Databricks workspaces.
- [Delta Sharing](/concepts/delta-sharing.md) – The underlying open standard for data sharing.
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) – The Delta Lake feature that tracks row-level changes.
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) – Apache Spark’s incremental processing engine.
- ALTER SHARE – The SQL command to enable history sharing on a share.

## Sources

- read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md

# Citations

1. [read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md](/references/read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws-a44c61ff.md)
