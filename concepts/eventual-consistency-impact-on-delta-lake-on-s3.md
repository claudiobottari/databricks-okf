---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 26439164681829be0fc955adddca8d4e79cfc93f5a685e2b44a6a2a30f70bb35
  pageDirectory: concepts
  sources:
    - delta-lake-limitations-on-s3-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - eventual-consistency-impact-on-delta-lake-on-s3
    - ECIODLOS
  citations:
    - file: delta-lake-limitations-on-s3-databricks-on-aws.md
title: Eventual Consistency Impact on Delta Lake on S3
description: Amazon S3's eventually consistent model can cause data corruption and data loss when multiple systems or clusters modify the same Delta Lake table simultaneously, especially across workspaces.
tags:
  - delta-lake
  - s3
  - consistency
  - distributed-systems
timestamp: "2026-06-19T10:00:02.989Z"
---

# Eventual Consistency Impact on Delta Lake on S3

**Eventual Consistency Impact on Delta Lake on S3** describes the operational constraints and risks that arise when using [Delta Lake](/concepts/delta-lake.md) tables stored on Amazon S3, due to S3’s eventually consistent data model. While Delta Lake provides ACID transactions and snapshot isolation on top of object storage, S3’s consistency guarantees introduce specific limitations for bucket versioning, concurrent writes, and file deletion.

## Bucket Versioning and Delta Lake

Databricks recommends **not** turning on [S3 bucket versioning](/concepts/s3-bucket-versioning-and-delta-lake.md) for buckets that store Delta Lake data, including tables managed by [Unity Catalog](/concepts/unity-catalog.md). Delta Lake implements its own versioning and garbage collection. When S3 bucket versioning is enabled, S3 retains copies of metadata and data files that Delta Lake’s `VACUUM` and automatic transaction log cleanup consider deleted, leading to unnecessary storage costs and potential performance degradation. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

If bucket versioning must be used, Databricks suggests retaining at most three versions and applying a lifecycle management policy that deletes versions after 7 days or less. Performance slowdowns on tables stored in versioned buckets should be reported to Databricks support with mention that bucket versioning is enabled. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Multi-Cluster Write Limitations

The **eventually consistent** model of Amazon S3 can cause problems when multiple systems or clusters modify the same [Delta Lake Table](/concepts/delta-lake-table.md) concurrently. Databricks and Delta Lake support [multi-cluster writes](/concepts/multi-cluster-writes-feature-toggle.md) by default, meaning that simultaneous writes from multiple clusters within **a single Databricks workspace** do not corrupt the table. However, this guarantee **does not extend across different workspaces**. Databricks recommends against modifying the same [Delta Lake Table](/concepts/delta-lake-table.md) stored in S3 from different workspaces to avoid data corruption and data loss. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

When multi-cluster writes are enabled, the following features are not supported:
- Server-Side Encryption with Customer-Provided Encryption Keys (SSE-C)
- S3 paths with credentials in a cluster that cannot access AWS Security Token Service (STS)

^[delta-lake-limitations-on-s3-databricks-on-aws.md]

Multi-cluster writes can be turned off by setting `spark.databricks.delta.multiClusterWrites.enabled` to `false`. When disabled, **all writes to a table must originate from a single cluster**. Modifying the same table from multiple clusters concurrently while multi-cluster writes are off may cause data loss or corruption. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Stale Data After Deleting Files with `rm -rf`

Do not use `rm -rf` to drop a [Delta Lake Table](/concepts/delta-lake-table.md) stored on S3. Such manual file deletion leaves the Delta transaction log and table metadata in an inconsistent state, resulting in stale data references. Instead, always use the proper DROP TABLE command. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Related Concepts

- [Delta Lake ACID Transactions](/concepts/delta-acid-transactions.md)
- [S3 Consistency Model](/concepts/s3-eventually-consistent-model.md)
- VACUUM
- Delta Lake Multi-Cluster Writes
- Databricks S3 Commit Service
- [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md)

## Sources

- delta-lake-limitations-on-s3-databricks-on-aws.md

# Citations

1. [delta-lake-limitations-on-s3-databricks-on-aws.md](/references/delta-lake-limitations-on-s3-databricks-on-aws-516e860e.md)
