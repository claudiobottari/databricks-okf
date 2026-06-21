---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 850c7aaa0db9b533731e5da12a06524ca3a5c892fb06da1aed547d1fcf47ff80
  pageDirectory: concepts
  sources:
    - develop-code-based-scorers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-hosted-llms-with-openai-compatible-api
    - DLWOA
  citations:
    - file: develop-code-based-scorers-databricks-on-aws.md
title: Databricks-hosted LLMs with OpenAI-compatible API
description: Using the databricks-openai package to create an OpenAI-compatible client that connects to Databricks-hosted foundation models for GenAI application development.
tags:
  - databricks
  - llm
  - openai
  - api
timestamp: "2026-06-18T12:01:02.656Z"
---

# Databricks-hosted LLMs with OpenAI-compatible API

**Databricks-hosted LLMs with OpenAI-compatible API** provides access to a range of foundation models (LLMs) hosted on Databricks infrastructure through an API that mirrors the standard OpenAI client interface. This allows users to interact with Databricks-hosted models using the same patterns and tools they would use with OpenAI's API.

## Overview

Databricks offers a set of pre-trained foundation models that are hosted on Databricks infrastructure. These models can be accessed programmatically through the [`databricks-openai` package](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models), which provides an OpenAI-compatible client interface. ^[develop-code-based-scorers-databricks-on-aws.md]

The hosted models are available for direct use in [MLflow](/concepts/mlflow.md)-based applications and can be selected from the list of supported foundation models. ^[develop-code-based-scorers-databricks-on-aws.md]

## Using the API

### Setup

To use Databricks-hosted LLMs, install the `databricks-openai` package alongside the required MLflow dependencies:

```python
%pip install -q --upgrade "mlflow[databricks]>=3.1" opendai
dbutils.library.restartPython()
```

Note: The `mlflow[databricks]` version should be at least 3.1 for the best GenAI experience. The `openai` package is required as the example below uses the OpenAI client. ^[develop-code-based-scorers-databricks-on-aws.md]

### Creating a Client

Create an OpenAI-compatible client that connects to Databricks-hosted LLMs:

```python
from databricks_openai import DatabricksOpenAI

# Create an OpenAI client that is connected to Databricks-hosted LLMs
client = DatabricksOpenAI()
```

^[develop-code-based-scorers-databricks-on-aws.md]

### Selecting a Model

Choose a model from the list of [available foundation models](/concepts/foundation-model-apis.md). For example, to use a specific model:

```python
# Select an LLM
model_name = "databricks-claude-sonnet-4"
```

Note: Check the [supported models documentation](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models) for the current list of available models. ^[develop-code-based-scorers-databricks-on-aws.md]

### Making API Calls

Use the standard OpenAI chat completions pattern to generate responses:

```python
@mlflow.trace
def sample_app(messages: list[dict[str, str]]):
    # 1. Prepare messages for the LLM
    messages_for_llm = [
        {"role": "system", "content": "You are a helpful assistant."},
        *messages,
    ]
    # 2. Call LLM to generate a response
    response = client.chat.completions.create(
        model=model_name,
        messages=messages_for_llm,
    )
    return response.choices[0].message.content

sample_app([{"role": "user", "content": "What is the capital of France?"}])
```

^[develop-code-based-scorers-databricks-on-aws.md]

## Automatic Instrumentation with [MLflow Tracing](/concepts/mlflow-tracing.md)

Databricks automatically instruments applications using the [MLflow Tracing](/concepts/mlflow-tracing.md) system when `mlflow.openai.autolog()` is enabled:

```python
import mlflow
mlflow.openai.autolog()
```

This ensures that all interactions with the LLM are automatically captured and recorded for [trace-based evaluation](/concepts/mlflow-trace-based-evaluation.md) and monitoring purposes. ^[develop-code-based-scorers-databricks-on-aws.md]

## Key Features

### OpenAI Compatibility

The API uses the same request/response format as OpenAI's API, making it easy to migrate existing applications or use standard OpenAI tooling:

- Request format: `{"model": model_name, "messages": messages}`
- Response format: `response.choices[0].message.content`

### Integration with MLflow Evaluation

The [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) framework can be used directly with Databricks-hosted LLMs. The `evaluate()` function supports:

- [custom code-based scorers](/concepts/code-based-scorers.md) for flexible evaluation metrics
- [LLM-as-a-Judge](/concepts/llm-as-a-judge.md) metrics for semantic evaluation
- [Production Monitoring](/concepts/production-monitoring.md) for continuous quality assessment

## Setting up Tracking

If running outside of Databricks, configure MLflow tracking to point to a Databricks workspace:

```python
# Set up MLflow tracking to Databricks
mlflow.set_tracking_uri("databricks")
```

For Databricks notebooks, the experiment defaults to the notebook environment:

```python
# In Databricks notebooks, the experiment defaults to the notebook experiment
mlflow.set_experiment("/Shared/docs-demo")
```

^[develop-code-based-scorers-databricks-on-aws.md]

## Related Concepts

- Foundation Models — Pre-trained models hosted on Databricks infrastructure
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Automatic telemetry and tracing for LLM interactions
- Custom Code-Based Scorers — Flexible evaluation metrics for AI applications
- [LLM-as-a-Judge](/concepts/llm-as-a-judge.md) — Semantic evaluation using LLM judges
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Continuous quality monitoring for deployed agents
- Supported Foundation Models — List of available models on Databricks
- Databricks OpenAI Client — The Python package for accessing Databricks-hosted LLMs

## Common Use Cases

### Application Development

Build AI applications using Databricks-hosted LLMs as the core reasoning engine:

- Question-answering assistants
- Conversational agents
- Customer support
- Content generation

### Evaluation and Monitoring

Use [Custom Judges](/concepts/custom-judges.md) and [[scorers]] to evaluate the quality of LLM responses:

- Automated quality assessment
- A/B comparison of different model versions
- [Trace-based analysis](/concepts/mlflow-trace-analysis.md) of agent behavior
- [Production Monitoring](/concepts/production-monitoring.md) for deployed applications

### Development Workflow

The code-based scorer development workflow allows rapid iteration:

1. Define evaluation data
2. Generate traces from the application
3. Store and analyze traces
4. Iterate on scorers using stored traces

## Sources

- develop-code-based-scorers-databricks-on-aws.md

# Citations

1. [develop-code-based-scorers-databricks-on-aws.md](/references/develop-code-based-scorers-databricks-on-aws-4fba7668.md)
