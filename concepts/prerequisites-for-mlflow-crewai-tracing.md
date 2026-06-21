---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 498d055dda9393ea1f8b76fc3655d6036c418a1c5e20dc2b5aee53df34d570d2
  pageDirectory: concepts
  sources:
    - tracing-crewai-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prerequisites-for-mlflow-crewai-tracing
    - PFMCT
  citations:
    - file: tracing-crewai-databricks-on-aws.md
title: Prerequisites for MLflow CrewAI Tracing
description: Environment setup requirements including MLflow 3+, crewai library, API keys, and Databricks credentials
tags:
  - mlflow
  - crewai
  - setup
  - prerequisites
timestamp: "2026-06-19T23:10:34.094Z"
---

# Prerequisites for [MLflow](/concepts/mlflow.md) CrewAI Tracing

The **Prerequisites for [MLflow](/concepts/mlflow.md) CrewAI Tracing** describe the software, environment configuration, and access setup required to enable automatic trace capture of CrewAI multi-agent workflows using [MLflow Tracing](/concepts/mlflow-tracing.md). These prerequisites cover both development and production environments.

## Software Requirements

To use [MLflow Tracing](/concepts/mlflow-tracing.md) with CrewAI, you must install [MLflow](/concepts/mlflow.md) and the `crewai` library (which includes `crewai_tools`). ^[tracing-crewai-databricks-on-aws.md]

For development environments, install the full [MLflow](/concepts/mlflow.md) package with Databricks extras and `crewai`:

```bash
pip install --upgrade "[[mlflow|MLflow]][databricks]>=3.1" crewai
```

The full `mlflow[databricks]` package includes all features for local development and experimentation on Databricks. [MLflow 3](/concepts/mlflow-3.md) is highly recommended for the best tracing experience with CrewAI. ^[tracing-crewai-databricks-on-aws.md]

## Environment Configuration

### Databricks Credentials

**For users outside Databricks notebooks**: You must set your Databricks environment variables to enable [MLflow](/concepts/mlflow.md) to communicate with your Databricks workspace:

```bash
export DATABRICKS_HOST="https://your-workspace.cloud.databricks.com"
export DATABRICKS_TOKEN="your-personal-access-token"
```

**For users inside Databricks notebooks**: These credentials are automatically set for you. ^[tracing-crewai-databricks-on-aws.md]

### API Keys for LLM Providers

Ensure any necessary LLM provider API keys are configured. For production use, use [AI Gateway](/concepts/ai-gateway.md) or [Databricks secrets](/concepts/databricks-secret-scopes.md) instead of hardcoded values:

```bash
export OPENAI_API_KEY="your-openai-api-key"
export SERPER_API_KEY="your-serper-api-key"
# Add other provider keys as needed
```

^[tracing-crewai-databricks-on-aws.md]

## Explicit Autologging Requirement

On serverless compute clusters, [Autologging for GenAI Tracing](/concepts/autologging-for-genai-tracing.md) frameworks is not automatically enabled. You must explicitly enable autologging by calling the appropriate `mlflow.<library>.autolog()` function for the specific integrations you want to trace. For CrewAI, this means calling `mlflow.crewai.autolog()` to enable [Automatic Tracing](/concepts/automatic-tracing.md). ^[tracing-crewai-databricks-on-aws.md]

## Supported Workloads

Currently, [MLflow](/concepts/mlflow.md) CrewAI integration only supports tracing for synchronous task execution. Asynchronous task execution and `kickoff` are not supported. ^[tracing-crewai-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- CrewAI
- [MLflow Autologging](/concepts/mlflow-autologging.md)
- Databricks Secrets
- [MLflow Experiments](/concepts/mlflow-experiment.md)

## Sources

- tracing-crewai-databricks-on-aws.md

# Citations

1. [tracing-crewai-databricks-on-aws.md](/references/tracing-crewai-databricks-on-aws-c9f44377.md)
