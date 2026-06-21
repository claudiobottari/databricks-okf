---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c67def6985f2c699c1505ffa61dcc9e1c18b3f2cf8224716bcdb33f0b8b3eddb
  pageDirectory: concepts
  sources:
    - delta_duplicate_columns_found-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_duplicate_columns_found-error-condition
    - DEC
    - DELTA_DUPLICATE_COLUMNS_FOUND error condition
  citations:
    - file: delta_duplicate_columns_found-error-condition-databricks-on-aws.md
title: DELTA_DUPLICATE_COLUMNS_FOUND error condition
description: A Delta Lake error (SQLSTATE 42711) raised when duplicate column names are detected during various table operations such as schema changes, data writes, or metadata updates.
tags:
  - delta-lake
  - error-handling
  - databricks
timestamp: "2026-06-18T11:53:12.139Z"
---

#DELTA_DUPLICATE_COLUMNS_FOUND error condition

The **`DELTA_DUPLICATE_COLUMNS_FOUND`** error occurs when Delta Lake detects duplicate column names during an operation that reads, writes, or modifies a Delta table. The error indicates that a set of column names specified in the operation contains repeats, which is not allowed because Delta tables require unique column names. The error belongs to SQLSTATE class `42711` (syntax error or access rule violation). ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## Error Message

The general error message is:

```
Found duplicate column(s): `<duplicateCols>`.
```

The `<duplicateCols>` placeholder lists the column names that appear more than once. The message is accompanied by a subcategory identifier that pinpoints where the duplication was detected. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## Subcategories

Each subcategory corresponds to a specific operation context in which the duplicate columns were found. The following table lists all documented subcategories:

| Subcategory | Description |
|-------------|-------------|
| `ADDING_COLUMNS` | The duplicate was found while adding columns to an existing table. |
| `CLUSTER_BY` | The duplicate was found in the `CLUSTER BY` clause. |
| `CONVERT_TO_DELTA` | The duplicate was found during conversion to Delta format. |
| `DATA` | The duplicate was found in the data being saved. |
| `EXISTING_SCHEMA` | The duplicate was found in the existing table schema. |
| `PARTITION_COLUMNS` | The duplicate was found in the partition columns specification. |
| `PARTITION_SCHEMA` | The duplicate was found in the partition schema. |
| `READ_SCHEMA` | The duplicate was found in the schema of the data being read. |
| `REPLACING_COLUMNS` | The duplicate was found while replacing columns. |
| `SPECIFIED_COLUMNS` | The duplicate was found in the explicitly specified columns. |
| `TABLE_SCHEMA` | The duplicate was found in the table schema. |

^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

The subcategory `EXISTING_SCHEMA` also covers cases where the duplicate was found in the metadata update. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## Common Causes

Duplicate column names can arise from several scenarios:

- **Schema evolution operations** such as `ALTER TABLE ADD COLUMNS` or `REPLACE COLUMNS` when the new column list accidentally repeats a column name.
- **Writing data** where the source schema contains duplicate columns (for example, a SELECT statement that aliases two columns to the same name).
- **Partitioning** when the partition column list includes the same column more than once.
- **Data ingestion** during `CONVERT TO DELTA` if the source has duplicate column names.
- **Reading data** with a user-specified read schema that contains duplicates.
- **CLUSTER BY** clause when columns are repeated.

## Resolution

To resolve the error, identify the duplicate column names from the error message and remove or rename the repeated entries. Check the operation context (the subcategory) to determine exactly where the duplication was introduced. For example, if the subcategory is `DATA`, inspect the output schema of the query or the data frame being written. If it is `PARTITION_COLUMNS`, ensure each partition column is listed only once.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that enforces unique column constraints
- Schema evolution — Operations that modify the table schema and may introduce duplicates
- Partition columns — Columns used to partition a Delta table
- CLUSTER BY — A clause that defines table clustering
- [CONVERT TO DELTA](/concepts/convert-to-delta.md) — The operation that transforms Parquet or other formats into Delta
- SQLSTATE — Standard error code system; class 42 indicates syntax or access rule violations

## Sources

- delta_duplicate_columns_found-error-condition-databricks-on-aws.md

# Citations

1. [delta_duplicate_columns_found-error-condition-databricks-on-aws.md](/references/delta_duplicate_columns_found-error-condition-databricks-on-aws-42950ac1.md)
