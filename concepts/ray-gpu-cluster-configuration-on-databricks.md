---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a930f8ef256b769032fc2f2b0bf2f41625f69d301a20641efa862afbcba51015
  pageDirectory: concepts
  sources:
    - create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-gpu-cluster-configuration-on-databricks
    - RGCCOD
  citations:
    - file: create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
title: Ray GPU cluster configuration on Databricks
description: Configuring GPU resources for Ray clusters on Databricks, including head/worker node GPU allocation and best practices for mixed GPU/CPU workloads
tags:
  - ray
  - gpu
  - databricks
timestamp: "2026-06-18T14:50:12.622Z"
---

Here is the wiki page for "Ray GPU cluster configuration on Databricks".

---

## Ray GPU cluster configuration on Databricks

**Ray GPU cluster configuration on Databricks** refers to the process of creating and managing Ray compute clusters on the Databricks platform that are provisioned with GPU (Graphics Processing Unit) resources. This configuration enables the execution of [GPU-accelerated](/concepts/gpu-accelerated-xgboost-training.md) workloads, such as deep learning and [machine learning](/concepts/cicd-for-machine-learning.md) training tasks, within the Databricks environment.

### Overview

To create a Ray cluster on Databricks, you must have access to a Databricks all-purpose compute resource. The required settings for this compute resource are:

- **Runtime**: Databricks Runtime 12.2 LTS ML and above. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]
- **Access mode**: Dedicated (formerly single user) or no isolation shared access modes. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

> **Note:** Ray clusters are currently not supported on [serverless compute](/concepts/serverless-gpu-compute.md). ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Installation

With Databricks Runtime ML 15.0 onwards, Ray is preinstalled on Databricks clusters. For earlier runtimes, you can install Ray using `pip`:

```python
%pip install ray[default]>=2.3.0
```

^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Creating a GPU Ray Cluster

You can create a GPU-accelerated Ray cluster by specifying the number of GPUs per node using the `setup_ray_cluster()` API. The following example configures a cluster with 2 to 4 worker nodes, each with 1 GPU: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

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

# Pass any custom Ray configuration with ray.init
ray.init(ignore_reinit_error=True)
```

### Global Mode Ray Cluster

Using Ray 2.9.0 and above, you can create a **global mode** Ray cluster. This allows all users attached to the Databricks compute resource to also use the Ray cluster. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
from ray.util.spark import setup_global_ray_cluster
setup_global_ray_cluster(
  max_worker_nodes=2,
  ...  # other arguments
)
```

Key properties of a global mode cluster include:
- Only one active global mode Ray cluster can exist at a time on a Databricks cluster. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]
- It can be used by all users in any attached Databricks notebook. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]
- It remains active until the `setup_ray_cluster` call is interrupted; it does not have an automatic shutdown timeout. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Configuring Log Output

You can set the `collect_log_to_path` argument to specify a destination for Ray cluster logs. Databricks recommends using a path starting with `/dbfs/` or a Unity Catalog Volume path to preserve logs if the Apache Spark cluster is terminated. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Best Practices for GPU Workloads

#### Adjusting GPU Resource Allocation for Spark

To prevent Apache Spark tasks from consuming GPU resources intended for Ray, set the Spark configuration `spark.task.resource.gpu.amount` to `0`. This prevents Spark UDFs and DataFrame transformations from using GPUs, which has two benefits: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

- It increases Spark job parallelism, as the GPU instance type typically has many more CPU cores than GPU devices. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]
- It prevents Spark jobs from competing for GPU resources with concurrently running Ray workloads. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

#### Handling Transformers and MLflow

If you use Ray train to fine-tune a [transformers](/concepts/mlflow-transformers-flavor.md) model, the **transformers trainer MLflow integration** (enabled by default) will cause Ray tasks to fail due to a credential issue. To avoid this, set the `DISABLE_MLFLOW_INTEGRATION` environment variable to `'TRUE'` when starting your Apache Spark cluster. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

#### Ray Remote Function Pickling Errors

If you encounter pickling errors when running Ray tasks, a common fix is to move import statements inside the task function. For example, the `datasets.load_dataset` function is often patched on the driver side; placing the import inside the task function resolves the issue: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
def ray_task_func():
  from datasets import load_dataset  # import inside
  ...
```

#### Disabling the Ray Memory Monitor (Ray 2.9.3)

In Ray 2.9.3, the Ray memory monitor has known issues that can stop tasks unexpectedly. To avoid this, set the environment variable `RAY_memory_monitor_refresh_ms` to `0` within the Databricks cluster configuration. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Using MLflow with Ray

Integration of Databricks MLflow with Ray requires Ray 2.41 and above. To use MLflow with Ray Tune, Ray Train, or custom Ray tasks, set the following environmental variables before calling `setup_ray_cluster`: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
import os
from ray.util.spark import setup_ray_cluster

os.environ["DATABRICKS_HOST"] = "https://....databricks.com"
os.environ["DATABRICKS_TOKEN"] = "<your PAT token>"
setup_ray_cluster(num_cpus_worker_node=2, ...)
```

### Related Concepts

- Ray cluster creation
- Ray GPU cluster
- Ray for machine learning
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- GPU scheduling
- [A100 GPU support](/concepts/a100-gpu-support-on-databricks.md)

### Sources

- create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md

# Citations

1. [create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md](/references/create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws-68773ede.md)
