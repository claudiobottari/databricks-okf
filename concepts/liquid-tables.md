---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9385ec275113a475facca2f0edb13cd97eaac97ddb10d72c103e42cf47c1fb41
  pageDirectory: concepts
  sources:
    - delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - liquid-tables
    - Liquid table
    - Liquid Table Commands
  citations:
    - file: delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md
title: Liquid tables
description: Delta Lake tables that support clustering columns and impose restrictions on certain commands requiring predicates that reference only clustering columns.
tags:
  - delta-lake
  - liquid-tables
  - clustering
timestamp: "2026-06-19T18:28:28.253Z"
---

# Liquid Tables

**Liquid tables** are a type of table in Databricks that support **clustering columns**. Certain commands (such as those that use predicates) impose restrictions on which columns and expressions can be referenced when operating on a Liquid table. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

## Clustering Columns

A Liquid table can have one or more clustering columns — columns that define the physical layout of the data for optimised queries. When a command is run on a Liquid table, its predicate may reference **only** the clustering columns. Referencing a non‑clustering column in such a command triggers a `NON_CLUSTERING_COLUMN` error, which lists the allowed clustering columns. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

## Limitations

- **No clustering columns**: If a Liquid table has no clustering columns at all, the command is rejected with a `NO_CLUSTERING_COLUMNS` error. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]
- **Unresolved column**: If a column name in the predicate cannot be resolved against the set of clustering columns, an `UNRESOLVED_COLUMN` error is raised, showing the available clustering columns. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]
- **Unsupported expression**: The predicate expression itself must be one that the command supports. If an unsupported expression is used, an `UNSUPPORTED_EXPRESSION` error is produced. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

These restrictions ensure that operations on Liquid tables remain efficient by leveraging the clustering layout, and they prevent queries that would break that optimisation. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

## Related Concepts

- [Clustering columns](/concepts/clustering-columns.md) – The columns that define data layout in Liquid tables.
- [Delta tables](/concepts/delta-lake-table.md) – Liquid tables are a type of Delta table on Databricks.
- Predicate pushdown – The optimisation that benefits from clustering column predicates.
- [Error conditions](/concepts/delta-error-sub-conditions.md) – The `DELTA_UNSUPPORTED_CLUSTERING_COLUMN_PREDICATES` error class.

## Sources

- delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md

# Citations

1. [delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md](/references/delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws-b9f8e20f.md)
