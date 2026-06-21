---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5471c676eac7216e2b8c76bf875976330e28b6d2916ca55b94c2612200f2d65e
  pageDirectory: concepts
  sources:
    - delta-lake-limitations-on-s3-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-multi-cluster-write-restrictions-on-s3
    - DLMWROS
    - Delta Lake multi-cluster write limitations on S3
  citations:
    - file: delta-lake-limitations-on-s3-databricks-on-aws.md
title: Delta Lake multi-cluster write restrictions on S3
description: S3's eventual consistency model limits multi-cluster writes to a single Databricks workspace; cross-workspace writes to the same Delta table on S3 risk data corruption.
tags:
  - delta-lake
  - s3
  - databricks
  - consistency
timestamp: "2026-06-19T18:20:21.923Z"
---

# Delta Lake Multi-Cluster Write Restrictions on S3

**Delta Lake multi-cluster write restrictions on S3** refer to the limitations and risks associated with writing to the same [Delta Lake](/concepts/delta-lake.md) table stored in Amazon S3 from multiple clusters or workspaces simultaneously. These restrictions stem from S3's eventually consistent data model.

## Overview

Databricks and Delta Lake support multi-cluster writes by default, meaning that queries writing to a table from multiple clusters at the same time won't corrupt the table. However, for Delta Lake tables stored on S3, this guarantee is limited to a single Databricks workspace. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Major Restriction: Single Workspace Only

To avoid potential data corruption and data loss, Databricks recommends that you do not modify the same [Delta Lake Table](/concepts/delta-lake-table.md) stored in S3 from different workspaces. The eventually consistent model used in Amazon S3 can lead to potential problems when multiple systems or clusters modify data in the same table simultaneously. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

While multi-cluster writes within a single workspace are safe, attempting to write to the same table from multiple workspaces risks data corruption and data loss.

## Configuring Multi-Cluster Writes

You can turn off multi-cluster writes by setting `spark.databricks.delta.multiClusterWrites.enabled` to `false`. If multi-cluster writes are turned off, writes to a single table **must** originate from a single cluster. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

**Warning:** Turning off multi-cluster writes and modifying the same [Delta Lake Table](/concepts/delta-lake-table.md) from multiple clusters concurrently might cause data loss or data corruption. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Unsupported Features

The following features are not supported when running in multi-cluster write mode:

- Server-Side Encryption with Customer-Provided Encryption Keys (SSE-C) — AWS S3 server-side encryption using customer-provided keys
- S3 paths with credentials in a cluster that cannot access AWS Security Token Service (STS)

^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The open-source storage layer
- Amazon S3 — The underlying cloud storage
- Eventual Consistency — The data consistency model that causes these restrictions
- Single Workspace Write Guarantee — The scope within which Delta Lake guarantees data safety
- [Configuring Databricks S3 Commit Service](/concepts/databricks-s3-commit-service-and-multi-cluster-writes.md) — Related settings for multi-cluster writes
- [Bucket Versioning and Delta Lake](/concepts/s3-bucket-versioning-and-delta-lake.md) — Related limitation about S3 bucket versioning
- Concurrent Writes — General concept of simultaneous table modifications

## Sources

- delta-lake-limitations-on-s3-databricks-on-aws.md

# Citations

1. [delta-lake-limitations-on-s3-databricks-on-aws.md](/references/delta-lake-limitations-on-s3-databricks-on-aws-516e860e.md)
