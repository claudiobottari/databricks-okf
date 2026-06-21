---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 92f46bec3c00cf213a8dff46768e96777c5b2b6ebcc2d4688e698e940ecc26fa
  pageDirectory: concepts
  sources:
    - read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-profile-path-syntax
    - OPPS
  citations:
    - file: read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md
title: OpenSharing Profile Path Syntax
description: The URL-like path format '<profile-path>#<share-name>.<schema-name>.<table-name>' used to locate shared tables in Spark DataFrame read operations.
tags:
  - syntax
  - data-sharing
  - apache-spark
  - databricks
timestamp: "2026-06-19T20:12:14.738Z"
---

---

title: OpenSharing Profile Path Syntax
summary: The syntax for constructing the path used to read OpenSharing shared tables with Apache Spark DataFrames, including support for change data feed and structured streaming.
sources:
  - read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T12:00:00.000Z"
updatedAt: "2026-06-19T12:00:00.000Z"
tags:
  - opensharing
  - delta-sharing
  - spark-dataframe
  - syntax
aliases:
  - opensharing-profile-path-syntax
  - OPSP
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# OpenSharing Profile Path Syntax

The **OpenSharing Profile Path Syntax** defines how to construct the file path used with Apache Spark DataFrame read operations when querying data shared via [OpenSharing (Delta Sharing)](/concepts/opensharing-delta-sharing.md). This syntax is used with the `deltasharing` format keyword and supports batch reads, change data feed (CDF), and Structured Streaming. ^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]

## Path Structure

The profile path consists of three parts separated by a `#` and dots:

```
<profile-path>#<share-name>.<schema-name>.<table-name>
```

- **`<profile-path>`** – The location of the OpenSharing profile file (e.g., a local path or a URI) that contains the credentials and endpoint for the share provider.
- **`<share-name>`** – The name of the share being accessed.
- **`<schema-name>`** – The schema (namespace) within the share.
- **`<table-name>`** – The specific table to read.

The entire string is passed as the argument to the `.load()` method of a Spark DataFrameReader. ^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]

## Usage Examples

### Batch Read

To read a shared table in batch mode, specify `format("deltasharing")` and provide the profile path as the load argument:

```python
df = (spark.read
  .format("deltasharing")
  .load("<profile-path>#<share-name>.<schema-name>.<table-name>"))
```

^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]

### Change Data Feed (CDF)

If the source table has [change data feed](/concepts/delta-change-data-feed-cdf.md) enabled and history sharing is enabled on the share, you can read CDF records by setting the `readChangeFeed` option to `true` and optionally specifying `startingTimestamp` and `endingTimestamp`:

```python
df = (spark.read
  .format("deltasharing")
  .option("readChangeFeed", "true")
  .option("startingTimestamp", "2021-04-21 05:45:46")
  .option("endingTimestamp", "2021-05-21 12:00:00")
  .load("<profile-path>#<share-name>.<schema-name>.<table-name>"))
```

History sharing requires Databricks Runtime 12.2 LTS or above. ^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]

### Structured Streaming

For tables with history sharing enabled, the profile path can also be used as a source for [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md):

```python
streaming_df = (spark.readStream
  .format("deltasharing")
  .load("<profile-path>#<share-name>.<schema-name>.<table-name>"))
```

If change data feed is also enabled on the source table, you can stream CDF records:

```python
streaming_cdf_df = (spark.readStream
  .format("deltasharing")
  .option("readChangeFeed", "true")
  .option("startingTimestamp", "2021-04-21 05:45:46")
  .load("<profile-path>#<share-name>.<schema-name>.<table-name>"))
```

Structured Streaming with OpenSharing requires Databricks Runtime 12.2 LTS or above. ^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]

## Related Concepts

- [OpenSharing (Delta Sharing)](/concepts/opensharing-delta-sharing.md) – The open protocol for sharing data across platforms.
- [Delta Sharing Recipient Setup](/concepts/delta-sharing-recipient-object.md) – How recipients configure access to shared data.
- [Apache Spark DataFrame](/concepts/apache-spark-dataframes-to-tfrecord-conversion.md) – The core data structure used for reading shared tables.
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) – Incremental data change tracking on Delta tables.
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) – Stream processing engine for continuous data ingestion.
- ALTER SHARE – DDL command to enable history sharing on a share.

## Sources

- read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md

# Citations

1. [read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md](/references/read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws-a44c61ff.md)
