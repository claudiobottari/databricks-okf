---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a7cc575b786c1bfe05facf6bb09b8112fa1353d7ba510c9705a1d6161c66fe3e
  pageDirectory: concepts
  sources:
    - delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-error-sqlstate-codes
    - DESC
    - Delta Lake SQLSTATE Error Codes
    - SQLSTATE error classes|SQLSTATE class `KD00E`
  citations:
    - file: delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md
title: Delta error SQLSTATE codes
description: Standardized SQLSTATE codes used by Databricks Delta to classify error conditions, such as class 0A for feature not supported
tags:
  - error-messages
  - sql
  - databricks
timestamp: "2026-06-19T15:09:39.022Z"
---

# Delta error SQLSTATE codes

**Delta error SQLSTATE codes** are standard SQL state identifiers assigned to errors that occur when operations are performed on [Delta Lake](/concepts/delta-lake.md) tables. Each error class corresponds to a specific SQLSTATE value that indicates the category of the failure. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

## SQLSTATE: 0A000 – Feature not supported

Error class `DELTA_UNSUPPORTED_CLUSTERING_COLUMN_PREDICATES` is assigned SQLSTATE `0A000`, which falls under the **Feature not supported** category in the SQL standard. This error is raised when a command issued against a [Liquid table](/concepts/liquid-tables.md) uses predicates that are not supported for the operation. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

## Sub‑error conditions

Each occurrence of the error class includes a specific sub‑condition that describes the exact reason for the failure. The following sub‑conditions are defined:

### NON_CLUSTERING_COLUMN[​](#non_clustering_column)

The predicate references a column that is not configured as a clustering column. Only clustering columns may be referenced when running the command on a Liquid table. The error message lists the available clustering columns. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

### NO_CLUSTERING_COLUMNS[​](#no_clustering_columns)

The command is not supported on a Liquid table that has no clustering columns defined. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

### UNRESOLVED_COLUMN[​](#unresolved_column)

The column named in the predicate cannot be resolved against the table’s clustering columns. The error message shows the list of available clustering columns. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

### UNSUPPORTED_EXPRESSION[​](#unsupported_expression)

The predicate contains an expression that is not supported for the operation, regardless of which columns it references. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

## Related concepts

- SQLSTATE – Standard SQL state codes used in Databricks error messages.
- [Delta Lake](/concepts/delta-lake.md) – The open‑source storage layer that provides ACID transactions and table clustering.
- [Liquid tables](/concepts/liquid-tables.md) – A [Delta Lake Table](/concepts/delta-lake-table.md) variant that supports liquid clustering.
- [Clustering columns](/concepts/clustering-columns.md) – Columns used to physically co‑locate data for query performance.
- [Delta error classes](/concepts/databricks-error-classes.md) – The full taxonomy of error classes in Databricks.

## Sources

- delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md

# Citations

1. [delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md](/references/delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws-b9f8e20f.md)
