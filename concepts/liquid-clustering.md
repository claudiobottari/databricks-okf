---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3629a5096dd23cf0ce7974a63788083bf69098d6e050d6fbcf431aa81e8123ac
  pageDirectory: concepts
  sources:
    - best-practices-delta-lake-databricks-on-aws.md
    - create-bloom-filter-index-deprecated-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - liquid-clustering
    - Use liquid clustering for tables
  citations:
    - file: best-practices-delta-lake-databricks-on-aws.md
    - file: create-bloom-filter-index-deprecated-databricks-on-aws.md
    - file: what-is-delta-lake-in-databricks-databricks-on-aws.md
    - file: tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md
title: Liquid Clustering
description: A Databricks data layout optimization technique recommended for Delta Lake tables to improve query performance.
tags:
  - clustering
  - performance
  - data-layout
timestamp: "2026-06-19T17:40:19.584Z"
---

# Liquid Clustering

**Liquid clustering** is a data layout optimization technique for [Delta Lake](/concepts/delta-lake.md) tables that automatically co-locates related data based on specified clustering keys. It is recommended by Databricks as a modern replacement for deprecated [Bloom filter indexes](/concepts/bloom-filter-indexes.md) and as a general best practice for most Delta Lake workloads.^[best-practices-delta-lake-databricks-on-aws.md, create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Overview

Liquid clustering reorganizes data on write to improve data skipping and query performance. Unlike traditional partitioning, which requires careful planning and can be difficult to change, liquid clustering provides flexible and adaptive data organization that automatically adjusts as data is written and optimized.^[what-is-delta-lake-in-databricks-databricks-on-aws.md]

## Key Benefits

Liquid clustering simplifies data layout management by eliminating the need for predefined partitioning schemes. It automatically clusters data based on specified keys, enabling more efficient query pruning and reducing the number of files that need to be scanned for any given query. This improves read performance, particularly for tables with high-cardinality columns.^[what-is-delta-lake-in-databricks-databricks-on-aws.md]

## Enabling Liquid Clustering

To enable liquid clustering on a [Delta Lake Table](/concepts/delta-lake-table.md), use the `ALTER TABLE` SQL command with the `CLUSTER BY` clause, specifying one or more columns to cluster by. After enabling clustering, use `OPTIMIZE FULL` to apply the clustering to all existing data.^[tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md]

```sql
ALTER TABLE workspace.default.people_10k CLUSTER BY (firstName);
OPTIMIZE FULL workspace.default.people_10k;
```

This example enables clustering on the `firstName` column, which can improve query performance when filtering or grouping by first name.^[tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md]

## Comparison with Alternatives

### Bloom Filter Indexes

Bloom filter indexes have been deprecated in Databricks. Databricks advises users not to create new Bloom filter indexes and to migrate existing workloads to either [Predictive I/O](/concepts/predictive-io.md) or liquid clustering.^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

### Predictive I/O

[Predictive I/O](/concepts/predictive-io.md) is another recommended alternative that reduces I/O by predicting which data files a query needs. Both predictive I/O and liquid clustering serve as modern replacements for Bloom filter indexes, depending on the specific workload requirements.^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## How Liquid Clustering Works

Liquid clustering co-locates related data based on the specified clustering keys. When data is written to a table with liquid clustering enabled, Databricks organizes the data such that rows with similar clustering key values are stored together in the same or adjacent files. This physical colocation enables the query engine to skip irrelevant files more effectively when filtering on clustering key columns.^[what-is-delta-lake-in-databricks-databricks-on-aws.md]

Unlike traditional partitioning, which creates separate directories for each partition value, liquid clustering maintains a flat file structure while still providing efficient data skipping. This avoids issues with partition explosion — where tables with high-cardinality partitions create too many small directories — and allows clustering keys to be changed without rewriting data.^[what-is-delta-lake-in-databricks-databricks-on-aws.md]

## Integration with Other Optimizations

Liquid clustering works well with other Delta Lake optimization features. For example, [Low Shuffle Merge](/concepts/low-shuffle-merge.md) preserves existing data layout optimizations such as liquid clustering on unmodified data, improving merge performance while maintaining clustering benefits.^[best-practices-delta-lake-databricks-on-aws.md]

## Deprecation Context

For users who currently rely on Bloom filter indexes, Databricks recommends adopting either predictive I/O or liquid clustering. Detailed migration guidance is available in the deprecated Bloom filter indexes documentation.^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Related Concepts

- [Bloom filter indexes](/concepts/bloom-filter-indexes.md) – The deprecated feature that liquid clustering replaces
- [Predictive I/O](/concepts/predictive-io.md) – Another recommended alternative to Bloom filter indexes
- [Delta Lake](/concepts/delta-lake.md) – The storage layer on which liquid clustering operates
- Data skipping – The optimization mechanism that liquid clustering enhances
- Optimize data file layout – Related operation for compacting small data files
- [Table partitioning](/concepts/delta-table-partitioning-mismatch.md) – Traditional data organization method that liquid clustering simplifies
- [Low Shuffle Merge](/concepts/low-shuffle-merge.md) – Merge optimization that preserves liquid clustering
- [Predictive optimization](/concepts/predictive-optimization-for-delta-lake.md) – Automated optimization that includes liquid clustering management

## Sources

- best-practices-delta-lake-databricks-on-aws.md
- create-bloom-filter-index-deprecated-databricks-on-aws.md
- tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md
- what-is-delta-lake-in-databricks-databricks-on-aws.md

# Citations

1. [best-practices-delta-lake-databricks-on-aws.md](/references/best-practices-delta-lake-databricks-on-aws-aef26632.md)
2. [create-bloom-filter-index-deprecated-databricks-on-aws.md](/references/create-bloom-filter-index-deprecated-databricks-on-aws-ac15d2e3.md)
3. [what-is-delta-lake-in-databricks-databricks-on-aws.md](/references/what-is-delta-lake-in-databricks-databricks-on-aws-49c98a82.md)
4. [tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md](/references/tutorial-create-and-manage-delta-lake-tables-databricks-on-aws-481179d7.md)
