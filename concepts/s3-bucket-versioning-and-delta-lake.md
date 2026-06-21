---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9f61814f840467d224dde994373415e752507aa526ecde5d32b0600a8be1c343
  pageDirectory: concepts
  sources:
    - delta-lake-limitations-on-s3-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - s3-bucket-versioning-and-delta-lake
    - Delta Lake and S3 Bucket Versioning
    - SBVADL
    - Bucket Versioning and Delta Lake
    - Bucket versioning and Delta Lake
    - S3 Bucket Versioning
    - S3 bucket versioning
  citations:
    - file: delta-lake-limitations-on-s3-databricks-on-aws.md
title: S3 Bucket Versioning and Delta Lake
description: Databricks recommends against enabling S3 bucket versioning for Delta Lake tables because Delta Lake implements its own versioning and garbage collection, and S3 versioning can cause performance degradation and storage bloat.
tags:
  - delta-lake
  - s3
  - storage
  - best-practices
timestamp: "2026-06-18T15:15:13.891Z"
---

# S3 Bucket Versioning and Delta Lake

**S3 Bucket Versioning and Delta Lake** refers to the compatibility concerns and best practices when using Amazon S3 bucket versioning with Delta Lake tables stored on Databricks. Delta Lake implements its own internal versioning and garbage collection, which can conflict with S3’s object versioning mechanism, leading to unnecessary storage costs and potential performance degradation.^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Overview

Databricks recommends that you do **not** enable S3 bucket versioning on buckets that store Delta Lake data, including [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md). Delta Lake already tracks table versions through its transaction log and performs its own garbage collection (e.g., via `VACUUM`). When S3 bucket versioning is turned on, every delete or overwrite of a file creates a new version of that object instead of permanently removing it. As a result, S3 retains copies of metadata and data files that Databricks considers deleted, including files removed by `VACUUM` and transaction logs cleaned up automatically during regular Delta Lake operations.^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Recommendations

If you choose to enable S3 bucket versioning despite the recommendation, Databricks suggests the following mitigations:

- **Retain at most three non-current versions** of each object.
- **Set a lifecycle management policy** that expires non-current versions after 7 days or less.

These practices help limit storage bloat and reduce the overhead of managing unnecessary object versions.^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Performance Considerations

Bucket versioning can cause performance slowdowns on Delta Lake tables. If you observe degraded performance on tables stored in a versioned bucket, be sure to mention that versioning is enabled when contacting Databricks support.^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that provides ACID transactions and its own versioning.
- VACUUM — The Delta Lake command for physically removing old data files.
- [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md) — Tables whose data is managed by Databricks in the cloud storage account.
- [Multi-cluster writes](/concepts/multi-cluster-writes-feature-toggle.md) — Concurrent writes from multiple clusters, which have additional limitations on S3.
- Lifecycle management policies — AWS S3 policies that automatically manage object versions and expiration.

## Sources

- delta-lake-limitations-on-s3-databricks-on-aws.md

# Citations

1. [delta-lake-limitations-on-s3-databricks-on-aws.md](/references/delta-lake-limitations-on-s3-databricks-on-aws-516e860e.md)
