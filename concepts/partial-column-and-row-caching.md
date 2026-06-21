---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 166aa00d4bbb5951fa7c4740633b38763eb0b835f1882643d78b078077faa09e
  pageDirectory: concepts
  sources:
    - cache-select-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - partial-column-and-row-caching
    - Row Caching and Partial Column
    - PCARC
  citations:
    - file: cache-select-databricks-on-aws.md
title: Partial Column and Row Caching
description: The ability to cache only a subset of columns and rows from a table using column lists and WHERE predicates in the CACHE SELECT statement.
tags:
  - databricks
  - caching
  - sql
  - optimization
timestamp: "2026-06-19T09:12:00.929Z"
---

# Partial Column and Row Caching

**Partial Column and Row Caching** refers to the ability to cache only a selected subset of columns and rows from a table into the [disk cache] ([Disk Cache](/concepts/databricks-disk-cache.md)) using the `CACHE SELECT` statement. This approach reduces the amount of data cached compared to caching entire tables, leading to more efficient cache usage and faster subsequent queries that access the same data.

## Overview

The `CACHE SELECT` statement in Databricks SQL allows you to cache the results of a simple `SELECT` query that specifies a subset of columns and an optional row‑filtering predicate. The cached data is stored in the local disk cache, enabling later queries to avoid scanning the original source files. This construct is applicable only to [Delta tables](/concepts/delta-lake-table.md) and Parquet tables. Views are also supported, but the expanded queries must remain simple (i.e., no joins, aggregations, or subqueries). ^[cache-select-databricks-on-aws.md]

## Usage

The syntax is:

```sql
CACHE SELECT column_name [, ...] FROM table_name [ WHERE boolean_expression ]
```

- **Column list**: A comma‑separated list of columns to cache. Only these columns are stored in the disk cache.
- **Table name**: The name of the Delta or Parquet table.
- **WHERE clause** (optional): A boolean expression that filters which rows are cached. Only rows satisfying the predicate are stored.

After a `CACHE SELECT` statement executes, subsequent queries that reference the same columns and satisfy the same (or a subset of) row filters may read directly from the cache without scanning the original files. ^[cache-select-databricks-on-aws.md]

## Example

The following example caches only the `device_id` and `device_type` columns from the `devices` table, restricting the cached rows to those where the type is `sensor`:

```sql
CACHE SELECT device_id, device_type FROM devices WHERE device_type = 'sensor';
```

After this statement, queries that request `device_id` or `device_type` from `devices` and include a filter on `device_type = 'sensor'` can leverage the cached data. ^[cache-select-databricks-on-aws.md]

## Limitations

- The `SELECT` query must be **simple**: it cannot contain joins, aggregations, subqueries, or complex expressions.
- Supported only for [Delta tables](/concepts/delta-lake-table.md) and Parquet tables (and views that expand to such simple queries).
- The cache is local to each node and is not shared across clusters. Cache contents are automatically invalidated when the underlying data changes. ^[cache-select-databricks-on-aws.md]

## Related Concepts

- [Disk Cache](/concepts/databricks-disk-cache.md) – The underlying local storage cache on Databricks compute nodes.
- CACHE SELECT – Full Table Caching – Caching an entire table without column or row subsetting.
- [Delta Lake Caching](/concepts/delta-table-caching.md) – Broader caching strategies for Delta Lake.
- Cache Hinting – Query hints that affect caching behavior.
- Performance Optimization with Caching – Best practices for using caching effectively.

## Sources

- cache-select-databricks-on-aws.md

# Citations

1. [cache-select-databricks-on-aws.md](/references/cache-select-databricks-on-aws-6988f8be.md)
