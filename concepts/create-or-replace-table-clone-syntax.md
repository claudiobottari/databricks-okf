---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f92afe624aa447888583494d20ecf7a29bf70428b592cfd6ec9194b10e0c8e8c
  pageDirectory: concepts
  sources:
    - create-table-clone-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - create-or-replace-table-clone-syntax
    - REPLACE TABLE CLONE Syntax OR CREATE
    - CORTCS
  citations:
    - file: create-table-clone-databricks-on-aws.md
title: CREATE OR REPLACE TABLE CLONE Syntax
description: A SQL syntax variant for cloning that either replaces an existing target table or creates a new one if it does not exist.
tags:
  - databricks
  - sql-syntax
  - cloning
timestamp: "2026-06-19T14:38:53.953Z"
---

# CREATE OR REPLACE TABLE CLONE Syntax

**Applies to:** Databricks SQL and Databricks Runtime.

The `CREATE OR REPLACE TABLE CLONE` statement clones a source Delta, managed Apache Iceberg, or Apache Parquet table to a target location at a specific version. If the target table already exists, it is replaced; if it does not exist, it is created. Cloning can be either deep or shallow. ^[create-table-clone-databricks-on-aws.md]

## Overview

This command creates a copy of a source table at a specified version. A **deep clone** copies both the table’s metadata and its data files, producing an independent copy. A **shallow clone** copies only the table’s definition and references the source table’s data files. ^[create-table-clone-databricks-on-aws.md]

- **Delta**, **Parquet**, and **Foreign Iceberg** tables support both deep and shallow cloning.  
- **Managed Iceberg** tables support only deep cloning, and the table format cannot be changed during the clone. ^[create-table-clone-databricks-on-aws.md]

> **Important:** There are important differences between shallow and deep clones that affect storage, performance, and data independence. See Clone a table on Databricks for details.  
> **Note:** Streaming tables and [materialized views](/concepts/materialized-views-in-databricks.md) are not supported as source or target tables for `CLONE`. ^[create-table-clone-databricks-on-aws.md]

## Syntax

```sql
[CREATE OR] REPLACE TABLE table_name
  [SHALLOW | DEEP] CLONE source_table_name
  [TBLPROPERTIES clause]
  [LOCATION path]
```

The `CREATE OR` phrase is optional. If omitted, `table_name` must already exist. If `CREATE OR` is included, the table is replaced if it exists or created new if it does not. ^[create-table-clone-databricks-on-aws.md]

## Parameters

- **IF NOT EXISTS**  
  If specified, the statement is ignored when `table_name` already exists. (Not shown in the REPLACE syntax above, but available in the simple `CREATE TABLE` variant.) ^[create-table-clone-databricks-on-aws.md]

- **`[CREATE OR] REPLACE`**  
  Determines whether the target table must already exist (`REPLACE`) or can be created fresh (`CREATE OR REPLACE`). ^[create-table-clone-databricks-on-aws.md]

- **table_name**  
  The name of the target table. The name must not include a temporal specification or options specification. If unqualified, the table is created in the current schema. The table must not already exist unless `REPLACE` or `IF NOT EXISTS` is specified. ^[create-table-clone-databricks-on-aws.md]

- **SHALLOW CLONE** or **DEEP CLONE**  
  - `SHALLOW CLONE`: Copies only the table definition; data files remain in the source location.  
  - `DEEP CLONE` (default): Creates a complete, independent copy of the source table, including all data files.  
  Managed Iceberg tables support only deep clone. ^[create-table-clone-databricks-on-aws.md]

- **source_table_name**  
  The name of the source table to clone. The name may include a temporal specification or options specification. ^[create-table-clone-databricks-on-aws.md]

- **TBLPROPERTIES clause**  
  Optionally sets one or more user-defined properties on the target table. ^[create-table-clone-databricks-on-aws.md]

- **LOCATION path**  
  Optionally creates an external table at the specified path. If `table_name` itself is a path (instead of a table identifier), the operation fails. `path` must be a STRING literal. ^[create-table-clone-databricks-on-aws.md]

## Examples

### Deep clone a Delta table

```sql
CREATE OR REPLACE TABLE target_catalog.target_schema.target_table
DEEP CLONE source_catalog.source_schema.source_table;
```

### Shallow clone a Delta table

```sql
CREATE OR REPLACE TABLE target_catalog.target_schema.target_table
SHALLOW CLONE source_catalog.source_schema.source_table;
```

### Deep clone a managed Iceberg table (only deep clone is supported)

```sql
CREATE OR REPLACE TABLE target_catalog.target_schema.target_table
DEEP CLONE source_catalog.source_schema.source_table;
```

^[create-table-clone-databricks-on-aws.md]

For more Delta Lake clone examples (including data archiving and ML workflows), see Clone a table on Databricks. For managed Iceberg clone examples, see [Clone a managed Iceberg table](/concepts/managed-iceberg-table-cloning.md).

## Related Concepts

- Deep Clone vs Shallow Clone — Differences in storage, cost, and data independence.
- Clone a table on Databricks — Comprehensive guide with use cases.
- [Delta Lake](/concepts/delta-lake.md) — Format that supports both clone types.
- Managed Iceberg tables — Supported only for deep clone.
- [Incrementally clone Parquet and Apache Iceberg tables to Delta Lake](/concepts/incremental-clone-of-parquet-and-iceberg-to-delta-lake.md) — For incremental cloning workflows.
- Streaming tables and [Materialized views](/concepts/materialized-views-in-databricks.md) — Not supported as source or target for `CLONE`.
- [Unity Catalog Shallow Clone](/concepts/unity-catalog-shallow-clone.md) — Shallow clone support for Unity Catalog managed tables (Databricks SQL and Runtime 13.3 LTS and above).

## Sources

- create-table-clone-databricks-on-aws.md

# Citations

1. [create-table-clone-databricks-on-aws.md](/references/create-table-clone-databricks-on-aws-49def2a6.md)
