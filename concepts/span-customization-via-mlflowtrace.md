---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 90bc7156c3c05fdbf768c8f6f3adac07d8be934225c251ce2f93e48b595bf23d
  pageDirectory: concepts
  sources:
    - function-decorators-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - span-customization-via-mlflowtrace
    - SCV@
  citations:
    - file: function-decorators-databricks-on-aws.md
title: Span Customization via @mlflow.trace
description: Customizing created spans through decorator parameters (name, span_type, attributes) and dynamically via mlflow.get_current_active_span().
tags:
  - mlflow
  - tracing
  - span-configuration
timestamp: "2026-06-19T10:41:54.727Z"
---

# Span Customization via `@mlflow.trace`

The `@mlflow.trace` decorator provides the simplest path to adding [tracing](/concepts/mlflow-tracing.md) to Python functions. Beyond basic tracing, it offers several parameters and complementary APIs that let you customize how spans are created, named, attributed, and displayed. ^[function-decorators-databricks-on-aws.md]

## Overview

When you decorate a function with `@mlflow.trace`, MLflow automatically creates a span that captures the function's name, inputs, outputs, and execution time. The decorator supports:

- Overriding the span name and type.
- Adding custom attributes (key-value metadata) at decoration time or dynamically inside the function.
- Controlling how the trace’s request and response are previewed in the UI.
- Aggregating streaming outputs via an `output_reducer`.
- Seamless integration with auto-tracing features and other decorators (when placed outermost).

All of these capabilities are exposed through the `@mlflow.trace` decorator arguments and the `mlflow.get_current_active_span()` and `mlflow.update_current_trace()` APIs. ^[function-decorators-databricks-on-aws.md]

## Prerequisites

- MLflow 3.x with `mlflow[databricks]` ≥ 3.1 installed.
- Python ≥ 3.8.

```python
%pip install --upgrade "mlflow[databricks]>=3.1"
```

(Optional: install `openai` ≥ 1.0.0 if using OpenAI integrations.) ^[function-decorators-databricks-on-aws.md]

## Basic Example

```python
import mlflow

@mlflow.trace(span_type="func", attributes={"key": "value"})
def add_1(x):
    return x + 1

@mlflow.trace(span_type="func", attributes={"key1": "value1"})
def minus_1(x):
    return x - 1

@mlflow.trace(name="Trace Test")
def trace_test(x):
    step1 = add_1(x)
    return minus_1(step1)

trace_test(4)
```

This creates a trace with three spans. The root span is named `"Trace Test"` (overriding the function name `trace_test`), and each child span carries the attributes defined in its decorator. ^[function-decorators-databricks-on-aws.md]

## Customizing Spans

### Span Name

By default, the span name equals the decorated function's name. Use the `name` parameter to override it:

```python
@mlflow.trace(name="call-local-llm")
def invoke(prompt: str):
    ...
```

### Span Type

Set the `span_type` parameter to one of the built-in Span Types (e.g., `SpanType.LLM`, `SpanType.FUNCTION`) or a custom string.

```python
from mlflow.entities import SpanType

@mlflow.trace(span_type=SpanType.LLM, attributes={"model": "gpt-4o-mini"})
def invoke(prompt: str):
    ...
```

### Static Attributes

Use the `attributes` parameter to attach key-value pairs to the span at creation time.

```python
@mlflow.trace(attributes={"model": "gpt-4o-mini", "version": "2.1"})
```

### Dynamic Attributes (Inside the Function)

Use `mlflow.get_current_active_span()` to retrieve the LiveSpan object and call `set_attributes()` on it:

```python
@mlflow.trace(span_type=SpanType.LLM)
def invoke(prompt: str):
    span = mlflow.get_current_active_span()
    span.set_attributes({"model": "gpt-4o-mini", "temperature": 0.7})
    ...
```

### Trace-Level Tags

To add metadata at the trace level (visible across all spans), use `mlflow.update_current_trace()`:

```python
@mlflow.trace
def my_func(x):
    mlflow.update_current_trace(tags={"fruit": "apple"})
    return x + 1
```

## Customizing Request and Response Previews

The **Traces** tab in the MLflow UI shows a preview of each trace's input (Request) and output (Response). By default, these are truncated. You can control what appears using `request_preview` and `response_preview` in `mlflow.update_current_trace()`:

```python
@mlflow.trace(name="Summarization Pipeline")
def summarize_document(document_content: str, user_instructions: str):
    request_p = f"Doc: {document_content[:30]}... Instr: {user_instructions[:30]}..."
    mlflow.update_current_trace(request_preview=request_p)
    summary = f"Summary of document starting with '{document_content[:20]}...'"
    response_p = f"Summary: {summary[:50]}..."
    mlflow.update_current_trace(response_preview=response_p)
    return summary
```

This is especially useful for complex inputs or long outputs where the default truncation may hide the most relevant information. ^[function-decorators-databricks-on-aws.md]

## Automatic Exception Handling

