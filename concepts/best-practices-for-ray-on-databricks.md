---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dabf6711e8ab3de13bcd998a1ca30fd6275a5085d541d1039844a06397c8885f
  pageDirectory: concepts
  sources:
    - create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - best-practices-for-ray-on-databricks
    - BPFROD
  citations:
    - file: create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
title: Best Practices for Ray on Databricks
description: Collection of optimization and troubleshooting guidance including GPU allocation, pickling errors, OOM errors, transformers MLflow integration, and batch data processing
tags:
  - ray
  - databricks
  - best-practices
  - troubleshooting
timestamp: "2026-06-19T17:58:12.166Z"
---

---
title: Best Practices for Ray on Databricks
summary: Collection of recommended practices including GPU allocation, MLflow integration, pickling, OOM handling, and batch processing
sources:
  - create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T09:31:17.568Z"
updatedAt: "2026-06-19T09:31:17.568Z"
tags:
  - ray
  - databricks
  - best-practices
aliases:
  - best-practices-for-ray-on-databricks
  - BPFROD
confidence: 0.9
provenanceState: merged
inferredParagraphs: 3
---

# Best Practices for Ray on Databricks

This page collects best practices for creating, configuring, and running Ray clusters on Databricks in production and development environments. The guidance is based on Databricks' own recommendations and covers infrastructure setup, GPU management, MLflow integration, error handling, and data processing patterns.

## General Configuration

### Log Output Location

Set the `collect_log_to_path` argument when calling `setup_ray_cluster()` to specify a destination for Ray cluster logs. Databricks recommends using a path starting with `/dbfs/` or a Unity Catalog Volume path so that logs survive after the Apache Spark cluster is terminated. Local storage on the cluster is deleted when the cluster shuts down, making logs unrecoverable without a persistent path. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Non‑GPU Workloads

Ray clusters run on top of a Databricks Spark cluster. When using Spark for simple data preprocessing and Ray for GPU‑intensive machine learning tasks, set the Spark cluster‑level configuration parameter `spark.task.resource.gpu.amount` to `0`. This prevents Apache Spark DataFrame transformations and UDF executions from consuming GPU resources, increasing Spark job parallelism and avoiding contention with concurrently running Ray workloads. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Disable Transformers Trainer MLflow Integration in Ray Tasks

The `transformers` library enables MLflow integration by default in its trainer. If you use [Ray Train](/concepts/ray-train-resource-allocation.md) to fine‑tune a transformers model, Ray tasks will fail due to a credential issue. To avoid this, set the environment variable `DISABLE_MLFLOW_INTEGRATION` to `'TRUE'` in the Databricks cluster configuration before starting the Spark cluster. This problem does not occur when you use MLflow directly for training. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Address Ray Remote Function Pickling Errors

Ray pickles task functions before execution. If pickling fails, diagnose whether the cause is an external reference, a closure, or a reference to a stateful object. A common fix is to move import statements inside the task function body. For example, `datasets.load_dataset` is patched on the Databricks Runtime driver side, making it unpicklable as a global reference. Moving the import into the function resolves the issue: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
def ray_task_func():
    from datasets import load_dataset  # import inside the function
    ...
```

### Disable Ray Memory Monitor if OOM Kills Occur

In Ray 2.9.3, the Ray memory monitor has known issues that can cause Ray tasks to be inadvertently stopped even when sufficient memory is available. To work around this, disable the memory monitor by setting the environment variable `RAY_memory_monitor_refresh_ms` to `0` in the Databricks cluster configuration before starting the Spark cluster. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Data Processing

### Applying Transformation Functions to Batches of Data

For batch processing, use the Ray Data API with the `map_batches` function. This approach is more efficient and scalable for large datasets or complex computations. Convert any Spark DataFrame to a Ray Dataset using `ray.data.from_spark`, and write processed output to Databricks Unity Catalog tables with `ray.data.write_databricks_table`. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## MLflow Integration

### Using MLflow in Ray Tuner, Ray Train, or Custom Ray Tasks

Integrating [MLflow](/concepts/mlflow.md) with Ray requires Ray 2.41 and above. Set the environment variables `DATABRICKS_HOST` and `DATABRICKS_TOKEN` (or `DATABRICKS_CLIENT_ID` and `DATABRICKS_CLIENT_SECRET` for service principals) before calling `ray.util.spark.setup_ray_cluster`. This ensures that Ray actors can authenticate with the Databricks workspace and log metrics, parameters, and artifacts. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
import os
from ray.util.spark import setup_ray_cluster

os.environ["DATABRICKS_HOST"] = "https://....databricks.com"
os.environ["DATABRICKS_TOKEN"] = "<your PAT token>"
setup_ray_cluster(num_cpus_worker_node=2, num_gpus_worker_node=0,
                  max_worker_nodes=1, min_worker_nodes=1)
```

### Using Notebook‑Scoped or Cluster Python Libraries in Ray Tasks

Ray 2.12 and above support notebook‑scoped Python libraries and cluster libraries in remote Ray tasks. In Ray 2.11 and below, this is a known issue — additional dependencies must be pre‑installed using `%pip` before starting the Ray cluster. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Monitoring and Diagnostics

### Enable Stack Traces and Flame Graphs on the Ray Dashboard Actors Page

To view stack traces and flame graphs for active Ray actors on the Ray Dashboard, install `py-spy` before starting the Ray cluster. This can be done via `%pip install py-spy` in a notebook cell before calling `setup_ray_cluster()`. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Deployment

### Use Databricks Jobs Instead of Ray Job CLI

While the Ray Job CLI can be connected to a Ray cluster running on Databricks (using the driver proxy URL and a session cookie), Databricks recommends deploying Ray jobs using [Lakeflow Jobs](/concepts/lakeflow-jobs.md), creating a Ray cluster per application, and using Databricks Asset Bundles or workflow triggers to orchestrate execution. This aligns with existing Databricks tooling and avoids external dependencies on the Ray CLI. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Related Concepts

- Ray Data API — For batch transformations (`map_batches`, `from_spark`, `write_databricks_table`).
- Ray Train and Ray Tune — Distributed training and hyperparameter tuning on Ray.
- GPU Scheduling on Databricks — Configuring GPU resources for mixed Spark/Ray workloads.
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Logging experiments from Ray tasks.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The runtime that includes Ray pre‑installed from version 15.0 onward.

## Sources

- create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md

# Citations

1. [create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md](/references/create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws-68773ede.md)
