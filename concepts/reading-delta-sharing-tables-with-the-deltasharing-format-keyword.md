---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 20c9a0315c1de9cf2614b9d9af1f8157ba719621c21469878b39971c901e4793
  pageDirectory: concepts
  sources:
    - read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - reading-delta-sharing-tables-with-the-deltasharing-format-keyword
    - RDSTWTDFK
  citations:
    - file: read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md
title: Reading Delta Sharing Tables with the deltasharing Format Keyword
description: Using .format('deltasharing') in Apache Spark DataFrames to read shared tables from an OpenSharing provider.
tags:
  - apache-spark
  - dataframes
  - data-sharing
  - databricks
timestamp: "2026-06-19T20:11:58.376Z"
---

## Reading Delta Sharing Tables with the `deltasharing` Format Keyword

The **`deltasharing`** keyword is a Spark format option that enables reading data shared through [OpenSharing](/concepts/opensharing.md) (also called [Delta Sharing](/concepts/delta-sharing.md)) using Apache Spark DataFrames. It is used with `.format("deltasharing")` in DataFrame reader operations. ^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]

When an OpenSharing catalog is registered in the [Metastore](/concepts/metastore.md), you can also query shared tables using their table name directly in SQL or Python, for example:

```sql
SELECT * FROM shared_table_name
```

For more information on configuring OpenSharing and querying with table names, see Read data shared using Databricks-to-Databricks OpenSharing (for recipients). ^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]

### Basic Read

To load a shared table with the `deltasharing` format, provide a profile path followed by the fully qualified table name (share.schema.table):

```python
df = (spark.read
  .format("deltasharing")
  .load("<profile-path>#<share-name>.<schema-name>.<table-name>"))
```

This returns a DataFrame with the current snapshot of the shared table. ^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]

### Reading with Change Data Feed

If the source Delta table has [change data feed](/concepts/delta-change-data-feed-cdf.md) enabled **and** the share has history shared, you can read change data feed records using the `readChangeFeed` option. History sharing requires Databricks Runtime **12.2 LTS or above**. ^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]

```python
df = (spark.read
  .format("deltasharing")
  .option("readChangeFeed", "true")
  .option("startingTimestamp", "2021-04-21 05:45:46")
  .option("endingTimestamp", "2021-05-21 12:00:00")
  .load("<profile-path>#<share-name>.<schema-name>.<table-name>"))
```

### Structured Streaming

You can use [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) to incrementally process records from a shared table that has history sharing enabled. This also requires Databricks Runtime 12.2 LTS or above. ^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]

```python
streaming_df = (spark.readStream
  .format("deltasharing")
  .load("<profile-path>#<share-name>.<schema-name>.<table-name>"))
```

If change data feed is also enabled on the source table, you can stream the change feed with `readChangeFeed` and a starting timestamp:

```python
streaming_cdf_df = (spark.readStream
  .format("deltasharing")
  .option("readChangeFeed", "true")
  .option("startingTimestamp", "2021-04-21 05:45:46")
  .load("<profile-path>#<share-name>.<schema-name>.<table-name>"))
```

### Enabling History Sharing

For history sharing to work, it must be enabled on the share using the `ALTER SHARE` command. See ALTER SHARE in the SQL language reference. ^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]

### Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol for sharing data across platforms.
- [OpenSharing](/concepts/opensharing.md) – Databricks implementation of the Delta Sharing protocol.
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) – Tracks row-level changes in Delta tables.
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) – Incremental stream processing in Spark.
- [Read data shared using Databricks-to-Databricks OpenSharing](/concepts/databricks-to-databricks-sharing.md) – Alternative ways to query shared data.
- Spark DataFrame Reader – General Spark API for reading data.

### Sources

- read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md

# Citations

1. [read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md](/references/read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws-a44c61ff.md)
