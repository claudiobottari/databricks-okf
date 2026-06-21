---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 117a7b3780d70ceccea9ca7f01d613b9c25fc627453aeb317318ea9f1c42b1be
  pageDirectory: concepts
  sources:
    - automatic-tracing-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - combining-manual-and-automatic-tracing-in-mlflow
    - Automatic Tracing in MLflow and Combining Manual
    - CMAATIM
  citations:
    - file: automatic-tracing-databricks-on-aws.md
title: Combining Manual and Automatic Tracing in MLflow
description: Using @mlflow.trace decorators alongside mlflow.autolog() to create unified traces that capture both automatic LLM calls and custom business logic as a single trace hierarchy.
tags:
  - mlflow
  - tracing
  - manual-instrumentation
  - patterns
timestamp: "2026-06-19T17:37:47.100Z"
---

# Combining Manual and Automatic Tracing in MLflow

**Combining Manual and Automatic Tracing in MLflow** refers to the practice of using both `@mlflow.trace` decorators and `mlflow.<library>.autolog()` functions together to create comprehensive, unified traces of generative AI application execution. This hybrid approach captures both framework-level LLM calls and custom application logic within a single trace, providing full visibility into complex workflows.^[automatic-tracing-databricks-on-aws.md]

## Overview

Automatic tracing uses `mlflow.<library>.autolog()` to instrument supported frameworks (such as OpenAI, LangChain, and others) without requiring manual instrumentation on each call. Manual tracing uses the `@mlflow.trace` decorator to instrument custom functions and business logic. When combined, both types of instrumentation integrate into the same trace hierarchy, enabling end-to-end observability of multi-component agent systems.^[automatic-tracing-databricks-on-aws.md]

MLflow 3 is recommended for the latest [GenAI tracing](/concepts/mlflow-genai-tracing.md) capabilities.^[automatic-tracing-databricks-on-aws.md]

## Why Combine Both Approaches

Combining manual and automatic tracing addresses these common scenarios:^[automatic-tracing-databricks-on-aws.md]

- **Multiple LLM calls in one workflow** — Automatically trace each provider call while manually tracing the overall orchestration logic.
- **Multi-agent systems with different providers** — Auto-trace different frameworks (OpenAI, LangChain, Anthropic) while adding manual spans for coordination logic.
- **Custom logic between LLM calls** — Use manual spans to instrument data transformation, validation, or routing logic that occurs between framework calls.

## How It Works

When you enable autologging for one or more frameworks and also decorate custom functions with `@mlflow.trace`, MLflow combines all spans into a single trace. The trace hierarchy respects the call order and nesting of both manual and automatic spans.^[automatic-tracing-databricks-on-aws.md]

The `@mlflow.trace` decorator can specify a `span_type` from `mlflow.entities.SpanType`, such as `SpanType.CHAIN`, to categorize the span. This helps differentiate manual workflow spans from automatic LLM invocation spans in the trace visualization.^[automatic-tracing-databricks-on-aws.md]

## Basic Example

The following example enables automatic tracing for OpenAI and adds manual spans for the overall workflow and helper functions:^[automatic-tracing-databricks-on-aws.md]

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

Running this code generates a single trace combining:
- The manual span for the `run` function
- Manual spans for `build_messages` and `parse_response`
- An automatic span for the OpenAI API call

## Multi-Framework Example

Auto-tracing can be enabled for multiple frameworks simultaneously, and manual spans can wrap the combined workflow:^[automatic-tracing-databricks-on-aws.md]

```python
import mlflow
import openai
from mlflow.entities import SpanType
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

mlflow.openai.autolog()
mlflow.langchain.autolog()

client = openai.OpenAI()

@mlflow.trace(span_type=SpanType.CHAIN)
def multi_provider_workflow(query: str):
    # OpenAI call is auto-traced
    analysis = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Analyze the query and extract key topics."},
            {"role": "user", "content": query}
        ]
    )
    topics = analysis.choices[0].message.content
    
    # LangChain call is auto-traced
    llm = ChatOpenAI(model="gpt-4o-mini")
    prompt = ChatPromptTemplate.from_template(
        "Based on these topics: {topics}\nGenerate a detailed response to: {query}"
    )
    chain = prompt | llm
    response = chain.invoke({"topics": topics, "query": query})
    return response

result = multi_provider_workflow("Explain quantum computing")
```

## Multiple LLM Calls Example

A common pattern is making sequential decisions with multiple LLM calls in a single workflow. Automatic tracing captures each invocation as a child span under the manual parent span:^[automatic-tracing-databricks-on-aws.md]

```python
import mlflow
import openai
from mlflow.entities import SpanType

mlflow.openai.autolog()

client = openai.OpenAI()

@mlflow.trace(span_type=SpanType.CHAIN)
def process_user_query(query: str):
    # First LLM call: Analyze the query (auto-traced)
    analysis = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Analyze the user's query and determine if it requires factual information or creative writing."},
            {"role": "user", "content": query}
        ]
    )
    analysis_result = analysis.choices[0].message.content
    
    # Second LLM call: Generate response based on analysis (auto-traced)
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
- One parent span for `process_user_query`
- Two child spans for the OpenAI calls

## Serverless Compute Note

On serverless compute clusters, autologging for GenAI tracing frameworks is not automatically enabled. You must explicitly call the appropriate `mlflow.<library>.autolog()` function for each integration you want to trace.^[automatic-tracing-databricks-on-aws.md]

## Related Concepts

- [Automatic Tracing](/concepts/automatic-tracing.md) — Automated instrumentation for supported frameworks
- [Manual Tracing](/concepts/manual-tracing.md) — Using `@mlflow.trace` decorators for custom code
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The overall tracing infrastructure in MLflow
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — MLflow's capabilities for generative AI applications
- [Supported Tracing Integrations](/concepts/mlflow-supported-tracing-libraries.md) — The 20+ libraries compatible with automatic tracing
- Span Types — Categorization of spans in the trace hierarchy

## Sources

- automatic-tracing-databricks-on-aws.md

# Citations

1. [automatic-tracing-databricks-on-aws.md](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
