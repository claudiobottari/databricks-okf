---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ddab3660fcac630c8834d8f17f08dbf0071a3f8ac0a445ea02cef750c4bbc4b4
  pageDirectory: concepts
  sources:
    - create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-on-databricks-overview
    - RODO
  citations:
    - file: create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
title: Ray on Databricks Overview
description: Running Ray compute clusters on top of Databricks Spark clusters using Databricks Runtime ML
tags:
  - ray
  - databricks
  - compute
timestamp: "2026-06-19T09:30:52.218Z"
---

# Ray on Databricks Overview

**Ray on Databricks** refers to the integration of the open-source [Ray] distributed computing framework with the Databricks platform. Ray enables distributed training, hyperparameter tuning, reinforcement learning, and general-purpose parallel computing. On Databricks, Ray runs on top of Apache Spark clusters, allowing users to leverage the Spark ecosystem for data preprocessing while using Ray for machine learning workloads.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Requirements

To create a Ray cluster on Databricks, you need access to a Databricks all-purpose compute resource with the following settings:

- **Databricks Runtime:** Databricks Runtime 12.2 LTS ML and above.
- **Access mode:** Dedicated (formerly single user) or no isolation shared access mode.
- **Not supported:** Ray clusters are currently not supported on serverless compute.

^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Installing Ray

With Databricks Runtime ML 15.0 and above, Ray is pre-installed on the cluster. For older runtimes (12.2 LTS ML through 14.x ML), you must install Ray manually using a notebook-scoped pip command:

```python
%pip install ray[default]>=2.3.0
```

^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Creating a Ray Cluster

You create a Ray cluster from within a Databricks notebook by using the `ray.util.spark.setup_ray_cluster` API. The Ray cluster runs on top of the existing Spark cluster, borrowing its resources. Two modes are available: user-specific and global.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### User-Specific (Single-User) Ray Cluster

By default, a Ray cluster created with `setup_ray_cluster` is visible only to the current notebook user. It automatically shuts down when the notebook is detached from the cluster or after 30 minutes of inactivity. You can create both fixed-size and auto-scaling clusters. Example for a fixed-size cluster: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
import ray
from ray.util.spark import setup_ray_cluster, shutdown_ray_cluster

setup_ray_cluster(
    max_worker_nodes=1,
    collect_log_to_path="/dbfs/path/to/ray_collected_logs"
)
ray.init(ignore_reinit_error=True)
```

### Global Mode Ray Cluster

Using Ray 2.9.0 and above, you can start a global mode Ray cluster with `setup_global_ray_cluster`. This cluster is accessible to all users attached to the Databricks compute resource. It does not have an automatic inactivity timeout; it remains running until you interrupt the cell, detach the notebook, or terminate the Spark cluster. Only one global Ray cluster can be active per Databricks cluster at a time.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### GPU Clusters

To enable GPU support, specify `num_gpus_per_node` and `num_gpus_head_node` in the `setup_ray_cluster` call. Example: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
setup_ray_cluster(
    min_worker_nodes=2,
    max_worker_nodes=4,
    num_cpus_per_node=8,
    num_gpus_per_node=1,
    num_cpus_head_node=8,
    num_gpus_head_node=1,
    collect_log_to_path="/dbfs/path/to/ray_collected_logs"
)
ray.init(ignore_reinit_error=True)
```

## Connecting to a Ray Cluster

After creating a Ray cluster, you call `ray.init()` in the same notebook to connect. For remote connections (e.g., from another process), you can use the Ray client. The connection string is returned by `setup_ray_cluster`. Note that the Ray client does not support the `ray.data` API; as a workaround, wrap Ray Data operations inside a remote Ray task.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

The Ray Job CLI can also be used to submit jobs to the cluster by addressing the driver proxy URL, though Databricks recommends using existing tooling such as Databricks Asset Bundles or Workflow Triggers for job deployment.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Best Practices

- **Non-GPU workloads:** Set the Spark configuration `spark.task.resource.gpu.amount` to `0` to prevent Spark tasks from using GPU resources, leaving them exclusively for Ray. This also improves Spark task parallelism.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

- **MLflow integration:** If you use Ray Train with the Transformers library, set the environment variable `DISABLE_MLFLOW_INTEGRATION='TRUE'` in the cluster configuration to avoid credential issues. When using MLflow directly with Ray Tune, Ray Train, or custom Ray tasks (Ray 2.41+), set `DATABRICKS_HOST` and `DATABRICKS_TOKEN` (or `DATABRICKS_CLIENT_ID` and `DATABRICKS_CLIENT_SECRET`) before calling `setup_ray_cluster`.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

- **Pickling errors:** Move import statements inside Ray task functions to avoid pickling failures caused by external references that cannot be serialized.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

- **Ray memory monitor:** In Ray 2.9.3, known issues in the memory monitor can cause tasks to be killed unexpectedly. Disable it by setting `RAY_memory_monitor_refresh_ms=0` in the cluster configuration.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

- **Batch processing:** Use the Ray Data API with `map_batches` for efficient batch transformations. Convert Spark DataFrames to Ray Datasets with `ray.data.from_spark` and write results back to Databricks Unity Catalog tables using `ray.data.write_databricks_table`.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Logging and Shutdown

Set `collect_log_to_path` (e.g., `/dbfs/...` or a Unity Catalog volume path) to preserve Ray cluster logs after shutdown. Single-user clusters auto-terminate after 30 minutes of inactivity or when the notebook is detached. Global mode clusters remain active until explicitly stopped.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Related Concepts

- Ray – The open-source distributed computing framework.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – The ML runtime that includes Ray.
- GPU Scheduling – Best practices for sharing GPU resources between Spark and Ray.
- [MLflow on Databricks](/concepts/mlflow-on-databricks.md) – How to integrate MLflow tracking with Ray workloads.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – Ray’s role in scaling model training.

## Sources

- create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md

# Citations

1. [create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md](/references/create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws-68773ede.md)
