---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8c26162388d1ce1363449cfb9e24c0724772d9c0830edc198eb6ff5ca8635be1
  pageDirectory: concepts
  sources:
    - choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-active-experiment
    - MAE
    - Active Experiment
    - active experiment
    - Set the active experiment
    - Workspace Experiments
  citations:
    - file: choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
title: MLflow active experiment
description: The mechanism for controlling which experiment MLflow logs runs to, which can be set using mlflow.set_experiment(), mlflow.start_run(), or environment variables.
tags:
  - mlflow
  - experiment-management
  - configuration
timestamp: "2026-06-18T14:35:45.762Z"
---

# MLflow Active Experiment

**MLflow active experiment** refers to the mechanism by which [MLflow](/concepts/mlflow.md) determines where to log run data when no explicit experiment is specified in a run command. It is a key concept for managing experiment organization and ensuring that runs are correctly associated with the intended tracking context.^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Overview

MLflow uses the active experiment as the default destination for all run metadata, including parameters, metrics, artifacts, and models. This allows users to control the experiment scope without needing to pass an experiment ID or name to every individual run invocation.^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Behavior and Defaults

### Default Experiment

If no experiment is explicitly set, MLflow runs are logged to the notebook experiment. This is the default behavior when tracking is used from within a Databricks notebook environment.^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

### Explicit Experiment Setting

Users can override the default experiment selection by setting the active experiment through one of the following methods:

- `mlflow.set_experiment()`
- `mlflow.start_run()`
- Environment variables

Setting an experiment using `mlflow.set_experiment()` establishes the active experiment for all subsequent runs in the current execution context.^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Setting the Active Experiment

To set the active experiment, use `mlflow.set_experiment()` with the experiment path:

```python
import mlflow
mlflow.set_experiment("/Shared/my-experiment")
```

After this call, all subsequent runs within the same execution context will be logged to the specified experiment path.^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

### Remote Tracking Server

When working with a [Remote MLflow tracking server](/concepts/remote-mlflow-tracking-server.md), users must configure both the tracking URI and the experiment path to ensure proper routing of experiment data:

```python
import mlflow

# Set the tracking URI to the remote server
mlflow.set_tracking_uri("databricks://remote-workspace-url")

# Set the experiment path in the remote server
mlflow.set_experiment("/Shared/centralized-experiments/my-project")

# All subsequent runs will be logged to the remote server
with mlflow.start_run():
    mlflow.log_param("model_type", "random_forest")
    mlflow.log_metric("accuracy", 0.95)
```

## Authentication Considerations

Remote tracking server connections require proper authentication. Two common authentication methods are available:

- **Personal Access Tokens (PAT)** — Simple token-based authentication, suitable for development but user-specific and requires manual token management
- **OAuth (service principal)** — More secure for production environments

```python
import os

# Set authentication token
os.environ["DATABRICKS_TOKEN"] = "your-personal-access-token"

# Configure remote tracking
mlflow.set_tracking_uri("databricks://remote-workspace-url")
mlflow.set_experiment("/Shared/remote-experiment")
```

## Related Concepts

- [MLflow Experiment](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs
- [MLflow tracking server](/concepts/remote-mlflow-tracking-server.md) — The service that stores and manages experiment data
- [MLflow runs](/concepts/mlflow-run.md) — Individual executions of machine learning code
- [MLflow run context](/concepts/mlflow-run.md) — The execution environment for a run
- [MLflow tracking URI](/concepts/mlflow-tracking-uri.md) — The URI pointing to the tracking server

## Sources

- choose-where-your-mlflow-data-is-stored-databricks-on-aws.md

# Citations

1. [choose-where-your-mlflow-data-is-stored-databricks-on-aws.md](/references/choose-where-your-mlflow-data-is-stored-databricks-on-aws-1fe2cb47.md)
