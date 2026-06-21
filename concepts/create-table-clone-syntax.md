---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 636ac8839bcff9fa61f00b76fbeecc36b8250852c9feabf656d7c2a1eaf50891
  pageDirectory: concepts
  sources:
    - create-table-clone-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - create-table-clone-syntax
    - CTCS
    - CREATE TABLE CLONE
    - CREATE TABLE ... DEEP CLONE
  citations:
    - file: create-table-clone-databricks-on-aws.md
title: CREATE TABLE CLONE Syntax
description: The SQL syntax for cloning tables in Databricks, including CREATE TABLE, CREATE OR REPLACE TABLE, IF NOT EXISTS, SHALLOW/DEEP CLONE, TBLPROPERTIES, and LOCATION clauses.
tags:
  - databricks
  - sql
  - reference
timestamp: "2026-06-19T09:38:45.642Z"
---

# CREATE TABLE CLONE Syntax

**CREATE TABLE CLONE** is a SQL statement in Databricks that creates a copy of a source [Delta Lake](/concepts/delta-lake.md), managed [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md), or Apache Parquet table at a specific version. Cloning can be either **deep** (copies the data) or **shallow** (references the source data without copying it). ^[create-table-clone-databricks-on-aws.md]

## Supported Table Types

- **Delta**, **Parquet**, and **Foreign Iceberg** tables support both deep and shallow cloning. ^[create-table-clone-databricks-on-aws.md]
- **Managed Iceberg** tables support only deep cloning, and the table format cannot be changed during cloning. ^[create-table-clone-databricks-on-aws.md]

## Syntax[​](#syntax "Direct link to Syntax")

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

## Parameters[​](#parameters "Direct link to Parameters")

- **`IF NOT EXISTS`** — If specified, the statement is ignored if `table_name` already exists. ^[create-table-clone-databricks-on-aws.md]
- **`[CREATE OR] REPLACE`** — If `CREATE OR` is specified, the table is replaced if it exists and newly created if it does not. Without `CREATE OR`, the `table_name` must exist. ^[create-table-clone-databricks-on-aws.md]
- **`table_name`** — The name of the table to be created. The name must not include a temporal specification or options specification. If the name is not qualified, the table is created in the current schema. `table_name` must not exist already unless `REPLACE` or `IF NOT EXISTS` has been specified. ^[create-table-clone-databricks-on-aws.md]
- **`SHALLOW CLONE`** or **`DEEP CLONE`** — `SHALLOW CLONE` copies the source table's definition but refers to the source table's files. `DEEP CLONE` (default) makes a complete, independent copy of the source table. Managed Iceberg tables only support deep cloning. ^[create-table-clone-databricks-on-aws.md]
- **`source_table_name`** — The name of the table to be cloned. The name may include a temporal specification or options specification. ^[create-table-clone-databricks-on-aws.md]
- **`TBLPROPERTIES` clause** — Optionally sets one or more user-defined properties. ^[create-table-clone-databricks-on-aws.md]
- **`LOCATION path`** — Optionally creates an external table, with the provided location as the path where the data is stored. If `table_name` itself is a path instead of a table identifier, the operation will fail. `path` must be a STRING literal. ^[create-table-clone-databricks-on-aws.md]

## Examples[​](#examples "Direct link to Examples")

### Deep Clone and Shallow Clone of a [Delta Lake Table](/concepts/delta-lake-table.md)

```sql
-- Deep clone: copies data and metadata
CREATE TABLE target_catalog.target_schema.target_table
DEEP CLONE source_catalog.source_schema.source_table;

-- Shallow clone: copies metadata only, references source data files
CREATE TABLE target_catalog.target_schema.target_table
SHALLOW CLONE source_catalog.source_schema.source_table;
```

^[create-table-clone-databricks-on-aws.md]

### Deep Clone of a Managed Iceberg Table

```sql
CREATE TABLE target_catalog.target_schema.target_table
DEEP CLONE source_catalog.source_schema.source_table;
```

^[create-table-clone-databricks-on-aws.md]

## Limitations

- Streaming tables and [materialized views](/concepts/materialized-views-in-databricks.md) are not supported as source or target tables for `CLONE`. ^[create-table-clone-databricks-on-aws.md]
- In Databricks Runtime 12.2 LTS and below, there is no support for shallow clones in [Unity Catalog](/concepts/unity-catalog.md). Shallow clone with Unity Catalog managed tables is supported in Databricks SQL and Databricks Runtime 13.3 LTS and above. ^[create-table-clone-databricks-on-aws.md]

## Related Concepts

- [Deep Clone](/concepts/deep-clone.md) — A complete, independent copy of the source table including data.
- [Shallow Clone](/concepts/shallow-clone.md) — A metadata-only copy that references source data files.
- Clone a Table on Databricks — Detailed guidance on cloning operations, including data archiving and ML workflows.
- [Incrementally Clone Parquet and Iceberg Tables to Delta Lake](/concepts/incremental-clone-of-parquet-and-iceberg-to-delta-lake.md) — Cloning process for migrating data to Delta Lake format.
- Shallow Clone for Unity Catalog Tables — Specific considerations for shallow cloning within Unity Catalog.

## Sources

- create-table-clone-databricks-on-aws.md

# Citations

1. [create-table-clone-databricks-on-aws.md](/references/create-table-clone-databricks-on-aws-49def2a6.md)
