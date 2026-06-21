---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 272a4c478ac50297a8fa9ac3761e3ef9fc73a07c3320f45cb20efa5b12f87847
  pageDirectory: concepts
  sources:
    - best-practices-delta-lake-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-predictive-optimization
    - DLPO
    - predictive optimization
  citations:
    - file: best-practices-delta-lake-databricks-on-aws.md
title: Delta Lake Predictive Optimization
description: A Databricks feature that automatically runs OPTIMIZE and VACUUM commands on Unity Catalog managed tables to maintain performance
tags:
  - delta-lake
  - optimization
  - databricks
timestamp: "2026-06-19T22:12:39.520Z"
---

# Delta Lake Predictive Optimization

**Delta Lake Predictive Optimization** is a feature on Databricks that automatically performs maintenance operations on [Unity Catalog](/concepts/unity-catalog.md) [managed tables](/concepts/managed-tables-in-databricks.md). It is recommended as a best practice for most Delta Lake workloads. ^[best-practices-delta-lake-databricks-on-aws.md]

## Automatic Maintenance Operations

Predictive optimization automatically runs two key commands to keep tables performant:

- **`OPTIMIZE`** – Compacts small files into larger ones, improving read throughput and query performance.
- **`VACUUM`** – Removes old, unreferenced data files that are no longer needed by the table’s transaction log.

Both commands are executed on Unity Catalog managed tables without requiring manual intervention. ^[best-practices-delta-lake-databricks-on-aws.md]

## Scope

Predictive optimization applies only to Unity Catalog managed tables. It does not run on external tables or tables not registered in Unity Catalog. ^[best-practices-delta-lake-databricks-on-aws.md]

## Relationship with Other Features

Predictive optimization complements other table maintenance and layout features:

- [Liquid Clustering](/concepts/liquid-clustering.md) – An alternative to traditional partitioning for data layout; predictive optimization preserves clustering optimizations during `OPTIMIZE`.
- Compact files – While predictive optimization automates compaction, users can also run `OPTIMIZE` manually for immediate results.

## Source

- best-practices-delta-lake-databricks-on-aws.md

# Citations

1. [best-practices-delta-lake-databricks-on-aws.md](/references/best-practices-delta-lake-databricks-on-aws-aef26632.md)
