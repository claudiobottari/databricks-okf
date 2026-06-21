---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: de5526e69eea818aa1cfd2541444869e6012ef2f2098295f864759244b9dc87b
  pageDirectory: concepts
  sources:
    - choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - tracking-uri-in-mlflow
    - TUIM
    - Tracing in MLflow
  citations:
    - file: choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
title: Tracking URI in MLflow
description: Configuration parameter that specifies the location of the MLflow tracking server, used to direct experiment logging to a specific server instance.
tags:
  - mlflow
  - tracking-uri
  - configuration
timestamp: "2026-06-19T14:11:33.603Z"
---

Here is the wiki page for "Tracking URI in MLflow", written solely from the provided source material.

---

## Tracking URI in MLflow

A **Tracking URI** in [MLflow](/concepts/mlflow.md) specifies the location of the MLflow tracking server where experiment data, runs, and models are logged and stored. Configuring the correct tracking URI allows users to control where MLflow data resides and how to access experiments across different environments. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Default Behavior

By default, Databricks provides a managed MLflow tracking server that requires no additional setup or configuration. This server stores experiment data in the workspace and integrates seamlessly with Databricks notebooks and clusters. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

All MLflow runs are logged to the workspace's tracking server using the active experiment. If no experiment is explicitly set, runs are logged to the notebook-linked experiment. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Setting the Tracking URI

Users may need to set a custom tracking URI to log data to a remote MLflow tracking server. This is common when developing locally and wanting to track against a [Databricks-hosted tracking server](/concepts/databricks-hosted-mlflow-tracking-server.md) or when routing experiments to a server in a different workspace. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

### Using `mlflow.set_tracking_uri()`

The tracking URI is configured programmatically using `mlflow.set_tracking_uri()`. For remote tracking servers, the URI follows the format `databricks://<workspace-url>`. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

```python
import mlflow

# Set the tracking URI to a remote server
mlflow.set_tracking_uri("databricks://remote-workspace-url")

# Set the experiment path in the remote server
mlflow.set_experiment("/Shared/centralized-experiments/my-project")

# All subsequent runs will be logged to the remote server
with mlflow.start_run():
    mlflow.log_param("model_type", "random_forest")
    mlflow.log_metric("accuracy", 0.95)
```

## Authentication

Connecting to a remote tracking server requires proper authentication. Two common methods are supported:

### Personal Access Token (PAT)

PATs provide simple token-based authentication. They are easy to set up and good for development, but are user-specific and require manual token management. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

```python
import os

# Set authentication token
os.environ["DATABRICKS_TOKEN"] = "your-personal-access-token"

# Configure remote tracking
mlflow.set_tracking_uri("databricks://remote-workspace-url")
mlflow.set_experiment("/Shared/remote-experiment")
```

### OAuth (Service Principal)

OAuth using service principals is the alternative authentication method for remote server connections. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Setting the Active Experiment

Alongside the tracking URI, users can control where runs are logged by setting the active experiment using:
- `mlflow.set_experiment()`
- `mlflow.start_run()`
- Environment variables

## Related Concepts

- [MLflow Tracking Server](/concepts/remote-mlflow-tracking-server.md)
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- [Databricks-hosted tracking server](/concepts/databricks-hosted-mlflow-tracking-server.md)
- [Remote MLflow tracking server](/concepts/remote-mlflow-tracking-server.md)
- [Authentication for MLflow](/concepts/mlflow-authentication-methods.md)

## Sources

- choose-where-your-mlflow-data-is-stored-databricks-on-aws.md

# Citations

1. [choose-where-your-mlflow-data-is-stored-databricks-on-aws.md](/references/choose-where-your-mlflow-data-is-stored-databricks-on-aws-1fe2cb47.md)
