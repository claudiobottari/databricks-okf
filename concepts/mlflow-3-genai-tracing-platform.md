---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aea1884fd511641fdc2135c50dcab817c9eaef10df80eecaff0a23401251a8f6
  pageDirectory: concepts
  sources:
    - automatic-tracing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3-genai-tracing-platform
    - M3GTP
  citations:
    - file: automatic-tracing-databricks-on-aws.md
title: MLflow 3 GenAI Tracing Platform
description: MLflow 3 provides the recommended platform for GenAI tracing with capabilities for automatic and manual tracing of LLM calls, spans, and multi-step workflows on Databricks.
tags:
  - mlflow
  - tracing
  - databricks
  - genai
timestamp: "2026-06-18T10:50:23.048Z"
---

# MLflow 3 GenAI Tracing Platform

**MLflow 3 GenAI Tracing Platform** is a built-in observability layer in MLflow 3 that records, visualizes, and debugs the execution of generative AI applications. By adding a single line of code—`mlflow.<library>.autolog()`—you can automatically trace calls to 20+ supported libraries and frameworks, capturing the full chain of LLM requests, responses, metadata, and custom logic without any manual instrumentation.^[automatic-tracing-databricks-on-aws.md]

## Automatic tracing overview

Automatic tracing works with integrations including OpenAI, LangChain, Anthropic, Mistral, and many others. When enabled, MLflow captures each LLM API call as a span within a trace, recording inputs, outputs, latency, token usage, and errors. These traces are viewable in the MLflow UI and can be associated with experiments for model comparison and debugging.^[automatic-tracing-databricks-on-aws.md]

On serverless compute clusters, autologging for GenAI tracing frameworks is not automatically enabled. You must explicitly call the appropriate `mlflow.<library>.autolog()` function for the specific integrations you want to trace.^[automatic-tracing-databricks-on-aws.md]

## Prerequisites

MLflow 3 is recommended for the latest GenAI tracing capabilities. To get started, install the core package and any integration packages you need:^[automatic-tracing-databricks-on-aws.md]

```python
%pip install --upgrade "mlflow[databricks]>=3.1" openai>=1.0.0
dbutils.library.restartPython()
```

In a Databricks notebook, set the necessary API keys as environment variables:^[automatic-tracing-databricks-on-aws.md]

```python
import os
os.environ["OPENAI_API_KEY"] = "your-api-key"
```

## Basic automatic tracing example

The following example enables automatic tracing for OpenAI and uses the client to query a Databricks Foundation Model API endpoint. All calls are automatically traced.^[automatic-tracing-databricks-on-aws.md]

```python
import mlflow
import os
from openai import OpenAI

mlflow.set_tracking_uri("databricks")
mlflow.set_experiment("/Shared/databricks-sdk-autolog-example")

# Enable auto-tracing for OpenAI
mlflow.openai.autolog()

client = OpenAI(
    api_key=os.environ.get("DATABRICKS_TOKEN"),
    base_url=f"{os.environ.get('DATABRICKS_HOST')}/serving-endpoints"
)

response = client.chat.completions.create(
    model="databricks-llama-4-maverick",
    messages=[{"role": "user", "content": "What are the key features of [[mlflow-tracing|MLflow Tracing]]?"}]
)
```

## Auto-trace multiple frameworks

You can enable tracing for several frameworks in a single agent. The example below combines direct OpenAI API calls with a LangChain chain and custom logic, all merged into one trace.^[automatic-tracing-databricks-on-aws.md]

```python
mlflow.openai.autolog()
mlflow.langchain.autolog()

@mlflow.trace(span_type=SpanType.CHAIN)
def multi_provider_workflow(query):
    # Direct OpenAI call
    analysis = client.chat.completions.create( ... )
    # LangChain chain
    chain = prompt | llm
    response = chain.invoke({"topics": topics, "query": query})
    return response
```

## Combine manual and automatic tracing

Use the `@mlflow.trace` decorator alongside automatic tracing to create unified traces that include custom business logic, helper functions, or multi-agent orchestration. The decorator can be applied to any function to create a span that nests automatically traced LLM calls as children.^[automatic-tracing-databricks-on-aws.md]

```python
@mlflow.trace(span_type=SpanType.CHAIN)
def run(question):
    messages = build_messages(question)
    response = client.chat.completions.create(...)  # automatically traced
    return parse_response(response)

@mlflow.trace
def build_messages(question):
    return [{"role": "system", "content": "..."}, {"role": "user", "content": question}]

@mlflow.trace
def parse_response(response):
    return response.choices[0].message.content
```

This pattern is useful for [multi-agent systems](/concepts/multi-model-strategy-in-agent-systems.md), custom logic between LLM calls, and workflows that span multiple providers.^[automatic-tracing-databricks-on-aws.md]

## Advanced example: multiple LLM calls

The following pattern traces a sequential decision-making pipeline: one LLM call to analyze a query, followed by a second LLM call that chooses a model or system prompt based on the analysis. MLflow captures both calls as child spans under a single parent span.^[automatic-tracing-databricks-on-aws.md]

```python
@mlflow.trace(span_type=SpanType.CHAIN)
def process_user_query(query):
    analysis = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "Analyze the query..."}]
    )
    if "factual" in analysis.choices[0].message.content.lower():
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": "Provide a factual response."}]
        )
    else:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": "Provide a creative response."}]
        )
    return response.choices[0].message.content
```

## Related concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) — Core experiment logging and management
- [MLflow 3](/concepts/mlflow-3.md) — The major version introducing GenAI tracing
- [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md) — Served endpoints that can be traced
- LangChain — Framework with supported automatic tracing
- [GenAI Tracing](/concepts/mlflow-genai-tracing.md) — The broader capability for observing generative AI applications
- [Automatic tracing integrations](/concepts/automatic-vs-manual-tracing-instrumentation.md) — The 20+ libraries and frameworks supported out of the box

## Sources

- automatic-tracing-databricks-on-aws.md

# Citations

1. [automatic-tracing-databricks-on-aws.md](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
