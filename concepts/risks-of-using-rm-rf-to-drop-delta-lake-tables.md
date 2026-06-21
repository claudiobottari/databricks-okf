---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5031e810a09bab6b2b92d03f306909afcb30bb725736d152814faeda08d9432e
  pageDirectory: concepts
  sources:
    - delta-lake-limitations-on-s3-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - risks-of-using-rm-rf-to-drop-delta-lake-tables
    - ROUR-TDDLT
  citations:
    - file: delta-lake-limitations-on-s3-databricks-on-aws.md
title: Risks of using rm -rf to drop Delta Lake tables
description: Using rm -rf to delete a Delta Lake table on S3 can lead to stale data issues; Databricks recommends using proper drop table operations instead.
tags:
  - delta-lake
  - s3
  - data-management
timestamp: "2026-06-19T18:20:35.437Z"
---

# Risks of using `rm -rf` to drop Delta Lake tables

Using the shell command `rm -rf` to delete the files of a [Delta Lake](/concepts/delta-lake.md) table stored on Amazon S3 is strongly discouraged. Databricks explicitly warns against this practice and recommends using the proper [`DROP TABLE` operation](https://docs.databricks.com/aws/en/tables/operations/drop-table) instead. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Stale data after deleting files with `rm -rf`

Directly removing table files with `rm -rf` bypasses Delta Lake’s transactional metadata. Because Delta Lake implements its **own versioning and garbage collection**, the system does not know that the files have been deleted externally. This can leave the Delta [transaction log](/concepts/delta-transaction-log.md) pointing to non‑existent data files, causing stale references and potentially corrupting queries or downstream processes. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Why it is risky

When bucket versioning is enabled on the S3 bucket, the problem is compounded: S3 retains deleted objects as versions, but Delta Lake’s garbage collection (`VACUUM`) considers those files permanently removed. This mismatch between the S3 object store and Delta Lake’s internal state can lead to unexpected behavior, such as:

- Stale data appearing in query results because the transaction log still references old versions.
- Inability to clean up storage space effectively because `VACUUM` cannot mark those files as deletable.
- Confusion between S3‑versioned copies and Delta‑versioned snapshots.

Databricks recommends **not** enabling bucket versioning for buckets that hold Delta Lake data, and never using `rm -rf` to drop a table. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Recommended alternative

Instead of `rm -rf`, use the `DROP TABLE` SQL command or the Databricks table‑deletion UI. This ensures that the Delta transaction log is properly updated and that all metadata references are cleaned up safely. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Related concepts

- [Delta Lake](/concepts/delta-lake.md) – The open‑source storage layer that provides ACID transactions and versioning.
- [Transaction log](/concepts/delta-transaction-log.md) – The core metadata that Delta Lake uses to track table state.
- VACUUM – A Delta Lake command that garbage‑collects unreferenced data files.
- [S3 bucket versioning](/concepts/s3-bucket-versioning-and-delta-lake.md) – A feature that can conflict with Delta Lake’s own versioning.
- DROP TABLE – The correct way to remove a [Delta Lake Table](/concepts/delta-lake-table.md).

## Sources

- delta-lake-limitations-on-s3-databricks-on-aws.md

# Citations

1. [delta-lake-limitations-on-s3-databricks-on-aws.md](/references/delta-lake-limitations-on-s3-databricks-on-aws-516e860e.md)
