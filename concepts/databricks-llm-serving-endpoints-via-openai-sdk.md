---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 12f5a9e2b7a891038ab81202f54148c2bbe4a9c3049df4646b8dbf3009a91394
  pageDirectory: concepts
  sources:
    - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-llm-serving-endpoints-via-openai-sdk
    - DLSEVOS
  citations:
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
title: Databricks LLM Serving Endpoints via OpenAI SDK
description: Using the OpenAI Python SDK client configured with Databricks credentials to call Databricks-hosted LLMs (e.g., Claude Sonnet) as serving endpoints.
tags:
  - databricks
  - openai
  - llm-serving
  - api
timestamp: "2026-06-19T21:53:55.784Z"
---

# Databricks LLM Serving Endpoints via OpenAI SDK

**Databricks LLM Serving Endpoints via OpenAI SDK** refers to the method of connecting to Databricks-hosted large language model (LLM) serving endpoints using the OpenAI Python SDK. This approach allows developers to use the familiar OpenAI client interface while routing requests through Databricks serving endpoints, enabling access to models such as Claude Sonnet hosted on Databricks infrastructure. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Overview

The OpenAI SDK can be configured to communicate with Databricks LLM serving endpoints by setting the client's `base_url` to the Databricks serving endpoints URL and providing a Databricks authentication token as the API key. This enables applications to use OpenAI-compatible API calls while leveraging models deployed on Databricks. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Configuration

To connect to a Databricks LLM serving endpoint using the OpenAI SDK, you must configure the client with Databricks credentials:

```python
from openai import OpenAI
import mlflow

# Get Databricks credentials
mlflow_creds = mlflow.utils.databricks_utils.get_databricks_host_creds()

# Configure OpenAI client to use Databricks serving endpoints
client = OpenAI(
    api_key=mlflow_creds.token,
    base_url=f"{mlflow_creds.host}/serving-endpoints"
)
```

^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### Authentication Requirements

When running outside a Databricks notebook, you must set the following environment variables:

- `DATABRICKS_HOST`: Your workspace URL (e.g., `https://your-workspace.cloud.databricks.com`)
- `DATABRICKS_TOKEN`: Your personal access token

^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Usage

Once configured, the client can be used to make chat completion requests to Databricks-hosted models. The model parameter specifies the serving endpoint name:

```python
response = client.chat.completions.create(
    model="databricks-claude-sonnet-4-5",  # Databricks hosted model endpoint
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"},
    ],
)
return response.choices[0].message.content
```

^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Integration with MLflow

The OpenAI SDK integration with Databricks serving endpoints works seamlessly with [MLflow](/concepts/mlflow.md) for tracing and evaluation. Enable automatic tracing to capture all API calls:

```python
mlflow.openai.autolog()
```

^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

This allows you to:
- Trace all LLM calls for debugging and monitoring
- Evaluate GenAI applications using [MLflow Scorers](/concepts/mlflow-scorers.md)
- Compare results across different prompts and model configurations

## Use Cases

- **GenAI Application Development**: Build and evaluate applications that use Databricks-hosted LLMs with the familiar OpenAI SDK interface
- **Prompt Engineering**: Iterate on system prompts and evaluate results using [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md)
- **Multi-Model Access**: Switch between different Databricks-hosted models by changing the `model` parameter
- **Production Monitoring**: Combine with [Production Monitoring](/concepts/production-monitoring.md) for scheduled scoring workflows

## Related Concepts

- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — Framework for evaluating GenAI applications
- [MLflow Scorers](/concepts/mlflow-scorers.md) — Define evaluation criteria for LLM outputs
- LLM Serving Endpoints — Databricks infrastructure for hosting LLMs
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — Controls for serverless workload spending
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) — Evaluation workflow for AI agents

## Sources

- 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md

# Citations

1. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
