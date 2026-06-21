---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 03e6531a388884e859e141da2e3e759a0c7bc660af6201238a8b4743adb1e632
  pageDirectory: concepts
  sources:
    - delta-lake-limitations-on-s3-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unsupported-features-for-delta-lake-on-s3-with-multi-cluster-writes
    - UFFDLOSWMW
  citations:
    - file: delta-lake-limitations-on-s3-databricks-on-aws.md
title: Unsupported features for Delta Lake on S3 with multi-cluster writes
description: Server-Side Encryption with Customer-Provided Keys (SSE-C) and S3 paths with credentials lacking STS access are not supported when multi-cluster writes are enabled on Delta Lake tables stored in S3.
tags:
  - delta-lake
  - s3
  - encryption
  - security
timestamp: "2026-06-19T18:20:30.401Z"
---

# Unsupported Features for Delta Lake on S3 with Multi-Cluster Writes

**Unsupported features for Delta Lake on S3 with multi-cluster writes** refers to two specific Amazon S3 configurations that are not supported when multiple clusters write concurrently to the same [Delta Lake](/concepts/delta-lake.md) table stored on S3. While Databricks and Delta Lake support multi-cluster writes by default — preventing table corruption when writes originate from multiple clusters **within the same workspace** — the eventually consistent nature of S3 imposes limitations when certain S3 features are used. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Unsupported Features

The following features are **not supported** when running in multi-cluster write mode for Delta Lake tables on S3:

- **Server-Side Encryption with Customer-Provided Encryption Keys (SSE-C)** — S3 server‑side encryption using customer‑provided keys is incompatible with the S3 commit service that Databricks uses to coordinate concurrent writes across clusters. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]
- **S3 paths with embedded credentials** when the cluster cannot access AWS Security Token Service (STS) — If a cluster uses access keys directly in the S3 path (e.g., `s3://key:secret@bucket/path`) and that cluster lacks the ability to call STS, multi-cluster writes are not supported. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Scope of the Limitation

Multi-cluster write support for Delta Lake on S3 is guaranteed only within a **single Databricks workspace**. Modifying the same table from different workspaces concurrently is not recommended and may lead to data corruption or data loss due to S3’s eventual consistency model. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Disabling Multi-Cluster Writes

You can disable multi-cluster writes by setting `spark.databricks.delta.multiClusterWrites.enabled` to `false`. When disabled, **all writes to a single table must originate from a single cluster**. If multiple clusters write to the same table while multi-cluster writes are off, data loss or corruption can occur. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md)
- [Multi-cluster writes](/concepts/multi-cluster-writes-feature-toggle.md)
- Amazon S3
- Server-Side Encryption
- AWS Security Token Service
- Data corruption
- [S3 commit service](/concepts/s3-commit-service-for-delta-lake.md)
- Eventually consistent storage

## Sources

- delta-lake-limitations-on-s3-databricks-on-aws.md

# Citations

1. [delta-lake-limitations-on-s3-databricks-on-aws.md](/references/delta-lake-limitations-on-s3-databricks-on-aws-516e860e.md)
