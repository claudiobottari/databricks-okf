---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9dc99fd7015c29bb9f49be5b76ac5f3b7a6ecb5bab9ec68a6184cecd5b46d11b
  pageDirectory: concepts
  sources:
    - create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-integration-with-ray-on-databricks
    - MIWROD
  citations:
    - file: create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
title: MLflow Integration with Ray on Databricks
description: Using MLflow tracking with Ray Tune, Ray Train, or customized Ray tasks on Databricks by setting authentication environment variables
tags:
  - ray
  - mlflow
  - databricks
  - mlops
timestamp: "2026-06-19T17:58:10.770Z"
---

```yaml
---
title: MLflow Integration with Ray on Databricks
summary: Configuring MLflow authentication and environment variables for use with Ray Tune, Ray Train, and custom Ray tasks on Databricks clusters.
sources:
  - create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:16:48.131Z"
updatedAt: "2026-06-18T11:16:48.131Z"
tags:
  - mlflow
  - ray
  - databricks
aliases:
  - mlflow-integration-with-ray-on-databricks
  - MIWROD
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 1
---

# MLflow Integration with Ray on Databricks

**MLflow Integration with Ray on Databricks** enables experiment tracking and model logging within distributed Ray workloads — specifically [[Ray Tune]], [[Ray Train Resource Allocation|Ray Train]], and custom Ray tasks — while running on Databricks clusters. This integration allows you to use Databricks MLflow for tracking parameters, metrics, and artifacts from Ray-based computations.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Requirements

Integrating Databricks MLflow with Ray requires **Ray 2.41 and above**. Earlier versions do not support the necessary credential passing mechanism for MLflow to authenticate with the Databricks workspace from within Ray worker processes.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Setting Environment Variables

To enable MLflow from within Ray tasks, you must set the appropriate Databricks authentication environment variables **before** calling `ray.util.spark.setup_ray_cluster`. Two authentication methods are supported:^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

- **Personal Access Token (PAT):** Set `DATABRICKS_HOST` and `DATABRICKS_TOKEN`.
- **OAuth (client ID + secret):** Set `DATABRICKS_HOST`, `DATABRICKS_CLIENT_ID`, and `DATABRICKS_CLIENT_SECRET`.

The following example demonstrates the PAT method:^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
import os
from ray.util.spark import setup_ray_cluster

os.environ["DATABRICKS_HOST"] = "https://<workspace-url>.databricks.com"
os.environ["DATABRICKS_TOKEN"] = "<your-pat-token>"

setup_ray_cluster(
    num_cpus_worker_node=2,
    num_gpus_worker_node=0,
    max_worker_nodes=1,
    min_worker_nodes=1
)
```

Once the environment variables are set, you can use MLflow APIs (such as `mlflow.start_run`, `mlflow.log_param`, `mlflow.log_metric`) inside any Ray remote function, [Ray Tune](/concepts/ray-tune.md) trial, [Ray Train](/concepts/ray-train-resource-allocation.md) worker, or custom Ray task without additional authentication steps. The credentials propagate through the Ray cluster to each worker node.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Known Issue: Transformers Trainer MLflow Integration

The Hugging Face Transformers library enables its own MLflow integration by default when used with the `Trainer` API. When you use [Ray Train](/concepts/ray-train-resource-allocation.md) to fine-tune a Transformers model, this automatic integration can cause Ray tasks to fail due to credential issues. The problem does **not** occur when using MLflow directly for training (calling `mlflow.log_*` functions manually rather than relying on the Transformers integration).^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

**Workaround:** Disable the Transformers-built-in MLflow integration by setting the environment variable `DISABLE_MLFLOW_INTEGRATION` to `'TRUE'` in the Databricks cluster configuration *before starting the Apache Spark cluster*. This prevents the credential conflict while still allowing you to use MLflow explicitly in your own code.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Best Practices

- **Set environment variables early.** Always configure `DATABRICKS_HOST` and the chosen authentication method before initializing the Ray cluster with `setup_ray_cluster`. Ray tasks will inherit these variables.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]
- **Prefer OAuth for production.** Use `DATABRICKS_CLIENT_ID` and `DATABRICKS_CLIENT_SECRET` over PAT tokens for better security and lifecycle management.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]
- **Disable Transformers integration when it causes failures.** If you encounter credential errors during Ray Train with Transformers, apply the `DISABLE_MLFLOW_INTEGRATION` workaround described above.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) — Logging parameters, metrics, and artifacts from ML workloads
- [Ray Cluster on Databricks](/concepts/ray-cluster-on-databricks.md) — Creating and managing Ray compute clusters
- Databricks Authentication — Setting up credentials for workspace access
- [Ray Tune](/concepts/ray-tune.md) — Hyperparameter optimization with MLflow integration
- [Ray Train](/concepts/ray-train-resource-allocation.md) — Distributed training with MLflow logging
- Create and connect to Ray clusters — Complete guide for Ray on Databricks

## Sources

- create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md

# Citations

1. [create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md](/references/create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws-68773ede.md)
