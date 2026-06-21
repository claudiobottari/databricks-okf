---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a4fcc7e1191c9eaccf92b12e2d621c2abc6ae865ce59d2d5c3027fc3f6824dc3
  pageDirectory: concepts
  sources:
    - automatic-tracing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-framework-auto-tracing-in-mlflow
    - MAIM
  citations:
    - file: automatic-tracing-databricks-on-aws.md
title: Multi-Framework Auto-Tracing in MLflow
description: The ability to enable automatic tracing for multiple frameworks (e.g., OpenAI and LangChain) simultaneously in the same agent, producing a single unified trace.
tags:
  - mlflow
  - tracing
  - multi-framework
  - instrumentation
timestamp: "2026-06-19T14:06:18.478Z"
---

---
title: Multi-Framework Auto-Tracing in MLflow
summary: Enabling automatic tracing for multiple frameworks (e.g., OpenAI and LangChain) simultaneously within the same agent workflow.
sources:
  - automatic-tracing-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T09:05:55.746Z"
updatedAt: "2026-06-19T09:05:55.746Z"
tags:
  - mlflow
  - tracing
  - multi-framework
aliases:
  - multi-framework-auto-tracing-in-mlflow
  - MAIM
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Multi-Framework Auto-Tracing in MLflow

**Multi-Framework Auto-Tracing in MLflow** allows developers to instrument generative AI applications that use multiple libraries or frameworks with a single line of code per framework. Instead of manually wrapping every function call, you call `mlflow.<library>.autolog()` to automatically capture traces for the supported framework. MLflow supports over 20 frameworks out of the box, including OpenAI, LangChain, Anthropic, and many others. ^[automatic-tracing-databricks-on-aws.md]

## Overview

When building agents that combine different LLM providers, orchestration libraries, and custom logic, visibility into each component’s execution becomes critical for debugging, monitoring, and optimization. Multi-framework auto-tracing unifies all spans from different frameworks within a single trace, making it easy to follow the end-to-end flow of a request across OpenAI calls, LangChain chains, or any other supported integration. ^[automatic-tracing-databricks-on-aws.md]

## How to Enable Multi-Framework Auto-Tracing

Automatic tracing is enabled by calling the appropriate `mlflow.<library>.autolog()` function for each framework you want to trace. For example, to trace both OpenAI and LangChain in the same notebook:

```python
import mlflow

mlflow.openai.autolog()
mlflow.langchain.autolog()
```

After calling these functions, every subsequent call to the corresponding library’s API (chat completions, chains, etc.) is automatically instrumented and appears as a span in the MLflow trace. ^[automatic-tracing-databricks-on-aws.md]

### Prerequisites

- MLflow 3.1 or later with the `[databricks]` extras (e.g., `mlflow[databricks]>=3.1`).
- The integration package you want to trace (e.g., `openai>=1.0.0`, `langchain`, `anthropic`).
- On **serverless compute clusters**, auto-tracing is not enabled by default—you must explicitly call the autolog functions. ^[automatic-tracing-databricks-on-aws.md]

## Example: Tracing OpenAI and LangChain Together

The following code demonstrates multi-framework auto-tracing by combining direct OpenAI API calls with a LangChain chain inside a single workflow: ^[automatic-tracing-databricks-on-aws.md]

```python
import mlflow
import openai
from mlflow.entities import SpanType
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Enable auto-tracing for both frameworks
mlflow.openai.autolog()
mlflow.langchain.autolog()

client = openai.OpenAI()

@mlflow.trace(span_type=SpanType.CHAIN)
def multi_provider_workflow(query: str):
    # Direct OpenAI call
    analysis = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Analyze the query and extract key topics."},
            {"role": "user", "content": query}
        ]
    )
    topics = analysis.choices[0].message.content

    # LangChain chain
    llm = ChatOpenAI(model="gpt-4o-mini")
    prompt = ChatPromptTemplate.from_template(
        f"Based on these topics: {topics}\nGenerate a detailed response to: {{query}}"
    )
    chain = prompt | llm
    response = chain.invoke({"topics": topics, "query": query})
    return response

multi_provider_workflow("Explain quantum computing")
```

Running this code produces a single trace containing spans for the OpenAI completion call, the LangChain chain invocation, and the parent `multi_provider_workflow` span. ^[automatic-tracing-databricks-on-aws.md]

## Combining Automatic and Manual Tracing

You can mix auto-tracing with manual tracing using the `@mlflow.trace` decorator. This is useful for adding custom business logic spans between library calls, or for creating parent spans that group multiple auto-traced invocations. The example above already demonstrates this: the `multi_provider_workflow` function is manually traced as a chain, while the inner OpenAI and LangChain calls are auto-traced. ^[automatic-tracing-databricks-on-aws.md]

A simpler pattern for combining manual and automatic tracing looks like this: ^[automatic-tracing-databricks-on-aws.md]

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

This creates a single trace that merges manually decorated spans with the automatic OpenAI span. ^[automatic-tracing-databricks-on-aws.md]

## Advanced Example: Multiple LLM Calls in One Trace

Multi-framework auto-tracing is especially valuable when an application makes sequential LLM decisions using the same or different providers. The following example uses two OpenAI calls inside one manually traced parent function, producing a single trace with nested spans: ^[automatic-tracing-databricks-on-aws.md]

```python
@mlflow.trace(span_type=SpanType.CHAIN)
def process_user_query(query: str):
    # First LLM call: classify
    analysis = client.chat.completions.create(...)
    analysis_result = analysis.choices[0].message.content

    # Second LLM call: conditional response
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

The resulting trace contains a parent span for `process_user_query` and two child spans for the two OpenAI calls, providing end-to-end visibility into the decision logic. ^[automatic-tracing-databricks-on-aws.md]

## Supported Frameworks

MLflow supports automatic tracing for 20+ libraries and frameworks. For the full list, see the [MLflow Tracing Integrations](/concepts/mlflow-tracing-integrations.md) page. ^[automatic-tracing-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The foundational tracing system behind auto-tracing.
- [Manual Tracing with Decorators](/concepts/mlflowtrace-decorator.md) – Adding custom spans with `@mlflow.trace`.
- [MLflow Autolog](/concepts/mlflow-autologging.md) – General autologging mechanism for ML frameworks.
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – Evaluation and monitoring of generative AI applications.
- OpenAI Integration – Auto-tracing for OpenAI API calls.

## Sources

- automatic-tracing-databricks-on-aws.md

# Citations

1. [automatic-tracing-databricks-on-aws.md](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
