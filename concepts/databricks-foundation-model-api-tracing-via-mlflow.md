---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1376027fddc561f4b7a9fe5ec71f40475b826bbdcb417ff1883e1bad4567c9c9
  pageDirectory: concepts
  sources:
    - automatic-tracing-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-foundation-model-api-tracing-via-mlflow
    - DFMATVM
    - databricks-foundation-model-api-tracing-via-openai-client
    - DFMATVOC
  citations:
    - file: automatic-tracing-databricks-on-aws.md
title: Databricks Foundation Model API Tracing via MLflow
description: Using MLflow's OpenAI autolog to trace calls to Databricks Foundation Model APIs by configuring an OpenAI client with Databricks host and token, then querying models like Llama 4 Maverick.
tags:
  - databricks
  - foundation-model-apis
  - mlflow
  - openai
  - tracing
timestamp: "2026-06-19T14:06:31.386Z"
---

# Databricks Foundation Model API Tracing via MLflow

**Databricks Foundation Model API Tracing via MLflow** enables automatic instrumentation of LLM calls made through the Databricks Foundation Model API by using MLflow's `autolog()` functions. With a single line of code, every invocation of supported frameworks — such as OpenAI's SDK configured for Databricks — is automatically captured as a trace, providing observability into model inputs, outputs, and latency. ^[automatic-tracing-databricks-on-aws.md]

## Overview

MLflow's [Automatic Tracing](/concepts/automatic-tracing.md) works with over 20 supported libraries and frameworks out of the box. On a Databricks workspace, you can use it to trace calls to Databricks Foundation Model APIs by configuring the OpenAI client to point to the Databricks serving endpoint and then enabling `mlflow.openai.autolog()`. ^[automatic-tracing-databricks-on-aws.md]

By default, serverless compute clusters do **not** enable autologging for GenAI tracing frameworks — you must explicitly call the appropriate `mlflow.<library>.autolog()` function for the integrations you want to trace. ^[automatic-tracing-databricks-on-aws.md]

## Prerequisites

- **MLflow 3 or later**: Install `mlflow[databricks]>=3.1` to get core MLflow functionality with GenAI features and Databricks connectivity.
- **OpenAI SDK `>=1.0.0`** (if using the OpenAI‑compatible Databricks endpoint).
- **Additional SDKs** for any other frameworks you wish to trace (e.g., LangChain, Anthropic).

```python
%pip install --upgrade "mlflow[databricks]>=3.1" openai>=1.0.0
# Also install libraries you want to trace (langchain, anthropic, etc.)
dbutils.library.restartPython()
```

^[automatic-tracing-databricks-on-aws.md]

## Enabling Tracing for Databricks Foundation Model API

1. **Set the tracking URI and experiment** (recommended) using `mlflow.set_tracking_uri("databricks")` and `mlflow.set_experiment(...)`.
2. **Enable OpenAI autologging** with `mlflow.openai.autolog()`.
3. **Create an OpenAI client** configured with your Databricks host and token, and use the Databricks serving endpoint as the base URL.
4. **Make a chat completion call** to a Foundation Model (e.g., `databricks-llama-4-maverick`). The request and response are automatically traced.

The following example demonstrates the full workflow:

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
```

^[automatic-tracing-databricks-on-aws.md]

## Combining Multiple Frameworks

You can autolog multiple frameworks in the same agent. For example, enabling both `mlflow.openai.autolog()` and `mlflow.langchain.autolog()` allows traces to capture direct OpenAI calls, LangChain chains, and any custom logic — all merged into a single trace. ^[automatic-tracing-databricks-on-aws.md]

## Mixing Manual and Automatic Tracing

Use the `@mlflow.trace` decorator alongside `autolog()` to add custom spans for business logic that sits between LLM calls. This creates a unified trace that includes both the automatically generated spans for the foundation model calls and the manually instrumented steps. ^[automatic-tracing-databricks-on-aws.md]

## Advanced Example: Multiple LLM Calls

When your application makes sequential LLM calls (e.g., first analyzing a query, then generating a response), automatic tracing captures each call as a child span under a parent span you define. The example below shows two separate OpenAI calls traced within a single workflow:

```python
@mlflow.trace(span_type=SpanType.CHAIN)
def process_user_query(query: str):
    # First LLM call: Analyze the query
    analysis = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[...]
    )
    analysis_result = analysis.choices[0].message.content

    # Second LLM call: Generate response based on analysis
    if "factual" in analysis_result.lower():
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[...]
        )
    else:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[...]
        )
    return response.choices[0].message.content
```

^[automatic-tracing-databricks-on-aws.md]

## Related Concepts

- [Automatic Tracing](/concepts/automatic-tracing.md) – The general mechanism for instrumenting supported libraries.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – The overall tracing infrastructure in MLflow.
- [OpenAI autolog](/concepts/mlflow-openai-autolog.md) – The specific autolog function for OpenAI SDK.
- [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md) – The managed model endpoints traceable with this approach.
- [Manual Tracing](/concepts/manual-tracing.md) – Adding custom spans with `@mlflow.trace`.

## Sources

- automatic-tracing-databricks-on-aws.md

# Citations

1. [automatic-tracing-databricks-on-aws.md](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
