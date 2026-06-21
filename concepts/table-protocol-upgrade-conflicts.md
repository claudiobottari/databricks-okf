---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4153554a8b264658cde50c05459114e35d6a4b01b5ae05d7fe6e8995affa3a2a
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - table-protocol-upgrade-conflicts
    - TPUC
    - TPU
  citations:
    - file: delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
title: Table Protocol Upgrade Conflicts
description: A conflict condition where a concurrent operation upgraded the table protocol, invalidating the current transaction's assumptions and requiring a retry.
tags:
  - delta-lake
  - protocol
  - schema-evolution
timestamp: "2026-06-19T15:03:19.711Z"
---

# Table Protocol Upgrade Conflicts

**Table Protocol Upgrade Conflicts** occur when a concurrent [Delta Lake](/concepts/delta-lake.md) transaction upgrades the protocol version of a table while another transaction (such as a `DELETE`, `UPDATE`, or `MERGE`) is attempting to modify data in that same table. This conflict is a specific subtype of the larger DELTA_CONCURRENT_DELETE_DELETE Error Class|DELTA_CONCURRENT_DELETE_DELETE error class and is identified by the error sub‑type `PROTOCOL_CHANGE`. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Error Message

When a table protocol upgrade conflict is detected, the system returns the following error description:

> The concurrent operation upgraded the table protocol. Please retry the operation.

The full error condition is reported as:

```
DELTA_CONCURRENT_DELETE_DELETE.PROTOCOL_CHANGE
```

^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Cause

A table protocol upgrade (for example, enabling a new feature such as change data feed or deletion vectors) changes the metadata and protocol version of the Delta table. If another concurrent transaction that performs a delete – or any modification that uses row‑level conflict detection – has already started but not yet committed, the protocol upgrade conflicts with the pending modification. The database cannot safely apply both operations simultaneously, so it aborts the modifying transaction to prevent data corruption or inconsistent table state. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Solution

The recommended resolution is to **retry the operation**. Because protocol upgrades are performed by a separate concurrent transaction, the conflicting delete transaction can be re‑executed after the upgrade completes. The retry will operate against the newly upgraded table protocol without conflict. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### Best Practices

- **Sequence upgrades during low‑activity windows** to reduce the likelihood of concurrent conflicts.
- **Use retry logic in application code** (e.g., exponential backoff) to automatically recover from transient protocol change conflicts.
- **Assess whether the protocol upgrade is necessary** before running long‑running modification transactions in parallel.

## Related Concepts

- [Delta Lake table protocol](/concepts/delta-lake-table-protocol-changes.md) – The versioned metadata protocol that governs table capabilities.
- Concurrent write conflicts – Various conflict types that can arise during parallel Delta Lake transactions.
- DELTA_CONCURRENT_DELETE_DELETE Error Class|DELTA_CONCURRENT_DELETE_DELETE error class – The broader error class covering delete‑related transaction conflicts.
- [Transaction isolation in Delta Lake](/concepts/acid-transactions-in-data-lakes.md) – How Delta Lake ensures serializable isolation for concurrent operations.
- Retry patterns for Delta Lake – Common strategies for handling transient transaction conflicts.

## Sources

- delta_concurrent_delete_delete-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_delete-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_delete-error-condition-databricks-on-aws-6fcec7a7.md)
