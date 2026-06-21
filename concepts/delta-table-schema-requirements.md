---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a7b615a230720d6cf4597c1f09952413d31363554bc414d1953dcb9d09582c7b
  pageDirectory: concepts
  sources:
    - delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-table-schema-requirements
    - DTSR
    - Delta Lake Schema Enforcement
    - Delta Lake schema enforcement
    - Delta Table Schema Constraints
    - Delta Table Schema Management
  citations:
    - file: delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
title: Delta table schema requirements
description: The requirement that a Delta table must have at least one non-void column and any struct columns must have at least one non-void field to be writable.
tags:
  - delta-lake
  - table-creation
  - schema-design
timestamp: "2026-06-18T15:17:01.537Z"
---

# Delta table schema requirements

Delta tables require a valid schema composed of supported data types. Writing to a Delta table fails when the table's schema is empty or contains unsupported types, notably the `VOID` type. The error class `DELTA_CANNOT_WRITE_EMPTY_SCHEMA` (SQLSTATE: 428GU) identifies four specific conditions that make a schema unsupported.^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Schema requirements

- The **table schema must contain at least one column**. A schema with zero columns (`TABLE_NO_COLUMNS`) is not writeable.^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]
- **No column may be of type `VOID`**. If all columns in the table have `VOID` type (`TABLE_ALL_VOID_COLUMNS`), the schema is invalid.^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]
- **Struct columns must have at least one field** and that field must not be `VOID`. A struct with zero fields (`STRUCT_NO_FIELDS`) or a struct where all fields are of type `VOID` (`STRUCT_ALL_VOID_FIELDS`) is unsupported.^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

These requirements apply at all nesting levels; a `VOID` type or empty struct anywhere in the schema tree will cause the write to fail.

## Error conditions

| Condition | Meaning |
|-----------|---------|
| `TABLE_NO_COLUMNS` | The table schema has no columns defined. |
| `TABLE_ALL_VOID_COLUMNS` | All columns in the table schema have `VOID` type. |
| `STRUCT_NO_FIELDS` | A column of type `STRUCT` has no fields. |
| `STRUCT_ALL_VOID_FIELDS` | A column of type `STRUCT` has fields, but all of them are of `VOID` type. |

The error message reports the specific column path that caused the issue, enabling targeted schema corrections.^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Best practices

- Always define at least one non-void column when creating a Delta table.
- When using nested types, ensure each struct contains at least one field with a concrete data type.
- Validate schemas programmatically before writes to avoid runtime failures.

## Related concepts

- [Delta table](/concepts/delta-lake-table.md) – Core storage format
- Schema definition in SQL – How columns and types are declared
- Data types in Databricks – Supported and unsupported types
- Error classes in Databricks – General error handling framework
- [VOID type](/concepts/void-type-in-delta-lake.md) – The type that cannot appear in a Delta schema

## Sources

- delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md

# Citations

1. [delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md](/references/delta_cannot_write_empty_schema-error-condition-databricks-on-aws-78122c55.md)
