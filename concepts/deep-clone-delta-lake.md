---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 928759d3e532b8f77073a7be7652b27e3127600304aadd71828415d548c5ede5
  pageDirectory: concepts
  sources:
    - create-table-clone-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deep-clone-delta-lake
    - DC(L
    - CLONE (Delta Lake)
    - Clone Table
  citations:
    - file: create-table-clone-databricks-on-aws.md
title: Deep Clone (Delta Lake)
description: A complete, independent copy of a source Delta, Iceberg, or Parquet table, including both data and metadata.
tags:
  - delta-lake
  - cloning
  - data-management
timestamp: "2026-06-19T18:02:30.319Z"
---

# Deep Clone (Delta Lake)

**Deep Clone (Delta Lake)** is a `CREATE TABLE CLONE` operation that creates a complete, independent copy of a source [Delta Lake Table](/concepts/delta-lake-table.md), including both the table's metadata and all of its underlying data files. In Databricks SQL and Databricks Runtime, deep clone is the default cloning behavior when no shallow or deep keyword is specified.^[create-table-clone-databricks-on-aws.md]

## Overview

When you perform a deep clone, Databricks copies the full table definition and all data files to a new target location, producing a fully independent table that does not reference the source. Deep clones are supported for Delta tables, managed Apache Parquet tables, and foreign Apache Iceberg tables. Managed Iceberg tables support only deep cloning — shallow cloning is not available for that format.^[create-table-clone-databricks-on-aws.md]

Deep clones are useful for creating production snapshots, archiving historical states, and building isolated environments for testing or machine learning workflows. Unlike a [Shallow Clone (Delta Lake)](/concepts/shallow-clone-delta-lake.md), a deep clone's target table will not break if the source table is deleted or its files are changed, because all data has been physically copied.

## Syntax

The basic syntax for a deep clone is:

```sql
CREATE TABLE target_catalog.target_schema.target_table
DEEP CLONE source_catalog.source_schema.source_table;
```

Or, to replace an existing table:

```sql
CREATE OR REPLACE TABLE table_name
DEEP CLONE source_table_name;
```

The `DEEP CLONE` keyword is optional when performing a deep clone because deep is the default clone type. However, explicitly specifying it is recommended for clarity.^[create-table-clone-databricks-on-aws.md]

### Optional Clauses

- **`IF NOT EXISTS`** — Skips the operation if the target table already exists.^[create-table-clone-databricks-on-aws.md]
- **`[CREATE OR] REPLACE`** — Creates the table if it does not exist, or replaces it if it does.^[create-table-clone-databricks-on-aws.md]
- **`TBLPROPERTIES clause`** — Sets one or more user-defined properties on the cloned table.^[create-table-clone-databricks-on-aws.md]
- **`LOCATION path`** — Specifies an external storage path for the target table's data.^[create-table-clone-databricks-on-aws.md]

## Supported Source Formats

| Source Format | Deep Clone Supported | Shallow Clone Supported |
|---|---|---|
| Delta Lake | Yes | Yes |
| Foreign Iceberg | Yes | Yes |
| Managed Iceberg | Yes | No |
| Parquet | Yes | Yes |

^[create-table-clone-databricks-on-aws.md]

## Limitations

- **Streaming tables and materialized views** cannot be used as source or target tables for any `CLONE` operation.^[create-table-clone-databricks-on-aws.md]
- For managed Iceberg tables, the table format cannot be changed during cloning.^[create-table-clone-databricks-on-aws.md]

## Related Concepts

- [Shallow Clone (Delta Lake)](/concepts/shallow-clone-delta-lake.md) — A clone that copies only metadata and references source data files without copying the data.
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format for delta tables on Databricks.
- Clone a table on Databricks — General guidance for when to use deep vs. shallow clones.
- [Incrementally clone Parquet and Apache Iceberg tables to Delta Lake](/concepts/incremental-clone-of-parquet-and-iceberg-to-delta-lake.md) — Procedure for incremental cloning of non-Delta formats.
- [Shallow clone for Unity Catalog tables](/concepts/shallow-clone-delta-table.md) — Unity Catalog-specific considerations for shallow cloning.
- Databricks SQL — The SQL interface used for executing `CREATE TABLE CLONE` statements.

## Sources

- create-table-clone-databricks-on-aws.md

# Citations

1. [create-table-clone-databricks-on-aws.md](/references/create-table-clone-databricks-on-aws-49def2a6.md)
