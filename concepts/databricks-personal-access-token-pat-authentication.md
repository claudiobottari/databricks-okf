---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dbcf8dfe04ba2ffc791cd79603da8c92932b4383d99a4b3b7c0a9c5cedbd922c
  pageDirectory: concepts
  sources:
    - get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-personal-access-token-pat-authentication
    - DPAT(A
    - Databricks personal access token authentication
    - personal access token (PAT) authentication
    - Create personal access tokens for workspace users
    - Databricks personal access token
    - Personal Access Token (PAT)
    - Personal Access Token (PAT) authentication#Databricks PAT|Databricks personal access token authentication
    - Personal Access Token Authentication
    - Personal Access Tokens
    - Personal Access Tokens (PAT)
    - Personal access token
    - Personal access token (PAT)
    - Personal access token authentication
    - Personal access tokens
    - personal access token
    - personal access token (PAT)
    - personal access token authentication
    - personal access tokens
    - personal access tokens (PATs)
  citations:
    - file: get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md
title: Databricks Personal Access Token (PAT) Authentication
description: An authentication method for connecting local development tools to Databricks workspaces, using DATABRICKS_TOKEN and DATABRICKS_HOST environment variables.
tags:
  - authentication
  - databricks
  - security
  - ide
timestamp: "2026-06-19T10:44:37.866Z"
---

Here is the wiki page for "Databricks Personal Access Token (PAT) Authentication".

---

## Databricks Personal Access Token (PAT) Authentication

**Databricks Personal Access Token (PAT) Authentication** is a method for authenticating access to the Databricks workspace API. A PAT is a user- or service-principal-generated token that is used to programmatically interact with Databricks resources, such as running jobs, querying the catalog, or—most commonly—connecting a local IDE or notebook environment to MLflow for GenAI development. ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

### Usage in [MLflow Tracing](/concepts/mlflow-tracing.md)

In the context of [MLflow Tracing for GenAI](/concepts/mlflow-tracing-for-genai.md), a Databricks PAT is the primary authentication mechanism used to connect a local development environment (such as VS Code, PyCharm, or Jupyter) to your Databricks workspace. This enables you to log traces and experiments from your local code directly to the Databricks-hosted MLflow server. ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

MLflow also supports other Databricks-supported authentication methods, though the PAT is the most common for local development workflows. ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

### How to Generate and Use a PAT

1. **Generate a Token**: Within the MLflow Experiment UI, navigate to the kebab menu (the three-dot icon) and select **Log traces locally** > **Generate API Key**. A code snippet is generated containing the necessary environment variables.
2. **Set Environment Variables**: The generated snippet exports the following environment variables in your terminal:
   - `DATABRICKS_TOKEN`: The personal access token value.
   - `DATABRICKS_HOST`: The URL of your Databricks workspace (e.g., `https://<workspace-name>.cloud.databricks.com`).
3. **Configure MLflow**: These environment variables, along with `MLFLOW_TRACKING_URI=databricks` and `MLFLOW_REGISTRY_URI=databricks-uc`, configure the MLflow client to authenticate and communicate with your workspace. ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

### Related Concepts

- Databricks-supported authentication methods — Other ways to authenticate with Databricks (e.g., OAuth, service principals).
- [MLflow Tracing for GenAI](/concepts/mlflow-tracing-for-genai.md) — The broader framework that uses PAT authentication for local development.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The container for GenAI app traces and runs.
- Databricks CLI — Another tool that can use PAT-based authentication for workspace operations.
- Service Principals — Alternative identity type that can also generate tokens.

### Sources

- get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md

# Citations

1. [get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md](/references/get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws-58181913.md)
