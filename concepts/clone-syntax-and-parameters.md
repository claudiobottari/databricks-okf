---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f4fd369f0b752b5682d84a945d664b2c11728f5a4a92c5a37c1a6419453de008
  pageDirectory: concepts
  sources:
    - create-table-clone-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - clone-syntax-and-parameters
    - Parameters and CLONE Syntax
    - CSAP
  citations:
    - file: create-table-clone-databricks-on-aws.md
title: CLONE Syntax and Parameters
description: The SQL syntax for cloning tables, including CREATE TABLE, REPLACE TABLE, IF NOT EXISTS, SHALLOW/DEEP CLONE, TBLPROPERTIES, and LOCATION clauses.
tags:
  - sql
  - syntax
  - reference
timestamp: "2026-06-19T18:02:36.920Z"
---

# CLONE Syntax and Parameters

**CLONE** is a SQL statement in Databricks that creates a copy of a source Delta, managed Apache Iceberg, or Apache Parquet table at a specific version. Cloning can be performed as either a **deep clone** or a **shallow clone**, depending on whether the data itself is copied or only the table metadata. ^[create-table-clone-databricks-on-aws.md]

## Overview

Deep clones create a complete, independent copy of the source table, including all data files. Shallow clones copy only the table definition and metadata, referencing the source table's data files without copying them. ^[create-table-clone-databricks-on-aws.md]

- **Delta**, **Parquet**, and **Foreign Iceberg** tables support both deep and shallow cloning. ^[create-table-clone-databricks-on-aws.md]
- **Managed Iceberg** tables support only deep cloning. You cannot change the table format during cloning. ^[create-table-clone-databricks-on-aws.md]

Streaming tables and materialized views are not supported as source or target tables for `CLONE`. ^[create-table-clone-databricks-on-aws.md]

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

### `IF NOT EXISTS`

If specified, the statement is ignored when `table_name` already exists. ^[create-table-clone-databricks-on-aws.md]

### `[CREATE OR] REPLACE`

If `CREATE OR` is specified, the table is replaced if it exists and newly created if it does not. Without `CREATE OR`, the `table_name` must already exist. ^[create-table-clone-databricks-on-aws.md]

### `table_name`

The name of the table to be created or replaced. The name must not include a temporal specification or options specification. If the name is not qualified, the table is created in the current schema. `table_name` must not exist already unless `REPLACE` or `IF NOT EXISTS` has been specified. ^[create-table-clone-databricks-on-aws.md]

### `SHALLOW CLONE` or `DEEP CLONE`

- **`SHALLOW CLONE`**: Creates a copy of the source table's definition but refers to the source table's files. The data is not physically copied. ^[create-table-clone-databricks-on-aws.md]
- **`DEEP CLONE`** (default): Creates a complete, independent copy of the source table, including all data files. ^[create-table-clone-databricks-on-aws.md]

Managed Iceberg tables support only deep cloning. ^[create-table-clone-databricks-on-aws.md]

### `source_table_name`

The name of the table to be cloned. The name may include a temporal specification or options specification. ^[create-table-clone-databricks-on-aws.md]

### `TBLPROPERTIES clause`

Optionally sets one or more user-defined properties on the target table. ^[create-table-clone-databricks-on-aws.md]

### `LOCATION path`

Optionally creates an external table with the provided location as the path where data is stored. If `table_name` itself is a path instead of a table identifier, the operation fails. `path` must be a STRING literal. ^[create-table-clone-databricks-on-aws.md]

## Examples

### Deep Clone a [Delta Lake Table](/concepts/delta-lake-table.md)

The following example creates a complete, independent copy of the source table:

```sql
CREATE TABLE target_catalog.target_schema.target_table
DEEP CLONE source_catalog.source_schema.source_table;
```

^[create-table-clone-databricks-on-aws.md]

### Shallow Clone a [Delta Lake Table](/concepts/delta-lake-table.md)

The following example creates a copy of the source table's metadata that references the source data files:

```sql
CREATE TABLE target_catalog.target_schema.target_table
SHALLOW CLONE source_catalog.source_schema.source_table;
```

^[create-table-clone-databricks-on-aws.md]

### Deep Clone a Managed Iceberg Table

Only deep cloning is supported for managed Iceberg tables:

```sql
CREATE TABLE target_catalog.target_schema.target_table
DEEP CLONE source_catalog.source_schema.source_table;
```

^[create-table-clone-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The underlying storage format that powers clone operations.
- [Deep Clone](/concepts/deep-clone.md) – A cloning method that creates a full, independent copy of the data.
- [Shallow Clone](/concepts/shallow-clone.md) – A cloning method that copies metadata only and references source data.
- [Unity Catalog](/concepts/unity-catalog.md) – Where shallow clone support is available for managed tables in Databricks SQL and Databricks Runtime 13.3 LTS and above.
- TBLPROPERTIES – Used to set user-defined properties on tables during cloning.
- [Incremental Cloning](/concepts/incremental-cloning-to-delta-lake.md) – A related capability for cloning Parquet and Iceberg tables incrementally to Delta Lake.

## Sources

- create-table-clone-databricks-on-aws.md

# Citations

1. [create-table-clone-databricks-on-aws.md](/references/create-table-clone-databricks-on-aws-49def2a6.md)
