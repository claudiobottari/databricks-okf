---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a0bda43f3a5e19a2ce2ec08ce800cd371c7b53f97594a861a309a4f55687cdac
  pageDirectory: concepts
  sources:
    - delta-lake-limitations-on-s3-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - eventually-consistent-storage-impact-on-delta-lake
    - ECSIODL
  citations:
    - file: delta-lake-limitations-on-s3-databricks-on-aws.md
title: Eventually consistent storage impact on Delta Lake
description: Amazon S3's eventually consistent model introduces risks for Delta Lake operations like concurrent writes and table modifications, requiring workarounds and single-workspace isolation.
tags:
  - delta-lake
  - s3
  - consistency
  - architecture
timestamp: "2026-06-18T11:48:42.292Z"
---

# Eventually Consistent Storage Impact on Delta Lake

**Eventually consistent storage** refers to a data consistency model where updates to a storage system are not immediately visible to all readers. Amazon S3 is an eventually consistent object store, and this property introduces specific limitations when [Delta Lake](/concepts/delta-lake.md) tables are stored on S3.

## Multi-Cluster Write Limitations

Databricks and Delta Lake support [multi-cluster writes](/concepts/multi-cluster-writes-feature-toggle.md) by default, meaning concurrent writes from multiple clusters do not corrupt the table. For Delta Lake tables stored on Amazon S3, this guarantee is limited: concurrent writes are only safe within a single Databricks workspace. Writing to the same Delta table from different workspaces may cause data corruption or data loss due to S3's eventual consistency model. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

Databricks recommends that you **do not** modify the same [Delta Lake Table](/concepts/delta-lake-table.md) stored on S3 from different workspaces. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

Additional features that are **not supported** when multi-cluster writes are enabled with S3:

- Server-Side Encryption with Customer-Provided Encryption Keys (SSE-C)
- S3 paths with credentials that cannot access AWS Security Token Service (STS)

You can disable multi-cluster writes by setting `spark.databricks.delta.multiClusterWrites.enabled` to `false`. If disabled, all writes to a single table must originate from a single cluster. Disabling this setting while writing from multiple clusters may cause data loss or corruption. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Bucket Versioning

Databricks recommends **not** enabling bucket versioning on S3 buckets that store Delta Lake data, including [Unity Catalog](/concepts/unity-catalog.md) managed tables. Delta Lake implements its own versioning and garbage collection via the transaction log and `VACUUM`. Enabling S3 bucket versioning causes S3 to retain copies of metadata and data files that Delta Lake considers deleted — such as files removed by `VACUUM` or cleaned up during routine Delta Lake operations. This retention can lead to performance degradation. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

If bucket versioning is required, Databricks recommends retaining at most three versions and implementing a lifecycle management policy that retains versions for 7 days or less. When contacting Databricks support about performance slowdowns on such tables, mention that bucket versioning is enabled. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Stale Data After Deleting Files with `rm -rf`

Using `rm -rf` to drop a [Delta Lake Table](/concepts/delta-lake-table.md) can produce stale data due to S3's eventual consistency. When files are deleted directly (rather than through Delta Lake's own drop operation), the transaction log may still reference the deleted files, causing inconsistent reads or errors. Databricks advises against using `rm -rf` to delete Delta tables and instead recommends using the proper [Drop or replace a table](/concepts/create-or-replace-table-clone.md) operations. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Best Practices Summary

- Keep multi-cluster writes within a single workspace when using S3.
- Avoid S3 bucket versioning on Delta Lake buckets; if unavoidable, limit version count and retention duration.
- Never use `rm -rf` to drop Delta tables; use Databricks SQL or API to drop tables.
- Be aware that S3's eventual consistency is the root cause of these limitations; plan your workloads accordingly.

## Related Concepts

- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md)
- Multi-cluster Writes
- VACUUM
- [Amazon S3 Consistency Model](/concepts/s3-eventually-consistent-model.md)
- [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md)
- Databricks S3 Commit Service

## Sources

- delta-lake-limitations-on-s3-databricks-on-aws.md

# Citations

1. [delta-lake-limitations-on-s3-databricks-on-aws.md](/references/delta-lake-limitations-on-s3-databricks-on-aws-516e860e.md)
