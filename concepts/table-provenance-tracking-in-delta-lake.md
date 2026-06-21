---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5486ddc9b8cc74211d73734b8b9d74369b9cc21457c5e6ab958a82a4f710963f
  pageDirectory: concepts
  sources:
    - describe-history-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - table-provenance-tracking-in-delta-lake
    - TPTIDL
  citations:
    - file: describe-history-databricks-on-aws.md
title: Table provenance tracking in Delta Lake
description: Delta Lake automatically records operation type, user identity, and other metadata for every write to a table
tags:
  - delta-lake
  - audit
  - metadata
timestamp: "2026-06-19T15:11:03.919Z"
---

# Table Provenance Tracking in Delta Lake

**Table provenance tracking in Delta Lake** refers to the ability to retrieve historical metadata about every write operation performed on a Delta table. This feature is exposed through the `DESCRIBE HISTORY` SQL command, which returns provenance information including the operation type, user identity, and other operational details for each write to a table. ^[describe-history-databricks-on-aws.md]

## Overview

Delta Lake automatically records a detailed history of all changes made to a table. This history is retained for 30 days, after which older entries are automatically removed. The provenance information enables users to audit table modifications, understand who made changes, and track the evolution of data over time. ^[describe-history-databricks-on-aws.md]

## DESCRIBE HISTORY Command

The `DESCRIBE HISTORY` command is the primary interface for accessing table provenance information. It is available in Databricks SQL and Databricks Runtime. ^[describe-history-databricks-on-aws.md]

### Syntax

```sql
DESCRIBE HISTORY table_name
```

^[describe-history-databricks-on-aws.md]

### Parameters

- **table_name**: Identifies an existing Delta table. The name must not include a temporal specification or options specification. ^[describe-history-databricks-on-aws.md]

### Output

The command returns a table with one row per write operation, containing columns such as:

- **version**: The table version number after the operation
- **timestamp**: When the operation occurred
- **userId**: The user who performed the operation
- **userName**: The user name
- **operation**: The type of operation (e.g., WRITE, MERGE, DELETE, UPDATE)
- **operationParameters**: Parameters specific to the operation
- **job**: Information about the job that ran the operation (if applicable)
- **notebook**: Information about the notebook that ran the operation (if applicable)
- **clusterId**: The cluster that executed the operation
- **readVersion**: The version of the table that was read before the write
- **isolationLevel**: The isolation level used for the operation
- **isBlindAppend**: Whether the operation was a blind append
- **operationMetrics**: Metrics about the operation (e.g., number of files added, number of rows affected)
- **userMetadata**: Optional user-provided metadata

## Retention

Table history is retained for 30 days. After this period, historical entries are automatically purged. This means that provenance information is only available for operations performed within the last 30 days. ^[describe-history-databricks-on-aws.md]

## Use Cases

- **Auditing**: Track who modified data and when
- **Debugging**: Investigate unexpected data changes by reviewing operation history
- **Compliance**: Meet regulatory requirements for data lineage tracking
- **Reproducibility**: Understand the sequence of operations that led to the current table state

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that provides ACID transactions and time travel capabilities
- Time Travel in Delta Lake — Querying previous versions of a table using version numbers or timestamps
- table_changes function|table_changes Function — A SQL function for retrieving row-level changes between table versions
- Work with Table History — Detailed documentation on using table history features
- Delta Lake Operations — The various write operations tracked in table history

## Sources

- describe-history-databricks-on-aws.md

# Citations

1. [describe-history-databricks-on-aws.md](/references/describe-history-databricks-on-aws-c4aeec74.md)
