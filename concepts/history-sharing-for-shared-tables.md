---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b10cdb1d39e34a17a35a76bc1245805fd64bc953d97c82f3e8d92b04ebba304b
  pageDirectory: concepts
  sources:
    - read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - history-sharing-for-shared-tables
    - HSFST
  citations:
    - file: read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md
title: History Sharing for Shared Tables
description: A prerequisite feature on OpenSharing shares that enables metadata history, enabling Structured Streaming and change data feed capabilities on shared tables.
tags:
  - data-sharing
  - delta-lake
  - databricks
  - configuration
timestamp: "2026-06-19T20:12:06.943Z"
---

Here is the wiki page for "History Sharing for Shared Tables", based solely on the provided source material.

---

# History Sharing for Shared Tables

**History Sharing for Shared Tables** is a feature in [Delta Sharing](/concepts/delta-sharing.md) that allows recipients to access historical snapshots and change data feed (CDF) records of a shared table. When history sharing is enabled on a share, the shared table becomes eligible for time-travel queries, incremental processing via [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md), and CDF reads. ^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]

## Prerequisites

History sharing requires the following:

- **Databricks Runtime 12.2 LTS or above** on the recipient side. ^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]
- The share must have history **enabled** on the table. This is controlled by the provider using the ALTER SHARE command. ^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]

## Enabling History Sharing

History sharing is enabled at the share level using the `ALTER SHARE` SQL command. The exact syntax is documented in the ALTER SHARE language manual. Once enabled, recipients can query past versions of the table and, if the source Delta table has [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) (CDF) enabled, read row-level change records. ^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]

## Use Cases

### Structured Streaming

When history sharing is enabled, a shared table can be used as a source for Structured Streaming, allowing incremental processing of new records. The following example shows how to set up a streaming read against a shared table: ^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]

```python
streaming_df = (spark.readStream
  .format("deltasharing")
  .load("<profile-path>#<share-name>.<schema-name>.<table-name>"))
```

### Change Data Feed (CDF)

If the shared table has CDF enabled on the source Delta table **and** history enabled on the share, recipients can read CDF records using both batch and streaming DataFrames. The following example reads CDF records between two timestamps: ^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]

```python
df = (spark.read
  .format("deltasharing")
  .option("readChangeFeed", "true")
  .option("startingTimestamp", "2021-04-21 05:45:46")
  .option("endingTimestamp", "2021-05-21 12:00:00")
  .load("<profile-path>#<share-name>.<schema-name>.<table-name>"))
```

CDF can also be consumed via Structured Streaming when both features are enabled: ^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]

```python
streaming_cdf_df = (spark.readStream
  .format("deltasharing")
  .option("readChangeFeed", "true")
  .option("startingTimestamp", "2021-04-21 05:45:46")
  .load("<profile-path>#<share-name>.<schema-name>.<table-name>"))
```

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) – The protocol used for Databricks-to-Databricks sharing.
- [Delta Sharing](/concepts/delta-sharing.md) – The underlying framework for sharing data across platforms.
- ALTER SHARE – The SQL command used to enable history on a share.
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) – Row-level change tracking on Delta tables.
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) – Incremental stream processing on Databricks.
- Read OpenSharing shared tables using Apache Spark DataFrames – General guide for reading shared tables.

## Sources

- read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md

# Citations

1. [read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md](/references/read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws-a44c61ff.md)
