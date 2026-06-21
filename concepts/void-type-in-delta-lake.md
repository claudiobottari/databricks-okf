---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8e0e4e555aabf7fdf3db4f1505e6dc8408bb31e0422d50cfb75df54d23cbe2b7
  pageDirectory: concepts
  sources:
    - delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - void-type-in-delta-lake
    - VTIDL
    - VOID Type
    - VOID type
    - Void type
    - VoidType|VOID type
    - void-type-in-delta-lake-schemas
    - VTIDLS
  citations:
    - file: delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
title: VOID type in Delta Lake
description: An unsupported column type in Delta Lake schemas; when all columns or all struct fields are of VOID type, the table is considered unwritable.
tags:
  - delta-lake
  - schema
  - data-types
timestamp: "2026-06-18T15:16:53.885Z"
---

## VOID type in Delta Lake

**VOID type** is a special data type in [Delta Lake](/concepts/delta-lake.md) that represents the absence of a meaningful value at the type level. A column or struct field of type VOID has no valid representation in storage, which makes Delta tables that contain only VOID columns or struct fields unreadable and unwritable.

## Error Condition

When a Delta table has a schema that is entirely composed of VOID types—either at the table level or within nested structs—writing to the table fails with the `DELTA_CANNOT_WRITE_EMPTY_SCHEMA` error. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

The error message includes one of four specific reasons:

- **STRUCT_ALL_VOID_FIELDS** – A struct column exists where all of its fields are of VOID type. The column path is reported. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]
- **STRUCT_NO_FIELDS** – A struct column has no fields at all, which is semantically similar to having all VOID fields. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]
- **TABLE_ALL_VOID_COLUMNS** – Every column in the table schema is of VOID type. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]
- **TABLE_NO_COLUMNS** – The table schema has no columns defined. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## SQLSTATE

The error condition has the SQLSTATE `428GU`, which falls under Class 42 – Syntax Error or Access Rule Violation. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Implications

A table with an entirely VOID schema cannot store or retrieve data. This scenario typically arises from inadvertent schema manipulation (e.g., dropping all columns or casting all columns to a null type) or from creating a table with no columns at all. The error prevents writes to such tables, ensuring that no invalid data is persisted.

To resolve the error, the table schema must be altered to include at least one non-VOID column, or structs must contain at least one field with a concrete type.

## Related Concepts

- Delta Lake Schema
- Struct Type in Delta Lake
- [Databricks Error Messages](/concepts/databricks-error-message-reference.md)
- [SQLSTATE 428GU](/concepts/sqlstate-428gu.md)

## Sources

- delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md

# Citations

1. [delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md](/references/delta_cannot_write_empty_schema-error-condition-databricks-on-aws-78122c55.md)