If the decorated function raises an `Exception`, MLflow captures the partial span and marks the invocation as unsuccessful in the UI. Details of the exception are recorded as span **Events**, making debugging easier.

![Trace Error](https://assets.docs.databricks.com/_static/images/mlflow3/tracing/trace-exception.gif)

## Combining with Auto-Tracing

Manual `@mlflow.trace` decorators work alongside MLflow's auto-tracing features (e.g., `mlflow.openai.autolog()`). The decorator sets the correct parent–child relationships with auto-generated spans, giving you full visibility into both custom logic and library calls. ^[function-decorators-databricks-on-aws.md]

## Complex Workflow Tracing

For multi-step pipelines, you can nest mlflow.start_span() Context Manager|context manager spans inside the decorated function. The decorator creates the root span; inner spans can be added with `mlflow.start_span()`:

```python
@mlflow.trace(name="data_pipeline")
def process_data_pipeline(data_source: str):
    with mlflow.start_span(name="extract") as extract_span:
        raw_data = extract_from_source(data_source)
        extract_span.set_outputs({"record_count": len(raw_data)})
    with mlflow.start_span(name="transform") as transform_span:
        transformed = apply_transformations(raw_data)
        transform_span.set_outputs({"transformed_count": len(transformed)})
    # ...
```

## Multi‑Threading

[MLflow Tracing](/concepts/mlflow-tracing.md) is thread‑safe by default because it uses Python’s `ContextVar`. However, `ContextVar` is not propagated across threads automatically. To trace work in a `ThreadPoolExecutor`, copy the context from the main thread with `contextvars.copy_context()` and run the worker inside that context:

```python
import contextvars
from concurrent.futures import ThreadPoolExecutor

@mlflow.trace
def worker(question: str) -> str:
    ...

@mlflow.trace
def main(questions: list[str]) -> list[str]:
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = []
        for question in questions:
            ctx = contextvars.copy_context()
            futures.append(executor.submit(ctx.run, worker, question))
        # ...
```

For `asyncio`-based concurrency, `ContextVar` is automatically copied to tasks, so no manual copying is needed. ^[function-decorators-databricks-on-aws.md]

## Streaming Outputs

Since MLflow 2.20.2, `@mlflow.trace` can decorate generator functions. The span remains open until the generator is exhausted. By default, all yielded values are collected into a list and set as the span’s output.

### Using Output Reducers

The `output_reducer` parameter accepts a callable that receives the list of yielded chunks and returns a single aggregated value. This is useful for consolidating streaming LLM responses, metrics, or errors.

```python
@mlflow.trace(output_reducer=lambda x: ",".join(x))
def stream_data():
    for c in "hello":
        yield c
# Output: "h,e,l,l,o"
```

Common patterns include:

- **Token aggregation**: `"".join(chunks)`
- **Metrics aggregation**: compute count, sum, average, max, min.
- **JSON parsing**: clean markdown wrappers and parse JSON from LLM output.
- **Multi‑model response aggregation**: combine results from several models.

The raw chunks remain visible in the span’s **Events** tab for debugging. ^[function-decorators-databricks-on-aws.md]

### Testing Output Reducers

Reducers can be unit‑tested independently of the tracing framework, as they are plain functions receiving a list of chunks.

## Using `@mlflow.trace` with Other Decorators

When applying multiple decorators, `@mlflow.trace` **must be the outermost decorator** (the one at the very top). This ensures MLflow captures the full execution including modifications made by inner decorators (e.g., timing, logging, or web‑framework decorators).

```python
# Correct order
@mlflow.trace(name="my_decorated_function_correct_order")
@simple_timing_decorator
def my_complex_function(x, y):
    ...
```

If `@mlflow.trace` is placed below another decorator, the trace may miss input/output transformations or execution time introduced by the outer decorator. ^[function-decorators-databricks-on-aws.md]

## Supported Function Types

`@mlflow.trace` supports:

- Synchronous functions
- Asynchronous functions (`async def`)
- Generator functions (with optional `output_reducer`)
- Functions decorated with other wrappers (when `@mlflow.trace` is outermost)

## Next Steps

- mlflow.start_span() Context Manager|Span Tracing with Context Managers – finer control over span boundaries.
- Low‑Level Client APIs – advanced scenarios requiring direct span creation.
- Auto‑tracing Integrations – use `@mlflow.trace` alongside OpenAI, LangChain, etc.
- [Debug and Observe with Traces](/concepts/genai-trace-analysis-and-debugging.md) – explore the trace UI and filtering.

## Related Concepts

- Spans and [Traces](/concepts/traces.md)
- Span Types
- LiveSpan – the object returned by `mlflow.get_current_active_span()`
- [OpenAI autolog](/concepts/mlflow-openai-autologging.md) – automatic tracing for OpenAI calls
- Context Managers – for nesting spans inside a decorated function

## Sources

- function-decorators-databricks-on-aws.md

# Citations

1. [function-decorators-databricks-on-aws.md](/references/function-decorators-databricks-on-aws-0ffe82de.md)
