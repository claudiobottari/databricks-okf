---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a3feb2fc10925db4d2ece47c0329e1691202366107fe19e563b04f14c525020c
  pageDirectory: concepts
  sources:
    - best-practices-delta-lake-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - predictive-optimization-for-delta-lake
    - POFDL
    - Predictive optimization
  citations:
    - file: best-practices-delta-lake-databricks-on-aws.md
title: Predictive Optimization for Delta Lake
description: Automatic optimization feature on Databricks that runs OPTIMIZE and VACUUM commands on Unity Catalog managed tables without manual intervention.
tags:
  - optimization
  - databricks
  - automation
timestamp: "2026-06-19T17:40:03.235Z"
---

# Predictive Optimization for Delta Lake

**Predictive optimization** is a Databricks feature for [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md) in [Delta Lake](/concepts/delta-lake.md) that automatically runs maintenance operations to keep tables performant. It eliminates the need to manually schedule `OPTIMIZE` and `VACUUM` commands on those tables. ^[best-practices-delta-lake-databricks-on-aws.md]

## Overview

Databricks recommends enabling predictive optimization for all Unity Catalog managed Delta Lake tables. It is listed among the top general best practices, alongside using Unity Catalog managed tables and [Liquid Clustering](/concepts/liquid-clustering.md). ^[best-practices-delta-lake-databricks-on-aws.md]

## How It Works

Predictive optimization automatically executes the `OPTIMIZE` command to compact small files and the `VACUUM` command to remove stale files that are no longer referenced by the transaction log. Both operations run in the background without user intervention. ^[best-practices-delta-lake-databricks-on-aws.md]

When predictive optimization is enabled, you do not need to run `VACUUM` separately after `OPTIMIZE`; the feature handles both operations automatically.

## Best Practices

- **Enable predictive optimization** on all Unity Catalog managed tables to benefit from automatic compaction and cleanup. ^[best-practices-delta-lake-databricks-on-aws.md]
- If you manually run `OPTIMIZE` for a table that has predictive optimization enabled, it is still safe; the system will continue to manage VACUUM automatically.

## Related Concepts

- [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md) – The table type that predictive optimization supports.
- OPTIMIZE – The command used to compact small files in Delta Lake.
- VACUUM – The command used to remove old, unreferenced data files.
- [Delta Lake](/concepts/delta-lake.md) – The storage layer that provides ACID transactions and time travel.
- [Liquid Clustering](/concepts/liquid-clustering.md) – Another optimization technique recommended for Delta Lake tables.
- Compact files – Manual process that predictive optimization automates.

## Sources

- best-practices-delta-lake-databricks-on-aws.md

# Citations

1. [best-practices-delta-lake-databricks-on-aws.md](/references/best-practices-delta-lake-databricks-on-aws-aef26632.md)
