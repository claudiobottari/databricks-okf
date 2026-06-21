---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: db73f61e92395d0383245c084852f34d72a6409b44efdc823dcabc55a48181db
  pageDirectory: concepts
  sources:
    - create-table-clone-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - clone-with-unity-catalog
    - CWUC
  citations:
    - file: create-table-clone-databricks-on-aws.md
title: CLONE with Unity Catalog
description: Support for shallow cloning Unity Catalog managed tables in Databricks SQL and Runtime 13.3 LTS+, with no shallow clone support in Runtime 12.2 LTS and below.
tags:
  - databricks
  - unity-catalog
  - cloning
timestamp: "2026-06-19T14:38:51.280Z"
---

# CLONE with Unity Catalog

**CLONE with Unity Catalog** refers to the ability to create deep or shallow clones of a source table while the target table is managed under a [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md). Unity Catalog support for the `CREATE TABLE CLONE` command depends on the Databricks Runtime version and the type of clone performed.

## Overview

The `CREATE TABLE [SHALLOW | DEEP] CLONE` command copies a source table’s definition and optionally its data to a new target location. Unity Catalog managed tables can be the target of either deep or shallow clones, with the following version constraints:

- **Databricks SQL and Databricks Runtime 13.3 LTS and above**: shallow clone is fully supported with Unity Catalog managed tables.  
- **Databricks Runtime 12.2 LTS and below**: shallow clone is **not** supported for Unity Catalog managed tables.

These constraints apply only to the target table; the source table can be any supported format (Delta, managed Iceberg, or Parquet). ^[create-table-clone-databricks-on-aws.md]

## Shallow vs. Deep Clone with Unity Catalog

Both deep and shallow clones are available for **Delta**, **Parquet**, and **foreign Iceberg** tables when the target is in Unity Catalog. However, **managed Iceberg tables** support only deep cloning; shallow cloning is not permitted for that source type. ^[create-table-clone-databricks-on-aws.md]

The choice between shallow and deep clones has important data management implications (see Clone a table on Databricks for differences). Shallow clones reference the source data files without copying them, while deep clones create an independent copy of the data. ^[create-table-clone-databricks-on-aws.md]

## Syntax

The general syntax for cloning a table into Unity Catalog is:

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

The `table_name` must follow Unity Catalog naming conventions (catalog.schema.table). If not specified, the table is created in the current schema. ^[create-table-clone-databricks-on-aws.md]

## Examples

**Deep clone** (default) of a Delta table between Unity Catalog schemas:

```sql
CREATE TABLE target_catalog.target_schema.target_table
DEEP CLONE source_catalog.source_schema.source_table;
```

**Shallow clone** of a Delta table (supported in Unity Catalog from Databricks Runtime 13.3 LTS+):

```sql
CREATE TABLE target_catalog.target_schema.target_table
SHALLOW CLONE source_catalog.source_schema.source_table;
```

**Deep clone of a managed Iceberg table** (only deep cloning is supported):

```sql
CREATE TABLE target_catalog.target_schema.target_table
DEEP CLONE source_catalog.source_schema.source_table;
```

^[create-table-clone-databricks-on-aws.md]

## Limitations

- **Streaming tables** and **materialized views** are not supported as either source or target tables for `CLONE`. ^[create-table-clone-databricks-on-aws.md]
- For Unity Catalog managed tables, shallow clone is unavailable on Databricks Runtime 12.2 LTS and earlier. ^[create-table-clone-databricks-on-aws.md]
- Managed Iceberg tables cannot be shallow cloned, and their format cannot be changed during cloning. ^[create-table-clone-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The data governance and metadata layer for tables.
- Clone a table on Databricks – Comprehensive guide to clone operations, including best practices.
- [Delta Lake](/concepts/delta-lake.md) – Default table format for deep/shallow cloning.
- Iceberg tables – Managed Iceberg tables have unique clone restrictions.
- [Shallow Clone](/concepts/shallow-clone.md) – Metadata-only clone referencing source files.
- [Deep Clone](/concepts/deep-clone.md) – Full independent copy of source data.
- Streaming tables – Not supported as CLONE targets.
- [Materialized views](/concepts/materialized-views-in-databricks.md) – Not supported as CLONE sources or targets.

## Sources

- create-table-clone-databricks-on-aws.md

# Citations

1. [create-table-clone-databricks-on-aws.md](/references/create-table-clone-databricks-on-aws-49def2a6.md)
