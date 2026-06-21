---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f513137ddbbf50ea3bc164698acca8507c5129b4e0a3ffe211203e896b3a8672
  pageDirectory: concepts
  sources:
    - convert-to-delta-databricks-on-aws.md
  confidence: 0.94
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - partitioned-conversion-and-metastore-metadata
    - Metastore Metadata and Partitioned Conversion
    - PCAMM
  citations:
    - file: convert-to-delta-databricks-on-aws.md
title: Partitioned Conversion and Metastore Metadata
description: When converting partitioned data, PARTITIONED BY is required for path-based tables; mismatches between catalog metadata and the Delta transaction log throw a convertMetastoreMetadataMismatchException.
tags:
  - partitioning
  - delta-lake
  - metastore
timestamp: "2026-06-18T14:44:44.331Z"
---

# Partitioned Conversion and [Metastore](/concepts/metastore.md) Metadata

**Partitioned Conversion and [Metastore](/concepts/metastore.md) Metadata** describes how the `CONVERT TO DELTA` command handles partition specifications and interacts with the Unity Catalog or Hive [Metastore](/concepts/metastore.md) when converting an existing Parquet or Iceberg table to a [Delta Lake](/concepts/delta-lake.md) table. Understanding these mechanics is essential for a successful conversion, especially when the target table is registered in a [Metastore](/concepts/metastore.md) and already contains partition information.

## Overview

`CONVERT TO DELTA` transforms a directory of Apache Parquet files into a Delta table by listing all files, creating a Delta transaction log, inferring the schema from the Parquet footers, and collecting statistics. For partitioned tables, the command must know the partition columns to correctly interpret the directory layout. The partition specification can either be provided explicitly in the SQL statement or, for tables already registered in a [Metastore](/concepts/metastore.md), loaded automatically from the catalog metadata. ^[convert-to-delta-databricks-on-aws.md]

## Partitioned Conversion

The behavior of `CONVERT TO DELTA` with respect to partitioning depends on how the table is referenced:

- **When `table_name` is a path** (e.g., `parquet.'s3://bucket/path'`), the `PARTITIONED BY` clause is **required** for partitioned data. The command checks whether the directory structure matches the given partition columns; if it does not, the conversion aborts with an exception. ^[convert-to-delta-databricks-on-aws.md]
- **When `table_name` is a qualified table identifier** (e.g., `database_name.table_name`), the `PARTITIONED BY` clause is **optional**. If omitted, the partition specification is loaded from the [Metastore](/concepts/metastore.md). The same conformance check applies: the on‑disk directory layout must match the metastore’s partition definition. ^[convert-to-delta-databricks-on-aws.md]

In Databricks Runtime 11.1 and earlier, `PARTITIONED BY` was a required argument for all partitioned data, even for tables registered in the [Metastore](/concepts/metastore.md). ^[convert-to-delta-databricks-on-aws.md]

For Iceberg tables (supported only when the underlying file format is Parquet), you do **not** need to provide partitioning information. The converter reads the Iceberg manifest to obtain the schema, partitioning, and file layout. ^[convert-to-delta-databricks-on-aws.md]

## [Metastore](/concepts/metastore.md) Metadata Handling

During conversion, `CONVERT TO DELTA` populates the Delta transaction log with catalog information such as the table schema and table properties. This metadata is taken from the [Metastore](/concepts/metastore.md) when a qualified table name is used. ^[convert-to-delta-databricks-on-aws.md]

If the directory has **already been converted** to Delta Lake (i.e., a transaction log already exists) and the catalog metadata differs from the metadata already in the transaction log, the command raises a `convertMetastoreMetadataMismatchException`. This prevents accidental overwrites that could cause inconsistency between the catalog and the Delta log. ^[convert-to-delta-databricks-on-aws.md]

To force an overwrite of the existing Delta metadata with the catalog’s values, you can set the SQL configuration `spark.databricks.delta.convert.metadataCheck.enabled` to `false`. This is available only in Databricks Runtime. ^[convert-to-delta-databricks-on-aws.md]

## The `NO STATISTICS` Option

The `NO STATISTICS` option bypasses statistics collection during conversion, making the process faster. After conversion, Databricks recommends using [Liquid Clustering](/concepts/liquid-clustering.md) to reorganize the data and generate statistics. The option is independent of partitioned conversion but is available for any conversion. ^[convert-to-delta-databricks-on-aws.md]

## Caveats

- During conversion, **no external writes** (e.g., Spark jobs writing Parquet directly) should be happening to the underlying directory. Files not tracked by Delta become invisible and can be removed by `VACUUM`. ^[convert-to-delta-databricks-on-aws.md]
- If multiple external tables share the same Parquet directory, converting one prevents access to the others until they are also converted. ^[convert-to-delta-databricks-on-aws.md]

## Related Concepts

- [CONVERT TO DELTA](/concepts/convert-to-delta.md) — The full SQL command syntax and parameters
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — The foundation of Delta table metadata
- Partitioned Data — How partitioning affects storage and query performance
- [Liquid Clustering](/concepts/liquid-clustering.md) — Recommended after conversion for better data layout and statistics
- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) — The catalog that stores table metadata including partition specs

## Sources

- convert-to-delta-databricks-on-aws.md

# Citations

1. [convert-to-delta-databricks-on-aws.md](/references/convert-to-delta-databricks-on-aws-4b099753.md)
