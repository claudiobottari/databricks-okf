---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ac17d2da8106094114e9344cb205fd8dbcd7689e34d474038efe1c64d9b1ea55
  pageDirectory: concepts
  sources:
    - choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracking-uri-configuration
    - MTUC
  citations:
    - file: choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
title: MLflow tracking URI configuration
description: Setting the tracking URI to point to a remote MLflow tracking server using mlflow.set_tracking_uri() to direct where experiment data is logged.
tags:
  - mlflow
  - tracking-uri
  - configuration
timestamp: "2026-06-19T17:42:54.305Z"
---

```markdown
---
title: MLflow tracking URI configuration
summary: How to configure the tracking URI (e.g., databricks://remote-workspace-url) to point MLflow to a remote tracking server.
sources:
  - choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:56:24.947Z"
updatedAt: "2026-06-18T10:56:24.947Z"
tags:
  - mlflow
  - configuration
  - tracking
aliases:
  - mlflow-tracking-uri-configuration
  - MTUC
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# MLflow tracking URI configuration

**MLflow tracking URI configuration** determines where MLflow experiment data, runs, and models are stored and managed. The tracking URI directs MLflow to a tracking server, which can be Databricks-hosted or a remote server in a different workspace or environment.^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Databricks-hosted tracking server

By default, Databricks provides a managed MLflow tracking server that requires no additional setup or configuration. It stores experiment data in your workspace and integrates seamlessly with Databricks notebooks and clusters.^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Setting the active experiment

By default, all MLflow runs are logged to the workspace's tracking server using the active experiment. If no experiment is explicitly set, runs are logged to the [[Notebook experiment in Databricks|notebook experiment]].^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

You can control where runs are logged by setting the active experiment using `mlflow.set_experiment()`, `mlflow.start_run()`, or environment variables. For example:

```python
import mlflow
mlflow.set_experiment("/Shared/my-experiment")
```

This sets the experiment for all subsequent runs in the execution.^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Remote MLflow tracking server

You may need to set up a connection to a remote MLflow tracking server. Common scenarios include developing locally and tracking against the Databricks-hosted server, or tracking to a different tracking server in a different workspace.^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

### Setting the tracking URI and experiment

To log experiments to a remote tracking server, configure both the tracking URI and experiment path:

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

### Authentication methods

Remote tracking server connections require proper authentication. Two supported methods are Personal Access Tokens (PAT) and OAuth using service principals.^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

**PAT authentication** uses a simple token-based approach:

```python
import os

# Set authentication token
os.environ["DATABRICKS_TOKEN"] = "your-personal-access-token"

# Configure remote tracking
mlflow.set_tracking_uri("databricks://remote-workspace-url")
mlflow.set_experiment("/Shared/remote-experiment")
```

PAT authentication offers simple setup and is good for development, but is user-specific and requires manual token management.^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Related concepts

- [[MLflow Tracking]] — The core logging component of MLflow.
- [[MLflow Experiment|MLflow Experiments]] — Logical grouping of MLflow runs.
- [[MLflow Run|MLflow Runs]] — The fundamental unit of logged experiments.
- [[Databricks Autologging]] — Automatic MLflow logging for common ML frameworks.
- [[Notebook experiment in Databricks|Notebook Experiment]] — Default experiment linked to a specific notebook.

## Sources

- choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
```

# Citations

1. [choose-where-your-mlflow-data-is-stored-databricks-on-aws.md](/references/choose-where-your-mlflow-data-is-stored-databricks-on-aws-1fe2cb47.md)
