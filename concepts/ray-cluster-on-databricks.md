---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 729e588da6e4ec06a132a4db91be0ff5021ca102f335aca2263fbe24591bdf42
  pageDirectory: concepts
  sources:
    - create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-cluster-on-databricks
    - RCOD
    - GPU Clusters on Databricks
    - GPU clusters on Databricks
    - Ray Cluster Scaling on Databricks
    - Ray Cluster Setup on Databricks
    - Ray Clusters on Databricks
    - Scale Ray clusters on Databricks
    - Scaling Ray Clusters on Databricks
  citations:
    - file: create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
title: Ray Cluster on Databricks
description: Creating and running Ray compute clusters on top of Databricks Spark clusters using the ray.util.spark.setup_ray_cluster API
tags:
  - ray
  - databricks
  - distributed-computing
timestamp: "2026-06-19T17:57:48.936Z"
---

# Ray Cluster on Databricks

**Ray Cluster on Databricks** refers to the deployment and management of [Ray](https://ray.io) compute clusters within a Databricks environment. Ray is a unified framework for scaling AI and Python applications, and on Databricks it runs on top of an Apache Spark cluster provisioned through Databricks compute resources. This setup enables users to combine Spark data processing with Ray-based distributed machine learning and inference workloads. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Requirements

To create a Ray cluster, you must have access to a Databricks all-purpose compute resource with the following settings:

- **Databricks Runtime**: 12.2 LTS ML and above.
- **Access mode**: Dedicated (formerly single user) or no isolation shared access mode.

Ray clusters are currently not supported on serverless compute. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Installation

With [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) 15.0 and later, Ray is preinstalled on Databricks clusters. For runtimes prior to 15.0, install Ray using pip:

```
%pip install ray[default]>=2.3.0
```

^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Creating a Ray Cluster

Ray clusters are created using the `ray.util.spark.setup_ray_cluster` API from within a Databricks notebook that is attached to an all-purpose cluster. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### User-Specific (Fixed-Size) Cluster

A user-specific Ray cluster is available only to the current notebook user. It is automatically shut down after the notebook is detached from the cluster or after 30 minutes of inactivity (no tasks submitted to Ray). ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
import ray
from ray.util.spark import setup_ray_cluster, shutdown_ray_cluster

setup_ray_cluster(
    max_worker_nodes=1,
    collect_log_to_path="/dbfs/path/to/ray_collected_logs"
)

ray.init(ignore_reinit_error=True)
```

### Auto-Scaling Ray Cluster

For auto-scaling behavior, refer to the dedicated documentation on scaling Ray clusters on Databricks. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Global Mode Ray Cluster

Starting with Ray 2.9.0, you can create a **global mode** Ray cluster that all users attached to the Databricks compute resource can use. This is done via the `setup_global_ray_cluster` API. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
from ray.util.spark import setup_global_ray_cluster

setup_global_ray_cluster(
    max_worker_nodes=2,
    ...
)
```

Global mode clusters have the following properties:

- Only one active global mode Ray cluster can exist per Databricks cluster at a time.
- The global mode cluster is accessible to all users in any attached notebook (via `ray.init()`).
- It remains active until the `setup_ray_cluster` call is interrupted; there is no automatic shutdown timeout. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### GPU Ray Cluster

To include GPUs in the Ray cluster, specify GPU counts for head and worker nodes:

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

## Connecting to a Ray Cluster

### Ray Client

From the same notebook that created the cluster, simply call `ray.init()`. To obtain a remote connection string for external access, use the return value from `setup_ray_cluster`:

```python
from ray.util.spark import setup_ray_cluster

_, remote_conn_str = setup_ray_cluster(num_worker_nodes=2, ...)
ray.init(remote_conn_str)
```

Note that the Ray client does not support the Ray dataset API (`ray.data`) directly. As a workaround, wrap dataset API calls inside a remote Ray task. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Ray Job CLI

The Ray Job CLI can be connected to a Ray cluster on Databricks via the driver proxy. Provide the Databricks workspace URL and the proxy path found in the Ray Dashboard proxy URL. The typical command is:

```shell
ray job submit \
  --headers '{"cookie" : "DATAPLANE_DOMAIN_SESSIONID=<REDACTED>"}' \
  --address 'https://<DATABRICKS WORKSPACE URL>/driver-proxy/o/<etc>' \
  --working-dir='.' \
  -- python run_task.py
```

Databricks recommends using existing tooling ([Lakeflow Jobs](/concepts/lakeflow-jobs.md), Databricks Asset Bundles, or Workflow Triggers) rather than the Ray Job CLI for job submission. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Logging

Set the `collect_log_to_path` argument in `setup_ray_cluster` to specify a destination for Ray cluster logs. Log collection runs after the Ray cluster is shut down. Databricks recommends using a path starting with `/dbfs/` or a Unity Catalog Volume path to preserve logs beyond cluster termination. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Monitoring

After creating a Ray cluster, the Ray Dashboard can be opened from the notebook interface. To enable stack traces and flame graphs for active Ray actors on the Actors page, install `py-spy` before starting the cluster:

```bash
%pip install py-spy
```

^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Best Practices

### Non-GPU Workloads

When using both Spark and Ray on the same cluster, set `spark.task.resource.gpu.amount` to `0` in the Spark configuration. This ensures that Spark DataFrame and UDF executions do not use GPU resources, increasing parallelism for Spark jobs and avoiding contention with Ray GPU workloads. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Disable `transformers` Trainer MLflow Integration in Ray Tasks

If you use the `transformers` library’s trainer inside Ray tasks, set the environment variable `DISABLE_MLFLOW_INTEGRATION` to `'TRUE'` in the Databricks cluster configuration before starting the cluster. This prevents credential-related failures when the transformers trainer attempts [MLflow Autologging](/concepts/mlflow-autologging.md). Direct use of MLflow itself is unaffected. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Address Ray Remote Function Pickling Errors

Ray pickles task functions before execution. To avoid pickling failures, move import statements inside the function declaration. For example, `datasets.load_dataset` is patched in the Databricks Runtime driver and may cause unpickling errors if imported at the module level. Instead, import it inside the task function:

```python
def ray_task_func():
    from datasets import load_dataset
    ...
```

^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Disable Ray Memory Monitor if OOM Errors Occur

In Ray 2.9.3, the Ray memory monitor has known issues that can cause Ray tasks to be killed inadvertently. To disable it, set the environment variable `RAY_memory_monitor_refresh_ms` to `0` in the Databricks cluster configuration. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Batch Data Processing

For batch processing, use the Ray Data API with `map_batches`. Convert any Spark DataFrame to a Ray Dataset using `ray.data.from_spark`. Write processed results back to Databricks Unity Catalog tables using `ray.data.write_databricks_table`. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Using MLflow in Ray Tune, Ray Train, or Custom Ray Tasks

Integrating [MLflow](/concepts/mlflow.md) with Ray requires Ray 2.41 and above. Set the environment variables `DATABRICKS_HOST` and `DATABRICKS_TOKEN` (or `DATABRICKS_CLIENT_ID` and `DATABRICKS_CLIENT_SECRET`) before calling `setup_ray_cluster`. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Notebook-Scoped Python Libraries in Ray Tasks

Using notebook-scoped or cluster Python libraries inside remote Ray tasks requires Ray 2.12 and above. For Ray 2.11 and below, pre-install dependencies with `%pip` before starting the Ray cluster. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- Apache Spark on Databricks
- Ray for Distributed Training
- GPU Compute on Databricks
- MLflow Integration
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)

## Sources

- create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md

# Citations

1. [create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md](/references/create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws-68773ede.md)
