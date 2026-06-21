---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2374bc7a61d0680cc08deac0ea17a016184a906c14fa97e0cdc3263e14c8c0af
  pageDirectory: concepts
  sources:
    - span-tracing-with-context-managers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hybrid-tracing-patterns
    - HTP
  citations:
    - file: span-tracing-with-context-managers-databricks-on-aws.md
title: Hybrid Tracing Patterns
description: Combining mlflow.start_span() context managers, @mlflow.trace function decorators, and automatic tracing (autolog) for comprehensive application observability.
tags:
  - mlflow
  - tracing
  - patterns
  - instrumentation
timestamp: "2026-06-19T23:06:43.684Z"
---

# Hybrid Tracing Patterns

**Hybrid Tracing Patterns** refer to the practice of combining multiple tracing techniques within a single application to capture different levels of detail—from coarse-grained function calls to fine-grained code-block interactions. In [MLflow](/concepts/mlflow.md)'s [GenAI Tracing](/concepts/mlflow-genai-tracing.md) framework, developers can mix [Function Decorators](/concepts/mlflowtrace-function-decorator.md), the mlflow.start_span() Context Manager|Start Span Context Manager, and [Automatic Tracing](/concepts/automatic-tracing.md) in the same script to get a complete picture of their application's execution. ^[span-tracing-with-context-managers-databricks-on-aws.md]

## Overview

Hybrid tracing is useful when the granularity offered by a single technique is insufficient. For example, a function decorator might trace the high-level conversation loop, but you also want to inspect individual intermediate steps inside that loop. Hybrid tracing lets you overlay fine-grained context-manager spans onto coarser function-decorated [Traces](/concepts/traces.md). ^[span-tracing-with-context-managers-databricks-on-aws.md]

## Core Techniques

### Start Span Context Manager

The [`mlflow.start_span()`](https://[MLflow](/concepts/mlflow.md).org/docs/latest/api_reference/python_api/[MLflow](/concepts/mlflow.md).html#mlflow.start_span) context manager creates spans for arbitrary code blocks. Unlike function decorators, it requires you to provide the span name, inputs, and outputs manually via the returned [`LiveSpan`](https://[MLflow](/concepts/mlflow.md).org/docs/latest/api_reference/python_api/[MLflow](/concepts/mlflow.md).entities.html#mlflow.entities.LiveSpan) object. The context manager automatically handles parent-child relationships, exceptions, and execution time. ^[span-tracing-with-context-managers-databricks-on-aws.md]

```python
import [[mlflow|MLflow]]

with [[mlflow|MLflow]].start_span(name="my_span") as span:
    x = 1
    y = 2
    span.set_inputs({"x": x, "y": y})
    z = x + y
    span.set_outputs(z)
```

### Function Decorators

The `@mlflow.trace` decorator is a simpler approach that [Traces](/concepts/traces.md) entire functions. It is the most common companion to the context manager in a hybrid setup. ^[span-tracing-with-context-managers-databricks-on-aws.md]

### [Automatic Tracing](/concepts/automatic-tracing.md)

[Automatic Tracing](/concepts/automatic-tracing.md) (e.g., `mlflow.openai.autolog()`) captures calls to supported SDKs like the OpenAI client without manual instrumentation. It can run alongside both the context manager and decorator. ^[span-tracing-with-context-managers-databricks-on-aws.md]

## Span Events and Status

Hybrid tracing also supports [SpanEvents](/concepts/spanevent-objects.md), [SpanStatus](/concepts/spanstatus-api.md), and [SpanStatusCodes](/concepts/spanstatus-api.md). The code snippet below shows how to create events with different timestamps and how to set span status: ^[span-tracing-with-context-managers-databricks-on-aws.md]

```python
from [[mlflow|MLflow]].entities import SpanEvent, SpanStatus, SpanStatusCode, SpanType
import time

with [[mlflow|MLflow]].start_span(name="manual_span", span_type=SpanType.CHAIN) as span:
    # Event with current timestamp
    event = SpanEvent(
        name="validation_completed",
        attributes={"records_validated": 1000, "errors_found": 3}
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
        span.add_event(error_event)

    # Set status
    success_status = SpanStatus(SpanStatusCode.OK)
    span.set_status(success_status)
```

## `RETRIEVER` Spans

[RETRIEVER Spans](/concepts/retriever-spans.md) are a special span type used for document retrieval. They must output a list of `Document` objects. In a hybrid trace, a retriever span might be created by a decorated function that manually constructs `Document` objects: ^[span-tracing-with-context-managers-databricks-on-aws.md]

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
        )
    ]
    span.set_outputs(documents)
    return [doc.to_dict() for doc in documents]
```

## Advanced Example

The following example combines all three techniques: `@mlflow.trace` for high-level functions, `mlflow.start_span()` for intermediate logic, and `mlflow.openai.autolog()` for automatic capture of API calls: ^[span-tracing-with-context-managers-databricks-on-aws.md]

```python
from databricks_openai import DatabricksOpenAI
import [[mlflow|MLflow]]
from [[mlflow|MLflow]].entities import SpanEvent, SpanType
import openai
import time

[[mlflow|MLflow]].openai.autolog()

client = DatabricksOpenAI()

@mlflow.trace(span_type=SpanType.CHAIN)
def chat_iteration(messages, user_input):
    with [[mlflow|MLflow]].start_span(name="User", span_type=SpanType.CHAIN) as span:
        span.set_inputs({
            "messages": messages,
            "timestamp": time.time(),
        })
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
    print(f"Assistant: {answer}")
    messages.append({"role": "assistant", "content": answer})

chat_iteration(
    messages=[{"role": "system", "content": "You are a friendly chat bot"}],
    user_input="What is your favorite color?"
)
```

## Benefits

- **Fine-grained control**: Trace individual code blocks, not just whole functions.
- **Automatic parent-child relationships**: [MLflow](/concepts/mlflow.md) handles span hierarchy and cleanup.
- **Exception handling**: Both decorators and context managers capture errors automatically.
- **Mix and match**: Use the simplest technique for each part of the code. ^[span-tracing-with-context-managers-databricks-on-aws.md]

## Related Concepts

- [Function Decorators](/concepts/mlflowtrace-function-decorator.md) – A simpler approach for tracing entire functions.
- mlflow.start_span() Context Manager|Start Span Context Manager – Create spans for arbitrary code blocks.
- [Automatic Tracing](/concepts/automatic-tracing.md) – Auto-capture calls to supported SDKs.
- [RETRIEVER Spans](/concepts/retriever-spans.md) – Special span type for document retrieval.
- [SpanEvents](/concepts/spanevent-objects.md) – Record specific occurrences during a span's lifetime.
- [SpanStatus and SpanStatusCodes](/concepts/spanstatus-api.md) – Define the status of a span.

## Sources

- span-tracing-with-context-managers-databricks-on-aws.md

# Citations

1. [span-tracing-with-context-managers-databricks-on-aws.md](/references/span-tracing-with-context-managers-databricks-on-aws-d67ed6d9.md)
