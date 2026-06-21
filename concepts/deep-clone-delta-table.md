---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 60a1f07fcaa52c791bd8b0ddd093a781ac6a088ef64f18eb029619d2ed530492
  pageDirectory: concepts
  sources:
    - create-table-clone-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deep-clone-delta-table
    - DC(T
    - Deep Clone a Delta Table
    - Deep Clone a Delta Table|clone a Delta table
  citations:
    - file: create-table-clone-databricks-on-aws.md
title: Deep Clone (Delta Table)
description: A complete, independent copy of a source Delta, Iceberg, or Parquet table, including both data and metadata.
tags:
  - databricks
  - delta-lake
  - cloning
timestamp: "2026-06-19T14:38:42.231Z"
---

# Deep Clone (Delta Table)

**Deep Clone (Delta Table)** is a Delta Lake operation that creates a complete, independent copy of a source Delta table, including both its metadata and underlying data files. Unlike a [Shallow Clone (Delta Table)](/concepts/shallow-clone-delta-table.md), a deep clone does not reference the source table's files — the target table is fully self-contained and can be modified without affecting the source.

## Overview

A deep clone copies the full table definition and all data files from the source to a target location. The resulting table is an independent snapshot of the source at the time of cloning. This makes deep clones suitable for scenarios where the target must be isolated from the source, such as data archiving, creating development or testing environments, or producing immutable snapshots for machine learning workflows. ^[create-table-clone-databricks-on-aws.md]

Deep cloning is the default behavior when no clone type is explicitly specified. ^[create-table-clone-databricks-on-aws.md]

## Syntax

```sql
CREATE TABLE target_catalog.target_schema.target_table
DEEP CLONE source_catalog.source_schema.source_table;
```

The `DEEP` keyword is optional — omitting it also produces a deep clone. ^[create-table-clone-databricks-on-aws.md]

### Parameters

- **`table_name`** — The name of the target table to create. Must not include a temporal specification or options specification. If the name is unqualified, the table is created in the current schema. ^[create-table-clone-databricks-on-aws.md]
- **`source_table_name`** — The name of the source table to clone. May include a temporal specification or options specification to clone from a specific version or timestamp. ^[create-table-clone-databricks-on-aws.md]
- **`TBLPROPERTIES clause`** — Optionally sets one or more user-defined properties on the target table. ^[create-table-clone-databricks-on-aws.md]
- **`LOCATION path`** — Optionally creates an external table with the provided path as the storage location. The path must be a STRING literal. ^[create-table-clone-databricks-on-aws.md]

### Variants

- **`CREATE TABLE [IF NOT EXISTS] ... DEEP CLONE`** — Creates the target table only if it does not already exist. ^[create-table-clone-databricks-on-aws.md]
- **`[CREATE OR] REPLACE TABLE ... DEEP CLONE`** — Replaces the target table if it exists, or creates it if it does not. ^[create-table-clone-databricks-on-aws.md]

## Supported Source Formats

Deep cloning is supported for the following source table formats:

- **Delta tables** — Both managed and external Delta tables can be deep cloned. ^[create-table-clone-databricks-on-aws.md]
- **Managed Apache Iceberg tables** — Only deep cloning is supported; shallow cloning is not available for managed Iceberg tables. ^[create-table-clone-databricks-on-aws.md]
- **Apache Parquet tables** — Parquet tables can be deep cloned to Delta Lake. ^[create-table-clone-databricks-on-aws.md]
- **Foreign Iceberg tables** — Foreign Iceberg tables support deep cloning. ^[create-table-clone-databricks-on-aws.md]

## Limitations

- **Streaming tables and materialized views** are not supported as source or target tables for `CLONE`. ^[create-table-clone-databricks-on-aws.md]
- **Managed Iceberg tables** support only deep cloning; you cannot change the table format during cloning. ^[create-table-clone-databricks-on-aws.md]
- If `table_name` is itself a path instead of a table identifier, the operation will fail. ^[create-table-clone-databricks-on-aws.md]

## Example

```sql
-- Deep clone: copies data and metadata
CREATE TABLE target_catalog.target_schema.target_table
DEEP CLONE source_catalog.source_schema.source_table;
```

This creates a fully independent copy of `source_table` at `target_table`. Any subsequent writes to either table do not affect the other. ^[create-table-clone-databricks-on-aws.md]

## Related Concepts

- [Shallow Clone (Delta Table)](/concepts/shallow-clone-delta-table.md) — Copies metadata only; references source data files without copying them.
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format for Delta tables.
- Clone a Table on Databricks — General guidance on when to use deep vs. shallow clones.
- [Incrementally Clone Parquet and Iceberg Tables to Delta Lake](/concepts/incremental-clone-of-parquet-and-iceberg-to-delta-lake.md) — Migration workflows using clone operations.
- [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md) — Support for shallow clones in Unity Catalog (Databricks SQL and Databricks Runtime 13.3 LTS+).

## Sources

- create-table-clone-databricks-on-aws.md

# Citations

1. [create-table-clone-databricks-on-aws.md](/references/create-table-clone-databricks-on-aws-49def2a6.md)
