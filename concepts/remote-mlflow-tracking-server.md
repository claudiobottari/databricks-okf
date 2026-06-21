---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c37f491566f21a444eb20390aa8b66b4122144f947746f83cca1114e0f43db50
  pageDirectory: concepts
  sources:
    - choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - remote-mlflow-tracking-server
    - RMTS
    - MLflow Tracking Server
    - MLflow Tracking server
    - MLflow tracking server
    - Remote MLflow Tracking
    - MLflow Tracking Service
    - MLflow tracking service
    - Tracking server
  citations:
    - file: choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
title: Remote MLflow tracking server
description: Setting up a connection to a remote MLflow tracking server to log experiments from local development or across different Databricks workspaces.
tags:
  - mlflow
  - tracking
  - remote
  - databricks
timestamp: "2026-06-18T10:56:02.607Z"
---

# Remote MLflow tracking server

A **remote MLflow tracking server** is an MLflow tracking server hosted outside the current Databricks workspace, used to store and manage experiment data, runs, and models from different environments. While Databricks provides a managed, built-in tracking server by default, you may need to connect to a remote server when developing locally and tracking against the Databricks-hosted server, or when you want to track experiments to a server in a different workspace.^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Default Databricks-hosted tracking server

By default, each Databricks workspace includes a managed MLflow tracking server that requires no additional setup or configuration. This server stores experiment data within the workspace and integrates seamlessly with Databricks notebooks and clusters. All MLflow runs are logged to this server using the active experiment; if no experiment is explicitly set, runs are logged to the notebook experiment.^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Scenarios for remote tracking

You may need to set up a connection to a remote MLflow tracking server in the following common scenarios:^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

- Developing code locally and wanting to track experiments against the Databricks-hosted server.
- Tracking experiments to an MLflow tracking server located in a different Databricks workspace.

## Setting up tracking to a remote server

To log experiments to a remote tracking server, you must configure both the **tracking URI** and the **experiment path**. The tracking URI identifies the remote server, and the experiment path specifies where runs should be logged within that server.^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

### Example configuration

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

You can also set the active experiment using `mlflow.set_experiment()`, `mlflow.start_run()`, or environment variables.^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Authentication methods

Remote tracking server connections require proper authentication. Databricks supports two primary methods:^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

### Personal Access Tokens (PAT)

Use PATs for simple token-based authentication. This approach is easy to set up and suitable for development, but it is user-specific and requires manual token management.

```python
import os

# Set authentication token
os.environ["DATABRICKS_TOKEN"] = "your-personal-access-token"

# Configure remote tracking
mlflow.set_tracking_uri("databricks://remote-workspace-url")
mlflow.set_experiment("/Shared/remote-experiment")
```

### OAuth (service principal)

OAuth authentication using a service principal provides a more robust, non-user-specific mechanism suitable for production and automated workflows. The source material does not include a code example for OAuth, but it is listed as an available option.^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Related concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) — The core logging component of MLflow
- [Databricks-hosted MLflow tracking server](/concepts/databricks-hosted-mlflow-tracking-server.md) — the default managed tracking server
- [MLflow Experiments](/concepts/mlflow-experiment.md) — containers for organizing runs
- [Personal Access Tokens](/concepts/databricks-personal-access-token-pat-authentication.md) — token-based authentication for Databricks APIs
- Service Principals — identity for automated tools and applications
- [MLflow tracking URI](/concepts/mlflow-tracking-uri.md) — the URI that specifies which tracking server to use

## Sources

- choose-where-your-mlflow-data-is-stored-databricks-on-aws.md

# Citations

1. [choose-where-your-mlflow-data-is-stored-databricks-on-aws.md](/references/choose-where-your-mlflow-data-is-stored-databricks-on-aws-1fe2cb47.md)
