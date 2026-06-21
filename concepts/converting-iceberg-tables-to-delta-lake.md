---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5b01e6366b4c8dc9f394ac8f63c313dafa56b845b53c00869d160cd44439500c
  pageDirectory: concepts
  sources:
    - convert-to-delta-lake-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - converting-iceberg-tables-to-delta-lake
    - CITTDL
  citations:
    - file: convert-to-delta-lake-databricks-on-aws.md
title: Converting Iceberg tables to Delta Lake
description: One-time conversion of Apache Iceberg tables to Delta Lake with specific version and feature limitations
tags:
  - iceberg
  - delta-lake
  - data-migration
timestamp: "2026-06-19T14:26:28.076Z"
---

---

title: Converting Iceberg Tables to Delta Lake
summary: A one-time conversion of Apache Iceberg tables to Delta Lake using the `CONVERT TO DELTA` SQL command, supported on Databricks.
sources:
  - convert-to-delta-lake-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:00:00.000Z"
updatedAt: "2026-06-18T12:00:00.000Z"
tags:
  - databricks
  - delta-lake
  - iceberg
  - data-migration
  - sql
aliases:
  - converting-iceberg-tables-to-delta-lake
  - iceberg-to-delta
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Converting Iceberg Tables to Delta Lake

**Converting Iceberg tables to Delta Lake** refers to the one-time migration of an existing [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) table to the [Delta Lake](/concepts/delta-lake.md) format using the `CONVERT TO DELTA` SQL command on Databricks. This operation reads the Iceberg metadata and data files (Parquet) and produces a Delta Lake transaction log, enabling all Delta Lake features such as [ACID transactions](/concepts/delta-acid-transactions.md), [time travel](/concepts/delta-lake-time-travel.md), and [Unity Catalog](/concepts/unity-catalog.md) integration. ^[convert-to-delta-lake-databricks-on-aws.md]

## Overview

The `CONVERT TO DELTA` command performs a batch conversion. For incremental, ongoing synchronization of Iceberg tables to Delta Lake, Databricks recommends using the [Incremental clone](/concepts/incremental-cloning-to-delta-lake.md) mechanism instead. ^[convert-to-delta-lake-databricks-on-aws.md]

### Supported Scenarios

- Iceberg tables stored in external locations managed by [Unity Catalog](/concepts/unity-catalog.md). ^[convert-to-delta-lake-databricks-on-aws.md]
- Directories of Iceberg data files (e.g., `iceberg.`<code>s3://bucket/path</code>). ^[convert-to-delta-lake-databricks-on-aws.md]

### Unsupported Scenarios

- Iceberg [Metastore](/concepts/metastore.md) tables (tables registered in the Hive [Metastore](/concepts/metastore.md) via Iceberg’s catalog integration) are **not** supported for conversion. ^[convert-to-delta-lake-databricks-on-aws.md]
- Iceberg tables that have experienced [partition evolution](/concepts/partition-evolution-in-iceberg.md) cannot be converted. ^[convert-to-delta-lake-databricks-on-aws.md]

### Limitations with Truncated Columns

If the Iceberg table defines partitions on **truncated columns**, the following restrictions apply: ^[convert-to-delta-lake-databricks-on-aws.md]

| Databricks Runtime Version | Supported Truncated Column Types |
|----------------------------|----------------------------------|
| ≤ 12.2 LTS                 | `string` only                    |
| 13.3 LTS and above         | `string`, `long`, or `int`       |
| All versions               | `decimal` truncated columns are **not** supported |

## Prerequisites

- Databricks Runtime 10.4 LTS or above. ^[convert-to-delta-lake-databricks-on-aws.md]
- Write access on the storage location where the Iceberg data resides. ^[convert-to-delta-lake-databricks-on-aws.md]
- For Unity Catalog external tables, the user must have the `CREATE EXTERNAL TABLE` permission on the [External location](/concepts/external-location.md). ^[convert-to-delta-lake-databricks-on-aws.md]

## Syntax

### Convert a directory of Iceberg files

```sql
CONVERT TO DELTA iceberg.`s3://my-bucket/iceberg-data`;
```

### Convert a Unity Catalog external Iceberg table

```sql
CONVERT TO DELTA catalog_name.database_name.table_name;
```

### Provide partitioning information

When converting a Unity Catalog external table that is partitioned, you must supply the partition columns explicitly: ^[convert-to-delta-lake-databricks-on-aws.md]

```sql
CONVERT TO DELTA catalog_name.database_name.table_name PARTITIONED BY (date_updated DATE);
```

> **Note:** For Hive [Metastore](/concepts/metastore.md) tables, Databricks Runtime 11.3 LTS and above automatically infers partitioning during conversion. This inference does **not** apply to Unity Catalog external tables. ^[convert-to-delta-lake-databricks-on-aws.md]

## Best Practices

1. **Use incremental clone for live data.** If the Iceberg table continues to receive new data, prefer the [Incremental clone](/concepts/incremental-cloning-to-delta-lake.md) feature to keep the Delta Lake copy up-to-date. ^[convert-to-delta-lake-databricks-on-aws.md]
2. **Verify partition evolution status.** Check whether the Iceberg table has undergone partition evolution before attempting conversion, as such tables are unsupported. ^[convert-to-delta-lake-databricks-on-aws.md]
3. **Test on a copy before production.** Run the conversion on a staging directory or a snapshot of the Iceberg data to validate compatibility. ^[convert-to-delta-lake-databricks-on-aws.md] (inferred, but reasonable based on general practice)
4. **Register the converted table in Unity Catalog.** After conversion, create an external table in Unity Catalog pointing to the Delta Lake location to enable governance and discovery. ^[convert-to-delta-lake-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The target format.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – The source format.
- [Unity Catalog](/concepts/unity-catalog.md) – Governs external locations and supports converted tables.
- [External location](/concepts/external-location.md) – Cloud storage path managed by Unity Catalog.
- [CONVERT TO DELTA SQL Command](/concepts/convert-to-delta-sql-command.md) – Reference documentation.
- [Incremental clone of Parquet and Iceberg tables](/concepts/incremental-clone-of-parquet-and-iceberg-to-delta-lake.md) – Alternative for ongoing synchronization.
- Partition Evolution – A feature of Iceberg that is incompatible with conversion.

## Sources

- convert-to-delta-lake-databricks-on-aws.md

# Citations

1. [convert-to-delta-lake-databricks-on-aws.md](/references/convert-to-delta-lake-databricks-on-aws-85c3b3fb.md)
