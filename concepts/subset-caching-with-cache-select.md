---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 226ba4a77bd1d5e576cd25eb9450c8848e7fe62f9856dc415c26b471c346b1bb
  pageDirectory: concepts
  sources:
    - cache-select-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - subset-caching-with-cache-select
    - SCWCS
  citations:
    - file: cache-select-databricks-on-aws.md
title: Subset Caching with CACHE SELECT
description: Technique of caching only a subset of columns and/or rows from a table by specifying column names and a WHERE predicate in CACHE SELECT.
tags:
  - caching
  - optimization
  - sql
timestamp: "2026-06-18T10:55:37.597Z"
---

# Subset Caching with CACHE SELECT

**Subset Caching with CACHE SELECT** is a Databricks SQL feature that caches the data accessed by a simple `SELECT` query in the [disk cache](https://docs.databricks.com/aws/en/optimizations/disk-cache). It allows you to cache only a subset of columns and rows from a table, enabling subsequent queries to avoid scanning the original files as much as possible. This construct is applicable only to Delta tables and Parquet tables. Views are also supported, but the expanded queries are restricted to simple queries. ^[cache-select-databricks-on-aws.md]

## Syntax

```sql
CACHE SELECT column_name [, ...] FROM table_name [ WHERE boolean_expression ]
```

^[cache-select-databricks-on-aws.md]

## How It Works

The `CACHE SELECT` statement caches the results of a simple `SELECT` query in the Databricks disk cache. You can choose a subset of columns to be cached by providing a list of column names, and choose a subset of rows by providing a predicate in a `WHERE` clause. ^[cache-select-databricks-on-aws.md]

When subsequent queries access the same data, they can read from the cache instead of scanning the original files, improving query performance. This is particularly useful for frequently accessed subsets of large tables.

## Supported Table Formats

- [Delta Tables](/concepts/delta-lake-table.md) — Fully supported
- Parquet Tables — Fully supported
- Views — Supported, but the expanded queries are restricted to simple queries as described above

^[cache-select-databricks-on-aws.md]

## Use Cases

- **Frequently queried subsets**: Cache a commonly used subset of columns and rows from a large table to speed up repeated queries.
- **Dashboard acceleration**: Pre-cache the data needed by dashboards that query the same subset repeatedly.
- **ETL optimization**: Cache intermediate results that are accessed multiple times during a pipeline.

## Related Concepts

- [Disk Cache](/concepts/databricks-disk-cache.md) — The underlying caching mechanism that stores data on local SSDs attached to cluster nodes
- [Delta Cache](/concepts/delta-cache.md) — The broader caching feature for Delta tables
- [Query Optimization](/concepts/trace-query-performance-optimization.md) — General techniques for improving query performance in Databricks
- [Delta Tables](/concepts/delta-lake-table.md) — A table format supported by CACHE SELECT
- Parquet Tables — Another supported table format

## Sources

- cache-select-databricks-on-aws.md

# Citations

1. [cache-select-databricks-on-aws.md](/references/cache-select-databricks-on-aws-6988f8be.md)
