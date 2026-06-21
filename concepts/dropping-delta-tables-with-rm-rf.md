---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c2aec553bf0a54ecb0c8c59d1f223b043d3535ffa67aa61edb9078e5f51a7192
  pageDirectory: concepts
  sources:
    - delta-lake-limitations-on-s3-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dropping-delta-tables-with-rm-rf
    - DDTWR-
  citations:
    - file: delta-lake-limitations-on-s3-databricks-on-aws.md
title: Dropping Delta Tables with rm -rf
description: Using rm -rf to drop a Delta Lake table on S3 leads to stale data issues; Databricks recommends using proper table drop or replace operations instead.
tags:
  - delta-lake
  - s3
  - table-operations
timestamp: "2026-06-18T15:15:17.298Z"
---

# Dropping Delta Tables with rm -rf

**Dropping Delta Tables with rm -rf** refers to the practice of using the Unix `rm -rf` command to delete [Delta Lake Table](/concepts/delta-lake-table.md) files directly from the filesystem (such as Amazon S3). This approach is strongly discouraged by Databricks due to the risk of stale data and potential data corruption.

## Risks

Using `rm -rf` to drop a [Delta Lake Table](/concepts/delta-lake-table.md) can lead to stale data issues. When you delete Delta table files directly from the filesystem, the Delta transaction log may still contain references to those files, creating inconsistencies between the table metadata and the actual data on disk. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Recommended Approach

Instead of using `rm -rf`, Databricks recommends using the proper table drop operations. See [Drop or replace a table](/concepts/create-or-replace-table-clone.md) for the correct methods to safely remove Delta Lake tables. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Related Concepts

- Delta Lake table operations — Proper methods for managing Delta tables
- VACUUM — Delta Lake garbage collection for cleaning up old files
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — The metadata layer that tracks table state
- [Delta Lake Limitations on S3](/concepts/delta-lake-limitations-on-s3.md) — Broader constraints when using Delta Lake with Amazon S3

## Sources

- delta-lake-limitations-on-s3-databricks-on-aws.md

# Citations

1. [delta-lake-limitations-on-s3-databricks-on-aws.md](/references/delta-lake-limitations-on-s3-databricks-on-aws-516e860e.md)
