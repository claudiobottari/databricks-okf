---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7d338997bc0cfaa79a3ed87084cc0d9e2fdc941fef15cee4f404b1bf4c7b7945
  pageDirectory: concepts
  sources:
    - drop-bloom-filter-index-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - bloom-filter-index-deprecation-in-databricks
    - BFIDID
  citations:
    - file: drop-bloom-filter-index-databricks-on-aws.md
title: Bloom filter index deprecation in Databricks
description: Bloom filter indexes are deprecated in Databricks; users are recommended to drop all existing Bloom filter indexes
tags:
  - deprecation
  - databricks
  - bloom-filter
  - delta-table
timestamp: "2026-06-18T15:35:26.247Z"
---

# Bloom Filter Index Deprecation in Databricks

**Bloom Filter Index Deprecation in Databricks** refers to the official deprecation of [Bloom filter indexes](/concepts/bloom-filter-indexes.md) across Databricks SQL and Databricks Runtime. Databricks recommends that users drop all existing bloom filter indexes and adopt alternative optimization techniques. ^[drop-bloom-filter-index-databricks-on-aws.md]

## Deprecation Status

Bloom filter indexes are deprecated in Databricks. This deprecation applies to both Databricks SQL and Databricks Runtime. Databricks recommends that users remove all existing bloom filter indexes from their Delta tables and use recommended alternatives instead. ^[drop-bloom-filter-index-databricks-on-aws.md]

## Dropping a Bloom Filter Index

To remove a bloom filter index, use the `DROP BLOOMFILTER INDEX` command. ^[drop-bloom-filter-index-databricks-on-aws.md]

### Syntax

```sql
DROP BLOOMFILTER INDEX ON [TABLE] table_name [FOR COLUMNS (columnName1 [, ...] ) ]
```

^[drop-bloom-filter-index-databricks-on-aws.md]

### Parameters

- `table_name` – Identifies an existing Delta table. The name must not include a temporal specification or options specification. ^[drop-bloom-filter-index-databricks-on-aws.md]
- `FOR COLUMNS` – Optional clause specifying which columns to drop the bloom filter index from. If omitted, the index is dropped from all columns on the table. ^[drop-bloom-filter-index-databricks-on-aws.md]

### Behavior

- The command fails if the table name or any specified column does not exist. ^[drop-bloom-filter-index-databricks-on-aws.md]
- All bloom filter related metadata is removed from the specified columns. ^[drop-bloom-filter-index-databricks-on-aws.md]
- When a table no longer has any bloom filters, the underlying index files are cleaned when the table is VACUUM'd. ^[drop-bloom-filter-index-databricks-on-aws.md]

### Example

```sql
-- Drop bloom filter index from a specific column
DROP BLOOMFILTER INDEX ON TABLE sales_data FOR COLUMNS (order_id);

-- Drop bloom filter index from multiple columns
DROP BLOOMFILTER INDEX ON TABLE sales_data FOR COLUMNS (order_id, customer_id);

-- Drop all bloom filter indexes from a table
DROP BLOOMFILTER INDEX ON TABLE sales_data;
```

## Recommended Alternatives

For details on recommended alternatives to bloom filter indexes, see the [bloom filter indexes (deprecated)](/concepts/bloom-filter-index-deprecated.md) documentation. ^[drop-bloom-filter-index-databricks-on-aws.md]

## Related Concepts

- [Bloom filter indexes](/concepts/bloom-filter-indexes.md) – The deprecated indexing feature.
- Delta Lake optimization techniques – Alternative approaches for query performance.
- DROP INDEX – General index removal operations.
- VACUUM – Cleanup operation that removes orphaned index files.

## Sources

- drop-bloom-filter-index-databricks-on-aws.md

# Citations

1. [drop-bloom-filter-index-databricks-on-aws.md](/references/drop-bloom-filter-index-databricks-on-aws-7a6d5bf4.md)
