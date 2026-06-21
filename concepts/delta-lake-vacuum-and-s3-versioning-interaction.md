---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 49087974bd45b93d4e1d61dbbfff45e0ba41f869299760d76354c010bba0770b
  pageDirectory: concepts
  sources:
    - delta-lake-limitations-on-s3-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-vacuum-and-s3-versioning-interaction
    - S3 Versioning Interaction and Delta Lake VACUUM
    - DLVASVI
  citations:
    - file: delta-lake-limitations-on-s3-databricks-on-aws.md
      start: 19
      end: 24
    - file: delta-lake-limitations-on-s3-databricks-on-aws.md
      start: 12
      end: 17
    - file: delta-lake-limitations-on-s3-databricks-on-aws.md
      start: 26
      end: 28
    - file: delta-lake-limitations-on-s3-databricks-on-aws.md
      start: 30
      end: 32
title: Delta Lake VACUUM and S3 Versioning Interaction
description: When S3 bucket versioning is enabled, VACUUM operations and automatic transaction log cleanup in Delta Lake do not permanently delete files; S3 retains older versions.
tags:
  - delta-lake
  - s3
  - vacuum
  - garbage-collection
timestamp: "2026-06-19T10:00:15.316Z"
---

# Delta Lake VACUUM and S3 Versioning Interaction

**Delta Lake VACUUM and S3 Versioning Interaction** describes how enabling Amazon S3 bucket versioning affects the Delta Lake `VACUUM` command and the automatic cleanup of transaction logs. Because both Delta Lake and S3 implement their own versioning mechanisms, enabling S3 versioning can undermine Delta Lake’s garbage collection and lead to unexpected storage growth and performance degradation.

## Overview

Delta Lake maintains its own versioning and garbage collection system. The `VACUUM` command permanently removes old data files that are no longer referenced by the current table version, and transaction logs are cleaned up automatically during regular table operations. ^[delta-lake-limitations-on-s3-databricks-on-aws.md#L19-L24]

When S3 bucket versioning is turned on for a bucket that stores Delta Lake data (including [Unity Catalog](/concepts/unity-catalog.md) managed tables), S3 retains copies of all objects that are deleted or overwritten. This includes:

- Data files that `VACUUM` would otherwise permanently delete. ^[delta-lake-limitations-on-s3-databricks-on-aws.md#L19-L24]
- Transaction log files that are cleaned up automatically. ^[delta-lake-limitations-on-s3-databricks-on-aws.md#L19-L24]

As a result, the intended space reclamation from `VACUUM` does not occur — the files remain in S3 as non-current versions, consuming storage and potentially causing performance slowdowns. ^[delta-lake-limitations-on-s3-databricks-on-aws.md#L19-L24]

## Recommendation

Databricks recommends **not turning on bucket versioning** for buckets that store Delta Lake data. ^[delta-lake-limitations-on-s3-databricks-on-aws.md#L12-L17]

If bucket versioning is required, Databricks advises: ^[delta-lake-limitations-on-s3-databricks-on-aws.md#L26-L28]

- **Retain a maximum of three non-current versions**.
- **Implement a lifecycle management policy** that deletes non-current versions after 7 days or less.

These practices limit the storage impact of retained objects while preserving the ability to recover from accidental deletions or overwrites.

## Performance Impact

Users who enable bucket versioning may observe **performance slowdowns** on tables stored in those buckets. If such issues occur, Databricks asks customers to mention that bucket versioning is enabled when contacting Databricks support. ^[delta-lake-limitations-on-s3-databricks-on-aws.md#L30-L32]

## Related Concepts

- Delta Lake VACUUM – The command for permanently removing old data files.
- [S3 Versioning](/concepts/delta-table-versioning.md) – Amazon S3’s mechanism for retaining object versions.
- [Garbage Collection in Delta Lake](/concepts/delta-lake-vacuum-and-garbage-collection.md) – Automated cleanup of unreferenced data and log files.
- Lifecycle Management Policy – S3 rules to expire non-current object versions.
- [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md) – Table storage that is affected by S3 versioning.

## Sources

- delta-lake-limitations-on-s3-databricks-on-aws.md

# Citations

1. [delta-lake-limitations-on-s3-databricks-on-aws.md:19-24](/references/delta-lake-limitations-on-s3-databricks-on-aws-516e860e.md)
2. [delta-lake-limitations-on-s3-databricks-on-aws.md:12-17](/references/delta-lake-limitations-on-s3-databricks-on-aws-516e860e.md)
3. [delta-lake-limitations-on-s3-databricks-on-aws.md:26-28](/references/delta-lake-limitations-on-s3-databricks-on-aws-516e860e.md)
4. [delta-lake-limitations-on-s3-databricks-on-aws.md:30-32](/references/delta-lake-limitations-on-s3-databricks-on-aws-516e860e.md)
