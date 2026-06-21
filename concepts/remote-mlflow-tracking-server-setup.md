---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c061b15cfdde9cbf9282a5bac3fa02e0d69d309d60f39a68ddd9a14928f92190
  pageDirectory: concepts
  sources:
    - choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - remote-mlflow-tracking-server-setup
    - RMTSS
  citations:
    - file: choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
title: Remote MLflow tracking server setup
description: Configuration required to connect to a remote MLflow tracking server, including setting the tracking URI and experiment path to log experiments across different environments.
tags:
  - mlflow
  - remote-tracking
  - configuration
timestamp: "2026-06-19T17:42:59.364Z"
---

```markdown
## Remote MLflow Tracking Server Setup

**Remote MLflow Tracking Server Setup** refers to the configuration steps required to direct MLflow logging from a local or non-Databricks environment to a remote, hosted MLflow tracking server—such as the managed server provided by a Databricks workspace. This setup is essential for centralizing experiment metadata across distributed teams and development environments.

### Why Configure a Remote Tracking Server

By default, Databricks provides a managed MLflow tracking server that requires no additional setup and stores experiment data directly in the workspace. However, common scenarios demand a remote connection:

- Developing locally and wanting to log runs against the Databricks-hosted server
- Tracking experiments to a different MLflow tracking server, such as one in another workspace
- Centralizing experiment data across multiple environments for team-wide visibility

^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

### Configuration Steps

#### Set the Tracking URI and Experiment

To log experiments to a remote server, you must configure both the tracking URI and the experiment path.

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

#### Authentication Methods

Remote connections require proper authentication. Choose between Personal Access Tokens (PAT) or OAuth using service principals.

**PAT (Personal Access Token)** offers simple setup ideal for development but is user-specific and requires manual token management.

```python
import os

os.environ["DATABRICKS_TOKEN"] = "your-personal-access-token"

mlflow.set_tracking_uri("databricks://remote-workspace-url")
mlflow.set_experiment("/Shared/remote-experiment")
```

^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

### Databricks-Hosted Tracking Server

By default, Databricks provides a managed MLflow tracking server that:

- Requires no additional setup or configuration
- Stores experiment data in your workspace
- Integrates seamlessly with Databricks notebooks and clusters

^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

### Setting the Active Experiment

By default, all MLflow runs are logged to the workspace's tracking server using the active experiment. If no experiment is explicitly set, runs are logged to the notebook experiment. Control where runs are logged by setting the active experiment via `mlflow.set_experiment()`, `mlflow.start_run()`, or environment variables.

```python
import mlflow
mlflow.set_experiment("/Shared/my-experiment")
```

^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

### Related Concepts

- [[Remote MLflow tracking server|MLflow Tracking Server]] – The central service for storing experiment metadata
- [[Databricks Workspace Feature Store UI|Databricks Workspace]] – The environment hosting the managed tracking server
- Experiment Management – Organizing and configuring MLflow experiments
- [[Authentication methods for remote MLflow tracking|Authentication for MLflow]] – PAT vs OAuth setup for remote tracking

### Sources

- choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
```

# Citations

1. [choose-where-your-mlflow-data-is-stored-databricks-on-aws.md](/references/choose-where-your-mlflow-data-is-stored-databricks-on-aws-1fe2cb47.md)
