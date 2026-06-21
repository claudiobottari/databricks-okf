---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ecb62e9ef04d7d253751a77015aa317fd8537098d8de4b15ac1678ef184336bb
  pageDirectory: concepts
  sources:
    - choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracking-uri
    - MTU
    - MLflow Tracing Guide
    - MLflow Tracking Service
    - MLflow Tracking UI
    - MLflow tracking service
    - Tracking URI
    - tracking URI
  citations:
    - file: choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
title: MLflow tracking URI
description: A configuration parameter that specifies which tracking server MLflow should log experiment data to, set via mlflow.set_tracking_uri() with a URI like 'databricks://remote-workspace-url'.
tags:
  - mlflow
  - configuration
  - networking
timestamp: "2026-06-18T14:35:30.968Z"
---

# MLflow Tracking URI

The **MLflow tracking URI** tells the MLflow client where to store and retrieve experiment metadata, parameters, metrics, artifacts, and model information. It acts as the connection endpoint that directs all tracking operations — such as creating runs, logging parameters, and recording metrics — to a specific [MLflow tracking server](/concepts/remote-mlflow-tracking-server.md). The tracking URI can point to a local file system, a remote server, or a Databricks-hosted managed tracking server. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Default Databricks-Hosted Tracking Server

By default, Databricks provides a managed MLflow tracking server that requires no additional setup. It stores experiment data directly in the workspace and integrates seamlessly with Databricks notebooks and clusters. When running code inside a Databricks notebook, the tracking URI is automatically configured to point to this workspace-based server, so users typically do not need to set it explicitly. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Setting the Active Experiment

Even with the tracking URI configured, users must select an active experiment to determine which experiment each run is logged to. If no experiment is explicitly set, runs are logged to the notebook experiment (the experiment that is automatically associated with the notebook's source file). ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

The active experiment can be controlled using:

- `mlflow.set_experiment()`
- `mlflow.start_run()`
- Environment variables

For example, to log all subsequent runs under a specific experiment:

```python
import mlflow
mlflow.set_experiment("/Shared/my-experiment")
```

^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Remote Tracking to an External Server

There are scenarios where you need to log experiments to a remote MLflow tracking server — for instance, when developing locally and tracking against a Databricks-hosted server, or when centralizing experiment data across multiple workspaces. In such cases you must configure both the tracking URI and the experiment path. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

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

^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

### Authentication Methods

Connecting to a remote tracking server requires proper authentication. MLflow supports two primary approaches on Databricks: Personal Access Tokens (PAT) and OAuth using service principals.

**Personal Access Token (PAT)** – Simple token-based authentication. Suitable for development but requires manual token management and is tied to the user who generated the token.

```python
import os
os.environ["DATABRICKS_TOKEN"] = "your-personal-access-token"
mlflow.set_tracking_uri("databricks://remote-workspace-url")
mlflow.set_experiment("/Shared/remote-experiment")
```

^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

**OAuth (service principal)** – Enables token-based authentication using a service principal identity. This method is better suited for production automation because it avoids user-specific tokens and can be rotated programmatically.

_Note: The source material provides high-level pros and cons for PAT and mentions OAuth as an alternative, but does not include an OAuth code example._ ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Related Concepts

- [MLflow tracking server](/concepts/remote-mlflow-tracking-server.md) – The backend service that stores experiment metadata.
- [MLflow Experiment](/concepts/mlflow-experiment.md) – The logical container for runs.
- [MLflow Run](/concepts/mlflow-run.md) – A single execution of a model training script.
- [Personal Access Token (PAT)](/concepts/databricks-personal-access-token-pat-authentication.md) – Authentication method for remote tracking.
- OAuth with service principal – Production-ready authentication alternative.
- [Environment variables](/concepts/model-serving-environment-variables.md) – Alternative way to set the tracking URI (e.g., `MLFLOW_TRACKING_URI`).

## Sources

- choose-where-your-mlflow-data-is-stored-databricks-on-aws.md

# Citations

1. [choose-where-your-mlflow-data-is-stored-databricks-on-aws.md](/references/choose-where-your-mlflow-data-is-stored-databricks-on-aws-1fe2cb47.md)
