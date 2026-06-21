---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 22dc4e2d6e5de581784a6c1f6ece1a0a3102e1604727bf8039a42b9ac1df948c
  pageDirectory: concepts
  sources:
    - delta-lake-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - acid-transactions-on-data-lakes
    - ATODL
  citations:
    - file: delta-lake-api-reference-databricks-on-aws.md
title: ACID Transactions on Data Lakes
description: Delta Lake provides ACID (Atomicity, Consistency, Isolation, Durability) transaction guarantees on top of existing data lakes, bringing database-like reliability to data lake storage.
tags:
  - data-lake
  - transactions
  - reliability
timestamp: "2026-06-19T18:20:06.601Z"
---

# ACID Transactions on Data Lakes

**ACID Transactions on Data Lakes** refers to the atomic, consistent, isolated, and durable transaction guarantees provided by [Delta Lake](/concepts/delta-lake.md) on top of existing data lake storage. Delta Lake is an open source storage layer that brings these database‑like guarantees to data lake architectures, making them more reliable for production workloads. ^[delta-lake-api-reference-databricks-on-aws.md]

## Overview

Traditional data lakes lack transactional support, making it difficult to handle concurrent writes, partial failures, or schema changes. Delta Lake addresses this by running on top of your existing data lake and implementing full ACID transactions. This allows multiple readers and writers to work simultaneously without corrupting the data. ^[delta-lake-api-reference-databricks-on-aws.md]

## Key Capabilities

Delta Lake provides three main capabilities beyond ACID transactions:

- **ACID transactions** – Enables atomic, consistent, isolated, and durable operations on data lake tables. ^[delta-lake-api-reference-databricks-on-aws.md]
- **Scalable metadata handling** – Efficiently manages metadata even for large datasets with billions of files. ^[delta-lake-api-reference-databricks-on-aws.md]
- **Unified streaming and batch processing** – Allows batch and streaming workloads to use the same table format, simplifying pipeline design. ^[delta-lake-api-reference-databricks-on-aws.md]

## Integration with Apache Spark

Delta Lake is fully compatible with Apache Spark APIs, meaning you can use existing Spark jobs and DataFrames to read from and write to Delta tables. This compatibility enables a smooth migration from traditional data lake processing to a transactional data lake without changing your compute layer. ^[delta-lake-api-reference-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The open source storage layer that implements ACID transactions.
- data lake – The underlying storage that Delta Lake enhances with transactional guarantees.
- Apache Spark – The compute engine that natively interacts with Delta Lake.
- [streaming and batch data processing](/concepts/unified-streaming-and-batch-processing.md) – Workloads that benefit from the unified format provided by Delta Lake.

## Sources

- delta-lake-api-reference-databricks-on-aws.md

# Citations

1. [delta-lake-api-reference-databricks-on-aws.md](/references/delta-lake-api-reference-databricks-on-aws-4e26d809.md)
