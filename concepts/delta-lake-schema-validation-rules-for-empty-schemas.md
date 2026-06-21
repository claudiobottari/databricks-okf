---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 38322ed990e1b7c527171f504969541c1de3c79039fe4d691b1464898352415c
  pageDirectory: concepts
  sources:
    - delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-schema-validation-rules-for-empty-schemas
    - DLSVRFES
  citations:
    - file: delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
title: Delta Lake schema validation rules for empty schemas
description: The four specific sub-conditions (STRUCT_ALL_VOID_FIELDS, STRUCT_NO_FIELDS, TABLE_ALL_VOID_COLUMNS, TABLE_NO_COLUMNS) under which Delta Lake refuses to write because the schema is effectively empty.
tags:
  - delta-lake
  - schema-validation
  - databricks
timestamp: "2026-06-18T15:16:59.686Z"
---

# Delta Lake Schema Validation Rules for Empty Schemas

**Delta Lake schema validation rules for empty schemas** define the conditions under which Delta Lake rejects write operations because the table schema is structurally empty or contains only unsupported types. These rules prevent writing data to schemas that cannot represent meaningful data. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Error Class and SQLSTATE

When a write operation is attempted against a Delta table with an invalid empty schema, Delta Lake raises the `DELTA_CANNOT_WRITE_EMPTY_SCHEMA` error condition with SQLSTATE `428GU`. The error message indicates the specific reason the schema is considered invalid. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Validation Rules

Delta Lake enforces four specific rules that trigger this error condition:

### TABLE_NO_COLUMNS

The table schema has no columns defined. This is the most basic form of an empty schema — a Delta table must have at least one column to be writable. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

### TABLE_ALL_VOID_COLUMNS

All columns in the table schema have [VOID type](/concepts/void-type-in-delta-lake.md). Even though columns are defined, none of them can hold actual data, making the table effectively unwritable. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

### STRUCT_NO_FIELDS

A column of struct type contains no fields. The error message identifies which column path contains the empty struct. Nested structs must have at least one field to be valid. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

### STRUCT_ALL_VOID_FIELDS

A column of struct type has fields, but all of those fields are of VOID type. The error message identifies the problematic column path. Like table-level VOID columns, structurally void fields cannot store meaningful data. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Common Causes

These validation errors typically occur when:

- Schema evolution operations produce invalid schemas
- Programmatic schema construction omits required columns
- [DataFrame transformations](/concepts/remote-dataframe-operations.md) inadvertently drop or void all columns
- [Column mapping](/concepts/column-mapping-in-delta-lake.md) operations result in empty struct definitions

## Resolution

To resolve this error, ensure that the Delta table schema contains at least one non-void column with an appropriate data type. For struct columns, ensure at least one field is defined with a supported type. Valid schemas should include columns with types such as STRING, INTEGER, FLOAT, or other supported Delta data types.

## Related Concepts

- Delta Lake schema validation
- Schema evolution in Delta Lake
- Void type in Apache Spark
- DataFrame schema requirements
- Delta Lake error classes

## Sources

- delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md

# Citations

1. [delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md](/references/delta_cannot_write_empty_schema-error-condition-databricks-on-aws-78122c55.md)
