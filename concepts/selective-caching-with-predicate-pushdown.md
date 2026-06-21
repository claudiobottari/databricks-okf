---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2fbbe9325dcae71768b45095cbaac3b1ad8c339578b9c4bf318b481ffc3327a4
  pageDirectory: concepts
  sources:
    - cache-select-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - selective-caching-with-predicate-pushdown
    - SCWPP
    - Predicate Pushdown
    - predicate pushdown
  citations:
    - file: cache-select-databricks-on-aws.md
title: Selective Caching with Predicate Pushdown
description: Technique of caching only a subset of columns and rows from a table using column lists and WHERE predicates, enabling subsequent queries to avoid scanning original files.
tags:
  - databricks
  - caching
  - optimization
  - query-tuning
timestamp: "2026-06-19T17:42:39.957Z"
---

## Selective Caching with Predicate Pushdown

**Selective Caching with Predicate Pushdown** is a data caching technique that stores only a subset of rows and columns from a [Delta Table](/concepts/delta-lake-table.md) or Parquet table into the [Disk Cache](/concepts/databricks-disk-cache.md). By combining column projection with a `WHERE` predicate, subsequent queries that access the same filtered data can read directly from the cache instead of scanning the original files, reducing I/O and improving performance. ^[cache-select-databricks-on-aws.md]

### Overview

The `CACHE SELECT` statement implements selective caching. It accepts a comma‑separated list of column names and an optional `boolean_expression` in a `WHERE` clause. The expression acts as a **predicate pushdown** filter: only the rows that satisfy the condition are cached, along with only the specified columns. This targeted caching is especially useful for frequently accessed subsets of large tables. ^[cache-select-databricks-on-aws.md]

### Syntax

```sql
CACHE SELECT column_name [, ...] FROM table_name [ WHERE boolean_expression ]
```

- `column_name [, ...]` – Specifies which columns to cache.
- `boolean_expression` – A predicate that limits the cached rows to those matching the condition.

### Applicability

`CACHE SELECT` works only with **Delta tables** and **Parquet tables**. Views are also supported, but the underlying query expansion must be a simple `SELECT` (as described above). Nested subqueries, joins, aggregations, or complex expressions are not allowed in the cached query. ^[cache-select-databricks-on-aws.md]

### Related Concepts

- [Disk Cache](/concepts/databricks-disk-cache.md) – The underlying storage layer where cached data is held.
- [Predicate Pushdown](/concepts/selective-caching-with-predicate-pushdown.md) – The general technique of applying filters early in the data access path.
- [Delta Table](/concepts/delta-lake-table.md) – A transactional table format that supports caching.
- Parquet – A columnar storage format that works with `CACHE SELECT`.
- [Query Optimization](/concepts/trace-query-performance-optimization.md) – Broader strategies for speeding up analytical queries.

## Sources

- cache-select-databricks-on-aws.md

# Citations

1. [cache-select-databricks-on-aws.md](/references/cache-select-databricks-on-aws-6988f8be.md)
