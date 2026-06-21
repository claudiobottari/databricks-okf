---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cd69ebe2801e33018fbc62979c6271b521d746ab0f1900110812f779371be765
  pageDirectory: concepts
  sources:
    - create-bloom-filter-index-deprecated-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - bloom-filter-indexes-databricks
    - BFI(
  citations:
    - file: create-bloom-filter-index-deprecated-databricks-on-aws.md
title: Bloom Filter Indexes (Databricks)
description: A deprecated indexing technique in Databricks that uses Bloom filters to skip non-matching files during query execution, improving performance on equality predicates.
tags:
  - databricks
  - indexing
  - deprecated
timestamp: "2026-06-18T11:21:45.510Z"
---

# Bloom Filter Indexes (Databricks)

**Bloom filter indexes** are a deprecated indexing feature in Databricks that were used to improve query performance on [Delta Lake](/concepts/delta-lake.md) tables by filtering out files that do not contain relevant data. Databricks recommends against creating new Bloom filter indexes and advises migrating to modern alternatives. ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Deprecation Status

Bloom filter indexes are deprecated. Databricks does not support creating new Bloom filter indexes. ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Recommended Alternatives

Databricks recommends using the following features instead of Bloom filter indexes:

- **[Predictive I/O](/concepts/predictive-io.md)** — a mechanism that uses statistics and machine learning to skip reading unnecessary data files during query execution.
- **[Liquid Clustering](/concepts/liquid-clustering.md)** — a re-clustering strategy that organizes data layout for more efficient pruning and file skipping.

For detailed migration guidance and deprecation status, refer to the official documentation on [Bloom filter indexes (deprecated)](https://docs.databricks.com/aws/en/optimizations/bloom-filters). ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — the storage layer that Bloom filter indexes previously targeted.
- [Predictive I/O](/concepts/predictive-io.md) — a recommended replacement for Bloom filter indexes.
- [Liquid Clustering](/concepts/liquid-clustering.md) — another recommended replacement for Bloom filter indexes.
- Data skipping — the technique that both Bloom filter indexes and alternatives use to improve query performance.

## Sources

- create-bloom-filter-index-deprecated-databricks-on-aws.md

# Citations

1. [create-bloom-filter-index-deprecated-databricks-on-aws.md](/references/create-bloom-filter-index-deprecated-databricks-on-aws-ac15d2e3.md)
