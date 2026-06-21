---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 25580e175f924b73a42452fde00599aaf4af0cf41c2a6fcb7f25e0c41e3f392b
  pageDirectory: concepts
  sources:
    - get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md
    - get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflowtrace-decorator
    - MLflow Tracing @trace Decorator
    - Manual Tracing with Decorators
    - Manual tracing with decorators
  citations:
    - file: function-decorators-databricks-on-aws.md
title: "@mlflow.trace decorator"
description: A Python decorator that wraps any function to automatically capture its inputs, outputs, and execution metadata as a span in an MLflow trace.
tags:
  - mlflow
  - tracing
  - decorator
  - python
timestamp: "2026-06-19T18:59:36.038Z"
---

# @mlflow.trace Decorator

The **`@mlflow.trace` decorator** allows you to create a span for any Python function, providing the simplest path to adding [MLflow Tracing](/concepts/mlflow-tracing.md) to your application with minimal code changes. It is a core component of manual tracing instrumentation in MLflow 3. ^[function-decorators-databricks-on-aws.md]

## Overview

The decorator automatically logs the function's name, inputs, outputs, and execution time. It also captures exceptions during function execution and records them as span events, enabling debugging through the MLflow UI. ^[function-decorators-databricks-on-aws.md]

Key capabilities:

- Detects parent-child relationships between functions, making it compatible with auto-tracing integrations. ^[function-decorators-databricks-on-aws.md]
- Can be used alongside auto-tracing features. ^[function-decorators-databricks-on-aws.md]
- Supports streaming outputs (generators and iterators) since MLflow 2.20.2. ^[function-decorators-databricks-on-aws.md]
- Thread-safe for multi-threaded applications. ^[function-decorators-databricks-on-aws.md]

## Prerequisites

- `mlflow[databricks]` 3.1 and above for core MLflow functionality with GenAI features and Databricks connectivity. ^[function-decorators-databricks-on-aws.md]
- Optional: `openai` 1.0.0 and above if your custom code interacts with OpenAI. ^[function-decorators-databricks-on-aws.md]

## Basic usage

The following is a minimum example of using the decorator for tracing Python functions:

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

^[function-decorators-databricks-on-aws.md]

When a trace contains multiple spans with the same name, MLflow appends an auto-incrementing suffix to them, such as `_1`, `_2`. ^[function-decorators-databricks-on-aws.md]

## Customizing spans

The `@mlflow.trace` decorator accepts the following arguments to customize the created span: ^[function-decorators-databricks-on-aws.md]

- **`name`**: Overrides the span name from the default (the name of the decorated function).
- **`span_type`**: Sets the type of span. Can be one of the built-in Span Types or a custom string.
- **`attributes`**: Adds custom attributes to the span.

Example with custom parameters:

```python
@mlflow.trace(
    name="call-local-llm",
    span_type=SpanType.LLM,
    attributes={"model": "gpt-4o-mini"}
)
def invoke(prompt: str):
    return client.invoke(
        messages=[{"role": "user", "content": prompt}],
        model="gpt-4o-mini"
    )
```

^[function-decorators-databricks-on-aws.md]

## Dynamic span updates

You can update an active span dynamically inside the function using `mlflow.get_current_active_span()`:

```python
@mlflow.trace(span_type=SpanType.LLM)
def invoke(prompt: str):
    model_id = "gpt-4o-mini"
    span = mlflow.get_current_active_span()
    span.set_attributes({"model": model_id})
    return client.invoke(
        messages=[{"role": "user", "content": prompt}],
        model=model_id
    )
```

^[function-decorators-databricks-on-aws.md]

## Decorator ordering

When applying multiple decorators to a single function, `@mlflow.trace` must be the **outermost** decorator (the one at the very top). This ensures that MLflow captures the entire execution of the function, including the behavior of any inner decorators. If `@mlflow.trace` is not the outermost decorator, its visibility into the function's execution may be limited or incorrect, potentially leading to incomplete traces or misrepresentation of the function's inputs, outputs, and execution time. ^[function-decorators-databricks-on-aws.md]

```python
# Correct order: @mlflow.trace is outermost
@mlflow.trace(name="my_decorated_function_correct_order")
@simple_timing_decorator
def my_complex_function(x, y):
    time.sleep(0.1)
    return x + y

# Incorrect order: @mlflow.trace is NOT outermost
@simple_timing_decorator
@mlflow.trace(name="my_decorated_function_incorrect_order")
def my_other_complex_function(x, y):
    time.sleep(0.1)
    return x * y
```

^[function-decorators-databricks-on-aws.md]

## Adding trace-level tags

Tags can be added to traces to provide additional metadata at the trace level:

```python
@mlflow.trace
def my_func(x):
    mlflow.update_current_trace(tags={"fruit": "apple"})
    return x + 1
```

^[function-decorators-databricks-on-aws.md]

## Customizing request and response previews

