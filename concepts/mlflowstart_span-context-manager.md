---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 274eba0969dfca9967a673ab7f32559ee798e79e728e152e57fea1510e675838
  pageDirectory: concepts
  sources:
    - span-tracing-with-context-managers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflowstart_span-context-manager
    - MCM
    - Start Span Context Manager
    - mlflow.start_span() context manager
    - Span Tracing with Context Managers
    - Span context and propagation
    - context manager spans
    - span tracing with context managers|`mlflow.start_span()` context manager
  citations:
    - file: span-tracing-with-context-managers-databricks-on-aws.md
title: mlflow.start_span() Context Manager
description: A context manager API in MLflow for creating spans around arbitrary code blocks, providing fine-grained control over tracing beyond function-level decorators.
tags:
  - mlflow
  - tracing
  - context-manager
  - observability
timestamp: "2026-06-19T23:05:33.716Z"
---

# `mlflow.start_span()` Context Manager

The [`mlflow.start_span()`](https://[MLflow](/concepts/mlflow.md).org/docs/latest/api_reference/python_api/[MLflow](/concepts/mlflow.md).html#mlflow.start_span) context manager creates spans for arbitrary code blocks, offering fine-grained control over what code is traced in [MLflow Tracing](/concepts/mlflow-tracing.md). Unlike Function decorators that trace at the granularity of entire functions, `start_span()` can capture complex, multi-step interactions within a single function or across code segments. ^[span-tracing-with-context-managers-databricks-on-aws.md]

Key capabilities include:
- **Arbitrary code blocks**: Trace any code block, not just entire functions.
- **Automatic context management**: [MLflow](/concepts/mlflow.md) handles parent-child relationships and cleanup.
- **Works with function decorators**: Mix and match with `@mlflow.trace` for hybrid approaches.
- **Exception handling**: Automatic error capturing, similarly to function decorators.

^[span-tracing-with-context-managers-databricks-on-aws.md]

## Prerequisites

For [MLflow 3](/concepts/mlflow-3.md) (recommended), install:
- `mlflow[databricks]` 3.1 and above
- `openai` 1.0.0 and above (if using the OpenAI client)

For [MLflow](/concepts/mlflow.md) 2, use:
- `mlflow[databricks]` 2.15.0 and above, below 3.0.0
- `openai` 1.0.0 and above (optional)

^[span-tracing-with-context-managers-databricks-on-aws.md]

## Span tracing API

The context manager automatically captures the parent-child relationship, exceptions, and execution time. It is compatible with [Automatic Tracing](/concepts/automatic-tracing.md) as well. Unlike the function decorator, the name, inputs, and outputs of the span must be provided manually using the [`LiveSpan`](https://[MLflow](/concepts/mlflow.md).org/docs/latest/api_reference/python_api/[MLflow](/concepts/mlflow.md).entities.html#mlflow.entities.LiveSpan) object returned by the context manager. ^[span-tracing-with-context-managers-databricks-on-aws.md]

```python
import [[mlflow|MLflow]]

with [[mlflow|MLflow]].start_span(name="my_span") as span:
    x = 1
    y = 2
    span.set_inputs({"x": x, "y": y})
    z = x + y
    span.set_outputs(z)
```

## Span events

[`SpanEvent`](https://[MLflow](/concepts/mlflow.md).org/docs/latest/api_reference/python_api/[MLflow](/concepts/mlflow.md).entities.html#mlflow.entities.SpanEvent) objects record specific occurrences during a span's lifetime. The API supports:
- Creating an event with the current timestamp
- Creating an event with a specific timestamp (in nanoseconds)
- Creating an event from an `Exception` using `SpanEvent.from_exception(e)`, which automatically sets the name to `"exception"` and captures the exception message, type, and stacktrace.

^[span-tracing-with-context-managers-databricks-on-aws.md]

```python
from [[mlflow|MLflow]].entities import SpanEvent, SpanType
import time

with [[mlflow|MLflow]].start_span(name="manual_span", span_type=SpanType.CHAIN) as span:
    event = SpanEvent(
        name="validation_completed",
        attributes={
            "records_validated": 1000,
            "errors_found": 3,
            "validation_type": "schema"
        }
    )
    span.add_event(event)

    # Event with specific timestamp (nanoseconds)
    specific_time_event = SpanEvent(
        name="data_checkpoint",
        timestamp=int(time.time() * 1e9),
        attributes={"checkpoint_id": "ckpt_123"}
    )
    span.add_event(specific_time_event)

    # Event from an exception
    try:
        raise ValueError("Invalid input format")
    except Exception as e:
        error_event = SpanEvent.from_exception(e)
        span = [[mlflow|MLflow]].get_current_active_span()
        span.add_event(error_event)
```

## Span status

[`SpanStatus`](https://[MLflow](/concepts/mlflow.md).org/docs/latest/api_reference/python_api/[MLflow](/concepts/mlflow.md).entities.html#mlflow.entities.SpanStatus) defines the status of a span. Note that the `mlflow.start_span()` context manager overwrites the status upon exit — if the block exits successfully, the status is set to `OK`. ^[span-tracing-with-context-managers-databricks-on-aws.md]

```python
from [[mlflow|MLflow]].entities import SpanStatus, SpanStatusCode, SpanType

with [[mlflow|MLflow]].start_span(name="manual_span", span_type=SpanType.CHAIN) as span:
    success_status = SpanStatus(SpanStatusCode.OK)
    error_status = SpanStatus(
        SpanStatusCode.ERROR,
        description="Failed to connect to database"
    )
    span.set_status(success_status)
    # Or use string shortcuts:
    span.set_status("OK")
    span.set_status("ERROR")
```

Query status from completed spans:

```python
last_trace_id = [[mlflow|MLflow]].get_last_active_trace_id()
trace = [[mlflow|MLflow]].get_trace(last_trace_id)
for span in trace.data.spans:
    print(span.status.status_code)
```

## [RETRIEVER Spans](/concepts/retriever-spans.md)

Use `SpanType.RETRIEVER` spans when retrieving documents from a data store. [RETRIEVER Spans](/concepts/retriever-spans.md) must output a list of [`Document`](https://[MLflow](/concepts/mlflow.md).org/docs/latest/api_reference/python_api/[MLflow](/concepts/mlflow.md).entities.html#mlflow.entities.Document) objects for proper UI rendering. The `Document` object accepts `page_content`, `metadata` (including `doc_uri`, `chunk_id`, `relevance_score`, etc.), and an optional `id`. ^[span-tracing-with-context-managers-databricks-on-aws.md]

```python
from [[mlflow|MLflow]].entities import Document, SpanType

@mlflow.trace(span_type=SpanType.RETRIEVER)
def retrieve_documents(query: str):
    span = [[mlflow|MLflow]].get_current_active_span()
    documents = [
        Document(
            page_content="The content of the document...",
            metadata={
                "doc_uri": "path/to/document.md",
                "chunk_id": "chunk_001",
                "relevance_score": 0.95,
                "source": "knowledge_base"
            },
            id="doc_123"
        ),
    ]
    span.set_outputs(documents)
    return [doc.to_dict() for doc in documents]
```

Access retriever outputs from a completed trace:

```python
last_trace_id = [[mlflow|MLflow]].get_last_active_trace_id()
trace = [[mlflow|MLflow]].get_trace(last_trace_id)
retriever_span = trace.search_spans(span_type=SpanType.RETRIEVER)[0]
if retriever_span.outputs:
    for doc in retriever_span.outputs:
        if isinstance(doc, dict):
            content = doc.get('page_content', '')
            uri = doc.get('metadata', {}).get('doc_uri', '')
            score = doc.get('metadata', {}).get('relevance_score', 0)
            print(f"Document from {uri} (score: {score})")
```

## Advanced example

The context manager can be combined with `@mlflow.trace` function decorators and [Automatic Tracing](/concepts/automatic-tracing.md) (e.g., `mlflow.openai.autolog()`). The following example demonstrates a chat iteration that manually creates a `User` span with attributes, events, and inputs/outputs, while the OpenAI call is automatically traced. ^[span-tracing-with-context-managers-databricks-on-aws.md]

```python
from databricks_openai import DatabricksOpenAI
import [[mlflow|MLflow]]
from [[mlflow|MLflow]].entities import SpanEvent, SpanType
import time

[[mlflow|MLflow]].openai.autolog()
client = DatabricksOpenAI()

@mlflow.trace(span_type=SpanType.CHAIN)
def chat_iteration(messages, user_input):
    with [[mlflow|MLflow]].start_span(name="User", span_type=SpanType.CHAIN) as span:
        span.set_inputs({"messages": messages, "timestamp": time.time()})
        span.set_attribute("messages_length", len(messages))
        span.set_attributes({
            "environment": "production",
            "custom_metadata": {"key": "value"}
        })
        span.add_event(SpanEvent(
            name="processing_started",
            attributes={"stage": "initialization", "memory_usage_mb": 256}
        ))
        span.set_outputs(user_input)

    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="databricks-claude-sonnet-4-5",
        max_tokens=100,
        messages=messages,
    )
    answer = response.choices[0].message.content
    messages.append({"role": "assistant", "content": answer})
```

## Next steps

- Function decorators – Simpler approach for tracing entire functions.
- Low-level client APIs – Advanced scenarios requiring full control.
- Debug and analyze your app – Query and analyze logged [Traces](/concepts/traces.md).

## Sources

- span-tracing-with-context-managers-databricks-on-aws.md

# Citations

1. [span-tracing-with-context-managers-databricks-on-aws.md](/references/span-tracing-with-context-managers-databricks-on-aws-d67ed6d9.md)
