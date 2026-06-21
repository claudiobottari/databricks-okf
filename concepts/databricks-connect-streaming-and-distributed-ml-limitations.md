---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 15a813ab81e7284ee99ae99dc5ff6ea5f1f4ab5968d5974a2f45cdad1bf78ede
  pageDirectory: concepts
  sources:
    - limitations-with-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-streaming-and-distributed-ml-limitations
    - Distributed ML Limitations and Databricks Connect Streaming
    - DCSADML
  citations:
    - file: limitations-with-databricks-connect-for-python-databricks-on-aws.md
title: Databricks Connect Streaming and Distributed ML Limitations
description: Streaming foreachBatch, distributed ML training, and ApplyInPandas/Cogroup with standard access mode are unsupported in certain Databricks Connect runtime versions.
tags:
  - databricks
  - limitations
  - streaming
  - machine-learning
timestamp: "2026-06-19T19:12:29.938Z"
---

# Databricks Connect Streaming and Distributed ML Limitations

**Databricks Connect Streaming and Distributed ML Limitations** refers to the specific functionalities that are unavailable or restricted when using [Databricks Connect](/concepts/databricks-connect.md) for Python to interact with streaming data pipelines and distributed machine learning workloads. These limitations vary depending on the version of Databricks Runtime and Databricks Connect being used. ^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]

## Streaming Limitations

### `foreachBatch` in Streaming

The `foreachBatch` operation for streaming DataFrames is **not available** on Databricks Connect for Databricks Runtime 13.3 LTS and below. This means users cannot apply batch-level operations to micro-batches of streaming data when using these older runtime versions. ^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]

### Long-Running Streaming Queries

Long queries that exceed **3600 seconds** (1 hour) are **not available** on Databricks Connect for Databricks Runtime 13.3 LTS and below. This limitation affects streaming applications that require sustained execution beyond the one-hour threshold. ^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]

## Distributed ML Limitations

### Distributed ML Training

**Distributed ML training is not supported** in Databricks Connect. This means that [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) workflows that leverage multiple nodes or GPUs for model training cannot be executed through the Databricks Connect interface. Users must run distributed training directly on the cluster rather than through a remote client connection. ^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]

### Unavailable Libraries and Components

Several libraries and components that are commonly used in ML pipelines are unavailable with Databricks Connect. This includes libraries that depend on RDDs, Spark Context, or direct access to the underlying Spark JVM. Specific examples include:

- **Mosaic geospatial** library
- **GraphFrames**
- **GreatExpectations**

^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]

These libraries cannot be used through Databricks Connect, which constrains the types of ML and data engineering workflows that can be executed remotely.

## Version-Specific Limitations

| Feature | Runtime Version Limitation |
|---------|---------------------------|
| `foreachBatch` streaming | Not available on Runtime 13.3 LTS and below |
| Queries > 3600 seconds | Not available on Runtime 13.3 LTS and below |
| `ApplyInPandas()` and `Cogroup()` with standard access mode compute | Not available on Runtime 15.3 and below |
| UDFs with custom libraries on serverless compute | Not available on Runtime 16.3 and below |

^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]

## General Unavailable Features

Beyond streaming and ML-specific limitations, the following features are generally **not available** with Databricks Connect:

- `dataframe.display()` API
- Databricks Utilities: `credentials`, `library`, `notebook workflow`, `widgets`
- Spark Context
- RDDs
- `CREATE TABLE <table-name> AS SELECT` (use `spark.sql("SELECT ...").write.saveAsTable("table")` instead)
- Changing the log4j log level through `SparkContext`
- Synchronizing the local development environment with the remote cluster

^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library for connecting remote applications to Databricks clusters
- Streaming DataFrames — Structured streaming on Databricks
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Multi-node ML training approaches
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Memory-efficient distributed training
- Databricks Runtime — The runtime environment on Databricks clusters
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — On-demand GPU infrastructure for ML workloads

## Sources

- limitations-with-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [limitations-with-databricks-connect-for-python-databricks-on-aws.md](/references/limitations-with-databricks-connect-for-python-databricks-on-aws-334fca41.md)
