---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0a84693cab8a55b8ba33b165113b7486bbd0f5eb1cedab3b8d95c054bb3869e1
  pageDirectory: concepts
  sources:
    - convert-to-delta-lake-databricks-on-aws.md
  confidence: 0.8
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - hive-metastore-to-unity-catalog-migration
    - HMTUCM
    - Hive to Unity Catalog Migration
    - upgrade tables managed by the Hive metastore to Unity Catalog
  citations:
    - file: convert-to-delta-lake-databricks-on-aws.md
title: Hive Metastore to Unity Catalog Migration
description: Strategies for upgrading legacy Hive metastore managed and external Parquet tables to Unity Catalog Delta Lake tables using CONVERT TO DELTA or CTAS.
tags:
  - hive
  - unity-catalog
  - migration
  - delta-lake
timestamp: "2026-06-18T14:45:05.897Z"
---

# Hive [Metastore](/concepts/metastore.md) to Unity Catalog Migration

**Hive [Metastore](/concepts/metastore.md) to Unity Catalog Migration** refers to the process of moving existing tables, schemas, and associated metadata from a legacy Hive [Metastore](/concepts/metastore.md) into [Unity Catalog](/concepts/unity-catalog.md), Databricks’ unified governance solution. The migration typically involves converting table formats and registering tables as managed or external objects in Unity Catalog while preserving data and access control.

## Overview

Databricks provides several mechanisms to migrate tables from the Hive [Metastore](/concepts/metastore.md) to Unity Catalog. The choice of method depends on whether the source table is managed or external, the current file format (Parquet, Iceberg, Delta Lake), and whether the data resides in a Unity Catalog–managed storage location. Unity Catalog supports the `CONVERT TO DELTA` SQL command for Parquet and Iceberg tables stored in external locations that are managed by Unity Catalog.^[convert-to-delta-lake-databricks-on-aws.md]

## Migration Methods

### Convert External Parquet or Iceberg Tables to Delta Lake

If you have an external Parquet or Iceberg table already registered with Unity Catalog, you can convert it to an external [Delta Lake](/concepts/delta-lake.md) table using `CONVERT TO DELTA`. This step is optional but recommended to unlock Delta Lake features such as ACID transactions, time travel, and schema enforcement. Partitioning information must be provided if the source table is partitioned.^[convert-to-delta-lake-databricks-on-aws.md]

```sql
CONVERT TO DELTA catalog_name.database_name.table_name;
CONVERT TO DELTA catalog_name.database_name.table_name PARTITIONED BY (date_updated DATE);
```

### Upgrade a Hive [Metastore](/concepts/metastore.md) Managed Table to Unity Catalog Using CTAS

For a legacy Hive [Metastore](/concepts/metastore.md) *managed* Parquet table, use a `CREATE TABLE AS SELECT` (CTAS) statement to create a new managed table directly in Unity Catalog. The data is copied into the Unity Catalog managed storage location, and the original Hive table is left in place.^[convert-to-delta-lake-databricks-on-aws.md]

```sql
CREATE TABLE catalog_name.database_name.new_table
USING DELTA
AS SELECT * FROM hive_metastore.database_name.source_table;
```

This approach converts both the table format (to Delta Lake) and the governance model (to Unity Catalog).

### Upgrade External Tables Using the Upgrade Wizard

To upgrade an external Parquet table (where data lives in cloud storage that Unity Catalog can manage) from the Hive [Metastore](/concepts/metastore.md) to Unity Catalog as an external table, use the [upgrade wizard](https://docs.databricks.com/aws/en/data-governance/unity-catalog/migrate#wizard-bulk). This bulk migration tool registers the table in Unity Catalog without moving the underlying data. After the external table is registered, you can optionally convert it to Delta Lake with `CONVERT TO DELTA`.^[convert-to-delta-lake-databricks-on-aws.md]

The upgrade wizard is recommended for large-scale migrations of schemas and tables from the Hive [Metastore](/concepts/metastore.md) to Unity Catalog external tables.^[convert-to-delta-lake-databricks-on-aws.md]

## Important Limitations

- Converting Iceberg tables is supported starting in Databricks Runtime 10.4 LTS and above.^[convert-to-delta-lake-databricks-on-aws.md]
- Converting Iceberg *metastore tables* (tables defined in an Iceberg catalog) is **not** supported.^[convert-to-delta-lake-databricks-on-aws.md]
- Iceberg tables that have experienced [partition evolution](https://iceberg.apache.org/docs/latest/evolution/#partition-evolution) are not supported for conversion.^[convert-to-delta-lake-databricks-on-aws.md]
- Converting Iceberg tables with partitions defined on truncated columns has runtime-dependent limitations.^[convert-to-delta-lake-databricks-on-aws.md]
- The `CONVERT TO DELTA` command can only be used to create Unity Catalog *external* tables; it cannot convert a legacy managed Parquet table directly to a Unity Catalog managed table. Use the CTAS approach for that case.^[convert-to-delta-lake-databricks-on-aws.md]
- For Unity Catalog external tables, partitioning information must be explicitly provided during conversion, whereas for Hive [Metastore](/concepts/metastore.md) tables in Databricks Runtime 11.3 LTS and above, partitioning is automatically inferred.^[convert-to-delta-lake-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that manages data assets after migration.
- [Delta Lake](/concepts/delta-lake.md) – The open storage format that tables are often converted to during migration.
- External Tables – Tables whose data resides in external cloud storage, managed by Unity Catalog.
- [Hive Metastore](/concepts/built-in-hive-metastore.md) – The legacy [Metastore](/concepts/metastore.md) that stores table metadata before migration.
- [CONVERT TO DELTA](/concepts/convert-to-delta.md) – The SQL command used for one-time format conversion.
- [CTAS (CREATE TABLE AS SELECT)](/concepts/create-table-as-select-ctas-for-migration.md) – A method for migrating managed tables.

## Sources

- convert-to-delta-lake-databricks-on-aws.md

# Citations

1. [convert-to-delta-lake-databricks-on-aws.md](/references/convert-to-delta-lake-databricks-on-aws-85c3b3fb.md)
