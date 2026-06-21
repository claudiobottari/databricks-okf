---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fcc1bfa27b2e68423d783f4fee89d41b235080302ea14252c2f7435e3b1bd4dc
  pageDirectory: concepts
  sources:
    - create-table-clone-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - source-table-types-for-clone
    - STTFC
  citations:
    - file: create-table-clone-databricks-on-aws.md
title: Source Table Types for CLONE
description: CLONE supports Delta, Parquet, Foreign Iceberg, and Managed Iceberg tables as source tables, each with different cloning capabilities.
tags:
  - source
  - compatibility
  - delta-lake
  - iceberg
  - parquet
timestamp: "2026-06-19T18:02:37.139Z"
---

# Source Table Types for CLONE

**Source Table Types for CLONE** refers to the supported table formats that can be used as the source of a `CREATE TABLE CLONE` operation on Databricks. The `CLONE` command creates a copy of a source table at a specific version, and the available clone behavior — deep or shallow — depends on the source table's format. ^[create-table-clone-databricks-on-aws.md]

## Supported Source Table Types

### Delta Lake Tables

Delta Lake tables support both deep and shallow cloning. A deep clone creates a complete, independent copy of the source table, including all data files. A shallow clone copies only the table's metadata and references the source table's data files without copying them. ^[create-table-clone-databricks-on-aws.md]

### Apache Parquet Tables

Parquet tables support both deep and shallow cloning, following the same behavior as Delta Lake tables. ^[create-table-clone-databricks-on-aws.md]

### Apache Iceberg Tables

The cloning behavior for Iceberg tables depends on whether the table is managed or foreign:

- **Managed Iceberg tables** support only deep cloning. Shallow cloning is not supported for managed Iceberg tables. Additionally, you cannot change the table format during cloning. ^[create-table-clone-databricks-on-aws.md]
- **Foreign Iceberg tables** support both deep and shallow cloning. ^[create-table-clone-databricks-on-aws.md]

## Unsupported Source Table Types

Streaming tables and materialized views are not supported as source tables for the `CLONE` operation. ^[create-table-clone-databricks-on-aws.md]

## Summary Table

| Source Table Type | Deep Clone | Shallow Clone |
|---|---|---|
| Delta Lake | Supported | Supported |
| Apache Parquet | Supported | Supported |
| Managed Iceberg | Supported | Not supported |
| Foreign Iceberg | Supported | Supported |
| Streaming tables | Not supported | Not supported |
| Materialized views | Not supported | Not supported |

## Related Concepts

- [Deep Clone](/concepts/deep-clone.md) — Creates a complete, independent copy of the source table.
- [Shallow Clone](/concepts/shallow-clone.md) — Creates a metadata-only copy that references source data files.
- [CREATE TABLE CLONE](/concepts/create-table-clone-syntax.md) — The SQL command for cloning tables.
- [Delta Lake](/concepts/delta-lake.md) — The default table format on Databricks.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — An open table format supported for cloning.
- [Managed Tables vs External Tables](/concepts/managed-vs-external-tables-in-unity-catalog.md) — Table management types that affect clone behavior.
- [Unity Catalog](/concepts/unity-catalog.md) — The catalog system that supports shallow clones for managed tables.

## Sources

- create-table-clone-databricks-on-aws.md

# Citations

1. [create-table-clone-databricks-on-aws.md](/references/create-table-clone-databricks-on-aws-49def2a6.md)
