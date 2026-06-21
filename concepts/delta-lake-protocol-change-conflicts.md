---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1b9026263dc5ee5b9b2c5af53c8ec6493bb321944495472a5520dac0cb3a74ce
  pageDirectory: concepts
  sources:
    - delta_concurrent_append-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-protocol-change-conflicts
    - DLPCC
    - delta-lake-protocol-upgrade-conflicts
    - DLPUC
    - delta-lake-table-protocol-upgrade-conflicts
    - DLTPUC
  citations:
    - file: delta_concurrent_append-error-condition-databricks-on-aws.md
title: Delta Lake Protocol Change Conflicts
description: A transaction conflict triggered when a concurrent operation upgrades the table protocol in Delta Lake, requiring the conflicting operation to be retried.
tags:
  - delta-lake
  - protocol
  - transaction-conflicts
timestamp: "2026-06-18T15:17:57.487Z"
---

# Delta Lake Protocol Change Conflicts

**Delta Lake Protocol Change Conflicts** are a sub‑error of the DELTA_CONCURRENT_APPEND error class. They occur when a concurrent transaction upgrades the table protocol while another transaction is in flight. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Error Details

The conflict is identified by the `PROTOCOL_CHANGE` sub‑error identifier. The accompanying message states:

> The concurrent operation upgraded the table protocol. Please retry the operation.

^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Cause

A [Delta Lake](/concepts/delta-lake.md) table has an internal protocol that controls available features (e.g., column mapping, deletion vectors). If one concurrent operation upgrades this protocol, any other writer that started before the upgrade will detect the change at commit time. Delta Lake raises this conflict to inform the writer that the metadata it read is no longer current. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Solution

Retry the transaction. On retry, the operation reads the updated table metadata, including the new protocol version, and can proceed normally. No manual intervention beyond re‑attempting the write is required. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_CONCURRENT_APPEND — Parent error class for Delta Lake write conflicts.
- [Delta Lake Protocol Versioning](/concepts/delta-lake-table-protocol-changes.md) — How the table protocol governs feature support.
- Concurrent Writes in Delta Lake — General concurrency control mechanisms.
- Table Protocol Upgrade — The operation that triggers this conflict (e.g., enabling a new table feature).

## Sources

- delta_concurrent_append-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_append-error-condition-databricks-on-aws.md](/references/delta_concurrent_append-error-condition-databricks-on-aws-47a87778.md)
