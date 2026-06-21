---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c6392829f51d15ac05b3aedb201e6f3761085356df2264082165b20f46eede73
  pageDirectory: concepts
  sources:
    - delta-lake-limitations-on-s3-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-cluster-write-limitations-on-s3
    - MWLOS
    - Delta Lake multi-cluster write limitations on S3
    - Multi-cluster write limitations
    - multi-cluster write limitations
    - Multi-Cluster Writes
    - Multi-cluster writes on S3
  citations:
    - file: delta-lake-limitations-on-s3-databricks-on-aws.md
title: Multi-cluster Write Limitations on S3
description: Delta Lake tables on S3 have multi-cluster write guarantees limited to a single Databricks workspace due to S3's eventual consistency model; modifying the same table from different workspaces risks data corruption.
tags:
  - delta-lake
  - s3
  - consistency
  - aws
timestamp: "2026-06-19T14:59:16.394Z"
---

# Multi-cluster Write Limitations on S3

**Multi-cluster write limitations on S3** describe the constraints and risks associated with concurrently modifying the same [Delta Lake](/concepts/delta-lake.md) table stored in Amazon S3 from multiple clusters or workspaces. These limitations arise from S3's eventual consistency model, which can lead to data corruption or data loss when multiple systems write to the same table simultaneously. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Overview

Delta Lake and Databricks support multi-cluster writes by default, meaning that queries writing to a table from multiple clusters at the same time will not corrupt the table. However, for Delta Lake tables stored on S3, this guarantee is limited to a single Databricks workspace. Modifying the same [Delta Lake Table](/concepts/delta-lake-table.md) from different workspaces is not recommended. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Key Limitation: Cross-Workspace Writes

To avoid potential data corruption and data loss issues, Databricks recommends that you do not modify the same [Delta Lake Table](/concepts/delta-lake-table.md) stored in S3 from different workspaces. The eventually consistent model used in Amazon S3 can lead to potential problems when multiple systems or clusters modify data in the same table simultaneously. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Unsupported Features

The following features are not supported when running in multi-cluster write mode on S3: ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

- Server-Side Encryption with Customer-Provided Encryption Keys (SSE-C)
- S3 paths with credentials in a cluster that cannot access AWS Security Token Service (STS)

## Disabling Multi-Cluster Writes

You can turn off multi-cluster writes by setting `spark.databricks.delta.multiClusterWrites.enabled` to `false`. If multi-cluster writes are turned off, writes to a single table _must_ originate from a single cluster. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

> **Warning:** Turning off `spark.databricks.delta.multiClusterWrites.enabled` and modifying the same [Delta Lake Table](/concepts/delta-lake-table.md) from _multiple_ clusters concurrently might cause data loss or data corruption. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Best Practices

- **Keep writes within a single workspace.** For Delta Lake tables stored on S3, ensure all concurrent writes originate from clusters within the same Databricks workspace. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]
- **Avoid cross-workspace modifications.** Do not modify the same [Delta Lake Table](/concepts/delta-lake-table.md) from different workspaces to prevent consistency issues. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]
- **Understand the consistency model.** S3's eventual consistency means that changes made by one cluster may not be immediately visible to others, which can lead to conflicts and data corruption. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]
- **Consider alternative storage.** For workloads requiring multi-workspace writes, consider using storage solutions with stronger consistency guarantees.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The open-source storage layer that provides ACID transactions
- Amazon S3 — The cloud object storage service used for Delta Lake tables
- [Eventual consistency](/concepts/s3-eventually-consistent-model.md) — The consistency model of S3 that underlies these limitations
- [S3 commit service](/concepts/s3-commit-service-for-delta-lake.md) — Databricks service that helps manage concurrent writes to S3
- [Bucket versioning and Delta Lake](/concepts/s3-bucket-versioning-and-delta-lake.md) — Related S3 limitation regarding versioning
- Delta Lake table operations — Safe methods for dropping or replacing tables

## Sources

- delta-lake-limitations-on-s3-databricks-on-aws.md

# Citations

1. [delta-lake-limitations-on-s3-databricks-on-aws.md](/references/delta-lake-limitations-on-s3-databricks-on-aws-516e860e.md)
