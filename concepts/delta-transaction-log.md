---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 253e4311ec66e678398d029bae0640b763e154fa9ad5ad5bc03f960270eb4637
  pageDirectory: concepts
  sources:
    - delta_versions_not_contiguous-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-transaction-log
    - DTL
    - Transaction Log
    - Transaction log
    - transaction log
  citations:
    - file: delta-lake-on-databricks-overview-databricks-on-aws.md
    - file: delta_versions_not_contiguous-error-condition-databricks-on-aws.md
title: Delta transaction log
description: The commit log that records all changes made to a Delta table in sequential version order.
tags:
  - delta-lake
  - architecture
timestamp: "2026-06-19T18:29:08.884Z"
---

# Delta Transaction Log

The **Delta transaction log** is the core mechanism that enables [Delta Lake](/concepts/delta-lake.md) to provide ACID transactions, scalable metadata handling, and time travel capabilities. It serves as a single source of truth for tracking all changes made to a Delta table, recording every operation in the order they occur.

## Overview

The Delta transaction log is an ordered record of every transaction performed on a Delta table. It is stored as a series of JSON files (called "delta files") within a `_delta_log` directory at the root of the table's storage location. Each transaction corresponds to a single commit, and the log maintains a strict ordering of these commits. The transaction log allows Delta Lake to provide ACID transactions, scalable metadata handling, and data versioning through time travel. ^[delta-lake-on-databricks-overview-databricks-on-aws.md]

## How It Works

When a write operation is performed on a Delta table, Delta Lake follows a two-step process:

1. **Check for conflicts**: Delta Lake checks the transaction log to ensure no conflicting operations have been committed since the operation started.
2. **Commit the transaction**: If no conflict is detected, Delta Lake writes a new ordered commit file (e.g., `0000001.json`) to the `_delta_log` directory. If a conflict is detected, the operation is retried.

This process implements an [optimistic concurrency control](/concepts/delta-lake-optimistic-concurrency-control.md) protocol, which allows multiple writers to operate on the same Delta table simultaneously while maintaining data consistency. ^[delta-lake-on-databricks-overview-databricks-on-aws.md]

## Commit Files

Each commit in the transaction log is a JSON file named with a zero-padded incrementing integer (e.g., `00000000000000000001.json`). These files contain:

- The set of **actions** performed in the transaction, such as adding or removing files (data files in Parquet format)
- **Transaction metadata**, including the operation type and timestamp
- **Schema updates**, if the transaction involved a schema change

The log files are written atomically, meaning a reader will either see a complete commit file or not see it at all. ^[delta-lake-on-databricks-overview-databricks-on-aws.md]

## Checkpoint Files

To improve read performance, Delta Lake periodically creates a **checkpoint file** that contains a full snapshot of the entire state of the table at a given version. This checkpoint includes all actions from the transaction log condensed into a single file, typically in Parquet format for efficient storage and retrieval. Checkpoint files allow Delta Lake to quickly reconstruct the state of a table without replaying every single transaction from the beginning. ^[delta-lake-on-databricks-overview-databricks-on-aws.md]

## Contiguous Versions Requirement

For Delta Lake to operate correctly, the versions in the transaction log must be contiguous — there must be no gaps between commit versions. If a gap is detected, Delta Lake raises the `DELTA_VERSIONS_NOT_CONTIGUOUS` error condition. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

This error can occur when files have been manually removed from the Delta log, or in AWS environments, due to [S3 eventual consistency](/concepts/s3-eventually-consistent-model.md) when a table is deleted and recreated at the same location. When this happens, users must contact Databricks support to repair the table. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Key Capabilities Enabled by the Transaction Log

### ACID Transactions
The transaction log ensures that all operations on a Delta table are atomic, consistent, isolated, and durable. Multiple concurrent readers and writers can safely access the same table. ^[delta-lake-on-databricks-overview-databricks-on-aws.md]

### Time Travel
Because every change is recorded in the transaction log, users can query previous versions of a table using version numbers or timestamps. This enables data audit trails and reproducibility. ^[delta-lake-on-databricks-overview-databricks-on-aws.md]

### Scalable Metadata Handling
The transaction log stores metadata as files rather than in a centralized [Metastore](/concepts/metastore.md), allowing Delta Lake to handle metadata for very large tables (petabyte-scale) efficiently. ^[delta-lake-on-databricks-overview-databricks-on-aws.md]

### Schema Evolution
Schema changes are recorded in the transaction log, allowing tables to evolve over time while maintaining a consistent view of the data lineage. ^[delta-lake-on-databricks-overview-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The open-source storage layer that relies on the transaction log
- [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) — The protocol used for conflict detection
- [ACID Transactions](/concepts/delta-acid-transactions.md) — The transactional guarantees provided by the log
- Time Travel in Delta Lake — Querying historical versions using the log
- Checkpointing — Performance optimization for log replay
- Parquet — The columnar storage format used for checkpoint files and data files
- DELTA_VERSIONS_NOT_CONTIGUOUS error condition — Error when log versions are not sequential

## Sources

- delta-lake-on-databricks-overview-databricks-on-aws.md
- delta_versions_not_contiguous-error-condition-databricks-on-aws.md

# Citations

1. delta-lake-on-databricks-overview-databricks-on-aws.md
2. [delta_versions_not_contiguous-error-condition-databricks-on-aws.md](/references/delta_versions_not_contiguous-error-condition-databricks-on-aws-ad1fe2ac.md)
