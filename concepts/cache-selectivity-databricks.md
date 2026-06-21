---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 53962730aed4f754980d5ece5417560c67a01f6873e514a322ad6aaeb28881f0
  pageDirectory: concepts
  sources:
    - cache-select-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cache-selectivity-databricks
    - CS(
  citations:
    - file: cache-select-databricks-on-aws.md
title: Cache Selectivity (Databricks)
description: The ability to cache only a subset of columns (via column list) and rows (via WHERE predicate) from a table, reducing cache footprint and improving performance.
tags:
  - databricks
  - caching
  - optimization
  - query-tuning
timestamp: "2026-06-19T14:11:15.971Z"
---

# Cache Selectivity (Databricks)

**Cache Selectivity** refers to the ability of the `CACHE SELECT` command in Databricks SQL to cache only a subset of columns and rows from a table into the [disk cache](/concepts/databricks-disk-cache.md). By choosing which data to cache, you reduce the amount of storage consumed by the cache and speed up subsequent queries that access the same data patterns.

## Overview

`CACHE SELECT` is a SQL construct that caches the results of a simple `SELECT` query on [Delta tables](/concepts/delta-lake-table.md) or Parquet tables into Databricks' disk cache. Unlike caching an entire table, cache selectivity lets you specify:

- A subset of **columns** – by listing the column names after `SELECT`.
- A subset of **rows** – by providing a `WHERE` clause with a boolean expression.

This selective caching enables subsequent queries to avoid scanning the original files as much as possible, improving performance for repeated access patterns.^[cache-select-databricks-on-aws.md]

## Syntax

The syntax is:

```sql
CACHE SELECT column_name [, ...]
FROM table_name
[ WHERE boolean_expression ]
```

- `column_name [, ...]` – a comma-separated list of columns to cache. If omitted, all columns are cached.
- `table_name` – the name of a Delta table or Parquet table (views are also supported, but the expanded query must be a simple `SELECT`).
- `WHERE boolean_expression` – an optional predicate to filter which rows are cached.

## How Cache Selectivity Works

1. When you execute `CACHE SELECT`, Databricks reads the specified columns and rows from the underlying files and stores them in the disk cache.
2. Subsequent queries that access the same cached columns and rows (or a subset thereof) retrieve the data from the cache instead of re‑scanning the source files.
3. The cache is local to the compute node and persists across queries as long as the node is running.

Because only the selected columns and rows are cached, the cache uses less disk space and can be populated faster. The trade‑off is that queries needing other columns or rows will still read the original files.

## Usage

Typical use cases include:

- **Frequent sub‑queries** – if a dashboard repeatedly queries the same few columns of a large Delta table, cache only those columns.
- **Filtered access patterns** – if most queries filter on a common predicate (e.g., `date > '2025-01-01'`), cache only the relevant rows.
- **Accelerating iterative exploration** – during ad‑hoc analysis, cache a focused slice of the data to speed up repeated queries.

### Example

```sql
-- Cache only the 'id', 'name', and 'status' columns
-- for rows where status = 'active'.
CACHE SELECT id, name, status
FROM user_events
WHERE status = 'active';
```

After this command, a query like `SELECT name FROM user_events WHERE status = 'active'` will read from the cache rather than scanning the entire table.

## Limitations

- The `CACHE SELECT` command only works with simple `SELECT` queries. Aggregations, joins, subqueries, and other complex expressions are not allowed.
- Views are supported, but the underlying query must be a simple `SELECT` as described above.
- The cache is not automatically refreshed when the underlying table is updated; you must re‑run `CACHE SELECT` to reflect new data.

## Related Concepts

- [Disk cache](/concepts/databricks-disk-cache.md) – the underlying caching mechanism used by Databricks.
- [Delta tables](/concepts/delta-lake-table.md) – the primary table format that supports `CACHE SELECT`.
- Parquet tables – also supported by `CACHE SELECT`.
- [Delta Cache](/concepts/delta-cache.md) – another name for the disk cache feature.
- SQL language manual – reference for DML and caching commands.

## Sources

- cache-select-databricks-on-aws.md

# Citations

1. [cache-select-databricks-on-aws.md](/references/cache-select-databricks-on-aws-6988f8be.md)
