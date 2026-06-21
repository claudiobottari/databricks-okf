---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e28304aa1732f20938e619cbeba185b19bbbab96f17d47226803ef5d0a776b26
  pageDirectory: concepts
  sources:
    - delta_duplicate_columns_found-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sqlstate-42711
  citations:
    - file: delta_duplicate_columns_found-error-condition-databricks-on-aws.md
title: SQLSTATE 42711
description: A SQL standard error code for duplicate column definition violations, referenced by the DELTA_DUPLICATE_COLUMNS_FOUND error class in Databricks.
tags:
  - sql-standard
  - error-handling
  - databricks
timestamp: "2026-06-19T15:04:14.803Z"
---

# SQLSTATE 42711

**SQLSTATE 42711** is a SQL standard error code in class 42 (Syntax Error or Access Rule Violation). It indicates that a duplicate column name was found in a context where column names must be unique. In Databricks, this error is raised by the `DELTA_DUPLICATE_COLUMNS_FOUND` error class when Delta Lake operations encounter columns with the same name in locations that require uniqueness.^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## Error Message

The error message follows the pattern:

```
[SQLSTATE: 42711]
Found duplicate column(s): <duplicateCols>.
```

The placeholder `<duplicateCols>` lists the specific column names that appear more than once.^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## Classification

SQLSTATE 42711 belongs to **Class 42 — Syntax Error or Access Rule Violation**, which covers SQL syntax issues and access control violations.^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## Subtypes

The `DELTA_DUPLICATE_COLUMNS_FOUND` error class includes several subtypes that specify where the duplicate column was encountered:^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

| Subtype | Description |
|---------|-------------|
| `ADDING_COLUMNS` | Duplicate found while adding columns |
| `CLUSTER_BY` | Duplicate found in `CLUSTER BY` clause |
| `CONVERT_TO_DELTA` | Duplicate found during conversion to Delta format |
| `DATA` | Duplicate found in the data being saved |
| `EXISTING_SCHEMA` | Duplicate found in the existing table schema or a metadata update |
| `PARTITION_COLUMNS` | Duplicate found in partition columns |
| `PARTITION_SCHEMA` | Duplicate found in the partition schema |
| `READ_SCHEMA` | Duplicate found in the schema of data being read |
| `REPLACING_COLUMNS` | Duplicate found while replacing columns |
| `SPECIFIED_COLUMNS` | Duplicate found in specified columns |
| `TABLE_SCHEMA` | Duplicate found in the table schema |

## Common Causes

SQLSTATE 42711 typically occurs when:

- A schema definition includes the same column name more than once.
- Partition columns contain duplicates.
- A schema merge or update introduces duplicate names.
- Data written to a Delta table contains columns with duplicate names.
- Converting a non-Delta table to Delta format detects duplicate columns in the source schema.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that enforces unique column constraints.
- Table Schema Management — Best practices for managing Delta table schemas.
- Schema Evolution — How Delta Lake handles schema changes.
- SQLSTATE Error Classes — Other SQL state error codes in Databricks.

## Sources

- delta_duplicate_columns_found-error-condition-databricks-on-aws.md

# Citations

1. [delta_duplicate_columns_found-error-condition-databricks-on-aws.md](/references/delta_duplicate_columns_found-error-condition-databricks-on-aws-42950ac1.md)
