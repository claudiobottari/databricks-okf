---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f562b3aa81e7290e089ed4eef634bd03aa26d0c969808b535c82aa7daffd2068
  pageDirectory: concepts
  sources:
    - cache-select-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cache-select-with-views
    - CSWV
  citations:
    - file: cache-select-databricks-on-aws.md
title: CACHE SELECT with Views
description: Support for caching views with CACHE SELECT, but with the restriction that the expanded view query must be a simple SELECT as defined by the syntax.
tags:
  - views
  - caching
  - sql
  - databricks
timestamp: "2026-06-18T14:35:16.144Z"
---

# CACHE SELECT with Views

**CACHE SELECT with Views** refers to the use of the `CACHE SELECT` statement on views in Databricks. The `CACHE SELECT` construct populates the [disk cache](https://docs.databricks.com/aws/en/optimizations/disk-cache) with data accessed by a specified simple `SELECT` query, enabling subsequent queries to avoid scanning the original files. While this construct is primarily applicable to Delta tables and Parquet tables, views are also supported with a specific restriction: the expanded query from the view definition must itself be a simple `SELECT` query. ^[cache-select-databricks-on-aws.md]

## Syntax and Usage

The basic syntax for `CACHE SELECT` is:

```sql
CACHE SELECT column_name [, ...] FROM table_name [ WHERE boolean_expression ]
```

When using the statement with a view, `table_name` can be replaced with the view name, provided the view’s underlying query expands to a simple `SELECT`. You can choose:

- A subset of columns to cache by providing a comma-separated list of column names.
- A subset of rows to cache by providing a `WHERE` predicate. ^[cache-select-databricks-on-aws.md]

## Restrictions on View Expansion

The only restriction that applies to views is that the expanded query – the query produced by resolving the view definition – must be a simple `SELECT` query. This is the same requirement that applies to a direct `CACHE SELECT` on a table. Views whose expanded query contains more complex constructs (for example, joins, subqueries, or aggregations) are not eligible for caching through this mechanism. ^[cache-select-databricks-on-aws.md]

## Related Concepts

- [Disk Cache](/concepts/databricks-disk-cache.md) — The underlying caching mechanism that `CACHE SELECT` populates
- [Delta Tables](/concepts/delta-lake-table.md) — One of the primary table types supported by `CACHE SELECT`
- Parquet Tables — Another supported table format for caching
- [CACHE SELECT](/concepts/cache-select.md) — The core caching statement and its general syntax
- [Query Optimization](/concepts/trace-query-performance-optimization.md) — Performance tuning techniques for Databricks SQL
- Views — Logical tables defined by SQL queries

## Sources

- cache-select-databricks-on-aws.md

# Citations

1. [cache-select-databricks-on-aws.md](/references/cache-select-databricks-on-aws-6988f8be.md)
