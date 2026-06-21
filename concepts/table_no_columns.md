---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c5234e811241e8cbcba0c0b468337701a597edbff316d4f3ee7270f416d2cdd1
  pageDirectory: concepts
  sources:
    - delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - table_no_columns
    - TABLE_NO_COLUMNS
    - table_no_columns-error-condition
    - TEC
    - TABLE_NO_COLUMNS error condition
  citations:
    - file: delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
title: TABLE_NO_COLUMNS
description: A sub-reason for DELTA_CANNOT_WRITE_EMPTY_SCHEMA where the table schema has no columns defined at all.
tags:
  - delta-lake
  - error-messages
  - schema
timestamp: "2026-06-19T18:22:06.432Z"
---

# TABLE_NO_COLUMNS

**TABLE_NO_COLUMNS** is a specific sub-reason of the DELTA_CANNOT_WRITE_EMPTY_SCHEMA error class in Delta Lake. It occurs when a user attempts to write data to a Delta table whose schema has no columns defined. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Error Context

The error message reads: "The table schema has no columns defined." This condition corresponds to SQLSTATE `428GU`. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Common Causes

- An empty schema was explicitly provided during a write operation (e.g., `INSERT INTO` or `CREATE TABLE ... AS SELECT` with no columns).
- An upstream transformation or schema evolution resulted in a table schema containing zero columns.
- A metadata-only operation stripped all column definitions from the schema without dropping the table.
- A table was created with only [VOID type](/concepts/void-type-in-delta-lake.md) columns, which Delta Lake treats as having no valid columns.

The error is a safeguard: Delta Lake refuses to write data to a table that lacks any column definition because such a write would produce an unreadable dataset.

## Related Sub-Errors

TABLE_NO_COLUMNS is one of four sub-errors under the `DELTA_CANNOT_WRITE_EMPTY_SCHEMA` error class. The other related sub-errors include:

- STRUCT_ALL_VOID_FIELDS — Occurs when a struct column contains only VOID type fields.
- STRUCT_NO_FIELDS — Occurs when a struct column has no fields defined.
- TABLE_ALL_VOID_COLUMNS — Occurs when all columns in the table schema have VOID type.

## How to Resolve

1. **Define at least one column** in the table schema before writing. If creating a new table, use `CREATE TABLE ... (col_name data_type, ...)` or write a DataFrame that has a non-empty schema.
2. **Drop and recreate** the existing Delta table with a proper schema if it currently has no columns and should not exist.
3. **Review schema evolution** settings. If automatic schema evolution is enabled, ensure that the incoming data contains valid columns. Without columns, writes are blocked.
4. **Check for VOID type columns** — If all columns have been assigned VOID type, redefine them with appropriate data types.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The open-format storage layer that enforces schema constraints.
- Schema enforcement — The Delta Lake feature that prevents writes with mismatched schemas.
- Schema evolution — The mechanism for safely updating table schemas over time.
- [SQLSTATE 428GU](/concepts/sqlstate-428gu.md) — The database-standard SQL state code mapped to this error class.

## Sources

- delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md

# Citations

1. [delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md](/references/delta_cannot_write_empty_schema-error-condition-databricks-on-aws-78122c55.md)
