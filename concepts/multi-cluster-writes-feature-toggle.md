---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cab43df104b1f8d8b8410257f06acf98555c7a5b95300b4299e697916cd5c1b9
  pageDirectory: concepts
  sources:
    - delta-lake-limitations-on-s3-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-cluster-writes-feature-toggle
    - MWFT
    - Multi-cluster writes
    - Multi‑cluster writes
    - multi-cluster writes
  citations:
    - file: delta-lake-limitations-on-s3-databricks-on-aws.md
title: Multi-cluster writes feature toggle
description: The spark.databricks.delta.multiClusterWrites.enabled setting controls whether Delta Lake tables on S3 support concurrent writes from multiple clusters; disabling it requires single-cluster access.
tags:
  - delta-lake
  - configuration
  - spark
timestamp: "2026-06-19T18:20:25.268Z"
---

# Multi-cluster writes feature toggle

The **Multi-cluster writes feature toggle** is a configuration setting in [Delta Lake](/concepts/delta-lake.md) on Databricks that controls whether multiple clusters can write to the same [Delta table](/concepts/delta-lake-table.md) concurrently. This toggle is configured via the Spark configuration property `spark.databricks.delta.multiClusterWrites.enabled`. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Default behavior

By default, multi-cluster writes are enabled, meaning that queries writing to a table from multiple clusters at the same time will not corrupt the table. This provides a safety guarantee for concurrent write operations across different clusters within the same workspace. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## S3-specific limitations

For [Delta Lake tables stored on Amazon S3](/concepts/delta-lake-table-deletion-on-s3.md), the guarantee of safe multi-cluster writes is limited to a **single Databricks workspace**. To avoid potential data corruption and data loss, Databricks recommends that you do not modify the same [Delta Lake Table](/concepts/delta-lake-table.md) stored in S3 from different workspaces. This limitation exists because Amazon S3 uses an eventually consistent model, which can lead to problems when multiple systems or clusters modify data in the same table simultaneously. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Disabling multi-cluster writes

You can turn off multi-cluster writes by setting `spark.databricks.delta.multiClusterWrites.enabled` to `false`. If the feature is turned off, writes to a single table **must** originate from a single cluster. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

> **⚠️ Warning:** Turning off this feature and modifying the same [Delta Lake Table](/concepts/delta-lake-table.md) from multiple clusters concurrently might cause data loss or data corruption. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Unsupported features when multi-cluster writes are enabled

The following features are not supported when running with multi-cluster writes enabled for Delta Lake tables on S3:

- Server-Side Encryption with Customer-Provided Encryption Keys (SSE-C)
- S3 paths with credentials in a cluster that cannot access AWS Security Token Service (STS)

^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Related concepts

- [Delta Lake](/concepts/delta-lake.md)
- [Delta table](/concepts/delta-lake-table.md)
- [S3 commit service](/concepts/s3-commit-service-for-delta-lake.md)
- [Concurrent write operations](/concepts/concurrent-copy-into-invocations.md)
- [Data consistency on S3](/concepts/s3-eventually-consistent-model.md)
- Table isolation levels

## Sources

- delta-lake-limitations-on-s3-databricks-on-aws.md

# Citations

1. [delta-lake-limitations-on-s3-databricks-on-aws.md](/references/delta-lake-limitations-on-s3-databricks-on-aws-516e860e.md)
