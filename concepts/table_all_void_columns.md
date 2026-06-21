---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bf28532d4d1ae385a73c22cfff28452fa7c98a7d4e14e5ce631d89fe1da3f070
  pageDirectory: concepts
  sources:
    - delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - table_all_void_columns
    - TABLE_ALL_VOID_COLUMNS
  citations:
    - file: delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
title: TABLE_ALL_VOID_COLUMNS
description: A sub-reason for DELTA_CANNOT_WRITE_EMPTY_SCHEMA where every column in the table schema has VOID type.
tags:
  - delta-lake
  - error-messages
  - schema
timestamp: "2026-06-19T18:22:00.323Z"
---

# TABLE_ALL_VOID_COLUMNS

**TABLE_ALL_VOID_COLUMNS** is a specific sub-reason for the [`DELTA_CANNOT_WRITE_EMPTY_SCHEMA` error class](https://docs.databricks.com/aws/en/error-messages/delta-cannot-write-empty-schema-error-class) (SQLSTATE: 428GU). It occurs when a [Delta Lake](/concepts/delta-lake.md) write operation attempts to use a schema where every column in the table schema has the `VOID` data type. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Error Message

The exact error returned is:

```
All columns in the table schema have VOID type.
```

^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Cause

The `VOID` type in Apache Spark represents an absence of a data type. This error occurs when a Delta table is not writable because all columns in its schema are of `VOID` type. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Related Conditions

Other sub-conditions of `DELTA_CANNOT_WRITE_EMPTY_SCHEMA` include:

- STRUCT_ALL_VOID_FIELDS – A struct column where all fields have `VOID` type.
- STRUCT_NO_FIELDS – A struct column with no fields.
- TABLE_NO_COLUMNS – The table schema has no columns defined at all.

^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Sources

- delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md

# Citations

1. [delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md](/references/delta_cannot_write_empty_schema-error-condition-databricks-on-aws-78122c55.md)
