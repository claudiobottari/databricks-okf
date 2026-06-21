---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2b2c6e3896f61814f2eca35b5ee93c146fd8b2cec971085aee8288d63f91e1ba
  pageDirectory: concepts
  sources:
    - delta-lake-api-reference-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-api
    - DLA
    - DeltaTable API
    - delta-lake-api-reference
    - DLAR
    - Delta Lake SQL Reference
    - delta-lake-apis
  citations:
    - file: delta-lake-api-reference-databricks-on-aws.md
title: Delta Lake API
description: The programming interface for interacting with Delta Lake, with API references available for Scala, Java, and Python on the Delta Lake website.
tags:
  - api
  - scala
  - java
  - python
timestamp: "2026-06-19T14:59:32.015Z"
---

# Delta Lake API

The **Delta Lake API** is a set of programmatic interfaces for interacting with [Delta Lake](/concepts/delta-lake.md), an open source storage layer that brings reliability to data lakes. The API provides primitives to create, read, update, and manage Delta Lake tables, and is fully compatible with Apache Spark APIs. ^[delta-lake-api-reference-databricks-on-aws.md]

## Overview

Delta Lake runs on top of an existing data lake and unifies streaming and batch data processing. The Delta Lake API exposes this functionality through Scala, Java, and [Python](/concepts/python-wheel-task.md) bindings, allowing users to leverage [ACID transactions](/concepts/delta-acid-transactions.md), scalable metadata handling, and incremental data processing directly from their Spark applications. ^[delta-lake-api-reference-databricks-on-aws.md]

## API References

The full API documentation for Scala, Java, and Python is hosted on the Delta Lake project website at [docs.delta.io](https://docs.delta.io/latest/delta-apidoc.html#delta-spark). ^[delta-lake-api-reference-databricks-on-aws.md]

For usage guidance on Databricks, refer to the following resources:

- [What is Delta Lake in Databricks?](/concepts/delta-lake-on-databricks.md)
- Tutorial: Create and manage Delta Lake tables
- [Delta Lake API documentation](/concepts/databricks-delta-lake-documentation.md)

## Key Features

The Delta Lake API enables the following capabilities:

- **ACID Transactions**: Atomic, consistent, isolated, and durable operations on data lake tables. ^[delta-lake-api-reference-databricks-on-aws.md]
- **Scalable Metadata Handling**: Efficient management of metadata at scale. ^[delta-lake-api-reference-databricks-on-aws.md]
- **Unified Streaming and Batch Processing**: A single API for both streaming and batch workloads. ^[delta-lake-api-reference-databricks-on-aws.md]
- **Schema Enforcement and Evolution**: Automatic validation and evolution of table schemas.
- **Time Travel**: Access to historical versions of data.
- **Data Compaction and Optimization**: Utilities for maintaining table performance.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The underlying storage layer and its core features.
- Apache Spark – The computation engine the Delta Lake API builds on.
- [ACID Transactions](/concepts/delta-acid-transactions.md) – Atomic, consistent, isolated, durable operations supported by Delta Lake.
- Data Lake – The storage architecture Delta Lake runs on top of.
- [Streaming and Batch Processing](/concepts/unified-streaming-and-batch-processing.md) – Unified data processing supported by the Delta Lake API.
- [Delta Lake Table](/concepts/delta-lake-table.md) – A table format that provides ACID properties on data lakes.
- [Delta Sharing](/concepts/delta-sharing.md) – An open protocol for secure data sharing across platforms.

## Sources

- delta-lake-api-reference-databricks-on-aws.md

# Citations

1. [delta-lake-api-reference-databricks-on-aws.md](/references/delta-lake-api-reference-databricks-on-aws-4e26d809.md)
