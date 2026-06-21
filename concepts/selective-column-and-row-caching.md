---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3ecb33c6a34a968cf80b45fe1c7d48935af6ab7a67c5dbaad664ce52a397981c
  pageDirectory: concepts
  sources:
    - cache-select-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - selective-column-and-row-caching
    - Row Caching and Selective Column
    - SCARC
  citations:
    - file: cache-select-databricks-on-aws.md
title: Selective Column and Row Caching
description: The ability to cache only a subset of columns (via column list) and rows (via WHERE predicate) in the disk cache, minimizing scan overhead.
tags:
  - caching
  - sql
  - optimization
  - query-tuning
timestamp: "2026-06-18T14:35:07.229Z"
---

# Selective Column and Row Caching

**Selective Column and Row Caching** refers to the ability to cache only a subset of columns and rows from a [Delta table](/concepts/delta-lake-table.md) or Parquet table in the [disk cache](/concepts/databricks-disk-cache.md), using a `CACHE SELECT` statement. This approach optimizes memory and disk usage by storing only the data that subsequent queries are likely to need, and avoids scanning the original files repeatedly. ^[cache-select-databricks-on-aws.md]

## Overview

The `CACHE SELECT` construct allows you to define a lightweight materialized view that persists a filtered portion of a table in the disk cache. By choosing a list of columns and a row predicate (via a `WHERE` clause), you can reduce the cache footprint and speed up repeated access patterns. The cache is maintained until it is explicitly evicted or the cluster is restarted. This construct is applicable only to [Delta tables](/concepts/delta-lake-table.md) and Parquet tables; views are also supported, but the expanded query must conform to the same simple `SELECT` restrictions. ^[cache-select-databricks-on-aws.md]

## Syntax

```sql
CACHE SELECT column_name [, ...] FROM table_name [ WHERE boolean_expression ]
```

- **column_name**: One or more columns to include in the cache. If omitted, all columns are cached.
- **table_name**: The name of the Delta or Parquet table (or a view that resolves to such a table).
- **WHERE boolean_expression**: A predicate that selects a subset of rows. If omitted, all rows are cached.

The query must be a simple `SELECT` — no joins, aggregations, subqueries, or complex expressions are allowed. ^[cache-select-databricks-on-aws.md]

## Applicability

- **Supported table formats**: Delta Lake tables, Parquet tables.
- **Views**: Allowed only if the expanded query is a simple `SELECT` meeting the same restrictions.
- **Not supported**: Other formats (e.g., CSV, JSON, ORC) or queries with joins, aggregations, or subqueries.

## Related Concepts

- [Disk Cache](/concepts/databricks-disk-cache.md) – The underlying storage layer for cached data.
- [Delta Table](/concepts/delta-lake-table.md) – The primary target format for selective caching.
- Parquet Table – Another supported format.
- Cache Management – Commands to list and evict cached data.
- Query Optimization with Caching – Best practices for using cached data to accelerate workloads.

## Sources

- cache-select-databricks-on-aws.md

# Citations

1. [cache-select-databricks-on-aws.md](/references/cache-select-databricks-on-aws-6988f8be.md)
