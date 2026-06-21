---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 70dd4b669625ebc5e5b116dcaee6550146766d627584b083ad450ec8649cf529
  pageDirectory: concepts
  sources:
    - delta_duplicate_columns_found-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_duplicate_columns_found
    - DELTA_DUPLICATE_COLUMNS_FOUND
  citations:
    - file: delta_duplicate_columns_found-error-condition-databricks-on-aws.md
title: DELTA_DUPLICATE_COLUMNS_FOUND
description: A Delta Lake error class raised when duplicate column names are detected in a table operation, with sub-reasons identifying the specific operation context.
tags:
  - delta-lake
  - error-handling
  - schema
timestamp: "2026-06-19T15:04:13.189Z"
---

# DELTA_DUPLICATE_COLUMNS_FOUND

`DELTA_DUPLICATE_COLUMNS_FOUND` is a Delta Lake error condition that occurs when duplicate column names are detected during a metadata operation. The error is associated with SQLSTATE 42711 (class 42 – syntax error or access rule violation). When raised, the error message includes the duplicate column names found: `Found duplicate column(s): <duplicateCols>`. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## Sub‑error Contexts

The error class provides several sub‑error types that indicate the specific operation in which the duplicate was detected:

| Sub‑error | Description |
|-----------|-------------|
| `ADDING_COLUMNS` | Duplicate found while adding columns. |
| `CLUSTER_BY` | Duplicate found in the `CLUSTER BY` clause. |
| `CONVERT_TO_DELTA` | Duplicate found during conversion to Delta format. |
| `DATA` | Duplicate found in the data being saved. |
| `EXISTING_SCHEMA` | Duplicate found in the existing table schema (also used for metadata update duplicates). |
| `PARTITION_COLUMNS` | Duplicate found in the partition columns. |
| `PARTITION_SCHEMA` | Duplicate found in the partition schema. |
| `READ_SCHEMA` | Duplicate found in the schema of the data being read. |
| `REPLACING_COLUMNS` | Duplicate found while replacing columns. |
| `SPECIFIED_COLUMNS` | Duplicate found in the specified columns. |
| `TABLE_SCHEMA` | Duplicate found in the table schema. |

^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The storage layer that enforces schema constraints.
- [Error Handling in Databricks](/concepts/error-handling-in-databricks-notebook-workflows.md) – General guidance for managing errors.
- SQLSTATE – The SQL standard error code classification used by this error.

## Sources

- delta_duplicate_columns_found-error-condition-databricks-on-aws.md

# Citations

1. [delta_duplicate_columns_found-error-condition-databricks-on-aws.md](/references/delta_duplicate_columns_found-error-condition-databricks-on-aws-42950ac1.md)
