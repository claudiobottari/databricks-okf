---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 14484bf79b5ea2ed323133dfc9c66bbddc868832eff0c2e5c80a4920aeb6b4d1
  pageDirectory: concepts
  sources:
    - create-bloom-filter-index-deprecated-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - predictive-io
    - predictive-io-databricks
    - PI(
  citations:
    - file: create-bloom-filter-index-deprecated-databricks-on-aws.md
title: Predictive I/O
description: A modern replacement for Bloom filter indexes in Databricks that optimizes data skipping during queries.
tags:
  - optimization
  - databricks
  - performance
timestamp: "2026-06-19T18:00:48.132Z"
---

# Predictive I/O

**Predictive I/O** is the recommended replacement for the deprecated [Bloom filter indexes](/concepts/bloom-filter-index.md) feature in Databricks. ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Overview

Bloom filter indexes are deprecated. New Bloom filter indexes should not be created. Instead, users should use Predictive I/O or [Liquid Clustering](/concepts/liquid-clustering.md) as a replacement. ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Migration Guidance

For existing tables that use Bloom filter indexes, see the dedicated documentation on [Bloom filter indexes (deprecated)](/concepts/bloom-filter-index.md) for details and migration guidance on replacing them with Predictive I/O or liquid clustering. ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Related Concepts

- [Bloom filter indexes](/concepts/bloom-filter-index.md) — The deprecated feature that Predictive I/O replaces.
- [Liquid Clustering](/concepts/liquid-clustering.md) — Another alternative for data clustering and skipping.
- Data skipping — The broader technique of avoiding irrelevant data during scans.
- [Delta Lake](/concepts/delta-lake.md) — The storage layer on which Predictive I/O operates.
- Query optimization — The goal that Predictive I/O supports.

## Sources

- create-bloom-filter-index-deprecated-databricks-on-aws.md

# Citations

1. [create-bloom-filter-index-deprecated-databricks-on-aws.md](/references/create-bloom-filter-index-deprecated-databricks-on-aws-ac15d2e3.md)
