---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 00371458192759f78fbb6fd8a7c7ef4e86dc3c25798c37b9cdfeb6e04ee4a679
  pageDirectory: concepts
  sources:
    - create-table-clone-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - shallow-clone
    - shallow-clone-databricks
    - SC(
    - shallow-clone-delta-lake
    - SC(L
    - Shallow clone vs. deep clone
    - shallow-clone-delta-table
    - SC(T
    - Shallow clone for Unity Catalog tables
  citations:
    - file: create-table-clone-databricks-on-aws.md
title: Shallow Clone
description: A cloning strategy that copies only the source table's metadata and references the source data files without copying the data.
tags:
  - delta-lake
  - data-management
  - cloning
timestamp: "2026-06-18T14:55:51.256Z"
---

# Shallow Clone

**Shallow clone** is a table cloning operation in Databricks that creates a copy of a source table's metadata and schema without copying its underlying data files. Instead, the shallow clone references the source table's existing data files, making it a lightweight, zero-copy operation.

## How it works

When you perform a shallow clone, Databricks creates a new table definition that points to the same storage location as the source table. The clone inherits the source table's schema, partitioning, and table properties, but does not duplicate the data. This means the shallow clone is essentially a snapshot of the table's metadata that shares the original data files. ^[create-table-clone-databricks-on-aws.md]

## Supported sources

- **Delta Lake** tables: Support both shallow and deep cloning.
- **Parquet** tables: Support both shallow and deep cloning.
- **Foreign Apache Iceberg** tables: Support both shallow and deep cloning.
- **Managed Iceberg** tables: Support only deep cloning; shallow cloning is not supported for managed Iceberg tables.

^[create-table-clone-databricks-on-aws.md]

## Platform support

In Databricks SQL and Databricks Runtime 13.3 LTS and above, shallow clones are supported with [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md). In Databricks Runtime 12.2 LTS and below, shallow clones are not supported in Unity Catalog. ^[create-table-clone-databricks-on-aws.md]

## Syntax

The basic syntax for creating a shallow clone is:

```sql
CREATE TABLE [IF NOT EXISTS] table_name
SHALLOW CLONE source_table_name
[TBLPROPERTIES clause]
[LOCATION path]
```

Or to replace an existing table:

```sql
[CREATE OR] REPLACE TABLE table_name
SHALLOW CLONE source_table_name
[TBLPROPERTIES clause]
[LOCATION path]
```

^[create-table-clone-databricks-on-aws.md]

## Parameters

- **table_name**: The name of the target table to create. Must not include a temporal specification or options specification.
- **source_table_name**: The name of the source table to clone. May include a temporal specification.
- **TBLPROPERTIES**: Optionally sets user-defined properties on the cloned table.
- **LOCATION path**: Optionally creates an external table at a specified storage path.

^[create-table-clone-databricks-on-aws.md]

## Deep clone vs. shallow clone

The key difference between deep clone and shallow clone is that deep clones create a complete, independent copy of the source data, while shallow clones only copy the table's definition and metadata, referencing the source data files. This distinction determines how they can be used:

- **Deep clone**: Makes a full copy of the data and metadata, creating an independent table.
- **Shallow clone**: Copies only metadata, with the new table referencing the source data files.

^[create-table-clone-databricks-on-aws.md]

## Limitations

Streaming tables and materialized views are not supported as source or target tables for the `CLONE` operation. ^[create-table-clone-databricks-on-aws.md]

## Use cases

Shallow clones are useful for:

- Creating lightweight copies of large tables for testing or development
- Sharing a table's schema structure without duplicating storage
- Creating multiple derived versions of a table that share the same base data

## Related concepts

- [Deep Clone](/concepts/deep-clone.md) – The alternative cloning method that copies both data and metadata
- [Delta Lake](/concepts/delta-lake.md) – The storage format that supports shallow cloning
- [Table cloning](/concepts/delta-table-cloning.md) – The general operation for creating table copies
- [Unity Catalog](/concepts/unity-catalog.md) – The catalog system that supports shallow clones in newer runtimes

# Citations

1. [create-table-clone-databricks-on-aws.md](/references/create-table-clone-databricks-on-aws-49def2a6.md)
