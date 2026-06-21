---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3d845e45c82c8c94ba549f769dcbb8a450a21c424bcbcbf3ecf08388a2f17b42
  pageDirectory: concepts
  sources:
    - delta-lake-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unified-streaming-and-batch-processing
    - Batch Processing and Unified Streaming
    - USABP
    - Streaming and Batch Processing
    - Batch processing
    - Streaming vs. Batch Processing
    - streaming and batch data processing
  citations:
    - file: delta-lake-api-reference-databricks-on-aws.md
title: Unified Streaming and Batch Processing
description: Delta Lake enables a unified approach to stream and batch data processing, allowing users to treat streaming and batch data pipelines with the same table abstractions and semantics.
tags:
  - streaming
  - batch-processing
  - data-pipeline
timestamp: "2026-06-19T18:20:20.352Z"
---

```markdown
---
title: Unified Streaming and Batch Processing
summary: Delta Lake's capability to treat streaming and batch data uniformly, allowing the same table to serve both workloads seamlessly.
sources:
  - delta-lake-api-reference-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T15:15:01.831Z"
updatedAt: "2026-06-18T15:15:01.831Z"
tags:
  - streaming
  - batch-processing
  - data-processing
aliases:
  - unified-streaming-and-batch-processing
  - Batch Processing and Unified Streaming
  - USABP
confidence: 1
provenanceState: extracted
inferredParagraphs: 3
---

# Unified Streaming and Batch Processing

**Unified Streaming and Batch Processing** is a property of [[Delta Lake]] that enables processing real-time streaming data and historical batch data using the same storage layer, table definitions, and APIs.^[delta-lake-api-reference-databricks-on-aws.md]

Delta Lake is an open‑source storage layer that brings reliability to data lakes. It provides ACID transactions, scalable metadata handling, and unifies streaming and batch data processing. It runs on top of existing data lakes and is fully compatible with Apache Spark APIs.^[delta-lake-api-reference-databricks-on-aws.md]

This eliminates the need for separate systems or codebases for streaming and batch workloads, simplifying data pipeline architecture.

## Key Capabilities

Delta Lake provides ACID transactions and scalable metadata handling, ensuring consistency and performance whether writes are made via streaming or batch jobs.^[delta-lake-api-reference-databricks-on-aws.md]

- **ACID transactions** – Guarantees data reliability for concurrent streaming and batch writes.
- **Scalable metadata handling** – Efficiently manages metadata for high-frequency streaming updates and large batch updates.
- **Same table, multiple modes** – A single Delta table can serve as both a batch-read source for historical analysis and a streaming sink for real-time ingestion, using the same API calls.

## Benefits

Using a unified model reduces architectural complexity and maintenance overhead. Batch and streaming pipelines share the same schema enforcement, evolution rules, and transaction guarantees. This consistency is valuable in production environments where data arrives both in bulk (batches) and incrementally (streams).

## Use Cases

- **Real-time dashboards with historical context** – Ingest streaming events into a Delta table while running batch aggregations over the same table for long-term trends.
- **Incremental processing pipelines** – Process new data as it arrives (streaming) and periodically backfill or recalculate older data (batch) without duplicating infrastructure.
- **Unified lakehouse architecture** – Store all data, whether from live streams or periodic batch uploads, in Delta tables managed under the same processing framework.

## Related Concepts

- [[Delta Lake]] – The open‑source storage layer that provides unified streaming and batch processing.
- [[ACID Transactions in Data Lakes|ACID Transactions in Delta Lake]] – Ensures reliability during concurrent streaming and batch writes.
- Apache Spark APIs – The programming interface for building both streaming and batch pipelines on Delta tables.
- Structured Streaming in Apache Spark – The streaming engine commonly used with Delta Lake.
- Schema Enforcement and Evolution – Applies uniformly to streaming and batch operations.

## Sources

- delta-lake-api-reference-databricks-on-aws.md
```

# Citations

1. [delta-lake-api-reference-databricks-on-aws.md](/references/delta-lake-api-reference-databricks-on-aws-4e26d809.md)
