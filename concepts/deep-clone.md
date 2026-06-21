---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 034af79621f8c070072bae115cac28550735578cc90009d42b381cf4ebc5be82
  pageDirectory: concepts
  sources:
    - create-table-clone-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deep-clone
    - CLONE
    - Deep cloning
    - Delta Deep Clone
  citations:
    - file: create-table-clone-databricks-on-aws.md
title: Deep Clone
description: A cloning strategy that creates a complete, independent copy of a source table, including all data and metadata.
tags:
  - delta-lake
  - data-management
  - cloning
timestamp: "2026-06-18T14:55:39.125Z"
---

# Deep Clone

**Deep Clone** is an operation that creates a complete, independent copy of a source table, including its data and metadata. Unlike [Shallow Clone](/concepts/shallow-clone.md), which references the source's data files, a deep clone duplicates the data so that the target table is fully independent. ^[create-table-clone-databricks-on-aws.md]

## Overview

When you perform a DEEP CLONE, Databricks copies the source table's definition, data files, and metadata to a new location, producing a standalone table. This is the default clone mode (if neither `SHALLOW CLONE` nor `DEEP CLONE` is specified, deep clone is used). ^[create-table-clone-databricks-on-aws.md]

Deep clones are useful for data archiving, creating snapshots for machine learning workflows, or making an independent copy of a table for development and testing without affecting the original.

## Supported Table Formats

Deep clone is supported for the following source table formats:

- **Delta Lake** tables (managed and external)
- **Apache Parquet** tables
- **Foreign Iceberg** tables (Iceberg tables managed outside Databricks)
- **Managed Iceberg** tables (Iceberg tables managed by Databricks; only deep cloning is supported, not shallow cloning) ^[create-table-clone-databricks-on-aws.md]

Managed Iceberg tables also do not allow you to change the table format during cloning. ^[create-table-clone-databricks-on-aws.md]

## Syntax

The `CREATE TABLE ... DEEP CLONE` and `REPLACE TABLE ... DEEP CLONE` statements are used.

```sql
CREATE TABLE [IF NOT EXISTS] table_name
  DEEP CLONE source_table_name
  [TBLPROPERTIES clause]
  [LOCATION path]

[CREATE OR] REPLACE TABLE table_name
  DEEP CLONE source_table_name
  [TBLPROPERTIES clause]
  [LOCATION path]
```

^[create-table-clone-databricks-on-aws.md]

### Parameters

- **IF NOT EXISTS** – If specified, the statement is ignored if `table_name` already exists. ^[create-table-clone-databricks-on-aws.md]
- **[CREATE OR] REPLACE** – If `CREATE OR` is specified, the table is replaced if it exists and newly created if it does not. Without `CREATE OR`, the `table_name` must already exist. ^[create-table-clone-databricks-on-aws.md]
- **table_name** – The name of the table to be created. The name must not include a temporal specification or options specification. If the name is not qualified, the table is created in the current schema. ^[create-table-clone-databricks-on-aws.md]
- **source_table_name** – The name of the table to be cloned. May include a temporal specification or options specification (e.g., to clone at a specific version). ^[create-table-clone-databricks-on-aws.md]
- **TBLPROPERTIES** – Optionally sets one or more user-defined properties on the target table. ^[create-table-clone-databricks-on-aws.md]
- **LOCATION path** – Optionally creates an external table with the provided path as the data storage location. `path` must be a STRING literal. If `table_name` itself is a path instead of a table identifier, the operation will fail. ^[create-table-clone-databricks-on-aws.md]

## Examples

### Deep clone a [Delta Lake Table](/concepts/delta-lake-table.md)

```sql
CREATE TABLE target_catalog.target_schema.target_table
DEEP CLONE source_catalog.source_schema.source_table;
```

^[create-table-clone-databricks-on-aws.md]

### Deep clone a managed Iceberg table

```sql
CREATE TABLE target_catalog.target_schema.target_table
DEEP CLONE source_catalog.source_schema.source_table;
```

^[create-table-clone-databricks-on-aws.md]

## Limitations

- **Streaming tables** and **materialized views** are not supported as source or target tables for any CLONE operation (deep or shallow). ^[create-table-clone-databricks-on-aws.md]
- For managed Iceberg tables, only deep cloning is available; shallow cloning is not supported. ^[create-table-clone-databricks-on-aws.md]
- When cloning managed Iceberg tables, you cannot change the table format during the clone operation. ^[create-table-clone-databricks-on-aws.md]

## Comparison with Shallow Clone

| Aspect | Deep Clone | Shallow Clone |
|--------|------------|---------------|
| Data copy | Full, independent copy | References source data files |
| Metadata | Copied independently | Copied definition only |
| Independence | Fully independent from source | Dependent on source files |
| Default | Yes (if no SHALLOW specified) | No |
| Unity Catalog support (managed tables) | Supported | Supported in Databricks SQL and Runtime 13.3 LTS+ |

*Note: Detailed comparison is available in the [Clone a table on Databricks](https://docs.databricks.com/aws/en/tables/operations/clone) documentation.* ^[create-table-clone-databricks-on-aws.md]

## Related Concepts

- [Shallow Clone](/concepts/shallow-clone.md)
- [Delta Lake](/concepts/delta-lake.md)
- [Managed Iceberg](/concepts/managed-iceberg-table-cloning.md)
- Clone Table on Databricks
- External Table

## Sources

- create-table-clone-databricks-on-aws.md

# Citations

1. [create-table-clone-databricks-on-aws.md](/references/create-table-clone-databricks-on-aws-49def2a6.md)
