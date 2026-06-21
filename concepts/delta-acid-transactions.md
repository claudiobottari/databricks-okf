---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 43c7ca67b0d9f2abd9f10c2599631c045606b44db88635a1c979141764928328
  pageDirectory: concepts
  sources:
    - delta-lake-api-reference-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-acid-transactions
    - DAT
    - ACID Transactions
    - ACID transactions
    - Delta Lake ACID Transactions
    - Delta Lake ACID transactions
    - ACID transaction
    - Delta Lake Transactions
    - Transactions
  citations:
    - file: delta-lake-api-reference-databricks-on-aws.md
title: Delta ACID Transactions
description: Delta Lake provides ACID transaction support to data lakes, ensuring data reliability and consistency.
tags:
  - transactions
  - data-reliability
timestamp: "2026-06-18T11:48:29.032Z"
---

# Delta ACID Transactions

**Delta ACID Transactions** refer to the transactional guarantees (Atomicity, Consistency, Isolation, Durability) provided by [Delta Lake](/concepts/delta-lake.md), the open source storage layer that brings reliability to data lakes. Delta Lake runs on top of existing data lakes and is fully compatible with Apache Spark APIs. ^[delta-lake-api-reference-databricks-on-aws.md]

Delta Lake’s ACID transactions ensure that concurrent reads and writes are consistent and isolated, preventing partial writes or corrupted data. In addition to ACID transactions, Delta Lake offers scalable metadata handling and unifies streaming and batch data processing. ^[delta-lake-api-reference-databricks-on-aws.md]

The four ACID properties as implemented by Delta Lake:

- **Atomicity** – Each transaction (write, delete, merge) is all-or-nothing; partial failures are rolled back.
- **Consistency** – Data constraints and schema validation are enforced after every transaction.
- **Isolation** – Concurrent operations see a consistent snapshot; writes do not interfere with active reads.
- **Durability** – Committed data is persisted to storage and survives system failures.

These guarantees make Delta Lake suitable for workloads that require reliability and correctness, from batch ETL pipelines to real-time streaming applications.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The open source storage layer that provides ACID transactions
- ACID – The standard set of transactional properties
- Data Lake – The underlying storage architecture
- Apache Spark – The compute engine fully compatible with Delta Lake
- [Delta Lake API](/concepts/delta-lake-api.md) – The programming interfaces for Scala, Java, and Python

## Sources

- delta-lake-api-reference-databricks-on-aws.md

# Citations

1. [delta-lake-api-reference-databricks-on-aws.md](/references/delta-lake-api-reference-databricks-on-aws-4e26d809.md)
