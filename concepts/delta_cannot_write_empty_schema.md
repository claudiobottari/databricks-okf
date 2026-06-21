---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2dd2d2673e1cb6074c616a8f9d118f938efcac0d306a67ad1978d406cf387a4d
  pageDirectory: concepts
  sources:
    - delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_cannot_write_empty_schema
    - DELTA_CANNOT_WRITE_EMPTY_SCHEMA
  citations:
    - file: delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
title: DELTA_CANNOT_WRITE_EMPTY_SCHEMA
description: A Delta Lake error raised when attempting to write to a table whose schema is empty or contains only unsupported (VOID) types.
tags:
  - delta-lake
  - error-messages
  - schema
timestamp: "2026-06-19T18:22:05.368Z"
---

```markdown
---
title: DELTA_CANNOT_WRITE_EMPTY_SCHEMA
summary: A Delta Lake error condition raised when attempting to write to a table whose schema is empty or composed entirely of unsupported VOID‑type columns.
sources:
  - delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:50:05.431Z"
updatedAt: "2026-06-19T10:02:26.774Z"
tags:
  - error-messages
  - delta-lake
  - schema-validation
aliases:
  - delta_cannot_write_empty_schema
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# DELTA_CANNOT_WRITE_EMPTY_SCHEMA Error Condition

**DELTA_CANNOT_WRITE_EMPTY_SCHEMA** is a Delta Lake error that occurs when attempting to write to a Delta table whose schema is empty or contains only unsupported column types. The error is classified under **SQLSTATE 428GU**. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Error Message

The error message follows this pattern:

```
The Delta table is not writable because parts of the schema are not supported. Reason: <reason_code>
```

Where `<reason_code>` is one of the following sub‑conditions. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Sub‑Conditions

The error includes a specific reason code that identifies the exact schema issue.

### STRUCT_ALL_VOID_FIELDS

The column `<columnPath>` is a struct where all fields have VOID type. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

### STRUCT_NO_FIELDS

The column `<columnPath>` is a struct with no fields. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

### TABLE_ALL_VOID_COLUMNS

All columns in the table schema have VOID type. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

### TABLE_NO_COLUMNS

The table schema has no columns defined. ^[delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md]

## Related Concepts

- [[Delta Lake]] — The storage layer that enforces schema validation.
- [[SQLSTATE 428GU]] — The SQLSTATE classification for this error.
- [[VOID type in Delta Lake|VOID Type]] — The data type representing an undefined or missing type.
- Struct data type — A composite type that can contain multiple fields.
- Schema Validation — The process of checking schema correctness before writes.

## Sources

- delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md
```

# Citations

1. [delta_cannot_write_empty_schema-error-condition-databricks-on-aws.md](/references/delta_cannot_write_empty_schema-error-condition-databricks-on-aws-78122c55.md)
