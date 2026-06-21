---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c70f9831c0332fa0a2c5b2a7314480e1bac0923c9ea40ad3cd6b944c5269b650
  pageDirectory: concepts
  sources:
    - mlflow-tracing-integrations-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-integrations
    - MTI
    - Tracing Integrations
    - Auto-tracing integrations
    - GenAI Tracing Integrations
    - MLflow Tracing integrations documentation
    - Trace Instrumentation
    - Trace ingestion
    - auto-tracing integrations
    - mlflow-tracing-integrations-library
    - MTIL
  citations:
    - file: mlflow-tracing-integrations-databricks-on-aws.md
title: MLflow Tracing Integrations
description: The set of popular GenAI libraries and frameworks that MLflow Tracing natively supports for automatic observability.
tags:
  - mlflow
  - tracing
  - integrations
timestamp: "2026-06-19T19:41:05.339Z"
---

---

title: [MLflow Tracing](/concepts/mlflow-tracing.md) Integrations
summary: [MLflow Tracing](/concepts/mlflow-tracing.md) provides one-line automatic tracing for various Generative AI libraries and frameworks, with secure API key management and support for multiple integrations.
sources:
  - mlflow-tracing-integrations-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T20:00:00.000Z"
updatedAt: "2026-06-19T20:00:00.000Z"
tags:
  - mlflow
  - tracing
  - generative-ai
  - observability
aliases:
  - mlflow-tracing-integrations
  - mlflow-auto-tracing
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0

---

# [MLflow Tracing](/concepts/mlflow-tracing.md) Integrations

**MLflow Tracing Integrations** refers to the built-in support within [MLflow Tracing](/concepts/mlflow-tracing.md) for automatically instrumenting a wide array of popular Generative AI libraries and frameworks. It provides a **one-line automatic tracing** experience that enables immediate observability into GenAI applications with minimal setup, capturing application logic and intermediate steps such as LLM calls, tool usage, and agent interactions. ^[mlflow-tracing-integrations-databricks-on-aws.md]

## Overview

The integration covers many widely used libraries, including OpenAI, LangChain, LangGraph, Anthropic, DSPy, Databricks, Bedrock, and AutoGen. For each supported library, calling `mlflow.<library>.autolog()` enables automatic trace generation. This broad support means you can gain observability without significant code changes, leveraging existing tools. For custom components or unsupported libraries, MLflow also provides powerful [Manual Tracing APIs](/concepts/manual-tracing-apis.md). ^[mlflow-tracing-integrations-databricks-on-aws.md]

On serverless compute clusters, autologging for GenAI tracing frameworks is not automatically enabled. You must explicitly enable autologging by calling the appropriate `mlflow.<library>.autolog()` function for each integration you want to trace. ^[mlflow-tracing-integrations-databricks-on-aws.md]

## Top Integrations at a Glance

Below is a quick‑start example for the OpenAI integration. Similar one‑line enabling patterns apply to all other supported libraries. For detailed prerequisites and advanced scenarios, refer to the dedicated integration pages linked from the source documentation.

```python
import mlflow
import openai

# If running outside a Databricks notebook, set DATABRICKS_HOST and DATABRICKS_TOKEN.

# Enable auto-tracing for OpenAI
mlflow.openai.autolog()

# Set up MLflow tracking
mlflow.set_tracking_uri("databricks")
mlflow.set_experiment("/Shared/openai-tracing-demo")

client = openai.OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "What is the capital of France?"}],
    temperature=0.1,
    max_tokens=100,
)
# View trace in MLflow UI
```

^[mlflow-tracing-integrations-databricks-on-aws.md]

## Secure API Key Management

For production environments, Databricks recommends using either [AI Gateway](/concepts/ai-gateway.md) (preferred) or Databricks Secrets to manage API keys. Never commit API keys directly in code or notebooks. ^[mlflow-tracing-integrations-databricks-on-aws.md]

- **AI Gateway (Recommended):** Create a Foundation Model endpoint configured with AI Gateway. During endpoint configuration, enable AI Gateway and set rate limiting, fallbacks, and guardrails as needed. The endpoint can then be queried with tracing automatically enabled. ^[mlflow-tracing-integrations-databricks-on-aws.md]
- **Databricks Secrets:** An alternative method for storing and accessing sensitive credentials. ^[mlflow-tracing-integrations-databricks-on-aws.md]

Example of using AI Gateway with OpenAI tracing in a Databricks notebook:

```python
import mlflow
from openai import OpenAI

# In Databricks notebook, get token from context
DATABRICKS_TOKEN = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()

mlflow.openai.autolog()
mlflow.set_tracking_uri("databricks")
mlflow.set_experiment("/Shared/my-genai-app")

client = OpenAI(
    api_key=DATABRICKS_TOKEN,
    base_url="<YOUR_HOST_URL>/serving-endpoints"
)

chat_completion = client.chat.completions.create(
    messages=[...],
    model="<YOUR_ENDPOINT_NAME>",
    max_tokens=256,
)
```

^[mlflow-tracing-integrations-databricks-on-aws.md]

## Enabling Multiple Auto Tracing Integrations

GenAI applications often combine multiple libraries. [MLflow Tracing](/concepts/mlflow-tracing.md) allows enabling auto‑tracing for several integrations simultaneously, generating a single cohesive trace that spans all steps. For example:

```python
import mlflow

mlflow.langchain.autolog()
mlflow.openai.autolog()

# Code using both LangChain and OpenAI directly...
# MLflow generates one combined trace.
```

^[mlflow-tracing-integrations-databricks-on-aws.md]

More examples of combining integrations can be found on the [Automatic Tracing](/concepts/automatic-tracing.md) page. ^[mlflow-tracing-integrations-databricks-on-aws.md]

## Disabling Auto Tracing

Auto tracing for a specific library can be disabled by calling `mlflow.<library>.autolog(disable=True)`. To disable all autologging integrations at once, use `mlflow.autolog(disable=True)`. ^[mlflow-tracing-integrations-databricks-on-aws.md]

```python
import mlflow

# Disable for a specific library
mlflow.openai.autolog(disable=True)

# Disable all autologging
mlflow.autolog(disable=True)
```

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [Manual Tracing APIs](/concepts/manual-tracing-apis.md)
- [Automatic Tracing](/concepts/automatic-tracing.md)
- [AI Gateway](/concepts/ai-gateway.md)
- Databricks Secrets
- [Foundation Model Endpoints](/concepts/foundation-model-serving-endpoints.md)

## Sources

- mlflow-tracing-integrations-databricks-on-aws.md

# Citations

1. [mlflow-tracing-integrations-databricks-on-aws.md](/references/mlflow-tracing-integrations-databricks-on-aws-22e947f8.md)
