---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f75a07ecc852628173288c4e404f0f95507f65f12f549fed4e84e7caba28dc56
  pageDirectory: concepts
  sources:
    - delta_duplicate_columns_found-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sqlstate-42711-duplicate-column-error
    - S4(CE
  citations:
    - file: delta_duplicate_columns_found-error-condition-databricks-on-aws.md
title: SQLSTATE 42711 (duplicate column error)
description: The SQL standard error code 42711, classified under class 42 (syntax error or access rule violation), which maps to the Delta Lake duplicate column error condition.
tags:
  - sql-standard
  - error-codes
  - databricks
timestamp: "2026-06-18T15:19:09.187Z"
---

Here is a draft for the **SQLSTATE 42711 (duplicate column error)** wiki page.

---

## SQLSTATE 42711 (duplicate column error)

**SQLSTATE 42711** is a class 42 (syntax error or access rule violation) error code that indicates a duplicate column was found in a data definition or query operation. The error is raised when two or more columns with the same name are detected in a single context, such as during table creation, schema modification, data insertion, or query parsing.

## Error Message

The error message follows this pattern:

```
Found duplicate column(s): `<duplicateCols>`.
```

where `<duplicateCols>` lists the column names that appear more than once in the operation. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## Error Sub‑types

The error is further categorized by the operation during which the duplicate was detected:

- **ADDING_COLUMNS** – The duplicate was found while adding columns. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **CLUSTER_BY** – The duplicate was found in a `CLUSTER BY` clause. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **CONVERT_TO_DELTA** – The duplicate was found during conversion to [Delta Lake](/concepts/delta-lake.md). ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **DATA** – The duplicate was found in the data being saved. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **EXISTING_SCHEMA** – The duplicate was found in the existing table schema. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **METADATA** – The duplicate was found in the metadata update. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **PARTITION_COLUMNS** – The duplicate was found in the partition columns. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **PARTITION_SCHEMA** – The duplicate was found in the partition schema. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **READ_SCHEMA** – The duplicate was found in the schema of the data being read. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **REPLACING_COLUMNS** – The duplicate was found while replacing columns. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **SPECIFIED_COLUMNS** – The duplicate was found in the specified columns. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **TABLE_SCHEMA** – The duplicate was found in the table schema. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## Causes

A duplicate column error can arise from many scenarios:

- A `CREATE TABLE` statement lists the same column name twice.
- An `ALTER TABLE ADD COLUMNS` statement includes a column already present in the table.
- A `SELECT *` or explicit column list in a query produces duplicate aliases.
- A `CLUSTER BY` or `PARTITION BY` clause includes a column name more than once.
- The source data file contains duplicate column names in its schema.
- A metadata operation (e.g., renaming a column to an existing name) creates a conflict.

## Resolution

- **Review the schema definition** – Ensure column names are unique in the table or query definition.
- **Check the source data** – Verify that the input files (e.g., CSV, Parquet, JSON) do not contain duplicate column headers.
- **Use explicit column lists** – Avoid `SELECT *` when the schema is unknown or when joining tables with overlapping column names.
- **Rename or drop duplicate columns** – Use `ALTER TABLE ... RENAME COLUMN` or `DROP COLUMN` to resolve duplicates in an existing table.
- **Consult error sub‑type** – The sub‑type (e.g., `ADDING_COLUMNS`, `PARTITION_COLUMNS`) indicates the operation that triggered the error, helping narrow the search for the duplicate.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) schema enforcement
- Schema evolution
- SQLSTATE reference
- Class 42 — Syntax error or access rule violation
- Data definition language (DDL)

## Sources

- delta_duplicate_columns_found-error-condition-databricks-on-aws.md

---

# Citations

1. [delta_duplicate_columns_found-error-condition-databricks-on-aws.md](/references/delta_duplicate_columns_found-error-condition-databricks-on-aws-42950ac1.md)
