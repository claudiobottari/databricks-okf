---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: abf078c78f482eb0ca1f7e41a9a7d85c04698469bdbf8d84bb6e81060c3d1d48
  pageDirectory: concepts
  sources:
    - automatic-tracing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflowautolog-for-generative-ai-tracing
    - MFGAT
  citations:
    - file: automatic-tracing-databricks-on-aws.md
title: mlflow.autolog() for Generative AI Tracing
description: One-line automatic tracing of generative AI applications using mlflow.<library>.autolog(), supporting 20+ frameworks out of the box.
tags:
  - mlflow
  - tracing
  - generative-ai
timestamp: "2026-06-19T09:05:38.553Z"
---

# `mlflow.autolog()` for Generative AI Tracing

The `mlflow.autolog()` family of functions provides one-line automatic instrumentation for generative AI applications that use supported libraries. By calling `mlflow.<library>.autolog()`, MLflow captures traces of LLM calls, agent workflows, and other model interactions without requiring manual span creation. This enables debugging, monitoring, and performance analysis of GenAI applications with minimal code changes.^[automatic-tracing-databricks-on-aws.md]

Automatic tracing works out of the box with [20+ supported libraries and frameworks](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/), including OpenAI, LangChain, Anthropic, and Mistral. Each integration provides zero-configuration capture of the library’s API calls, including request payloads, response content, and latency metrics.^[automatic-tracing-databricks-on-aws.md]

> **Note:** On serverless compute clusters, autologging for GenAI tracing frameworks is not automatically enabled. You must explicitly call the appropriate `mlflow.<library>.autolog()` function for each integration you want to trace.^[automatic-tracing-databricks-on-aws.md]

## Prerequisites

Databricks recommends MLflow 3 for the latest GenAI tracing capabilities. To get started, install the core MLflow package with Databricks support and any integration-specific SDKs you plan to trace:

```python
%pip install --upgrade "mlflow[databricks]>=3.1" openai>=1.0.0
# Also install other libraries you want to trace (langchain, anthropic, etc.)
dbutils.library.restartPython()
```

^[automatic-tracing-databricks-on-aws.md]

You also need to configure credentials for the LLM providers you use. In a Databricks notebook, set API keys as environment variables:

```python
import os
os.environ["OPENAI_API_KEY"] = "your-api-key"
# os.environ["ANTHROPIC_API_KEY"] = "your-api-key"
# os.environ["MISTRAL_API_KEY"] = "your-api-key"
```

^[automatic-tracing-databricks-on-aws.md]

## Enabling automatic tracing

Call `mlflow.openai.autolog()` (or the equivalent for your library) before making any LLM calls. The following example enables automatic tracing for OpenAI calls made through the Databricks Foundation Model APIs:

```python
import mlflow
from openai import OpenAI

mlflow.set_tracking_uri("databricks")
mlflow.set_experiment("/Shared/databricks-sdk-autolog-example")

mlflow.openai.autolog()       # Enable auto-tracing for OpenAI

client = OpenAI(
    api_key=os.environ.get("DATABRICKS_TOKEN"),
    base_url=f"{os.environ.get('DATABRICKS_HOST')}/serving-endpoints"
)

response = client.chat.completions.create(
    model="databricks-llama-4-maverick",
    messages=[...],
    max_tokens=150,
    temperature=0.7
)
```

^[automatic-tracing-databricks-on-aws.md]

## Tracing multiple frameworks

You can auto-trace multiple frameworks in the same agent. For example, to trace both OpenAI and LangChain calls:

```python
mlflow.openai.autolog()
mlflow.langchain.autolog()
```

After enabling both integrations, any OpenAI API call and any LangChain chain invocation in the same process will be captured in a single trace.^[automatic-tracing-databricks-on-aws.md]

## Combining manual and automatic tracing

Use `@mlflow.trace` alongside automatic tracing to add custom spans for business logic, data transformation, or multi-step orchestration. The manually created spans appear in the same trace as the auto‑traced LLM calls, giving you a unified view of the entire workflow.^[automatic-tracing-databricks-on-aws.md]

```python
import mlflow
from mlflow.entities import SpanType

mlflow.openai.autolog()

@mlflow.trace(span_type=SpanType.CHAIN)
def run(question):
    messages = build_messages(question)
    response = client.chat.completions.create(...)
    return parse_response(response)

@mlflow.trace
def build_messages(question): ...

@mlflow.trace
def parse_response(response): ...
```

^[automatic-tracing-databricks-on-aws.md]

## Advanced example: multiple LLM calls

When your application makes several LLM calls in sequence (e.g., first analyzing a query, then generating a response based on that analysis), automatic tracing captures each call as a child span under a parent span you define with `@mlflow.trace`. This pattern makes it easy to inspect the full decision chain in the trace viewer.^[automatic-tracing-databricks-on-aws.md]

## Next steps

- Explore all [supported integrations](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/) for automatic tracing.
- Learn about manual tracing with decorators to capture custom business logic alongside auto‑traced LLM calls.
- See how to combine [MLflow Tracing](/concepts/mlflow-tracing.md) with [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md).

## Sources

- automatic-tracing-databricks-on-aws.md

# Citations

1. [automatic-tracing-databricks-on-aws.md](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
