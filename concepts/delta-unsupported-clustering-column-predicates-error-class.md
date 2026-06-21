---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: efdb050fd29567381f2002f76f3522b0f19328903b58ada0d56fee8c8b06771c
  pageDirectory: concepts
  sources:
    - delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-unsupported-clustering-column-predicates-error-class
    - DUCCPEC
  citations:
    - file: delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md
title: Delta Unsupported Clustering Column Predicates Error Class
description: A Delta Lake error class (DELTA_UNSUPPORTED_CLUSTERING_COLUMN_PREDICATES) raised when a command on a Liquid table uses predicates that reference non-clustering columns, missing clustering columns, unresolved columns, or unsupported expressions.
tags:
  - databricks
  - delta-lake
  - error-messages
  - clustering
timestamp: "2026-06-18T11:57:33.238Z"
---

# Delta Unsupported Clustering Column Predicates Error Class

The **DELTA_UNSUPPORTED_CLUSTERING_COLUMN_PREDICATES** error class occurs when a command on a [Liquid table](/concepts/liquid-tables.md) uses predicates that reference columns which are not allowed. Liquid tables support predicate pushdown only on clustering columns; any predicate referring to non‑clustering columns, missing columns, or unsupported expressions triggers this error. The SQLSTATE for this class is `0A000` (feature not supported). ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

## Sub‑errors

The error class includes four distinct sub‑errors, each with its own message template.

### NON_CLUSTERING_COLUMN

The command’s predicate references a column that is not a clustering column of the Liquid table. Only the clustering columns may be used in predicates when the command is run on a Liquid table.

> `<command>` predicate references non-clustering column '`<columnName>`'. Only the clustering columns may be referenced when `<command>` is run on a Liquid table: \[`<columnList>`\].

^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

### NO_CLUSTERING_COLUMNS

The Liquid table has no clustering columns defined, so predicate‑based commands are not supported.

> `<command>` command is not supported on Liquid tables without clustering columns.

^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

### UNRESOLVED_COLUMN

The predicate references a column that cannot be resolved against the table’s clustering columns. The message lists the available clustering columns.

> Fail to resolve column '`<columnName>`' in `<command>` predicate. Available clustering columns: \[`<columnList>`\].

^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

### UNSUPPORTED_EXPRESSION

The predicate contains an expression that is not supported for Liquid table commands.

> Unsupported expression: `<expression>`.

^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that underpins Liquid tables.
- [Liquid table](/concepts/liquid-tables.md) — A table type that supports clustering columns for optimized predicate pushdown.
- [Clustering columns](/concepts/clustering-columns.md) — Columns used to physically organize data in a Liquid table.
- SQLSTATE — The standard error code classification used by Databricks.

## Sources

- delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md

# Citations

1. [delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md](/references/delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws-b9f8e20f.md)
