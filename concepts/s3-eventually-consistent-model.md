---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 450e45cf04195f3f15f102b1f596482e1d6981434881fff8f2fe76da6af48ee0
  pageDirectory: concepts
  sources:
    - delta-lake-limitations-on-s3-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - s3-eventually-consistent-model
    - SECM
    - Eventually Consistent Model
    - Eventually consistent model
    - eventual consistency model
    - eventually consistent
    - eventually consistent model
    - Amazon S3 Consistency Model
    - Data consistency on S3
    - Eventual consistency
    - S3 Consistency Model
    - S3 Eventual Consistency
    - S3 consistency model
    - S3 eventual consistency
    - eventual consistency
  citations:
    - file: delta-lake-limitations-on-s3-databricks-on-aws.md
title: S3 Eventually Consistent Model
description: Amazon S3's eventual consistency model can cause data corruption and data loss when multiple systems or clusters modify the same Delta Lake table stored on S3 simultaneously.
tags:
  - s3
  - consistency
  - delta-lake
timestamp: "2026-06-18T15:15:17.719Z"
---

## S3 Eventually Consistent Model

Amazon S3 operates under an **eventually consistent** model, meaning that after a write or delete operation, updates to objects are not immediately visible to all read requests. This design provides high throughput and availability but introduces challenges for systems that require strong consistency, such as [Delta Lake](/concepts/delta-lake.md) tables stored on S3. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

### Multi-Cluster Write Limitations

For Delta Lake tables stored on S3, the eventually consistent model can lead to problems when multiple clusters or systems modify the same table simultaneously. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

Databricks and Delta Lake support multi-cluster writes by default, meaning concurrent writes from multiple clusters within a single workspace do not corrupt the table. However, this guarantee is **limited to a single Databricks workspace**. To avoid potential data corruption and data loss, Databricks recommends **not modifying the same [Delta Lake Table](/concepts/delta-lake-table.md) stored in S3 from different workspaces**. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

The following features are **not supported** when multi-cluster writes are enabled on S3:

- Server-Side Encryption with Customer-Provided Encryption Keys (SSE-C)
- S3 paths with credentials in a cluster that cannot access AWS Security Token Service (STS)

You can disable multi-cluster writes by setting `spark.databricks.delta.multiClusterWrites.enabled` to `false`. If disabled, all writes to a single table must originate from a single cluster. Modifying the same table from multiple clusters while multi-cluster writes are turned off **may cause data loss or data corruption**. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

### Bucket Versioning and Delta Lake

Databricks recommends **not enabling bucket versioning** for buckets that store Delta Lake data, including Unity Catalog managed tables. Delta Lake implements its own versioning and garbage collection. When S3 bucket versioning is turned on, S3 retains copies of metadata and data files that Delta Lake processes (such as `VACUUM`) consider deleted. This includes transaction logs cleaned up during regular operations, leading to unnecessary storage costs and potential performance degradation. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

If you choose to use bucket versioning, Databricks recommends retaining at most **three versions** and implementing a lifecycle management policy that retains versions for **7 days or less**. If you encounter performance slowdown on tables stored in buckets with versioning enabled, mention this when contacting Databricks support. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

### Stale Data After Deleting Files with `rm -rf`

Do not use `rm -rf` to drop a [Delta Lake Table](/concepts/delta-lake-table.md). Doing so can leave stale data and transaction logs, potentially causing inconsistencies. Use the standard table drop operations provided by Databricks and Delta Lake instead. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

### Related Concepts

- [Delta Lake on S3](/concepts/delta-lake.md)
- [Multi-Cluster Writes](/concepts/multi-cluster-write-limitations-on-s3.md)
- VACUUM
- [S3 Consistency Model](/concepts/s3-eventually-consistent-model.md)
- Databricks S3 Commit Service

### Sources

- delta-lake-limitations-on-s3-databricks-on-aws.md

# Citations

1. [delta-lake-limitations-on-s3-databricks-on-aws.md](/references/delta-lake-limitations-on-s3-databricks-on-aws-516e860e.md)
