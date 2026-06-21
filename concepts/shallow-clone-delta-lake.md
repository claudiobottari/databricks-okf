---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 70a86a1a0dcfb5f07298ce8463e965e487bd655439f189fae925389e5d179a0b
  pageDirectory: concepts
  sources:
    - create-table-clone-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - shallow-clone-delta-lake
    - SC(L
    - Shallow clone vs. deep clone
  citations:
    - file: create-table-clone-databricks-on-aws.md
title: Shallow Clone (Delta Lake)
description: A metadata-only copy of a source Delta, Parquet, or Foreign Iceberg table that references the source's data files without copying them.
tags:
  - delta-lake
  - cloning
  - data-management
timestamp: "2026-06-19T18:02:32.092Z"
---

# Shallow Clone (Delta Lake)

A **shallow clone** is a type of table clone that copies only the source table's metadata (definition) while pointing to the source table's existing data files. No data is physically copied, making the operation fast and storage‑efficient. It is supported for Delta, Parquet, and Foreign Iceberg tables. ^[create-table-clone-databricks-on-aws.md]

Shallow clones are created using the `CREATE TABLE ... SHALLOW CLONE` SQL statement. The resulting clone is a full‑fledged table that can be queried and written to independently; however, because the clone references the source's data files, changes made to the underlying data through either the source or the clone may affect the other if they share the same files. (Deep clones, in contrast, produce a completely independent copy of the data.) ^[create-table-clone-databricks-on-aws.md]

## Syntax

```sql
CREATE TABLE [IF NOT EXISTS] table_name
  SHALLOW CLONE source_table_name
  [TBLPROPERTIES clause] [LOCATION path]
```

### Parameters

- **table_name** – The name of the target table. Must not already exist unless `IF NOT EXISTS` or `REPLACE` is specified.
- **source_table_name** – The name of the source table to clone. May include temporal or options specifications.
- **TBLPROPERTIES** – Optional user‑defined table properties.
- **LOCATION path** – Optional path to store the clone’s metadata (if an external table is desired). If omitted, the clone is created as a managed table in the current schema.

The `REPLACE` variant (`CREATE OR REPLACE TABLE ... SHALLOW CLONE`) replaces an existing table or creates a new one if it does not exist.

## Supported Table Formats

| Source Table Type | Shallow Clone Supported | Notes |
|-------------------|-------------------------|-------|
| Delta Lake        | Yes                     | Default behavior with `SHALLOW CLONE` keyword |
| Apache Parquet    | Yes                     | Cloned to Delta Lake format |
| Foreign Iceberg   | Yes                     | Cloned to Delta Lake format |
| Managed Iceberg   | **No**                  | Only deep clone is allowed |

^[create-table-clone-databricks-on-aws.md]

## Unity Catalog Support

Shallow clones of Unity Catalog managed tables are supported in **Databricks SQL** and **Databricks Runtime 13.3 LTS and above**. In Databricks Runtime 12.2 LTS and below, shallow clones are not supported for Unity Catalog tables. ^[create-table-clone-databricks-on-aws.md]

## Limitations

- Streaming tables and materialized views cannot be used as source or target for `CLONE` operations.
- Shallow clones are not supported for managed Iceberg tables.
- The target table name must be a simple identifier, not a path.
- When using `LOCATION`, the target becomes an external table.

## Best Use Cases

Because shallow clones do not duplicate data, they are useful for:
- Creating a lightweight copy of a production table for development or testing.
- Enabling incremental data migrations where metadata is shared but data remains in the source.
- Performing schema evolution experiments without duplicating large datasets.

For full details on deep and shallow clone behavior, see Clone Operations on Databricks.

## Sources

- create-table-clone-databricks-on-aws.md

## Related Concepts

- [Deep Clone (Delta Lake)](/concepts/deep-clone-delta-lake.md)
- [Delta Lake](/concepts/delta-lake.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [CREATE TABLE CLONE](/concepts/create-table-clone-syntax.md)
- Managed Iceberg Tables on Databricks
- [Incremental Cloning of Parquet and Iceberg Tables](/concepts/incremental-cloning-of-parquet-and-iceberg-to-delta-lake.md)

# Citations

1. [create-table-clone-databricks-on-aws.md](/references/create-table-clone-databricks-on-aws-49def2a6.md)
