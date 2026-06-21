---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8efbbe2bb3e43bf8599e6d7eb7d5d241b4fc7ad0df008b33de2b3ac25b765920
  pageDirectory: concepts
  sources:
    - delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_cannot_write_empty_schema-error-class
    - DEC
  citations:
    - file: delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
title: DELTA_CANNOT_WRITE_EMPTY_SCHEMA error class
description: A Databricks Delta Lake error raised when a table cannot be written because its schema is empty or composed entirely of VOID-type columns
tags:
  - error-messages
  - delta-lake
  - databricks
timestamp: "2026-06-19T15:01:53.618Z"
---

# DELTA_CANNOT_WRITE_EMPTY_SCHEMA error class

**DELTA_CANNOT_WRITE_EMPTY_SCHEMA** is an error class in Databricks that occurs when attempting to write to a Delta table whose schema is considered empty or unsupported. The error is associated with SQLSTATE 428GU, which falls under class 42 (Syntax Error or Access Rule Violation). ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Error Message

The error message indicates that the Delta table is not writable because parts of the schema are not supported, followed by a specific reason code. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Error Conditions

The `DELTA_CANNOT_WRITE_EMPTY_SCHEMA` error class includes four distinct error conditions, each describing a specific schema issue:

### STRUCT_ALL_VOID_FIELDS

This error occurs when a column is a struct type, and all fields within that struct have VOID type. The VOID type in Spark/Databricks represents an empty or undefined data type, and a struct containing only void fields is effectively unusable for data storage. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

### STRUCT_NO_FIELDS

This error occurs when a column is a struct type with no fields defined. An empty struct has no usable structure for storing data. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

### TABLE_ALL_VOID_COLUMNS

This error occurs when all columns in the table schema have VOID type. With no columns of a usable data type, the table cannot store any meaningful data. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

### TABLE_NO_COLUMNS

This error occurs when the table schema has no columns defined. A schema with zero columns provides no structure for data storage. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Root Cause

The error arises when the schema of a [Delta Table](/concepts/delta-lake-table.md) is effectively empty — either because all columns are of VOID type, there are no columns at all, or struct columns contain no usable fields. This can happen due to incorrect schema definitions, data type conversions that result in void types, or operations that produce empty schemas. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Resolution

To resolve this error, ensure that the table schema contains at least one column with a non-void, supported data type. Common fixes include:

- Adding at least one column with a meaningful data type (e.g., STRING, INTEGER, TIMESTAMP) to the schema.
- If using struct columns, ensure they contain at least one field with a non-void type.
- Reviewing any schema transformations or type casting operations that may be converting all columns to VOID type.
- Checking that the schema definition does not produce empty structs or empty column lists.

## Related Concepts

- [Delta Table](/concepts/delta-lake-table.md) — The storage layer that enforces schema validation.
- [Delta Lake schema enforcement](/concepts/delta-table-schema-requirements.md) — Schema validation rules for Delta tables.
- Void type in Spark — The data type representing undefined or null types.
- [SQLSTATE 428GU](/concepts/sqlstate-428gu.md) — The SQL state code associated with this error.
- Error classes in Databricks — Comprehensive list of error classes.

## Sources

- delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md

# Citations

1. [delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md](/references/delta_cannot_write_empty_schema-error-condition-databricks-on-aws-78122c55.md)
