---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: db3adeeafc64f53c331f67c1f163c1b955d146f486e63b90ce50532819b515c2
  pageDirectory: concepts
  sources:
    - convert-to-delta-lake-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hive-metastore-to-unity-catalog-table-migration
    - HMTUCTM
    - Upgrade a schema or tables from the Hive metastore to Unity Catalog external tables using the upgrade wizard
  citations:
    - file: convert-to-delta-lake-databricks-on-aws.md
title: Hive Metastore to Unity Catalog Table Migration
description: Strategies for converting legacy Hive metastore managed and external Parquet tables to Unity Catalog Delta Lake tables using CTAS or upgrade wizard
tags:
  - unity-catalog
  - hive-metastore
  - data-migration
timestamp: "2026-06-19T09:25:02.327Z"
---

Here is the wiki page for "Hive [Metastore](/concepts/metastore.md) to Unity Catalog Table Migration," written solely from the provided source material.

---

## Hive [Metastore](/concepts/metastore.md) to Unity Catalog Table Migration

**Hive [Metastore](/concepts/metastore.md) to Unity Catalog Table Migration** refers to the process of moving tables registered in the legacy Hive [Metastore](/concepts/metastore.md) to [Unity Catalog](/concepts/unity-catalog.md). Unity Catalog is Databricks’ centralized governance solution, and migrating tables is a key step in adopting its capabilities. The appropriate migration method depends on whether the source table is a managed or external table and the target table type in Unity Catalog.

### Converting Managed Parquet Tables

To migrate a legacy Hive [Metastore](/concepts/metastore.md) **managed** Parquet table directly to a Unity Catalog **managed** [Delta Lake Table](/concepts/delta-lake-table.md), use a `CTAS` (CREATE TABLE AS SELECT) statement. ^[convert-to-delta-lake-databricks-on-aws.md]

### Converting External Parquet and Iceberg Tables

For **external** tables, the migration process involves two main steps: first register the table in Unity Catalog, then convert its underlying file format to Delta Lake. ^[convert-to-delta-lake-databricks-on-aws.md]

#### Step 1: Register the Table in Unity Catalog

You can upgrade an external Parquet table to a Unity Catalog external table using the Unity Catalog upgrade wizard. This registers the table with Unity Catalog while keeping its existing Parquet data files in place. ^[convert-to-delta-lake-databricks-on-aws.md]

#### Step 2: Convert to Delta Lake

Once registered in Unity Catalog, you can convert the external Parquet table to an external [Delta Lake Table](/concepts/delta-lake-table.md) using the `CONVERT TO DELTA` SQL command. If the Parquet table is partitioned, you must provide the partitioning information in the command. ^[convert-to-delta-lake-databricks-on-aws.md]

```sql
CONVERT TO DELTA catalog_name.database_name.table_name;
CONVERT TO DELTA catalog_name.database_name.table_name PARTITIONED BY (date_updated DATE);
```

Unity Catalog supports the `CONVERT TO DELTA` SQL command for both Parquet and Apache Iceberg tables stored in external locations that Unity Catalog manages. ^[convert-to-delta-lake-databricks-on-aws.md]

### Converting a Directory of Parquet or Iceberg Files

You can also convert a directory of Parquet or Iceberg data files directly to a [Delta Lake Table](/concepts/delta-lake-table.md), as long as you have write access to the storage location. This creates a [Delta Lake Table](/concepts/delta-lake-table.md) without first registering it in the Hive [Metastore](/concepts/metastore.md). To subsequently load the converted table as an external table in Unity Catalog, you need the `CREATE EXTERNAL TABLE` permission on the external location. ^[convert-to-delta-lake-databricks-on-aws.md]

```sql
CONVERT TO DELTA parquet.`s3://my-bucket/parquet-data`;
CONVERT TO DELTA iceberg.`s3://my-bucket/iceberg-data`;
```

#### Limitations for Iceberg Tables

- Converting Iceberg [Metastore](/concepts/metastore.md) tables is not supported. ^[convert-to-delta-lake-databricks-on-aws.md]
- Converting Iceberg tables that have experienced [partition evolution](https://iceberg.apache.org/docs/latest/evolution/#partition-evolution) is not supported. ^[convert-to-delta-lake-databricks-on-aws.md]
- For Iceberg tables with partitions defined on truncated columns, Databricks Runtime 13.3 LTS and above supports truncated columns of types `string`, `long`, or `int`. Truncated columns of type `decimal` are not supported. ^[convert-to-delta-lake-databricks-on-aws.md]

### Incremental Conversion

For incremental (ongoing) conversion of Parquet or Iceberg tables to Delta Lake, rather than a one-time conversion, see the documentation on incrementally cloning Parquet and Apache Iceberg tables to Delta Lake. ^[convert-to-delta-lake-databricks-on-aws.md]

### Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The target governance system for migration.
- [Delta Lake](/concepts/delta-lake.md) – The target table format after conversion.
- External Tables – Tables that store data outside of Databricks-managed storage.
- [Managed Tables](/concepts/managed-tables-in-databricks.md) – Tables where Databricks manages the data lifecycle.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – An alternative open table format that can be converted to Delta Lake.
- Parquet – A common columnar storage format for data lakes.

## Sources

- convert-to-delta-lake-databricks-on-aws.md

# Citations

1. [convert-to-delta-lake-databricks-on-aws.md](/references/convert-to-delta-lake-databricks-on-aws-85c3b3fb.md)
