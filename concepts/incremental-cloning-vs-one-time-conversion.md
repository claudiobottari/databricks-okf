---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 959ca029fe1337c78238cf728028c124dda0ee8ffb97041db13f175db4d7598d
  pageDirectory: concepts
  sources:
    - convert-to-delta-lake-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - incremental-cloning-vs-one-time-conversion
    - ICVOC
    - Incremental conversion
  citations:
    - file: convert-to-delta-lake-databricks-on-aws.md
title: Incremental Cloning vs One-Time Conversion
description: Distinction between the one-time CONVERT TO DELTA command and incremental cloning for Parquet and Iceberg tables to Delta Lake
tags:
  - delta-lake
  - data-migration
  - incremental-processing
timestamp: "2026-06-19T09:24:59.134Z"
---

# Incremental Cloning vs One-Time Conversion

**Incremental Cloning vs One-Time Conversion** describes two approaches for migrating existing Parquet and Apache Iceberg tables to [Delta Lake](/concepts/delta-lake.md) format within the Databricks environment. The choice between them depends on whether you need a single bulk conversion or ongoing synchronization of changes.

## One-Time Conversion with `CONVERT TO DELTA`

The `CONVERT TO DELTA` SQL command performs a single, one-time conversion of Parquet and Apache Iceberg tables to Delta Lake tables. ^[convert-to-delta-lake-databricks-on-aws.md]

This command is suitable when you want to convert existing data files in bulk and do not need to capture subsequent changes made to the source data. After conversion, the table becomes a [Delta Lake Table](/concepts/delta-lake-table.md) and benefits from Delta Lake features such as [ACID transactions](/concepts/delta-acid-transactions.md), time travel, and schema enforcement. ^[convert-to-delta-lake-databricks-on-aws.md]

### Supported Formats

- **Parquet**: Supported in all Databricks Runtime versions.
- **Apache Iceberg**: Supported in Databricks Runtime 10.4 LTS and above, with certain limitations. ^[convert-to-delta-lake-databricks-on-aws.md]

### Iceberg Conversion Limitations

- Converting Iceberg [Metastore](/concepts/metastore.md) tables is not supported.
- Converting Iceberg tables that have experienced [partition evolution](/concepts/partition-evolution-in-iceberg.md) is not supported.
- For Iceberg tables with partitions defined on truncated columns:
  - In Databricks Runtime 12.2 LTS and below, only `string` truncated columns are supported.
  - In Databricks Runtime 13.3 LTS and above, `string`, `long`, and `int` truncated columns are supported.
  - `decimal` truncated columns are not supported. ^[convert-to-delta-lake-databricks-on-aws.md]

### Usage

```sql
CONVERT TO DELTA parquet.`s3://my-bucket/parquet-data`;
CONVERT TO DELTA iceberg.`s3://my-bucket/iceberg-data`;
```

^[convert-to-delta-lake-databricks-on-aws.md]

For Unity Catalog external tables, you must provide partitioning information if the Parquet table is partitioned:

```sql
CONVERT TO DELTA catalog_name.database_name.table_name PARTITIONED BY (date_updated DATE);
```

^[convert-to-delta-lake-databricks-on-aws.md]

## Incremental Cloning

For scenarios where you need to continuously synchronize changes from Parquet or Iceberg tables to Delta Lake, Databricks recommends using [Incremental Clone](/concepts/incremental-cloning-to-delta-lake.md) operations instead of one-time conversion. ^[convert-to-delta-lake-databricks-on-aws.md]

Incremental cloning captures only the changes (new, updated, or deleted records) since the last clone operation, making it more efficient for ongoing data synchronization. This approach is documented in the guide on how to incrementally clone Parquet and Apache Iceberg tables to Delta Lake. ^[convert-to-delta-lake-databricks-on-aws.md]

## When to Use Each Approach

| Consideration | One-Time Conversion (`CONVERT TO DELTA`) | Incremental Cloning |
|---------------|------------------------------------------|---------------------|
| **Use case** | Single bulk migration of existing data | Ongoing synchronization of changing source data |
| **Source format** | Parquet, Iceberg | Parquet, Iceberg |
| **Performance** | Processes all data at once | Processes only changes, more efficient for updates |
| **Ongoing sync** | No — one-time operation only | Yes — captures incremental changes |

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The target format for both approaches
- [CONVERT TO DELTA](/concepts/convert-to-delta.md) — Technical documentation for the one-time conversion command
- [Incremental Clone](/concepts/incremental-cloning-to-delta-lake.md) — Technical documentation for incremental synchronization
- [External Locations](/concepts/external-location.md) — How to configure access to cloud storage with Unity Catalog
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer for managing Delta Lake tables

## Sources

- convert-to-delta-lake-databricks-on-aws.md

# Citations

1. [convert-to-delta-lake-databricks-on-aws.md](/references/convert-to-delta-lake-databricks-on-aws-85c3b3fb.md)
