---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9eb31dc5f510d49db93701a4f8eaa024ab4381211c939075daf4d7a8cbcc2671
  pageDirectory: concepts
  sources:
    - delta_versions_not_contiguous-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - table-deletion-and-recreation-at-same-s3-location
    - recreation at same S3 location and Table deletion
    - TDARASSL
  citations:
    - file: delta_versions_not_contiguous-error-condition-databricks-on-aws.md
title: Table deletion and recreation at same S3 location
description: A specific operational pattern on AWS S3 that can lead to Delta log gaps due to S3's eventual consistency model when a table is dropped and re-created at the same path.
tags:
  - aws
  - s3
  - operational-patterns
  - delta-lake
timestamp: "2026-06-19T10:10:40.297Z"
---

# Table Deletion and Recreation at Same S3 Location

**Table deletion and recreation at same S3 location** refers to a scenario where a [Delta Lake](/concepts/delta-lake.md) table is dropped and then recreated at the same path in Amazon S3, which can cause data consistency issues due to S3's [eventual consistency](/concepts/s3-eventually-consistent-model.md) model.

## Overview

When a Delta table is deleted and then recreated at the same S3 location, the Delta log may become corrupted. This occurs because S3's eventual consistency guarantees mean that old log files from the deleted table may still be visible to read operations after the new table has been created. The Delta log expects a contiguous sequence of version files, but the presence of stale files from the previous table incarnation can create gaps or conflicts in the version history. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Error Condition

This scenario triggers the `DELTA_VERSIONS_NOT_CONTIGUOUS` error condition. The error message states:

```
Versions (<versionList>) are not contiguous. A gap in the delta log between versions <startVersion> and <endVersion> was detected while trying to load version <versionToLoad>.
```

^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Root Cause

The root cause is S3's eventual consistency model. When a table is deleted and recreated at the same path:

1. The old table's Delta log files (in the `_delta_log` directory) may not be immediately removed or may still be visible to read operations.
2. The new table creates its own Delta log starting from version 0.
3. Due to eventual consistency, readers may see a mix of old and new log files, resulting in non-contiguous version numbers or conflicting metadata.

This issue is specific to AWS S3 and does not apply to Azure Blob Storage or other storage backends with strong consistency guarantees. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Resolution

To resolve this issue, contact Databricks support to repair the table. The repair process involves cleaning up the Delta log to remove stale entries and restore a consistent version history. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Prevention

To avoid this issue, consider the following practices:

- **Use different S3 paths** for different table incarnations rather than reusing the same location.
- **Use table names with unique identifiers** or timestamps to prevent path collisions.
- **Wait for S3 consistency** before recreating a table at the same location, though this is not guaranteed to prevent the issue.
- **Use [Unity Catalog](/concepts/unity-catalog.md) managed tables** which handle table lifecycle and storage management more robustly.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that manages ACID transactions on data lakes
- Delta Log — The transaction log that tracks all changes to a Delta table
- DELTA_VERSIONS_NOT_CONTIGUOUS error|DELTA_VERSIONS_NOT_CONTIGUOUS — The error condition caused by this scenario
- [S3 Eventual Consistency](/concepts/s3-eventually-consistent-model.md) — The underlying consistency model that causes this issue
- [Unity Catalog](/concepts/unity-catalog.md) — Databricks' governance solution that can help manage table lifecycles
- [Table Repair](/concepts/delta-table-repair.md) — The process of fixing corrupted Delta tables

## Sources

- delta_versions_not_contiguous-error-condition-databricks-on-aws.md

# Citations

1. [delta_versions_not_contiguous-error-condition-databricks-on-aws.md](/references/delta_versions_not_contiguous-error-condition-databricks-on-aws-ad1fe2ac.md)
