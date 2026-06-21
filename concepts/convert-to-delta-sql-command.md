---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1e4c1fd9853f88d91d2ac30e2813f3f42420a0f203830080bdcd0f2db4c38746
  pageDirectory: concepts
  sources:
    - convert-to-delta-lake-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - convert-to-delta-sql-command
    - CTDSC
  citations:
    - file: convert-to-delta-databricks-on-aws.md
    - file: convert-to-delta-lake-databricks-on-aws.md
title: CONVERT TO DELTA SQL Command
description: A one-time SQL command that converts Parquet and Apache Iceberg tables to Delta Lake tables on Databricks.
tags:
  - delta-lake
  - migration
  - sql-command
timestamp: "2026-06-19T17:53:02.425Z"
---

# CONVERT TO DELTA (SQL Command)

The `CONVERT TO DELTA` SQL command performs a one-time, in-place conversion of existing Apache Parquet or [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) tables to [Delta Lake](/concepts/delta-lake.md) tables. It creates a Delta Lake transaction log that tracks existing files and infers the schema by reading Parquet file footers. The conversion collects statistics for query performance unless explicitly bypassed. If a table name is provided, the [Metastore](/concepts/metastore.md) is updated to reflect the new Delta format.^[convert-to-delta-databricks-on-aws.md, convert-to-delta-lake-databricks-on-aws.md]

For Iceberg tables whose underlying file format is Parquet, the converter uses the Iceberg table's native file manifest, schema, and partitioning information to generate the transaction log. This approach preserves existing metadata and reduces the need for manual specification.^[convert-to-delta-databricks-on-aws.md]

For incremental conversion of Parquet or Iceberg tables to Delta Lake, see [Incrementally clone Parquet and Apache Iceberg tables to Delta Lake](/concepts/incremental-clone-of-parquet-and-iceberg-to-delta-lake.md).^[convert-to-delta-lake-databricks-on-aws.md]

## Syntax

```sql
CONVERT TO DELTA table_name [ NO STATISTICS ] [ PARTITIONED BY clause ]
```

^[convert-to-delta-databricks-on-aws.md]

## Parameters

### `table_name`

Either an optionally qualified table identifier (e.g., `database_name.table_name`) or a path to a directory containing `parquet` or `iceberg` files. The name must not include a temporal specification or options specification. For Iceberg tables, only paths can be used — converting managed Iceberg tables is not supported.^[convert-to-delta-databricks-on-aws.md, convert-to-delta-lake-databricks-on-aws.md]

### `NO STATISTICS`

Bypasses statistics collection during conversion, making the conversion faster. After the table is converted to Delta Lake, it is recommended to use [Liquid Clustering](/concepts/liquid-clustering.md) to reorganize the data layout and generate statistics.^[convert-to-delta-databricks-on-aws.md]

### `PARTITIONED BY`

Partitions the converted table by the specified columns. When `table_name` is a path, `PARTITIONED BY` is **required** if the data is partitioned. When `table_name` is a qualified table identifier, the partitioning specification is loaded from the [Metastore](/concepts/metastore.md); `PARTITIONED BY` is optional in that case. The command aborts if the directory structure does not match the partitioning specification.^[convert-to-delta-databricks-on-aws.md]

> **Note:** For Databricks Runtime 11.1 and below, `PARTITIONED BY` is a required argument for all partitioned data.^[convert-to-delta-databricks-on-aws.md]

## Examples

```sql
-- Convert a Parquet table registered in the Hive [[metastore|Metastore]]
CONVERT TO DELTA database_name.table_name;

-- Convert a partitioned Parquet table stored at a path
CONVERT TO DELTA parquet.`s3://my-bucket/path/to/table`
  PARTITIONED BY (date DATE);

