---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6444f1594c8fb7923a3a66a9a47514ef80139beaf99704c967c22b1d4650fc5f
  pageDirectory: concepts
  sources:
    - create-bloom-filter-index-deprecated-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - bloom-filter-index-deprecation-databricks
    - BFID(
  citations:
    - file: create-bloom-filter-index-deprecated-databricks-on-aws.md
title: Bloom Filter Index Deprecation (Databricks)
description: Bloom filter indexes are deprecated in Databricks, with migration guidance to predictive I/O or liquid clustering.
tags:
  - deprecation
  - optimization
  - databricks
timestamp: "2026-06-19T09:35:36.386Z"
---

# Bloom Filter Index Deprecation (Databricks)

**Bloom Filter Index Deprecation (Databricks)** refers to the formal deprecation of Bloom filter indexes in Databricks. Databricks recommends that users do not create new Bloom filter indexes and migrate existing ones to alternative optimization features.

## Overview

[Bloom filter indexes](/concepts/bloom-filter-indexes.md) are a data skipping technique that Databricks previously supported for improving query performance by filtering out data files that do not contain relevant data. As of the current guidance, these indexes are deprecated and should not be used in new workloads.^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Deprecation Status

The `CREATE BLOOM FILTER INDEX` command is deprecated. Databricks advises against creating new Bloom filter indexes in any new or existing workloads.^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Recommended Alternatives

Databricks recommends the following alternatives to Bloom filter indexes:

- **[Predictive I/O](/concepts/predictive-io.md)**: A performance optimization feature that provides better data skipping capabilities with lower maintenance overhead.
- **[Liquid Clustering](/concepts/liquid-clustering.md)**: A clustering strategy that offers improved data organization and query optimization without the need for separate index structures.

Both alternatives provide superior performance and are better integrated with the Databricks platform.^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Migration Guidance

For existing Bloom filter indexes, Databricks provides detailed migration guidance in their documentation on [Bloom filter indexes (deprecated)](/concepts/bloom-filter-index-deprecated.md). Users should review this documentation to understand how to transition existing workloads away from Bloom filter indexes.^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Related Concepts

- Data skipping
- Query optimization in Databricks
- [Table clustering](/concepts/delta-lake-liquid-clustering.md)
- Viewing and managing Bloom filters

## Sources

- create-bloom-filter-index-deprecated-databricks-on-aws.md

# Citations

1. [create-bloom-filter-index-deprecated-databricks-on-aws.md](/references/create-bloom-filter-index-deprecated-databricks-on-aws-ac15d2e3.md)
