---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e2437a0217a9ca79649f83aff1b93bc0bf768797bc65c5c8ddb7c4a8b977b7ca
  pageDirectory: concepts
  sources:
    - cache-select-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-table-caching
    - DTC
    - Delta Lake Caching
    - Caching
  citations:
    - file: cache-select-databricks-on-aws.md
title: Delta Table Caching
description: The application of CACHE SELECT specifically to Delta Lake tables, enabling faster subsequent queries by avoiding full file scans.
tags:
  - delta-lake
  - caching
  - databricks
  - query-optimization
timestamp: "2026-06-18T14:35:19.875Z"
---

# Delta Table Caching

**Delta Table Caching** refers to the practice of explicitly caching the data accessed by a simple `SELECT` query from a Delta table (or Parquet table) in the Databricks disk cache, using the `CACHE SELECT` SQL construct. This enables subsequent queries to avoid re‑scanning the original source files, improving query performance for repeated access patterns. ^[cache-select-databricks-on-aws.md]

## Overview

The `CACHE SELECT` statement caches the results of a simple `SELECT` query in the [disk cache](https://docs.databricks.com/aws/en/optimizations/disk-cache). You can select a subset of columns by providing a list of column names and restrict rows by providing a predicate in a `WHERE` clause. This construct is applicable only to [Delta tables](/concepts/delta-lake-table.md) and Parquet tables. Views are also supported, but the expanded queries are restricted to the same simple query form. ^[cache-select-databricks-on-aws.md]

## Syntax

```sql
CACHE SELECT column_name [, ...] FROM table_name [ WHERE boolean_expression ]
```

^[cache-select-databricks-on-aws.md]

## How It Works

When you execute `CACHE SELECT`, Databricks caches only the specific columns and rows requested by the query, rather than the entire table. This targeted caching reduces the storage footprint of the cache and allows you to optimize for common access patterns. The cached data resides in the cluster's local disk cache, which is automatically managed and evicted based on an LRU (Least Recently Used) policy when space is needed.

## Benefits

- **Improved query performance**: Subsequent queries that access the same columns and rows can read from the fast local disk cache instead of scanning remote storage files. ^[cache-select-databricks-on-aws.md]  
- **Reduced I/O**: Avoids repeatedly reading data from cloud storage (S3, ADLS, GCS), lowering costs and reducing latency.  
- **Selective caching**: You cache only the data you actually need, preserving cache capacity for other workloads.

## Applicability

The `CACHE SELECT` construct is designed for:

- [Delta tables](/concepts/delta-lake-table.md)
- Parquet tables
- Views (with the restriction that the expanded query must be a simple `SELECT`)

^[cache-select-databricks-on-aws.md]

## Limitations

- The construct only supports simple `SELECT` queries — no joins, aggregations, subqueries, or complex expressions.
- Views are supported, but the underlying query expansion must still conform to the simple SELECT restrictions.
- The cache is local to the cluster; data cached on one cluster is not available on another.
- Cached data is lost when the cluster is terminated or restarted.

## Related Concepts

- [Disk cache](/concepts/databricks-disk-cache.md) — The local SSD‑based caching layer on cluster nodes
- [Delta Cache](/concepts/delta-cache.md) — Automatic caching of Parquet data files in Delta Lake
- Query optimization — Broader strategies for improving query performance
- Databricks SQL optimization — Performance tuning for SQL workloads

## Sources

- cache-select-databricks-on-aws.md

# Citations

1. [cache-select-databricks-on-aws.md](/references/cache-select-databricks-on-aws-6988f8be.md)
