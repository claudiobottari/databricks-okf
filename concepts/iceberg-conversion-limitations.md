---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 57e0ced12e1cb0eea60b7c8fb2eb1d06c155f3141970534a73d3afa2f9ed45db
  pageDirectory: concepts
  sources:
    - convert-to-delta-lake-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - iceberg-conversion-limitations
    - ICL
    - iceberg-table-conversion-limitations
    - ITCL
    - iceberg-to-delta-conversion-limitations
    - ITDCL
    - iceberg-to-delta-lake-conversion-limitations
    - ITDLCL
  citations:
    - file: convert-to-delta-lake-databricks-on-aws.md
title: Iceberg Conversion Limitations
description: Known restrictions when converting Apache Iceberg tables to Delta Lake, including unsupported features like partition evolution and metastore tables.
tags:
  - iceberg
  - delta-lake
  - limitations
  - data-migration
timestamp: "2026-06-18T11:10:57.669Z"
---

# Iceberg Conversion Limitations

**Iceberg Conversion Limitations** refers to the constraints and unsupported scenarios when using the `CONVERT TO DELTA` SQL command to perform a one-time conversion of Apache Iceberg tables to [Delta Lake](/concepts/delta-lake.md) tables on Databricks. `CONVERT TO DELTA` is supported for Parquet and Iceberg tables stored in external locations managed by [Unity Catalog](/concepts/unity-catalog.md). For incremental conversion, see [Incremental cloning of Parquet and Iceberg tables](/concepts/incremental-clone-of-parquet-and-iceberg-to-delta-lake.md).^[convert-to-delta-lake-databricks-on-aws.md]

## Supported Runtime Versions

Converting Iceberg tables is supported in **Databricks Runtime 10.4 LTS and above**.^[convert-to-delta-lake-databricks-on-aws.md]

## Unsupported Iceberg Table Types

- **Iceberg [Metastore](/concepts/metastore.md) tables** are not supported for conversion.^[convert-to-delta-lake-databricks-on-aws.md]
- **Iceberg tables that have experienced [partition evolution](https://iceberg.apache.org/docs/latest/evolution/#partition-evolution)** are not supported.^[convert-to-delta-lake-databricks-on-aws.md]

## Truncated Column Partition Limitations

When converting Iceberg tables that define partitions on **truncated columns**, the behavior depends on the column data type and the Databricks Runtime version:

- In **Databricks Runtime 12.2 LTS and below**, only truncated columns of type `string` are supported.^[convert-to-delta-lake-databricks-on-aws.md]
- In **Databricks Runtime 13.3 LTS and above**, truncated columns of types `string`, `long`, or `int` are supported.^[convert-to-delta-lake-databricks-on-aws.md]
- Databricks **does not support** working with truncated columns of type `decimal` in any runtime version.^[convert-to-delta-lake-databricks-on-aws.md]

## Other Requirements

When converting Iceberg directories or external tables to Delta Lake using `CONVERT TO DELTA`:

- You must have **write access** on the storage location.^[convert-to-delta-lake-databricks-on-aws.md]
- To register the converted table as an external table in Unity Catalog, you need the `CREATE EXTERNAL TABLE` permission on the external location.^[convert-to-delta-lake-databricks-on-aws.md]
- Partitioning information must be provided for Unity Catalog external tables (not automatically inferred).^[convert-to-delta-lake-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The target format after conversion
- [CONVERT TO DELTA](/concepts/convert-to-delta.md) — The SQL command used for conversion
- [Parquet to Delta Lake Conversion](/concepts/parquet-to-delta-lake-conversion.md) — Similar conversion for Parquet files
- [Unity Catalog](/concepts/unity-catalog.md) — Governed catalog that supports the command for external tables
- [Incremental cloning of Parquet and Iceberg tables](/concepts/incremental-clone-of-parquet-and-iceberg-to-delta-lake.md) — Alternative approach for incremental conversion
- Databricks Runtime versions — Version‑specific feature support

## Sources

- convert-to-delta-lake-databricks-on-aws.md

# Citations

1. [convert-to-delta-lake-databricks-on-aws.md](/references/convert-to-delta-lake-databricks-on-aws-85c3b3fb.md)
