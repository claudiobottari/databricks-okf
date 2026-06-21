---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 076eb0864d4b20300236e7f4e6123e97a1b6bb8acdcd78f710e37cef378f6637
  pageDirectory: concepts
  sources:
    - delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - table_all_void_columns-error-condition
    - TEC
    - TABLE_ALL_VOID_COLUMNS error condition
  citations:
    - file: delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
title: TABLE_ALL_VOID_COLUMNS error condition
description: A sub-error of DELTA_CANNOT_WRITE_EMPTY_SCHEMA where every column in the table schema is of VOID type
tags:
  - error-messages
  - delta-lake
  - schema-validation
timestamp: "2026-06-19T15:01:43.533Z"
---

# TABLE_ALL_VOID_COLUMNS Error Condition

**TABLE\_ALL\_VOID\_COLUMNS** is a specific sub-reason of the DELTA_CANNOT_WRITE_EMPTY_SCHEMA error|DELTA_CANNOT_WRITE_EMPTY_SCHEMA error condition. It occurs when a write operation is attempted against a Delta table whose schema contains only columns of type `VOID`. Because every column in the table has the `VOID` type, the schema is considered unsupported for writing. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Error Details

- **Error class:** `DELTA_CANNOT_WRITE_EMPTY_SCHEMA`
- **SQLSTATE:** `428GU` (Class 42 – Syntax error or access rule violation)
- **Reason:** `TABLE_ALL_VOID_COLUMNS`
- **Message:** "All columns in the table schema have VOID type."

## Cause

A `VOID` type column represents an absence of data (similar to `NULL` but at the type level). When every column in the schema is `VOID`, the Delta writer cannot determine a valid physical layout for the data. This typically arises from operations that inadvertently eliminate all non-void columns (e.g., a series of `ALTER TABLE ... DROP COLUMN` statements that remove all columns, or a schema inference that produces only void-typed columns from an empty or malformed source). ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Related Sub‑Reasons

The `DELTA_CANNOT_WRITE_EMPTY_SCHEMA` error class includes several similar conditions:

- STRUCT_ALL_VOID_FIELDS – A struct column where all fields have VOID type.
- STRUCT_NO_FIELDS – A struct column with no fields.
- TABLE_NO_COLUMNS – The table schema has no columns defined at all.

## Resolution

To resolve `TABLE_ALL_VOID_COLUMNS`, the table schema must contain at least one column with a non‑void data type. Depending on how the schema became void-only, consider the following approaches:

- Drop the Delta table and recreate it with a valid schema.
- If the table was inadvertently altered, use `ALTER TABLE ... ADD COLUMN` to reintroduce a non‑void column before writing.
- If the schema was inferred from an empty data source, ensure the source provides a well‑defined schema with concrete types.

## Related Concepts

- [Delta table](/concepts/delta-lake-table.md) – The storage format affected by this error.
- [VOID type](/concepts/void-type-in-delta-lake.md) – The data type that causes the schema to be considered empty.
- DELTA_CANNOT_WRITE_EMPTY_SCHEMA error|DELTA_CANNOT_WRITE_EMPTY_SCHEMA error condition – The parent error class.
- STRUCT_ALL_VOID_FIELDS error condition
- STRUCT_NO_FIELDS error condition
- TABLE_NO_COLUMNS error condition
- DELTA_CANNOT_WRITE_EMPTY_SCHEMA error|Delta write empty schema troubleshooting

## Sources

- delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md

# Citations

1. [delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md](/references/delta_cannot_write_empty_schema-error-condition-databricks-on-aws-78122c55.md)
