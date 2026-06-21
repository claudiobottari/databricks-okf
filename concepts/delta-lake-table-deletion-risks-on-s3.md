---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 546d7651f15a9b946e64f91b5073336231a26ad1e86f93d69cf15eaf54d1f289
  pageDirectory: concepts
  sources:
    - delta-lake-limitations-on-s3-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-table-deletion-risks-on-s3
    - DLTDROS
  citations:
    - file: delta-lake-limitations-on-s3-databricks-on-aws.md
title: Delta Lake table deletion risks on S3
description: Using rm -rf or direct file deletion to drop Delta Lake tables on S3 causes stale data issues; proper drop or replace table operations should be used instead.
tags:
  - delta-lake
  - s3
  - data-management
  - risks
timestamp: "2026-06-18T11:48:44.737Z"
---

# [Delta Lake Table](/concepts/delta-lake-table.md) Deletion Risks on S3

**Delta Lake table deletion risks on S3** refer to the potential data corruption, data loss, and unintended consequences that can occur when improperly deleting or managing Delta Lake tables stored in Amazon S3. These risks arise from S3's eventual consistency model, versioning behavior, and the mismatch between Delta Lake's internal management and S3's native operations.

## Stale Data After Deleting Files with `rm -rf`

Do not use `rm -rf` or equivalent file-level deletion commands to drop a [Delta Lake Table](/concepts/delta-lake-table.md) on S3. Using `rm -rf` removes data files without updating the Delta transaction log, leaving the table metadata in an inconsistent state. This can result in stale references and potential data corruption when the table is accessed afterward. Always use Delta Lake's supported operations — such as `DROP TABLE` or `DELETE FROM` — to safely remove tables or data. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Bucket Versioning and Delta Lake

Databricks recommends that you do not enable [S3 bucket versioning](/concepts/s3-bucket-versioning-and-delta-lake.md) for buckets that store Delta Lake data, including [Unity Catalog](/concepts/unity-catalog.md) managed tables. Delta Lake implements its own versioning and garbage collection mechanisms. When bucket versioning is enabled, S3 retains copies of metadata and data files that Databricks considers deleted, including files that VACUUM would permanently remove and transaction logs cleaned up automatically during regular Delta Lake operations. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

If you choose to use bucket versioning despite this recommendation, Databricks advises retaining a maximum of three versions and implementing a lifecycle management policy that retains versions for 7 days or less. If you encounter performance slowdowns on tables stored in versioned buckets, mention that bucket versioning is enabled when contacting Databricks support. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Multi-Cluster Write Limitations

To avoid potential data corruption and data loss, Databricks recommends not modifying the same [Delta Lake Table](/concepts/delta-lake-table.md) stored in S3 from different Databricks workspaces. S3's [eventually consistent model](/concepts/s3-eventually-consistent-model.md) can cause problems when multiple systems or clusters modify data in the same table simultaneously, even though Delta Lake supports multi-cluster writes by default. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

For Delta Lake tables stored on S3, the guarantee of safe multi-cluster writes is limited to a single Databricks workspace. The following features are not supported when running in this mode: ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

- Server-Side Encryption with Customer-Provided Encryption Keys (SSE-C)
- S3 paths with credentials in a cluster that cannot access AWS Security Token Service (STS)

You can disable multi-cluster writes by setting `spark.databricks.delta.multiClusterWrites.enabled` to `false`. However, if multi-cluster writes are turned off and you modify the same [Delta Lake Table](/concepts/delta-lake-table.md) from multiple clusters concurrently, data loss or data corruption may occur. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Risks from Improper Deletion

Improper deletion of Delta Lake tables on S3 can lead to:

- **Data corruption** — Removing files without updating the transaction log leaves the table in an inconsistent state.
- **Data loss** — Direct file deletion can remove data that is still referenced by active table versions.
- **Performance degradation** — Accumulated orphaned data files from bucket versioning can slow query performance.
- **Recovery complications** — Deleted files retained by bucket versioning may not align with Delta Lake's internal versioning, complicating recovery efforts.

## Best Practices for Safe Deletion

- **Use Delta Lake commands** — Always use `DROP TABLE`, `DELETE FROM`, or `VACUUM` to manage table data and metadata.
- **Disable bucket versioning** — Avoid S3 bucket versioning for Delta Lake buckets, or limit version retention to 7 days and 3 versions at most.
- **Single-workspace writes** — Modify Delta Lake tables from only one Databricks workspace to avoid consistency issues.
- **Leverage Databricks S3 commit service** — For multi-cluster write scenarios within a single workspace, configure the [Databricks S3 commit service](/concepts/databricks-s3-commit-service-and-multi-cluster-writes.md) for safe concurrent writes.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer providing ACID transactions on data lakes
- VACUUM — Delta Lake operation for garbage-collecting old data files
- [Unity Catalog](/concepts/unity-catalog.md) — Data governance solution for managing Delta Lake tables
- [S3 bucket versioning](/concepts/s3-bucket-versioning-and-delta-lake.md) — AWS feature that can conflict with Delta Lake's own versioning
- [Eventually consistent model](/concepts/s3-eventually-consistent-model.md) — S3 consistency model that affects multi-cluster writes
- [Databricks S3 commit service](/concepts/databricks-s3-commit-service-and-multi-cluster-writes.md) — Service enabling safe multi-cluster writes within a workspace

## Sources

- delta-lake-limitations-on-s3-databricks-on-aws.md

# Citations

1. [delta-lake-limitations-on-s3-databricks-on-aws.md](/references/delta-lake-limitations-on-s3-databricks-on-aws-516e860e.md)
