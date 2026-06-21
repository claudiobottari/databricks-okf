---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8d65d9ec41f3a92865322600c4b1930797d0afc523edc4a668b0be7ac35f11ff
  pageDirectory: concepts
  sources:
    - create-table-clone-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - create-or-replace-table-clone
    - REPLACE TABLE CLONE OR CREATE
    - CORTC
    - CREATE OR REPLACE TABLE
    - Drop or replace a table
  citations:
    - file: create-table-clone-databricks-on-aws.md
title: CREATE OR REPLACE TABLE CLONE
description: A DDL syntax variant that creates a new cloned table or replaces an existing one at the target location.
tags:
  - delta-lake
  - sql
  - ddl
timestamp: "2026-06-18T14:55:47.575Z"
---

# CREATE OR REPLACE TABLE CLONE

**CREATE OR REPLACE TABLE CLONE** is a variant of the `CREATE TABLE CLONE` command in Databricks that creates a new table as a copy of an existing table — or replaces an existing table with a cloned copy if it already exists. It supports both shallow and deep cloning for Delta, managed Apache Iceberg, and Apache Parquet tables. ^[create-table-clone-databricks-on-aws.md]

## Syntax

```
CREATE OR REPLACE TABLE table_name
  [SHALLOW | DEEP] CLONE source_table_name
  [TBLPROPERTIES clause]
  [LOCATION path]
```

The `CREATE OR` clause allows the command to either create the table if it does not exist or replace it if it does. Without `CREATE OR`, the target table must already exist (when using `REPLACE TABLE` alone). ^[create-table-clone-databricks-on-aws.md]

## Parameters

| Parameter | Description |
|-----------|-------------|
| `table_name` | The name of the table to be created or replaced. The name must not include a temporal specification or options specification. If the name is not qualified, the table is created in the current schema. ^[create-table-clone-databricks-on-aws.md] |
| `SHALLOW CLONE` / `DEEP CLONE` | `SHALLOW CLONE` copies only the source table’s metadata; it references the source table’s data files. `DEEP CLONE` (default) makes a complete, independent copy of the data and metadata. Managed Iceberg tables support only deep cloning. ^[create-table-clone-databricks-on-aws.md] |
| `source_table_name` | The name of the table to be cloned. May include a temporal or options specification. ^[create-table-clone-databricks-on-aws.md] |
| `TBLPROPERTIES clause` | Optionally sets one or more user-defined properties on the target table. ^[create-table-clone-databricks-on-aws.md] |
| `LOCATION path` | Optionally creates an external table with the given storage path. The path must be a STRING literal. If `table_name` itself is a path, the operation fails. ^[create-table-clone-databricks-on-aws.md] |

## Examples

### Deep clone (default)

```sql
CREATE OR REPLACE TABLE target_catalog.target_schema.target_table
DEEP CLONE source_catalog.source_schema.source_table;
```

Copies all data and metadata from the source to the target. If the target table already exists, it is replaced. ^[create-table-clone-databricks-on-aws.md]

### Shallow clone

```sql
CREATE OR REPLACE TABLE target_catalog.target_schema.target_table
SHALLOW CLONE source_catalog.source_schema.source_table;
```

Creates or replaces the target table with a metadata-only copy that references the source’s data files. ^[create-table-clone-databricks-on-aws.md]

### Deep clone a managed Iceberg table

```sql
CREATE OR REPLACE TABLE target_catalog.target_schema.target_table
DEEP CLONE source_catalog.source_schema.source_table;
```

Managed Iceberg tables support only deep cloning; shallow clone is not allowed. ^[create-table-clone-databricks-on-aws.md]

## Comparison of Shallow and Deep Clone

- **Deep clone**: A fully independent copy of the source table’s data and metadata. Modifications to the clone do not affect the source, and vice versa. ^[create-table-clone-databricks-on-aws.md]
- **Shallow clone**: Copies only the table definition and references the source’s data files. The clone shares the underlying data with the source until writes occur (copy-on-write). Recommended for fast, lightweight copies used for testing or development. ^[create-table-clone-databricks-on-aws.md]

Both shallow and deep clones can be used with Delta, Parquet, and foreign Iceberg tables. ^[create-table-clone-databricks-on-aws.md]

## Limitations

- Delta Streaming tables and materialized views cannot be used as source or target for `CLONE`. ^[create-table-clone-databricks-on-aws.md]
- In Databricks Runtime 12.2 LTS and earlier, shallow clones are not supported in Unity Catalog. Unity Catalog support for shallow clones was added in Databricks Runtime 13.3 LTS and above. ^[create-table-clone-databricks-on-aws.md]
- The `table_name` parameter must not include a temporal specification or options specification. ^[create-table-clone-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The format for which cloning is primarily designed.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that enforces clone permissions and supports shallow cloning from Databricks Runtime 13.3 LTS onward.
- [Deep Clone](/concepts/deep-clone.md) — A complete, independent copy of a table’s data and metadata.
- [Shallow Clone](/concepts/shallow-clone.md) — A metadata-only copy that references the source’s data files.
- Clone a Table on Databricks — General guide on cloning operations, including use cases for archiving and ML workflows.
- [CREATE TABLE CLONE](/concepts/create-table-clone-syntax.md) — The base syntax without the `CREATE OR REPLACE` variant.

## Sources

- create-table-clone-databricks-on-aws.md

# Citations

1. [create-table-clone-databricks-on-aws.md](/references/create-table-clone-databricks-on-aws-49def2a6.md)
