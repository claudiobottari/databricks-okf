---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f41317735b035ae24c2ea1df0bd9be4500911b637bdb0df70c92c6bbc7227676
  pageDirectory: concepts
  sources:
    - delta_duplicate_columns_found-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_duplicate_columns_found-error-databricks
    - DE(
  citations:
    - file: delta_duplicate_columns_found-error-condition-databricks-on-aws.md
title: DELTA_DUPLICATE_COLUMNS_FOUND Error (Databricks)
description: A Delta Lake error class raised when duplicate column names are detected during table operations, with sub-classifications for different operation contexts.
tags:
  - delta-lake
  - error-messages
  - databricks
timestamp: "2026-06-19T10:05:12.506Z"
---

# DELTA_DUPLICATE_COLUMNS_FOUND Error (Databricks)

**DELTA_DUPLICATE_COLUMNS_FOUND** is a Delta Lake error class that occurs when duplicate column names are detected in a schema, data, or operation. The error is raised when the Delta writer or reader encounters column names that are not unique within the scope of the operation. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## Error Message

The full error message includes the list of duplicate columns:

```
Found duplicate column(s): <duplicateCols>.
```

This error is associated with SQLSTATE 42711 (class 42 – syntax error or access rule violation). ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## SQLSTATE

| State | Meaning |
|-------|---------|
| 42711 | Duplicate column(s) found |

## Common Causes

The error class is divided into sub‑types that indicate the operation or context in which the duplicate was found. The following sub‑causes are documented:

| Sub‑cause | Description |
|------------|-------------|
| `ADDING_COLUMNS` | Duplicate column detected while adding columns to a table. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md] |
| `CLUSTER_BY` | Duplicate column found in a `CLUSTER BY` clause. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md] |
| `CONVERT_TO_DELTA` | Duplicate column encountered during conversion of a non‑Delta table to [Delta Lake](/concepts/delta-lake.md) format. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md] |
| `DATA` | Duplicate column detected in the data being saved or written to a table. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md] |
| `EXISTING_SCHEMA` | Duplicate column found in the existing table schema (or in a metadata update). ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md] |
| `PARTITION_COLUMNS` | Duplicate column specified as a partition column. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md] |
| `PARTITION_SCHEMA` | Duplicate column found in the partition schema. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md] |
| `READ_SCHEMA` | Duplicate column detected in the schema of data being read. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md] |
| `REPLACING_COLUMNS` | Duplicate column found while replacing columns (e.g., using `ALTER TABLE REPLACE COLUMNS`). ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md] |
| `SPECIFIED_COLUMNS` | Duplicate column found in an explicitly specified column list. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md] |
| `TABLE_SCHEMA` | Duplicate column found in the table schema (e.g., during schema validation). ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md] |

## Troubleshooting

- **Inspect the duplicate column names** reported in the error message.
- **Review the operation** that triggered the error (e.g., the `ADDING_COLUMNS` sub‑cause suggests an `ALTER TABLE ADD COLUMNS` statement, while `DATA` suggests the source DataFrame has duplicate column names).
- **Ensure column names are unique** in the schema before performing writes, schema changes, or partitioning operations.
- **Check partition and clustering columns** for duplication when using `PARTITIONED BY` or `CLUSTER BY`.
- **Avoid duplicate names** when using schema evolution features such as `mergeSchema` or `overwriteSchema`.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The storage layer that enforces the duplicate column constraint.
- [Table Schema](/concepts/labeling-schema.md) – The definition of column names and types for a Delta table.
- Schema Evolution – Techniques for handling schema changes, which can expose duplicate column errors.
- ALTER TABLE – DDL statements that may trigger `ADDING_COLUMNS` or `REPLACING_COLUMNS` sub‑causes.
- Partitioning – Defining partition columns that must be unique.
- CLUSTER BY – A Delta feature that uses specified columns for clustering (requires unique column names).

## Sources

- delta_duplicate_columns_found-error-condition-databricks-on-aws.md

# Citations

1. [delta_duplicate_columns_found-error-condition-databricks-on-aws.md](/references/delta_duplicate_columns_found-error-condition-databricks-on-aws-42950ac1.md)
