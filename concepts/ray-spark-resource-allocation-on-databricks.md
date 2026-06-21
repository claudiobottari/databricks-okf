---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eb39a6441665d3e2aa640e2276cd6aec3e9f0e54aaa38d8d98a4e51c3b7d1977
  pageDirectory: concepts
  sources:
    - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-spark-resource-allocation-on-databricks
    - RRAOD
  citations:
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
title: Ray-Spark Resource Allocation on Databricks
description: Best practices for configuring CPU and GPU resources when running Ray and Spark workers on the same Databricks cluster, including num_cpus_worker_node settings
tags:
  - ray
  - spark
  - databricks
  - configuration
timestamp: "2026-06-19T09:17:25.557Z"
---

# Ray-Spark Resource Allocation on Databricks

**Ray-Spark Resource Allocation on Databricks** refers to the configuration practices and constraints for running Ray and Apache Spark in the same execution environment on Databricks, ensuring that both distributed computing engines have sufficient compute resources and operate without interference.

## Overview

When combining Ray and Spark workloads on Databricks, resource allocation must account for the fact that both frameworks consume CPUs, GPUs, and memory on the same cluster nodes. Proper configuration prevents resource starvation, cache misses, and performance degradation. The core principle is that each Spark worker node typically launches one Ray worker node that fully utilizes the node’s resources. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Key Configuration Parameters

### CPU Allocation

- **`num_cpus_worker_node`**: This configuration must match the number of CPU cores available on the Spark worker node. When Ray tasks are expected to also run Spark operations (e.g., via Spark Connect), it is recommended to reserve one CPU for Spark by setting `num_cpus_worker_node` to one less than the total cores on the worker node. For example, if a worker node has 8 CPUs, set `num_cpus_worker_node = 7`. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

- When using [Spark Connect](/concepts/spark-connect.md) from Ray tasks, the Spark driver runs on the cluster driver node, and the Ray worker must have enough CPU capacity for both its own tasks and the Spark executor processes. The allocation approach described above ensures Spark has a dedicated CPU to avoid contention. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### GPU Allocation

- **`num_gpus_worker_node`**: Set this to the number of GPUs per Spark worker node to ensure Ray can leverage the same GPU resources as Spark. This is critical for GPU-accelerated workloads such as deep learning inference or training with [Ray Train](/concepts/ray-train-resource-allocation.md). ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Autoscaling Considerations

Autoscaling Spark clusters (including those using spot instances) require special handling when using `ray.data.from_spark()` to transfer data in memory from Spark to Ray. The `use_spark_chunk_api` parameter must be set to `False` when autoscaling is enabled. Otherwise, the API call will result in cache misses because the Spark executor’s cache is lost when the executor terminates due to scaling down or spot instance preemption. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
ray_ds = ray.data.from_spark(df, use_spark_chunk_api=False)
```

## Best Practices

- Always refer to the Ray cluster best practice guide to ensure the cluster is fully utilized. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- Use Unity Catalog Volumes to store output data in a non-tabular format, providing governance and a shared staging area for Ray-to-Spark data transfers. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- For large datasets that exceed the driver node’s memory, prefer persisting Ray task outputs to a temporary location (DBFS or Unity Catalog Volumes) rather than collecting all data in memory, then reading with Spark. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- When using [Spark Connect](/concepts/spark-connect.md) from multiple concurrent Ray tasks, be aware that all tasks share a single Spark driver, creating a threading lock. This leads to sequential execution of Spark jobs; for high concurrency, persist outputs and combine later. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Limitations

- Unity Catalog currently does not share credentials for writing to tables from non-Spark writers (e.g., Ray Core tasks). All data written to a Unity Catalog table from a Ray Core task must be persisted and then read with Spark, or [Databricks Connect](/concepts/databricks-connect.md) must be set up within the Ray task. This adds overhead and requires careful resource planning. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Ray on Databricks](/concepts/ray-on-databricks.md)
- Spark on Databricks
- Ray Data
- [Spark Connect](/concepts/spark-connect.md)
- [Databricks Connect](/concepts/databricks-connect.md)
- Unity Catalog Volumes
- [In-memory Spark to Ray Transfer](/concepts/in-memory-spark-to-ray-data-transfer.md)
- Ray Cluster Best Practices

## Sources

- combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

# Citations

1. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
