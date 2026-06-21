---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 193d5cfe56cb5c6a38cb1878f0b42d1f5c2dfc020e6aaea0e1a4958aaa3fd9e7
  pageDirectory: concepts
  sources:
    - cache-select-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cache-select-databricks-sql
    - CS(S
  citations:
    - file: cache-select-databricks-on-aws.md
title: CACHE SELECT (Databricks SQL)
description: SQL command that caches data from a SELECT query into the Databricks disk cache, supporting column and row subset selection for Delta and Parquet tables.
tags:
  - databricks
  - sql
  - caching
  - optimization
timestamp: "2026-06-19T17:42:25.821Z"
---

Here is the wiki page for "CACHE SELECT (Databricks SQL)", written solely based on the provided source material.

---

## CACHE SELECT (Databricks SQL)

**CACHE SELECT** is a SQL command in Databricks that caches the data accessed by a specified simple `SELECT` query into the local [disk cache](/concepts/databricks-disk-cache.md). By caching frequently accessed data, subsequent queries can read from the cache instead of re-scanning the original files, improving query performance. ^[cache-select-databricks-on-aws.md]

## Syntax

```sql
CACHE SELECT column_name [, ...] FROM table_name [ WHERE boolean_expression ]
```

## Details

The command allows you to cache only a subset of columns by listing the desired column names, and a subset of rows by providing an optional `WHERE` clause with a `boolean_expression`. This targeted caching helps optimize storage and memory usage. ^[cache-select-databricks-on-aws.md]

The `CACHE SELECT` construct is applicable only to [Delta tables](/concepts/delta-lake-table.md) and Parquet tables. Views are also supported, but when using views, the expanded underlying queries must meet the same restrictions — they must be simple `SELECT` queries. ^[cache-select-databricks-on-aws.md]

## Related Concepts

- [Disk Cache](/concepts/databricks-disk-cache.md)
- [Delta Tables](/concepts/delta-lake-table.md)
- Parquet Tables
- [Query Optimization](/concepts/trace-query-performance-optimization.md)

## Sources

- cache-select-databricks-on-aws.md

# Citations

1. [cache-select-databricks-on-aws.md](/references/cache-select-databricks-on-aws-6988f8be.md)
