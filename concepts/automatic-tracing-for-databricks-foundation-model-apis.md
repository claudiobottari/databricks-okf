---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5f65dcc42d15c175de70f01518b4f50b192f93ec29bd1b3c9b212c55426fc860
  pageDirectory: concepts
  sources:
    - automatic-tracing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automatic-tracing-for-databricks-foundation-model-apis
    - ATFDFMA
  citations:
    - file: automatic-tracing-databricks-on-aws.md
title: Automatic Tracing for Databricks Foundation Model APIs
description: Using mlflow.openai.autolog() to trace calls to Databricks Foundation Model APIs via the OpenAI-compatible endpoint.
tags:
  - mlflow
  - databricks
  - foundation-model-apis
timestamp: "2026-06-19T09:06:11.709Z"
---

# Automatic Tracing for Databricks Foundation Model APIs

**Automatic Tracing for Databricks Foundation Model APIs** enables you to instrument your generative AI applications with a single line of code — `mlflow.<library>.autolog()` — to automatically capture traces of calls to [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md) and other LLM providers. This functionality is part of [MLflow 3](/concepts/mlflow-3.md)'s [GenAI Tracing](/concepts/mlflow-genai-tracing.md) capabilities and works with [20+ supported libraries and frameworks](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/) out of the box. ^[automatic-tracing-databricks-on-aws.md]

## Overview

Automatic tracing captures the full execution flow of LLM interactions, including model calls, input/output payloads, and latency metrics. When using Databricks Foundation Model APIs via the OpenAI Python client, setting up automatic tracing requires calling `mlflow.openai.autolog()` before making any API calls. The traces are then visible in the [MLflow Experiment](/concepts/mlflow-experiment.md) UI for debugging, monitoring, and optimization. ^[automatic-tracing-databricks-on-aws.md]

On serverless compute clusters, autologging for GenAI tracing frameworks is **not automatically enabled**. You must explicitly enable autologging by calling the appropriate `mlflow.<library>.autolog()` function for the specific integrations you want to trace. ^[automatic-tracing-databricks-on-aws.md]

## Prerequisites

Databricks recommends MLflow 3 for the latest GenAI tracing capabilities. The minimal installation requires: ^[automatic-tracing-databricks-on-aws.md]

```bash
%pip install --upgrade "mlflow[databricks]>=3.1" openai>=1.0.0
```

Additional libraries (such as `langchain`, `anthropic`, etc.) must be installed for their respective integrations. After installation, call `dbutils.library.restartPython()` to reload the environment. ^[automatic-tracing-databricks-on-aws.md]

LLM API keys must be configured in the environment before tracing:

```python
import os
os.environ["OPENAI_API_KEY"] = "your-api-key"
```

^[automatic-tracing-databricks-on-aws.md]

## Enabling Tracing for Databricks Foundation Model APIs

The following example demonstrates how to enable automatic tracing for OpenAI agents connecting to Databricks Foundation Model APIs: ^[automatic-tracing-databricks-on-aws.md]

```python
import mlflow
import os
from openai import OpenAI

# Databricks Foundation Model APIs use Databricks authentication.
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

## Multi-Framework Auto-Tracing

You can auto-trace multiple frameworks simultaneously within the same agent. This is useful for applications that combine direct OpenAI API calls with LangChain chains and custom logic, producing a single unified trace for debugging. ^[automatic-tracing-databricks-on-aws.md]

```python
import mlflow
import openai
from mlflow.entities import SpanType
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Enable auto-tracing for both OpenAI and LangChain
mlflow.openai.autolog()
mlflow.langchain.autolog()

# (Proceed with mixed OpenAI + LangChain calls...)
```

## Combining Manual and Automatic Tracing

Use `@mlflow.trace` decorators alongside auto-tracing to capture custom business logic as part of the same trace. This pattern is valuable for scenarios involving multiple LLM calls, multi-agent systems with different providers, or custom logic between LLM calls. ^[automatic-tracing-databricks-on-aws.md]

```python
import mlflow
import openai
from mlflow.entities import SpanType

mlflow.openai.autolog()

client = openai.OpenAI()

@mlflow.trace(span_type=SpanType.CHAIN)
def run(question):
    messages = build_messages(question)
    # MLflow automatically generates a span for OpenAI invocation
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=100,
        messages=messages,
    )
    return parse_response(response)

@mlflow.trace
def build_messages(question):
    return [
        {"role": "system", "content": "You are a helpful chatbot."},
        {"role": "user", "content": question},
    ]

@mlflow.trace
def parse_response(response):
    return response.choices[0].message.content

run("What is MLflow?")
```

This creates a single trace with a parent span for `run()` and child spans for `build_messages()`, the OpenAI call, and `parse_response()`. ^[automatic-tracing-databricks-on-aws.md]

## Advanced Usage: Multiple LLM Calls in a Workflow

Automatic tracing captures multiple LLM calls within a single workflow. For example, an agent that first analyzes a query with one model call and then generates a response based on that analysis will produce a trace with a parent span and multiple child spans for each LLM invocation. ^[automatic-tracing-databricks-on-aws.md]

## Related Concepts

- [MLflow 3](/concepts/mlflow-3.md) — The MLflow version required for GenAI Tracing
- [GenAI Tracing](/concepts/mlflow-genai-tracing.md) — The tracing framework underlying automatic instrumentation
- [Manual Tracing with Decorators](/concepts/mlflowtrace-decorator.md) — Adding custom spans alongside auto-traced calls
- [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md) — The serving endpoints traced by this integration
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Where traces are stored and visualized
- [OpenAI API Compatibility](/concepts/ollama-openai-api-compatibility.md) — How Databricks Foundation Model APIs expose an OpenAI-compatible interface

## Sources

- automatic-tracing-databricks-on-aws.md

# Citations

1. [automatic-tracing-databricks-on-aws.md](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
