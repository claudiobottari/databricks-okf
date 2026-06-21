---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 14f9e9866c6264d62af52460c188bf2d808d870b3c387d21daa23be1087aa68d
  pageDirectory: concepts
  sources:
    - delta-lake-limitations-on-s3-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - s3-eventual-consistency-impact-on-delta-lake
    - SECIODL
  citations:
    - file: delta-lake-limitations-on-s3-databricks-on-aws.md
title: S3 eventual consistency impact on Delta Lake
description: Amazon S3's eventually consistent model can cause data corruption or loss when multiple clusters or systems concurrently modify the same Delta Lake table stored on S3.
tags:
  - s3
  - delta-lake
  - consistency
  - databricks
timestamp: "2026-06-19T18:20:47.674Z"
---

# S3 Eventual Consistency Impact on Delta Lake

Amazon S3's **eventual consistency model** introduces specific constraints and risks when storing Delta Lake tables on S3. While Delta Lake’s transaction log provides ACID guarantees, the underlying storage system can cause problems in multi‑cluster write scenarios and with certain operational practices. This page covers the known limitations and recommended mitigations.

## Multi-Cluster Write Limitations

Delta Lake supports concurrent writes from multiple clusters by default. However, when the table is stored on S3, this guarantee is **limited to a single Databricks workspace** because S3’s eventually consistent model can lead to potential data corruption or data loss when the same table is modified from different workspaces at the same time. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

To avoid these issues, Databricks recommends **not modifying the same [Delta Lake Table](/concepts/delta-lake-table.md) stored in S3 from different workspaces**. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

The following features are **not supported** when multi‑cluster writes are enabled on S3:

- Server‑Side Encryption with Customer‑Provided Encryption Keys (SSE‑C)
- S3 paths with credentials in a cluster that cannot access the AWS Security Token Service (STS)

^[delta-lake-limitations-on-s3-databricks-on-aws.md]

You can disable multi‑cluster writes by setting `spark.databricks.delta.multiClusterWrites.enabled` to `false`. If disabled, all writes to a table **must** originate from a single cluster; modifying the table from multiple clusters with this setting off may cause data loss or corruption. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Bucket Versioning and Delta Lake

Databricks recommends **not turning on bucket versioning** for S3 buckets that store Delta Lake data, including [Unity Catalog](/concepts/unity-catalog.md) managed tables. Delta Lake implements its own versioning and garbage collection. When bucket versioning is enabled, S3 retains copies of metadata and data files that Databricks considers deleted (such as files removed by VACUUM or transaction‑log cleanups). This can lead to performance degradation and increased storage costs. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

If you must use bucket versioning, Databricks recommends:

- Retaining **three versions** at most.
- Implementing a lifecycle management policy that retains versions for **7 days or less**.

If you encounter performance issues on tables stored in versioned buckets, mention that bucket versioning is enabled when contacting Databricks support. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Direct File Deletion Risks

You should **never use `rm -rf` or equivalent commands** to drop a [Delta Lake Table](/concepts/delta-lake-table.md) on S3. Because S3 is eventually consistent, deleting the underlying files without going through Delta Lake’s protocol can leave the table in an inconsistent state and cause stale metadata to be served to subsequent operations. Always use the proper [Drop or replace a table](/concepts/create-or-replace-table-clone.md) commands provided by Databricks. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Recommendations Summary

- Keep all writes to a given [Delta Lake Table](/concepts/delta-lake-table.md) on S3 within **a single Databricks workspace**.
- Disable S3 bucket versioning for Delta Lake buckets, or restrict retention to 3 versions and ≤7 days.
- Never delete Delta Lake files with OS‑level commands; use Databricks table operations instead.

## Related Concepts

- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md)
- [Multi‑cluster writes](/concepts/multi-cluster-writes-feature-toggle.md)
- [S3 consistency model](/concepts/s3-eventually-consistent-model.md)
- VACUUM
- [Unity Catalog](/concepts/unity-catalog.md)
- [Databricks S3 commit service](/concepts/databricks-s3-commit-service-and-multi-cluster-writes.md)

## Sources

- delta-lake-limitations-on-s3-databricks-on-aws.md

# Citations

1. [delta-lake-limitations-on-s3-databricks-on-aws.md](/references/delta-lake-limitations-on-s3-databricks-on-aws-516e860e.md)
