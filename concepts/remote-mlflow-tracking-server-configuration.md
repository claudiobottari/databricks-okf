---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 208235e9f4c01c24961f151f4a1ac447da6c4f612b0a2bfd3af1182f0c6360f8
  pageDirectory: concepts
  sources:
    - choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - remote-mlflow-tracking-server-configuration
    - RMTSC
  citations:
    - file: choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
title: Remote MLflow Tracking Server Configuration
description: Process of setting up MLflow to log experiments to a remote tracking server by configuring both the tracking URI and experiment path.
tags:
  - mlflow
  - remote-tracking
  - configuration
timestamp: "2026-06-19T14:11:56.038Z"
---

Here is the wiki page for **Remote MLflow Tracking Server Configuration** based solely on the source material provided.

---

# Remote MLflow Tracking Server Configuration

**Remote MLflow Tracking Server Configuration** refers to the process of setting up a connection between an MLflow client and an externally hosted MLflow tracking server — for example, when developing locally and wanting to log runs to a Databricks workspace or to a tracking server in a different workspace. This configuration centralizes experiment data, runs, and models across different environments. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Overview

By default, Databricks provides a managed MLflow tracking server that requires no additional setup. It stores experiment data in the workspace and integrates seamlessly with Databricks notebooks and clusters. However, there are common scenarios where you may need to log runs to a remote server:

- Developing locally while tracking runs against the Databricks hosted server
- Tracking runs to a tracking server located in a different workspace
- Centralizing experiment data across multiple environments

In these cases, you must configure both the tracking URI and the experiment path to point to the remote server. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Setting the Active Experiment

Before tracking runs to a remote server, you control where runs are logged by setting the active experiment. This can be done using:

- `mlflow.set_experiment()`
- `mlflow.start_run()`
- Environment variables

For example: ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

```python
import mlflow
mlflow.set_experiment("/Shared/my-experiment")
```

If no experiment is explicitly set, runs are logged to the notebook experiment. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Configuring Remote Tracking

To log experiments to a remote MLflow tracking server, you must configure two things:

1. **Tracking URI** – the address of the remote server
2. **Experiment path** – the location in the remote workspace where runs will be recorded

Both must be set before starting a run. The following example demonstrates logging to a remote Databricks workspace: ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

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

After configuration, all subsequent runs are logged to the specified remote experiment. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Authentication Methods

Remote tracking server connections require proper authentication. MLflow supports two main methods. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

### Personal Access Tokens (PAT)

PATs provide simple token-based authentication. They are easy to set up for development but are user-specific and require manual token management. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

```python
import os

# Set authentication token
os.environ["DATABRICKS_TOKEN"] = "your-personal-access-token"

# Configure remote tracking
mlflow.set_tracking_uri("databricks://remote-workspace-url")
mlflow.set_experiment("/Shared/remote-experiment")
```

### OAuth with Service Principals

OAuth authentication using a service principal is more suitable for production or automated workflows. The source material does not provide code examples for this method. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Related Concepts

- [Databricks-hosted tracking server](/concepts/databricks-hosted-mlflow-tracking-server.md) – the default managed server for Databricks workspaces
- [MLflow experiments](/concepts/mlflow-experiment.md) – the organizational unit for runs and models
- [Personal Access Tokens](/concepts/databricks-personal-access-token-pat-authentication.md) – token-based authentication for Databricks APIs
- OAuth with service principals – identity-based authentication for automated workflows
- [MLflow tracking URI](/concepts/mlflow-tracking-uri.md) – the address used to connect to a tracking server

## Sources

- choose-where-your-mlflow-data-is-stored-databricks-on-aws.md

# Citations

1. [choose-where-your-mlflow-data-is-stored-databricks-on-aws.md](/references/choose-where-your-mlflow-data-is-stored-databricks-on-aws-1fe2cb47.md)
