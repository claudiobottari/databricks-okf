---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e1884cf7ffe56e1277574cb19f30dfdf709fd503269c59e4f379368d714756cf
  pageDirectory: concepts
  sources:
    - drop-bloom-filter-index-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - bloom-filter-index-deprecation-on-databricks
    - BFIDOD
  citations:
    - file: drop-bloom-filter-index-databricks-on-aws.md
title: Bloom Filter Index Deprecation on Databricks
description: Official recommendation from Databricks to drop all existing Bloom filter indexes and migrate to recommended alternatives.
tags:
  - databricks
  - deprecation
  - migration
timestamp: "2026-06-19T10:20:21.224Z"
---

```yaml
---
title: Bloom Filter Index Deprecation on Databricks
summary: Bloom filter indexes on Delta tables are deprecated. Databricks recommends dropping all existing Bloom filter indexes using the DROP BLOOMFILTER INDEX command.
sources:
  - drop-bloom-filter-index-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:00:00.000Z"
updatedAt: "2026-06-19T10:00:00.000Z"
tags:
  - databricks
  - deprecation
  - bloom-filter
  - delta-lake
aliases:
  - bloom-filter-index-deprecation-on-databricks
  - BFIDOD
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Bloom Filter Index Deprecation on Databricks

## Overview

Bloom filter indexes are deprecated in Databricks. Databricks recommends dropping all existing Bloom filter indexes from Delta tables. For details on why these indexes are deprecated and for recommended alternatives, see the official documentation on [[Bloom Filter Index (Deprecated)|Bloom filter indexes (deprecated)]]. ^[drop-bloom-filter-index-databricks-on-aws.md]

## Recommended Action

To remove a Bloom filter index, use the `DROP BLOOMFILTER INDEX` command. This command removes all Bloom filter related metadata from the specified columns of a Delta table. ^[drop-bloom-filter-index-databricks-on-aws.md]

### Syntax

```sql
DROP BLOOMFILTER INDEX ON [TABLE] table_name [FOR COLUMNS ( columnName1 [, ...] ) ]
```

- **`table_name`**: Identifies an existing Delta table. The name must not include a temporal specification or options specification.  
- **`FOR COLUMNS`**: Optional. Specifies a list of columns from which to drop the Bloom filter index. If omitted, the index is dropped for all columns. ^[drop-bloom-filter-index-databricks-on-aws.md]

The command fails if the table name or any of the specified columns do not exist. ^[drop-bloom-filter-index-databricks-on-aws.md]

### Post-Drop Cleanup

After all Bloom filters are dropped from a table, the underlying index files are cleaned when the table is vacuumed using the VACUUM command. ^[drop-bloom-filter-index-databricks-on-aws.md]

## Related Concepts

- [[Bloom Filter Index (Deprecated)|Bloom filter indexes (deprecated)]] – Databricks documentation with deprecation details and alternatives.
- [[Delta Lake Table|Delta tables]] – The table type that supported Bloom filter indexes.
- VACUUM – Operation that cleans up unreferenced index files after dropping Bloom filter indexes.
- [[DROP BLOOM FILTER INDEX syntax|DROP BLOOMFILTER INDEX]] – The SQL command to drop a Bloom filter index.

## Sources

- drop-bloom-filter-index-databricks-on-aws.md
```

# Citations

1. [drop-bloom-filter-index-databricks-on-aws.md](/references/drop-bloom-filter-index-databricks-on-aws-7a6d5bf4.md)
