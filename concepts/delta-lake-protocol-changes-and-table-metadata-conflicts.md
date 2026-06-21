---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e3c2372a1ddec2db8c94ec4c0afb1cab6ac28b114d4dfb76e4118cf12129e104
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_read-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - delta-lake-protocol-changes-and-table-metadata-conflicts
    - table metadata conflicts and Delta Lake protocol changes
    - DLPCATMC
  citations:
    - file: delta_concurrent_delete_read-error-condition-databricks-on-aws.md
title: Delta Lake protocol changes and table metadata conflicts
description: A concurrency conflict type where a concurrent operation upgrades the table protocol or changes table metadata (schema, partitioning), invalidating an in-progress transaction.
tags:
  - delta-lake
  - protocol
  - schema-evolution
timestamp: "2026-06-19T10:04:58.684Z"
---

---
title: Delta Lake protocol changes and table metadata conflicts
summary: A classification of Delta Lake concurrent-write conflicts where a parallel operation upgrades the table protocol or changes schema, partitioning, or other metadata, causing the current transaction to fail.
sources:
  - delta_concurrent_delete_read-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-21T12:00:00.000Z"
updatedAt: "2026-06-21T12:00:00.000Z"
tags:
  - delta-lake
  - transactions
  - error-handling
  - concurrency
aliases:
  - delta-lake-protocol-changes-and-table-metadata-conflicts
  - DLPCTMC
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Delta Lake protocol changes and table metadata conflicts

**Delta Lake protocol changes and table metadata conflicts** are a category of the `DELTA_CONCURRENT_DELETE_READ` error that occurs when a concurrent [Delta Lake](/concepts/delta-lake.md) transaction modifies the table’s protocol version, schema, partitioning, or other structural metadata while another transaction is in progress. The conflicting operation prevents the current transaction from committing, requiring a retry. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Protocol upgrade conflicts

### PROTOCOL_CHANGE

A concurrent operation upgraded the table protocol (for example, changed the Delta Lake reader or writer protocol version). The current transaction must be retried because it read data under an older protocol version that is no longer valid. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

```
The concurrent operation upgraded the table protocol. Please retry the operation.
```

## Metadata change conflicts

### METADATA_CHANGE

A concurrent operation changed the table metadata, such as the schema or partitioning scheme. The current transaction cannot proceed because its view of the table structure no longer matches the committed state. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

```
The concurrent operation changed the table metadata (for example, schema or partitioning). Please retry the operation.
```

Note: In the source error class listing, this sub-condition is not assigned a separate heading — it is described in the prose after the `EMPTY_READ_PREDICATES` entry. It is a distinct metadata-conflict reason. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Resolution

All metadata and protocol conflicts share the same recommended remedy:

- **Retry the operation**. The conflicting concurrent transaction has already committed; the failed transaction can safely re-read the latest table state and proceed. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

No user code change is required beyond implementing a retry loop in the application or query engine. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Related concepts

- Delta Lake transaction protocol – The reader/writer protocol version that governs table behavior.
- [Delta Lake concurrency control](/concepts/delta-lake-optimistic-concurrency-control.md) – Overview of optimistic concurrency and conflict detection.
- DELTA_CONCURRENT_DELETE_READ Error|DELTA_CONCURRENT_DELETE_READ error – The parent error class for all Delta concurrent-read/write conflicts.
- [Row-Level Conflict Resolution](/concepts/row-level-conflict-resolution.md) – The mechanism that resolves conflicts at the row level when supported.
- ALLOTTED_TIME_EXCEEDED Sub-error|Allotted time exceeded – A sub-condition where row-level conflict detection itself timed out.

## Sources

- delta_concurrent_delete_read-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_read-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_read-error-condition-databricks-on-aws-d0015916.md)
