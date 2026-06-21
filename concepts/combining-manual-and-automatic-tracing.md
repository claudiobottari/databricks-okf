---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2cb8e311b322477afe8b7b5d109635e1bbde16fc8637b3afd37d3b5959b9182c
  pageDirectory: concepts
  sources:
    - automatic-tracing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - combining-manual-and-automatic-tracing
    - Automatic Tracing and Combining Manual
    - CMAAT
  citations:
    - file: automatic-tracing-databricks-on-aws.md
title: Combining Manual and Automatic Tracing
description: Using `@mlflow.trace` decorator alongside automatic autolog tracing to create unified traces covering both LLM calls and custom business logic.
tags:
  - mlflow
  - tracing
  - manual-tracing
  - decorators
timestamp: "2026-06-18T14:29:53.354Z"
---

```markdown
---
title: Combining Manual and Automatic Tracing
summary: Using @mlflow.trace decorator alongside mlflow.autolog() to create unified traces that capture both auto-instrumented LLM calls and custom business logic spans in one view.
sources:
  - automatic-tracing-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:50:23.652Z"
updatedAt: "2026-06-18T10:50:23.652Z"
tags:
  - mlflow
  - tracing
  - decorators
  - instrumentation
aliases:
  - combining-manual-and-automatic-tracing
  - Automatic Tracing and Combining Manual
  - CMAAT
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Combining Manual and Automatic Tracing

**Combining manual and automatic tracing** is a pattern in [[MLflow Tracing]] that uses the `@mlflow.trace` decorator together with auto-tracing functions (e.g., `mlflow.openai.autolog()`) to produce a single, unified trace for a generative AI workflow. This approach captures both the framework-level LLM calls (traced automatically) and any custom business logic (traced manually) in one coherent view. ^[automatic-tracing-databricks-on-aws.md]

## Why Combine Tracing Approaches

Auto-tracing with `mlflow.<library>.autolog()` automatically instruments calls to supported frameworks such as OpenAI and LangChain. However, complex AI applications often include custom logic between LLM calls — message construction, response parsing, or branching decision logic. Manual tracing with `@mlflow.trace` fills this gap by adding visibility into the custom code that orchestrates multiple LLM invocations. ^[automatic-tracing-databricks-on-aws.md]

Combining both approaches is useful in the following scenarios: ^[automatic-tracing-databricks-on-aws.md]

- **Multiple LLM calls in one workflow** — Automatic tracing captures each LLM call, while manual tracing groups them under a parent span that represents the overall workflow.
- **Multi-agent systems with different providers** — Automatic tracing covers each provider integration, and manual tracing ties the agent interactions together.
- **Custom logic between LLM calls** — Manual tracing captures data transformations, routing decisions, or preprocessing steps that auto-tracing does not instrument.

## How It Works

When you call `mlflow.<library>.autolog()` for a supported framework (e.g., `mlflow.openai.autolog()`), MLflow automatically generates a span for each invocation of that framework's API, such as `client.chat.completions.create()`. Simultaneously, functions decorated with `@mlflow.trace` produce their own spans. All spans within the same execution context are assembled into a single trace, preserving the parent-child relationships defined by the manual decorators. ^[automatic-tracing-databricks-on-aws.md]

## Basic Example

The following example demonstrates combining automatic OpenAI tracing with manual `@mlflow.trace` decorators: ^[automatic-tracing-databricks-on-aws.md]

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

Running this code generates a single trace that combines the manual spans (`run`, `build_messages`, `parse_response`) with the automatic OpenAI tracing, producing a complete picture of the request flow. ^[automatic-tracing-databricks-on-aws.md]

## Advanced Example: Multiple LLM Calls

Automatic tracing captures multiple LLM calls within a single workflow. The following example shows sequential decision-making with two LLM invocations: ^[automatic-tracing-databricks-on-aws.md]

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

This creates one trace with a parent span for `process_user_query` and two child spans for the OpenAI calls. ^[automatic-tracing-databricks-on-aws.md]

## Enabling Auto-Tracing on Serverless Compute

On serverless compute clusters, autologging for GenAI tracing frameworks is not automatically enabled. You must explicitly enable autologging by calling the appropriate `mlflow.<library>.autolog()` function for the specific integrations you want to trace. ^[automatic-tracing-databricks-on-aws.md]

## Related Concepts

- [[MLflow Tracing]] — The core tracing framework for generative AI applications
- [[Automatic Tracing]] — Framework-level tracing enabled via `mlflow.<library>.autolog()`
- [[Manual Tracing]] — Custom span creation with the `@mlflow.trace` decorator
- LangChain Tracing — Automatic tracing for LangChain frameworks
- OpenAI Tracing — Automatic tracing for OpenAI API calls
- SpanType — Enum used to classify spans in manual tracing

## Sources

- automatic-tracing-databricks-on-aws.md
```

# Citations

1. [automatic-tracing-databricks-on-aws.md](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
