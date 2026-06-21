---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e70722f9289a502e45dd0d3b88001c3c5bb4f387fef86ec3d39c4906c73a7ede
  pageDirectory: concepts
  sources:
    - delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - struct_all_void_fields-error-condition
    - SEC
    - STRUCT_ALL_VOID_FIELDS error condition
  citations:
    - file: delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
title: STRUCT_ALL_VOID_FIELDS error condition
description: A sub-error of DELTA_CANNOT_WRITE_EMPTY_SCHEMA where a struct column has all fields of VOID type
tags:
  - error-messages
  - delta-lake
  - schema-validation
timestamp: "2026-06-19T15:01:30.031Z"
---

Here is the wiki page for "STRUCT_ALL_VOID_FIELDS error condition", written based solely on the provided source material.

---

## STRUCT_ALL_VOID_FIELDS error condition

**STRUCT_ALL_VOID_FIELDS** is a specific error condition that can occur when attempting to write to a [Delta Lake](/concepts/delta-lake.md) table. It is a sub-type of the DELTA_CANNOT_WRITE_EMPTY_SCHEMA error|DELTA_CANNOT_WRITE_EMPTY_SCHEMA error condition, which indicates the target Delta table is not writable because parts of its schema are unsupported. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

### Error Message

The error message identifies the specific column causing the issue and indicates the problem: the column is a StructType|struct where every field has been defined as [VoidType|VOID type](/concepts/void-type-in-delta-lake.md).

```
The column `<columnPath>` is a struct where all fields have VOID type.
```

^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

### Cause

This error occurs when a schema contains a column of type `STRUCT` (a nested data type containing sub-fields), but every sub-field within that struct is of type `VOID`. A `VOID` type field represents the absence of a valid data type, resulting in an empty or unsupported schema structure that Delta Lake cannot write to. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

### Related Concepts

- DELTA_CANNOT_WRITE_EMPTY_SCHEMA error|DELTA_CANNOT_WRITE_EMPTY_SCHEMA error condition — The parent error class that encompasses this condition and other similar schema-related write errors.
- STRUCT_NO_FIELDS error condition — A related condition where a struct column has no fields at all (as opposed to all fields being of VOID type).
- TABLE_ALL_VOID_COLUMNS error condition — A related condition where all columns in the table schema have VOID type.
- TABLE_NO_COLUMNS error condition — A related condition where the table schema has no columns defined.
- [Delta Lake schema enforcement](/concepts/delta-table-schema-requirements.md) — The mechanism that prevents writing data with mismatched or unsupported schemas.
- [SQLSTATE 428GU](/concepts/sqlstate-428gu.md) — The SQL standard error code associated with this error class (Class 42: Syntax Error or Access Rule Violation).

## Sources

- delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md

# Citations

1. [delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md](/references/delta_cannot_write_empty_schema-error-condition-databricks-on-aws-78122c55.md)
