---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 10558e336238eb269b4dc48e47a60cb44e79a476949660dff3ac9a5d2866f0ea
  pageDirectory: concepts
  sources:
    - drop-bloom-filter-index-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - bloom-filter-index-metadata-cleanup-on-drop
    - BFIMCOD
  citations:
    - file: drop-bloom-filter-index-databricks-on-aws.md
title: Bloom filter index metadata cleanup on DROP
description: Dropping a Bloom filter index removes all Bloom filter related metadata from specified columns or entire table
tags:
  - metadata
  - delta-table
  - index-management
timestamp: "2026-06-18T15:35:15.490Z"
---

# Bloom Filter Index Metadata Cleanup on DROP

**Bloom filter index metadata cleanup on DROP** refers to the behavior of the `DROP BLOOMFILTER INDEX` command in Databricks SQL and Databricks Runtime, which removes all metadata associated with Bloom filter indexes from specified columns of a Delta table. This operation is part of the deprecation path for Bloom filter indexes; Databricks recommends dropping all existing Bloom filter indexes and migrating to alternatives.

## Overview

Bloom filter indexes are deprecated in Databricks. The `DROP BLOOMFILTER INDEX` command provides a way to clean up both the metadata and, eventually, the underlying index files for tables that have been configured with Bloom filter indexes. The command removes all Bloom filter–related metadata from the specified columns. After the command completes, the table no longer uses Bloom filter indexing for query optimization. ^[drop-bloom-filter-index-databricks-on-aws.md]

## Syntax

```sql
DROP BLOOMFILTER INDEX ON [TABLE] table_name
    [FOR COLUMNS ( columnName1 [, ...] )]
```

- **table_name**: Identifies an existing Delta table. The name must not include a temporal specification or options specification.^[drop-bloom-filter-index-databricks-on-aws.md]

All specified columns must exist in the table. If either the table or any of the named columns does not exist, the command fails.^[drop-bloom-filter-index-databricks-on-aws.md]

## How Metadata Cleanup Works

When the `DROP BLOOMFILTER INDEX` command is executed, Databricks immediately removes all Bloom filter–related metadata from the specified columns. This metadata includes the index definitions, statistics, and any references used by the query optimizer. After the operation, the table’s metadata no longer records any Bloom filter indexes on those columns.^[drop-bloom-filter-index-databricks-on-aws.md]

If no `FOR COLUMNS` clause is specified, the command drops all Bloom filter indexes on the table. If specific columns are listed, only the Bloom filter indexes on those columns are dropped.^[drop-bloom-filter-index-databricks-on-aws.md]

## Storage Cleanup (Index Files)

The command only removes metadata. The underlying index files (stored in the Delta table’s directory) are not deleted immediately. Instead, they are cleaned up automatically when the table is vacuumed — but only after all Bloom filter indexes have been dropped from the table. Once the table has no remaining Bloom filter indexes, the next `VACUUM` operation will remove the now-unreferenced index files.^[drop-bloom-filter-index-databricks-on-aws.md]

## Error Conditions

The command fails if:
- The specified table does not exist.
- Any of the specified column names do not exist in the table.

## Related Concepts

- [Bloom filter indexes (deprecated)](/concepts/bloom-filter-index.md) — Details on deprecation and recommended alternatives.
- [Delta table](/concepts/delta-lake-table.md) — The table type that supports Bloom filter indexes.
- VACUUM — The operation that eventually cleans up index files after metadata removal.
- Optimizations on Databricks — General guidance on performance tuning, including alternatives to Bloom filter indexes.

## Sources

- drop-bloom-filter-index-databricks-on-aws.md

# Citations

1. [drop-bloom-filter-index-databricks-on-aws.md](/references/drop-bloom-filter-index-databricks-on-aws-7a6d5bf4.md)
