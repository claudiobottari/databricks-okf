---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bdbebc48a9b98ac52acd071dc01466f999732f9c377734aa1f61076d84be83f4
  pageDirectory: concepts
  sources:
    - drop-bloom-filter-index-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - vacuum-and-bloom-filter-index-file-cleanup
    - Bloom filter index file cleanup and VACUUM
    - VABFIFC
  citations:
    - file: drop-bloom-filter-index-databricks-on-aws.md
title: VACUUM and Bloom filter index file cleanup
description: Underlying Bloom filter index files are cleaned only when the Delta table is vacuumed after all indexes are dropped
tags:
  - storage-management
  - delta-table
  - vacuum
  - databricks
timestamp: "2026-06-18T15:35:16.412Z"
---

# VACUUM and Bloom filter index file cleanup

**Bloom filter indexes** are deprecated in Databricks. Databricks recommends dropping all existing Bloom filter indexes and using recommended alternatives instead. ^[drop-bloom-filter-index-databricks-on-aws.md]

## Cleanup process

When a [DROP BLOOM FILTER INDEX](https://docs.databricks.com/aws/en/sql/language-manual/delta-drop-bloomfilter-index) command is issued, all Bloom filter related metadata is removed from the specified columns. ^[drop-bloom-filter-index-databricks-on-aws.md]

The underlying index files (the physical files that stored the Bloom filter data) are **not** removed immediately by the `DROP` command. Instead, those files remain on disk until the next [VACUUM](https://docs.databricks.com/aws/en/sql/language-manual/delta-vacuum) operation on the table. When the table no longer has any Bloom filter indexes, running `VACUUM` cleans up the leftover index files. ^[drop-bloom-filter-index-databricks-on-aws.md]

## Best practice

Because Bloom filter indexes are deprecated, you should:

1. Drop all existing Bloom filter indexes using `DROP BLOOM FILTER INDEX ON <table_name>`.
2. Run `VACUUM` on the table to reclaim the storage space occupied by the obsolete index files.

After the cleanup, replace Bloom filter indexes with the recommended alternatives described in the [Bloom filter indexes (deprecated)](https://docs.databricks.com/aws/en/optimizations/bloom-filters) documentation. ^[drop-bloom-filter-index-databricks-on-aws.md]

## Related concepts

- VACUUM - The command that removes unreferenced files from Delta tables.
- [Bloom filter indexes](/concepts/bloom-filter-index.md) - The deprecated indexing feature whose files are cleaned by VACUUM.
- [DROP BLOOM FILTER INDEX](/concepts/drop-bloom-filter-index-syntax.md) - The command that removes Bloom filter metadata.
- Delta table maintenance - Best practices for keeping Delta tables healthy.

## Sources

- drop-bloom-filter-index-databricks-on-aws.md

# Citations

1. [drop-bloom-filter-index-databricks-on-aws.md](/references/drop-bloom-filter-index-databricks-on-aws-7a6d5bf4.md)
