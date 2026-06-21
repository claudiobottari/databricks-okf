---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b34fac84ce76ba66d20c5fc6dc713c41761f850ede87689e1fa3b4aa3e693b76
  pageDirectory: concepts
  sources:
    - create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-gpu-cluster-configuration
    - RGCC
    - Cluster Configuration
    - Cluster configuration
    - GPU Cluster Configuration
    - Ray Cluster Configuration
    - ray-gpu-cluster-configuration-on-databricks
    - RGCCOD
  citations:
    - file: create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
title: Ray GPU Cluster Configuration
description: Configuring Ray clusters on Databricks to leverage GPU resources by specifying num_gpus_per_node and num_gpus_head_node parameters
tags:
  - ray
  - gpu
  - databricks
timestamp: "2026-06-19T17:58:04.320Z"
---

---
title: Ray GPU Cluster Configuration
summary: Configuring Ray clusters on Databricks with GPU resources, including min/max worker nodes, CPU per node, and GPU per node parameters
sources:
  - create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
kind: concept
createdAt: "2026-06-20T10:00:00.000Z"
updatedAt: "2026-06-20T10:00:00.000Z"
tags:
  - ray
  - gpu
  - databricks
  - distributed-computing
aliases:
  - ray-gpu-cluster-configuration
  - RGCC
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Ray GPU Cluster Configuration

**Ray GPU Cluster Configuration** refers to the process of provisioning and configuring Ray clusters on Databricks that utilize GPU resources for distributed machine learning workloads. When creating a Ray cluster on Databricks, you can specify GPU allocation for both head and worker nodes to enable GPU‑accelerated tasks such as model training, inference, and data processing.

## Requirements

To create a Ray GPU cluster, you must have access to a Databricks all‑purpose compute resource with the following settings:

- **Databricks Runtime**: 12.2 LTS ML and above. Ray is preinstalled on Databricks Runtime ML 15.0 and later. For earlier runtimes, install Ray using `%pip install ray[default]>=2.3.0`.
- **Access mode**: Dedicated (formerly single user) or no isolation shared access modes. Ray clusters are not supported on serverless compute. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Creating a Ray GPU Cluster

Use the `ray.util.spark.setup_ray_cluster` API and specify the `num_gpus_per_node` and `num_gpus_head_node` parameters to allocate GPUs to the Ray cluster: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

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

### Fixed-Size vs. Auto-Scaling Clusters

Ray GPU clusters can be fixed‑size (set `min_worker_nodes` equal to `max_worker_nodes`) or auto‑scaling (set a range of minimum and maximum worker nodes). For details on auto‑scaling, see [Scale Ray clusters on Databricks](/concepts/ray-cluster-on-databricks.md). ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Global Mode Ray GPU Clusters

With Ray 2.9.0 and above, you can create a *global mode* Ray cluster that multiple users attached to the same Databricks compute resource can share: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
from ray.util.spark import setup_global_ray_cluster

setup_global_ray_cluster(
    max_worker_nodes=2,
    num_gpus_per_node=1,
    # other arguments same as setup_ray_cluster
)
```

Global mode clusters have these properties: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

- Only one active global mode Ray cluster per Databricks cluster at a time.
- All users in any attached notebook can connect using `ray.init()`.
- The cluster runs until the `setup_global_ray_cluster` call is interrupted — there is no automatic shutdown timeout like single‑user Ray clusters.

## Best Practices for GPU Workloads

### Prevent Spark from Using GPU Resources

When mixed workloads use Spark for data preprocessing and Ray for GPU‑accelerated ML tasks, set the Spark cluster configuration `spark.task.resource.gpu.amount` to `0`. This prevents Spark DataFrame transformations and UDFs from consuming GPU resources, which: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

- Increases Apache Spark job parallelism because GPU instance types typically have many more CPU cores than GPU devices.
- Prevents Spark jobs from competing for GPU resources with concurrently running Ray workloads in multi‑user clusters.

### Disable Transformers Trainer MLflow Integration

If you use Ray Train to fine‑tune a `transformers` model, the `transformers` library’s built‑in MLflow integration (enabled by default) can cause Ray tasks to fail due to credential issues. To avoid this, set the `DISABLE_MLFLOW_INTEGRATION` environment variable to `'TRUE'` in the Databricks cluster configuration when starting your Spark cluster. This issue does not apply if you directly use [MLflow](/concepts/mlflow.md) for logging. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Disable Ray Memory Monitor for OOM Issues

In Ray 2.9.3 the Ray memory monitor has known issues that can cause GPU tasks to be inadvertently killed. To address this, set the environment variable `RAY_memory_monitor_refresh_ms` to `0` in the Databricks cluster configuration. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Address Ray Remote Function Pickling Errors

Ray pickles task functions for distributed execution. If pickling fails, common causes include external references, closures, and references to stateful objects. One common fix is to move import statements inside the task function declaration: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
def ray_gpu_task_func():
    from datasets import load_dataset  # import inside the function
    # GPU‑accelerated task logic here
    ...
```

### Using MLflow with Ray GPU Clusters

Integrating Databricks MLflow with Ray requires Ray 2.41 and above. To use MLflow with Ray Tune, Ray Train, or custom Ray tasks, set the following environment variables *before* calling `setup_ray_cluster`: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
import os
from ray.util.spark import setup_ray_cluster

os.environ["DATABRICKS_HOST"] = "https://....databricks.com"
os.environ["DATABRICKS_TOKEN"] = "<your PAT token>"
# OR use OAuth:
# os.environ["DATABRICKS_HOST"] = "https://....databricks.com"
# os.environ["DATABRICKS_CLIENT_ID"] = "<client id>"
# os.environ["DATABRICKS_CLIENT_SECRET"] = "<client secret>"

setup_ray_cluster(
    num_cpus_worker_node=2,
    num_gpus_worker_node=0,
    max_worker_nodes=1,
    min_worker_nodes=1
)
```

## Logging and Monitoring

Set the `collect_log_to_path` argument when creating the Ray cluster to collect logs after shutdown. Databricks recommends using a path starting with `/dbfs/` or a Unity Catalog Volume path to preserve logs after cluster termination; local storage is deleted when the cluster shuts down. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

To view stack traces and flame graphs for active Ray actors on the Ray Dashboard Actors page, install `py-spy` before starting the Ray cluster. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

After creating a Ray cluster, you can run Ray application code directly in your notebook. Click **Open Ray Cluster Dashboard in a new tab** to view the Ray dashboard. To use the Ray Job CLI, connect through the driver proxy with the appropriate `DATAPLANE_DOMAIN_SESSIONID` cookie and the proxy URL displayed after the cluster starts. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Ray Cluster Scaling](/concepts/ray-cluster-scaling-best-practices.md) — Auto‑scaling Ray clusters on Databricks
- [Ray on Databricks Overview](/concepts/ray-on-databricks-overview.md) — General concepts for running Ray on Databricks
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — Pre‑built runtime with GPU support and Ray preinstalled
- GPU Compute on Databricks — Configuring GPU compute resources in Databricks
- Unity Catalog Volumes — Persistent storage for Ray logs and data
- MLflow Integration with Ray — Using MLflow tracking in Ray tasks

## Sources

- create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md

# Citations

1. [create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md](/references/create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws-68773ede.md)
