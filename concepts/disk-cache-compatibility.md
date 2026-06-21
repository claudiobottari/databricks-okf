---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 035f2a4ad291294d811ac5ef9fbaf4990941b104bebdd2b959ba5b2c6272675f
  pageDirectory: concepts
  sources:
    - cache-select-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - disk-cache-compatibility
    - DCC
  citations:
    - file: cache-select-databricks-on-aws.md
title: Disk Cache Compatibility
description: The Databricks disk cache (and therefore CACHE SELECT) is applicable only to Delta tables and Parquet tables; views are supported but with expanded query restrictions.
tags:
  - databricks
  - caching
  - delta-lake
  - parquet
timestamp: "2026-06-19T17:42:33.916Z"
---

# Disk Cache Compatibility

**Disk Cache Compatibility** refers to the types of tables, query constructs, and data formats that are supported by the Databricks disk cache feature for accelerating query performance.

## Supported Table Types

The disk cache can be used with [Delta Tables](/concepts/delta-lake-table.md) and Parquet Tables. These are the only table formats that support the `CACHE SELECT` operation. ^[cache-select-databricks-on-aws.md]

## Supported Query Constructs

The `CACHE SELECT` statement caches data accessed by a simple `SELECT` query. You can specify a subset of columns to cache by providing a list of column names, and you can choose a subset of rows by providing a predicate (`WHERE` clause). This enables subsequent queries to avoid scanning the original files as much as possible. ^[cache-select-databricks-on-aws.md]

### Views

Views are also supported for disk caching, but with a restriction: the expanded queries from the view must conform to the simple query requirements. Views that expand to complex queries or constructs beyond simple `SELECT` statements are not compatible. ^[cache-select-databricks-on-aws.md]

## Syntax Requirements

The `CACHE SELECT` construct is applicable only to simple `SELECT` queries. Complex queries involving joins, subqueries, aggregations, or other advanced SQL constructs may not be compatible with the disk cache.

```sql
CACHE SELECT column_name [, ...] FROM table_name [ WHERE boolean_expression ]
```

## Unsupported Table Formats

The disk cache does not support table formats other than Delta and Parquet. Tables in other formats cannot be cached using the `CACHE SELECT` statement. ^[cache-select-databricks-on-aws.md]

## Related Concepts

- [Disk Cache](/concepts/databricks-disk-cache.md) – The underlying caching mechanism for accelerating query performance.
- [Delta Lake](/concepts/delta-lake.md) – The Delta table format supported by the disk cache.
- Parquet File Format – The Parquet file format supported by the disk cache.
- [CACHE SELECT](/concepts/cache-select.md) – The SQL statement for manually populating the disk cache.
- Query Optimization on Databricks – General optimization strategies for improving query performance.

## Sources

- cache-select-databricks-on-aws.md

# Citations

1. [cache-select-databricks-on-aws.md](/references/cache-select-databricks-on-aws-6988f8be.md)
