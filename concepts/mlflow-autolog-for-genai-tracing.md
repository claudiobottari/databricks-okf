---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1bec0c8c68416ca481fc02af7c364c3939f4009b5629f5da1b6bcf730d78728c
  pageDirectory: concepts
  sources:
    - automatic-tracing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-autolog-for-genai-tracing
    - MAFGT
  citations:
    - file: automatic-tracing-databricks-on-aws.md
title: MLflow Autolog for GenAI Tracing
description: A single-line code pattern (mlflow.<library>.autolog()) that automatically traces generative AI applications across 20+ supported libraries and frameworks.
tags:
  - mlflow
  - tracing
  - generative-ai
  - instrumentation
timestamp: "2026-06-19T14:06:20.217Z"
---

# MLflow Autolog for GenAI Tracing

**MLflow Autolog for GenAI Tracing** refers to the mechanism by which MLflow automatically instruments and traces calls to supported generative AI libraries and frameworks with a single line of code. By calling `mlflow.<library>.autolog()`, developers can capture detailed execution traces — including LLM invocations, tool calls, and intermediate steps — without modifying application logic. ^[automatic-tracing-databricks-on-aws.md]

## Overview

Autologging is the simplest way to enable GenAI tracing in MLflow. A single call to `mlflow.<library>.autolog()` activates automatic instrumentation for over 20 supported libraries and frameworks out of the box. Once enabled, every call to the instrumented library is automatically captured as a span within a trace, giving developers visibility into model inputs, outputs, latency, and errors. ^[automatic-tracing-databricks-on-aws.md]

Autologging works with both manual tracing via the `@mlflow.trace` decorator and other automatic tracing integrations, allowing teams to create unified traces that capture custom business logic alongside auto-instrumented LLM calls. ^[automatic-tracing-databricks-on-aws.md]

## Prerequisites

### MLflow Version

Databricks recommends MLflow 3 for the latest GenAI tracing capabilities. The core package requirement is `mlflow[databricks]>=3.1`, which includes GenAI features and Databricks connectivity. ^[automatic-tracing-databricks-on-aws.md]

### Installation

Install the base requirements and any integration-specific libraries you plan to trace:

```python
%pip install --upgrade "mlflow[databricks]>=3.1" openai>=1.0.0
# Also install libraries you want to trace (langchain, anthropic, etc.)
dbutils.library.restartPython()
```

^[automatic-tracing-databricks-on-aws.md]

### Credential Configuration

In a Databricks notebook, set any necessary LLM API keys as environment variables before making traced calls:

```python
import os
os.environ["OPENAI_API_KEY"] = "your-api-key"
# os.environ["ANTHROPIC_API_KEY"] = "your-api-key"
# os.environ["MISTRAL_API_KEY"] = "your-api-key"
```

^[automatic-tracing-databricks-on-aws.md]

## Enabling Autologging

### Basic Usage

To enable automatic tracing for a specific library, call its autolog function before making any calls through that library. For example, to trace OpenAI client calls including those routed through [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md):

```python
import mlflow
import os
from openai import OpenAI

mlflow.set_tracking_uri("databricks")
mlflow.set_experiment("/Shared/databricks-sdk-autolog-example")

mlflow.openai.autolog()

client = OpenAI(
    api_key=os.environ.get("DATABRICKS_TOKEN"),
    base_url=f"{os.environ.get('DATABRICKS_HOST')}/serving-endpoints"
)

response = client.chat.completions.create(
    model="databricks-llama-4-maverick",
    messages=[{"role": "user", "content": "What are the key features of [[mlflow-tracing|MLflow Tracing]]?"}],
    max_tokens=150,
    temperature=0.7
)
```

^[automatic-tracing-databricks-on-aws.md]

### Serverless Compute Note

On serverless compute clusters, autologging for GenAI tracing frameworks is **not** automatically enabled. You must explicitly call the appropriate `mlflow.<library>.autolog()` function for the specific integrations you want to trace. ^[automatic-tracing-databricks-on-aws.md]

## Multi-Framework Autologging

You can enable auto-tracing for multiple frameworks in the same agent. The following example combines OpenAI direct API calls and LangChain chains in a single trace:

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
    # First, use OpenAI directly for initial processing
    analysis = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Analyze the query and extract key topics."},
            {"role": "user", "content": query}
        ]
    )
    topics = analysis.choices[0].message.content

    # Then use LangChain for structured processing
    llm = ChatOpenAI(model="gpt-4o-mini")
    prompt = ChatPromptTemplate.from_template(
        "Based on these topics: {topics}\nGenerate a detailed response to: {query}"
    )
    chain = prompt | llm
    response = chain.invoke({"topics": topics, "query": query})
    return response
```

This produces a single trace containing spans from both frameworks, organized hierarchically. ^[automatic-tracing-databricks-on-aws.md]

## Combining Manual and Automatic Tracing

Use the `@mlflow.trace` decorator alongside autologging to create unified traces that capture custom logic between LLM calls. This is useful for:

- Multi-step workflows with multiple LLM calls
- Multi-agent systems using different providers
- Custom preprocessing or postprocessing logic

```python
import mlflow
import openai
from mlflow.entities import SpanType

mlflow.openai.autolog()
client = openai.OpenAI()

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

run("What is MLflow?")
```

This generates a single trace that combines manually created spans (`build_messages`, `parse_response`) with the automatically traced OpenAI span. ^[automatic-tracing-databricks-on-aws.md]

## Advanced Example: Sequential LLM Calls

When an application makes multiple LLM calls in sequence — for example, first analyzing a query and then generating a response based on that analysis — autologging captures each call as a separate child span within the parent trace:

```python
@mlflow.trace(span_type=SpanType.CHAIN)
def process_user_query(query: str):
    # First LLM call: Analyze the query
    analysis = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Analyze the user's query..."},
            {"role": "user", "content": query}
        ]
    )
    analysis_result = analysis.choices[0].message.content

    # Second LLM call: Generate response based on analysis
    if "factual" in analysis_result.lower():
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Provide a factual response."},
                {"role": "user", "content": query}
            ]
        )
    else:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Provide a creative response."},
                {"role": "user", "content": query}
            ]
        )
    return response.choices[0].message.content
```

This creates one trace with a parent span for `process_user_query` and two child spans for the OpenAI calls. ^[automatic-tracing-databricks-on-aws.md]

## Supported Integrations

Autologging works with over 20 supported libraries and frameworks. For the complete list, see [Automatic tracing integrations](/concepts/automatic-vs-manual-tracing-instrumentation.md). ^[automatic-tracing-databricks-on-aws.md]

## Related Concepts

- [Manual tracing with decorators](/concepts/mlflowtrace-decorator.md) — Adding custom spans with `@mlflow.trace`
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The overall tracing infrastructure in MLflow
- [GenAI evaluation](/concepts/mlflow-genai-evaluation.md) — Using traces to evaluate agent quality
- Trace visualization — Viewing and analyzing captured traces in the Databricks UI
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizing traced runs within experiments
- Span types — Categorizing spans (LLM, CHAIN, AGENT, TOOL, etc.)

## Sources

- automatic-tracing-databricks-on-aws.md

# Citations

1. [automatic-tracing-databricks-on-aws.md](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
