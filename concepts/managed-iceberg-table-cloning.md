---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 34e6b193dfd1603e4d334ce5d558a830ba24f878af194f7619978f848ce097e0
  pageDirectory: concepts
  sources:
    - create-table-clone-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - managed-iceberg-table-cloning
    - MITC
    - Managed Iceberg Table
    - Clone a Managed Iceberg Table
    - Clone a managed Iceberg table
    - Managed Iceberg
    - Managed Iceberg Table|managed Iceberg tables
    - managed-iceberg-table-clone-limitations
    - MITCL
    - managed-iceberg-table-clone-restrictions
    - MITCR
  citations:
    - file: create-table-clone-databricks-on-aws.md
title: Managed Iceberg Table Cloning
description: Managed Iceberg tables on Databricks support only deep cloning, not shallow cloning, and the table format cannot be changed during the clone operation.
tags:
  - databricks
  - iceberg
  - cloning
timestamp: "2026-06-19T09:38:36.503Z"
---

# Managed Iceberg Table Cloning

**Managed Iceberg Table Cloning** refers to the process of creating an independent, full copy of a managed Apache Iceberg table at a specific version using Databricks’ `CREATE TABLE CLONE` syntax. Unlike [Delta Lake](/concepts/delta-lake.md) or foreign Iceberg tables, managed Iceberg tables support only deep cloning and do not allow changing the table format during the cloning operation. ^[create-table-clone-databricks-on-aws.md]

## Definition and Scope

A clone is a copy of a source table at a particular point in time. For managed Iceberg tables, only a **deep clone** is supported — a complete, independent copy that includes both the table definition and all underlying data files. A shallow clone (which copies only metadata and references the source’s data files) is not permitted for managed Iceberg tables. ^[create-table-clone-databricks-on-aws.md]

Additionally, you cannot change the table format when cloning a managed Iceberg table; the target table must also be Iceberg. ^[create-table-clone-databricks-on-aws.md]

## Syntax

The generic `CREATE TABLE CLONE` syntax applies, but for managed Iceberg tables you must use `DEEP CLONE`. The `SHALLOW CLONE` keyword is not supported; if omitted, `DEEP CLONE` is the default.

```sql
CREATE TABLE [IF NOT EXISTS] target_catalog.target_schema.target_table
DEEP CLONE source_catalog.source_schema.source_table;

-- or with REPLACE
CREATE OR REPLACE TABLE target_catalog.target_schema.target_table
DEEP CLONE source_catalog.source_schema.source_table;
```

^[create-table-clone-databricks-on-aws.md]

## Parameters

- **IF NOT EXISTS** – The statement is ignored if `table_name` already exists.
- **[CREATE OR] REPLACE** – Creates the table if it does not exist, or replaces it if it does.
- **table_name** – The name of the target table. Must not include a temporal or options specification.
- **SHALLOW CLONE or DEEP CLONE** – For managed Iceberg tables, only `DEEP CLONE` is valid. `SHALLOW CLONE` results in an error.
- **source_table_name** – The source table; may include a temporal specification (e.g., version as of a timestamp).
- **TBLPROPERTIES clause** – Optionally sets user-defined properties.
- **LOCATION path** – Optionally creates an external table at the given path.

^[create-table-clone-databricks-on-aws.md]

## Example

```sql
CREATE TABLE target_catalog.target_schema.target_table
DEEP CLONE source_catalog.source_schema.source_table;
```

^[create-table-clone-databricks-on-aws.md]

## Limitations for Managed Iceberg Tables

- Only deep cloning is supported; shallow cloning is not allowed.
- The table format cannot be changed during cloning (the target remains Iceberg).
- Streaming tables and materialized views are not supported as either source or target for any `CLONE` operation, including Iceberg clones. ^[create-table-clone-databricks-on-aws.md]

## Related Concepts

- [Deep Clone](/concepts/deep-clone.md) – A complete, independent copy of a table.
- [Shallow Clone](/concepts/shallow-clone.md) – A metadata‑only copy that references source data files (not supported for managed Iceberg).
- Managed Iceberg Tables – Unity Catalog‑managed Apache Iceberg tables.
- [Delta Table Cloning](/concepts/delta-table-cloning.md) – Similar cloning concepts for Delta Lake tables, which support both deep and shallow clones.
- [CREATE TABLE CLONE](/concepts/create-table-clone-syntax.md) – The full SQL command reference.
- Foreign Iceberg Tables – Iceberg tables registered externally; these support both deep and shallow clones.

## Sources

- create-table-clone-databricks-on-aws.md

# Citations

1. [create-table-clone-databricks-on-aws.md](/references/create-table-clone-databricks-on-aws-49def2a6.md)
