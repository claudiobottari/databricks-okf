---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 968d6ae3c36a4a6349a3b796b7801d0c982f7d511f847369f540138137749632
  pageDirectory: concepts
  sources:
    - convert-to-delta-lake-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - partition-inference-in-delta-conversion
    - PIIDC
  citations:
    - file: convert-to-delta-lake-databricks-on-aws.md
title: Partition Inference in Delta Conversion
description: Automatic partitioning inference for Hive metastore tables during CONVERT TO DELTA, and the requirement to provide partitioning info for Unity Catalog external tables.
tags:
  - partitioning
  - delta-lake
  - data-optimization
timestamp: "2026-06-18T14:44:57.376Z"
---

# Partition Inference in Delta Conversion

**Partition Inference in Delta Conversion** refers to the behavior of the `CONVERT TO DELTA` SQL command when converting Parquet or Iceberg tables to Delta Lake tables, specifically regarding how partitioning information is determined for the resulting table.

## Overview

When converting existing data files to Delta Lake format using `CONVERT TO DELTA`, the command handles partitioning information differently depending on the source of the data and the Databricks Runtime version. The ability to infer partitions automatically varies between Hive [Metastore](/concepts/metastore.md) tables and Unity Catalog external tables. ^[convert-to-delta-lake-databricks-on-aws.md]

## Automatic Partition Inference (Hive [Metastore](/concepts/metastore.md))

For tables registered to the Hive [Metastore](/concepts/metastore.md), `CONVERT TO DELTA` automatically infers partitioning information in Databricks Runtime 11.3 LTS and above. This means you do not need to explicitly specify partition columns when converting Hive [Metastore](/concepts/metastore.md) Parquet tables to Delta Lake. ^[convert-to-delta-lake-databricks-on-aws.md]

## Manual Partition Specification (Unity Catalog External Tables)

For Unity Catalog external tables converted to Delta Lake, you must provide partitioning information explicitly if the Parquet table is partitioned. The `CONVERT TO DELTA` command does not automatically infer partition columns for Unity Catalog external tables. ^[convert-to-delta-lake-databricks-on-aws.md]

```sql
CONVERT TO DELTA catalog_name.database_name.table_name PARTITIONED BY (date_updated DATE);
```

## Iceberg Partition Evolution Limitation

When converting Iceberg tables, partition inference is further constrained by a specific limitation: converting Iceberg tables that have experienced [partition evolution](https://iceberg.apache.org/docs/latest/evolution/#partition-evolution) is not supported. Iceberg partition evolution allows changing a table's partition scheme over time without rewriting data, but this feature creates incompatible metadata for the conversion process. ^[convert-to-delta-lake-databricks-on-aws.md]

## Truncated Column Partition Limitations

For Iceberg tables with partitions defined on truncated columns, additional limitations apply based on the Databricks Runtime version:

- **Databricks Runtime 12.2 LTS and below**: The only truncated column type supported is `string`.
- **Databricks Runtime 13.3 LTS and above**: You can work with truncated columns of types `string`, `long`, or `int`.
- Databricks does not support working with truncated columns of type `decimal`. ^[convert-to-delta-lake-databricks-on-aws.md]

## Best Practices

- When converting tables registered to the Hive [Metastore](/concepts/metastore.md) in Databricks Runtime 11.3 LTS+, you can rely on automatic partition inference and omit the `PARTITIONED BY` clause. ^[convert-to-delta-lake-databricks-on-aws.md]
- When converting Unity Catalog external Parquet tables, explicitly provide partitioning information using the `PARTITIONED BY` clause to ensure correct table structure. ^[convert-to-delta-lake-databricks-on-aws.md]
- For external tables, ensure you have the `CREATE EXTERNAL TABLE` permission on the external location before attempting conversion. ^[convert-to-delta-lake-databricks-on-aws.md]
- Check whether your Iceberg source table has undergone partition evolution before attempting conversion, as such tables cannot be converted. ^[convert-to-delta-lake-databricks-on-aws.md]

## Related Concepts

- [CONVERT TO DELTA Command](/concepts/convert-to-delta-command.md) — The SQL command for one-time conversion to Delta Lake
- [Delta Lake](/concepts/delta-lake.md) — The underlying format that provides ACID transactions and unified batch/streaming
- [Unity Catalog External Tables](/concepts/unity-catalog-external-table-conversion.md) — Tables managed by Unity Catalog but stored in external cloud storage
- [Hive Metastore](/concepts/built-in-hive-metastore.md) — Legacy table catalog that supports automatic partition inference
- Iceberg Partition Evolution — A feature of Apache Iceberg that is incompatible with Delta conversion
- [Incremental Clone to Delta Lake](/concepts/incremental-cloning-to-delta-lake.md) — Alternative approach for ongoing conversion of Parquet or Iceberg tables

## Sources

- convert-to-delta-lake-databricks-on-aws.md

# Citations

1. [convert-to-delta-lake-databricks-on-aws.md](/references/convert-to-delta-lake-databricks-on-aws-85c3b3fb.md)
