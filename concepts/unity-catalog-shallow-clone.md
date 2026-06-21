---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2ef70ebe1378b1514745650e888afd888afdc40759e83e20809a3f0df3c7eb8a
  pageDirectory: concepts
  sources:
    - create-table-clone-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-shallow-clone
    - UCSC
    - unity-catalog-shallow-clone-support
    - UCSCS
  citations:
    - file: create-table-clone-databricks-on-aws.md
title: Unity Catalog Shallow Clone
description: Shallow clone support for Unity Catalog managed tables in Databricks SQL and Databricks Runtime 13.3 LTS and above, with no support in Databricks Runtime 12.2 LTS and below.
tags:
  - databricks
  - unity-catalog
  - cloning
timestamp: "2026-06-18T11:25:10.017Z"
---

# Unity Catalog Shallow Clone

**Unity Catalog Shallow Clone** creates a new Delta table that references the source table’s data files without copying the data. The clone stores only the table metadata (schema, partitioning, table properties) in the target catalog, while all read operations retrieve data from the original source files. This makes shallow clones both fast and storage-efficient. ^[create-table-clone-databricks-on-aws.md]

Shallow cloning is supported for Delta, Parquet, and foreign Iceberg source tables. In Databricks SQL and Databricks Runtime 13.3 LTS and above, shallow clones can target Unity Catalog managed tables. Databricks Runtime 12.2 LTS and below do not support shallow clones in Unity Catalog. ^[create-table-clone-databricks-on-aws.md]

**Important:** Shallow clones behave differently from [Deep Clone](/concepts/deep-clone.md) in several ways — see the general [clone documentation](https://docs.databricks.com/aws/en/tables/operations/clone) for a full comparison. Streaming tables and materialized views cannot be used as source or target for any clone operation. ^[create-table-clone-databricks-on-aws.md]

## Syntax

Two forms are available — one that creates a new table and one that replaces an existing table:

```sql
CREATE TABLE [IF NOT EXISTS] table_name
  SHALLOW CLONE source_table_name
  [TBLPROPERTIES clause]
  [LOCATION path]

[CREATE OR] REPLACE TABLE table_name
  SHALLOW CLONE source_table_name
  [TBLPROPERTIES clause]
  [LOCATION path]
```

^[create-table-clone-databricks-on-aws.md]

## Parameters

- **`IF NOT EXISTS`** – If the target table already exists, the statement is ignored.
- **`[CREATE OR] REPLACE`** – If `CREATE OR` is specified, the table is created if it does not exist or replaced if it does. Without `CREATE OR`, the target table must already exist.
- **`table_name`** – The name of the target table. Must not include a temporal or options specification. If unqualified, the table is created in the current schema.
- **`SHALLOW CLONE`** – Copies the source table’s definition (metadata) but refers to the source table’s data files. No data is physically copied.
- **`source_table_name`** – The name of the table to clone. May include a temporal specification or options specification (e.g., a specific version or timestamp).
- **`TBLPROPERTIES`** – Optional user-defined properties for the cloned table.
- **`LOCATION path`** – Optionally creates an external table at the given path. The path must be a STRING literal.

^[create-table-clone-databricks-on-aws.md]

## Example

```sql
-- Shallow clone: copies metadata only, references source data files
CREATE TABLE target_catalog.target_schema.target_table
SHALLOW CLONE source_catalog.source_schema.source_table;
```

^[create-table-clone-databricks-on-aws.md]

## Usage Notes

- Shallow clones are commonly used for creating test or development copies of production tables without duplicating storage costs, or for creating a point-in-time snapshot that can be independently modified (writes to the clone create new data files without affecting the source).
- Because the clone initially shares data files with the source, any write operation on the clone creates new files (copy-on-write semantics). The source table remains untouched.
- For Unity Catalog managed tables, the clone’s data files are still stored in the source table’s cloud storage location until the clone writes new data.

## Related Concepts

- [Deep Clone](/concepts/deep-clone.md) – Creates a complete, independent copy of the source table, including all data files.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that supports shallow clones for managed tables.
- [Delta Lake](/concepts/delta-lake.md) – The underlying storage format for cloned tables.
- [Managed Tables](/concepts/managed-tables-in-databricks.md) – Unity Catalog tables that can be shallow cloned.
- Clone a Table on Databricks – General documentation covering both shallow and deep clones.

## Sources

- create-table-clone-databricks-on-aws.md

# Citations

1. [create-table-clone-databricks-on-aws.md](/references/create-table-clone-databricks-on-aws-49def2a6.md)
