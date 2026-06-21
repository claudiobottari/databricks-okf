---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 14a90bebbabd581797fada66efd842d4e1b2170fc0f04a38de84732f7babdc2e
  pageDirectory: concepts
  sources:
    - delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-clustering-columns
    - DLCC
  citations:
    - file: delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md
title: Delta Lake Clustering Columns
description: Columns designated as clustering columns in Liquid tables; only these columns may be referenced in certain command predicates.
tags:
  - databricks
  - delta-lake
  - clustering
timestamp: "2026-06-18T15:25:00.002Z"
---

# Delta Lake Clustering Columns

**Delta Lake clustering columns** are one or more columns in a [Liquid table](https://docs.databricks.com/aws/en/liquid-clustering) that control how data is physically organized at the file level. Clustering columns are used to accelerate queries by reducing the amount of data scanned, especially for filter-heavy workloads. When a table defines clustering columns, certain operations and predicates are restricted to those columns to maintain the clustering property.

## Predicate restrictions on Liquid tables

On a Liquid table, only clustering columns may be referenced in predicates that are evaluated as part of certain commands (for example, `DELETE`, `UPDATE`, or `MERGE`). If a predicate references a column that is not a clustering column, the query fails with the `NON_CLUSTERING_COLUMN` error and lists the allowed clustering columns. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

If a Liquid table has no clustering columns defined, the command is not supported at all, and the `NO_CLUSTERING_COLUMNS` error is raised. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

## Unresolved and unsupported expressions

When a clustering column name in a predicate cannot be resolved (e.g., misspelled or does not exist), the `UNRESOLVED_COLUMN` error is returned along with the list of available clustering columns. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

If the predicate itself contains an expression that is not supported (for example, a complex function or subquery), the `UNSUPPORTED_EXPRESSION` error is returned. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

## Error conditions overview

| Error sub-type | Meaning |
|----------------|---------|
| `NON_CLUSTERING_COLUMN` | The predicate references a column that is not a clustering column. |
| `NO_CLUSTERING_COLUMNS` | The Liquid table has no clustering columns, so the command is not allowed. |
| `UNRESOLVED_COLUMN` | The referenced column name cannot be resolved against the table’s clustering columns. |
| `UNSUPPORTED_EXPRESSION` | The predicate expression is not supported by the command for Liquid tables. |

All errors belong to SQL state `0A000` (feature not supported). ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

## Related concepts

- [Liquid Clustering](/concepts/liquid-clustering.md) – The general feature for defining clustering columns in Delta Lake.
- [Delta Lake](/concepts/delta-lake.md) – The storage layer underlying Liquid tables.
- [Liquid Table Commands](/concepts/liquid-tables.md) – The set of DML commands that enforce clustering-column restrictions.

## Sources

- delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md

# Citations

1. [delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md](/references/delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws-b9f8e20f.md)
