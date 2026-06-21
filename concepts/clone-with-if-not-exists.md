---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fc5cd21f0d6984b6de6bd6be22e67cd565de34b918a945e69b63da85e3a74649
  pageDirectory: concepts
  sources:
    - create-table-clone-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - clone-with-if-not-exists
    - CWINE
  citations:
    - file: create-table-clone-databricks-on-aws.md
title: CLONE with IF NOT EXISTS
description: A SQL syntax modifier for CLONE that causes the operation to be silently ignored if the target table already exists.
tags:
  - databricks
  - sql-syntax
  - cloning
timestamp: "2026-06-19T14:39:04.689Z"
---

<!-- TODO: Improve summary to be more specific about CLONE context -->

# CLONE with IF NOT EXISTS

**CLONE with IF NOT EXISTS** is a clause in the `CREATE TABLE ... CLONE` statement that makes the operation idempotent: if the target table already exists, the statement is silently ignored rather than failing with an error. This is useful for scripts and workflows that should not fail when the target table has already been created by a previous run.

## Syntax

The `IF NOT EXISTS` clause can be placed after `CREATE TABLE` in any `CLONE` statement:

```sql
CREATE TABLE [IF NOT EXISTS] table_name
  [SHALLOW | DEEP] CLONE source_table_name
  [TBLPROPERTIES clause]
  [LOCATION path]
```

^[create-table-clone-databricks-on-aws.md]

## Parameters

- **`IF NOT EXISTS`** – If specified, the statement is ignored when `table_name` already exists. Without this clause, the statement fails if the target table exists (unless `REPLACE` is used). ^[create-table-clone-databricks-on-aws.md]

- **`table_name`** – The name of the table to create. Must not already exist unless `IF NOT EXISTS` or `REPLACE` is specified. ^[create-table-clone-databricks-on-aws.md]

## Behavior

The `IF NOT EXISTS` clause applies to both [Deep Clone](/concepts/deep-clone.md) and [Shallow Clone](/concepts/shallow-clone.md) operations. It ensures that the statement completes without error when the target table already exists, regardless of its content or structure. No validation of the existing table against the source is performed — the statement simply does nothing. ^[create-table-clone-databricks-on-aws.md]

## Usage Notes

- `IF NOT EXISTS` is mutually exclusive with `[[CREATE OR] REPLACE TABLE]`. Use `REPLACE` if you want to overwrite the existing table with a fresh clone.
- The clause is supported for [Delta Lake](/concepts/delta-lake.md) tables, managed [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) tables (deep clone only), and Parquet tables, subject to the same limitations as the base `CLONE` operation (e.g., streaming tables and materialized views cannot be source or target).
- In Databricks SQL and Databricks Runtime 13.3 LTS and above, shallow clone with Unity Catalog managed tables is supported; for earlier versions, shallow clone is not available in Unity Catalog.

## Examples

The following example creates a deep clone only if the target table does not already exist:

```sql
CREATE TABLE IF NOT EXISTS prod.user_backup
  DEEP CLONE source.sales.users;
```

If `prod.user_backup` exists, the statement is ignored. ^[create-table-clone-databricks-on-aws.md] (Syntax derived from source; example constructed to illustrate behavior.)

## Related Concepts

- [CREATE TABLE CLONE](/concepts/create-table-clone-syntax.md) — Full statement reference
- [Deep Clone](/concepts/deep-clone.md) — Copies data and metadata independently
- [Shallow Clone](/concepts/shallow-clone.md) — Copies only metadata, references source data files
- REPLACE TABLE — Overwrites an existing table unconditionally
- IF NOT EXISTS (general) — Idempotent creation pattern in SQL

## Sources

- create-table-clone-databricks-on-aws.md

# Citations

1. [create-table-clone-databricks-on-aws.md](/references/create-table-clone-databricks-on-aws-49def2a6.md)
