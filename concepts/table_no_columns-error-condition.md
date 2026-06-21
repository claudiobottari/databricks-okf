---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 287e9ab2254488080373e87f6e8e14ffae1411509e97f57a5814041417f38eaf
  pageDirectory: concepts
  sources:
    - delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - table_no_columns-error-condition
    - TEC
    - TABLE_NO_COLUMNS error condition
  citations:
    - file: delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
title: TABLE_NO_COLUMNS error condition
description: A sub-error of DELTA_CANNOT_WRITE_EMPTY_SCHEMA where the table schema has no columns defined at all
tags:
  - error-messages
  - delta-lake
  - schema-validation
timestamp: "2026-06-19T15:01:35.639Z"
---

# TABLE_NO_COLUMNS error condition

The **TABLE_NO_COLUMNS** error condition is a sub‑reason of the DELTA_CANNOT_WRITE_EMPTY_SCHEMA error|DELTA_CANNOT_WRITE_EMPTY_SCHEMA error condition class. It occurs when an operation attempts to write to a [Delta table](/concepts/delta-lake-table.md) whose schema has no columns defined. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Error Details

- **Error class:** `DELTA_CANNOT_WRITE_EMPTY_SCHEMA`
- **SQLSTATE:** `428GU`
- **Reason:** `TABLE_NO_COLUMNS`
- **Message:** "The table schema has no columns defined." ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

The Delta table is not writable because the schema is unsupported. The `TABLE_NO_COLUMNS` reason indicates that the table schema is completely empty – no columns exist. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Related Sub‑Reasons

The `DELTA_CANNOT_WRITE_EMPTY_SCHEMA` class includes several other sub‑reasons that prevent writing when parts of the schema are empty or void:

- STRUCT_ALL_VOID_FIELDS – a struct column where all fields have VOID type.
- STRUCT_NO_FIELDS – a struct column with no fields.
- TABLE_ALL_VOID_COLUMNS – all columns in the table schema have VOID type.
- **TABLE_NO_COLUMNS** – the table schema has no columns defined.

## Related Concepts

- [Delta table](/concepts/delta-lake-table.md) – the storage format affected by this error.
- Schema – the column structure of a Delta table.
- DELTA_CANNOT_WRITE_EMPTY_SCHEMA error|DELTA_CANNOT_WRITE_EMPTY_SCHEMA error condition – the parent error class.

## Sources

- delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md

# Citations

1. [delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md](/references/delta_cannot_write_empty_schema-error-condition-databricks-on-aws-78122c55.md)
