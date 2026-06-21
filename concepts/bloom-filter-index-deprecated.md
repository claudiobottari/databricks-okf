---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: be6c6a3e86e22d1d2c45f409d7ded222e139dd774809edfe449a74fd1b21c6fd
  pageDirectory: concepts
  sources:
    - drop-bloom-filter-index-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - bloom-filter-index-deprecated
    - BFI(
    - Bloom filter indexes (deprecated)
    - CREATE BLOOM FILTER INDEX (deprecated)
    - bloom filter indexes (deprecated)
    - Bloom filter indexes (deprecated)|the Bloom filter indexes documentation
  citations:
    - file: drop-bloom-filter-index-databricks-on-aws.md
title: Bloom Filter Index (Deprecated)
description: A deprecated indexing feature in Databricks that used Bloom filters to optimize data skipping during queries, now replaced by alternative optimizations.
tags:
  - databricks
  - indexing
  - deprecated-feature
timestamp: "2026-06-19T10:20:26.342Z"
---

# Bloom Filter Index (Deprecated)

**Bloom Filter Index (Deprecated)** refers to a now-deprecated indexing mechanism for Delta tables in Databricks that used Bloom filters to accelerate data skipping during queries. Databricks recommends dropping all existing Bloom filter indexes and migrating to alternative optimization strategies.^[drop-bloom-filter-index-databricks-on-aws.md]

## Overview

Bloom filter indexes were a type of data skipping index that could be created on columns of a [Delta table](/concepts/delta-lake-table.md) to improve query performance by quickly eliminating files that do not contain relevant data. The feature is now deprecated across Databricks SQL and Databricks Runtime.^[drop-bloom-filter-index-databricks-on-aws.md]

## Deprecation

Bloom filter indexes are marked as deprecated. Databricks recommends removing all existing Bloom filter indexes from Delta tables. For details and recommended alternatives, see the documentation on [Bloom filter indexes (deprecated)](/concepts/bloom-filter-index-deprecated.md).^[drop-bloom-filter-index-databricks-on-aws.md]

## Dropping a Bloom Filter Index

The `DROP BLOOMFILTER INDEX` command removes a Bloom filter index from a specified Delta table. If no columns are specified, all Bloom filter indexes on the table are dropped.^[drop-bloom-filter-index-databricks-on-aws.md]

### Syntax

```sql
DROP BLOOMFILTER INDEX
ON [TABLE] table_name
[FOR COLUMNS (columnName1 [, ...] ) ]
```

### Parameters

- **table_name**: Identifies an existing Delta table. The name must not include a temporal specification or options specification.^[drop-bloom-filter-index-databricks-on-aws.md]
- **FOR COLUMNS**: Optional clause specifying one or more column names whose Bloom filter index should be dropped. If omitted, all Bloom filter indexes on the table are dropped.^[drop-bloom-filter-index-databricks-on-aws.md]

### Behavior

- The command fails if the table name or any specified column does not exist.^[drop-bloom-filter-index-databricks-on-aws.md]
- All Bloom filter related metadata is removed from the specified columns.^[drop-bloom-filter-index-databricks-on-aws.md]
- When a table no longer has any Bloom filters, the underlying index files are cleaned up when the table is vacuumed.^[drop-bloom-filter-index-databricks-on-aws.md]

## Cleanup

After all Bloom filter indexes have been dropped from a table, the physical index files are not immediately removed. They are cleaned up as part of the regular VACUUM operation on the Delta table.^[drop-bloom-filter-index-databricks-on-aws.md]

## Related Concepts

- [Delta table](/concepts/delta-lake-table.md) – The table type that supports Bloom filter indexes.
- Data skipping – The optimization technique that Bloom filter indexes were designed to accelerate.
- VACUUM – The operation that cleans up orphaned index files after dropping Bloom filter indexes.
- Query optimization – The broader category of performance improvements that includes indexing strategies.
- [Bloom filter indexes (deprecated)](/concepts/bloom-filter-index-deprecated.md) – Reference documentation for the deprecated feature and recommended alternatives.

## Sources

- drop-bloom-filter-index-databricks-on-aws.md

# Citations

1. [drop-bloom-filter-index-databricks-on-aws.md](/references/drop-bloom-filter-index-databricks-on-aws-7a6d5bf4.md)
