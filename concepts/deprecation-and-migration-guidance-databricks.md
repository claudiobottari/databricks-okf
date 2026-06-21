---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f3735867df3969118cbd1c425b9b82d4d2224803c9419360f9137a2d5f0fcbe6
  pageDirectory: concepts
  sources:
    - create-bloom-filter-index-deprecated-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deprecation-and-migration-guidance-databricks
    - Migration Guidance (Databricks) and Deprecation
    - DAMG(
  citations:
    - file: create-bloom-filter-index-deprecated-databricks-on-aws.md
title: Deprecation and Migration Guidance (Databricks)
description: Databricks documentation providing migration paths away from deprecated Bloom filter indexes toward recommended alternatives like predictive I/O and liquid clustering.
tags:
  - databricks
  - deprecation
  - migration
timestamp: "2026-06-18T11:22:07.713Z"
---

# Deprecation and Migration Guidance (Databricks)

**Deprecation and Migration Guidance** refers to the process of identifying features that have been marked for removal in Databricks and applying the recommended replacements. Databricks periodically deprecates older functionality and provides clear migration paths to modern, supported alternatives. ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Bloom Filter Indexes (Deprecated)

Bloom filter indexes are deprecated. Databricks advises against creating new Bloom filter indexes and recommends migrating existing ones to either [Predictive I/O](/concepts/predictive-io.md) or [Liquid Clustering](/concepts/liquid-clustering.md). ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

### Migration Path

- **Predictive I/O** — A workload-aware optimization that automatically accelerates data skipping without requiring manual index creation.
- **Liquid clustering** — An incremental clustering technique that improves query performance by organizing data files in a layout optimized for common filter patterns.

For full details on the deprecation and step-by-step migration guidance, see [Bloom filter indexes (deprecated)](https://docs.databricks.com/aws/en/optimizations/bloom-filters). ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## General Principles

While only Bloom filter indexes are discussed in the provided source, the same pattern applies to other deprecated features: Databricks documents the reason for deprecation, the timeline (if applicable), and the exact replacement or upgrade path. Always consult the official documentation for the specific feature you are migrating from.

## Related Concepts

- [Bloom filter indexes](/concepts/bloom-filter-indexes.md) — The deprecated feature
- [Predictive I/O](/concepts/predictive-io.md) — Recommended replacement for Bloom filter indexes
- [Liquid Clustering](/concepts/liquid-clustering.md) — Recommended replacement for Bloom filter indexes
- Delta Lake optimization — Broader context for performance tuning

## Sources

- create-bloom-filter-index-deprecated-databricks-on-aws.md

# Citations

1. [create-bloom-filter-index-deprecated-databricks-on-aws.md](/references/create-bloom-filter-index-deprecated-databricks-on-aws-ac15d2e3.md)
