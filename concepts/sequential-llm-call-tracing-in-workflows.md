---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c636c7b67a01c7a262bb2d3edae8b2a822fb0b4d20a7882b4d5b809f9b689d27
  pageDirectory: concepts
  sources:
    - automatic-tracing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sequential-llm-call-tracing-in-workflows
    - SLCTIW
  citations:
    - file: automatic-tracing-databricks-on-aws.md
title: Sequential LLM Call Tracing in Workflows
description: Pattern where automatic tracing captures multiple LLM calls within a single workflow (e.g., analyze-then-respond), producing a trace with a parent span for the overall function and child spans for each LLM invocation.
tags:
  - mlflow
  - tracing
  - llm
  - workflows
timestamp: "2026-06-19T22:11:31.136Z"
---

# Sequential LLM Call Tracing in Workflows

**Sequential LLM Call Tracing in Workflows** refers to the ability to capture and visualize the complete execution path of an application that makes multiple successive calls to large language models (LLMs), where the output of one call influences the input or parameters of the next. This tracing technique is essential for debugging, monitoring, and understanding the behavior of complex multi-step agentic or chain‑based systems. ^[automatic-tracing-databricks-on-aws.md]

## Overview

When a generative AI workflow contains several LLM invocations arranged in sequence – for example, analyzing a query first, then generating a tailored response based on that analysis – each call can be recorded as a distinct span within a single trace. [MLflow Tracing](/concepts/mlflow-tracing.md) provides automatic and manual mechanisms to build these unified traces, showing parent‑child relationships between the overall workflow function and each LLM call. ^[automatic-tracing-databricks-on-aws.md]

## How It Works

With [Automatic Tracing](/concepts/automatic-tracing.md), adding one line of code, such as `mlflow.openai.autolog()`, enables MLflow to automatically capture every call to the OpenAI API made within the execution context. When a workflow function is decorated with `@mlflow.trace`, the resulting trace contains a parent span for the function and child spans for each automatically traced LLM call. ^[automatic-tracing-databricks-on-aws.md]

> **Note:** On serverless compute clusters, autologging for GenAI tracing frameworks is not automatically enabled. You must explicitly call the appropriate `mlflow.<library>.autolog()` function for the specific integrations you want to trace. ^[automatic-tracing-databricks-on-aws.md]

## Example: Multi‑Step Query Processing

The following example from the MLflow documentation demonstrates sequential LLM calls in a single workflow. The first call analyzes the user’s query; the second call generates a response using a system prompt that depends on the analysis result.

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

This code creates a single trace with a parent span for `process_user_query` and two child spans for the OpenAI calls. ^[automatic-tracing-databricks-on-aws.md]

## Combining Manual and Automatic Tracing

You can mix [Manual Tracing with Decorators](/concepts/mlflowtrace-decorator.md) (`@mlflow.trace`) and automatic tracing (`autolog()`) to capture both LLM calls and the custom logic that orchestrates them. This pattern is useful for workflows that include multiple LLM providers, custom processing steps between calls, or multi‑agent systems. ^[automatic-tracing-databricks-on-aws.md]

## Benefits

- **End‑to‑end visibility**: View the entire chain of LLM invocations in one trace, including inputs, outputs, and latency per call.
- **Dependency tracking**: Understand how the result of one LLM call affects subsequent calls.
- **Debugging**: Quickly identify which step in a sequential workflow failed or produced unexpected output.
- **Multi‑provider support**: Trace calls from different libraries (e.g., OpenAI, LangChain, Anthropic) within the same workflow. ^[automatic-tracing-databricks-on-aws.md]

## Related Concepts

- [Automatic Tracing](/concepts/automatic-tracing.md) – Enable tracing with a single line of code.
- [Manual Tracing with Decorators](/concepts/mlflowtrace-decorator.md) – Add custom spans for business logic.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – The overall tracing framework.
- Span Types – Classify spans (e.g., CHAIN, LLM, PARSER).
- LangChain Integration – Automatic tracing for LangChain chains.
- OpenAI Integration – Automatic tracing for OpenAI API calls.

## Sources

- automatic-tracing-databricks-on-aws.md

# Citations

1. [automatic-tracing-databricks-on-aws.md](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
