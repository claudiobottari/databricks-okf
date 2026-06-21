---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 46bf34f85549aa6bdd5e93501e4eed8adad0fcbb256676657a89c48e5c786fd1
  pageDirectory: concepts
  sources:
    - convert-to-delta-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - parquet-to-delta-conversion
    - Parquet Table Conversion
  citations:
    - file: convert-to-delta-databricks-on-aws.md
title: Parquet-to-Delta Conversion
description: The process of converting an existing Apache Parquet table to Delta Lake by listing files, creating a transaction log, and inferring schema by reading Parquet file footers.
tags:
  - delta-lake
  - parquet
  - data-migration
timestamp: "2026-06-19T14:25:52.514Z"
---

# Parquet-to-Delta Conversion

**Parquet-to-Delta Conversion** refers to the process of converting an existing Apache Parquet table into a [Delta Lake](/concepts/delta-lake.md) table in-place using the `CONVERT TO DELTA` SQL command. The command creates a Delta Lake transaction log that tracks the existing Parquet files, infers the schema from the Parquet file footers, and collects statistics to improve query performance on the converted table. If a table name is provided, the [Metastore](/concepts/metastore.md) is also updated to reflect that the table is now a Delta table. ^[convert-to-delta-databricks-on-aws.md]

## Overview

The `CONVERT TO DELTA` command lists all files in the directory, creates a Delta Lake transaction log, and automatically infers the data schema by reading the footers of all Parquet files. The conversion process collects statistics to enhance query performance on the converted Delta table. For tables whose underlying file format is Parquet and that are registered as [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) tables, the converter generates the Delta Lake transaction log based on the Iceberg table's native file manifest, schema, and partitioning information. ^[convert-to-delta-databricks-on-aws.md]

## Syntax

```sql
CONVERT TO DELTA table_name [ NO STATISTICS ] [ PARTITIONED BY clause ]
```

^[convert-to-delta-databricks-on-aws.md]

## Parameters

### `table_name`
An optionally qualified table identifier or a path to a Parquet or Iceberg file directory. The name must not include a temporal or options specification. For Iceberg tables, only paths are supported; converting managed Iceberg tables is not allowed. ^[convert-to-delta-databricks-on-aws.md]

### `NO STATISTICS`
Bypasses statistics collection during the conversion process, finishing the conversion faster. After the table is converted to Delta Lake, it is recommended to use [Liquid Clustering](/concepts/liquid-clustering.md) to reorganize the data layout and generate statistics. ^[convert-to-delta-databricks-on-aws.md]

### `PARTITIONED BY`
Partitions the created table by the specified columns. When `table_name` is a path, `PARTITIONED BY` is required for partitioned data. When `table_name` is a qualified table identifier, the `PARTITIONED BY` clause is optional, and the partition specification is loaded from the [Metastore](/concepts/metastore.md). The conversion process aborts and throws an exception if the directory structure does not conform to the provided or loaded partition specification. ^[convert-to-delta-databricks-on-aws.md]

> **Note:** In Databricks Runtime 11.1 and below, `PARTITIONED BY` is a required argument for all partitioned data. ^[convert-to-delta-databricks-on-aws.md]

## Examples

The following examples demonstrate typical usage:

```sql
-- Convert a Parquet table registered in the [[metastore|Metastore]]
CONVERT TO DELTA database_name.table_name;

-- Convert a partitioned Parquet table located at a path
CONVERT TO DELTA parquet.`s3://my-bucket/path/to/table` PARTITIONED BY (date DATE);

-- Convert an Iceberg table (uses Iceberg manifest for metadata)
CONVERT TO DELTA iceberg.`s3://my-bucket/path/to/table`;
```

^[convert-to-delta-databricks-on-aws.md]

## Caveats

- Any file not tracked by Delta Lake becomes invisible and can be deleted when running `VACUUM`. To avoid data loss, avoid updating or appending data files during the conversion process. After the table is converted, all writes must go through Delta Lake. ^[convert-to-delta-databricks-on-aws.md]

- If multiple external tables share the same underlying Parquet directory, running `CONVERT TO DELTA` on one table will make the other external tables inaccessible because the underlying directory has been converted from Parquet to Delta Lake. To query or write to those other tables again, you must run `CONVERT TO DELTA` on them as well. ^[convert-to-delta-databricks-on-aws.md]

- The `CONVERT` command populates catalog information (schema, table properties) into the Delta Lake transaction log. If the underlying directory has already been converted to Delta Lake and its metadata differs from the catalog metadata, a `convertMetastoreMetadataMismatchException` is thrown. To overwrite the existing metadata in the Delta Lake transaction log, set the SQL configuration `spark.databricks.delta.convert.metadataCheck.enabled` to `false` (Databricks Runtime only). ^[convert-to-delta-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The open-source storage layer that provides transactions and schema enforcement.
- Parquet – The columnar storage format being converted.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – Another table format that can be converted when it uses Parquet files.
- [Liquid Clustering](/concepts/liquid-clustering.md) – Recommended post-conversion step for data layout reorganization and statistics generation.
- VACUUM – The command that removes files not tracked by Delta Lake.
- Delta Lake partition pruning – How partitioning accelerates queries.

## Sources

- convert-to-delta-databricks-on-aws.md

# Citations

1. [convert-to-delta-databricks-on-aws.md](/references/convert-to-delta-databricks-on-aws-4b099753.md)
