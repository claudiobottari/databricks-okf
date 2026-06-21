---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 632650350a751bcc4d757747510cfad74a17742c92d17fc3d22d52e1a3137040
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - protocol-and-metadata-conflicts-in-delta-lake
    - metadata conflicts in Delta Lake and Protocol
    - PAMCIDL
  citations:
    - file: delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
      start: 24
      end: 25
    - file: delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
      start: 14
      end: 17
title: Protocol and metadata conflicts in Delta Lake
description: Transaction conflicts triggered by concurrent operations that change the table protocol version, schema, or partitioning metadata, requiring a retry.
tags:
  - delta-lake
  - protocol
  - schema-evolution
timestamp: "2026-06-19T10:04:03.433Z"
---

# Protocol and Metadata Conflicts in Delta Lake

**Protocol and metadata conflicts** in [Delta Lake](/concepts/delta-lake.md) occur when a concurrent operation changes the table’s protocol version or metadata (such as schema or partitioning) while another transaction is attempting to delete data from the same table. These conflicts are a subtype of transaction conflicts raised by the DELTA_CONCURRENT_DELETE_DELETE Error Class|DELTA_CONCURRENT_DELETE_DELETE error class.  

When such a conflict is detected, Delta Lake cannot safely resolve the operation automatically and returns an error instructing the user to retry the operation. The retry re-reads the updated table state and allows the transaction to proceed on the current protocol or metadata. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md:24-25]

---

## Subconditions

### PROTOCOL_CHANGE

The concurrent operation upgraded the table protocol. This happens when a separate writer modifies the table’s [Delta Lake protocol version](/concepts/delta-lake-table-protocol-changes.md) (e.g., enabling new features like change data feed or column mapping) between the read and write phases of the current delete transaction. The conflict is raised to prevent the transaction from operating on stale protocol expectations. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md:24-25]

### Metadata Change (EMPTY_READ_PREDICATES Subcondition)

The concurrent operation changed the table metadata, for example altering the schema or [partitioning](/concepts/delta-table-partitioning-mismatch.md) scheme. In the source material, this case is documented under the `EMPTY_READ_PREDICATES` subcondition of `DELTA_CONCURRENT_DELETE_DELETE`:

> The concurrent operation changed the table metadata (for example, schema or partitioning). Please retry the operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md:14-17]

Note that the `EMPTY_READ_PREDICATES` subcondition has two distinct causes: (1) the transaction performed a full table delete with no filters, and (2) a concurrent metadata change. The metadata change variant is the one relevant to this page.

---

## Resolution

The recommended resolution for both protocol and metadata conflicts is to **retry the operation**. A retry triggers Delta Lake’s read-write conflict detection cycle: the transaction re-reads the latest table state (including the updated protocol or metadata), re-evaluates the delete predicates if any, and attempts write again. This is typically safe because the conflicting change is now visible to the retried transaction. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md:24-25] ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md:14-17]

In the case of metadata changes, the source material also advises filtering the query to narrow the data scope before retrying, though this is primarily aimed at the “whole table read” aspect of the subcondition rather than the metadata change itself.

---

## Related Concepts

- Delta Lake protocol version management
- Schema evolution and enforcement in Delta Lake
- Partitioning strategies for Delta Lake
- [Transaction conflict resolution](/concepts/row-level-conflict-resolution.md)
- DELTA_CONCURRENT_DELETE_DELETE Error Class|DELTA_CONCURRENT_DELETE_DELETE error class
- [Concurrent write operations](/concepts/concurrent-copy-into-invocations.md)

---

## Sources

- delta_concurrent_delete_delete-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_delete-error-condition-databricks-on-aws.md:24-25](/references/delta_concurrent_delete_delete-error-condition-databricks-on-aws-6fcec7a7.md)
2. [delta_concurrent_delete_delete-error-condition-databricks-on-aws.md:14-17](/references/delta_concurrent_delete_delete-error-condition-databricks-on-aws-6fcec7a7.md)
