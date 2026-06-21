---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a3ed5a0e50b1fa26f5def96a73426960fc22e45745bc23b96537e53fd57b29b1
  pageDirectory: concepts
  sources:
    - create-bloom-filter-index-deprecated-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - predictive-io-databricks
    - PI(
  citations:
    - file: create-bloom-filter-index-deprecated-databricks-on-aws.md
title: Predictive I/O (Databricks)
description: A Databricks optimization feature recommended as a replacement for deprecated Bloom filter indexes.
tags:
  - optimization
  - databricks
  - I/O
timestamp: "2026-06-19T09:35:40.449Z"
---

# Predictive I/O (Databricks)

**Predictive I/O** is a Databricks optimization feature that improves query performance by intelligently scheduling and reducing I/O operations during data scanning. It is recommended as a modern replacement for the deprecated [Bloom filter indexes](/concepts/bloom-filter-indexes.md). ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Overview

Predictive I/O works by predicting which data files or partitions are relevant to a query before they are read, allowing the query engine to skip unnecessary I/O operations. This reduces the amount of data scanned and improves query performance, particularly for large datasets with selective filters. ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

The feature is part of Databricks' ongoing optimization efforts and is designed to provide similar or better I/O skipping benefits compared to Bloom filter indexes, without requiring manual index creation or maintenance. ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Relationship to Bloom Filter Indexes

Bloom filter indexes are deprecated in Databricks. Databricks advises against creating new Bloom filter indexes and instead recommends using predictive I/O or [Liquid Clustering](/concepts/liquid-clustering.md) as alternatives. ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

| Feature | Status | Recommendation |
|---------|--------|----------------|
| Bloom filter indexes | Deprecated | Do not create new indexes |
| Predictive I/O | Active | Recommended replacement |
| Liquid Clustering | Active | Alternative replacement |

## Migration Guidance

For detailed information on the deprecation of Bloom filter indexes and guidance for migrating to predictive I/O or liquid clustering, see the dedicated page on [Bloom filter indexes (deprecated)](https://docs.databricks.com/aws/en/optimizations/bloom-filters). ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Benefits

- **No manual maintenance**: Unlike Bloom filter indexes, predictive I/O does not require creating or rebuilding indexes manually. ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]
- **Automatic optimization**: The feature works automatically based on query patterns and data characteristics. ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]
- **Reduced storage overhead**: No additional index storage is needed. ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]
- **Improved query performance**: Reduces I/O by skipping irrelevant data files during query execution. ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Related Concepts

- [Bloom filter indexes (deprecated)](/concepts/bloom-filter-index-deprecated.md)
- [Liquid Clustering](/concepts/liquid-clustering.md)
- Delta Lake optimization
- Query performance tuning
- Data skipping

## Sources

- create-bloom-filter-index-deprecated-databricks-on-aws.md

# Citations

1. [create-bloom-filter-index-deprecated-databricks-on-aws.md](/references/create-bloom-filter-index-deprecated-databricks-on-aws-ac15d2e3.md)
