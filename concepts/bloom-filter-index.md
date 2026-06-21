---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 527a8c9a577a7e17abfc2df5e50586fc84848c5f2261a343e4062793059aa271
  pageDirectory: concepts
  sources:
    - create-bloom-filter-index-deprecated-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - bloom-filter-index
    - BFI
    - DROP BLOOM FILTER INDEX
    - DROP BLOOMFILTER INDEX
    - Bloom filter
  citations:
    - file: create-bloom-filter-index-deprecated-databricks-on-aws.md
title: Bloom Filter Index
description: A legacy indexing technique for Delta tables in Databricks used to skip irrelevant data files during query execution.
tags:
  - indexing
  - delta-lake
  - optimization
timestamp: "2026-06-19T18:00:38.906Z"
---

# Bloom Filter Index

Bloom Filter Index is a deprecated feature in Databricks used for optimizing query performance by skipping irrelevant data files. ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Deprecation Status

Bloom filter indexes are deprecated. Users are advised not to create new Bloom filter indexes and to migrate existing ones to alternative optimization methods. ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Recommended Alternatives

Instead of using Bloom filter indexes, Databricks recommends the following modern approaches:

- **[Predictive I/O](/concepts/predictive-io.md)** – A mechanism that automatically predicts which files are needed for a query, improving I/O throughput without manual index management.
- **[Liquid Clustering](/concepts/liquid-clustering.md)** – A clustering strategy that continuously reorganizes data for efficient data skipping, eliminating the need for static indexes.

For detailed migration guidance, see the official documentation on [Bloom filter indexes (deprecated)](https://docs.databricks.com/aws/en/optimizations/bloom-filters). ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Related Concepts

- [Predictive I/O](/concepts/predictive-io.md)
- [Liquid Clustering](/concepts/liquid-clustering.md)
- Data Skipping
- [Delta Lake](/concepts/delta-lake.md)

## Sources

- create-bloom-filter-index-deprecated-databricks-on-aws.md

# Citations

1. [create-bloom-filter-index-deprecated-databricks-on-aws.md](/references/create-bloom-filter-index-deprecated-databricks-on-aws-ac15d2e3.md)
