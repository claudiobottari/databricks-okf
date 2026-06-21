---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 076dabd956ac98295fa8cf9884c0f623630d73bf55353c1902c7c7ec80875feb
  pageDirectory: concepts
  sources:
    - delta-lake-limitations-on-s3-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-multi-cluster-writes-configuration
    - DLMWC
  citations:
    - file: delta-lake-limitations-on-s3-databricks-on-aws.md
title: Delta Lake Multi-Cluster Writes Configuration
description: The spark.databricks.delta.multiClusterWrites.enabled setting controls multi-cluster writes; when disabled, writes to a single Delta table must originate from exactly one cluster to avoid corruption.
tags:
  - delta-lake
  - configuration
  - spark
timestamp: "2026-06-19T14:59:39.807Z"
---

# Delta Lake Multi-Cluster Writes Configuration

**Delta Lake Multi-Cluster Writes Configuration** refers to the settings and guarantees that control how multiple clusters can concurrently write to the same [Delta Lake Table](/concepts/delta-lake-table.md). By default, Delta Lake supports multi-cluster writes to prevent data corruption, but this support has specific limitations when tables are stored on Amazon S3. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Overview

Delta Lake and Databricks enable multi-cluster writes by default, meaning that queries writing to a table from multiple clusters at the same time will not corrupt the table. This is a built-in safety mechanism for concurrent write operations. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Limitations on Amazon S3

When Delta Lake tables are stored on Amazon S3, the multi-cluster write guarantee is **limited to a single Databricks workspace**. This is due to the [eventually consistent model](/concepts/s3-eventually-consistent-model.md) used by Amazon S3, which can lead to potential problems when multiple systems or clusters modify data in the same table simultaneously. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

To avoid potential data corruption and data loss issues, Databricks **recommends that you do not modify the same [Delta Lake Table](/concepts/delta-lake-table.md) stored on S3 from different workspaces**. Cross-workspace concurrent writes are not safe under the default configuration. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Configuration

You can turn off multi-cluster writes by setting the Spark configuration property to `false`:

```
spark.databricks.delta.multiClusterWrites.enabled = false
```

If multi-cluster writes are turned off, writes to a single table **must** originate from a single cluster. Modifying the same [Delta Lake Table](/concepts/delta-lake-table.md) from multiple clusters concurrently while this setting is `false` **may cause data loss or data corruption**. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Unsupported Features When Multi-Cluster Writes Are Enabled

When running with multi-cluster writes enabled (the default), the following features are **not supported** on S3:

- Server-Side Encryption with Customer-Provided Encryption Keys (SSE-C)
- S3 paths with credentials in a cluster that cannot access AWS Security Token Service (STS)

These limitations are inherent to the S3 commit service used by Databricks to coordinate multi-cluster writes. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md)
- [Amazon S3 Consistency Model](/concepts/s3-eventually-consistent-model.md)
- Databricks S3 Commit Service
- Delta Lake table operations
- VACUUM

## Sources

- delta-lake-limitations-on-s3-databricks-on-aws.md

# Citations

1. [delta-lake-limitations-on-s3-databricks-on-aws.md](/references/delta-lake-limitations-on-s3-databricks-on-aws-516e860e.md)
