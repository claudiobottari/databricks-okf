---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4d37d30fa083971e9683ba8ae28693505f07b5b8292093cfe247672311066177
  pageDirectory: concepts
  sources:
    - choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - authentication-for-databricks-remote-mlflow-tracking
    - AFDRMT
  citations:
    - file: choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
title: Authentication for Databricks remote MLflow tracking
description: Methods for authenticating with a remote Databricks MLflow tracking server, including Personal Access Tokens (PAT) and OAuth via service principals.
tags:
  - mlflow
  - authentication
  - databricks
  - security
timestamp: "2026-06-18T14:35:36.325Z"
---

# Authentication for Databricks Remote MLflow Tracking

**Authentication for Databricks Remote MLflow Tracking** refers to the methods used to securely connect to a Databricks-hosted MLflow tracking server from a remote environment (e.g., local development, CI/CD, or a different workspace). Proper authentication ensures that experiment data and model metadata can be logged and retrieved across workspaces without compromising security. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## When Remote Authentication Is Needed

Remote authentication is required when you are developing locally and want to track runs against the Databricks hosted server, or when you need to log experiments to a tracking server in a different Databricks workspace. To use a remote server, you must configure both the tracking URI and the experiment path in your code. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Authentication Methods

MLflow supports two authentication methods for remote Databricks tracking servers: **Personal Access Tokens (PAT)** and **OAuth (service principal)**. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

### Personal Access Token (PAT)

PAT authentication uses a long-lived token tied to a Databricks user. It has a simple setup and is suitable for development environments. The token must be set as the environment variable `DATABRICKS_TOKEN` before making any MLflow API calls.

```python
import os

# Set authentication token
os.environ["DATABRICKS_TOKEN"] = "your-personal-access-token"

# Configure remote tracking
mlflow.set_tracking_uri("databricks://remote-workspace-url")
mlflow.set_experiment("/Shared/remote-experiment")
```

**Pros:** Simple setup, good for development.  
**Cons:** User-specific, requires manual token management. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

### OAuth (Service Principal)

OAuth authentication using a service principal is an alternative method mentioned in the Databricks documentation. No specific implementation details are provided in the source material beyond its availability as an authentication option. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Configuration Workflow

Regardless of the authentication method, the general workflow is:

1. Set the authentication credentials (e.g., environment variable or OAuth profile).
2. Call `mlflow.set_tracking_uri("databricks://<workspace-url>")` to point to the remote server.
3. Call `mlflow.set_experiment("<experiment-path>")` to specify the experiment in that remote workspace.
4. Log runs normally inside `mlflow.start_run()` blocks.

All subsequent MLflow runs will be logged to the remote server using the configured authentication. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Related Concepts

- [MLflow tracking server](/concepts/remote-mlflow-tracking-server.md) – The server that stores experiment and run data.
- [Personal Access Token (PAT)](/concepts/databricks-personal-access-token-pat-authentication.md) – Token‑based authentication for Databricks APIs.
- Service principal – Non‑user identity for automated workloads.
- Databricks workspace – The environment where the remote tracking server resides.
- [Set the active experiment](/concepts/mlflow-active-experiment.md) – Controlling which experiment MLflow logs to.

## Sources

- choose-where-your-mlflow-data-is-stored-databricks-on-aws.md

# Citations

1. [choose-where-your-mlflow-data-is-stored-databricks-on-aws.md](/references/choose-where-your-mlflow-data-is-stored-databricks-on-aws-1fe2cb47.md)
