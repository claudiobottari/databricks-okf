---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 28885e4b68e38dc75f451918c314a074299b00cbc6e244c6a4e5a71189f61995
  pageDirectory: concepts
  sources:
    - cache-select-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-cache
  citations:
    - file: cache-select-databricks-on-aws.md
title: Delta Cache
description: A Databricks caching feature for Delta Lake tables that materializes selected query results in the disk cache to avoid rescanning source files.
tags:
  - databricks
  - delta-lake
  - caching
  - optimization
timestamp: "2026-06-19T14:11:11.559Z"
---

# Delta Cache

**Delta Cache** is a Databricks feature that caches the data accessed by a simple `SELECT` query into the disk cache. By caching a subset of columns and rows, subsequent queries can avoid scanning the original files, improving performance for repeated access patterns. This construct is applicable only to [Delta tables](/concepts/delta-lake-table.md) and Parquet tables. ^[cache-select-databricks-on-aws.md]

## Syntax

```
CACHE SELECT column_name [, ...] FROM table_name [ WHERE boolean_expression ]
```

The statement allows you to choose a subset of columns to cache by providing a list of column names, and a subset of rows by providing a `WHERE` predicate. ^[cache-select-databricks-on-aws.md]

## Applicability

- **Delta tables** and **Parquet tables** are directly supported.
- **Views** are also supported, but the expanded query must be restricted to the same simple query form (a `SELECT` with optional column list and predicate). Complex views that involve joins, aggregations, or subqueries are not allowed. ^[cache-select-databricks-on-aws.md]

## Related Concepts

- [Disk Cache](/concepts/databricks-disk-cache.md) — the underlying caching mechanism on worker nodes.
- [Delta Tables](/concepts/delta-lake-table.md) — the primary table format supported by Delta Cache.
- Parquet Tables — another supported file format.
- Caching in Databricks — broader strategies for query acceleration.
- [Query Optimization](/concepts/trace-query-performance-optimization.md) — techniques for improving query performance.

## Sources

- cache-select-databricks-on-aws.md

# Citations

1. [cache-select-databricks-on-aws.md](/references/cache-select-databricks-on-aws-6988f8be.md)
