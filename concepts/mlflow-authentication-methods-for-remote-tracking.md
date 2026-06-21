---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a16ce9a49038dd0a6640fb5916ffec564132b6d43f54c3c9c704636b887ae7b1
  pageDirectory: concepts
  sources:
    - choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-authentication-methods-for-remote-tracking
    - MAMFRT
  citations:
    - file: choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
title: MLflow Authentication Methods for Remote Tracking
description: Authentication approaches for remote MLflow tracking server connections, including Personal Access Tokens (PAT) and OAuth using service principals.
tags:
  - mlflow
  - authentication
  - security
  - databricks
timestamp: "2026-06-19T09:12:13.382Z"
---

# MLflow Authentication Methods for Remote Tracking

**MLflow Authentication Methods for Remote Tracking** refers to the mechanisms used to authenticate connections to a remote MLflow tracking server when logging experiments, runs, and models outside the local environment. This is necessary when developing locally and tracking against a Databricks-hosted server, or when logging to a tracking server in a different workspace. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Overview

Remote tracking server connections require proper authentication. MLflow supports two primary authentication methods when connecting to a Databricks-hosted tracking server: [Personal Access Tokens (PAT)](/concepts/databricks-personal-access-token-pat-authentication.md) and OAuth using service principals. The choice depends on your security requirements, development workflow, and whether you need user-scoped or application-level access. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Authentication Methods

### Personal Access Tokens (PAT)

PATs provide a simple, token-based authentication mechanism. They are well suited for development scenarios where quick setup is a priority. However, PATs are user-specific and require manual token management. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

To use a PAT, set the `DATABRICKS_TOKEN` environment variable before configuring the tracking URI:

```python
import os
import mlflow

# Set authentication token
os.environ["DATABRICKS_TOKEN"] = "your-personal-access-token"

# Configure remote tracking
mlflow.set_tracking_uri("databricks://remote-workspace-url")
mlflow.set_experiment("/Shared/remote-experiment")
```

### OAuth (Service Principal)

OAuth authentication using a service principal is the recommended approach for automated or production workflows. Service principals allow application-level authentication without tying access to an individual user. The source material does not provide code examples for OAuth setup, but it lists it as an alternative to PAT. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Configuration Steps

To connect to a remote tracking server, perform two configuration steps:

1. Set the tracking URI to point to the remote workspace.
2. Set the experiment path within that remote server.

All subsequent runs will be logged to the specified remote experiment. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

Example with PAT and remote tracking:

```python
import os
import mlflow

os.environ["DATABRICKS_TOKEN"] = "your-personal-access-token"
mlflow.set_tracking_uri("databricks://remote-workspace-url")
mlflow.set_experiment("/Shared/centralized-experiments/my-project")

with mlflow.start_run():
    mlflow.log_param("model_type", "random_forest")
    mlflow.log_metric("accuracy", 0.95)
```

## Best Practices

- **Use OAuth for production systems** – PATs are user-specific and can expire or be revoked; service principals offer more robust access control for automated pipelines.
- **Keep tokens secure** – Never hard-code tokens in source code. Use environment variables or secret management tools.
- **Match the authentication method to the environment** – For local development, PATs are convenient; for CI/CD or scheduled jobs, prefer OAuth.
- **Verify connectivity** – After setting the tracking URI and authentication, test with a small run before scaling up.

## Related Concepts

- [Databricks-hosted MLflow tracking server](/concepts/databricks-hosted-mlflow-tracking-server.md) – The default managed server in Databricks workspaces.
- [MLflow tracking URI](/concepts/mlflow-tracking-uri.md) – The address used to connect to a tracking server.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – Logical grouping of runs in a tracking server.
- Service Principal Authentication – Identity-based authentication for automated workloads.
- [Personal Access Token (PAT)](/concepts/databricks-personal-access-token-pat-authentication.md) – Token-based user authentication.

## Sources

- choose-where-your-mlflow-data-is-stored-databricks-on-aws.md

# Citations

1. [choose-where-your-mlflow-data-is-stored-databricks-on-aws.md](/references/choose-where-your-mlflow-data-is-stored-databricks-on-aws-1fe2cb47.md)
