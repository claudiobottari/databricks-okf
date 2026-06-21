---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eccef80bda8df028b67192692b397113f277d83f57a81feb78831fe733ae097c
  pageDirectory: concepts
  sources:
    - delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - void-type-in-delta-lake-schemas
    - VTIDLS
  citations:
    - file: delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
title: VOID Type in Delta Lake Schemas
description: The VOID data type in Delta Lake represents columns or fields that have no valid type, making schemas containing it effectively empty and unwritable.
tags:
  - delta-lake
  - data-types
  - schema
timestamp: "2026-06-19T18:22:16.553Z"
---

# VOID Type in Delta Lake Schemas

The **VOID type** is a data type within [Delta Lake](/concepts/delta-lake.md) schemas that is not supported for write operations. When a Delta table’s schema contains columns or struct fields of type VOID, the write operation fails with the `DELTA_CANNOT_WRITE_EMPTY_SCHEMA` error. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Error Condition

The `DELTA_CANNOT_WRITE_EMPTY_SCHEMA` error (SQLSTATE: 428GU) occurs when the Delta table is not writable because parts of the schema are not supported. The error provides one of several reasons, two of which directly involve the VOID type. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

### TABLE_ALL_VOID_COLUMNS

This reason is raised when **all columns in the table schema have VOID type**. In this case, the entire table schema is composed of unsupported VOID columns, making writes impossible. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

### STRUCT_ALL_VOID_FIELDS

This reason is raised when a column of type `STRUCT` contains fields where **all fields have VOID type**. The error message includes the column path of the offending struct column. While the struct column itself might be of a supported type, its fields are all VOID, which prevents writing. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Related Empty Schema Conditions

Although not directly about the VOID type, the `DELTA_CANNOT_WRITE_EMPTY_SCHEMA` error class also covers two additional conditions that describe empty schemas without VOID fields:

- **TABLE_NO_COLUMNS** – The table schema has **no columns defined** at all. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]
- **STRUCT_NO_FIELDS** – A struct column has **no fields** defined. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

These conditions, together with the VOID‑related ones, ensure that every column or struct in a Delta table schema has a usable type.

## Implications

A Delta table cannot be written to if its schema contains any column or struct field of VOID type, or if the schema is otherwise empty. Users must ensure that the table schema contains only supported types (such as `INTEGER`, `STRING`, `STRUCT` with non‑VOID fields) before performing write operations. The VOID type typically indicates a malformed schema or a schema derived from an empty DataFrame.

## Related Concepts

- Delta Lake schemas
- [Delta Lake write operations](/concepts/delta-lake-dml-operations.md)
- STRUCT type in Delta Lake
- DataFrame schemas
- [SQLSTATE 428GU](/concepts/sqlstate-428gu.md)

## Sources

- delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md

# Citations

1. [delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md](/references/delta_cannot_write_empty_schema-error-condition-databricks-on-aws-78122c55.md)
