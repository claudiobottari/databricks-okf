---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e41fcac4bfa9e85902faad32dd3fa1abaa1bbe5f89cb13bbb82d186e7c0bbc3c
  pageDirectory: concepts
  sources:
    - migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - convert-to-delta
    - CTD
  citations:
    - file: migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md
title: CONVERT TO DELTA
description: A SQL command that transforms an existing directory of Parquet files into a Delta table in a single operation.
tags:
  - delta-lake
  - data-migration
  - sql
timestamp: "2026-06-19T19:31:58.314Z"
---

# CONVERT TO DELTA

**CONVERT TO DELTA** is a SQL command that transforms a directory of Parquet files into a [Delta Lake](/concepts/delta-lake.md) table in a single operation. It is one of several approaches for migrating an existing Parquet data lake to the Delta Lake format, which is the underlying storage format of the Databricks lakehouse. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Syntax

```sql
CONVERT TO DELTA parquet.`<path-to-parquet-directory>`;
```

The command takes a path to a directory containing Parquet files (using the `parquet.` format prefix) and converts it in place to a Delta table. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Usage notes

- Once a table has been converted to Delta Lake, you should stop reading and writing from the table using Parquet logic. Data written to the target directory after conversion has started might not be reflected in the resultant Delta table. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]
- The command does **not** duplicate data; it modifies the existing files in place by adding Delta transaction logs and statistics. This contrasts with a deep clone, which copies data to a new location. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md] *(Note: the source does not explicitly state "does not duplicate data" for CONVERT TO DELTA, but the comparison table in the source shows "Duplicates data" as "No" for CONVERT TO DELTA, while for other methods it says "Yes".)*
- The conversion is **not incremental**; it runs as a single batch operation. If new Parquet files are added to the directory after the conversion, they will not be automatically included in the Delta table. For incremental migration, consider using [CLONE Parquet](/concepts/clone-parquet.md) or Auto Loader. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Considerations before converting

Before converting, evaluate your existing partitioning strategy. Over-partitioned tables can cause slow workloads on Delta Lake. It is also important to consider whether the data is still growing and how frequently it is queried. Different Parquet tables in the data lake may benefit from different migration approaches (e.g., `CLONE`, Auto Loader, or custom batch logic). ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## When not to convert

Databricks recommends using Delta Lake for all tables that receive regular updates or queries from Databricks. However, you might choose to keep data in Parquet format if:

- An upstream system writes data to Parquet and does not support native writing to Delta Lake.
- A downstream system that reads Parquet data cannot read Delta Lake.

In such cases, you can replicate the tables to Delta Lake to leverage performance benefits while the original Parquet data remains untouched. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Alternatives to CONVERT TO DELTA

| Approach | Incremental | Duplicates data | Maintains partitioning | Backfill support |
|----------|-------------|-----------------|------------------------|------------------|
| `CONVERT TO DELTA` | No | No | Yes (can be maintained) | N/A |
| `CLONE` Parquet (shallow or deep) | Yes (deep) | Deep: yes; Shallow: no | Yes | Yes (deep) |
| Auto Loader | Yes | Yes | Configurable | Yes (backfill interval) |
| Custom Spark batch logic | Configurable | Yes | Configurable | Configurable |

^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Related concepts

- [Delta Lake](/concepts/delta-lake.md) – The underlying format of the lakehouse.
- [CLONE Parquet](/concepts/clone-parquet.md) – Incremental migration using shallow or deep clones.
- Auto Loader – Incremental ingestion that can be used for migration.
- Parquet – The source file format.
- Lakehouse – The Databricks architecture built on Delta Lake.
- Partitioning best practices on Databricks – Guidance on avoiding over-partitioned tables.

## Sources

- migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md

# Citations

1. [migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md](/references/migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws-01ccec95.md)
