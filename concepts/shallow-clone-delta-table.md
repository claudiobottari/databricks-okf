---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 42635644f2621c62cb2c98f1cfd555e00a33cea275725e223fb33c664cbf3b8a
  pageDirectory: concepts
  sources:
    - create-table-clone-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - shallow-clone-delta-table
    - SC(T
    - Shallow clone for Unity Catalog tables
  citations:
    - file: create-table-clone-databricks-on-aws.md
title: Shallow Clone (Delta Table)
description: A copy of a source table's definition that references the original data files without copying them, providing a lightweight metadata-only clone.
tags:
  - databricks
  - delta-lake
  - cloning
timestamp: "2026-06-19T14:38:48.841Z"
---

# Shallow Clone (Delta Table)

**Shallow Clone** is a `CREATE TABLE CLONE` operation that copies a source table’s metadata and table definition but does **not** copy the underlying data files. Instead, the cloned table references the source table’s existing data files, making it a lightweight, storage-efficient alternative to a deep clone.^[create-table-clone-databricks-on-aws.md]

## Syntax

Shallow clone can be used to create a new table or replace an existing table.

```sql
-- Create a new shallow clone
CREATE TABLE [IF NOT EXISTS] table_name
  SHALLOW CLONE source_table_name
  [TBLPROPERTIES clause]
  [LOCATION path]

-- Replace an existing table with a shallow clone
[CREATE OR] REPLACE TABLE table_name
  SHALLOW CLONE source_table_name
  [TBLPROPERTIES clause]
  [LOCATION path]
```

^[create-table-clone-databricks-on-aws.md]

### Parameters

- **`IF NOT EXISTS`** – If the target table already exists, the statement is ignored.
- **`[CREATE OR] REPLACE`** – Replaces the target table if it exists, or creates it if it does not.
- **`table_name`** – The name of the target table (must not include a temporal specification or options specification).
- **`source_table_name`** – The source table being cloned; may include a temporal specification or options specification.
- **`TBLPROPERTIES`** – Optional user-defined properties to set on the cloned table.
- **`LOCATION path`** – Optionally creates an external table with the given storage path. ^[create-table-clone-databricks-on-aws.md]

## Supported Source Table Formats

Shallow clone is supported for the following source table formats:

- **Delta Lake** – Full support.
- **Apache Parquet** – Supported as a source format.
- **Foreign Apache Iceberg** – Supported as a source format.

Managed Iceberg tables **do not** support shallow cloning; they only support deep clone.^[create-table-clone-databricks-on-aws.md]

## Unity Catalog Support

- **Databricks SQL and Databricks Runtime 13.3 LTS and above** – Shallow clone is supported for Unity Catalog managed tables.
- **Databricks Runtime 12.2 LTS and below** – Shallow clone is **not** supported in Unity Catalog.^[create-table-clone-databricks-on-aws.md]

For detailed guidance on using shallow clones with Unity Catalog, see the dedicated documentation on [shallow clone for Unity Catalog tables](https://docs.databricks.com/aws/en/tables/operations/clone-unity-catalog).^[create-table-clone-databricks-on-aws.md]

## Limitations

- **Streaming tables** and **materialized views** cannot be used as source or target tables for a `CLONE` operation (including shallow clone).^[create-table-clone-databricks-on-aws.md]
- Shallow clone is not supported for managed Iceberg tables.^[create-table-clone-databricks-on-aws.md]

## Related Concepts

- [Deep Clone (Delta Table)](/concepts/deep-clone-delta-table.md) – The alternative clone mode that creates a fully independent copy of the source data.
- [Delta Lake](/concepts/delta-lake.md) – The underlying storage format for Delta tables.
- [Unity Catalog](/concepts/unity-catalog.md) – The catalog service that supports shallow clones for managed tables in recent runtimes.
- Clone a Table on Databricks – Broader documentation covering both clone types, use cases, and best practices.

## Sources

- create-table-clone-databricks-on-aws.md

# Citations

1. [create-table-clone-databricks-on-aws.md](/references/create-table-clone-databricks-on-aws-49def2a6.md)
