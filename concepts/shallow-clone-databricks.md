---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 82cd61ff946281538a3eab4c2fea8b63860ad86579390b12ef490c0c2d69033e
  pageDirectory: concepts
  sources:
    - create-table-clone-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - shallow-clone-databricks
    - SC(
  citations:
    - file: create-table-clone-databricks-on-aws.md
title: Shallow Clone (Databricks)
description: A metadata-only copy of a source Delta, Iceberg, or Parquet table that references the source data files without copying them, creating a lightweight pointer.
tags:
  - databricks
  - delta-lake
  - cloning
timestamp: "2026-06-19T09:38:28.803Z"
---

# Shallow Clone (Databricks)

A **shallow clone** creates a copy of a source Delta, Apache Parquet, or Apache Iceberg (foreign) table’s metadata and table definition, but references the source table’s data files rather than copying them. It provides a lightweight, inexpensive way to snapshot a table’s schema, properties, and history without duplicating the underlying storage. ^[create-table-clone-databricks-on-aws.md]

In contrast, a deep clone copies both the metadata and the data files, producing a fully independent table. Shallow clones are the default when using `CLONE` without specifying `DEEP CLONE`? No — the default is **deep clone** unless `SHALLOW CLONE` is explicitly stated. ^[create-table-clone-databricks-on-aws.md]

## Syntax

```sql
CREATE TABLE [IF NOT EXISTS] table_name
  SHALLOW CLONE source_table_name
  [TBLPROPERTIES clause]
  [LOCATION path]

[CREATE OR] REPLACE TABLE table_name
  SHALLOW CLONE source_table_name
  [TBLPROPERTIES clause]
  [LOCATION path]
```

^[create-table-clone-databricks-on-aws.md]

## Parameters

| Parameter | Description |
|-----------|-------------|
| `IF NOT EXISTS` | If specified, the statement is ignored when `table_name` already exists. |
| `[CREATE OR] REPLACE` | Creates the table if it does not exist, or replaces it if it does. Without `CREATE OR`, the target table must already exist. |
| `table_name` | The name of the target table. Must not include a temporal or options specification. Created in the current schema if unqualified. |
| `SHALLOW CLONE` | Creates a copy of the source table's definition, but references the source table's data files. |
| `source_table_name` | The name of the source table; may include a temporal or options specification. |
| `TBLPROPERTIES` | Optional user‑defined properties to set on the target. |
| `LOCATION path` | Optionally creates an external table at the provided storage path. |

^[create-table-clone-databricks-on-aws.md]

## Behavior

- **Metadata‑only copy:** The shallow clone contains the same schema, partitioning, table properties, and transaction history as the source, but reads data from the original files. ^[create-table-clone-databricks-on-aws.md]
- **Independent writes:** Any writes to the shallow clone (e.g., `INSERT`, `DELETE`, `MERGE`) create new files in the clone’s own storage location, leaving the source table unchanged.
- **Unity Catalog support:** Shallow clone is supported for Unity Catalog managed tables in Databricks SQL and Databricks Runtime 13.3 LTS and above. In Databricks Runtime 12.2 LTS and below, shallow clones are not available in Unity Catalog. ^[create-table-clone-databricks-on-aws.md]

## Limitations

- **Managed Iceberg tables** support only deep cloning; shallow cloning is not allowed. ^[create-table-clone-databricks-on-aws.md]
- **Streaming tables and materialized views** cannot be used as source or target tables for any `CLONE` operation, including shallow clone. ^[create-table-clone-databricks-on-aws.md]
- Shallow clones of foreign Iceberg tables follow the same rules as Delta shallow clones, but foreign Iceberg tables that are not fully managed by Databricks may have additional restrictions.

## Example

```sql
-- Shallow clone: copies metadata only, references source data files
CREATE TABLE target_catalog.target_schema.target_table
SHALLOW CLONE source_catalog.source_schema.source_table;
```

^[create-table-clone-databricks-on-aws.md]

## Related Concepts

- [Deep Clone (Databricks)](/concepts/deep-clone-databricks.md) — A complete, independent copy of both metadata and data.
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format that supports both shallow and deep cloning.
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer that manages shallow clone support for registered tables.
- [Materialized Views](/concepts/materialized-views-in-databricks.md) — A dependent object type that cannot be used with `CLONE`.
- Streaming Tables — Another dependent object type incompatible with cloning operations.

## Sources

- create-table-clone-databricks-on-aws.md

# Citations

1. [create-table-clone-databricks-on-aws.md](/references/create-table-clone-databricks-on-aws-49def2a6.md)
