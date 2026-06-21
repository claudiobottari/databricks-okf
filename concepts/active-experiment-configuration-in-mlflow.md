---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fc3861b0fbd1601344147b2d32dc4ded46df79e8213e7041cdeeb0483e52fd80
  pageDirectory: concepts
  sources:
    - choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - active-experiment-configuration-in-mlflow
    - AECIM
  citations:
    - file: choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
title: Active experiment configuration in MLflow
description: Methods to control where MLflow runs are logged by setting the active experiment using set_experiment(), start_run(), or environment variables.
tags:
  - mlflow
  - experiment-tracking
  - configuration
timestamp: "2026-06-19T17:42:38.255Z"
---

# Active Experiment Configuration in MLflow

**Active Experiment Configuration in MLflow** refers to the mechanisms for controlling where MLflow runs are logged by setting the active experiment. By default, all MLflow runs are logged to the workspace's tracking server using the active experiment. If no experiment is explicitly set, runs are logged to the notebook experiment. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Overview

MLflow tracking servers store and manage experiment data, runs, and models. Configuring tracking servers allows you to control where MLflow data is stored and how to access experiments across different environments. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Databricks-Hosted Tracking Server

By default, Databricks provides a managed MLflow tracking server that requires no additional setup or configuration, stores experiment data in your workspace, and integrates seamlessly with Databricks notebooks and clusters. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Setting the Active Experiment

Control where runs are logged in Databricks by setting the active experiment using one of the following methods:

- `mlflow.set_experiment()`
- `mlflow.start_run()`
- Environment variables

The following example sets an experiment for all subsequent runs in the execution: ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

```python
import mlflow
mlflow.set_experiment("/Shared/my-experiment")
```

## Remote Tracking Server Configuration

You may need to set up a connection to a remote MLflow tracking server. This could be because you are developing locally and want to track against the Databricks hosted server, or you want to track to a different MLflow tracking server — for example, one in a different workspace. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

### Setting the Tracking URI and Experiment

To log experiments to a remote tracking server, configure both the tracking URI and experiment path: ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

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

### Authentication Methods

Remote tracking server connections require proper authentication. Choose between Personal Access Tokens (PAT) or OAuth using service principals. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

#### PAT Authentication

Use PATs for simple token-based authentication. This approach offers simple setup and is good for development, but is user-specific and requires manual token management. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

```python
import os

# Set authentication token
os.environ["DATABRICKS_TOKEN"] = "your-personal-access-token"

# Configure remote tracking
mlflow.set_tracking_uri("databricks://remote-workspace-url")
mlflow.set_experiment("/Shared/remote-experiment")
```

## Default Behavior

By default, all MLflow runs are logged to the workspace's tracking server using the active experiment. If no experiment is explicitly set, runs are logged to the notebook experiment. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracking Server](/concepts/remote-mlflow-tracking-server.md) — The server that stores and manages experiment data
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs
- MLflow Notebook Experiments — Default experiment for notebook-based runs
- [Remote MLflow Tracking](/concepts/remote-mlflow-tracking-server.md) — Logging experiments to external tracking servers
- [MLflow Authentication](/concepts/mlflow-authentication-methods.md) — Methods for authenticating with remote tracking servers
- [MLflow Runs](/concepts/mlflow-run.md) — Individual executions of MLflow code
- Experiment Tags in MLflow — Metadata stored with experiments for configuration

## Sources

- choose-where-your-mlflow-data-is-stored-databricks-on-aws.md

# Citations

1. [choose-where-your-mlflow-data-is-stored-databricks-on-aws.md](/references/choose-where-your-mlflow-data-is-stored-databricks-on-aws-1fe2cb47.md)
