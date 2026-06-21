---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f316c4ed20c0d4b35e33904a16d450056996ebd647ad8bd7df8b93e96642b5da
  pageDirectory: concepts
  sources:
    - choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - authentication-methods-for-remote-mlflow-tracking
    - AMFRMT
    - Authentication for MLflow
  citations:
    - file: choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
title: Authentication methods for remote MLflow tracking
description: "Two authentication approaches for remote tracking server connections: Personal Access Tokens (PAT) for simple token-based auth and OAuth using service principals."
tags:
  - mlflow
  - authentication
  - security
  - databricks
timestamp: "2026-06-19T17:42:45.500Z"
---

Here is the wiki page for "Authentication methods for remote MLflow tracking", written based solely on the provided source material.

---

## Authentication methods for remote MLflow tracking

**Authentication methods for remote MLflow tracking** are the mechanisms used to securely connect an [MLflow](/concepts/mlflow.md) client to a remote tracking server. When you need to log experiments to a server outside your local environment—such as a Databricks-hosted tracking server—proper authentication is required. The two primary methods are Personal Access Tokens (PAT) and OAuth using service principals. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

### Personal Access Tokens (PAT)

Personal Access Tokens provide simple token-based authentication for remote tracking server connections. PATs are set via the `DATABRICKS_TOKEN` environment variable before configuring the tracking URI. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

**Pros:** Simple setup, good for development. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

**Cons:** User-specific, requires manual token management. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

```python
import os
import mlflow

# Set authentication token
os.environ["DATABRICKS_TOKEN"] = "your-personal-access-token"

# Configure remote tracking
mlflow.set_tracking_uri("databricks://remote-workspace-url")
mlflow.set_experiment("/Shared/remote-experiment")
```

^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

### OAuth (service principal)

OAuth authentication using service principals provides an alternative to PAT-based connections. This method is appropriate for automated or service-based access to a remote MLflow tracking server. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

### Common remote tracking scenarios

Remote tracking connections are commonly needed when developing locally and wanting to track against a Databricks-hosted server, or when tracking to an MLflow tracking server in a different workspace. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

### Related concepts

- [MLflow tracking server](/concepts/remote-mlflow-tracking-server.md) — The server that stores experiment data, runs, and models.
- [Databricks-hosted tracking server](/concepts/databricks-hosted-mlflow-tracking-server.md) — The managed MLflow tracking server provided by default in Databricks workspaces.
- [Set tracking URI and experiment](/concepts/setting-the-active-experiment-in-mlflow.md) — Configuring both the tracking URI and experiment path for remote logging.
- Service principal authentication — OAuth-based authentication for automated access.
- [Personal access token (PAT)](/concepts/databricks-personal-access-token-pat-authentication.md) — A token-based authentication credential.

## Sources

- choose-where-your-mlflow-data-is-stored-databricks-on-aws.md

# Citations

1. [choose-where-your-mlflow-data-is-stored-databricks-on-aws.md](/references/choose-where-your-mlflow-data-is-stored-databricks-on-aws-1fe2cb47.md)
