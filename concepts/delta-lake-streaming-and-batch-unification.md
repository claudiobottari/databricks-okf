---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 77ee42ce5285864b75bd8b06d95c15c63d557936b6fd72c5757dc717e4dac355
  pageDirectory: concepts
  sources:
    - delta-lake-api-reference-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-streaming-and-batch-unification
    - Batch Unification and Delta Lake Streaming
    - DLSABU
    - Streaming and batch unification
  citations:
    - file: delta-lake-api-reference-databricks-on-aws.md
title: Delta Lake Streaming and Batch Unification
description: Delta Lake unifies streaming and batch data processing within a single storage layer.
tags:
  - streaming
  - batch-processing
timestamp: "2026-06-18T11:48:39.490Z"
---

# Delta Lake Streaming and Batch Unification

**Delta Lake Streaming and Batch Unification** is a core principle of [Delta Lake](/concepts/delta-lake.md) that enables data processing systems to treat streaming data and batch data through a single, consistent interface. By unifying these two traditionally separate paradigms, Delta Lake simplifies data architecture, reduces operational complexity, and ensures that data pipelines produce the same correct results regardless of whether they are processing data in real-time or in bulk.

## Overview

In traditional data architectures, streaming and batch processing are often handled by separate systems with different storage formats, processing semantics, and operational tooling. This dual-system approach leads to data silos, inconsistent data quality, and high maintenance overhead as teams must reconcile results between the two pathways.

Delta Lake unifies streaming and batch data processing by providing a single storage layer that supports both modes of operation with the same ACID guarantees and metadata management. This means that a [Delta table](/concepts/delta-lake-table.md) can serve as both a streaming source and a batch sink, and data written by a streaming job is immediately available for batch queries. ^[delta-lake-api-reference-databricks-on-aws.md]

## How Unification Works

Delta Lake achieves streaming and batch unification through several key architectural features:

### ACID Transactions on the Data Lake

Delta Lake brings ACID (Atomicity, Consistency, Isolation, Durability) transactions to [data lakes](/concepts/delta-lake.md), which is the foundation for unifying streaming and batch. Without transactional guarantees, streaming data written into a lake could produce partial or inconsistent results that batch readers would see—a phenomenon known as dirty reads. Delta Lake's transaction log ensures that every write—whether from a streaming micro-batch or a bulk batch load—is committed atomically, providing a consistent view of data across all consumers. ^[delta-lake-api-reference-databricks-on-aws.md]

### Scalable Metadata Handling

Traditional data lakes often struggle with metadata management at scale, especially when handling high-frequency streaming writes. Delta Lake uses [scalable metadata](/concepts/scalable-metadata-handling.md) through its [transaction log](/concepts/delta-transaction-log.md), which can handle millions of small files created by streaming jobs without the performance degradation that would affect Hive-style metadata stores. This enables both streaming and batch workloads to operate efficiently on the same storage layer. ^[delta-lake-api-reference-databricks-on-aws.md]

### Schema Enforcement and Evolution

Streaming and batch pipelines frequently evolve the structure of their data independently. Delta Lake provides schema enforcement to reject writes that do not match the table schema, and schema evolution to allow controlled changes to the schema over time. This means that a streaming job adding new columns can be accommodated without breaking downstream batch consumers that rely on a stable schema. ^[delta-lake-api-reference-databricks-on-aws.md]

### Compatibility with Apache Spark APIs

Delta Lake is fully compatible with Apache Spark APIs, including both the [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) API for processing continuous streams and the batch DataFrame/Dataset API for processing static datasets. This compatibility means that developers can use the same Spark code patterns—such as `DataFrame.readStream` and `DataFrame.writeStream`—to interact with a Delta table, whether the underlying data is arriving in real-time or was written hours ago. ^[delta-lake-api-reference-databricks-on-aws.md]

## Practical Benefits

### Single Source of Truth

When a [Delta table](/concepts/delta-lake-table.md) serves both streaming and batch workloads, it becomes the single source of truth for all data in that domain. Batch reports and streaming dashboards read from the same table, so they produce consistent results. This eliminates the need for late reconciliation between batch and streaming outputs. ^[delta-lake-api-reference-databricks-on-aws.md]

### Simplified Operations

Teams maintain one set of table definitions, one set of data quality checks, and one set of access controls for both streaming and batch workflows. This reduces operational overhead compared to managing separate streaming and batch storage layers. ^[delta-lake-api-reference-databricks-on-aws.md]

### Efficient Streaming-Batch Pipelines

Unification enables hybrid pipelines where streaming data is first ingested into Delta tables, then processed further using batch ETL jobs. Because batch jobs can read the Delta table directly, they avoid the small file problem that plagues traditional streaming-to-batch architectures with many tiny Parquet files. ^[delta-lake-api-reference-databricks-on-aws.md]

## Example Architecture

A common pattern enabled by streaming and batch unification is the lambda architecture simplified to a single layer:

1. **Streaming ingestion**: A Spark Structured Streaming job writes incoming data (e.g., clickstream events, sensor readings) to a Delta table, committing micro-batches every few seconds.
2. **Batch processing**: A scheduled batch job reads from the same Delta table, performing aggregations, joins, and transformations that are then written to a second Delta table (or a Delta Live Tables pipeline).
3. **Serving**: Both streaming and batch outputs are available for downstream consumers—BI tools for historical reporting and real-time dashboards for live monitoring—from the same Delta tables.

This architecture ensures that:
- The streaming and batch views of the data are always consistent.
- When the batch job runs, it sees all records written by the streaming job up to that point.
- No data duplication or manual sync is needed between streaming and batch paths. ^[delta-lake-api-reference-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The open source storage layer that provides the unifiying foundation
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) — The Spark API for processing continuous data streams
- [ACID Transactions](/concepts/delta-acid-transactions.md) — The property that ensures consistency across streaming and batch writes
- [Transaction Log](/concepts/delta-transaction-log.md) — The metadata store that enables ACID and scalable handling of streaming data
- [Delta Lake API Reference](/concepts/delta-lake-api-reference.md) — API documentation for Scala, Java, and Python
- Delta Live Tables — A declarative framework for building streaming-batch pipelines
- [Data Lakehouse](/concepts/avoiding-data-silos-in-lakehouse.md) — The architectural pattern that Delta Lake enables through streaming and batch unification

## Sources

- delta-lake-api-reference-databricks-on-aws.md

# Citations

1. [delta-lake-api-reference-databricks-on-aws.md](/references/delta-lake-api-reference-databricks-on-aws-4e26d809.md)
