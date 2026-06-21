---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 815f6dd02a5f7ea2e47ed5f224c61a79428e6ae2ef9cecbb7ba537a05bde9c64
  pageDirectory: concepts
  sources:
    - drop-bloom-filter-index-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - bloom-filter-index-cleanup-semantics
    - BFICS
  citations:
    - file: drop-bloom-filter-index-databricks-on-aws.md
title: Bloom Filter Index Cleanup Semantics
description: When a Bloom filter index is dropped, all related metadata is removed from specified columns and underlying index files are cleaned only after a vacuum
tags:
  - cleanup
  - storage
  - delta-table
timestamp: "2026-06-19T18:38:55.527Z"
---

# Bloom Filter Index Cleanup Semantics

**Bloom Filter Index Cleanup Semantics** describes the behavior and lifecycle of index files and metadata when a Bloom filter index is dropped from a Delta table in Databricks. Understanding the cleanup semantics is important for managing table storage and vacuum operations.

## Overview

When a `DROP BLOOMFILTER INDEX` command is issued on a Delta table, the index metadata and underlying index files are handled differently depending on the timing and the presence of any remaining Bloom filters on the table. ^[drop-bloom-filter-index-databricks-on-aws.md]

## Metadata Removal

When you run `DROP BLOOMFILTER INDEX ON [TABLE] table_name`, all Bloom filter-related metadata is immediately removed from the specified columns. The command fails if either the table name or one of the specified columns does not exist. ^[drop-bloom-filter-index-databricks-on-aws.md]

## Index File Cleanup

The cleanup of the underlying index files follows a deferred pattern:

- When a table still has at least one Bloom filter index (for example, if you drop only specific columns), the index files for the dropped columns are cleaned up at the time of the `DROP` command. ^[drop-bloom-filter-index-databricks-on-aws.md]
- When a table no longer has any Bloom filters — either because you dropped the last index or dropped all columns — the remaining index files are **not** immediately removed. Instead, they are cleaned up when you run `VACUUM` on the table. ^[drop-bloom-filter-index-databricks-on-aws.md]

## Recommended Practice

Databricks recommends dropping all existing [Bloom filter indexes](/concepts/bloom-filter-index.md) because the feature is deprecated. After dropping all indexes, running VACUUM is necessary to reclaim the storage space occupied by the orphaned index files. ^[drop-bloom-filter-index-databricks-on-aws.md]

## Related Concepts

- [Bloom Filter Index (Deprecated)](/concepts/bloom-filter-index.md) — The deprecated indexing feature
- VACUUM — The command that physically removes orphaned index files
- Delta Table Storage Management — General cleanup and maintenance practices
- Data Skipping — Recommended alternative for query optimization

## Sources

- drop-bloom-filter-index-databricks-on-aws.md

# Citations

1. [drop-bloom-filter-index-databricks-on-aws.md](/references/drop-bloom-filter-index-databricks-on-aws-7a6d5bf4.md)
