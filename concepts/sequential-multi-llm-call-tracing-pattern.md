---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 03184626c3445ab15aefb35e269fcae158b3a8e35781218b9ea248f9c49225d0
  pageDirectory: concepts
  sources:
    - automatic-tracing-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sequential-multi-llm-call-tracing-pattern
    - SMCTP
  citations:
    - file: automatic-tracing-databricks-on-aws.md
title: Sequential Multi-LLM Call Tracing Pattern
description: A pattern where automatic tracing captures multiple sequential LLM calls in a single workflow, creating a trace with a parent span and child spans for each LLM invocation.
tags:
  - mlflow
  - tracing
  - llm-workflow
  - pattern
timestamp: "2026-06-19T14:06:31.226Z"
---

---

title: Sequential Multi-LLM Call Tracing Pattern
summary: Automatic tracing captures multiple sequential LLM calls (e.g., analysis followed by response generation) as child spans within a single parent workflow trace.
sources:
  - automatic-tracing-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:29:57.329Z"
updatedAt: "2026-06-18T14:29:57.329Z"
tags:
  - mlflow
  - tracing
  - llm-calls
  - workflow
aliases:
  - sequential-multi-llm-call-tracing-pattern
  - SMCTP
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Sequential Multi-LLM Call Tracing Pattern

The **Sequential Multi-LLM Call Tracing Pattern** refers to a design pattern in generative AI applications where a single workflow makes multiple calls to a large language model (LLM) in sequence, with the output of one call informing the next. This pattern is captured as a unified trace by [Automatic Tracing](/concepts/automatic-tracing.md) in MLflow, allowing developers to debug and monitor the entire chain of reasoning. ^[automatic-tracing-databricks-on-aws.md]

## Use Cases

Sequential multi-LLM call patterns are common when an application needs to decompose a task into stages, such as first analyzing a user query and then generating a response based on that analysis. This approach is useful for applications that require sequential decision-making, where each step depends on the previous one. ^[automatic-tracing-databricks-on-aws.md]

## How It Works

When [Automatic Tracing](/concepts/automatic-tracing.md) is enabled for a supported framework (e.g., OpenAI, LangChain), MLflow automatically generates a span for each LLM call. By wrapping the overall workflow with a manual `@mlflow.trace` decorator, you create a parent span that contains multiple child spans—one for each sequential LLM call. The resulting trace shows the full sequence of calls and their inputs and outputs, making it easy to inspect the flow of reasoning. ^[automatic-tracing-databricks-on-aws.md]

## Example: Query Analysis Followed by Response Generation

The following example demonstrates the pattern using the OpenAI client. The workflow first calls the LLM to analyze a query, then uses that analysis to decide how to generate a response. Both LLM calls are automatically traced as child spans under the `process_user_query` parent span.

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

This code creates a single trace with one parent span (`process_user_query`) and two child spans for the OpenAI calls. ^[automatic-tracing-databricks-on-aws.md]

## Benefits

- **End-to-end visibility**: The trace captures the full sequence of LLM calls, showing how earlier outputs influence later decisions.
- **Simplified debugging**: Developers can inspect the input and output of each step without adding manual instrumentation per call.
- **Framework agnostic**: The pattern works with any LLM provider supported by MLflow's automatic tracing, including OpenAI, Anthropic, and LangChain. ^[automatic-tracing-databricks-on-aws.md]

## Related Patterns

- [Automatic Tracing](/concepts/automatic-tracing.md) – The underlying mechanism that generates spans for supported libraries.
- [Manual Tracing with Decorators](/concepts/mlflowtrace-decorator.md) – Used to create parent spans that wrap automatic traces.
- Multi-Provider Tracing – Combining calls to different LLM providers within a single trace.
- Branching Multi-LLM Call Pattern – A variant where calls run in parallel or conditionally.

## Sources

- automatic-tracing-databricks-on-aws.md

# Citations

1. [automatic-tracing-databricks-on-aws.md](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
