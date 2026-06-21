---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea697bb6e5c492054427ad81668b602b8937c4c8fdb31f1c3cf1215451739a57
  pageDirectory: concepts
  sources:
    - delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_cannot_write_empty_schema-error
    - DELTA_CANNOT_WRITE_EMPTY_SCHEMA error condition
    - Delta write empty schema troubleshooting
  citations:
    - file: delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
title: DELTA_CANNOT_WRITE_EMPTY_SCHEMA error
description: A Delta Lake error raised when a table schema is empty or consists entirely of unsupported VOID-type columns or empty structs, preventing writes.
tags:
  - delta-lake
  - error-message
  - databricks
timestamp: "2026-06-18T15:16:47.577Z"
---

# DELTA_CANNOT_WRITE_EMPTY_SCHEMA Error

The **DELTA_CANNOT_WRITE_EMPTY_SCHEMA** error occurs when an attempt to write to a [Delta table](/concepts/delta-lake.md) fails because the table schema is either empty or contains unsupported structural elements. This error has SQLSTATE code **428GU** and belongs to the syntax or access rule violation class. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Reasons

The error message includes one of the following sub‑reasons, which identify the specific schema issue:

### STRUCT_ALL_VOID_FIELDS

The column `<columnPath>` is a struct where all fields have VOID type. This means every subfield of the struct is defined as the empty `VOID` data type, which is not supported for writing. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

### STRUCT_NO_FIELDS

The column `<columnPath>` is a struct with no fields. A struct must contain at least one field to be written to a Delta table. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

### TABLE_ALL_VOID_COLUMNS

All columns in the table schema have VOID type. When no column has a concrete data type, the table cannot be written. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

### TABLE_NO_COLUMNS

The table schema has no columns defined. A Delta table must have at least one column to be writable. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Troubleshooting

Review the schema definition of the target Delta table. Ensure:

- Each column has a non‑void, supported data type.
- Struct types contain at least one field.
- Struct fields each have a valid type (not `VOID`).
- The table schema is not completely empty.

If the table was created with an empty schema or with columns that resolved to `VOID`, redefine the schema with appropriate types before writing data.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage format that enforces the schema constraint.
- Schema — The column and type definition for a table.
- Struct type — A complex data type composed of named fields.
- [Void type](/concepts/void-type-in-delta-lake.md) — A placeholder type that is not supported for data writing.
- SQLSTATE — Standard error code classification used by SQL engines.

## Sources

- delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md

# Citations

1. [delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md](/references/delta_cannot_write_empty_schema-error-condition-databricks-on-aws-78122c55.md)
