---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8f2ab2617d10a15f00998aa0c62be220140f622f36fad89606577423e65947c6
  pageDirectory: concepts
  sources:
    - create-table-clone-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - parquet-and-foreign-iceberg-to-delta-clone
    - Foreign Iceberg to Delta Clone and Parquet
    - PAFITDC
  citations:
    - file: create-table-clone-databricks-on-aws.md
title: Parquet and Foreign Iceberg to Delta Clone
description: The ability to incrementally clone Parquet and foreign Iceberg tables to Delta Lake format on Databricks, supporting both deep and shallow cloning.
tags:
  - databricks
  - delta-lake
  - migration
timestamp: "2026-06-19T09:38:41.796Z"
---

# Parquet and Foreign Iceberg to Delta Clone

**Parquet and Foreign Iceberg to Delta Clone** is a Databricks SQL operation that creates a copy — either deep or shallow — of a source Apache Parquet or foreign [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) table into a [Delta Lake](/concepts/delta-lake.md) table at a specific version. The command supports both `SHALLOW` and `DEEP` clones for these source formats, enabling incremental data migration and reproducible snapshots without disrupting the original source.^[create-table-clone-databricks-on-aws.md]

## Supported Clone Types

- **Deep Clone** (default): Copies both the table metadata and all data files, producing a fully independent Delta table. Subsequent changes to the source do not affect the clone.^[create-table-clone-databricks-on-aws.md]
- **Shallow Clone**: Copies only the table metadata; the target Delta table references the source’s data files. Shallow clones are lightweight and fast but remain dependent on the source data.^[create-table-clone-databricks-on-aws.md]

> **Note:** Managed Iceberg tables (native to Unity Catalog) support **only** deep cloning and cannot change the table format during cloning. This page covers the foreign Iceberg tables (non-managed) that do allow shallow cloning.^[create-table-clone-databricks-on-aws.md]

## Syntax

The syntax is identical to the general `CREATE TABLE ... CLONE` statement. The source table can be a Parquet or foreign Iceberg table:

```sql
CREATE TABLE [IF NOT EXISTS] target_table
  [SHALLOW | DEEP] CLONE source_table
  [TBLPROPERTIES clause]
  [LOCATION path];

-- To replace an existing table:
CREATE OR REPLACE TABLE target_table
  [SHALLOW | DEEP] CLONE source_table
  [TBLPROPERTIES clause]
  [LOCATION path];
```

^[create-table-clone-databricks-on-aws.md]

### Parameters

- `IF NOT EXISTS` – Skips the operation if the target table already exists.^[create-table-clone-databricks-on-aws.md]
- `[CREATE OR] REPLACE` – Replaces an existing table or creates a new one if it does not exist.^[create-table-clone-databricks-on-aws.md]
- `table_name` – Target Delta table name; must not include temporal or options specifications.^[create-table-clone-databricks-on-aws.md]
- `SHALLOW CLONE` / `DEEP CLONE` – Controls whether the data is copied or referenced.^[create-table-clone-databricks-on-aws.md]
- `source_table_name` – The Parquet or foreign Iceberg table to clone. May include temporal specifications (e.g., `TIMESTAMP AS OF`).^[create-table-clone-databricks-on-aws.md]
- `TBLPROPERTIES` – Optional user-defined properties applied to the cloned table.^[create-table-clone-databricks-on-aws.md]
- `LOCATION path` – Optional external table path. Must be a STRING literal.^[create-table-clone-databricks-on-aws.md]

## Example

The following example performs a deep clone of a foreign Iceberg table into a Delta table, and a shallow clone of a Parquet table into another Delta table:

```sql
-- Deep clone from a foreign Iceberg table
CREATE TABLE catalog.schema.delta_iceberg_clone
DEEP CLONE catalog.schema.foreign_iceberg_table;

-- Shallow clone from a Parquet table
CREATE TABLE catalog.schema.parquet_shallow
SHALLOW CLONE parquet.`/path/to/parquet/dir`;
```

^[create-table-clone-databricks-on-aws.md]

## Use Cases

- **Incremental migration** of Parquet or foreign Iceberg data to Delta Lake for better performance and features (e.g., [Delta Lake](/concepts/delta-lake.md) ACID transactions, time travel).^[create-table-clone-databricks-on-aws.md]
- **Creating reproducible snapshots** for machine learning experiments or data archival without duplicating storage for shallow clones.^[create-table-clone-databricks-on-aws.md]
- **Converting table formats** by deep cloning a Parquet or foreign Iceberg source to a Delta table with richer metadata.^[create-table-clone-databricks-on-aws.md]

## Limitations and Considerations

- Streaming tables and [Materialized views](/concepts/materialized-views-in-databricks.md) cannot be used as source or target for `CLONE`.^[create-table-clone-databricks-on-aws.md]
- For shallow clones, the target table remains dependent on the source files; deleting or modifying the source can invalidate the clone.^[create-table-clone-databricks-on-aws.md]
- Managed Iceberg tables (created natively in Unity Catalog) do not support shallow cloning or format conversion during clone – only deep clone is allowed. This page specifically addresses foreign Iceberg tables (registered externally).^[create-table-clone-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The target table format.
- [Deep Clone](/concepts/deep-clone.md) – Copying data and metadata.
- [Shallow Clone](/concepts/shallow-clone.md) – Reference-only clone.
- Clone a table on Databricks – General cloning guidance.
- [Incrementally clone Parquet and Apache Iceberg tables to Delta Lake](/concepts/incremental-clone-of-parquet-and-iceberg-to-delta-lake.md) – Step-by-step migration guide.

## Sources

- create-table-clone-databricks-on-aws.md

# Citations

1. [create-table-clone-databricks-on-aws.md](/references/create-table-clone-databricks-on-aws-49def2a6.md)
