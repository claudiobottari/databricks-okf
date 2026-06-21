---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ed6ca920ab7bdcb48c186bc279109e50384b41018f0dc5e1444ee42ca23ef7c1
  pageDirectory: concepts
  sources:
    - delta-lake-limitations-on-s3-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-table-deletion-on-s3
    - DLTDOS
    - Delta Lake tables stored on Amazon S3
    - delta-lake-table-deletion-risks-on-s3
    - DLTDROS
  citations:
    - file: delta-lake-limitations-on-s3-databricks-on-aws.md
title: Delta Lake Table Deletion on S3
description: Using rm -rf to drop a Delta Lake table on S3 can result in stale data; users should use proper table drop operations instead.
tags:
  - delta-lake
  - s3
  - operations
timestamp: "2026-06-19T14:59:44.585Z"
---

# [Delta Lake Table](/concepts/delta-lake-table.md) Deletion on S3

**Delta Lake Table Deletion on S3** refers to the specific risks, limitations, and best practices for deleting or removing Delta Lake tables stored in Amazon S3. Due to Delta Lake's own versioning and garbage collection mechanisms, standard file deletion approaches such as `rm -rf` can lead to data consistency issues and stale data.

## Risks of Direct File Deletion

You should not use `rm -rf` to drop a [Delta Lake Table](/concepts/delta-lake-table.md) stored in S3. When files are deleted directly using operating system commands, the Delta Lake transaction log becomes inconsistent with the underlying data files. This mismatch can result in stale data references and make the table unusable. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

Instead, use the DROP TABLE or DROP OR REPLACE operations provided by Databricks to properly remove Delta Lake tables. These operations ensure the transaction log is updated correctly. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Bucket Versioning Considerations

Databricks recommends against enabling [S3 bucket versioning](/concepts/s3-bucket-versioning-and-delta-lake.md) for buckets that store Delta Lake data, including [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md). Delta Lake implements its own versioning and garbage collection, which conflicts with S3's versioning. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

When bucket versioning is enabled:
- S3 retains copies of metadata and data files that Databricks considers deleted.
- This includes data files that `VACUUM` would permanently delete and transaction logs cleaned up automatically during regular Delta Lake operations.
- Bucket versioning can lead to performance slowdowns on tables. If you encounter such issues, mention that versioning is enabled when contacting Databricks support. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

If you choose to use bucket versioning, Databricks recommends retaining only **three versions** and implementing a lifecycle management policy that retains versions for **7 days or less**. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Proper Deletion Methods

### Dropping a Table

Use Databricks SQL or the Delta Lake API to properly drop a table. This updates the [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) and marks the table as removed, maintaining consistency between the log and underlying data files. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

### Vacuum

The `VACUUM` operation permanently deletes data files that are no longer referenced by the transaction log. This is Delta Lake's native garbage collection mechanism. When bucket versioning is enabled, however, `VACUUM` may not actually free storage space because S3 retains previous versions. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) – The core metadata structure that tracks table changes.
- DROP TABLE – The proper SQL command to remove a [Delta Lake Table](/concepts/delta-lake-table.md).
- VACUUM in Delta Lake – Garbage collection operation for removing unreferenced files.
- [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md) – Tables managed by Unity Catalog, subject to these same limitations.
- [S3 Bucket Versioning](/concepts/s3-bucket-versioning-and-delta-lake.md) – AWS feature that conflicts with Delta Lake's own versioning.
- [Delta Lake Limitations on S3](/concepts/delta-lake-limitations-on-s3.md) – Broader overview of S3-specific Delta Lake constraints.

## Sources

- delta-lake-limitations-on-s3-databricks-on-aws.md

# Citations

1. [delta-lake-limitations-on-s3-databricks-on-aws.md](/references/delta-lake-limitations-on-s3-databricks-on-aws-516e860e.md)
