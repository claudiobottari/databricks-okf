---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6d79e6da8f96cb4ba28a14ec4bb80dcf91720627aad889e8d232e4866e27a486
  pageDirectory: concepts
  sources:
    - drop-bloom-filter-index-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - bloom-filter-index-metadata-removal
    - BFIMR
  citations:
    - file: drop-bloom-filter-index-databricks-on-aws.md
title: Bloom Filter Index Metadata Removal
description: All Bloom filter-related metadata is removed from specified columns when the DROP BLOOMFILTER INDEX command succeeds.
tags:
  - delta-lake
  - metadata
  - indexing
timestamp: "2026-06-18T12:09:45.462Z"
---

# Bloom Filter Index Metadata Removal

**Bloom Filter Index Metadata Removal** refers to the process of deleting a [Bloom Filter Index](/concepts/bloom-filter-index.md) from a [Delta Lake](/concepts/delta-lake.md) table using the `DROP BLOOMFILTER INDEX` SQL command. This operation removes all Bloom filter related metadata from the specified columns and, over time, cleans up the underlying index files from storage. ^[drop-bloom-filter-index-databricks-on-aws.md]

Bloom filter indexes are deprecated. Databricks recommends dropping all existing Bloom filter indexes and migrating to alternative optimization techniques. See [Bloom filter indexes (deprecated)](/concepts/bloom-filter-index-deprecated.md) for details and recommended alternatives. ^[drop-bloom-filter-index-databricks-on-aws.md]

## Syntax

```sql
DROP BLOOMFILTER INDEX
ON [TABLE] table_name
[FOR COLUMNS ( columnName1 [, ...] ) ]
```

^[drop-bloom-filter-index-databricks-on-aws.md]

## Parameters

- `table_name`: Identifies an existing Delta table. The name must not include a temporal specification or options specification. ^[drop-bloom-filter-index-databricks-on-aws.md]

The command fails if either the table name or one of the specified columns does not exist. ^[drop-bloom-filter-index-databricks-on-aws.md]

## Behavior

All Bloom filter related metadata is removed from the specified columns immediately upon execution of the command. ^[drop-bloom-filter-index-databricks-on-aws.md]

The underlying Bloom filter index files are not removed immediately. They are cleaned up when the table is next vacuumed, but only after all Bloom filters on the table have been dropped. If only a subset of columns are dropped, the remaining index files stay in place. ^[drop-bloom-filter-index-databricks-on-aws.md]

## When to Use

Because Bloom filter indexes are deprecated, you should drop all existing Bloom filter indexes as a migration step. After dropping them, consider using alternative performance optimizations such as [Liquid Clustering](/concepts/liquid-clustering.md), [Z-ordering](/concepts/z-ordering-delta-lake.md), or data skipping improvements. ^[drop-bloom-filter-index-databricks-on-aws.md]

## Related Concepts

- [Bloom filter indexes (deprecated)](/concepts/bloom-filter-index-deprecated.md) — The deprecated feature this command removes
- [Delta Lake](/concepts/delta-lake.md) — The storage format that supports Bloom filter indexes
- VACUUM — The command that cleans up orphaned index files after all Bloom filters are dropped
- Data skipping — An alternative optimization technique for predicate filtering

## Sources

- drop-bloom-filter-index-databricks-on-aws.md

# Citations

1. [drop-bloom-filter-index-databricks-on-aws.md](/references/drop-bloom-filter-index-databricks-on-aws-7a6d5bf4.md)
