---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2ff0f5b8929ab818ebe0a94203c820b83285f2447cd41266f8d0704bbc91b90c
  pageDirectory: concepts
  sources:
    - create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-on-databricks-best-practices
    - RODBP
  citations:
    - file: create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
title: Ray on Databricks Best Practices
description: Collection of best practices for running Ray on Databricks including GPU allocation, transformers trainer MLflow integration, pickling errors, memory monitor, batch processing, and library scoping
tags:
  - ray
  - databricks
  - best-practices
timestamp: "2026-06-19T14:32:33.976Z"
---

# Ray on Databricks Best Practices

This page covers recommended practices for creating, configuring, and running Ray clusters on Databricks. Following these guidelines helps avoid common pitfalls, improve resource utilization, and ensure stable operation of Ray-based workloads.

## Overview

Ray clusters on Databricks run on top of an Apache Spark cluster. They can be created from a notebook using the `setup_ray_cluster` API (user-specific) or `setup_global_ray_cluster` API (shared across users). A solid understanding of how the Spark cluster and Ray cluster interact is key to efficient and reliable execution.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## General Configuration Practices

### Preserve logs after cluster termination

Set the `collect_log_to_path` argument to a path starting with `/dbfs/` or a [Unity Catalog](/concepts/unity-catalog.md) volume path. This preserves Ray cluster logs even after the Spark cluster is terminated. Without this setting, logs are lost because local storage is deleted when the cluster shuts down.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Always specify a log output location

Make it a standard practice to provide a `collect_log_to_path` value when calling `setup_ray_cluster`. Log collection runs automatically after the Ray cluster shuts down, so specifying a persistent location ensures you can access logs for debugging later.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Workload-Specific Best Practices

### Non-GPU workloads

When running Spark jobs — such as data preprocessing with Spark UDFs — alongside GPU-intensive Ray tasks, set the Spark cluster-level configuration `spark.task.resource.gpu.amount` to `0`. This prevents Spark executors from consuming GPU resources, which:

- Increases Spark job parallelism, because GPU instances typically have many more CPU cores than GPU devices.
- Avoids competition for GPU resources when the cluster is shared among multiple users.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Using MLflow with Ray

To use [MLflow](/concepts/mlflow.md) within [Ray Tune](/concepts/ray-tune.md), [Ray Train](/concepts/ray-train-resource-allocation.md), or custom Ray tasks, set the environment variables `DATABRICKS_HOST` and `DATABRICKS_TOKEN` (or `DATABRICKS_CLIENT_ID` and `DATABRICKS_CLIENT_SECRET`) **before** calling `setup_ray_cluster`. This integration requires Ray 2.4.1 and above.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
import os
from ray.util.spark import setup_ray_cluster

os.environ["DATABRICKS_HOST"] = "https://your-workspace.databricks.com"
os.environ["DATABRICKS_TOKEN"] = "<your PAT token>"

setup_ray_cluster(num_cpus_worker_node=2, ...)
```

### Disable transformers trainer MLflow integration in Ray tasks

The `transformers` library enables its own MLflow integration by default. When using Ray Train to fine-tune a transformers model, this integration causes Ray tasks to fail due to credential issues. (This does not affect direct MLflow usage.) To avoid the problem, set the environment variable `DISABLE_MLFLOW_INTEGRATION` to `'TRUE'` in the Databricks cluster configuration **before** starting the Spark cluster.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Handling pickling errors in Ray remote functions

Ray pickles task functions for distribution across workers. If pickling fails, common causes include external references, closures, or references to stateful objects. A quick fix for some cases — for example, when using `datasets.load_dataset`, which is patched on the driver side — is to move the import statement **inside** the task function declaration.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
def ray_task_func():
    from datasets import load_dataset  # import inside the function body
    ...
```

### Disable Ray memory monitor if unexpected OOM kills occur

In Ray 2.9.3, the memory monitor has known issues that can cause Ray tasks to be killed without legitimate cause. To work around this, set the environment variable `RAY_memory_monitor_refresh_ms` to `0` in the Databricks cluster configuration before starting the Spark cluster.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Batch transformations with Ray Data

For batch data processing, use the Ray Data API with the `map_batches` function. This approach is more efficient and scalable than per-row processing, especially for large datasets. Convert a Spark DataFrame to a Ray Dataset using `ray.data.from_spark`, and write results to Databricks Unity Catalog tables using `ray.data.write_databricks_table`.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Using Python libraries in Ray tasks

Notebook-scoped or cluster-scoped Python libraries are usable in Ray tasks starting from Ray 2.12. For Ray 2.11 and below, dependencies must be pre-installed using `%pip` **before** starting the Ray cluster, because those versions cannot pick up libraries installed after the cluster is already running.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Remote Ray client usage

When connecting to a Ray cluster using the Ray client (Ray 2.3.0+), note that the Ray Dataset API (`ray.data` module) is **not supported** over the client connection. As a workaround, wrap any code that calls Ray Dataset APIs inside a remote Ray task.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Related Concepts

- Setup Ray Cluster API – The primary method to create Ray clusters on Databricks.
- [Global Ray Cluster](/concepts/global-mode-ray-cluster.md) – A shared Ray cluster accessible by all users attached to the Spark cluster.
- Ray Data API – Efficient batch processing with `map_batches`.
- [MLflow on Databricks](/concepts/mlflow-on-databricks.md) – Tracking experiments from Ray workloads.
- GPU Scheduling – Managing GPU resources between Spark and Ray.
- [Auto-scaling Ray Clusters](/concepts/fixed-size-vs-auto-scaling-ray-clusters.md) – Scaling workers dynamically based on workload.
- [Unity Catalog](/concepts/unity-catalog.md) – For persistent log storage and table output.

## Sources

- create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md

# Citations

1. [create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md](/references/create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws-68773ede.md)
