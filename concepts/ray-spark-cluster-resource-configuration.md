---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d072a3547bea01c1ed1c7e13d6c1e434075c62fc7d6d5f69463dbab36251b59a
  pageDirectory: concepts
  sources:
    - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-spark-cluster-resource-configuration
    - RCRC
    - ray-and-spark-cluster-resource-configuration
    - Spark Cluster Resource Configuration and Ray
    - RASCRC
  citations:
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
title: Ray-Spark Cluster Resource Configuration
description: Best practices for configuring CPU and GPU resource allocations when running Ray and Spark on the same Databricks cluster, including num_cpus_worker_node and num_gpus_worker_node settings.
tags:
  - ray
  - spark
  - cluster-configuration
  - databricks
  - best-practices
timestamp: "2026-06-19T14:18:02.179Z"
---

# Ray–Spark Cluster Resource Configuration

**Ray–Spark Cluster Resource Configuration** refers to the CPU and GPU allocation settings that allow Ray and Apache Spark on Databricks|Spark to run in the same execution environment on Databricks without resource contention. Proper configuration ensures that both engines can operate efficiently within the same cluster nodes, enabling seamless data exchange and cooperative workloads.

## Overview

When Ray and Spark share a cluster, each Spark worker node typically launches one Ray worker node. The resource parameters `num_cpus_worker_node` and `num_gpus_worker_node` must be set so that the Ray worker fully utilizes the available CPU cores and GPUs of the underlying Spark worker node. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## CPU Resource Configuration

The most critical setting for CPU allocation is `num_cpus_worker_node`. This parameter should match the number of CPU cores available on the Spark worker node. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

When a separate [Spark Connect](/concepts/spark-connect.md) process must run alongside Ray (for example, to allow Ray tasks to interact with Spark DataFrames), the Ray worker should reserve CPU capacity for that process. As a rule of thumb, if a worker node has 8 CPUs, set `num_cpus_worker_node` to 7, leaving 1 CPU for the Spark driver process running on the node. For larger Spark tasks, allocate a larger share of resources. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## GPU Resource Configuration

For GPU-enabled clusters, the `num_gpus_worker_node` parameter must be set to the number of GPUs per Spark worker node. This ensures that each Ray worker has access to the correct number of GPUs and that GPU resources are not oversubscribed. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Spark Configuration

In addition to Ray-specific resource parameters, a Spark cluster configuration is required to enable in‑memory Spark‑to‑Ray data transfers. Set the following property **before starting the cluster**:

```
spark.databricks.pyspark.dataFrameChunk.enabled = true
```

This configuration allows the `ray.data.from_spark()` function to read a [Spark DataFrame](/concepts/spark-dataframe-evaluation-pattern.md) directly into a Ray dataset without writing to disk. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Autoscaling Considerations

Autoscaling Spark clusters — including those using spot instances — introduce additional constraints. When using the `ray.data.from_spark()` API on an autoscaling cluster, the `use_spark_chunk_api` parameter must be set to `False`. Otherwise, the operation fails because the chunk cache on a Spark executor is lost when the executor terminates due to scaling down. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
ray_ds = ray.data.from_spark(df, use_spark_chunk_api=False)
```

## Best Practices

- Always match the Ray worker resource configuration (`num_cpus_worker_node`, `num_gpus_worker_node`) to the Spark worker node’s available resources. This aligns one Ray worker per Spark worker node and maximizes utilization. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- When using [Spark Connect](/concepts/spark-connect.md) from within Ray tasks, be aware that all tasks serialize through a single Spark driver process, creating a threading lock. This pattern works best for workloads with few concurrent tasks; for high‑throughput scenarios, persist Ray output to a temporary location and combine into a Spark DataFrame afterwards. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- For writing data from Ray to [Unity Catalog](/concepts/unity-catalog.md) tables, note that Unity Catalog does not share credentials for non‑Spark writers. Data must be persisted to a temporary location (e.g., a Unity Catalog volume) and then read with Spark, or [Databricks Connect](/concepts/databricks-connect.md) must be set up inside the Ray task. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Limitations

- Autoscaling clusters have restricted compatibility with the in‑memory chunk transfer API, as described above.
- Third‑party libraries such as `deltalake` and `deltaray` can write to Delta Lake from Ray, but they currently work only with Hive [Metastore](/concepts/metastore.md) tables, not Unity Catalog tables. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Ray on Databricks](/concepts/ray-on-databricks.md)
- Spark on Databricks
- Ray Data
- [Spark Connect](/concepts/spark-connect.md)
- [Delta Lake](/concepts/delta-lake.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Distributed Computing Best Practices](/concepts/distributed-training-strategies-comparison.md)

## Sources

- combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

# Citations

1. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
