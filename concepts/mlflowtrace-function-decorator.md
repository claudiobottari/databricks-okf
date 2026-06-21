---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 307e3cca041d77e05aa33815f1d577355727a7f929a1deee36f19457c0f1040a
  pageDirectory: concepts
  sources:
    - function-decorators-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflowtrace-function-decorator
    - "@FD"
    - Function Decorator APIs
    - Function Decorators
    - Span Tracing with Function Decorators
    - function decorator API
  citations:
    - file: function-decorators-databricks-on-aws.md
title: "@mlflow.trace Function Decorator"
description: A Python decorator that creates a span for any function, automatically logging function name, inputs, outputs, and execution time with minimal code changes.
tags:
  - mlflow
  - tracing
  - decorator
timestamp: "2026-06-19T18:57:03.850Z"
---

# @mlflow.trace Function Decorator

The `@mlflow.trace` decorator enables you to create a span for any Python function with minimal code changes. It provides the simplest path to adding [tracing](/concepts/mlflow-tracing.md) to your MLflow-instrumented applications.^[function-decorators-databricks-on-aws.md]

## Overview

When applied to a function, `@mlflow.trace` automatically logs the function's name, inputs, outputs, and execution time. It detects parent-child relationships between functions, making it compatible with auto-tracing integrations. The decorator also captures exceptions during function execution and records them as span events.^[function-decorators-databricks-on-aws.md]

### Prerequisites

- `mlflow[databricks]` 3.1 and above for core MLflow functionality with GenAI features and Databricks connectivity
- `openai` 1.0.0 and above (optional, only if your custom code interacts with OpenAI)

^[function-decorators-databricks-on-aws.md]

## Basic Usage

The following example demonstrates minimum usage of the decorator for tracing Python functions:

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

When a trace contains multiple spans with the same name, MLflow appends an auto-incrementing suffix to them, such as `_1`, `_2`.^[function-decorators-databricks-on-aws.md]

## Customizing Spans

The `@mlflow.trace` decorator accepts the following arguments to customize the span:

- **`name`**: Overrides the span name from the default (the name of the decorated function)
- **`span_type`**: Sets the type of span. Use either a built-in [Span Types|Span Type](/concepts/span-types-and-lifecycle.md) or a custom string
- **`attributes`**: Adds custom attributes to the span

^[function-decorators-databricks-on-aws.md]

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

Alternatively, you can update an active or live span dynamically inside the function using `mlflow.get_current_active_span()`:

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

See Span Tracing for more examples of editing `LiveSpan` objects.^[function-decorators-databricks-on-aws.md]

## Decorator Order

When applying multiple decorators to a single function, `@mlflow.trace` must be the **outermost** decorator (the one at the very top). This ensures that MLflow can capture the entire execution of the function, including the behavior of any inner decorators. If `@mlflow.trace` is not the outermost decorator, its visibility into the function's execution may be limited or incorrect, potentially leading to incomplete traces or misrepresentation of inputs, outputs, and execution time.^[function-decorators-databricks-on-aws.md]

```python
# Correct order: @mlflow.trace is outermost
@mlflow.trace(name="my_decorated_function_correct_order")
@simple_timing_decorator
# @another_framework_decorator
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

## Adding Tags to Traces

Tags can be added to traces to provide additional metadata at the trace level:

```python
@mlflow.trace
def my_func(x):
    mlflow.update_current_trace(tags={"fruit": "apple"})
    return x + 1
```

^[function-decorators-databricks-on-aws.md]

## Customizing Request and Response Previews

The Traces tab in the MLflow UI displays a list of traces with `Request` and `Response` columns showing previews of end-to-end inputs and outputs. You can customize what's shown in these columns using the `request_preview` and `response_preview` parameters within `mlflow.update_current_trace()`. This is particularly useful for complex inputs or outputs where default truncation might not show the most relevant information.^[function-decorators-databricks-on-aws.md]

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

## Automatic Exception Handling

If an `Exception` is raised during processing of a trace-instrumented operation, the UI will show the invocation was not successful and a partial capture of data will be available for debugging. Details about the Exception are included within `Events` of the partially completed span, aiding identification of where issues are occurring within your code.^[function-decorators-databricks-on-aws.md]

## Streaming Outputs

Since MLflow 2.20.2, the `@mlflow.trace` decorator can trace functions that return a generator or iterator. A span for a stream function starts when the returned iterator begins to be **consumed** and ends when the iterator is exhausted or an exception is raised during iteration. By default, MLflow captures all yielded elements as a list in the span's output.^[function-decorators-databricks-on-aws.md]

```python
@mlflow.trace
def stream_data():
    for i in range(5):
        yield i
```

This generates a trace with a single span whose output is `[0, 1, 2, 3, 4]`.^[function-decorators-databricks-on-aws.md]

### Using Output Reducers

The `output_reducer` parameter allows you to specify a custom function to aggregate yielded elements into a single span output. The custom function takes a list of yielded elements as input. Raw chunks remain available in the `Events` tab of the span in the MLflow Trace UI for debugging individual yielded values.^[function-decorators-databricks-on-aws.md]

```python
from typing import List, Any

@mlflow.trace(output_reducer=lambda x: ",".join(x))
def stream_data():
    for c in "hello":
        yield c
```

The span output becomes `"h,e,l,l,o"`.^[function-decorators-databricks-on-aws.md]

Common output reducer patterns include:
- **Token aggregation**: Concatenating streaming tokens into complete text
- **Metrics aggregation**: Aggregating streaming metrics into summary statistics
- **Error collection**: Separating successful results from errors
- **Multi-model response aggregation**: Aggregating responses from multiple models

^[function-decorators-databricks-on-aws.md]

## Multi-Threading

[MLflow Tracing](/concepts/mlflow-tracing.md) is thread-safe, with traces isolated by default per thread using Python's built-in `ContextVar` mechanism. To create a trace spanning multiple threads, you must manually copy the context from the main thread to the worker thread.^[function-decorators-databricks-on-aws.md]

```python
import contextvars
from concurrent.futures import ThreadPoolExecutor

@mlflow.trace
def worker(question: str) -> str:
    # ... work with OpenAI client
    return response

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

In contrast, `ContextVar` is copied to async tasks by default, so manual context copying is not needed when using `asyncio`.^[function-decorators-databricks-on-aws.md]

## Supported Function Types

The `@mlflow.trace` decorator supports standard functions, generators/iterators (for streaming outputs), and functions used with auto-tracing integrations.^[function-decorators-databricks-on-aws.md]

## Combining with Auto-Tracing

Manual tracing seamlessly integrates with MLflow's auto-tracing capabilities. See [Combine manual and automatic tracing](/concepts/combined-manual-and-automatic-tracing.md) for details.^[function-decorators-databricks-on-aws.md]

## Related Concepts

- Span Tracing — Trace specific code blocks with more granular control
- Low-Level Client APIs — Advanced scenarios requiring full control
- [Auto-Tracing](/concepts/automatic-tracing.md) — Automatic instrumentation of supported frameworks
- Spans — The fundamental unit of tracing in MLflow
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizational unit for MLflow runs

## Sources

- function-decorators-databricks-on-aws.md

# Citations

1. [function-decorators-databricks-on-aws.md](/references/function-decorators-databricks-on-aws-0ffe82de.md)
