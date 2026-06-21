---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 966df755ef52d0dcc824ddc60c77be382d3dd2a89c1841d4e2d3b506541416d9
  pageDirectory: concepts
  sources:
    - convert-to-delta-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - in-place-table-conversion
    - ITC
    - in-place-table-format-conversion
    - ITFC
  citations:
    - file: convert-to-delta-databricks-on-aws.md
title: In-place Table Conversion
description: The approach of converting Parquet or Iceberg tables to Delta Lake format without copying or rewriting data files, only generating a new transaction log.
tags:
  - delta-lake
  - data-migration
  - etl
timestamp: "2026-06-18T11:10:27.994Z"
---

# In-place Table Conversion

**In-place table conversion** is the process of transforming an existing Apache Parquet or Apache Iceberg table into a [Delta Lake](/concepts/delta-lake.md) table without moving or rewriting the underlying data files. The `CONVERT TO DELTA` command accomplishes this by building a Delta Lake transaction log that references the existing files, thereby making the table immediately queryable as a Delta table while preserving the original data.^[convert-to-delta-databricks-on-aws.md]

## Syntax

```sql
CONVERT TO DELTA table_name [ NO STATISTICS ] [ PARTITIONED BY clause ]
```

^[convert-to-delta-databricks-on-aws.md]

## Parameters

- **table_name**  
  An optionally qualified table identifier or a path to a Parquet or Iceberg file directory. The name must not include a temporal specification or options specification. For Iceberg tables, only paths are supported; converting managed Iceberg tables is not supported.^[convert-to-delta-databricks-on-aws.md]

- **NO STATISTICS**  
  Bypasses statistics collection during the conversion and finishes faster. After conversion, Databricks recommends using [Liquid Clustering](/concepts/liquid-clustering.md) to reorganize the data layout and generate statistics.^[convert-to-delta-databricks-on-aws.md]

- **PARTITIONED BY**  
  Partitions the created table by the specified columns. When `table_name` is a path, `PARTITIONED BY` is required for partitioned data. When the table name is a qualified table identifier, the clause is optional and the partition specification is loaded from the [Metastore](/concepts/metastore.md). The conversion aborts with an exception if the directory structure does not conform to the provided or loaded specification.^[convert-to-delta-databricks-on-aws.md]  
  *In Databricks Runtime 11.1 and below, `PARTITIONED BY` is a required argument for all partitioned data.*^[convert-to-delta-databricks-on-aws.md]

## How Conversion Works

The command lists all files in the directory, creates a Delta Lake transaction log that tracks these files, and automatically infers the data schema by reading the footers of all Parquet files. The conversion process also collects statistics to improve query performance on the converted Delta table. If you provide a table name, the [Metastore](/concepts/metastore.md) is updated to reflect that the table is now a Delta table.^[convert-to-delta-databricks-on-aws.md]

For Iceberg tables whose underlying file format is Parquet, the converter generates the Delta Lake transaction log based on the Iceberg table’s native file manifest, schema, and partitioning information — no file scanning is needed.^[convert-to-delta-databricks-on-aws.md]

## Examples

```sql
-- Convert a Parquet table registered in the [[metastore|Metastore]]
CONVERT TO DELTA database_name.table_name;

-- Convert a partitioned Parquet directory
CONVERT TO DELTA parquet.`s3://my-bucket/path/to/table`
  PARTITIONED BY (date DATE);

-- Convert an Iceberg table (path only)
CONVERT TO DELTA iceberg.`s3://my-bucket/path/to/table`;
```

^[convert-to-delta-databricks-on-aws.md]

Note that partitioning information does not need to be provided for Iceberg tables or tables already registered to the [Metastore](/concepts/metastore.md).^[convert-to-delta-databricks-on-aws.md]

## Caveats

- **File visibility**: Any file not tracked by Delta Lake after conversion is invisible and can be deleted by VACUUM. Avoid updating or appending data files during the conversion process. After conversion, all writes must go through Delta Lake.^[convert-to-delta-databricks-on-aws.md]

- **Shared external directories**: If multiple external tables share the same underlying Parquet directory, converting one table makes the others inaccessible because the directory is converted from Parquet to Delta Lake. To query those other tables again, you must run `CONVERT` on them as well.^[convert-to-delta-databricks-on-aws.md]

- **Metadata mismatch**: `CONVERT` populates catalog information (schema, table properties) into the Delta Lake transaction log. If the underlying directory has already been converted and its metadata differs from the catalog metadata, a `convertMetastoreMetadataMismatchException` is thrown. To override existing metadata in the Delta log, set the SQL configuration `spark.databricks.delta.convert.metadataCheck.enabled` to `false` (available in Databricks Runtime).^[convert-to-delta-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that provides ACID transactions and time travel.
- [Liquid Clustering](/concepts/liquid-clustering.md) — Recommended after `NO STATISTICS` conversion to reorganize data and generate statistics.
- VACUUM — Removes files not tracked by the Delta transaction log.
- PARTITIONED BY — Clause for specifying table partitioning during conversion.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — Alternative open table format that can be converted to Delta Lake in-place.

## Sources

- convert-to-delta-databricks-on-aws.md

# Citations

1. [convert-to-delta-databricks-on-aws.md](/references/convert-to-delta-databricks-on-aws-4b099753.md)
