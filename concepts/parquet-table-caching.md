---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3982ed7f297629d0b786dc8a058d79f7d37909df25b463c7260c2b1b9ed01081
  pageDirectory: concepts
  sources:
    - cache-select-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - parquet-table-caching
    - PTC
  citations:
    - file: cache-select-databricks-on-aws.md
title: Parquet Table Caching
description: Caching support for Parquet tables in Databricks using the CACHE SELECT command.
tags:
  - parquet
  - caching
  - optimization
timestamp: "2026-06-18T10:55:50.134Z"
---

# Parquet Table Caching

**Parquet Table Caching** refers to the use of the `CACHE SELECT` statement in Databricks to explicitly cache data from a Parquet table into the [Disk Cache](/concepts/databricks-disk-cache.md). This enables subsequent queries to avoid re‑scanning the underlying Parquet files, reducing I/O and improving query performance for repeated access patterns. The feature is also supported for [Delta tables](/concepts/delta-lake-table.md), views, and other file‑based formats. ^[cache-select-databricks-on-aws.md]

## Syntax and Usage

The `CACHE SELECT` statement caches the result of a simple query that reads from a table. You can optionally restrict the cached data to a subset of columns and rows:

```sql
CACHE SELECT column_name [, ...] FROM table_name [ WHERE boolean_expression ]
```

- `table_name` – the name of the Parquet or Delta table to cache.
- `column_name [, ...]` – an optional comma‑separated list of columns to cache. If omitted, all columns are cached.
- `WHERE boolean_expression` – an optional predicate that selects only the rows that satisfy the condition.

The statement is valid only for simple `SELECT` queries; it does not support joins, aggregations, subqueries, or other complex expressions. Views are supported, but the expanded query must still be a simple selection. ^[cache-select-databricks-on-aws.md]

## Applicability

`CACHE SELECT` is applicable to:
- [Delta tables](/concepts/delta-lake-table.md)
- Parquet tables
- Views that expand to simple `SELECT` queries on the above table types

It is supported on Databricks clusters that have the disk cache enabled. ^[cache-select-databricks-on-aws.md]

## How It Works

When a `CACHE SELECT` statement is executed, the data that satisfies the query (all columns if none are specified, or only the listed columns; all rows if no `WHERE` clause, or only the filtered rows) is written to the cluster’s local SSD‑based disk cache. Subsequent queries that touch the same data will read from the cache instead of the original Parquet files, bypassing remote storage and decompression overhead. ^[cache-select-databricks-on-aws.md]

The cache is maintained per cluster and is not shared across clusters. It is automatically invalidated when the underlying data in the table changes (e.g., after an `INSERT`, `UPDATE`, `DELETE`, or `MERGE`). ^[cache-select-databricks-on-aws.md]

## Performance Considerations

- **Scan avoidance**: By caching only the columns and rows you frequently access, you reduce the amount of data scanned in subsequent queries.
- **Cache management**: The disk cache evicts least‑recently‑used blocks when space is constrained. `CACHE SELECT` does not pin data; it only populates the cache so that future queries are more likely to hit it.
- **Cost trade‑off**: Caching consumes local SSD space. Use it for frequently accessed, relatively static subsets of data.

## Limitations

- Only simple `SELECT` queries are supported. Complex transformations, joins, or aggregations are not allowed.
- The cache is local to the cluster. If the cluster is restarted or terminated, the cached data is lost and must be re‑cached.
- The cache is automatically invalidated when the underlying table is modified. Partial updates to cached rows may cause the entire cached partition to be invalidated, depending on the table’s partitioning scheme.

## Related Concepts

- [Disk Cache](/concepts/databricks-disk-cache.md) – the underlying SSD‑based caching layer on Databricks clusters.
- [Delta Table Caching](/concepts/delta-table-caching.md) – caching strategies specific to Delta Lake tables.
- [CACHE SELECT](/concepts/cache-select.md) – the SQL statement used to populate the cache.
- Parquet – the columnar storage format that benefits from caching.
- [Query Performance Optimization](/concepts/trace-query-performance-optimization.md) – broader topic of improving query speed.

## Sources

- cache-select-databricks-on-aws.md

# Citations

1. [cache-select-databricks-on-aws.md](/references/cache-select-databricks-on-aws-6988f8be.md)
