---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f45cd1221e34f552945350ce73de702e035e83ca064697a550fce522e8680bde
  pageDirectory: concepts
  sources:
    - cache-select-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cache-select
    - CACHE SELECT command
    - cache-select-databricks-sql
    - CS(S
  citations:
    - file: cache-select-databricks-on-aws.md
title: CACHE SELECT
description: A Databricks SQL construct that caches data accessed by a simple SELECT query in the disk cache, supporting column and row subsets.
tags:
  - sql
  - caching
  - databricks
  - optimization
timestamp: "2026-06-18T14:34:58.657Z"
---

---
title: CACHE SELECT
summary: Command that caches data accessed by a SELECT query in the Databricks disk cache, allowing column and row subset selection.
sources:
  - cache-select-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:55:22.793Z"
updatedAt: "2026-06-18T10:55:22.793Z"
tags:
  - sql
  - caching
  - databricks
aliases:
  - cache-select
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# CACHE SELECT

**CACHE SELECT** is a SQL command in Databricks that caches the data accessed by a specified simple `SELECT` query in the [disk cache]. This enables subsequent queries to avoid scanning the original files as much as possible, improving query performance for repeated accesses.^[cache-select-databricks-on-aws.md]

## Overview

`CACHE SELECT` allows you to selectively cache a subset of columns and rows from a table by providing a list of column names and an optional `WHERE` predicate. This construct is applicable only to [Delta tables](/concepts/delta-lake-table.md) and Parquet tables. Views are also supported, but the expanded queries are restricted to the simple queries described below.^[cache-select-databricks-on-aws.md]

## Syntax

```sql
CACHE SELECT column_name [, ...] FROM table_name [ WHERE boolean_expression ]
```

^[cache-select-databricks-on-aws.md]

## Parameters

- **`column_name`**: One or more columns to be cached. Specifying a subset of columns allows you to cache only the data you need, reducing cache memory usage.
- **`table_name`**: The name of the table to cache data from. Must be a Delta table or Parquet table.
- **`WHERE boolean_expression`**: An optional predicate to select a subset of rows for caching.

## Supported Data Sources

`CACHE SELECT` is applicable only to:
- [Delta tables](/concepts/delta-lake-table.md)
- Parquet tables
- Views (with restrictions on the expanded queries)

^[cache-select-databricks-on-aws.md]

## Behavior

When `CACHE SELECT` is executed, the data matching the specified columns and optional predicate is loaded into the disk cache. Subsequent queries that access the same data can read from the cache instead of scanning the original files, resulting in faster query execution.

## Related Concepts

- [Disk cache](/concepts/databricks-disk-cache.md) — The underlying caching mechanism that stores data on local SSDs
- [Delta tables](/concepts/delta-lake-table.md) — The primary table format supported by CACHE SELECT
- Parquet tables — Another supported file format for caching
- Query performance optimization — General strategies for improving query speed

## Sources

- cache-select-databricks-on-aws.md

# Citations

1. [cache-select-databricks-on-aws.md](/references/cache-select-databricks-on-aws-6988f8be.md)
