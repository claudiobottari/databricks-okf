---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 533a54fb323faccf77af18139111b3c289d2394d7d031c1428bfd0e7cb33050e
  pageDirectory: concepts
  sources:
    - delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - clustering-columns-in-delta-lake
    - CCIDL
    - Clustering in Delta Lake
  citations:
    - file: delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md
title: Clustering Columns in Delta Lake
description: Columns designated for data clustering in Delta Lake Liquid tables; commands on Liquid tables may only reference these columns in predicates, with specific error sub-conditions for violations.
tags:
  - databricks
  - delta-lake
  - clustering
  - data-organization
timestamp: "2026-06-18T11:57:42.153Z"
---

# Clustering Columns in Delta Lake

**Clustering columns in Delta Lake** are columns that are used to physically co-locate related data in a [Delta Lake](/concepts/delta-lake.md) table, improving query performance by enabling data skipping and predicate pushdown. When a table is defined as a *Liquid table*, certain commands (such as `UPDATE`, `DELETE`, or `MERGE`) require that predicates reference only the clustering columns. If a predicate references a non-clustering column, or if the Liquid table has no clustering columns defined, an error condition is raised. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

## `DELTA_UNSUPPORTED_CLUSTERING_COLUMN_PREDICATES` Error Class

This error class (SQLSTATE `0A000` – feature not supported) occurs when a command executed on a Liquid table contains predicates that are not valid for that table’s clustering columns. The error message includes one of four sub‑conditions, depending on the specific cause. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

### `NON_CLUSTERING_COLUMN`

```
<command> predicate references non-clustering column '<columnName>'.
Only the clustering columns may be referenced when <command> is run
on a Liquid table: [<columnList>].
```

This sub‑condition is raised when a predicate in the command refers to a column that is not in the set of clustering columns defined for the Liquid table. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

### `NO_CLUSTERING_COLUMNS`

```
<command> command is not supported on Liquid tables without clustering columns.
```

This sub‑condition occurs when the Liquid table has no clustering columns at all. The command cannot be executed because there are no clustering columns to constrain the predicate. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

### `UNRESOLVED_COLUMN`

```
Fail to resolve column '<columnName>' in <command> predicate.
Available clustering columns: [<columnList>].
```

This sub‑condition indicates that the column named in the predicate does not match any of the clustering columns listed for the table. The available clustering columns are provided in the error message. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

### `UNSUPPORTED_EXPRESSION`

```
Unsupported expression: <expression>.
```

This sub‑condition is raised when the predicate contains an expression that is not supported in the context of a Liquid table command. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The open‑source storage layer that provides ACID transactions and scalable metadata handling.
- [Liquid tables](/concepts/liquid-tables.md) — A special type of Delta table that enforces constraints on clustering columns for certain data manipulation commands.
- [Clustering in Delta Lake](/concepts/clustering-columns-in-delta-lake.md) — The broader concept of physically organizing data by key columns to accelerate queries.

## Sources

- delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md

# Citations

1. [delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md](/references/delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws-b9f8e20f.md)
