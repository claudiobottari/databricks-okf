---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e4516e307e7c7a737c68c710dc1475060855cec472c7d5f898cd4dedc2cc4a70
  pageDirectory: concepts
  sources:
    - delta-lake-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unified-streaming-and-batch-processing-in-delta-lake
    - batch processing in Delta Lake and Unified streaming
    - USABPIDL
  citations:
    - file: delta-lake-api-reference-databricks-on-aws.md
title: Unified streaming and batch processing in Delta Lake
description: Delta Lake's capability to unify streaming and batch data processing under a single storage layer, simplifying data pipeline architectures.
timestamp: "2026-06-19T09:59:41.738Z"
---

# Unified Streaming and Batch Processing in Delta Lake

**Unified streaming and batch processing in Delta Lake** refers to the storage layer’s ability to handle both real-time streaming data and traditional batch data using the same set of tables and APIs, eliminating the need for separate pipelines or infrastructure for each mode.

## Overview

Delta Lake is an open source storage layer that brings reliability to data lakes. Among its core capabilities, it unifies streaming and batch data processing, allowing developers to write and read data in both modes from the same Delta tables without manual reconciliation. ^[delta-lake-api-reference-databricks-on-aws.md]

## Key Features Supporting Unification

The unification is made possible by two other foundational features of Delta Lake, both mentioned in the same source:

- **ACID transactions**: Delta Lake provides atomic, consistent, isolated, and durable transactions. This ensures that concurrent streaming and batch writes do not corrupt data and that readers always see a consistent snapshot. ^[delta-lake-api-reference-databricks-on-aws.md]
- **Scalable metadata handling**: Delta Lake can efficiently manage metadata for tables with billions of partitions or files, which is essential when both streaming micro-batches and large batch jobs frequently update the table’s state. ^[delta-lake-api-reference-databricks-on-aws.md]

By combining these two properties with the unified processing model, Delta Lake enables a single copy of data to serve both real-time and analytical workloads.

## Benefits

- **Simplified architecture**: Teams no longer need separate “speed layers” and “batch layers”; one Delta table can serve as the source of truth for both streaming and batch jobs.
- **Consistent semantics**: The same ACID guarantees apply regardless of whether data arrives in micro-batches or large bulk loads.
- **Reduced operational overhead**: Updating metadata structures and managing file compaction is handled consistently across both processing modes.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The overall storage layer that enables this unification.
- [ACID transactions](/concepts/delta-acid-transactions.md) – The transactional guarantees that make concurrent streaming and batch writes safe.
- [Scalable Metadata Handling](/concepts/scalable-metadata-handling.md) – The mechanism that supports high-frequency updates from streaming.
- [Streaming vs. Batch Processing](/concepts/unified-streaming-and-batch-processing.md) – The traditional dichotomy that Delta Lake bridges.
- [Delta Lake on Databricks](/concepts/delta-lake-on-databricks.md) – The managed service that simplifies deployment.

## Sources

- delta-lake-api-reference-databricks-on-aws.md

# Citations

1. [delta-lake-api-reference-databricks-on-aws.md](/references/delta-lake-api-reference-databricks-on-aws-4e26d809.md)
