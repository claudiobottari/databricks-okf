---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: efa36841dfa2faaacbd60a58721800c3403fc84bf217b1d8e0175d1324564e6d
  pageDirectory: concepts
  sources:
    - automatic-tracing-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - auto-tracing-for-sequential-llm-calls
    - AFSLC
  citations:
    - file: automatic-tracing-databricks-on-aws.md
title: Auto-Tracing for Sequential LLM Calls
description: How MLflow automatic tracing captures multiple sequential LLM calls within a single workflow, creating a parent span with child spans for each OpenAI invocation.
tags:
  - mlflow
  - tracing
  - workflows
  - llm
timestamp: "2026-06-19T17:38:08.935Z"
---

# Auto-Tracing for Sequential LLM Calls

**Auto-Tracing for Sequential LLM Calls** refers to the automatic capture and visualization of multiple successive large language model (LLM) invocations within a single workflow using [MLflow Tracing](/concepts/mlflow-tracing.md). When enabled via `mlflow.<library>.autolog()`, the tracing system automatically generates [Spans|Trace Span](/concepts/trace-spans.md) for each LLM call, organizing them hierarchically under a parent span to provide a unified view of the entire processing pipeline. ^[automatic-tracing-databricks-on-aws.md]

## Overview

Sequential LLM call patterns are common in applications where a system needs to make intermediate decisions — such as analyzing a query first and then generating a response based on that analysis. Auto-tracing captures each call in the sequence as a child span within the same trace, making it possible to debug and monitor the chain of reasoning. ^[automatic-tracing-databricks-on-aws.md]

## Enabling Auto-Tracing for Sequential Workflows

To enable auto-tracing for sequential LLM calls, call the appropriate `mlflow.<library>.autolog()` function before making any LLM invocations. The following example demonstrates sequential calls using OpenAI: ^[automatic-tracing-databricks-on-aws.md]

```python
import mlflow
import openai
from mlflow.entities import SpanType

mlflow.openai.autolog()

client = openai.OpenAI()

@mlflow.trace(span_type=SpanType.CHAIN)
def process_user_query(query: str):
    # First LLM call: Analyze the query
    analysis = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Analyze the user's query and determine if it requires factual information or creative writing."},
            {"role": "user", "content": query}
        ]
    )
    analysis_result = analysis.choices[0].message.content

    # Second LLM call: Generate response based on analysis
    if "factual" in analysis_result.lower():
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Provide a factual, well-researched response."},
                {"role": "user", "content": query}
            ]
        )
    else:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Provide a creative, engaging response."},
                {"role": "user", "content": query}
            ]
        )
    return response.choices[0].message.content

result = process_user_query("Tell me about the history of artificial intelligence")
```

This produces a single trace with:
- A parent span for `process_user_query`
- Two child spans for the OpenAI calls ^[automatic-tracing-databricks-on-aws.md]

## Combining Manual and Automatic Tracing

You can use `@mlflow.trace` decorators alongside auto-tracing to create unified traces that capture both automatic LLM spans and custom business logic. This is useful for:

- Multi-LLM call workflows
- Multi-agent systems with different providers
- Custom logic between LLM calls ^[automatic-tracing-databricks-on-aws.md]

```python
@mlflow.trace(span_type=SpanType.CHAIN)
def run(question):
    messages = build_messages(question)
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
```

## Differences from Distributed Tracing

Unlike distributed tracing, which tracks requests across service boundaries, auto-tracing for sequential LLM calls captures calls within a single process or notebook session. It is designed for the common pattern of chaining multiple LLM invocations together in a script or application. ^[automatic-tracing-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The underlying tracing framework for capturing and visualizing LLM calls.
- [Manual Tracing with Decorators](/concepts/mlflowtrace-decorator.md) – Adding custom spans to capture business logic.
- [Supported Tracing Integrations](/concepts/mlflow-supported-tracing-libraries.md) – 20+ libraries and frameworks supported for auto-tracing.
- [Serverless Compute and Autologging](/concepts/serverless-compute-autologging-requirement.md) – Notes on explicit enabling required for serverless environments.
- Trace Visualization – Viewing and analyzing traces in the Databricks UI.

## Sources

- automatic-tracing-databricks-on-aws.md

# Citations

1. [automatic-tracing-databricks-on-aws.md](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
