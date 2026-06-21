---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d2172bd81b9e6a43ccb70b4176ad44c4ccf201c3c2c89c55e276397a3bce638d
  pageDirectory: concepts
  sources:
    - delta-lake-limitations-on-s3-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-bucket-versioning-limitations-on-s3
    - DLBVLOS
  citations:
    - file: delta-lake-limitations-on-s3-databricks-on-aws.md
title: Delta Lake Bucket Versioning Limitations on S3
description: Databricks recommends against enabling S3 bucket versioning for Delta Lake tables because it interferes with Delta Lake's own versioning and garbage collection, leading to retained metadata and data files.
tags:
  - delta-lake
  - s3
  - storage
  - versioning
timestamp: "2026-06-19T09:59:59.652Z"
---

# Delta Lake Bucket Versioning Limitations on S3

**Delta Lake Bucket Versioning Limitations on S3** describes the operational concerns and recommendations when using Amazon S3 bucket versioning with Delta Lake tables. Because Delta Lake implements its own internal versioning and garbage collection, enabling S3 bucket versioning can lead to unintended data retention, increased storage costs, and potential performance degradation. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Recommendation Against Bucket Versioning

Databricks recommends that you **do not turn on bucket versioning** for S3 buckets that store Delta Lake data, including Unity Catalog managed tables. Delta Lake already provides its own versioning and garbage collection mechanisms, making S3-level versioning redundant for most use cases. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

When bucket versioning is enabled, S3 retains copies of metadata and data files that Delta Lake considers deleted. This includes:

- Data files that `VACUUM` would permanently remove.
- Transaction log files that are automatically cleaned up during regular [Delta Lake Table](/concepts/delta-lake-table.md) operations.

The retention of these files can cause storage costs to accumulate unnecessarily and may interfere with Delta Lake’s own lifecycle management. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## If You Must Use Bucket Versioning

If you decide to enable bucket versioning despite the recommendation, Databricks advises the following configuration:

- Retain no more than **three versions** per object.
- Implement an S3 lifecycle management policy that deletes older versions **after 7 days or less**.

These limits help reduce the negative impact on storage costs and query performance while still providing a safety net for accidental modifications. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Performance Implications

Enabling bucket versioning can lead to slower performance on Delta Lake tables stored in S3. If you encounter performance issues and have bucket versioning enabled, you should mention this to Databricks support when filing a support ticket, as it may be a contributing factor. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md)
- Amazon S3
- VACUUM
- Lifecycle management policy
- Multi-cluster write limitations — Another Delta Lake on S3 limitation that is independent of bucket versioning but worth reviewing for overall S3 best practices.
- [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md)

## Sources

- delta-lake-limitations-on-s3-databricks-on-aws.md

# Citations

1. [delta-lake-limitations-on-s3-databricks-on-aws.md](/references/delta-lake-limitations-on-s3-databricks-on-aws-516e860e.md)
