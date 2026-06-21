---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 35aae191b45c4b06410af5af3b3c6a8883b3290a63be29958bd9b7b473717d79
  pageDirectory: concepts
  sources:
    - delta-lake-limitations-on-s3-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-s3-bucket-versioning-conflict
    - DLSBVC
  citations:
    - file: delta-lake-limitations-on-s3-databricks-on-aws.md
title: Delta Lake S3 bucket versioning conflict
description: S3 bucket versioning should not be enabled for Delta Lake tables because it conflicts with Delta Lake's own versioning and garbage collection, causing retained data files and performance degradation.
tags:
  - delta-lake
  - s3
  - storage
  - limitations
timestamp: "2026-06-18T11:48:43.094Z"
---

# Delta Lake S3 bucket versioning conflict

The **Delta Lake S3 bucket versioning conflict** refers to the operational and performance problems that arise when Amazon S3 bucket versioning is enabled on buckets that store [Delta Lake](/concepts/delta-lake.md) tables. Delta Lake implements its own internal versioning and garbage collection, and enabling S3 bucket versioning interferes with these mechanisms, leading to data retention issues, performance degradation, and administrative overhead. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Why bucket versioning causes issues

Delta Lake manages table state through a [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) and uses operations such as VACUUM to permanently delete obsolete data and metadata files. When S3 bucket versioning is turned on, S3 retains all previous versions of objects — including files that Delta Lake has logically deleted. This means: ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

- Data files that `VACUUM` would permanently delete remain accessible as versioned copies in S3, potentially inflating storage costs and complicating compliance with data retention policies.
- Transaction log files that Delta Lake automatically cleans up during routine table operations are also retained, leading to an ever-growing number of object versions that can degrade list and read performance.

The conflict is fundamentally one of competing lifecycle management: both Delta Lake and S3 bucket versioning attempt to track and retain history, but they are not synchronized. Delta Lake assumes it controls the lifecycle of its files; bucket versioning overrides that assumption. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Databricks recommendation

Databricks **recommends against enabling bucket versioning** for any S3 bucket that stores Delta Lake data, including [Unity Catalog](/concepts/unity-catalog.md) managed tables. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

If bucket versioning must be enabled for compliance or other non-Delta Lake reasons, Databricks advises: ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

- Retain no more than three noncurrent versions.
- Implement a S3 lifecycle policy that expires noncurrent versions after **7 days or less**.

These limits reduce the storage footprint and the performance impact of versioned files that Delta Lake’s own garbage collection would otherwise have removed. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## If bucket versioning is already enabled

If you encounter performance slowdowns on Delta Lake tables stored in versioned buckets, mention that bucket versioning is enabled when contacting Databricks support. The support team can factor the versioning overhead into their analysis. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Additional considerations

S3’s eventual consistency model also imposes additional constraints on Delta Lake tables stored in S3, particularly around [multi-cluster writes](/concepts/multi-cluster-writes-feature-toggle.md). While that is a separate issue from bucket versioning, both stem from S3’s distributed storage semantics and are often encountered together. See [Delta Lake multi-cluster write limitations on S3](/concepts/delta-lake-multi-cluster-write-restrictions-on-s3.md) for details. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Related concepts

- Delta Lake VACUUM – Delta Lake command that permanently removes old data files
- [Delta Lake garbage collection](/concepts/delta-lake-vacuum-and-garbage-collection.md) – The automatic cleanup of transaction logs and orphaned files
- [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md) – Tables that may be stored in S3 and affected by bucket versioning
- S3 lifecycle policies – AWS mechanism to manage object version retention

## Sources

- delta-lake-limitations-on-s3-databricks-on-aws.md

# Citations

1. [delta-lake-limitations-on-s3-databricks-on-aws.md](/references/delta-lake-limitations-on-s3-databricks-on-aws-516e860e.md)
