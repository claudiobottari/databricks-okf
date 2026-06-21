---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3140b84dddbc0f7489fb53325d089e8dd980899ec3638007ca07d2bb8ce63436
  pageDirectory: concepts
  sources:
    - create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - troubleshooting-ray-on-databricks
    - TROD
  citations:
    - file: create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
    - file: create-and-configure-best-practices -> Address Ray remote function pickling error
title: Troubleshooting Ray on Databricks
description: Common issues and solutions when running Ray on Databricks, including pickling errors, OOM memory monitor bugs, transformers MLflow integration conflicts, and library scoping limitations.
tags:
  - ray
  - databricks
  - troubleshooting
timestamp: "2026-06-18T11:16:57.854Z"
---

# Troubleshooting Ray on Databricks

This page covers common issues encountered when running Ray clusters on Databricks, along with their causes and solutions. It draws on best practices and workarounds documented in the official create-and-connect guide.

## Prerequisites

- Ray clusters require a Databricks all-purpose compute resource with **Databricks Runtime 12.2 LTS ML or above** and **Dedicated (formerly single user) or No Isolation Shared** access mode. Serverless compute is not supported.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Common Issues and Solutions

### Ray tasks fail with pickling errors

Ray pickles task functions before distributing them. Pickling can fail due to external references, closures, or references to stateful objects. For example, `datasets.load_dataset` is patched on the Databricks driver side and becomes unpicklable. ^[create-and-configure-best-practices -> Address Ray remote function pickling error]

**Solution:** Move import statements inside the task function declaration:

```python
def ray_task_func():
    from datasets import load_dataset  # import inside the function
    ...
```

^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Ray tasks fail with credential errors when using `transformers` trainer with MLflow

The `transformers` trainer has MLflow integration enabled by default. When Ray Train is used to fine-tune a `transformers` model, Ray tasks may fail due to credential issues. This does not occur when using MLflow directly for training. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

**Solution:** Set the environment variable `DISABLE_MLFLOW_INTEGRATION` to `'TRUE'` in the Databricks cluster configuration before starting the Spark cluster. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Ray tasks unexpectedly killed with out-of-memory (OOM) errors

In Ray 2.9.3, the Ray memory monitor has known issues that can cause Ray tasks to be inadvertently stopped. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

**Solution:** Disable the Ray memory monitor by setting the environment variable `RAY_memory_monitor_refresh_ms` to `0` in the Databricks cluster configuration before starting the Spark cluster. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### MLflow integration not working in Ray Tune, Ray Train, or custom Ray tasks

To use MLflow with Ray Tune, Ray Train, or custom Ray tasks, the required environment variables must be set **before** calling `setup_ray_cluster`. This requires Ray 2.4.1 or above. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

**Solution:** Set either `DATABRICKS_HOST` and `DATABRICKS_TOKEN`, or `DATABRICKS_HOST`, `DATABRICKS_CLIENT_ID`, and `DATABRICKS_CLIENT_SECRET` in your notebook before starting the Ray cluster:

```python
import os
from ray.util.spark import setup_ray_cluster

os.environ["DATABRICKS_HOST"] = "https://....databricks.com"
os.environ["DATABRICKS_TOKEN"] = "<your PAT token>"
setup_ray_cluster(...)
```

^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Notebook-scoped or cluster Python libraries not available in Ray tasks

For Ray versions 2.11 and below, Ray tasks cannot access notebook-scoped or cluster-installed Python libraries. This is a known limitation. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

**Solution:** Use Ray 2.12 or above for full support. For versions 2.11 and below, pre-install dependencies using `%pip` magic commands **before** starting the Ray cluster. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Ray dashboard stack traces and flame graphs not visible

The Actors page in the Ray Dashboard requires `py-spy` to display stack traces and flame graphs for active Ray actors. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

**Solution:** Install `py-spy` **before** starting the Ray cluster. Use `%pip install py-spy` in your notebook or install it on the cluster. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Ray cluster logs lost after Spark cluster termination

If a log output location is not specified, Ray logs are stored only on local cluster storage and are irrecoverable once the cluster terminates. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

**Solution:** Set the `collect_log_to_path` argument when calling `setup_ray_cluster` or `setup_global_ray_cluster`. Use a path starting with `/dbfs/` or a Unity Catalog Volume path to persist logs. Log collection runs automatically after the Ray cluster shuts down. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
setup_ray_cluster(
    ...,
    collect_log_to_path="/dbfs/path/to/ray_collected_logs"
)
```

### Ray Job CLI connection failures

When using the Ray Job CLI to submit jobs to a Ray cluster on Databricks, the connection requires authentication via a driver proxy URL and session cookie. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

**Solution:** Construct the command as follows:

```shell
ray job submit \
  --headers '{"cookie" : "DATAPLANE_DOMAIN_SESSIONID=<REDACTED>"}' \
  --address 'https://<WORKSPACE_URL>/driver-proxy/o/<etc>' \
  --working-dir='.' \
  -- python run_task.py
```

Replace `<WORKSPACE_URL>` with your Databricks workspace URL and `/driver-proxy/o/<etc>` with the value shown in the Ray Dashboard proxy URL displayed after the Ray cluster starts. Databricks recommends using [Lakeflow Jobs](/concepts/lakeflow-jobs.md), Databricks Asset Bundles, or workflow triggers instead of the Ray Job CLI for deploying jobs. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Single-user Ray cluster shuts down unexpectedly

A single-user (non-global) Ray cluster automatically shuts down after the notebook is detached from the Databricks cluster or after 30 minutes of inactivity (no Ray tasks submitted). ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

**Solution:** Use `setup_global_ray_cluster` to create a persistent Ray cluster that remains active until explicitly interrupted. Note that global clusters do not have an automatic inactivity timeout. They are available to all users attached to the Databricks compute resource. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Best Practices

- **Non-GPU workloads:** Set `spark.task.resource.gpu.amount` to `0` in the Spark configuration to prevent Spark jobs from using GPU resources, increasing parallelism and avoiding contention with Ray GPU workloads. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]
- **Batch processing:** Use the Ray Data API with `map_batches` for efficient batch transformations. Convert Spark DataFrames to Ray Datasets with `ray.data.from_spark` and write results to Databricks UC tables using `ray.data.write_databricks_table`. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]
- **Global mode limitations:** Only one active global-mode Ray cluster can exist per Databricks cluster at a time. Resource contention is possible because all users share the same Ray cluster. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Ray on Databricks](/concepts/ray-on-databricks.md) — Overview of Ray integration
- [Scale Ray clusters on Databricks](/concepts/ray-cluster-on-databricks.md) — Auto-scaling configuration
- MLflow integration with Ray — Using MLflow in Ray workloads
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — Machine learning runtime versions
- Unity Catalog Volumes — Persistent storage for logs and data

## Sources

- create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md

# Citations

1. [create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md](/references/create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws-68773ede.md)
2. create-and-configure-best-practices -> Address Ray remote function pickling error
