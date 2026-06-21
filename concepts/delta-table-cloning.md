---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d9cd1cdf80043a683fffad6160b9a4a13c2a51a4db59ff5cee73942b88924048
  pageDirectory: concepts
  sources:
    - create-table-clone-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-table-cloning
    - DTC
    - Delta Lake Cloning
    - Delta Lake Table Cloning
    - Delta Lake cloning
    - Delta Lake table cloning
    - Delta table clone
    - Delta Cloning
    - Delta Lake DEEP CLONE vs SHALLOW CLONE
    - Delta Lake Deep Clone
    - Table Cloning
    - Table cloning
  citations:
    - file: create-table-clone-databricks-on-aws.md
title: Delta Table Cloning
description: The ability to create deep or shallow copies of Delta tables, copying data and/or metadata to a target location for purposes like archiving, ML workflows, and data migration.
tags:
  - delta-lake
  - cloning
  - data-migration
timestamp: "2026-06-18T14:56:19.154Z"
---

# Delta Table Cloning

**Delta Table Cloning** is a feature in Databricks that creates a copy of a source table — either a [Delta Table](/concepts/delta-lake-table.md), a [managed Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) table, or an Apache Parquet table — at a specific version. Cloning can be performed as either a **deep clone** or a **shallow clone**, each with distinct implications for data independence, storage cost, and performance. ^[create-table-clone-databricks-on-aws.md]

Deep clones copy both the table's metadata and its underlying data to a fully independent target, while shallow clones copy only the table's definition and metadata, retaining a reference to the source data files. The choice between them determines how the target table behaves when the source table is modified or deleted. ^[create-table-clone-databricks-on-aws.md]

## Syntax

```sql
-- Deep clone (default)
CREATE TABLE target_catalog.target_schema.target_table
  DEEP CLONE source_catalog.source_schema.source_table;

-- Shallow clone
CREATE TABLE target_catalog.target_schema.target_table
  SHALLOW CLONE source_catalog.source_schema.source_table;
```

Both forms support the `IF NOT EXISTS`, `[CREATE OR] REPLACE`, `TBLPROPERTIES`, and `LOCATION` clauses. ^[create-table-clone-databricks-on-aws.md]

## Parameters

- **IF NOT EXISTS** — If specified, the statement is ignored when `table_name` already exists. ^[create-table-clone-databricks-on-aws.md]
- **\[CREATE OR\] REPLACE** — If `CREATE OR` is specified, the table is replaced if it exists and newly created if it does not. Without `CREATE OR`, `table_name` must exist. ^[create-table-clone-databricks-on-aws.md]
- **table_name** — The name of the target table. Must not include a temporal specification or options specification. If unqualified, the table is created in the current schema. ^[create-table-clone-databricks-on-aws.md]
- **SHALLOW CLONE** or **DEEP CLONE** — Determines whether the target table references the source's data files (shallow) or contains an independent copy (deep). Deep clone is the default. ^[create-table-clone-databricks-on-aws.md]
- **source_table_name** — The name of the table to be cloned. May include a temporal specification or options specification. ^[create-table-clone-databricks-on-aws.md]
- **TBLPROPERTIES** — Optionally sets one or more user-defined properties on the target table. ^[create-table-clone-databricks-on-aws.md]
- **LOCATION path** — Optionally creates an external table at the specified path. If `table_name` itself is a path, the operation fails. `path` must be a STRING literal. ^[create-table-clone-databricks-on-aws.md]

## Supported Source Formats

- **Delta tables** — Both deep and shallow cloning are supported. ^[create-table-clone-databricks-on-aws.md]
- **Apache Parquet tables** — Both deep and shallow cloning are supported. ^[create-table-clone-databricks-on-aws.md]
- **Foreign (unmanaged) Apache Iceberg tables** — Both deep and shallow cloning are supported. ^[create-table-clone-databricks-on-aws.md]
- **Managed Iceberg tables** — Only deep cloning is supported. You cannot change the table format during cloning. ^[create-table-clone-databricks-on-aws.md]

## Deep Clone

A deep clone makes a **complete, independent copy** of the source table, including all data files and metadata. The target table has no dependency on the source table after creation; modifications to the source do not affect the target. Deep clones are the default behavior. ^[create-table-clone-databricks-on-aws.md]

```sql
-- Deep clone: copies data and metadata
CREATE TABLE target_catalog.target_schema.target_table
  DEEP CLONE source_catalog.source_schema.source_table;
```

## Shallow Clone

A shallow clone copies only the **table definition and metadata** from the source, while the target table's data files remain references to the source table's files. This makes shallow clones fast and storage-efficient — no data is physically copied at creation time. ^[create-table-clone-databricks-on-aws.md]

```sql
-- Shallow clone: copies metadata only, references source data files
CREATE TABLE target_catalog.target_schema.target_table
  SHALLOW CLONE source_catalog.source_schema.source_table;
```

### Unity Catalog Support

In Databricks SQL and Databricks Runtime 13.3 LTS and above, shallow clone is supported with [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md). In Databricks Runtime 12.2 LTS and below, shallow clones for Unity Catalog managed tables are not supported. ^[create-table-clone-databricks-on-aws.md]

## Use Cases

- **Data archiving** — Deep clones create independent snapshots for long-term storage. ^[create-table-clone-databricks-on-aws.md]
- **Machine learning workflows** — Shallow clones enable rapid experimentation without duplicating data. See Clone a table on Databricks for more examples. ^[create-table-clone-databricks-on-aws.md]
- **Incremental migration** — Use shallow or deep clones to incrementally migrate Parquet and Iceberg tables to Delta Lake. See [Incrementally clone Parquet and Apache Iceberg tables to Delta Lake](/concepts/incremental-clone-of-parquet-and-iceberg-to-delta-lake.md). ^[create-table-clone-databricks-on-aws.md]
- **Environment sandboxing** — Shallow clones provide a read-only view of production data for development and QA. ^[create-table-clone-databricks-on-aws.md]

## Limitations

- Streaming tables and [materialized views](/concepts/materialized-views-in-databricks.md) are not supported as source or target tables for `CLONE`. ^[create-table-clone-databricks-on-aws.md]
- Managed Iceberg tables support only deep cloning; shallow cloning is not supported. ^[create-table-clone-databricks-on-aws.md]
- Shallow clones in Unity Catalog are not supported in Databricks Runtime 12.2 LTS and below. ^[create-table-clone-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md)
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md)
- Apache Parquet
- Deep clone vs shallow clone
- [Incrementally clone Parquet and Apache Iceberg tables to Delta Lake](/concepts/incremental-clone-of-parquet-and-iceberg-to-delta-lake.md)
- Clone a table on Databricks
- [Clone a managed Iceberg table](/concepts/managed-iceberg-table-cloning.md)

## Sources

- create-table-clone-databricks-on-aws.md

# Citations

1. [create-table-clone-databricks-on-aws.md](/references/create-table-clone-databricks-on-aws-49def2a6.md)
