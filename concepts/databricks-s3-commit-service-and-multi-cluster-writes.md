---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6d58e5e6553a2823aaf8ef68248229301e3fd26978681f78a17d9e78d0fa73c4
  pageDirectory: concepts
  sources:
    - delta-lake-limitations-on-s3-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-s3-commit-service-and-multi-cluster-writes
    - Multi-cluster Writes and Databricks S3 Commit Service
    - DSCSAMW
    - Configure Databricks S3 commit service-related settings
    - Configuring Databricks S3 Commit Service
    - Databricks S3 commit service
  citations:
    - file: delta-lake-limitations-on-s3-databricks-on-aws.md
title: Databricks S3 Commit Service and Multi-cluster Writes
description: Databricks provides an S3 commit service to support multi-cluster writes within a single workspace; certain features like SSE-C and STS-dependent credential paths are unsupported in this mode.
tags:
  - databricks
  - s3
  - commit-service
  - multi-cluster
timestamp: "2026-06-19T10:00:22.078Z"
---

Here is the wiki page for "Databricks S3 Commit Service and Multi-cluster Writes", written based solely on the provided source material.

---

## Databricks S3 Commit Service and Multi-cluster Writes

**Databricks S3 Commit Service** is a mechanism that enables [Delta Lake](/concepts/delta-lake.md) tables stored on Amazon S3 to support concurrent writes from multiple clusters within the same workspace. It addresses the limitations of S3's [eventual consistency](/concepts/s3-eventually-consistent-model.md) model, which can lead to conflicts or data corruption when multiple systems modify the same data simultaneously. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Multi-cluster Write Capabilities

Delta Lake supports multi-cluster writes by default, meaning queries writing to a table from multiple clusters at the same time will not corrupt the table. For Delta Lake tables stored on S3, this guarantee is limited to a single Databricks workspace. Modifying the same [Delta Lake Table](/concepts/delta-lake-table.md) stored in S3 from different workspaces can lead to potential data corruption and data loss issues, and Databricks recommends against doing so. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

The following features are not supported when running in multi-cluster write mode on S3:

- Server-Side Encryption with Customer-Provided Encryption Keys (SSE-C)
- S3 paths with credentials in a cluster that cannot access AWS Security Token Service (STS) ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Disabling Multi-cluster Writes

Multi-cluster writes can be turned off by setting `spark.databricks.delta.multiClusterWrites.enabled` to `false`. If turned off, all writes to a single table must originate from a single cluster. Modifying the same [Delta Lake Table](/concepts/delta-lake-table.md) from multiple clusters concurrently with this setting disabled can cause data loss or data corruption. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

For more information on configuring the S3 commit service-related settings, see the Databricks documentation on [Configure Databricks S3 commit service-related settings](https://docs.databricks.com/aws/en/security/network/classic/s3-commit-service). ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The open-format storage layer enabling ACID transactions on data lakes.
- Multi-cluster Writes — A Delta Lake feature allowing concurrent writes from multiple clusters.
- [S3 Consistency Model](/concepts/s3-eventually-consistent-model.md) — Amazon S3's eventual consistency guarantees that impact concurrent write operations.
- CONFIGURE DLI MIT SERVICE RELATED SETTINGS — Official Databricks configuration documentation for the commit service.

## Sources

- delta-lake-limitations-on-s3-databricks-on-aws.md

# Citations

1. [delta-lake-limitations-on-s3-databricks-on-aws.md](/references/delta-lake-limitations-on-s3-databricks-on-aws-516e860e.md)
