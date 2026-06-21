---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3864200f40199822557d7b78a9b32206f31713e22014d6ff1543550b2da0622e
  pageDirectory: concepts
  sources:
    - create-table-clone-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-clone-sql-syntax
    - DCSS
  citations:
    - file: create-table-clone-databricks-on-aws.md
title: Databricks CLONE SQL Syntax
description: The SQL language syntax for the CREATE TABLE CLONE and REPLACE TABLE CLONE statements, including parameters such as IF NOT EXISTS, SHALLOW/DEEP, TBLPROPERTIES, and LOCATION.
tags:
  - databricks
  - sql
  - syntax
timestamp: "2026-06-18T11:24:56.272Z"
---

# Databricks CLONE SQL Syntax

The `CREATE TABLE CLONE` and `REPLACE TABLE CLONE` SQL commands create a copy of a source Delta, managed Apache Iceberg, or Apache Parquet table at a specific version. Cloning can be either **deep** (copies data) or **shallow** (references source data without copying). ^[create-table-clone-databricks-on-aws.md]

## Syntax

```sql
CREATE TABLE [IF NOT EXISTS] table_name
  [SHALLOW | DEEP] CLONE source_table_name
  [TBLPROPERTIES clause]
  [LOCATION path]

[CREATE OR] REPLACE TABLE table_name
  [SHALLOW | DEEP] CLONE source_table_name
  [TBLPROPERTIES clause]
  [LOCATION path]
```

^[create-table-clone-databricks-on-aws.md]

## Parameters

### IF NOT EXISTS

If specified, the statement is ignored when `table_name` already exists. ^[create-table-clone-databricks-on-aws.md]

### [CREATE OR] REPLACE

If `CREATE OR` is specified, the table is replaced if it exists and newly created if it does not. Without `CREATE OR`, the `table_name` must already exist. ^[create-table-clone-databricks-on-aws.md]

### table_name

The name of the table to be created. The name must not include a temporal specification or options specification. If the name is not qualified, the table is created in the current schema. `table_name` must not already exist unless `REPLACE` or `IF NOT EXISTS` has been specified. ^[create-table-clone-databricks-on-aws.md]

### SHALLOW CLONE or DEEP CLONE

- **SHALLOW CLONE**: Makes a copy of the source table's definition but refers to the source table's data files. No data is copied.
- **DEEP CLONE** (default): Makes a complete, independent copy of the source table, including all data.

Managed Iceberg tables only support deep cloning, not shallow cloning. ^[create-table-clone-databricks-on-aws.md]

### source_table_name

The name of the table to be cloned. The name may include a temporal specification or options specification. ^[create-table-clone-databricks-on-aws.md]

### TBLPROPERTIES

Optionally sets one or more user-defined properties on the cloned table. ^[create-table-clone-databricks-on-aws.md]

### LOCATION path

Optionally creates an external table with the provided location as the path where the data is stored. If `table_name` itself is a path instead of a table identifier, the operation will fail. `path` must be a STRING literal. ^[create-table-clone-databricks-on-aws.md]

## Supported Table Formats

| Source Format | Deep Clone | Shallow Clone |
|---|---|---|
| Delta | Yes | Yes |
| Parquet | Yes | Yes |
| Foreign Iceberg | Yes | Yes |
| Managed Iceberg | Yes | No |

^[create-table-clone-databricks-on-aws.md]

## Examples

### Deep Clone a [Delta Lake Table](/concepts/delta-lake-table.md)

```sql
CREATE TABLE target_catalog.target_schema.target_table
DEEP CLONE source_catalog.source_schema.source_table;
```

^[create-table-clone-databricks-on-aws.md]

### Shallow Clone a [Delta Lake Table](/concepts/delta-lake-table.md)

```sql
CREATE TABLE target_catalog.target_schema.target_table
SHALLOW CLONE source_catalog.source_schema.source_table;
```

^[create-table-clone-databricks-on-aws.md]

### Deep Clone a Managed Iceberg Table

```sql
CREATE TABLE target_catalog.target_schema.target_table
DEEP CLONE source_catalog.source_schema.source_table;
```

Managed Iceberg tables only support deep cloning. ^[create-table-clone-databricks-on-aws.md]

## Important Considerations

### Shallow vs. Deep Clone

There are important differences between shallow and deep clones that determine how best to use them. Shallow clones are lightweight and fast because they only copy metadata, but they remain dependent on the source table's data files. Deep clones create fully independent copies at the cost of additional storage and time. ^[create-table-clone-databricks-on-aws.md]

### Unity Catalog Support

In Databricks SQL and Databricks Runtime 13.3 LTS and above, you can use shallow clone with Unity Catalog managed tables. In Databricks Runtime 12.2 LTS and below, there is no support for shallow clones in Unity Catalog. ^[create-table-clone-databricks-on-aws.md]

### Unsupported Source Types

Streaming tables and materialized views are not supported as source or target tables for `CLONE`. ^[create-table-clone-databricks-on-aws.md]

### Format Restrictions

Managed Iceberg tables support only deep cloning, and you cannot change the table format during cloning. ^[create-table-clone-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format for cloned tables
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer that supports shallow clones for managed tables
- Table Cloning Best Practices — Guidance on when to use deep vs. shallow clones
- [Incremental Cloning](/concepts/incremental-cloning-to-delta-lake.md) — Cloning Parquet and Iceberg tables incrementally to Delta Lake
- Managed Iceberg Tables — Iceberg tables managed by Unity Catalog with clone limitations

## Sources

- create-table-clone-databricks-on-aws.md

# Citations

1. [create-table-clone-databricks-on-aws.md](/references/create-table-clone-databricks-on-aws-49def2a6.md)
