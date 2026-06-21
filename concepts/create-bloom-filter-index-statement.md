---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e2bc7fde5cf4d18bfc4998e6c2ca71c0cdd9e81e4cd8c4bade573a520ca8eb66
  pageDirectory: concepts
  sources:
    - create-bloom-filter-index-deprecated-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - create-bloom-filter-index-statement
    - CBFIS
  citations:
    - file: create-bloom-filter-index-deprecated-databricks-on-aws.md
title: CREATE BLOOM FILTER INDEX Statement
description: The deprecated SQL statement used to create Bloom filter indexes on Delta tables in Databricks.
tags:
  - sql
  - indexing
  - databricks
timestamp: "2026-06-19T18:00:51.736Z"
---

# CREATE BLOOM FILTER INDEX Statement

**CREATE BLOOM FILTER INDEX** is a deprecated [Delta Lake](/concepts/delta-lake.md) SQL statement that was used to create a Bloom filter index on a table to accelerate data skipping during queries. Bloom filter indexes are no longer recommended for new use. ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Deprecation

Bloom filter indexes are deprecated in Databricks. You should not create new Bloom filter indexes. Existing indexes may continue to function, but Databricks recommends migrating away from them. ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Recommended Alternatives

Instead of creating a Bloom filter index, use one of the following features:

- [Predictive I/O](/concepts/predictive-io.md) — provides automatic data skipping optimizations without manual index management.
- [Liquid Clustering](/concepts/liquid-clustering.md) — reorganizes data layout to improve query performance and data skipping.

For details on the deprecation and step‑by‑step migration guidance, see the dedicated documentation page: [Bloom filter indexes (deprecated)](https://docs.databricks.com/aws/en/optimizations/bloom-filters). ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that supported Bloom filter indexes.
- Data Skipping — The performance optimization technique that Bloom filter indexes were designed to accelerate.
- Table Optimization on Databricks — Overview of performance features for Delta tables.

## Sources

- create-bloom-filter-index-deprecated-databricks-on-aws.md

# Citations

1. [create-bloom-filter-index-deprecated-databricks-on-aws.md](/references/create-bloom-filter-index-deprecated-databricks-on-aws-ac15d2e3.md)
