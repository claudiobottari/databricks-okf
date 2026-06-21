---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3608c188125b615c14bacbc8cf4a65f156d3b44d7bdba1ae61387520eec1970f
  pageDirectory: concepts
  sources:
    - drop-bloom-filter-index-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - bloom-filter-metadata-cleanup
    - BFMC
  citations:
    - file: drop-bloom-filter-index-databricks-on-aws.md
title: Bloom Filter Metadata Cleanup
description: Behavior of the DROP command to remove all Bloom filter related metadata from specified columns, with index file cleanup occurring on VACUUM.
tags:
  - databricks
  - metadata
  - delta-table
timestamp: "2026-06-19T10:20:19.925Z"
---

# Bloom Filter Metadata Cleanup

**Bloom Filter Metadata Cleanup** refers to the process of removing metadata and index files associated with deprecated [Bloom filter indexes](/concepts/bloom-filter-index.md) in [Delta Lake](/concepts/delta-lake.md) tables. This cleanup is necessary when dropping Bloom filter indexes, as the metadata removal and file cleanup occur at different stages.

## Overview

When a [Bloom Filter Index](/concepts/bloom-filter-index.md) is dropped using the [DROP BLOOM FILTER INDEX](/concepts/drop-bloom-filter-index-syntax.md) command, all Bloom filter related metadata is removed from the specified columns. However, the underlying index files are not immediately deleted from storage. ^[drop-bloom-filter-index-databricks-on-aws.md]

## Index File Cleanup

The actual index files remain on disk until the table is VACUUM. Only when a table has no remaining Bloom filters do the underlying index files become eligible for cleanup during the next vacuum operation. ^[drop-bloom-filter-index-databricks-on-aws.md]

### Cleanup Steps

1. **Drop the Bloom filter index** — Use the `DROP BLOOMFILTER INDEX` command to remove all Bloom filter metadata from the specified columns. This operation removes the logical definition but not the physical files. ^[drop-bloom-filter-index-databricks-on-aws.md]
2. **Verify all indexes are dropped** — Ensure no Bloom filters remain on the table. If any indexes still exist, the underlying files will not be cleaned. ^[drop-bloom-filter-index-databricks-on-aws.md]
3. **Run VACUUM** — Execute the [VACUUM command](/concepts/vacuum-command-databricks.md) on the table to delete the orphaned index files from storage. ^[drop-bloom-filter-index-databricks-on-aws.md]

## Related Articles

- [DROP BLOOM FILTER INDEX](/concepts/drop-bloom-filter-index-syntax.md) — The SQL command for removing Bloom filter indexes
- [Bloom filter indexes (deprecated)](/concepts/bloom-filter-index.md) — Overview of the deprecated feature and recommended alternatives
- Delta Lake table management
- Data skipping optimizations
- [VACUUM command](/concepts/vacuum-command-databricks.md)

## Sources

- drop-bloom-filter-index-databricks-on-aws.md

# Citations

1. [drop-bloom-filter-index-databricks-on-aws.md](/references/drop-bloom-filter-index-databricks-on-aws-7a6d5bf4.md)
