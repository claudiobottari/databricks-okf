---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9df93357715c227cf75be063a220d10c2b44d67e259ade7b6c26182edac0f647
  pageDirectory: concepts
  sources:
    - automatic-tracing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - combining-manual-and-automatic-mlflow-tracing
    - Automatic MLflow Tracing and Combining Manual
    - CMAAMT
  citations:
    - file: automatic-tracing-databricks-on-aws.md
title: Combining Manual and Automatic MLflow Tracing
description: Using @mlflow.trace decorators alongside autolog() to create unified traces that capture custom business logic and auto-traced LLM calls together.
tags:
  - mlflow
  - tracing
  - manual-tracing
timestamp: "2026-06-19T09:06:02.965Z"
---

# Combining Manual and Automatic [MLflow Tracing](/concepts/mlflow-tracing.md)

**Combining Manual and Automatic MLflow Tracing** refers to the practice of using both `@mlflow.trace` decorators and `mlflow.<library>.autolog()` calls together to create unified, comprehensive traces for generative AI applications. This hybrid approach allows developers to capture automatically generated spans from supported frameworks while also adding custom spans for business logic, preprocessing, and postprocessing steps. ^[automatic-tracing-databricks-on-aws.md]

## Overview

Automatic tracing with `mlflow.<library>.autolog()` captures spans from [20+ supported libraries and frameworks](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/) out of the box. However, many applications include custom logic between LLM calls — such as message construction, response parsing, or decision branching — that automatic tracing cannot capture. By combining manual tracing with automatic tracing, developers can produce a single trace that covers the entire workflow. ^[automatic-tracing-databricks-on-aws.md]

## When to Combine Manual and Automatic Tracing

Combining both approaches is useful for the following scenarios: ^[automatic-tracing-databricks-on-aws.md]

- **Multiple LLM calls in one workflow** — When an application makes several sequential or conditional LLM calls, automatic tracing captures each call individually, but manual tracing can wrap the entire workflow in a parent span.
- **Multi-agent systems with different providers** — When different agents use different LLM providers (e.g., OpenAI, Anthropic, LangChain), automatic tracing captures each provider's calls, while manual tracing can organize them under a unified orchestration span.
- **Custom logic between LLM calls** — When preprocessing (e.g., message construction) or postprocessing (e.g., response parsing) occurs between LLM invocations, manual tracing can capture these steps.

## How It Works

When you enable automatic tracing for a library (e.g., `mlflow.openai.autolog()`) and also decorate custom functions with `@mlflow.trace`, MLflow merges the automatically generated spans with the manually created spans into a single trace hierarchy. The manual spans become parent or sibling spans to the auto-traced spans, depending on how they are structured. ^[automatic-tracing-databricks-on-aws.md]

### Basic Example

The following example demonstrates combining automatic OpenAI tracing with manual tracing for message building and response parsing: ^[automatic-tracing-databricks-on-aws.md]

```python
import mlflow
import openai
from mlflow.entities import SpanType

mlflow.openai.autolog()

# Create OpenAI client
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

Running this code generates a single trace with:
- A parent span for `run`
- A child span for `build_messages` (manual)
- A child span for the OpenAI API call (automatic)
- A child span for `parse_response` (manual)

## Advanced Example: Multiple LLM Calls

The following example shows how automatic tracing captures multiple LLM calls in a single workflow, while manual tracing wraps the entire process: ^[automatic-tracing-databricks-on-aws.md]

```python
import mlflow
import openai
from mlflow.entities import SpanType

# Enable auto-tracing for OpenAI
mlflow.openai.autolog()

# Create OpenAI client
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

# Run the function
result = process_user_query("Tell me about the history of artificial intelligence")
```

This creates one trace with:
- A parent span for `process_user_query` (manual)
- Two child spans for the OpenAI calls (automatic)

## Multi-Framework Tracing

You can enable automatic tracing for multiple frameworks simultaneously and combine them with manual tracing. For example, you can trace both OpenAI and LangChain calls in the same workflow: ^[automatic-tracing-databricks-on-aws.md]

```python
import mlflow
import openai
from mlflow.entities import SpanType
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

# Run the function
result = multi_provider_workflow("Explain quantum computing")
```

## Best Practices

- **Use `SpanType` annotations** — When creating manual spans with `@mlflow.trace`, specify the `span_type` parameter (e.g., `SpanType.CHAIN`, `SpanType.LLM`, `SpanType.TOOL`) to help organize the trace hierarchy. ^[automatic-tracing-databricks-on-aws.md]
- **Wrap the entire workflow** — Create a top-level manual span around the complete workflow to provide context for all auto-traced spans within it. ^[automatic-tracing-databricks-on-aws.md]
- **Trace preprocessing and postprocessing** — Use `@mlflow.trace` on helper functions that prepare inputs or process outputs to capture the full data flow. ^[automatic-tracing-databricks-on-aws.md]
- **Enable autologging for all relevant frameworks** — If your application uses multiple LLM providers or frameworks, enable autologging for each one to ensure comprehensive coverage. ^[automatic-tracing-databricks-on-aws.md]

## Limitations

On serverless compute clusters, autologging for GenAI tracing frameworks is not automatically enabled. You must explicitly enable autologging by calling the appropriate `mlflow.<library>.autolog()` function for the specific integrations you want to trace. ^[automatic-tracing-databricks-on-aws.md]

## Related Concepts

- [Automatic MLflow Tracing](/concepts/automatic-tracing.md) — Enabling tracing with a single `autolog()` call
- [Manual MLflow Tracing](/concepts/manual-tracing.md) — Using `@mlflow.trace` decorators for custom spans
- [MLflow Tracing Integrations](/concepts/mlflow-tracing-integrations.md) — The 20+ supported libraries and frameworks
- Span Types — Categorizing spans with `SpanType` annotations
- [MLflow 3](/concepts/mlflow-3.md) — The recommended version for GenAI tracing capabilities

## Sources

- automatic-tracing-databricks-on-aws.md

# Citations

1. [automatic-tracing-databricks-on-aws.md](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
