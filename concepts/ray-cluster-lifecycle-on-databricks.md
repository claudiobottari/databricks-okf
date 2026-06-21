---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 32f82e22b803a2b522a49a680b4221bcc7704b24af87ff66893738d1e18af8b9
  pageDirectory: concepts
  sources:
    - create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-cluster-lifecycle-on-databricks
    - RCLOD
  citations:
    - file: create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
title: Ray cluster lifecycle on Databricks
description: Creating, managing, and shutting down Ray clusters within Databricks compute using the setup_ray_cluster and shutdown_ray_cluster APIs, including auto-shutdown after inactivity
tags:
  - ray
  - databricks
  - cluster-management
timestamp: "2026-06-18T14:49:48.008Z"
---

# Ray cluster lifecycle on Databricks

The **Ray cluster lifecycle on Databricks** encompasses the creation, configuration, usage, and automatic or manual shutdown of Ray compute clusters that run on top of a Databricks all-purpose compute resource. Understanding this lifecycle is essential for managing resources, avoiding unnecessary costs, and ensuring that Ray workloads are executed reliably.

## Requirements

A Ray cluster can be created only on a Databricks all-purpose compute resource that meets the following conditions:

- **Databricks Runtime**: 12.2 LTS ML or above.
- **Access mode**: Dedicated (formerly single user) or no isolation shared.
- **Not supported**: Serverless compute. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Installation

Starting with Databricks Runtime ML 15.0, Ray is preinstalled on Databricks clusters. For runtimes earlier than 15.0, you must install Ray manually using pip:

```python
%pip install ray[default]>=2.3.0
```

^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Creating a Ray cluster

### User-specific (single-user) Ray cluster

Use `ray.util.spark.setup_ray_cluster` to create a Ray cluster that is accessible only to the notebook user who started it. This is the typical approach for development and ad‑hoc workloads. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

**Fixed-size example:**

```python
import ray
from ray.util.spark import setup_ray_cluster, shutdown_ray_cluster

setup_ray_cluster(
    max_worker_nodes=1,
    collect_log_to_path="/dbfs/path/to/ray_collected_logs"
)
ray.init(ignore_reinit_error=True)
```

A fixed-size cluster uses the exact number of worker nodes specified. For auto‑scaling clusters, see [Scale Ray clusters on Databricks](/concepts/ray-cluster-on-databricks.md). ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Global (shared) Ray cluster

Ray 2.9.0 and above support `ray.util.spark.setup_global_ray_cluster`, which creates a Ray cluster that all users attached to the same Databricks compute resource can use. Global clusters **do not** have an automatic inactivity timeout. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
from ray.util.spark import setup_global_ray_cluster

setup_global_ray_cluster(
    max_worker_nodes=2,
    # other arguments same as setup_ray_cluster
)
```

Only one active global Ray cluster can exist per Databricks cluster. The call blocks until interrupted (via the **Interrupt** button, notebook detach, or Databricks cluster termination). ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### GPU clusters

GPU resources can be specified in the `setup_ray_cluster` call:

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

^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Connecting to the Ray cluster

After creating the cluster, call `ray.init()` in the same notebook to connect. For remote connections using the Ray client (Ray 2.3.0+), capture the remote connection string:

```python
_, remote_conn_str = setup_ray_cluster(num_worker_nodes=2, ...)
ray.init(remote_conn_str)
```

The Ray client does **not** support `ray.data` API directly; wrap such calls inside a remote Ray task as a workaround. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

The Ray Job CLI can be connected through the driver proxy, but Databricks recommends using [Lakeflow Jobs](/concepts/lakeflow-jobs.md), Databricks Asset Bundles, or Workflow Triggers instead. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Configuration and best practices

### Log output location

Set `collect_log_to_path` to a path under `/dbfs/` or a Unity Catalog Volume to preserve logs after the Spark cluster terminates. Local storage is deleted upon shutdown. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Non‑GPU workloads

When a Spark cluster with GPU instances is used, set `spark.task.resource.gpu.amount` to `0` so that Spark tasks do not consume GPU resources, leaving them for Ray. This also increases Spark parallelism on CPU cores. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Disable transformers MLflow integration

If using the `transformers` trainer inside Ray tasks, set the environment variable `DISABLE_MLFLOW_INTEGRATION` to `'TRUE'` in the Databricks cluster configuration to avoid credential failures. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Address pickling errors

Move import statements inside the remote task function to avoid pickling issues with Databricks‑patched libraries (e.g., `datasets.load_dataset`). ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Ray memory monitor

In Ray 2.9.3, the memory monitor may incorrectly kill tasks. Set `RAY_memory_monitor_refresh_ms` to `0` to disable it. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Using MLflow with Ray

MLflow integration with Ray Tune, Ray Train, or custom Ray tasks requires Ray 2.41 and above. Set the environment variables `DATABRICKS_HOST` and `DATABRICKS_TOKEN` (or `DATABRICKS_CLIENT_ID` and `DATABRICKS_CLIENT_SECRET`) **before** calling `setup_ray_cluster`. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Notebook‑scoped libraries

Ray 2.12 and above support notebook‑scoped Python libraries and cluster libraries inside Ray tasks. For Ray 2.11 and below, dependencies must be pre‑installed with `%pip` before starting the Ray cluster. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Shutdown and cleanup

### User‑specific Ray clusters

User‑specific Ray clusters are shut down automatically in two scenarios:

1. **Notebook detachment**: when the notebook is detached from the Databricks cluster.
2. **Inactivity timeout**: after 30 minutes with no tasks submitted to Ray.

Manual shutdown is also possible via `shutdown_ray_cluster()`. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Global Ray clusters

Global Ray clusters remain active until one of the following occurs:

- The cell that called `setup_global_ray_cluster` is interrupted.
- The notebook is detached from the Databricks cluster.
- The Databricks cluster is terminated.

There is **no** automatic inactivity timeout for global clusters. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Log collection

If `collect_log_to_path` was set, logs are gathered after the Ray cluster shuts down. Databricks recommends using paths under `/dbfs/` or Unity Catalog Volumes to make logs persistent beyond the Spark cluster lifetime. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Limitations

- Ray clusters are **not** supported on serverless compute.
- Only one global Ray cluster can run at a time on a given Databricks cluster.
- The Ray client (`ray.init(remote_conn_str)`) does not support `ray.data` API directly.
- Auto‑scaling is covered separately (see [Scale Ray clusters on Databricks](/concepts/ray-cluster-on-databricks.md)).

## Related concepts

- Ray (framework)
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- GPU clusters on Databricks
- Ray Dashboard
- [MLflow on Databricks](/concepts/mlflow-on-databricks.md)
- Unity Catalog Volumes
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md)
- Databricks Asset Bundles

## Sources

- create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md

# Citations

1. [create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md](/references/create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws-68773ede.md)
