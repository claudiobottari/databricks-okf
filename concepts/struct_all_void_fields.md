---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f19356dfe0bdc44af0e09fa5f882b8b73ad7596f2baa1e43a593eb3e58774819
  pageDirectory: concepts
  sources:
    - delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - struct_all_void_fields
    - STRUCT_ALL_VOID_FIELDS
    - struct_all_void_fields-error-condition
    - SEC
    - STRUCT_ALL_VOID_FIELDS error condition
  citations:
    - file: delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
title: STRUCT_ALL_VOID_FIELDS
description: A sub-reason for DELTA_CANNOT_WRITE_EMPTY_SCHEMA where a struct column has all fields of VOID type.
tags:
  - delta-lake
  - error-messages
  - schema
timestamp: "2026-06-19T18:22:02.092Z"
---

---
title: STRUCT_ALL_VOID_FIELDS
summary: A sub-reason for the DELTA_CANNOT_WRITE_EMPTY_SCHEMA error class, indicating a struct column where every field has the VOID type.
sources:
  - delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:50:10.579Z"
updatedAt: "2026-06-19T10:02:24.766Z"
tags:
  - delta-lake
  - error-message
  - schema
  - void
aliases:
  - struct_all_void_fields
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# STRUCT_ALL_VOID_FIELDS

**STRUCT_ALL_VOID_FIELDS** is a specific sub‑reason reported under the [DELTA_CANNOT_WRITE_EMPTY_SCHEMA](https://docs.databricks.com/aws/en/error-messages/delta-cannot-write-empty-schema-error-class) error class. It occurs when a Delta table cannot be written to because a struct‑typed column contains only fields whose data type is **VOID**. The VOID type represents the absence of a concrete schema, and a struct composed entirely of such fields provides no usable structure for writing data. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## SQLSTATE

The error class is reported with **SQLSTATE 428GU**, which falls under the “Syntax error or access rule violation” class. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Related Conditions

The `DELTA_CANNOT_WRITE_EMPTY_SCHEMA` error class includes three other sub‑reasons that describe different forms of an empty or void schema: ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

| Condition | Description |
|-----------|-------------|
| **STRUCT_ALL_VOID_FIELDS** | The column `<columnPath>` is a struct where all fields have VOID type. |
| **STRUCT_NO_FIELDS** | The column `<columnPath>` is a struct with no fields. |
| **TABLE_ALL_VOID_COLUMNS** | All columns in the table schema have VOID type. |
| **TABLE_NO_COLUMNS** | The table schema has no columns defined. |

## Sources

- delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md

---

### Related Wiki Links

- [Delta Lake](/concepts/delta-lake.md)
- Schema
- Error message
- SQLSTATE

# Citations

1. [delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md](/references/delta_cannot_write_empty_schema-error-condition-databricks-on-aws-78122c55.md)
