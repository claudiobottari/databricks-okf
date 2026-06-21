---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a80e113078740dcd6f3c6dadb75af8cd22506281965f9b657765426bf6805ecc
  pageDirectory: concepts
  sources:
    - cache-select-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-cache-supported-data-sources
    - DCSDS
  citations:
    - file: cache-select-databricks-on-aws.md
title: Delta Cache Supported Data Sources
description: The Delta Cache (disk cache) supports Delta tables, Parquet tables, and views, with views restricted to simple queries upon expansion.
tags:
  - databricks
  - delta-lake
  - caching
  - compatibility
timestamp: "2026-06-19T09:12:19.726Z"
---

# Delta Cache Supported Data Sources

**Delta Cache Supported Data Sources** describes the types of tabular data that the [Delta Cache](/concepts/delta-cache.md) (disk cache) can populate using the `CACHE SELECT` statement. The `CACHE SELECT` command caches the results of a simple `SELECT` query so that subsequent queries can avoid scanning the original files. ^[cache-select-databricks-on-aws.md]

## Supported Table Formats

`CACHE SELECT` is applicable only to [Delta tables](/concepts/delta-lake-table.md) and Parquet tables. These are the two table formats whose underlying data can be stored in the disk cache when explicitly cached via this command. ^[cache-select-databricks-on-aws.md]

## Views

Views are also supported, but the expanded queries derived from the view definition are restricted to the same simple `SELECT` queries that `CACHE SELECT` accepts for base tables. If a view’s query is more complex (for example, containing joins, aggregations, or subqueries), caching may not be possible. ^[cache-select-databricks-on-aws.md]

## Related Concepts

- [CACHE SELECT command](/concepts/cache-select.md) – The SQL statement used to populate the cache.
- [Disk cache](/concepts/databricks-disk-cache.md) – The underlying caching layer that stores data on local SSDs to accelerate query performance.
- [Delta table](/concepts/delta-lake-table.md) – A format supported for caching.
- Parquet table – Another supported format.
- Simple SELECT query – The type of query allowed by `CACHE SELECT`.

## Sources

- cache-select-databricks-on-aws.md

# Citations

1. [cache-select-databricks-on-aws.md](/references/cache-select-databricks-on-aws-6988f8be.md)
