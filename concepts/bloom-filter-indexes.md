---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0dbe1701ff1382fa0ba5df686b6c32120a7d2606e22f4e94ce652951e7845eff
  pageDirectory: concepts
  sources:
    - create-bloom-filter-index-deprecated-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - bloom-filter-indexes
    - BFI
  citations:
    - file: create-bloom-filter-index-deprecated-databricks-on-aws.md
title: Bloom filter indexes
description: A deprecated indexing feature in Delta Lake used to skip data files during reads; users are advised to migrate to Predictive I/O or Liquid Clustering.
tags:
  - databricks
  - delta-lake
  - deprecated
  - indexing
timestamp: "2026-06-19T14:36:10.295Z"
---

# Bloom filter indexes

**Bloom filter indexes** are a deprecated optimization feature in Databricks that were used to accelerate query performance by skipping irrelevant data files during scans. They are no longer recommended for new use.^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Deprecation status

Bloom filter indexes are deprecated. Databricks advises against creating new Bloom filter indexes. Existing indexes can continue to be used, but users should plan to migrate to supported alternatives.^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Alternatives

For the same performance benefits that Bloom filter indexes provided, Databricks recommends using:

- **[Predictive I/O](/concepts/predictive-io.md)** — a modern optimization that dynamically skips unnecessary data without requiring manual index creation.
- **[Liquid Clustering](/concepts/liquid-clustering.md)** — a data layout strategy that improves file skipping and incremental processing.

Both alternatives offer superior performance and are actively maintained.^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Migration guidance

Detailed information about Bloom filter indexes, including the migration path from existing indexes to predictive I/O or liquid clustering, is available in the dedicated deprecated feature page: [Bloom filter indexes (deprecated)](/concepts/bloom-filter-index-deprecated.md).^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Sources

- create-bloom-filter-index-deprecated-databricks-on-aws.md

# Citations

1. [create-bloom-filter-index-deprecated-databricks-on-aws.md](/references/create-bloom-filter-index-deprecated-databricks-on-aws-ac15d2e3.md)
