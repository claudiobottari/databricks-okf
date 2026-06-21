---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cb44dad497dc5a27e18c89c158cc4b6e0c61a54a1c9b985190ef308d4d183028
  pageDirectory: concepts
  sources:
    - delta_clone_incompatible_source-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - has_indexes
    - HAS_INDEXES
    - HAS_INDEXES error
    - Indexes
    - has_indexes-delta-clone-sub-error
    - H(CS
    - HAS_INDEXES (Delta Clone sub-error)
    - has_indexes-error-condition
    - HEC
    - has_indexes-sub-error
  citations:
    - file: delta_clone_incompatible_source-error-condition-databricks-on-aws.md
title: HAS_INDEXES
description: A subclass of DELTA_CLONE_INCOMPATIBLE_SOURCE error indicating the source table has indexes that must be dropped before cloning can succeed.
tags:
  - databricks
  - delta-lake
  - error-handling
  - indexes
timestamp: "2026-06-19T18:22:18.277Z"
---

# HAS_INDEXES

**HAS_INDEXES** is an error condition that occurs when attempting to clone a Delta table whose source has valid Delta format but contains indexes, which are unsupported for Delta clone operations. The error message identifies the table and the specific indexes that must be dropped before the clone can proceed. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Error Message

The full error reads:

```
Table `<tableName>` has indexes: `<indexNames>`. Drop the indexes before cloning.
```

^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Context

This error is a subclass of `DELTA_CLONE_INCOMPATIBLE_SOURCE`, which is raised when the clone source has a valid format but uses a feature that Delta does not support. Indexes are not natively supported in Delta tables, so tables that have been created or altered with indexes (e.g., from an external system or a previous schema evolution) must have those indexes removed before a clone operation can succeed. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Resolution

To resolve the error, drop all listed indexes from the source table. The exact SQL command depends on the indexing method used (e.g., `ALTER TABLE ... DROP INDEX` for standard SQL indexes, or dropping constraints in Databricks). After the indexes are removed, the clone operation can be retried. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The underlying storage format for Delta tables.
- CLONE (Delta Lake) – The operation that triggers this error.
- DELTA_CLONE_INCOMPATIBLE_SOURCE – The parent error class for cloning incompatible sources.
- HAS_INDEXES|Indexes – General concept of indexes in data systems.
- DROP INDEX – SQL command to remove an index.

## Sources

- delta_clone_incompatible_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_incompatible_source-error-condition-databricks-on-aws.md](/references/delta_clone_incompatible_source-error-condition-databricks-on-aws-b63ca67d.md)
