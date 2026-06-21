---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 48522477e8d317ce6d97fd781381092bd93ccc8c150844dd31babe076ac8c57e
  pageDirectory: concepts
  sources:
    - create-bloom-filter-index-deprecated-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - create-bloom-filter-index-databricks-sql
    - CBFI(S
  citations:
    - file: create-bloom-filter-index-deprecated-databricks-on-aws.md
title: CREATE BLOOM FILTER INDEX (Databricks SQL)
description: The SQL command syntax and usage for creating Bloom filter indexes in Databricks, now deprecated and not recommended for new use.
tags:
  - databricks
  - sql
  - command
  - deprecated
timestamp: "2026-06-18T11:22:06.229Z"
---

#CREATE BLOOM FILTER INDEX (Databricks SQL)

**CREATE BLOOM FILTER INDEX** is a legacy Databricks SQL command used to create a [Bloom Filter Index](/concepts/bloom-filter-index.md) on columns of a Delta table to accelerate queries that filter on those columns. The command is now deprecated and should not be used in new workloads. ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Deprecation Status

The `CREATE BLOOM FILTER INDEX` feature is deprecated as of the latest Databricks Runtime releases. Databricks recommends against creating new Bloom filter indexes and advises migrating existing indexes to alternative, more performant mechanisms. ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Alternatives

Databricks provides two modern replacements that deliver equivalent or better query acceleration without the overhead of manual index management:

- **[Predictive I/O](/concepts/predictive-io.md)** — Automatically skips irrelevant data files during query planning, reducing I/O without requiring explicit indexes. It is the recommended replacement for Bloom filter indexes on most workloads.
- **[Liquid Clustering](/concepts/liquid-clustering.md)** — A dynamic clustering strategy for Delta tables that reorganizes data layout and supports data skipping, improving query performance for selective filters. It supersedes the need for separate Bloom filter indexes.

See [Bloom filter indexes (deprecated)](/concepts/bloom-filter-index-deprecated.md) for a detailed comparison and migration guidance. ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Migration Guidance

If you currently use Bloom filter indexes, Databricks recommends the following migration path:

1. Drop existing Bloom filter indexes with `DROP BLOOM FILTER INDEX`.
2. Enable [Predictive I/O](/concepts/predictive-io.md) on the table or enable [Liquid Clustering](/concepts/liquid-clustering.md) for better data skipping.
3. Validate query performance after migration.

For full details, refer to the official documentation: [Bloom filter indexes (deprecated)](https://docs.databricks.com/aws/en/optimizations/bloom-filters).

## Sources

- create-bloom-filter-index-deprecated-databricks-on-aws.md

# Citations

1. [create-bloom-filter-index-deprecated-databricks-on-aws.md](/references/create-bloom-filter-index-deprecated-databricks-on-aws-ac15d2e3.md)
