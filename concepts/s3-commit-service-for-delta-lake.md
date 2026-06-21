---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 64b8024ea6d667240518e9af87c9fac00a2da46d7755e1a35e2de915f0463176
  pageDirectory: concepts
  sources:
    - delta-lake-limitations-on-s3-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - s3-commit-service-for-delta-lake
    - SCSFDL
    - S3 commit service
  citations:
    - file: delta-lake-limitations-on-s3-databricks-on-aws.md
title: S3 Commit Service for Delta Lake
description: Databricks provides an S3 commit service to help manage multi-cluster writes and consistency for Delta Lake tables stored on S3.
tags:
  - delta-lake
  - s3
  - consistency
  - databricks
timestamp: "2026-06-19T14:59:42.333Z"
---

## S3 Commit Service for Delta Lake

The **S3 Commit Service** is a Databricks feature that helps manage concurrent writes to [Delta Lake](/concepts/delta-lake.md) tables stored on Amazon S3. The source document provided does not contain detailed information about the configuration, architecture, or behavior of this service, but it references the service in the context of multi-cluster write limitations.

According to the source, Databricks recommends that you do not modify the same [Delta Lake Table](/concepts/delta-lake-table.md) stored in S3 from different workspaces, because S3’s eventually consistent model can cause problems during simultaneous concurrent modifications. For more information on how the S3 Commit Service supports multi-cluster writes, the source directs readers to the [Configure Databricks S3 commit service-related settings](https://docs.databricks.com/aws/en/security/network/classic/s3-commit-service) page. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The open‑source storage layer that provides ACID transactions on data lakes.
- Amazon S3 – The object store where Delta Lake tables may reside.
- [Multi-cluster writes](/concepts/multi-cluster-writes-feature-toggle.md) – Concurrent modifications from multiple clusters, which are limited by S3 consistency.
- [Delta Lake Limitations on S3](/concepts/delta-lake-limitations-on-s3.md) – Additional restrictions when using Delta Lake on S3.

## Sources

- delta-lake-limitations-on-s3-databricks-on-aws.md

# Citations

1. [delta-lake-limitations-on-s3-databricks-on-aws.md](/references/delta-lake-limitations-on-s3-databricks-on-aws-516e860e.md)
