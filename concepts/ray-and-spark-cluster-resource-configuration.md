---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 122bdd478c31d44c11d8fc53fe5c52226c36b4efc16d91c95ee3b08d31fb4a2d
  pageDirectory: concepts
  sources:
    - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-and-spark-cluster-resource-configuration
    - Spark Cluster Resource Configuration and Ray
    - RASCRC
  citations:
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
title: Ray and Spark Cluster Resource Configuration
description: Best practices for configuring CPU and GPU resources when co-locating Ray and Spark worker nodes, including num_cpus_worker_node and num_gpus_worker_node settings.
tags:
  - databricks
  - ray
  - spark
  - cluster-configuration
timestamp: "2026-06-19T17:46:52.150Z"
---

# Ray and Spark Cluster Resource Configuration

**Ray and Spark Cluster Resource Configuration** refers to the settings and best practices for allocating compute resources when running Ray and Apache Spark in the same execution environment on Databricks. Proper configuration ensures both frameworks can operate efficiently without resource contention, enabling seamless data exchange between them.

## Overview

When Ray and Spark run together on the same cluster, each framework needs explicit resource allocation to avoid CPU or GPU starvation. Databricks supports co-located workloads by allowing you to set dedicated resource limits for Ray worker nodes that correspond to Spark worker node resources. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Resource Configuration for In‑Memory Transfers

The `ray.data.from_spark()` function transfers data directly from a Spark DataFrame to a Ray dataset without writing to disk. This feature requires:

- **Spark cluster config** `spark.databricks.pyspark.dataFrameChunk.enabled` set to `true` before starting the cluster.
- **Autoscaling clusters** (including those using spot instances) must set the `use_spark_chunk_api` parameter to `False` when calling `from_spark()`. Otherwise, cache misses occur because the Spark executor cache is lost when the executor terminates. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Resource Allocation for Co‑located Ray and Spark Workers

A common pattern is to launch one Ray worker node per Spark worker node, making the Ray worker fully utilize the Spark worker node’s resources. The configuration must align the number of CPUs and GPUs:

- **`num_cpus_worker_node`** – Set to the number of CPU cores available on the Spark worker node.
- **`num_gpus_worker_node`** – Set to the number of GPUs per Spark worker node.

When running Spark inside Ray tasks via [Spark Connect](/concepts/spark-connect.md), leave at least one CPU for Spark on each node. For example, if a worker node has 8 CPUs, set the Ray worker’s CPU allocation to 7, reserving 1 CPU for Spark. Larger Spark tasks require proportionally more reserved CPU resources. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Best Practices

- Follow the [Ray cluster best practices](/concepts/ray-cluster-scaling-best-practices.md) guide to ensure the cluster is fully utilized.
- Use Unity Catalog volumes to store intermediate output data with governance when writing from Ray Core tasks.
- For large intermediate datasets that exceed driver memory, persist Ray task outputs to a temporary location (such as DBFS or Unity Catalog volumes) and then consolidate them into a Spark DataFrame rather than accumulating results in memory. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Limitations Impacting Resource Configuration

Unity Catalog does not share credentials for writing to tables from non‑Spark writers. Consequently, any write from a Ray Core task to a Unity Catalog table requires either:

1. Persisting data to a temporary location and then reading it with Spark, or
2. Setting up [Databricks Connect](/concepts/databricks-connect.md) (Spark Connect) inside the Ray task, which introduces a threading lock on the single Spark driver, causing sequential execution of Spark tasks. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Ray on Databricks](/concepts/ray-on-databricks.md)
- Spark on Databricks
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The runtime version that supports in‑memory Spark‑to‑Ray transfers (15.0 and above).
- [Spark Connect](/concepts/spark-connect.md) – Enables Ray tasks to interact with a Spark cluster directly.
- Autoscaling – Requires special configuration for `from_spark()`.
- GPU Scheduling – Relevant when configuring `num_gpus_worker_node`.
- Unity Catalog Volumes – Recommended temporary storage for Ray outputs.
- [Delta Lake](/concepts/delta-lake.md) – Common storage format for data written from Ray to Spark.
- Data Transfer Between Ray and Spark – Broader topic covering three main integration patterns.

## Sources

- combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

# Citations

1. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
