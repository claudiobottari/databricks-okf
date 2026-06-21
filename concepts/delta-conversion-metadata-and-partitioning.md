---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9dac58ad610711edf1415a7ce31f92763a3fca876cbd1095920a8c3d9b0e0beb
  pageDirectory: concepts
  sources:
    - convert-to-delta-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-conversion-metadata-and-partitioning
    - Partitioning and Delta Conversion Metadata
    - DCMAP
  citations:
    - file: convert-to-delta-databricks-on-aws.md
title: Delta Conversion Metadata and Partitioning
description: How CONVERT TO DELTA handles partition specifications from the metastore or explicit PARTITIONED BY clauses, with validation against directory structure.
tags:
  - delta-lake
  - partitioning
  - metadata
timestamp: "2026-06-18T11:10:44.242Z"
---

# Delta Conversion Metadata and Partitioning

**Delta Conversion Metadata and Partitioning** refers to the metadata and partitioning information that [Delta Lake](/concepts/delta-lake.md) generates when converting an existing Apache Parquet or [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) table to a Delta table using the `CONVERT TO DELTA` command. The conversion process creates a Delta Lake transaction log, infers the data schema, and establishes partitioning rules that govern the converted table. ^[convert-to-delta-databricks-on-aws.md]

## Conversion Process

When `CONVERT TO DELTA` runs, it lists all files in the directory, creates a [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) that tracks these files, and automatically infers the data schema by reading the footers of all Parquet files. The conversion process collects statistics to improve query performance on the converted Delta table. If a table name is provided, the [Metastore](/concepts/metastore.md) is also updated to reflect that the table is now a Delta table. ^[convert-to-delta-databricks-on-aws.md]

For [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) tables whose underlying file format is Parquet, the converter generates the Delta Lake transaction log based on the Iceberg table's native file manifest, schema, and partitioning information. ^[convert-to-delta-databricks-on-aws.md]

## Syntax

```sql
CONVERT TO DELTA table_name [ NO STATISTICS ] [ PARTITIONED BY clause ]
```

The command supports converting both Parquet and Iceberg file directories. ^[convert-to-delta-databricks-on-aws.md]

## Parameters

- **table_name**: An optionally qualified table identifier or a path to a `parquet` or `iceberg` file directory. The name must not include a temporal specification or options specification. For Iceberg tables, you can only use paths, as converting managed Iceberg tables is not supported. ^[convert-to-delta-databricks-on-aws.md]

- **NO STATISTICS**: Bypasses statistics collection during the conversion process and finishes conversion faster. After the table is converted to Delta Lake, Databricks recommends using [Liquid Clustering](/concepts/liquid-clustering.md) to reorganize the data layout and generate statistics. ^[convert-to-delta-databricks-on-aws.md]

- **PARTITIONED BY**: Partitions the created table by the specified columns. When `table_name` is a path, `PARTITIONED BY` is required for partitioned data. When the `table_name` is a qualified table identifier, `PARTITIONED BY` clause is optional and the partition specification is loaded from the [Metastore](/concepts/metastore.md). In either approach, the conversion process aborts and throws an exception if the directory structure does not conform to the provided or loaded `PARTITIONED BY` specification. In Databricks Runtime 11.1 and below, `PARTITIONED BY` was a required argument for all partitioned data. ^[convert-to-delta-databricks-on-aws.md]

## Partitioning Requirements

You do not need to provide partitioning information for Iceberg tables or tables registered to the [Metastore](/concepts/metastore.md). ^[convert-to-delta-databricks-on-aws.md]

## Examples

```sql
CONVERT TO DELTA database_name.table_name; -- only for Parquet tables
CONVERT TO DELTA parquet.`s3://my-bucket/path/to/table` PARTITIONED BY (date DATE); -- if the table is partitioned
CONVERT TO DELTA iceberg.`s3://my-bucket/path/to/table`; -- uses Iceberg manifest for metadata
```

## Metadata Considerations

`CONVERT` populates catalog information — such as schema and table properties — to the Delta Lake transaction log. If the underlying directory has already been converted to Delta Lake and its metadata is different from the catalog metadata, a `convertMetastoreMetadataMismatchException` is thrown. ^[convert-to-delta-databricks-on-aws.md]

While using Databricks Runtime, if you want `CONVERT` to overwrite the existing metadata in the Delta Lake transaction log, set the SQL configuration `spark.databricks.delta.convert.metadataCheck.enabled` to `false`. ^[convert-to-delta-databricks-on-aws.md]

## Caveats

Any file not tracked by Delta Lake is invisible and can be deleted when you run `VACUUM`. You should avoid updating or appending data files during the conversion process. After the table is converted, make sure all writes go through [Delta Lake](/concepts/delta-lake.md). ^[convert-to-delta-databricks-on-aws.md]

It is possible that multiple external tables share the same underlying Parquet directory. In this case, if you run `CONVERT` on one of the external tables, you will not be able to access the other external tables because their underlying directory has been converted from Parquet to [Delta Lake](/concepts/delta-lake.md). To query or write to these external tables again, you must run `CONVERT` on them as well. ^[convert-to-delta-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The open-source storage layer that provides ACID transactions
- [Transaction log](/concepts/delta-transaction-log.md) — The metadata foundation of Delta Lake
- Apache Parquet — The columnar storage format that Delta Lake tables are based on
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — Another table format that can be converted to Delta Lake
- [Liquid Clustering](/concepts/liquid-clustering.md) — Recommended method for reorganizing data layout after conversion
- VACUUM — The command that cleans up files not tracked by Delta Lake
- Table identifier — The naming syntax for referencing tables in SQL

## Sources

- convert-to-delta-databricks-on-aws.md

# Citations

1. [convert-to-delta-databricks-on-aws.md](/references/convert-to-delta-databricks-on-aws-4b099753.md)
