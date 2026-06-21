---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 40e703fb1ef1eda9f98cfac29f13e451638a25ee9219bcd15e5008e839095967
  pageDirectory: concepts
  sources:
    - create-table-clone-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - create-or-replace-clone
    - REPLACE CLONE OR CREATE
    - CORC
    - REPLACE ON
  citations:
    - file: create-table-clone-databricks-on-aws.md
title: CREATE OR REPLACE CLONE
description: A variant of the CLONE statement that replaces an existing table if it exists or creates a new one if it does not (without CREATE OR, the target table must already exist).
tags:
  - databricks
  - sql
  - cloning
timestamp: "2026-06-19T09:39:19.854Z"
---

# CREATE OR REPLACE CLONE

**CREATE OR REPLACE CLONE** is a SQL statement in Databricks that creates a table by cloning a source Delta, managed Apache Iceberg, or Apache Parquet table, replacing the target table if it already exists or creating it if it does not. This operation supports both deep and shallow cloning. ^[create-table-clone-databricks-on-aws.md]

## Overview

The `CREATE OR REPLACE CLONE` syntax is a variant of the `CREATE TABLE ... CLONE` statement. When `CREATE OR` is specified, the command either replaces the target table if it already exists or creates a new table if it does not. Without `CREATE OR`, the target table must already exist for a `REPLACE` operation. ^[create-table-clone-databricks-on-aws.md]

Cloning can be either deep or shallow:

- **Deep Clone** (default): Makes a complete, independent copy of the source table, including both data and metadata.
- **Shallow Clone**: Makes a copy of the source table's definition but refers to the source table's data files, without copying the data itself. ^[create-table-clone-databricks-on-aws.md]

## Syntax

```sql
[CREATE OR] REPLACE TABLE table_name
  [SHALLOW | DEEP] CLONE source_table_name
  [TBLPROPERTIES clause]
  [LOCATION path]
```

^[create-table-clone-databricks-on-aws.md]

## Parameters

- **`[CREATE OR] REPLACE`**: If `CREATE OR` is specified, the table is replaced if it exists and newly created if it does not. Without `CREATE OR`, the `table_name` must already exist. ^[create-table-clone-databricks-on-aws.md]

- **`table_name`**: The name of the table to be created or replaced. The name must not include a temporal specification or options specification. If the name is not qualified, the table is created in the current schema. ^[create-table-clone-databricks-on-aws.md]

- **`SHALLOW CLONE`** or **`DEEP CLONE`**: Specifies the clone type. `DEEP CLONE` is the default. Managed Iceberg tables only support deep cloning, not shallow cloning. ^[create-table-clone-databricks-on-aws.md]

- **`source_table_name`**: The name of the table to be cloned. The name may include a temporal specification or options specification. ^[create-table-clone-databricks-on-aws.md]

- **`TBLPROPERTIES`**: Optionally sets one or more user-defined properties. ^[create-table-clone-databricks-on-aws.md]

- **`LOCATION path`**: Optionally creates an external table with the provided location as the path where the data is stored. `path` must be a STRING literal. If `table_name` itself is a path instead of a table identifier, the operation will fail. ^[create-table-clone-databricks-on-aws.md]

## Supported Source Tables

- **Delta tables**: Support both deep and shallow cloning.
- **Parquet tables**: Support both deep and shallow cloning.
- **Foreign Iceberg tables**: Support both deep and shallow cloning.
- **Managed Iceberg tables**: Support only deep cloning. You cannot change the table format during cloning. ^[create-table-clone-databricks-on-aws.md]

## Limitations

- **Streaming tables** and **materialized views** are not supported as source or target tables for `CLONE`. ^[create-table-clone-databricks-on-aws.md]

- In Databricks Runtime 12.2 LTS and below, there is no support for shallow clones in Unity Catalog. Shallow clone is supported with Unity Catalog managed tables in Databricks SQL and Databricks Runtime 13.3 LTS and above. ^[create-table-clone-databricks-on-aws.md]

## Example

```sql
-- Replace the target table if it exists, or create it if it doesn't
CREATE OR REPLACE TABLE target_catalog.target_schema.target_table
DEEP CLONE source_catalog.source_schema.source_table;

-- Shallow clone with replace
CREATE OR REPLACE TABLE target_catalog.target_schema.target_table
SHALLOW CLONE source_catalog.source_schema.source_table;
```

^[create-table-clone-databricks-on-aws.md]

## Related Concepts

- Clone a Table on Databricks – General guidance on deep vs. shallow clones
- [CREATE TABLE CLONE](/concepts/create-table-clone-syntax.md) – The base cloning statement without replace behavior
- Shallow Clone for Unity Catalog Tables – Unity Catalog-specific shallow clone details
- [Incrementally Clone Parquet and Iceberg Tables to Delta Lake](/concepts/incremental-clone-of-parquet-and-iceberg-to-delta-lake.md) – Migration workflows using clone
- TBLPROPERTIES – Setting table properties during clone operations

## Sources

- create-table-clone-databricks-on-aws.md

# Citations

1. [create-table-clone-databricks-on-aws.md](/references/create-table-clone-databricks-on-aws-49def2a6.md)
