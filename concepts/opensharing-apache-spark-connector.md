---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b42ea6119717b8bfc9edd43c0275e459e9e273ba6502f64f22e7ac9a30611382
  pageDirectory: concepts
  sources:
    - read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-apache-spark-connector
    - OASC
    - OpenSharing Spark Connector
    - Apache Spark connector
    - Iceberg‑Spark connector
  citations:
    - file: read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md
title: OpenSharing Apache Spark Connector
description: A connector that enables reading shared data via Apache Spark using the delta-sharing-spark library, supporting batch queries, change data feed (CDF), structured streaming, deletion vectors, column mapping, and row tracking.
tags:
  - spark
  - delta-sharing
  - streaming
timestamp: "2026-06-19T20:11:13.006Z"
---

# OpenSharing Apache Spark Connector

The **OpenSharing Apache Spark Connector** (also known as the `delta-sharing-spark` connector) allows you to read data shared through the OpenSharing open protocol using Apache Spark 3.x or above. Together with the OpenSharing Python connector, it provides programmatic access to shared tables, change data feeds, and streaming sources. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

If your Databricks workspace is enabled for [Unity Catalog](/concepts/unity-catalog.md) and you have imported the provider using the Import provider UI, you do **not** need to install this connector or provide a credential file path — shared tables appear as standard Unity Catalog objects and can be queried with normal SQL or DataFrame APIs. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Prerequisites

- A credential file (`.share` or `config.share`) shared by the data provider. See Get access in the Databricks-to-Open sharing model.
- Apache Spark 3.x or above.
- The credential file must be accessible via an absolute path (local file, cloud object, or Unity Catalog volume).

## Installation

Install the OpenSharing Python connector and the Apache Spark connector:

```bash
pip install delta-sharing
```

This installs the Python connector and also makes the Spark connector (`delta-sharing-spark`) available. For the latest version and additional details, see the [OpenSharing connectors documentation](https://opensharing.io/). ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Listing shared tables

Use the `SharingClient` to list all tables shared with you:

```python
import delta_sharing

client = delta_sharing.SharingClient(f"<profile-path>/config.share")
client.list_all_tables()
```

The result is an array of `Table` objects, each containing the `share`, `schema`, and `name` of the table. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Accessing shared data

You can load a shared table into a Spark DataFrame using either the `load_as_spark` function or the `format("deltaSharing")` reader:

```python
# Using load_as_spark
delta_sharing.load_as_spark(
    f"<profile-path>#<share-name>.<schema-name>.<table-name>"
)

# Using DataFrameReader
spark.read.format("deltaSharing").load(
    "<profile-path>#<share-name>.<schema-name>.<table-name>"
)
```

Both methods accept optional `version` or `timestamp` parameters to read a specific snapshot of the table. Version-based queries require `delta-sharing-spark` 0.5.0 or above; timestamp-based queries require 0.6.0 or above. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Change data feed (CDF)

If the data provider has shared the table history and the table’s change data feed is enabled, you can read row-level changes between versions or timestamps:

```python
# Using load_table_changes_as_spark
delta_sharing.load_table_changes_as_spark(
    f"<profile-path>#<share-name>.<schema-name>.<table-name>",
    starting_version=<starting-version>,
    ending_version=<ending-version>
)

# Using DataFrameReader options
spark.read.format("deltaSharing") \
    .option("readChangeFeed", "true") \
    .option("startingVersion", <starting-version>) \
    .option("endingVersion", <ending-version>) \
    .load("<profile-path>#<share-name>.<schema-name>.<table-name>")
```

You can also specify `starting_timestamp` and `ending_timestamp` instead of version numbers. The `starting_version` or `starting_timestamp` is required. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Structured Streaming

When the table history is shared, you can read shared data as a streaming source using `readStream.format("deltaSharing")`. Requires `delta-sharing-spark` 0.6.0 or above.

Supported options:
- `ignoreDeletes`, `ignoreChanges`
- `startingVersion`, `startingTimestamp`
- `maxFilesPerTrigger`, `maxBytesPerTrigger`
- `readChangeFeed` – stream the change data feed

Unsupported option:
- `Trigger.availableNow`

Example:

```python
spark.readStream.format("deltaSharing") \
    .option("startingVersion", 0) \
    .option("ignoreDeletes", True) \
    .option("maxBytesPerTrigger", 10000) \
    .load("<profile-path>#<share-name>.<schema-name>.<table-name>")
```

^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Reading tables with deletion vectors or column mapping

If the provider enabled [Deletion Vectors](/concepts/deletion-vectors.md) or [column mapping](/concepts/column-mapping-in-delta-lake.md) on the shared Delta table, you need:

- `delta-sharing-spark` 3.1 or above
- For batch reads: Databricks Runtime 14.1 or above
- For CDF or streaming queries: Databricks Runtime 14.2 or above

When performing CDF or streaming reads on such tables, you must set the option `responseFormat=delta`:

```scala
spark.read.format("deltaSharing")
  .option("responseFormat", "delta")
  .load(tablePath)
```

Batch queries work without setting `responseFormat` because the connector automatically resolves the format. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Reading row tracking columns

If the provider enabled row tracking on the shared table, you can query row tracking metadata columns using Scala Spark. You must set `responseFormat=delta`:

```scala
spark.read.format("deltaSharing")
  .option("responseFormat", "delta")
  .load("<profile-path>#<share-name>.<schema-name>.<table-name>")
  .select("_metadata.row_id")
  .show()
```

Only the delta response format is supported for row tracking columns. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Limitations

### General Python connector limitations
- The OpenSharing Python connector 1.1.0+ supports snapshot queries on tables with column mapping, but CDF queries on tables with column mapping are **not** supported.
- The Python connector fails CDF queries with `use_delta_format=True` if the schema changed during the queried version range. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

### Streaming table limitations
You can only read the **current snapshot** of a shared streaming table. The following features are **not** supported:
- Querying table history
- Querying the change data feed (CDF)
- Using the table as a source for Spark Structured Streaming ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

### Materialized view limitations
You can only read the current snapshot of a shared materialized view. It cannot be used as a source for Spark Structured Streaming. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Related concepts

- [OpenSharing](/concepts/opensharing.md) – The open protocol for sharing data across platforms.
- [Delta Sharing](/concepts/delta-sharing.md) – The underlying data sharing protocol used by OpenSharing.
- Apache Spark – The distributed computing framework used by this connector.
- [Unity Catalog](/concepts/unity-catalog.md) – Databricks’ [Metastore](/concepts/metastore.md) that integrates with OpenSharing.
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) – Feature that provides row-level changes between table versions.
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) – Spark’s stream processing engine used with shared tables.
- [Deletion Vectors](/concepts/deletion-vectors.md) – Storage optimization feature that may be enabled on shared tables.
- [Column Mapping](/concepts/delta-table-column-mapping.md) – Feature supporting column renaming and dropping in Delta tables.
- Row Tracking – Feature that provides unique row identifiers in Delta tables.

## Sources

- read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md

# Citations

1. [read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md](/references/read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws-9252dd38.md)
