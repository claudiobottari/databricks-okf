---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5322e27d2df8e3321a1c85ac08c6f8eb02a5d2fa564f84a7a42a3555d622e469
  pageDirectory: concepts
  sources:
    - delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - liquid-tables-databricks
    - LT(
  citations:
    - file: delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md
title: Liquid tables (Databricks)
description: A Databricks table type that supports clustering columns and restricts certain command predicates to only reference those clustering columns.
tags:
  - databricks
  - liquid-tables
  - table-storage
timestamp: "2026-06-19T10:10:03.851Z"
---

# Liquid Tables (Databricks)

**Liquid Tables** are a table type in Databricks that use [Liquid Clustering](/concepts/liquid-clustering.md) to physically organize data for improved query performance. When write commands such as `DELETE`, `UPDATE`, or `MERGE` are executed on a Liquid table, the predicate (the `WHERE` clause) must reference only the table's clustering columns. If a predicate includes a non‑clustering column, the operation fails with a `DELTA_UNSUPPORTED_CLUSTERING_COLUMN_PREDICATES` error. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

## Predicate Restrictions

Commands on Liquid tables require that the predicate references only the table's clustering columns. The following restrictions apply:

- **NON_CLUSTERING_COLUMN** – The predicate references a column that is not a clustering column. Only clustering columns are allowed.
- **NO_CLUSTERING_COLUMNS** – The command is not supported on Liquid tables that have no clustering columns defined.
- **UNRESOLVED_COLUMN** – The predicate references a column that cannot be resolved among the available clustering columns.
- **UNSUPPORTED_EXPRESSION** – The predicate uses an expression type (e.g., subquery, function call) that is not supported. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

### Example

```sql
-- Liquid table 'orders' clustered on column 'order_date'
DELETE FROM orders WHERE customer_id = 123;  -- error: customer_id is not a clustering column
```

This would raise `DELTA_UNSUPPORTED_CLUSTERING_COLUMN_PREDICATES` with subclass `NON_CLUSTERING_COLUMN`.

## Error Class Details

| Error Class | SQLSTATE | Description |
|-------------|----------|-------------|
| `DELTA_UNSUPPORTED_CLUSTERING_COLUMN_PREDICATES` | 0A000 | The command for Liquid tables does not support the provided predicates. |

All four subclasses are described above. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

## Usage Notes

- To avoid the `NON_CLUSTERING_COLUMN` error, ensure `WHERE` clauses on `DELETE`, `UPDATE`, and `MERGE` refer only to the table's clustering columns.
- Liquid tables must have at least one clustering column to support these write commands; otherwise the `NO_CLUSTERING_COLUMNS` error occurs.
- Complex expressions in predicates may trigger `UNSUPPORTED_EXPRESSION`.

## Related Concepts

- [Liquid Clustering](/concepts/liquid-clustering.md) – The data organization technique used by Liquid tables.
- [Clustering columns](/concepts/clustering-columns.md) – The columns used to define data organization for Liquid tables.
- DELETE, UPDATE, MERGE – Write commands affected by the predicate restriction.
- [Delta Lake](/concepts/delta-lake.md) – The underlying storage format for Liquid tables.
- Data Skipping – Performance benefit enabled by clustering.

## Sources

- delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md

# Citations

1. [delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md](/references/delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws-b9f8e20f.md)
