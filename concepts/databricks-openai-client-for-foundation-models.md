---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0ab05c4e64064f4512b44dc764f35e3da2da57df70a59f01156470e0361abb84
  pageDirectory: concepts
  sources:
    - get-started-mlflow-3-for-genai-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-openai-client-for-foundation-models
    - DOCFFM
  citations:
    - file: get-started-mlflow-3-for-genai-databricks-on-aws.md
    - file: get-started-mlflow-3-for-genai-databricks-on-aws.md
      start: 34
      end: 39
    - file: get-started-mlflow-3-for-genai-databricks-on-aws.md
      start: 34
      end: 50
title: Databricks OpenAI Client for Foundation Models
description: The databricks-openai package provides an OpenAI-compatible API client for calling Databricks-hosted Foundation Model endpoints, enabling standard OpenAI SDK patterns against Databricks models.
tags:
  - databricks
  - openai
  - foundation-models
  - llm
timestamp: "2026-06-19T18:59:07.422Z"
---

# Databricks OpenAI Client for Foundation Models

The **Databricks OpenAI Client for Foundation Models** is a Python package (`databricks-openai`) that provides an OpenAI-compatible API client for calling Foundation Models on Databricks. It allows you to use the familiar OpenAI SDK interface to interact with Databricks-hosted large language models (LLMs), such as `databricks-claude-sonnet-4`, without needing to switch to a different client library. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]^[get-started-mlflow-3-for-genai-databricks-on-aws.md#L34-L39]

## Installation

Install the package with `pip`:

```python
%pip install databricks-openai
```

For use with [MLflow GenAI](/concepts/mlflow-3-for-genai.md) tracing and evaluation, it is recommended to also install `mlflow[databricks]`:

```python
%pip install -qq --upgrade "mlflow[databricks]>=3.1.0" databricks-openai
```

^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Usage

Import and instantiate the client, then call a Databricks-hosted model using the standard OpenAI chat completions API.

```python
from databricks_openai import DatabricksOpenAI

client = DatabricksOpenAI()

response = client.chat.completions.create(
    model="databricks-claude-sonnet-4",  # Replace with your Databricks model endpoint name
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"},
    ],
)
print(response.choices[0].message.content)
```

^[get-started-mlflow-3-for-genai-databricks-on-aws.md#L34-L50]

The client automatically routes requests to the Databricks serving endpoint that corresponds to the model name you specify (e.g., `databricks-claude-sonnet-4`). No additional API keys or endpoint URLs are required when running inside a Databricks workspace. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Integration with [MLflow Tracing](/concepts/mlflow-tracing.md)

When used together with MLflow, you can enable automatic tracing of OpenAI calls by calling `mlflow.openai.autolog()` before making requests. This logs request details, response content, token counts, and latency to the active [MLflow Experiment](/concepts/mlflow-experiment.md) as a trace. Tracing helps with debugging, performance analysis, and downstream evaluation. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

```python
import mlflow

mlflow.openai.autolog()
# The client calls will now be automatically traced.
```

^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Supported Models

The client can call any [Foundation Models on Databricks|Databricks Foundation Model](/concepts/foundation-models-apis-on-databricks.md) or custom model endpoint deployed to a Databricks serving endpoint. The model identifier passed to `client.chat.completions.create(model=...)` should match the endpoint name in your Databricks workspace. The example above uses `databricks-claude-sonnet-4`, a Databricks-managed Claude model. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Benefits

- **Standard OpenAI interface** – reduces learning curve when moving from OpenAI to Databricks-hosted models.
- **Works seamlessly in Databricks notebooks** – no additional authentication steps needed.
- **Tracing and evaluation** – integrates natively with [MLflow GenAI](/concepts/mlflow-3-for-genai.md) for monitoring and quality assessment.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md)
- Foundation Models on Databricks
- [MLflow experiments](/concepts/mlflow-experiment.md)
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md)

## Sources

- get-started-mlflow-3-for-genai-databricks-on-aws.md

# Citations

1. [get-started-mlflow-3-for-genai-databricks-on-aws.md](/references/get-started-mlflow-3-for-genai-databricks-on-aws-4186f156.md)
2. [get-started-mlflow-3-for-genai-databricks-on-aws.md:34-39](/references/get-started-mlflow-3-for-genai-databricks-on-aws-4186f156.md)
3. [get-started-mlflow-3-for-genai-databricks-on-aws.md:34-50](/references/get-started-mlflow-3-for-genai-databricks-on-aws-4186f156.md)
