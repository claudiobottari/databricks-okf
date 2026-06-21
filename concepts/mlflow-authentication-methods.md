---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 78bb2e91dfb61b34a828cb81504b2e6cddfebef3d72f2510e1764f09b4794d3d
  pageDirectory: concepts
  sources:
    - choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
  confidence: 0.92
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-authentication-methods
    - MAM
    - MLflow Authentication
  citations:
    - file: choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
title: MLflow Authentication Methods
description: Authentication approaches for connecting to remote MLflow tracking servers, including Personal Access Tokens (PAT) and OAuth with service principals.
tags:
  - mlflow
  - authentication
  - security
timestamp: "2026-06-19T14:11:23.429Z"
---

# MLflow Authentication Methods

**MLflow Authentication Methods** refer to the mechanisms used to authenticate connections to a remote [MLflow tracking server](/concepts/remote-mlflow-tracking-server.md). When you configure MLflow to log experiments to a remote server—for example, a Databricks-hosted server in a different workspace—you must provide credentials for the connection. The supported methods are Personal Access Tokens (PAT) and OAuth using service principals. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Personal Access Token (PAT)

Personal Access Tokens provide simple token-based authentication. They are straightforward to set up and are well-suited for development environments. However, PATs are user-specific and require manual token management. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

To use a PAT, set the `DATABRICKS_TOKEN` environment variable and then configure the remote tracking URI and experiment. All subsequent runs will be logged to the remote server.

```python
import os

# Set authentication token
os.environ["DATABRICKS_TOKEN"] = "your-personal-access-token"

# Configure remote tracking
mlflow.set_tracking_uri("databricks://remote-workspace-url")
mlflow.set_experiment("/Shared/remote-experiment")
```

^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## OAuth (Service Principal)

OAuth authentication using a service principal is the alternative to PAT. No further details on configuration or trade-offs are provided in the source material. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Setting Up Remote Tracking with Authentication

Regardless of the authentication method chosen, you must set both the tracking URI and the experiment path to direct runs to the remote server. The tracking URI uses the format `databricks://<workspace-url>`. After setting the active experiment, all subsequent calls to `mlflow.start_run()` will log data to the remote server. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

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

## Related Concepts

- Personal Access Token
- Service Principal
- [MLflow Tracking Server](/concepts/remote-mlflow-tracking-server.md)
- [Remote MLflow Tracking](/concepts/remote-mlflow-tracking-server.md)
- Databricks Authentication

## Sources

- choose-where-your-mlflow-data-is-stored-databricks-on-aws.md

# Citations

1. [choose-where-your-mlflow-data-is-stored-databricks-on-aws.md](/references/choose-where-your-mlflow-data-is-stored-databricks-on-aws-1fe2cb47.md)
