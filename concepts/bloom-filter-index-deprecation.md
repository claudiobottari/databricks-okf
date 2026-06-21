---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6a40e3aca95a5a10032607c34a3869572e959a6c6eabde58c6b827d518693925
  pageDirectory: concepts
  sources:
    - create-bloom-filter-index-deprecated-databricks-on-aws.md
    - drop-bloom-filter-index-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - bloom-filter-index-deprecation
    - BFID
  citations:
    - file: create-bloom-filter-index-deprecated-databricks-on-aws.md
    - file: drop-bloom-filter-index-databricks-on-aws.md
title: Bloom Filter Index Deprecation
description: Bloom filter indexes are deprecated in Databricks and should not be created anymore.
tags:
  - deprecation
  - indexing
  - databricks
timestamp: "2026-06-19T18:00:27.503Z"
---

# Bloom Filter Index Deprecation

**Bloom filter indexes** are a deprecated feature in Databricks. Users are advised not to create new Bloom filter indexes and to drop all existing ones. The recommended replacements are [Predictive I/O](/concepts/predictive-io.md) and [Liquid Clustering](/concepts/liquid-clustering.md), which provide improved performance and maintainability. ^[create-bloom-filter-index-deprecated-databricks-on-aws.md, drop-bloom-filter-index-databricks-on-aws.md]

## Migration Guidance

Databricks strongly recommends migrating away from Bloom filter indexes:

- **Do not** create new Bloom filter indexes.
- **Drop** all existing Bloom filter indexes using the `DROP BLOOMFILTER INDEX` SQL command.
- **Replace** Bloom filter indexes with:
  - [Predictive I/O](/concepts/predictive-io.md) – An optimization that automatically predicts which data files to read, reducing I/O.
  - [Liquid Clustering](/concepts/liquid-clustering.md) – A clustering technique that improves data skipping and query performance without requiring manual index maintenance.

For detailed migration instructions, see the official documentation on [Bloom filter indexes (deprecated)](/concepts/bloom-filter-index-deprecated.md). ^[create-bloom-filter-index-deprecated-databricks-on-aws.md, drop-bloom-filter-index-databricks-on-aws.md]

## Dropping Existing Bloom Filter Indexes

The `DROP BLOOMFILTER INDEX` command removes Bloom filter metadata from specified columns in a Delta table. The syntax is:

```
DROP BLOOMFILTER INDEX ON [TABLE] table_name [FOR COLUMNS (columnName1 [, ...])]
```

If the command omits the column list, all Bloom filter indexes on the table are dropped. After dropping, the underlying index files are cleaned when the table is next vacuumed. The command fails if the table or any specified column does not exist. ^[drop-bloom-filter-index-databricks-on-aws.md]

## Related Concepts

- [Predictive I/O](/concepts/predictive-io.md)
- [Liquid Clustering](/concepts/liquid-clustering.md)
- [Bloom filter indexes (deprecated)](/concepts/bloom-filter-index-deprecated.md)
- Delta Lake optimizations
- [Data skipping in Delta Lake](/concepts/z-ordering-delta-lake.md)
- [VACUUM command](/concepts/vacuum-command-databricks.md)

## Sources

- create-bloom-filter-index-deprecated-databricks-on-aws.md
- drop-bloom-filter-index-databricks-on-aws.md

# Citations

1. [create-bloom-filter-index-deprecated-databricks-on-aws.md](/references/create-bloom-filter-index-deprecated-databricks-on-aws-ac15d2e3.md)
2. [drop-bloom-filter-index-databricks-on-aws.md](/references/drop-bloom-filter-index-databricks-on-aws-7a6d5bf4.md)
