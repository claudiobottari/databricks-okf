---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d5f5025a0219b2a07f28b3f752482a217e34fac300a3ef08de23a7f7710f185d
  pageDirectory: concepts
  sources:
    - get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-hosted-llms
    - Databricks-hosted LLM
  citations:
    - file: get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md
title: Databricks-hosted LLMs
description: Large Language Models served directly from Databricks workspaces, accessible via the databricks-openai library which provides a compatible OpenAI client interface for models like databricks-claude-sonnet-4.
tags:
  - databricks
  - llm
  - foundation-models
  - openai-compatible
timestamp: "2026-06-19T18:59:46.073Z"
---

# Databricks-hosted LLMs

**Databricks-hosted LLMs** are large language models (LLMs) that are hosted directly on the Databricks platform and made accessible through standard APIs. They enable developers to integrate generative AI capabilities into their applications without managing their own model infrastructure.

## Overview

Databricks provides access to a range of foundation models that are hosted on the platform. These models can be called from applications using the `databricks_openai` Python library, which provides an OpenAI-compatible client interface. This allows developers to use familiar patterns for making chat completion requests while leveraging models hosted on Databricks infrastructure. ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

## Accessing Databricks-hosted LLMs

To use a Databricks-hosted LLM, you create a `DatabricksOpenAI` client from the `databricks_openai` package. This client works with the same OpenAI SDK interface but routes requests to Databricks-hosted models. You select a specific model from the list of [available foundation models](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models) on Databricks. ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

### Basic Usage

```python
from databricks_openai import DatabricksOpenAI

client = DatabricksOpenAI()
model_name = "databricks-claude-sonnet-4"

response = client.chat.completions.create(
    model=model_name,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is MLflow?"},
    ],
)
print(response.choices[0].message.content)
```

^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

## Integration with [MLflow Tracing](/concepts/mlflow-tracing.md)

Databricks-hosted LLMs integrate with [MLflow Tracing](/concepts/mlflow-tracing.md) for observability. By enabling automatic instrumentation via `mlflow.openai.autolog()`, every call to a Databricks-hosted LLM is automatically traced, capturing details such as:

- The input messages sent to the model
- The response generated
- How long the request took
- Token usage counts (affecting cost)

When combined with the `@mlflow.trace` decorator on the application entry point, the full execution path — including the LLM call as a child span under the application span — is visible in the MLflow experiment UI. ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

## Environment Setup

To use Databricks-hosted LLMs from a local development environment, you must:

1. Install MLflow with Databricks connectivity: `pip install "mlflow[databricks]>=3.1"`
2. Install the `databricks-openai` and `openai` packages
3. Configure authentication using a Databricks personal access token or another supported authentication method
4. Set up MLflow tracking to point to your Databricks workspace

^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

## Alternative: Using External LLMs

In addition to Databricks-hosted LLMs, the same code pattern can be adapted to use AI Gateway endpoints, Model Serving endpoints, or external models such as OpenAI's `gpt-4o` by replacing the model name in the client call. ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- OpenAI Automatic Instrumentation
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md)

## Sources

- get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md

# Citations

1. [get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md](/references/get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws-58181913.md)
