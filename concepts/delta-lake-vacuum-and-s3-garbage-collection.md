---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c6a2140d7ec79c3569f72bf71b19eb78eabeff0b93deedcc2ceb42cc0836dbdf
  pageDirectory: concepts
  sources:
    - delta-lake-limitations-on-s3-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-vacuum-and-s3-garbage-collection
    - S3 Garbage Collection and Delta Lake VACUUM
    - DLVASGC
  citations:
    - file: delta-lake-limitations-on-s3-databricks-on-aws.md
title: Delta Lake VACUUM and S3 Garbage Collection
description: Delta Lake's VACUUM command permanently deletes old data files as part of its garbage collection, but S3 bucket versioning retains these deleted files, undermining the cleanup process.
tags:
  - delta-lake
  - s3
  - storage-management
timestamp: "2026-06-19T14:59:36.774Z"
---

# Delta Lake VACUUM and S3 Garbage Collection

**Delta Lake VACUUM** is a command that permanently removes data files from a Delta table that are no longer referenced by the Delta transaction log and are older than a specified retention threshold. When Delta tables are stored on Amazon S3, VACUUM interacts with S3's own versioning and lifecycle mechanisms, creating important considerations for data management.

## VACUUM Overview

The `VACUUM` command deletes data files from storage that Delta Lake's transaction log has marked as no longer needed, typically because they have been overwritten or deleted by subsequent operations. This is Delta Lake's primary mechanism for garbage collection and storage reclamation. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## S3 Bucket Versioning Conflict

Databricks **strongly recommends against** enabling S3 bucket versioning for buckets that store Delta Lake data, including [Unity Catalog](/concepts/unity-catalog.md) managed tables. Delta Lake implements its own versioning system through the [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) and manages its own garbage collection process. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

When S3 bucket versioning is turned on, S3 retains copies of metadata and data files that Delta Lake considers deleted, including:

- Data files that `VACUUM` would permanently delete
- Transaction logs cleaned up automatically during regular [Delta Lake Table](/concepts/delta-lake-table.md) operations

This causes S3 to retain storage for files that Delta Lake has already garbage-collected, defeating the purpose of running VACUUM and potentially increasing storage costs. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

### Versioning Workaround

If you must use S3 bucket versioning for Delta Lake tables, Databricks recommends:

- Retaining a maximum of **three versions**
- Implementing an S3 lifecycle management policy that retains versions for **7 days or less** for all S3 buckets with versioning enabled

If you encounter performance slowdowns on tables stored in versioned buckets, mention that bucket versioning is enabled when contacting Databricks support. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Manual File Deletion Risks

Do **not** use `rm -rf` or any direct file deletion method to drop a [Delta Lake Table](/concepts/delta-lake-table.md) or remove its data files. Such manual deletion leaves stale metadata in the transaction log and can cause data integrity issues. Instead, use Delta Table Operations such as `DROP TABLE` or `DROP TABLE IF EXISTS` which properly manage both the transaction log and the underlying data files. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## S3 Eventual Consistency Impact

Amazon S3 uses an Eventually Consistent Model for certain operations. This can interact with Delta Lake's garbage collection process when multiple clusters or workspaces modify the same table. Databricks recommends that you do not modify the same [Delta Lake Table](/concepts/delta-lake-table.md) stored in S3 from different workspaces. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

Delta Lake supports [Multi-Cluster Writes](/concepts/multi-cluster-write-limitations-on-s3.md) by default, which prevents data corruption when multiple clusters write to the same table within a single workspace. For tables on S3, this guarantee is limited to a single Databricks workspace. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Best Practices

- Disable S3 bucket versioning for buckets containing Delta Lake tables
- Always use Delta Lake commands (like `VACUUM`, `DROP TABLE`) instead of direct S3 file manipulation
- Keep multi-cluster write operations within a single Databricks workspace
- Monitor storage costs to ensure garbage collection is working as expected

## Related Concepts

- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md)
- Delta Table Operations
- [Unity Catalog](/concepts/unity-catalog.md)
- [Multi-Cluster Writes](/concepts/multi-cluster-write-limitations-on-s3.md)
- [S3 Consistency Model](/concepts/s3-eventually-consistent-model.md)
- [VACUUM Retention Threshold](/concepts/vacuum-retention-threshold.md)

## Sources

- delta-lake-limitations-on-s3-databricks-on-aws.md

# Citations

1. [delta-lake-limitations-on-s3-databricks-on-aws.md](/references/delta-lake-limitations-on-s3-databricks-on-aws-516e860e.md)
