---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9461796d73c947f07232c2e255fbaff388c54cba55f94ba9c78e207417197f04
  pageDirectory: concepts
  sources:
    - mlflow-tracing-integrations-databricks-on-aws.md
    - tracing-dspy-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - secure-api-key-management-for-mlflow-tracing
    - SAKMFMT
  citations:
    - file: mlflow-tracing-integrations-databricks-on-aws.md
    - file: tracing-dspy-databricks-on-aws.md
title: Secure API Key Management for MLflow Tracing
description: Best practices for managing API keys in production GenAI tracing environments using AI Gateway or Databricks secrets instead of hardcoding credentials.
tags:
  - mlflow
  - security
  - api-keys
timestamp: "2026-06-19T19:41:02.653Z"
---

# Secure API Key Management for [MLflow Tracing](/concepts/mlflow-tracing.md)

**Secure API Key Management for MLflow Tracing** refers to the recommended practices for handling sensitive credentials — such as API keys for large language model (LLM) providers — when instrumenting [MLflow Tracing](/concepts/mlflow-tracing.md) in production. Exposing keys in code or notebooks poses a security risk, and Databricks provides two standard mechanisms to avoid this: [AI Gateway](/concepts/ai-gateway.md) and Databricks Secrets.

## Overview

For production environments, Databricks strongly advises against hard‑coding API keys in application code or notebooks. Instead, use one of the following approaches:

- **[AI Gateway](https://docs.databricks.com/aws/en/ai-gateway/) (preferred)** – Offers governance, rate limiting, fallbacks, and guardrails on top of credential management.
- **Databricks Secrets** – A secure store for sensitive values that can be referenced at runtime.

> **Warning:** Never commit API keys directly in your code or notebooks. Always use AI Gateway or Databricks secrets for sensitive credentials. ^[mlflow-tracing-integrations-databricks-on-aws.md]

## AI Gateway (Recommended)

AI Gateway is the recommended method for managing API keys in production [MLflow Tracing](/concepts/mlflow-tracing.md) workloads. It centralizes access control and monitoring for generative AI models.

To use AI Gateway with [MLflow Tracing](/concepts/mlflow-tracing.md):

1. In your Databricks workspace, go to **Serving** > **Create new endpoint**.
2. Choose an endpoint type and provider.
3. Configure the endpoint with your API key.
4. During endpoint configuration, enable **AI Gateway** and configure rate limiting, fallbacks, and guardrails as needed. ^[mlflow-tracing-integrations-databricks-on-aws.md]

Once the endpoint is created, you can query it using an OpenAI‑compatible client. The example below shows how to set up tracing with an AI Gateway–backed endpoint: ^[mlflow-tracing-integrations-databricks-on-aws.md]

```python
import mlflow
from openai import OpenAI

# In a Databricks notebook, the token is automatically available.
# For other environments, set DATABRICKS_TOKEN as an environment variable.
DATABRICKS_TOKEN = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()

# Enable auto-tracing for OpenAI
mlflow.openai.autolog()

# Set up MLflow tracking (if running outside Databricks)
mlflow.set_tracking_uri("databricks")
mlflow.set_experiment("/Shared/my-genai-app")

client = OpenAI(
  api_key=DATABRICKS_TOKEN,
  base_url="<YOUR_HOST_URL>/serving-endpoints"
)

chat_completion = client.chat.completions.create(
  model="<YOUR_ENDPOINT_NAME>",
  messages=[{"role": "user", "content": "What is MLflow?"}],
  max_tokens=256
)
print(chat_completion.choices[0].message.content)
```

The same pattern – using a Databricks token with a `base_url` pointing to a serving endpoint – applies to other LLM provider integrations (e.g., LangChain, Anthropic) that support an OpenAI‑compatible API.

## Databricks Secrets

Databricks Secrets provide an alternative mechanism for storing API keys securely. While the source material does not include a full code example, the documentation notes that secrets can be used in place of hard‑coded values. To use a secret:

1. Store the API key in a Databricks secret scope.
2. Retrieve it at runtime using `dbutils.secrets.get()` and pass it to your LLM client.

Both AI Gateway and Databricks secrets are referenced as production‑grade solutions across the [MLflow Tracing](/concepts/mlflow-tracing.md) integration guides, including for Tracing DSPy and other frameworks. ^[mlflow-tracing-integrations-databricks-on-aws.md, tracing-dspy-databricks-on-aws.md]

## General Best Practices

- Use environment variables (e.g., `OPENAI_API_KEY`) for local development only. For production, always switch to AI Gateway or Databricks secrets. ^[tracing-dspy-databricks-on-aws.md]
- When using AI Gateway, the Databricks host and token are already set in a Databricks notebook context; for external environments, set `DATABRICKS_HOST` and `DATABRICKS_TOKEN` as environment variables. ^[mlflow-tracing-integrations-databricks-on-aws.md]
- Ensure that auto‑tracing is enabled for your chosen integration (e.g., `mlflow.openai.autolog()`) **after** configuring credentials.

## Enabling Auto‑Tracing on Serverless Compute

On serverless compute clusters, autologging for GenAI tracing frameworks is **not** automatically enabled. You must explicitly call the appropriate `mlflow.<library>.autolog()` function for each integration you wish to trace. This is independent of API key management but is a required step for capturing traces in serverless environments. ^[mlflow-tracing-integrations-databricks-on-aws.md]

## Related Wiki Pages

- [AI Gateway](/concepts/ai-gateway.md)
- Databricks Secrets
- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [Foundation Model Endpoint](/concepts/foundation-model-serving-endpoints.md)
- Tracing DSPy
- [Automatic Tracing](/concepts/automatic-tracing.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) (serverless cluster considerations)

## Sources

- mlflow-tracing-integrations-databricks-on-aws.md
- tracing-dspy-databricks-on-aws.md

# Citations

1. [mlflow-tracing-integrations-databricks-on-aws.md](/references/mlflow-tracing-integrations-databricks-on-aws-22e947f8.md)
2. [tracing-dspy-databricks-on-aws.md](/references/tracing-dspy-databricks-on-aws-2f1da563.md)
