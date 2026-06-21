---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0673be6697204fa784fe8e7f6a2b6aa616374b2abd90408960f3011cb3eceef3
  pageDirectory: concepts
  sources:
    - automatic-tracing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-automatic-tracing-autolog
    - MAT(
    - MLflow Automatic Logging (autolog)
  citations:
    - file: automatic-tracing-databricks-on-aws.md
title: MLflow Automatic Tracing (autolog)
description: One-line code pattern using mlflow.<library>.autolog() to automatically trace generative AI applications across 20+ supported libraries and frameworks.
tags:
  - mlflow
  - tracing
  - generative-ai
  - instrumentation
timestamp: "2026-06-19T22:11:27.737Z"
---

# MLflow Automatic Tracing (autolog)

**MLflow Automatic Tracing (autolog)** is a feature that allows you to automatically trace generative AI application calls by adding a single line of code: `mlflow.<library>.autolog()`. It works with over 20 supported libraries and frameworks out of the box, including OpenAI, LangChain, and others.^[automatic-tracing-databricks-on-aws.md]

The tracing captures the full execution flow of LLM calls, chains, and custom logic, producing detailed spans that can be viewed in the MLflow UI for debugging and monitoring.

> **Note:** On serverless compute clusters, autologging for GenAI tracing frameworks is not automatically enabled. You must explicitly call the appropriate `mlflow.<library>.autolog()` function for the specific integrations you want to trace.^[automatic-tracing-databricks-on-aws.md]

## Prerequisites

Databricks recommends MLflow 3 for the latest GenAI tracing capabilities. To use automatic tracing, install the `mlflow` package with Databricks support and the SDK for the framework you intend to trace (for example, `openai`). The example installation command is:^[automatic-tracing-databricks-on-aws.md]

```python
%pip install --upgrade "mlflow[databricks]>=3.1" openai>=1.0.0
dbutils.library.restartPython()
```

You must also configure credentials, such as setting the `OPENAI_API_KEY` environment variable, either in a Databricks notebook or an external environment.^[automatic-tracing-databricks-on-aws.md]

## Basic Automatic Tracing Example

The following example enables automatic tracing for OpenAI calls, using the Databricks Foundation Model API via an OpenAI-compatible client:^[automatic-tracing-databricks-on-aws.md]

```python
import mlflow
import os
from openai import OpenAI

mlflow.set_tracking_uri("databricks")
mlflow.set_experiment("/Shared/databricks-sdk-autolog-example")

# Enable auto-tracing for OpenAI
mlflow.openai.autolog()

# Create an OpenAI client configured for Databricks
client = OpenAI(
    api_key=os.environ.get("DATABRICKS_TOKEN"),
    base_url=f"{os.environ.get('DATABRICKS_HOST')}/serving-endpoints"
)

# Query Llama 4 Maverick – the call is automatically traced
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

All calls to the Databricks Foundation Model API via the OpenAI client are automatically traced.^[automatic-tracing-databricks-on-aws.md]

## Auto-tracing Multiple Frameworks

You can enable autolog for multiple frameworks in the same agent. For example, the following code combines OpenAI and LangChain tracing:^[automatic-tracing-databricks-on-aws.md]

```python
import mlflow
import openai
from mlflow.entities import SpanType
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Enable automatic tracing for both OpenAI and LangChain
mlflow.openai.autolog()
mlflow.langchain.autolog()

client = openai.OpenAI()

@mlflow.trace(span_type=SpanType.CHAIN)
def multi_provider_workflow(query: str):
    # First, use OpenAI directly
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

result = multi_provider_workflow("Explain quantum computing")
```

This creates a single trace that contains spans from both frameworks, enabling unified debugging and monitoring.^[automatic-tracing-databricks-on-aws.md]

## Combining Manual and Automatic Tracing

You can mix manual spans (created with the `@mlflow.trace` decorator) with automatic tracing. This is useful for scenarios such as:^[automatic-tracing-databricks-on-aws.md]

- Multiple LLM calls in one workflow
- Multi-agent systems using different providers
- Custom logic that runs between LLM calls

Example:^[automatic-tracing-databricks-on-aws.md]

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

This produces a single trace combining the user-defined spans (`build_messages`, `parse_response`) with the automatically generated OpenAI span.^[automatic-tracing-databricks-on-aws.md]

## Advanced Example: Multiple LLM Calls

Automatic tracing captures multiple LLM calls in a sequential workflow, as shown below:^[automatic-tracing-databricks-on-aws.md]

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

The resulting trace includes a parent span for `process_user_query` and two child spans for the OpenAI calls, providing a clear view of the decision flow.^[automatic-tracing-databricks-on-aws.md]

## Next Steps

- Browse all [Automatic Tracing Integrations](/concepts/automatic-vs-manual-tracing-instrumentation.md) for the complete list of 20+ supported libraries and frameworks.^[automatic-tracing-databricks-on-aws.md]
- Learn how to add [Manual Tracing with Decorators](/concepts/mlflowtrace-decorator.md) to capture custom business logic alongside auto-traced LLM calls.^[automatic-tracing-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [GenAI Agent Tracing](/concepts/mlflow-genai-tracing.md)
- Span Types
- [Databricks Foundation Model API](/concepts/databricks-foundation-model-apis.md)

## Sources

- automatic-tracing-databricks-on-aws.md

# Citations

1. [automatic-tracing-databricks-on-aws.md](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
