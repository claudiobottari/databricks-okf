---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4927d808f699ca72ee8aacfbe436595754c0a0eb88a83ff313e4d575cd3d7807
  pageDirectory: concepts
  sources:
    - 10-minute-demo-collect-human-feedback-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-app-tracing-with-openai
    - MGATWO
  citations:
    - file: 10-minute-demo-collect-human-feedback-databricks-on-aws.md
title: MLflow GenAI App Tracing with OpenAI
description: Pattern for instrumenting Python GenAI applications using MLflow's automatic OpenAI client tracing and the @mlflow.trace decorator for custom functions like retrievers
tags:
  - mlflow
  - tracing
  - openai
  - genai
timestamp: "2026-06-18T14:14:40.838Z"
---

# MLflow GenAI App Tracing with OpenAI

**MLflow GenAI App Tracing with OpenAI** refers to the ability to automatically or manually capture execution traces for applications that call OpenAI-compatible APIs, including Databricks-hosted foundation models exposed through an OpenAI-compatible endpoint. By enabling tracing, developers gain visibility into every step of a GenAI application’s execution — from user input to LLM response — which is essential for debugging, evaluation, and collecting human feedback.

## Overview

MLflow provides two complementary mechanisms for instrumenting OpenAI-based applications:

1. **Automatic tracing** – using `mlflow.openai.autolog()` to capture all calls to the OpenAI API without modifying the application code.
2. **Manual tracing** – using the `@mlflow.trace` decorator to add custom spans for application-specific logic, such as retrieval or post-processing.

These mechanisms work together to produce a unified trace that shows the full chain of operations: a user query, context retrieval, the LLM call, and the final response. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Enabling Automatic OpenAI Tracing

To enable automatic tracing for the OpenAI client, call `mlflow.openai.autolog()` before any API calls are made. This automatically instruments the OpenAI SDK (including Databricks-hosted endpoints used via `databricks_openai`) so that every `chat.completions.create` or similar request is recorded as a span in the active MLflow trace. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

```python
import mlflow
from databricks_openai import DatabricksOpenAI

# Enable automatic tracing for the OpenAI client
mlflow.openai.autolog()

# Create an OpenAI client connected to Databricks-hosted LLMs
client = DatabricksOpenAI()
```

> **Note:** The `mlflow.openai.autolog()` function works with any OpenAI-compatible client. In the example above, `DatabricksOpenAI` is used to call Databricks-hosted models via an OpenAI-compatible API.

## Adding Custom Spans with the Trace Decorator

For application logic that is not automatically captured — such as a retrieval step — you can add manual spans using the `@mlflow.trace` decorator. The decorator accepts a `span_type` parameter that categorizes the span (for example, `"RETRIEVER"`). This enriches the trace with application-specific context. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

```python
@mlflow.trace(span_type="RETRIEVER")
def retrieve_context(query: str) -> str:
    # Simulated retrieval logic
    if "mlflow" in query.lower():
        return "MLflow is the largest open source AI engineering platform..."
    return "General information..."
```

A root span can be added by decorating the main application function:

```python
@mlflow.trace
def my_chatbot(user_question: str) -> str:
    context = retrieve_context(user_question)
    response = client.chat.completions.create(
        model="databricks-claude-sonnet-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Use the provided context to answer questions."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {user_question}"}
        ],
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].message.content
```

## Viewing Traces

After the application runs, a trace is automatically created. You can retrieve the trace ID for the most recent execution using `mlflow.get_last_active_trace_id()`. Traces are visible in the MLflow UI under the experiment’s **Logs** tab. Clicking a trace displays all spans — the root span, the retrieval span, and the OpenAI API call — along with their inputs, outputs, and timing. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

```python
trace_id = mlflow.get_last_active_trace_id()
print(f"Trace ID: {trace_id}")
```

## Enabling Human Feedback Collection

Traced applications are ready to collect human feedback from end users, developers, and domain experts. Each trace can be associated with feedback assessments (e.g., thumbs up/down, accuracy scores) logged via `mlflow.log_feedback()` or through the MLflow UI. Traces can also be added to [Labeling Sessions](/concepts/labeling-sessions.md) for structured expert review. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The general mechanism for capturing execution traces
- [MLflow OpenAI Autolog](/concepts/mlflow-openai-autolog.md) — The `mlflow.openai.autolog()` function in detail
- [GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — Using traces and feedback to evaluate application quality
- [Human Feedback Collection](/concepts/mlflow-human-feedback-collection.md) — Methods for collecting and using human assessments
- [Labeling Sessions](/concepts/labeling-sessions.md) — Structured expert review of traces

## Sources

- 10-minute-demo-collect-human-feedback-databricks-on-aws.md

# Citations

1. [10-minute-demo-collect-human-feedback-databricks-on-aws.md](/references/10-minute-demo-collect-human-feedback-databricks-on-aws-3f033604.md)
