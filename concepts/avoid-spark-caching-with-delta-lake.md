---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8a6e6e143fd15dae61809c878daa16d1121fbfa1be8ac251668ebf3df474c8e7
  pageDirectory: concepts
  sources:
    - best-practices-delta-lake-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - avoid-spark-caching-with-delta-lake
    - ASCWDL
  citations:
    - file: best-practices-delta-lake-databricks-on-aws.md
title: Avoid Spark Caching with Delta Lake
description: Databricks recommends against using Spark caching for Delta tables because it breaks data skipping optimizations and can serve stale data if the table is accessed via a different identifier.
tags:
  - delta-lake
  - spark
  - caching
timestamp: "2026-06-19T14:08:40.311Z"
---

# Avoid Spark Caching with Delta Lake

**Avoid Spark Caching with Delta Lake** refers to the recommendation against using the Spark cache (`DataFrame.cache()`, `.persist()`, etc.) for Delta Lake tables. Databricks advises against this practice because it can degrade query performance and produce stale results. ^[best-practices-delta-lake-databricks-on-aws.md]

## Why You Should Avoid Spark Caching

Spark caching is generally unnecessary—and often harmful—when working with [Delta Lake](/concepts/delta-lake.md) tables. The two primary reasons are:

1. **Loss of data skipping.** When you cache a `DataFrame`, any filters added after caching cannot leverage Delta Lake’s built-in data skipping optimisations. Data skipping uses table metadata (such as partition columns and file-level statistics) to prune irrelevant files early in the query plan. Caching bypasses that scan, so later filters no longer benefit from this pruning, leading to slower queries. ^[best-practices-delta-lake-databricks-on-aws.md]

2. **Stale or inconsistent data.** Cached data is static; it reflects the state of the table at the moment the cache was created. If the table is subsequently updated (for example, by another job or through a different identifier), the cache is not automatically refreshed. This can cause downstream queries to read outdated results. Delta Lake itself always serves the most recent committed version of the data, so manual caching only introduces staleness. ^[best-practices-delta-lake-databricks-on-aws.md]

## What to Use Instead

Databricks recommends relying on Delta Lake’s native capabilities rather than Spark caching:

- Use [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md) with [predictive optimization](/concepts/delta-lake-predictive-optimization.md) to automatically compact small files (`OPTIMIZE`) and remove stale data (`VACUUM`). These operations keep the table performant and fresh without manual caching. ^[best-practices-delta-lake-databricks-on-aws.md]
- For repeated queries, rely on Delta Lake’s **transaction log** and **data skipping**—the table always returns the latest committed data. Because Delta Lake uses an optimistic concurrency model, the transaction log provides a consistent view without the overhead of managing a cache. ^[best-practices-delta-lake-databricks-on-aws.md]
- If you need to speed up repeated access to the same subset of data, prefer using **materialized views** or **incremental table maintenance** (e.g., `OPTIMIZE`) rather than Spark caching. These approaches preserve data freshness and maintain the ability to prune data via filters.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The ACID transaction storage layer that eliminates the need for manual caching.
- Data skipping — Automatic pruning of Parquet files based on filter predicates.
- [Predictive optimization](/concepts/predictive-optimization-for-delta-lake.md) — Automated compaction and vacuum for Unity Catalog managed tables.
- Spark caching — Overview of Spark’s in-memory caching mechanisms and their trade-offs.
- OPTIMIZE — Command to compact small files into larger, more readable files.
- VACUUM — Command to remove stale data files that are no longer referenced by the transaction log.

## Sources

- best-practices-delta-lake-databricks-on-aws.md

# Citations

1. [best-practices-delta-lake-databricks-on-aws.md](/references/best-practices-delta-lake-databricks-on-aws-aef26632.md)
