---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 41654d632c5ebec946d697ea85bffc6a045220e04fa4ee78603aa9b58cf475ab
  pageDirectory: concepts
  sources:
    - automatic-tracing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - combined-manual-and-automatic-tracing
    - Automatic Tracing and Combined Manual
    - CMAAT
    - Combine Manual and Automatic Tracing
    - Combine manual and automatic tracing
  citations:
    - file: automatic-tracing-databricks-on-aws.md
title: Combined Manual and Automatic Tracing
description: Pattern of using @mlflow.trace decorator and @mlflow.trace(span_type=...), alongside mlflow.autolog() to create unified traces that capture both library-internal calls and custom business logic.
tags:
  - mlflow
  - tracing
  - decorators
  - instrumentation
timestamp: "2026-06-19T22:10:25.386Z"
---

# Combined Manual and Automatic Tracing

**Combined Manual and Automatic Tracing** is a pattern in [MLflow Tracing](/concepts/mlflow-tracing.md) that lets developers use `@mlflow.trace` decorators together with `mlflow.<library>.autolog()` to create unified traces for complex generative AI workflows. This approach combines the convenience of automatic span generation for supported libraries with the flexibility of custom spans for business logic, data processing, and orchestration code. ^[automatic-tracing-databricks-on-aws.md]

## Overview

Automatic tracing via `mlflow.<library>.autolog()` captures spans for calls to supported frameworks such as OpenAI, LangChain, Anthropic, and over 20 other libraries. However, many real-world applications contain custom logic between LLM calls — message construction, response parsing, conditional branching, or multi-agent coordination — that automatic tracing alone cannot instrument. The Combined Manual and Automatic Tracing pattern fills this gap. ^[automatic-tracing-databricks-on-aws.md]

By applying `@mlflow.trace` to custom functions and `@mlflow.trace(span_type=SpanType.CHAIN)` to orchestration functions, developers can wrap auto-traced LLM calls within manually created spans, producing a single hierarchical trace that shows both the application-level control flow and the detailed LLM requests and responses. ^[automatic-tracing-databricks-on-aws.md]

## Common Use Cases

### Multiple LLM Calls in One Workflow

When an application makes two or more LLM calls sequentially — for example, an analysis pass followed by a response generation pass — combined tracing captures both calls as child spans under a single parent orchestration span. The parent span (created with `@mlflow.trace`) represents the overall function, while the LLM calls are automatically traced as child spans by the autolog integration. ^[automatic-tracing-databricks-on-aws.md]

### Multi-Agent Systems with Different Providers

Applications that orchestrate multiple agents using different providers (e.g., OpenAI for one agent, Anthropic for another) can combine automatic tracing for each provider with manual spans that represent agent coordination logic. ^[automatic-tracing-databricks-on-aws.md]

### Custom Logic Between LLM Calls

When business logic, data transformation, or conditional branching occurs between LLM invocations, manual `@mlflow.trace` decorators on those utility functions capture that logic as distinct spans within the same trace as the auto-traced LLM calls. ^[automatic-tracing-databricks-on-aws.md]

## How It Works

1. **Enable auto-tracing** for the libraries you use by calling `mlflow.<library>.autolog()` for each (e.g., `mlflow.openai.autolog()`, `mlflow.langchain.autolog()`).
2. **Decorate orchestration functions** with `@mlflow.trace(span_type=SpanType.CHAIN)` to create a parent span for the overall workflow.
3. **Decorate helper functions** with `@mlflow.trace` to create custom spans for message construction, response parsing, validation, or any other business logic.
4. **Run the workflow**: MLflow automatically generates child spans for each supported library call, nesting them under the manually created spans in a unified trace. ^[automatic-tracing-databricks-on-aws.md]

## Example: Basic Combined Tracing

```python
import mlflow
import openai
from mlflow.entities import SpanType

mlflow.openai.autolog()

client = openai.OpenAI()

@mlflow.trace(span_type=SpanType.CHAIN)
def run(question):
    messages = build_messages(question)
    # MLflow automatically generates a span for the OpenAI invocation
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

This generates a single trace with:
- A parent span (`run`) of type `CHAIN`
- Two child spans for `build_messages` and `parse_response`
- A grandchild span for the OpenAI chat completion call, automatically captured by `mlflow.openai.autolog()` ^[automatic-tracing-databricks-on-aws.md]

## Best Practices

- **Use `SpanType.CHAIN`** for top-level orchestration functions to signal that the span represents a compound operation composed of sub-steps. ^[automatic-tracing-databricks-on-aws.md]
- **Decorate every function** that contains significant logic between LLM calls to ensure the trace captures the full application flow. ^[automatic-tracing-databricks-on-aws.md]
- **Enable auto-tracing early** in your application initialization, before any library calls are made. ^[automatic-tracing-databricks-on-aws.md]
- **Be explicit about span types** when setting `span_type` to improve trace visualization and filtering in the MLflow UI. ^[automatic-tracing-databricks-on-aws.md]

## Limitations

On serverless compute clusters, autologging for generative AI tracing frameworks is **not** automatically enabled. You must explicitly call `mlflow.<library>.autolog()` for each integration you want to trace. ^[automatic-tracing-databricks-on-aws.md]

## Related Concepts

- [Automatic Tracing](/concepts/automatic-tracing.md) — Enabling traces with a single line of code for supported libraries.
- [Manual Tracing with Decorators](/concepts/mlflowtrace-decorator.md) — Adding custom spans with `@mlflow.trace`.
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The overall tracing subsystem for generative AI applications.
- Span Type — Classification of spans (CHAIN, LLM, PARSER, etc.) for visualization.
- [GenAI Tracing Integrations](/concepts/mlflow-tracing-integrations.md) — The 20+ supported libraries and frameworks.

## Sources

- automatic-tracing-databricks-on-aws.md

# Citations

1. [automatic-tracing-databricks-on-aws.md](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