-- Convert an Iceberg table using its native manifest for metadata
CONVERT TO DELTA iceberg.`s3://my-bucket/path/to/table`;
```

^[convert-to-delta-databricks-on-aws.md, convert-to-delta-lake-databricks-on-aws.md]

> **Note:** You do not need to provide partitioning information for Iceberg tables or tables registered to the [Metastore](/concepts/metastore.md). For Databricks Runtime 11.3 LTS and above, `CONVERT TO DELTA` automatically infers partitioning information for tables registered to the Hive [Metastore](/concepts/metastore.md). You must provide partitioning information for Unity Catalog external tables.^[convert-to-delta-databricks-on-aws.md, convert-to-delta-lake-databricks-on-aws.md]

## Caveats & Limitations

### General Limitations

- **File visibility:** After conversion, any files not tracked by Delta Lake become invisible and can be removed by `VACUUM`. You should avoid updating or appending data files during the conversion process. After conversion, all writes must go through Delta Lake.^[convert-to-delta-databricks-on-aws.md]
- **Shared directories:** If multiple external tables share the same underlying Parquet directory, converting one table will make the others inaccessible because the underlying directory becomes a [Delta Lake Table](/concepts/delta-lake-table.md). To access them again, you must also run `CONVERT` on those other external tables.^[convert-to-delta-databricks-on-aws.md]
- **Metastore metadata mismatch:** If the underlying directory has already been converted to Delta Lake but its metadata differs from the catalog metadata, a `convertMetastoreMetadataMismatchException` is thrown. In Databricks Runtime, you can set `spark.databricks.delta.convert.metadataCheck.enabled` to `false` to overwrite existing metadata.^[convert-to-delta-databricks-on-aws.md]

### Iceberg Conversion Limitations

- Converting Iceberg tables is supported in Databricks Runtime 10.4 LTS and above.
- Converting Iceberg [Metastore](/concepts/metastore.md) tables is **not** supported.
- Converting Iceberg tables that have experienced [partition evolution](https://iceberg.apache.org/docs/latest/evolution/#partition-evolution) is **not** supported.
- For Iceberg tables with partitions on truncated columns:
  - In Databricks Runtime 12.2 LTS and below, only `string` type is supported for truncated columns.
  - In Databricks Runtime 13.3 LTS and above, `string`, `long`, or `int` types are supported.
  - Truncated columns of type `decimal` are **not** supported.

^[convert-to-delta-lake-databricks-on-aws.md]

## Unity Catalog Support

Unity Catalog supports `CONVERT TO DELTA` for Parquet and Iceberg tables stored in external locations managed by Unity Catalog. You can configure existing Parquet data files as [External Tables in Unity Catalog](/concepts/external-tables-in-unity-catalog.md) and then convert them to Delta Lake to unlock all features of the Databricks lakehouse. To load converted tables as external tables into Unity Catalog, you need the `CREATE EXTERNAL TABLE` permission on the external location.^[convert-to-delta-lake-databricks-on-aws.md]

For converting managed and external tables to Delta Lake on Unity Catalog: `CONVERT TO DELTA` syntax can only be used for creating Unity Catalog **external** tables. To convert a legacy Hive [Metastore](/concepts/metastore.md) managed Parquet table directly to a managed Unity Catalog [Delta Lake Table](/concepts/delta-lake-table.md), use a `CREATE TABLE AS SELECT` (CTAS) statement. To upgrade an external Parquet table to a Unity Catalog external table, see [Upgrade a schema or tables from the Hive metastore to Unity Catalog external tables using the upgrade wizard](/concepts/hive-metastore-to-unity-catalog-table-migration.md).^[convert-to-delta-lake-databricks-on-aws.md]

After you've registered an external Parquet table to Unity Catalog, you can convert it to an external [Delta Lake Table](/concepts/delta-lake-table.md). You must provide partitioning information if the Parquet table is partitioned.^[convert-to-delta-lake-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format for converted tables
- Parquet — The source file format for conversion
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — Another source format supported for conversion
- VACUUM — Command to remove unreferenced files after conversion
- [Liquid Clustering](/concepts/liquid-clustering.md) — Recommended after conversion to reorganize data and generate statistics
- [Incrementally clone Parquet and Apache Iceberg tables to Delta Lake](/concepts/incremental-clone-of-parquet-and-iceberg-to-delta-lake.md) — Alternative for incremental migration
- External table — Required for Unity Catalog managed conversions
- [Unity Catalog](/concepts/unity-catalog.md) — Data governance platform supporting external table conversion

## Sources

- convert-to-delta-databricks-on-aws.md
- convert-to-delta-lake-databricks-on-aws.md

# Citations

1. [convert-to-delta-databricks-on-aws.md](/references/convert-to-delta-databricks-on-aws-4b099753.md)
2. [convert-to-delta-lake-databricks-on-aws.md](/references/convert-to-delta-lake-databricks-on-aws-85c3b3fb.md)
