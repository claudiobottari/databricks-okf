---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a936eff662bcbbde8ac033e68cf9b1bf9b98c221c9cd8a1cff3c202f2acfd32e
  pageDirectory: concepts
  sources:
    - delta_concurrent_append-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-table-protocol-changes
    - DLTPC
    - Delta Lake Protocol Changes
    - Delta Lake table protocol
    - Delta Lake Protocol Versioning
    - Delta Lake protocol version
    - Delta Table Protocol
    - table protocol
    - delta-lake-transaction-protocol-changes
    - Delta Lake Transaction Protocol
    - Delta Lake transaction protocol
    - Delta Transaction Log Protocol
  citations:
    - file: delta_concurrent_append-error-condition-databricks-on-aws.md
title: Delta Lake Table Protocol Changes
description: A concurrent operation upgrading the table protocol version, causing transaction conflicts that require retrying the operation
tags:
  - delta-lake
  - protocol
  - table-versioning
timestamp: "2026-06-19T10:03:30.086Z"
---

---
title: [Delta Lake Table](/concepts/delta-lake-table.md) Protocol Changes
summary: A [Delta Lake Table](/concepts/delta-lake-table.md) protocol change occurs when a concurrent operation upgrades the table protocol version, causing transaction conflicts that require retrying the operation.
sources:
  - delta_concurrent_append-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T09:00:00.000Z"
updatedAt: "2026-06-19T09:00:00.000Z"
tags:
  - delta-lake
  - protocol
  - transaction-conflicts
aliases:
  - delta-lake-table-protocol-changes
  - DLTPC
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# [Delta Lake Table](/concepts/delta-lake-table.md) Protocol Changes

A **Delta Lake table protocol change** refers to a modification of the internal protocol version of a Delta table, typically performed by a concurrent operation. Because the protocol governs how table files, metadata, and operations are interpreted, a protocol upgrade invalidates in-flight transactions that depend on the previous protocol, leading to a transaction conflict. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Context

[Delta Lake](/concepts/delta-lake.md) uses a versioned protocol to manage table semantics. The protocol can be upgraded to enable new features (e.g., column mapping, change data feed, or deletion vectors). When one transaction upgrades the protocol, other concurrent transactions that began before the upgrade may fail with a `DELTA_CONCURRENT_APPEND` error. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Error Condition

The specific error condition for protocol changes is the `PROTOCOL_CHANGE` sub‑error of `DELTA_CONCURRENT_APPEND`. Its error message is:

> The concurrent operation upgraded the table protocol. Please retry the operation.

This indicates that a concurrent transaction committed an upgrade of the table protocol (for example, from protocol version 1 to version 2) while another transaction was in progress. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Resolution

The recommended resolution is to retry the failed operation. Upon retry, the transaction will read the updated protocol and proceed under the new protocol version. No manual intervention is required beyond the retry. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Related Error Conditions

The `DELTA_CONCURRENT_APPEND` error class includes several other sub‑errors that indicate different types of concurrent modifications, such as:

- `ROW_LEVEL_CHANGES` – Same rows modified by another transaction. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]
- `WHOLE_TABLE_REPLACE` – Entire table replaced concurrently. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]
- `PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE` – Conflict with a partitioned table. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

All such errors typically resolve with a retry. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) – The foundation for concurrent conflict detection.
- DELTA_CONCURRENT_APPEND Error Condition|DELTA_CONCURRENT_APPEND error condition – The full error class containing protocol change and other sub‑errors.
- [Optimistic Concurrency Control in Delta Lake](/concepts/delta-lake-optimistic-concurrency-control.md) – How Delta Lake detects and handles conflicts.
- [Delta Lake Protocol Versioning](/concepts/delta-lake-table-protocol-changes.md) – Details on how protocol versions are managed and upgraded.

## Sources

- delta_concurrent_append-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_append-error-condition-databricks-on-aws.md](/references/delta_concurrent_append-error-condition-databricks-on-aws-47a87778.md)
