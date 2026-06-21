---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d2b5d5215aaa04fa2ea6f041e0ae1c50ed2148c197735e43709335cc2086b842
  pageDirectory: concepts
  sources:
    - delta-lake-limitations-on-s3-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-multi-cluster-write-configuration
    - DLMWC
  citations:
    - file: delta-lake-limitations-on-s3-databricks-on-aws.md
title: Delta Lake multi-cluster write configuration
description: The spark.databricks.delta.multiClusterWrites.enabled setting controls whether multiple clusters can concurrently write to the same Delta Lake table; disabling it requires all writes to originate from a single cluster.
tags:
  - delta-lake
  - configuration
  - concurrency
timestamp: "2026-06-18T11:48:51.097Z"
---

# Delta Lake Multi-Cluster Write Configuration

**Delta Lake multi-cluster write configuration** governs how multiple compute clusters can concurrently write to the same Delta table stored on Amazon S3 within a single Databricks workspace. While Delta Lake provides built‑in support for multi-cluster writes, this guarantee does not extend across different workspaces, and certain S3 features are incompatible when multi-cluster writes are enabled. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Overview

By default, Delta Lake on Databricks allows multiple clusters in the same workspace to write to the same table simultaneously without corrupting the data. This is enabled by a coordination mechanism that uses the S3 commit service to manage atomic writes to the transaction log. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

However, due to Amazon S3’s **eventually consistent** model, this guarantee is limited to a **single Databricks workspace**. Databricks recommends that you do not modify the same Delta table stored in S3 from different workspaces, as concurrent writes across workspaces can lead to data corruption or data loss. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Limitations

When multi-cluster writes are enabled (the default), the following S3 features are **not supported**:

- **Server‑Side Encryption with Customer‑Provided Encryption Keys (SSE‑C)** – because the commit service cannot manage key material per request.
- **S3 paths with credentials in a cluster that cannot access AWS Security Token Service (STS)** – the commit service requires STS to generate temporary credentials.

If you rely on these features, you must disable multi-cluster writes and ensure that all writes to a given table originate from a single cluster. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Disabling Multi-Cluster Writes

You can turn off multi-cluster writes by setting the Spark configuration property:

```python
spark.conf.set("spark.databricks.delta.multiClusterWrites.enabled", "false")
```

Or, when creating a cluster, set this configuration in the Spark config section.

> **Warning**: Disabling multi-cluster writes and then modifying the same Delta table from *multiple* clusters concurrently might cause data loss or data corruption. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

If you disable multi-cluster writes, all writes to a single table **must** originate from only one cluster at any given time.

## Best Practices

- Keep multi-cluster writes enabled (default) for all tables accessed by multiple clusters within the same workspace.
- Never modify the same Delta table from different workspaces when the table is stored on S3, even with multi-cluster writes enabled, because cross‑workspace coordination is not provided. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]
- If your workload requires SSE‑C keys or STS‑less S3 access, restrict writes to a single cluster and disable multi-cluster writes.
- For additional tuning of the S3 commit service, see [Configure Databricks S3 commit service-related settings](/concepts/databricks-s3-commit-service-and-multi-cluster-writes.md).

## Related Concepts

- [Delta Lake on S3](/concepts/delta-lake.md) – general considerations for using Delta Lake with Amazon S3
- [S3 Eventual Consistency](/concepts/s3-eventually-consistent-model.md) – underlying consistency model that limits cross‑workspace writes
- Delta Lake Multi-Cluster Writes – general concept of concurrent writes in Delta Lake
- Databricks S3 Commit Service – internal mechanism that coordinates atomic writes

## Sources

- delta-lake-limitations-on-s3-databricks-on-aws.md

# Citations

1. [delta-lake-limitations-on-s3-databricks-on-aws.md](/references/delta-lake-limitations-on-s3-databricks-on-aws-516e860e.md)