The Traces tab in the MLflow UI displays a `Request` and `Response` column showing previews of each trace's end-to-end input and output. You can customize what's shown in these columns using the `request_preview` and `response_preview` parameters within `mlflow.update_current_trace()`: ^[function-decorators-databricks-on-aws.md]

```python
@mlflow.trace(name="Summarization Pipeline")
def summarize_document(document_content: str, user_instructions: str):
    request_p = f"Doc: {document_content[:30]}... Instr: {user_instructions[:30]}..."
    mlflow.update_current_trace(request_preview=request_p)
    
    summary = f"Summary of document starting with '{document_content[:20]}...' based on '{user_instructions}'"
    response_p = f"Summary: {summary[:50]}..."
    mlflow.update_current_trace(response_preview=response_p)
    return summary
```

^[function-decorators-databricks-on-aws.md]

## Automatic exception handling

If an `Exception` is raised during processing of a trace-instrumented operation, an indication is shown within the UI that the invocation was not successful and a partial capture of data is available for debugging. Details about the exception are included within the `Events` of the partially completed span. ^[function-decorators-databricks-on-aws.md]

## Streaming outputs

Since MLflow 2.20.2, the `@mlflow.trace` decorator supports tracing functions that return a generator or an iterator: ^[function-decorators-databricks-on-aws.md]

```python
@mlflow.trace
def stream_data():
    for i in range(5):
        yield i
```

A span for a stream function starts when the returned iterator begins to be **consumed** and ends when the iterator is exhausted or an exception is raised during iteration. By default, MLflow captures all yielded elements as a list in the span's output. ^[function-decorators-databricks-on-aws.md]

### Output reducers

Use the `output_reducer` parameter to specify a custom function that aggregates yielded elements into a single span output: ^[function-decorators-databricks-on-aws.md]

```python
@mlflow.trace(output_reducer=lambda x: ",".join(x))
def stream_data():
    for c in "hello":
        yield c
```

The raw chunks remain accessible in the `Events` tab of the span in the MLflow Trace UI for inspection during debugging. ^[function-decorators-databricks-on-aws.md]

## Complex workflow tracing with nested spans

For complex workflows with multiple steps, combine `@mlflow.trace` with `mlflow.start_span()` context managers for nested execution flow: ^[function-decorators-databricks-on-aws.md]

```python
@mlflow.trace(name="data_pipeline")
def process_data_pipeline(data_source: str):
    with mlflow.start_span(name="extract") as extract_span:
        raw_data = extract_from_source(data_source)
        extract_span.set_outputs({"record_count": len(raw_data)})
    
    with mlflow.start_span(name="transform") as transform_span:
        transformed = apply_transformations(raw_data)
        transform_span.set_outputs({"transformed_count": len(transformed)})
    
    with mlflow.start_span(name="load") as load_span:
        result = load_to_destination(transformed)
        load_span.set_outputs({"status": "success"})
    
    return result
```

^[function-decorators-databricks-on-aws.md]

## Multi-threading support

[MLflow Tracing](/concepts/mlflow-tracing.md) is thread-safe, with traces isolated by default per thread using Python's `ContextVar` mechanism. To create a trace that spans multiple threads, manually copy the context from the main thread to the worker thread using `contextvars.copy_context()`: ^[function-decorators-databricks-on-aws.md]

```python
import contextvars
from concurrent.futures import ThreadPoolExecutor

@mlflow.trace
def worker(question: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": question}],
    )
    return response.choices[0].message.content

@mlflow.trace
def main(questions: list[str]) -> list[str]:
    results = []
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = []
        for question in questions:
            ctx = contextvars.copy_context()
            futures.append(executor.submit(ctx.run, worker, question))
        for future in as_completed(futures):
            results.append(future.result())
    return results
```

^[function-decorators-databricks-on-aws.md]

In contrast, `ContextVar` is copied to **async** tasks by default, so no manual copying is needed when using `asyncio`. ^[function-decorators-databricks-on-aws.md]

## Supported function types

The `@mlflow.trace` decorator currently supports: ^[function-decorators-databricks-on-aws.md]

- Synchronous functions
- Async functions
- Generators and iterators (since MLflow 2.20.2)

## Related concepts

- Span — The basic unit of tracing
- Span Types — Built-in span type classifications
- [Manual Tracing](/concepts/manual-tracing.md) — Alternative approaches including context managers and low-level APIs
- [Auto-tracing](/concepts/automatic-tracing.md) — Automatic instrumentation for supported libraries
- [MLflow Tracing Integrations](/concepts/mlflow-tracing-integrations.md) — 20+ libraries with automatic tracing support
- Debug and observe your app with traces — Using traces for application debugging

## Sources

- function-decorators-databricks-on-aws.md
- get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md
- get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md

# Citations

1. [function-decorators-databricks-on-aws.md](/references/function-decorators-databricks-on-aws-0ffe82de.md)
