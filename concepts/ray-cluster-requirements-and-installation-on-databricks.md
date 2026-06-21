---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 46c7ebe4733642ba0837a1e3cfd78fc81d9e959c989ae53a7f60adad0d9a66a9
  pageDirectory: concepts
  sources:
    - create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-cluster-requirements-and-installation-on-databricks
    - installation on Databricks and Ray cluster requirements
    - RCRAIOD
  citations:
    - file: create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
title: Ray cluster requirements and installation on Databricks
description: Prerequisites for creating Ray clusters on Databricks including Databricks Runtime 12.2 LTS ML+, access modes, and Ray installation methods for different runtime versions
tags:
  - ray
  - databricks
  - setup
  - prerequisites
timestamp: "2026-06-18T14:50:16.018Z"
---

# Ray Cluster Requirements and Installation on Databricks

**Ray cluster requirements and installation on Databricks** covers the prerequisites, installation methods, and configuration best practices for running Ray compute clusters on top of Databricks compute resources. Ray clusters on Databricks enable distributed machine learning workloads, including training, tuning, and inference, while leveraging the Databricks platform for data processing and cluster management.

## Requirements

To create a Ray cluster on Databricks, you must have access to a Databricks all-purpose compute resource with the following settings:

- **Databricks Runtime**: Databricks Runtime 12.2 LTS ML and above.
- **Access mode**: Dedicated (formerly single user) or no isolation shared access modes.

Ray clusters are currently not supported on serverless compute. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Install Ray

With Databricks Runtime ML 15.0 onwards, Ray is preinstalled on Databricks clusters. For runtimes released prior to 15.0, use pip to install Ray on your cluster:

```python
%pip install ray[default]>=2.3.0
```

^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Creating a Ray Cluster

### User-Specific Ray Cluster

To create a Ray cluster available only to the current notebook user, use the `ray.util.spark.setup_ray_cluster` API. The Ray cluster is automatically shut down after the notebook is detached from the cluster or after 30 minutes of inactivity (no tasks submitted to Ray). ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

**Fixed-size Ray cluster example:**

```python
import ray
from ray.util.spark import setup_ray_cluster, shutdown_ray_cluster

setup_ray_cluster(
    max_worker_nodes=1,
    collect_log_to_path="/dbfs/path/to/ray_collected_logs"
)

ray.init(ignore_reinit_error=True)
```

^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Global Mode Ray Cluster (Ray 2.9.0+)

A global mode Ray cluster allows all users attached to the Databricks compute resource to use the Ray cluster. This mode does not have the active timeout functionality that a single-user Ray cluster has. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

To start a global Ray cluster:

```python
from ray.util.spark import setup_global_ray_cluster

setup_global_ray_cluster(
    max_worker_nodes=2,
    # other arguments are the same as with setup_ray_cluster
)
```

This is a blocking call that remains active until interrupted, the notebook is detached, or the Databricks cluster is terminated. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

**Global mode cluster properties:**
- Only one active global mode Ray cluster can exist per Databricks cluster at a time.
- All users in any attached Databricks notebook can use the cluster by calling `ray.init()`.
- Resource contention may occur since multiple users can access the same Ray cluster.
- No automatic shutdown timeout exists for global mode clusters. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### GPU Ray Cluster

For GPU workloads, you can configure GPU resources for both head and worker nodes:

```python
from ray.util.spark import setup_ray_cluster, shutdown_ray_cluster

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

^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Connecting to Remote Ray Clusters

In Ray version 2.3.0 and above, you can obtain a remote connection string from `setup_ray_cluster`:

```python
from ray.util.spark import setup_ray_cluster

_, remote_conn_str = setup_ray_cluster(num_worker_nodes=2, ...)
```

Then connect remotely:

```python
import ray
ray.init(remote_conn_str)
```

The Ray client does not support the Ray dataset API (`ray.data` module). As a workaround, wrap Ray dataset API calls inside a remote Ray task. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Log Output Location

Set the `collect_log_to_path` argument to specify where Ray cluster logs are collected after shutdown. Databricks recommends setting a path starting with `/dbfs/` or a Unity Catalog Volume path to preserve logs even after terminating the Apache Spark cluster. Without this setting, logs are not recoverable since local storage is deleted when the cluster shuts down. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Best Practices

### Non-GPU Workloads

When using Spark for data preprocessing and Ray for GPU-accelerated ML tasks, set `spark.task.resource.gpu.amount` to `0` in the Apache Spark cluster configuration. This prevents Spark jobs from using GPU resources, increasing Spark job parallelism and avoiding competition with Ray workloads for GPU devices. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Disable Transformers Trainer MLflow Integration

The `transformers` trainer MLflow integration is enabled by default. If using Ray Train to fine-tune a transformers model, Ray tasks may fail due to credential issues. Set the `DISABLE_MLFLOW_INTEGRATION` environment variable to `'TRUE'` in the Databricks cluster configuration to avoid this issue. This does not apply if using MLflow directly for training. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Address Pickling Errors

Ray pickles task functions for remote execution. Common pickling errors arise from external references, closures, and stateful objects. A common fix is to move import statements inside the task function declaration. For example, `datasets.load_dataset` is patched on the Databricks driver side and becomes unpicklable; move the import inside the task function to resolve this. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Disable Ray Memory Monitor

In Ray 2.9.3, the Ray memory monitor has known issues that can cause Ray tasks to be inadvertently stopped. To address this, set the environment variable `RAY_memory_monitor_refresh_ms` to `0` in the Databricks cluster configuration. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Batch Data Processing

Use the Ray Data API with `map_batches` for efficient batch processing. Convert any Spark DataFrame to a Ray Dataset using `ray.data.from_spark`. Write processed output to Databricks Unity Catalog tables using `ray.data.write_databricks_table`. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Using MLflow with Ray

Integrating Databricks MLflow and Ray requires Ray 2.41 and above. Set the following environment variables before calling `ray.util.spark.setup_ray_cluster`:

```python
import os
from ray.util.spark import setup_ray_cluster

os.environ["DATABRICKS_HOST"] = "https://....databricks.com"
os.environ["DATABRICKS_TOKEN"] = "<your PAT token>"

setup_ray_cluster(num_cpus_worker_node=2, num_gpus_worker_node=0, max_worker_nodes=1, min_worker_nodes=1)
```

Alternatively, set `DATABRICKS_HOST`, `DATABRICKS_CLIENT_ID`, and `DATABRICKS_CLIENT_SECRET` instead of using a PAT token. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Notebook-Scoped Python Libraries

Using notebook-scoped Python libraries or cluster Python libraries in remote Ray tasks requires Ray 2.12 and above. For Ray versions 2.11 and below, additional dependencies must be pre-installed using `%pip` before starting the Ray cluster. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Related Concepts

- Ray Cluster Scaling on Databricks – Auto-scaling Ray clusters
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – ML-optimized runtime versions
- GPU Scheduling – Managing GPU resources for distributed workloads
- MLflow Integration with Ray – Tracking Ray experiments with MLflow
- Unity Catalog Volumes – Persistent storage for logs and artifacts

## Sources

- create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md

# Citations

1. [create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md](/references/create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws-68773ede.md)
