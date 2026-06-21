---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: af427b65cf62a8571509f6e89e67d4701923c429f1be3bc96fea20cdc75834ac
  pageDirectory: concepts
  sources:
    - automatic-tracing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-framework-auto-tracing
  citations:
    - file: automatic-tracing-databricks-on-aws.md
title: Multi-framework Auto-tracing
description: Ability to enable automatic tracing for multiple AI frameworks (e.g., OpenAI and LangChain) simultaneously in the same agent workflow, producing unified traces.
tags:
  - mlflow
  - tracing
  - langchain
  - openai
timestamp: "2026-06-19T22:10:49.580Z"
---

# Multi-framework Auto-tracing

**Multi-framework Auto-tracing** refers to the ability to enable automatic tracing for multiple [Generative AI](/concepts/mlflow-tracing-for-generative-ai.md) frameworks (e.g., OpenAI, LangChain, Anthropic) simultaneously within the same agent workflow. By calling the appropriate `mlflow.<library>.autolog()` function for each integration, you can capture all LLM calls, chain executions, and custom logic in a single unified trace for easier debugging and monitoring. ^[automatic-tracing-databricks-on-aws.md]

## Overview

MLflow supports automatic tracing for over 20 libraries and frameworks out of the box. You can use auto-tracing for multiple frameworks in the same agent – for example, combining direct OpenAI API calls, LangChain chains, and custom business logic – without adding manual tracing code for each individual call. ^[automatic-tracing-databricks-on-aws.md]

## Enabling Multi-framework Auto-tracing

To use multi-framework auto-tracing, install the required packages and call `autolog()` for each framework you want to trace. The following example enables auto-tracing for both OpenAI and LangChain: ^[automatic-tracing-databricks-on-aws.md]

```python
import mlflow
import openai
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Enable auto-tracing for both OpenAI and LangChain
mlflow.openai.autolog()
mlflow.langchain.autolog()

# Create OpenAI client
client = openai.OpenAI()

@mlflow.trace(span_type=SpanType.CHAIN)
def multi_provider_workflow(query: str):
    # First, use OpenAI directly for initial processing
    analysis = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[...]
    )
    topics = analysis.choices[0].message.content

    # Then use LangChain for structured processing
    llm = ChatOpenAI(model="gpt-4o-mini")
    prompt = ChatPromptTemplate.from_template(...)
    chain = prompt | llm
    response = chain.invoke({"topics": topics, "query": query})
    return response

result = multi_provider_workflow("Explain quantum computing")
```

### Combining Auto-tracing with Manual Tracing

You can combine auto-tracing with manual tracing using the `@mlflow.trace` decorator to create unified traces for complex workflows. This pattern is useful for: ^[automatic-tracing-databricks-on-aws.md]

- Multiple LLM calls in one workflow
- Multi-agent systems with different providers
- Custom logic between LLM calls

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

Running this code generates a single trace that combines manual spans with automatic OpenAI tracing. ^[automatic-tracing-databricks-on-aws.md]

### Advanced Example: Sequential LLM Calls

When your application needs to make sequential decisions – such as analyzing a query first and then generating a response based on that analysis – multi-framework auto-tracing captures all LLM calls in a single trace. The following example demonstrates this pattern: ^[automatic-tracing-databricks-on-aws.md]

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

This creates one trace with:
- A parent span for `process_user_query`
- Two child spans for the OpenAI calls ^[automatic-tracing-databricks-on-aws.md]

## Serverless Compute Requirements

On serverless compute clusters, autologging for GenAI tracing frameworks is **not** automatically enabled. You must explicitly enable autologging by calling the appropriate `mlflow.<library>.autolog()` function for the specific integrations you want to trace. ^[automatic-tracing-databricks-on-aws.md]

## Related Concepts

- [Automatic Tracing](/concepts/automatic-tracing.md) – The general concept of auto-instrumentation for GenAI applications
- [Manual Tracing](/concepts/manual-tracing.md) – Adding custom spans with the `@mlflow.trace` decorator
- [MLflow Tracing Integrations](/concepts/mlflow-tracing-integrations.md) – The 20+ supported libraries and frameworks
- Span Types – Categories for spans such as `CHAIN`, `LLM`, and `TOOL`
- [MLflow 3](/concepts/mlflow-3.md) – The recommended version for GenAI tracing capabilities

## Sources

- automatic-tracing-databricks-on-aws.md

# Citations

1. [automatic-tracing-databricks-on-aws.md](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
