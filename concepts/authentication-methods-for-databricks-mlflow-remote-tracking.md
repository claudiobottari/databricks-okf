---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0ba6415c6e04b4d8fdeaea5a0897abbe63b110affdf34652c75e348c19b1d3b6
  pageDirectory: concepts
  sources:
    - choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - authentication-methods-for-databricks-mlflow-remote-tracking
    - AMFDMRT
  citations:
    - file: choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
title: Authentication methods for Databricks MLflow remote tracking
description: "Two authentication options for remote MLflow tracking: Personal Access Tokens (PAT) for simple development setups and OAuth using service principals for production."
tags:
  - mlflow
  - authentication
  - databricks
  - security
timestamp: "2026-06-18T10:56:19.582Z"
---

Here is the wiki page for "Authentication methods for Databricks MLflow remote tracking".

---

**Authentication methods for Databricks MLflow remote tracking** refer to the credentials and configurations used to connect an MLflow client to a remote [MLflow Tracking Server](/concepts/remote-mlflow-tracking-server.md), such as the Databricks-hosted tracking server in a different workspace. Proper authentication is required when the tracking URI is set to a remote endpoint and the client must prove its identity to the server.^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Overview

When you configure MLflow to log experiments to a remote tracking server—for example, by calling `mlflow.set_tracking_uri("databricks://remote-workspace-url")`—you must also provide authentication credentials. The two primary authentication methods for Databricks MLflow remote tracking are Personal Access Tokens (PAT) and OAuth using service principals. Both methods are configured through environment variables or by setting the corresponding parameters in the Databricks CLI configuration profile.^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Personal Access Tokens (PAT)

Personal Access Tokens provide a simple, token-based authentication mechanism. To use PAT authentication, generate a token from the target Databricks workspace and set it as the `DATABRICKS_TOKEN` environment variable.^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

**Pros:** Simple setup, good for development.  
**Cons:** User-specific, requires manual token management.^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

### Example: PAT authentication

```python
import os
import mlflow

# Set authentication token
os.environ["DATABRICKS_TOKEN"] = "your-personal-access-token"

# Configure remote tracking
mlflow.set_tracking_uri("databricks://remote-workspace-url")
mlflow.set_experiment("/Shared/remote-experiment")

with mlflow.start_run():
    mlflow.log_param("model_type", "random_forest")
    mlflow.log_metric("accuracy", 0.95)
```

^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## OAuth (Service Principal)

OAuth authentication uses a service principal to authenticate against the Databricks account API. This method is more suitable for automated or production workflows because it does not depend on a single user's credentials. The credentials are configured using the `DATABRICKS_CLIENT_ID` and `DATABRICKS_CLIENT_SECRET` environment variables, along with the Databricks account host.^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

**Pros:** Suitable for automated workflows and service identities, no reliance on individual user tokens.  
**Cons:** Requires setting up a service principal and managing client secrets.^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

### Example: OAuth (service principal) authentication

```python
import os
import mlflow

# Set OAuth credentials for a service principal
os.environ["DATABRICKS_CLIENT_ID"] = "your-service-principal-client-id"
os.environ["DATABRICKS_CLIENT_SECRET"] = "your-service-principal-client-secret"

# Configure remote tracking
mlflow.set_tracking_uri("databricks://remote-workspace-url")
mlflow.set_experiment("/Shared/remote-experiment")

with mlflow.start_run():
    mlflow.log_param("model_type", "random_forest")
    mlflow.log_metric("accuracy", 0.95)
```

^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Configuration Profiles

Both PAT and OAuth credentials can also be specified through a Databricks CLI configuration profile. The tracking URI uses the `databricks://profile-name` scheme to reference a named profile in the `.databrickscfg` file. This approach keeps credentials out of source code and allows you to switch between profiles for different environments.^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

### Example: Using a CLI profile

```python
import mlflow

# Use the 'central-ml' profile from .databrickscfg
mlflow.set_tracking_uri("databricks://central-ml")
mlflow.set_experiment("/Shared/centralized-experiments/my-project")
```

^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Choosing a Method

- Use **PAT** for interactive development where you want simple, fast setup.
- Use **OAuth (service principal)** for production pipelines, scheduled jobs, or any scenario where the MLflow client runs without a human user present.
- Use **CLI profiles** when you need to manage multiple remote workspaces or want to separate credentials from code entirely.

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) — The core logging component of MLflow
- [MLflow Tracking Server](/concepts/remote-mlflow-tracking-server.md) — The server that stores experiment and run data
- Databricks Personal Access Tokens — Token-based authentication for Databricks APIs
- Service Principal Authentication — OAuth-based authentication for production workloads
- [Databricks CLI Configuration](/concepts/databricks-configuration-profiles.md) — Profile-based credential management

## Sources

- choose-where-your-mlflow-data-is-stored-databricks-on-aws.md

# Citations

1. [choose-where-your-mlflow-data-is-stored-databricks-on-aws.md](/references/choose-where-your-mlflow-data-is-stored-databricks-on-aws-1fe2cb47.md)
