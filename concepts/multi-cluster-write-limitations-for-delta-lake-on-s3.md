---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4ae8269daa3297cbefeb047f44b2e747da3b18b639c7543e3ea72e01e65725b2
  pageDirectory: concepts
  sources:
    - delta-lake-limitations-on-s3-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-cluster-write-limitations-for-delta-lake-on-s3
    - MWLFDLOS
  citations:
    - file: delta-lake-limitations-on-s3-databricks-on-aws.md
title: Multi-cluster Write Limitations for Delta Lake on S3
description: Delta Lake tables on S3 support multi-cluster writes only within a single Databricks workspace due to S3's eventual consistency model; cross-workspace writes risk data loss or corruption.
tags:
  - delta-lake
  - s3
  - consistency
  - multi-cluster
timestamp: "2026-06-19T10:00:09.026Z"
---

# Multi-cluster Write Limitations for Delta Lake on S3

**Multi-cluster Write Limitations for Delta Lake on S3** describe the constraints and risks associated with writing to the same [Delta Lake](/concepts/delta-lake.md) table stored in Amazon S3 from multiple Databricks workspace simultaneously. Due to S3’s eventually consistent model, concurrent writes across different workspaces may cause data corruption or loss, even though Delta Lake supports multi-cluster writes within a single workspace.

## Overview

Delta Lake provides built-in support for multi-cluster writes, meaning that queries writing to a table from multiple clusters at the same time will not corrupt the table under normal conditions. However, for Delta Lake tables stored on S3, this guarantee is **limited to a single Databricks workspace**.^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Limitations

- **Cross-workspace writes are not safe.** Databricks recommends not modifying the same [Delta Lake Table](/concepts/delta-lake-table.md) stored in S3 from different workspaces, as S3’s eventually consistent model can lead to potential data corruption and data loss.^[delta-lake-limitations-on-s3-databricks-on-aws.md]
- **Unsupported features** when operating in multi-cluster write mode:
  - Server-Side Encryption with Customer-Provided Encryption Keys (SSE-C).
  - S3 paths that use credentials in a cluster that cannot access AWS Security Token Service (STS).^[delta-lake-limitations-on-s3-databricks-on-aws.md]
- **Turning off multi-cluster writes** is possible by setting `spark.databricks.delta.multiClusterWrites.enabled` to `false`. If disabled, all writes to a single table must originate from a single cluster. Modifying the same table from multiple clusters concurrently with this setting off **might cause data loss or data corruption**.^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Recommendations

- **Stay within a single workspace** when multiple clusters need to write to the same [Delta Lake Table](/concepts/delta-lake-table.md) on S3. Use a single Databricks workspace to coordinate concurrent writes safely.
- **Do not disable** `spark.databricks.delta.multiClusterWrites.enabled` unless you are certain that only one cluster will write to the table at any given time.
- For more details on multi-cluster writes and the S3 commit service, see [Configure Databricks S3 commit service-related settings](/concepts/databricks-s3-commit-service-and-multi-cluster-writes.md).^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md)
- [Amazon S3 Consistency Model](/concepts/s3-eventually-consistent-model.md)
- Databricks Workspace Isolation
- VACUUM – Garbage collection that interacts with S3 versioning.
- [Delta Lake Limitations on S3](/concepts/delta-lake-limitations-on-s3.md) – Broader page covering bucket versioning and file deletion risks.

## Sources

- delta-lake-limitations-on-s3-databricks-on-aws.md

# Citations

1. [delta-lake-limitations-on-s3-databricks-on-aws.md](/references/delta-lake-limitations-on-s3-databricks-on-aws-516e860e.md)
