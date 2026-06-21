---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4fbe20dc03c4dbade13adc634ed0dbee3ec50f8007a105e3f5522a963dc83860
  pageDirectory: concepts
  sources:
    - automatic-tracing-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - auto-tracing-with-databricks-foundation-model-apis
    - AWDFMA
  citations:
    - file: automatic-tracing-databricks-on-aws.md
title: Auto-Tracing with Databricks Foundation Model APIs
description: Configuring OpenAI client to call Databricks Foundation Model APIs (e.g., Llama 4 Maverick) while mlflow.openai.autolog() automatically traces those calls using Databricks authentication.
tags:
  - databricks
  - foundation-model-apis
  - mlflow
  - tracing
timestamp: "2026-06-19T17:38:16.604Z"
---

# Auto-Tracing with Databricks Foundation Model APIs

**Auto-Tracing with Databricks Foundation Model APIs** enables automatic instrumentation of generative AI applications that use Databricks Foundation Model APIs, with a single line of code: `mlflow.<library>.autolog()`. This feature is part of [MLflow 3](/concepts/mlflow-3.md)'s GenAI tracing capabilities and works out-of-the-box with [over 20 supported libraries and frameworks](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/). ^[automatic-tracing-databricks-on-aws.md]

On serverless compute clusters, autologging for GenAI tracing frameworks is not automatically enabled. You must explicitly call the appropriate `mlflow.<library>.autolog()` function for the specific integration you want to trace. ^[automatic-tracing-databricks-on-aws.md]

## Prerequisites

Databricks recommends using MLflow 3 for the latest GenAI tracing capabilities. Install the required packages — for example, `mlflow[databricks]>=3.1` and `openai>=1.0.0` — and set any necessary LLM API keys (such as `OPENAI_API_KEY` or `DATABRICKS_TOKEN`). ^[automatic-tracing-databricks-on-aws.md]

## Basic Example

To trace calls to [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md) through the OpenAI client, enable `mlflow.openai.autolog()` and configure the OpenAI client with the Databricks host and token: ^[automatic-tracing-databricks-on-aws.md]

```python
import mlflow
import os
from openai import OpenAI

mlflow.set_tracking_uri("databricks")
mlflow.set_experiment("/Shared/databricks-sdk-autolog-example")

# Enable auto-tracing for OpenAI (which will trace Databricks Foundation Model API calls)
mlflow.openai.autolog()

# Create OpenAI client configured for Databricks
client = OpenAI(
    api_key=os.environ.get("DATABRICKS_TOKEN"),
    base_url=f"{os.environ.get('DATABRICKS_HOST')}/serving-endpoints"
)

# Query Llama 4 Maverick using OpenAI client
response = client.chat.completions.create(
    model="databricks-llama-4-maverick",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What are the key features of [[mlflow-tracing|MLflow Tracing]]?"}
    ],
    max_tokens=150,
    temperature=0.7
)

print(response.choices[0].message.content)
# Your calls to Databricks Foundation Model APIs are automatically traced!
```

All calls to Foundation Model APIs made through the OpenAI client are automatically captured as traces. ^[automatic-tracing-databricks-on-aws.md]

## Auto-Trace Multiple Frameworks

You can enable auto-tracing for multiple frameworks in the same agent (e.g., both OpenAI and LangChain), creating a single combined trace that includes direct API calls, LangChain chains, and custom logic. This makes debugging and monitoring easier. ^[automatic-tracing-databricks-on-aws.md]

```python
import mlflow
from langchain_openai import ChatOpenAI

mlflow.openai.autolog()
mlflow.langchain.autolog()
# ... subsequent code creates a trace spanning both frameworks
```

## Combine Manual and Automatic Tracing

Use the `@mlflow.trace` decorator alongside auto-tracing to add custom spans for business logic, intermediate computations, or multi-agent coordination. The resulting trace includes both auto-generated spans (from library calls) and your custom spans, giving full visibility into the application flow. ^[automatic-tracing-databricks-on-aws.md]

## Advanced Example: Multiple LLM Calls

Auto-tracing captures multiple LLM calls within a single workflow. For example, an application that first analyzes a query, then decides which model or prompt to use, will produce a trace with a parent span for the orchestrating function and child spans for each LLM call. ^[automatic-tracing-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The broader tracing framework for GenAI applications.
- [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md) – The serving endpoints for models like Llama 4.
- [Manual Tracing with Decorators](/concepts/mlflowtrace-decorator.md) – Adding custom spans with `@mlflow.trace`.
- [Automatic Tracing Integrations](/concepts/automatic-vs-manual-tracing-instrumentation.md) – The list of 20+ supported libraries.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – Compute environment note regarding autologging.

## Sources

- automatic-tracing-databricks-on-aws.md

# Citations

1. [automatic-tracing-databricks-on-aws.md](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
