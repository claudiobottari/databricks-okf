---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cc39d5200759910bb7e2bb89119ed3ba45e872a6cfb4515fd2b074621d162886
  pageDirectory: concepts
  sources:
    - delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sqlstate-428gu
  citations:
    - file: delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
title: SQLSTATE 428GU
description: The SQL standard error code assigned to the DELTA_CANNOT_WRITE_EMPTY_SCHEMA error, classified under Class 42 (Syntax Error or Access Rule Violation).
tags:
  - delta-lake
  - error-messages
  - sql-standard
timestamp: "2026-06-19T18:22:22.094Z"
---

```markdown
---
title: SQLSTATE 428GU
summary: The SQL standard error code (class 42 — syntax error or access rule violation) assigned to the DELTA_CANNOT_WRITE_EMPTY_SCHEMA error condition in Databricks, raised when a Delta table schema is empty or consists entirely of VOID-type columns.
sources:
  - delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T15:30:00.000Z"
updatedAt: "2026-06-19T15:30:00.000Z"
tags:
  - sqlstate
  - error-code
  - databricks
  - standardization
aliases:
  - sqlstate-428gu
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# SQLSTATE 428GU

**SQLSTATE 428GU** is the error code assigned to the `DELTA_CANNOT_WRITE_EMPTY_SCHEMA` error condition in Databricks. It belongs to class 42 (syntax error or access rule violation) of the SQLSTATE standard. The error indicates that a [[Delta Lake]] table cannot be written to because its schema is unsupported — specifically, when the schema or its struct columns are empty or consist entirely of columns with a `VOID` type. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Error Conditions

The error has four distinct sub‑conditions, each providing a specific reason message: ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

| Sub‑condition | Reason message |
|---|---|
| `STRUCT_ALL_VOID_FIELDS` | The column `<columnPath>` is a struct where all fields have VOID type. |
| `STRUCT_NO_FIELDS` | The column `<columnPath>` is a struct with no fields. |
| `TABLE_ALL_VOID_COLUMNS` | All columns in the table schema have VOID type. |
| `TABLE_NO_COLUMNS` | The table schema has no columns defined. |

- **STRUCT_ALL_VOID_FIELDS**: Raised when a struct‑typed column contains only fields of type `VOID`, which cannot hold data. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]
- **STRUCT_NO_FIELDS**: Raised when a struct column has zero fields. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]
- **TABLE_ALL_VOID_COLUMNS**: Raised when every column in the table is of type `VOID`, effectively making the entire table empty. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]
- **TABLE_NO_COLUMNS**: Raised when the table schema has no columns defined at all. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Related Concepts

- [[Delta Lake]] – The storage layer that enforces schema validation and raises this error.
- SQLSTATE – Standard error code classification system.
- Class 42 Syntax Error or Access Rule Violation – The broader SQLSTATE class to which 428GU belongs.
- [[VOID type in Delta Lake|VOID type]] – A data type that represents the absence of data.
- Schema enforcement – The mechanism that prevents writes with unsupported schemas.

## Sources

- delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
```

# Citations

1. [delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md](/references/delta_cannot_write_empty_schema-error-condition-databricks-on-aws-78122c55.md)
