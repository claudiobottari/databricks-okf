---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b34d9c1c50b3b08d347ff33b6c2c5d1fd4369ea2c5c148947e45669a71d15851
  pageDirectory: concepts
  sources:
    - create-bloom-filter-index-deprecated-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - liquid-clustering-databricks
    - LC(
  citations:
    - file: create-bloom-filter-index-deprecated-databricks-on-aws.md
title: Liquid Clustering (Databricks)
description: A Databricks table clustering feature recommended as a replacement for deprecated Bloom filter indexes.
tags:
  - optimization
  - databricks
  - clustering
timestamp: "2026-06-19T09:36:07.039Z"
---

Here is the wiki page for "Liquid Clustering (Databricks)", based solely on the provided source material.

---

## Liquid Clustering (Databricks)

**Liquid Clustering** is a data layout optimization technique on Databricks that replaces legacy methods such as [Bloom filter indexes (deprecated)](/concepts/bloom-filter-index-deprecated.md) and Hive-style partitioning for improving query performance. It is the recommended alternative to both deprecated features, offering a more flexible and automated approach to organizing data in [Delta Lake](/concepts/delta-lake.md) tables. ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

### Overview

Liquid Clustering dynamically organizes data within a table based on specified clustering keys. This organization improves read performance by allowing queries to skip irrelevant data files, similar to the goal of a bloom filter index, but without requiring manual index creation or maintenance. ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

### Benefits Over Legacy Approaches

- **Replaces Bloom Filter Indexes**: Bloom filter indexes are deprecated. Administrators should not create new Bloom filter indexes and should migrate existing workloads to Liquid Clustering for continued optimization and support. ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]
- **Replaces Hive-style Partitioning**: Liquid Clustering can also serve as a replacement for traditional partitioning schemes, particularly for tables with high-cardinality or frequently changing partition columns, as it avoids the overhead of managing a fixed partition layout.

### How It Works

Liquid Clustering automatically co-locates data with similar clustering key values into the same files. As data is written or rewritten (through operations like `OPTIMIZE`), the clustering layout is maintained without manual intervention. This contrasts with static partitioning, where the partition structure is predetermined and must be specified at table creation. ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

### When to Use Liquid Clustering

Liquid Clustering is suitable for tables where query patterns involve filtering on specific columns. It is particularly effective for:

- **Replacing deprecated indexing features**: Migrate from Bloom filter indexes to Liquid Clustering. ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]
- **Replacing or augmenting partition layouts**: When a table’s partition column is frequently updated or has very high cardinality, leading to too many small files or partition management overhead.

For specific migration guidance from Bloom filter indexes, refer to the official documentation on [Bloom filter indexes (deprecated)](/concepts/bloom-filter-index-deprecated.md).

### Related Concepts

- [Predictive I/O](/concepts/predictive-io.md) – Another optimization technique that can be used in conjunction with or as an alternative to clustering.
- [Bloom filter indexes (deprecated)](/concepts/bloom-filter-index-deprecated.md) – The legacy feature that Liquid Clustering replaces.
- [Delta Lake](/concepts/delta-lake.md) – The storage layer that provides the foundation for Liquid Clustering.
- OPTIMIZE command – The operation that triggers the physical reorganization of data to maintain the clustering layout.

### Sources

- create-bloom-filter-index-deprecated-databricks-on-aws.md

# Citations

1. [create-bloom-filter-index-deprecated-databricks-on-aws.md](/references/create-bloom-filter-index-deprecated-databricks-on-aws-ac15d2e3.md)
