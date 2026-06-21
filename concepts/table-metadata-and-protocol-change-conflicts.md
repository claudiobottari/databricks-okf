---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3c65c2f9d396fabac584415bc4bff305da9c5c96d434e4e26ac10e2c696b811a
  pageDirectory: concepts
  sources:
    - delta_concurrent_append-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - table-metadata-and-protocol-change-conflicts
    - Protocol Change Conflicts and Table Metadata
    - TMAPCC
  citations:
    - file: delta_concurrent_append-error-condition-databricks-on-aws.md
title: Table Metadata and Protocol Change Conflicts
description: Conflict scenarios where concurrent operations change table metadata (schema, partitioning) or upgrade the table protocol, triggering the DELTA_CONCURRENT_APPEND error.
tags:
  - delta-lake
  - schema-evolution
  - protocol
timestamp: "2026-06-19T18:23:03.330Z"
---

# Table Metadata and Protocol Change Conflicts

**Table Metadata and Protocol Change Conflicts** are a class of transaction conflicts in [Delta Lake](/concepts/delta-lake.md) that occur when a concurrent operation modifies the table's metadata (such as schema or partitioning) or upgrades the table protocol while another transaction is in progress. These conflicts are reported under the `DELTA_CONCURRENT_APPEND` error condition with SQLSTATE 2D521. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Overview

Delta Lake uses [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) to manage concurrent reads and writes. When a transaction reads from a table and a concurrent operation modifies the table's metadata or protocol, the system detects a conflict and raises an error. The specific error sub-type indicates the nature of the metadata or protocol change. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Error Sub-Types

### METADATA_CHANGE

The `METADATA_CHANGE` sub-type occurs when a concurrent operation changes the table metadata — for example, altering the schema or partitioning scheme. The error message states: "The concurrent operation changed the table metadata (for example, schema or partitioning). Please retry the operation." ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### PROTOCOL_CHANGE

The `PROTOCOL_CHANGE` sub-type occurs when a concurrent operation upgrades the table protocol. The error message states: "The concurrent operation upgraded the table protocol. Please retry the operation." ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Resolution

For both `METADATA_CHANGE` and `PROTOCOL_CHANGE` conflicts, the recommended resolution is to retry the operation. The retry will read the updated metadata or protocol version and proceed with the new table state. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Related Error Sub-Types

Other `DELTA_CONCURRENT_APPEND` sub-types that may involve metadata or structural changes include:

- [PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE](/concepts/partitioned-table-merge-conflicts-in-delta-lake.md) – Row-level conflict detection could not be performed on a partitioned table.
- PREDICATES_NEED_REWRITE – Filter predicates could not be applied for row-level conflict detection.
- CHANGE_TYPE_COLUMN – A column named `_change_type` conflicts with Change Data Feed metadata columns.

## Related Concepts

- Delta Lake Transaction Protocol – The underlying protocol that governs table versioning and conflict detection.
- [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) – The concurrency model used by Delta Lake.
- DELTA_CONCURRENT_APPEND Error Condition – The parent error class for all concurrent append conflicts.
- [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) – A feature that can conflict with metadata columns.
- Table Schema Evolution – Operations that modify table schema, triggering metadata change conflicts.

## Sources

- delta_concurrent_append-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_append-error-condition-databricks-on-aws.md](/references/delta_concurrent_append-error-condition-databricks-on-aws-47a87778.md)
