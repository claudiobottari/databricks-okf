---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5d45bcf2c2029266276daed984f1b33977fc666475d86fb0f9c2a5b774696409
  pageDirectory: concepts
  sources:
    - delta-lake-limitations-on-s3-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - risks-of-direct-file-deletion-in-delta-lake-on-s3
    - RODFDIDLOS
  citations:
    - file: delta-lake-limitations-on-s3-databricks-on-aws.md
title: Risks of Direct File Deletion in Delta Lake on S3
description: Using shell commands like rm -rf to drop Delta Lake tables on S3 can cause stale data and corruption; Delta Lake tables should be dropped using proper table operations.
tags:
  - delta-lake
  - s3
  - data-management
  - deletion
timestamp: "2026-06-19T10:00:10.625Z"
---

# Risks of Direct File Deletion in Delta Lake on S3

**Risks of Direct File Deletion in Delta Lake on S3** refers to the data integrity and consistency issues that arise when users bypass Delta Lake's transactional operations and delete Delta Lake files directly from Amazon S3 using commands like `rm -rf` or other object-level deletion methods.

## Overview

Delta Lake implements its own versioning, transaction logging, and garbage collection mechanisms to maintain [ACID transactions](/concepts/delta-acid-transactions.md). When you delete files directly from S3 rather than through Delta Lake operations, you bypass these safeguards, leading to potential data corruption, stale metadata, and unrecoverable data loss. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Stale Data After Deleting Files with `rm -rf`

Databricks explicitly warns against using `rm -rf` to drop a [Delta Lake Table](/concepts/delta-lake-table.md). When files are deleted directly from S3, the Delta Lake transaction log still references those files as part of the table's metadata. This mismatch between the actual file state and the metadata state leaves the table in an inconsistent condition. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

For proper table removal, users should use the correct Databricks operations documented in [Drop or replace a table](/concepts/create-or-replace-table-clone.md). ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Interaction with S3 Bucket Versioning

Databricks recommends against enabling **bucket versioning** for S3 buckets that store Delta Lake data, including [Unity Catalog](/concepts/unity-catalog.md) managed tables. Delta Lake already implements its own versioning and garbage collection. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

When bucket versioning is enabled:
- S3 retains copies of metadata and data files that Delta Lake considers deleted.
- This includes data files that `VACUUM` would permanently delete.
- Transaction logs cleaned up automatically during regular [Delta Lake Table](/concepts/delta-lake-table.md) operations are also retained.

Direct file deletion in versioned buckets compounds these issues. While S3 retains previous versions of deleted objects, the Delta Lake transaction log may not correctly reference or reconcile these versions, creating further inconsistency. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Related Risks

Direct file deletion can also interfere with other Delta Lake operations and S3 configurations that are already sensitive:

- **Multi-cluster write limitations**: S3's eventually consistent model means that direct file deletion from one cluster may not be visible to other clusters writing to the same table, potentially causing data corruption or data loss. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]
- **VACUUM operations**: Direct file deletion bypasses VACUUM's safe garbage collection, leaving the table with metadata referencing nonexistent files.
- **[Transaction log integrity](/concepts/delta-lake-transaction-log-integrity.md)**: The Delta Lake transaction log may contain entries for files that no longer exist, breaking the table's ability to reconstruct its state.

## Best Practices

- Always use Delta Lake operations (such as `DROP TABLE`, `DELETE FROM`, or `VACUUM`) to remove data, rather than manipulating files directly in S3.
- If bucket versioning must be enabled, Databricks recommends retaining only three versions and implementing a lifecycle management policy that retains versions for 7 days or less. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]
- If performance slowdowns occur on tables stored in versioned buckets, mention that bucket versioning is enabled when contacting Databricks support. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Sources

- delta-lake-limitations-on-s3-databricks-on-aws.md

# Citations

1. [delta-lake-limitations-on-s3-databricks-on-aws.md](/references/delta-lake-limitations-on-s3-databricks-on-aws-516e860e.md)
