---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a8b35697d5bde17e2e22579522d0ac72c25ee8fa4a63c687740fb34d7b7ed673
  pageDirectory: concepts
  sources:
    - tracing-smolagents-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-environment-configuration-for-mlflow-tracing
    - DECFMT
  citations:
    - file: tracing-smolagents-databricks-on-aws.md
title: Databricks Environment Configuration for MLflow Tracing
description: Required environment setup including DATABRICKS_HOST, DATABRICKS_TOKEN, and LLM provider API keys for MLflow Tracing with Smolagents
tags:
  - databricks
  - configuration
  - mlflow
timestamp: "2026-06-19T23:13:20.277Z"
---

## Databricks Environment Configuration for [MLflow Tracing](/concepts/mlflow-tracing.md)

**Databricks Environment Configuration for [MLflow](/concepts/mlflow.md) Tracing** refers to the setup steps required to enable [MLflow Tracing](/concepts/mlflow-tracing.md) on Databricks, including credential configuration, API key management, and enabling autologging for supported integrations such as [Smolagents](/concepts/smolagents.md). Proper environment configuration ensures that [Traces](/concepts/traces.md) are captured and logged to the experiment UI without errors. ^[tracing-smolagents-databricks-on-aws.md]

### Prerequisites

To use [MLflow Tracing](/concepts/mlflow-tracing.md), install the full [MLflow](/concepts/mlflow.md) package with Databricks extras and the relevant library for the integration you want to trace. For example, for [Smolagents](/concepts/smolagents.md):

```bash
pip install --upgrade "[[mlflow|MLflow]][databricks]>=3.1" [[smolagents|Smolagents]] openai
```

[MLflow 3](/concepts/mlflow-3.md) is recommended for the best tracing experience. The `mlflow[databricks]` package includes all features for local development and experimentation on Databricks. ^[tracing-smolagents-databricks-on-aws.md]

### Credential Configuration

- **For users outside Databricks notebooks**: Set the `DATABRICKS_HOST` and `DATABRICKS_TOKEN` environment variables to point to your workspace and provide authentication:

  ```bash
  export DATABRICKS_HOST="https://your-workspace.cloud.databricks.com"
  export DATABRICKS_TOKEN="your-personal-access-token"
  ```

- **For users inside Databricks notebooks**: These credentials are automatically set for you, and no manual export is required.

^[tracing-smolagents-databricks-on-aws.md]

### API Key Management

Ensure that your LLM provider API keys (e.g., `OPENAI_API_KEY`) are configured as environment variables. For production environments, use [AI Gateway](/concepts/ai-gateway.md) or Databricks Secrets instead of hardcoded values for secure API key management:

```bash
export OPENAI_API_KEY="your-openai-api-key"
# Add other provider keys as needed
```

^[tracing-smolagents-databricks-on-aws.md]

### Enabling Autologging

Tracing requires explicit activation for each integration. Call the integration‑specific `autolog` function in your code. For [Smolagents](/concepts/smolagents.md):

```python
import [[mlflow|MLflow]]
[[mlflow|MLflow]].[[smolagents|Smolagents]].autolog()
```

**Important**: On Serverless Compute clusters, [Autologging for GenAI Tracing](/concepts/autologging-for-genai-tracing.md) frameworks is not automatically enabled. You must explicitly call `mlflow.<library>.autolog()` for the specific integration you want to trace. ^[tracing-smolagents-databricks-on-aws.md]

### Disabling Auto‑Tracing

To disable auto‑tracing for a specific integration, use `mlflow.[Smolagents](/concepts/smolagents.md).autolog(disable=True)`. To disable globally for all integrations, use `mlflow.autolog(disable=True)`. ^[tracing-smolagents-databricks-on-aws.md]

### Limitations

[MLflow](/concepts/mlflow.md) auto‑tracing only supports synchronous calls. Asynchronous API and streaming methods are not traced. ^[tracing-smolagents-databricks-on-aws.md]

### Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [Smolagents](/concepts/smolagents.md)
- [Autolog](/concepts/mlflow-autologging.md)
- [AI Gateway](/concepts/ai-gateway.md)
- Databricks Secrets
- [Serverless Compute Clusters](/concepts/serverless-gpu-compute.md)
- [Experiment UI](/concepts/mlflow-experiment.md)

### Sources

- tracing-smolagents-databricks-on-aws.md

# Citations

1. [tracing-smolagents-databricks-on-aws.md](/references/tracing-smolagents-databricks-on-aws-485dc1ff.md)
