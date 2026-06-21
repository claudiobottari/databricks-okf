---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c50e1db0261cd7ac2889a79d906df0f760ced07ea2711a1cb643e5d5a5a1fa0a
  pageDirectory: concepts
  sources:
    - delta-lake-limitations-on-s3-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - delta-lake-vacuum-and-garbage-collection-on-s3
    - garbage collection on S3 and Delta Lake VACUUM
    - DLVAGCOS
  citations:
    - file: delta-lake-limitations-on-s3-databricks-on-aws.md
title: Delta Lake VACUUM and garbage collection on S3
description: Delta Lake implements its own versioning and garbage collection (including VACUUM), which conflicts with S3 bucket versioning and lifecycle policies that retain deleted files.
tags:
  - delta-lake
  - s3
  - maintenance
  - storage
timestamp: "2026-06-18T11:48:39.897Z"
---

# Delta Lake VACUUM and Garbage Collection on S3

**Delta Lake VACUUM and garbage collection on S3** refers to the process of permanently removing old data files and transaction logs from Delta Lake tables stored in Amazon S3. Delta Lake implements its own versioning and garbage collection mechanisms that interact with S3's native features in specific ways.

## Overview

Delta Lake maintains a transaction log that tracks all changes to a table. Over time, old data files and transaction log entries accumulate. The `VACUUM` command removes these files that are no longer referenced by the current table state, freeing storage space. On S3, this process has important considerations due to the object storage model and potential interactions with S3 bucket versioning. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## VACUUM Behavior on S3

The `VACUUM` command permanently deletes data files that Delta Lake considers obsolete. This includes:

- Data files that are no longer referenced by any table version
- Transaction log files that have been cleaned up during regular [Delta Lake Table](/concepts/delta-lake-table.md) operations

When `VACUUM` runs on a table stored in S3, it issues delete requests to remove the corresponding objects from the bucket. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Interaction with S3 Bucket Versioning

Databricks recommends **not** enabling bucket versioning for buckets that store Delta Lake data, including [Unity Catalog](/concepts/unity-catalog.md) managed tables. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

When bucket versioning is enabled, S3 retains copies of metadata and data files that Databricks considers deleted. This includes files that `VACUUM` would permanently delete and transaction logs cleaned up automatically. The retained versions continue to consume storage space and can lead to increased costs. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

### If You Must Use Bucket Versioning

If you choose to use bucket versioning despite the recommendation, Databricks advises: ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

- Retaining a maximum of **three versions** of each object
- Implementing a lifecycle management policy that retains versions for **7 days or less** for all S3 buckets with versioning enabled

If you encounter performance slowdowns on tables stored in buckets with versioning enabled, mention that bucket versioning is enabled when contacting Databricks support. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Garbage Collection and Performance

Delta Lake's automatic garbage collection cleans up transaction logs during regular table operations. On S3, this process can be affected by:

- **Bucket versioning**: Retained versions of deleted files can slow down listing operations and increase the time required for garbage collection
- **Eventual consistency**: S3's eventually consistent model can cause temporary inconsistencies when multiple systems interact with the same table

## Best Practices

- **Disable bucket versioning** on S3 buckets used for Delta Lake tables to avoid storage bloat and performance issues
- **Use `VACUUM` regularly** to reclaim storage space from obsolete data files
- **Monitor storage costs** to detect unexpected growth that may indicate versioning-related retention
- **Avoid manual file deletion** — do not use `rm -rf` or other direct file removal methods to drop Delta Lake tables, as this can leave stale data and corrupt table metadata

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer providing ACID transactions and versioning
- [VACUUM Command](/concepts/vacuum-command-databricks.md) — The Delta Lake command for removing old data files
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — The log that tracks all table changes
- [S3 Bucket Versioning](/concepts/s3-bucket-versioning-and-delta-lake.md) — AWS feature that retains object versions
- [Unity Catalog](/concepts/unity-catalog.md) — Databricks governance solution that manages Delta Lake tables
- [Multi-cluster writes on S3](/concepts/multi-cluster-write-limitations-on-s3.md) — Limitations when writing to Delta tables from multiple clusters

## Sources

- delta-lake-limitations-on-s3-databricks-on-aws.md

# Citations

1. [delta-lake-limitations-on-s3-databricks-on-aws.md](/references/delta-lake-limitations-on-s3-databricks-on-aws-516e860e.md)
