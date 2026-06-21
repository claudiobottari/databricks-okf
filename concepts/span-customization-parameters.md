---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4d1b80cc384f59fc33402ea8a33867d9f781c155181da303e115ba32b15e075c
  pageDirectory: concepts
  sources:
    - function-decorators-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - span-customization-parameters
    - SCP
    - span-customization-via-decorator-parameters
    - SCVDP
  citations:
    - file: function-decorators-databricks-on-aws.md
title: Span customization parameters
description: The @mlflow.trace decorator accepts name, span_type, and attributes parameters to customize span metadata, with optional dynamic updates via mlflow.get_current_active_span().
tags:
  - mlflow
  - tracing
  - span-configuration
timestamp: "2026-06-18T12:27:57.181Z"
---

# Span customization parameters

**Span customization parameters** are attributes you can set when creating or modifying spans in [MLflow Tracing](/concepts/mlflow-tracing.md). They allow you to control the span’s name, type, metadata, and how its inputs and outputs appear in the UI. Customization is available both at creation time (via the `@mlflow.trace` decorator or `start_span` context manager) and dynamically (by retrieving the active span and updating its properties). ^[function-decorators-databricks-on-aws.md]

## Decorator-level parameters

The [`@mlflow.trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.trace) decorator accepts the following arguments to shape the span it creates:

| Parameter | Description | Example |
|-----------|-------------|---------|
| `name`     | Overrides the default span name (the decorated function’s name). | `@mlflow.trace(name="call-llm")` |
| `span_type` | Sets the semantic type of the span. Can be a built-in `SpanType` enum value or an arbitrary string. | `@mlflow.trace(span_type=SpanType.LLM)` or `@mlflow.trace(span_type="my_custom_type")` |
| `attributes` | A dictionary of key-value pairs attached to the span as metadata. | `@mlflow.trace(attributes={"model": "gpt-4o-mini"})` |

These parameters are set when the decorator is applied. ^[function-decorators-databricks-on-aws.md]

## Dynamic span customization

Inside a traced function you can retrieve the current active span with [`mlflow.get_current_active_span()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.get_current_active_span) and modify it in real time. The returned object is a [`LiveSpan`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.LiveSpan) whose `.set_attributes()` method accepts a dictionary of attributes:

```python
span = mlflow.get_current_active_span()
span.set_attributes({"model": "gpt-4o-mini"})
```

This approach is useful when the attribute value is not known until the function executes. ^[function-decorators-databricks-on-aws.md]

## Trace-level preview customization

The **Traces tab** in the MLflow UI shows `Request` and `Response` columns with truncated previews of the trace’s overall input and output. You can override these previews by calling [`mlflow.update_current_trace()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.update_current_trace) with the `request_preview` and `response_preview` parameters:

```python
mlflow.update_current_trace(
    request_preview="Doc: First 30 chars... Instr: short...",
    response_preview="Summary: First 50 chars..."
)
```

This is especially helpful for complex or long inputs/outputs where the default truncation may hide the most relevant information. ^[function-decorators-databricks-on-aws.md]

## Output reducers for streaming spans

When a traced function is a generator (Python 3.9+), the span is not finalized until the generator is exhausted. By default, the span’s `output` is a list of all yielded elements. You can control how that list is aggregated by supplying the `output_reducer` parameter to `@mlflow.trace`:

```python
@mlflow.trace(output_reducer=lambda chunks: ",".join(chunks))
def stream_text():
    yield "Hello"; yield " "; yield "World"
```

The `output_reducer` receives the full list of yielded chunks and must return a single value that becomes the span’s output. Common patterns include concatenating tokens, computing summary statistics, or parsing JSON. The raw chunks remain visible in the span’s **Events** tab in the UI. ^[function-decorators-databricks-on-aws.md]

## Combining customization with other decorators

When [`@mlflow.trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.trace) is used alongside other decorators (e.g., from Flask or other frameworks), it must be the **outermost** decorator so that MLflow can capture the full execution of the function, including modifications made by inner decorators. ^[function-decorators-databricks-on-aws.md]

## Related concepts

- Span Types – The built-in `SpanType` enum values (e.g., `LLM`, `CHAIN`, `AGENT`).
- [Trace](/concepts/traces.md) – The top-level container that groups spans.
- LiveSpan – The object returned by `get_current_active_span()` for dynamic updates.
- [Output Reducer](/concepts/output-reducers.md) – The `output_reducer` mechanism for streaming spans.
- [Manual Tracing](/concepts/manual-tracing.md) – General guidance on instrumenting code with spans.
- [@mlflow.trace decorator](/concepts/mlflowtrace-decorator.md) – API reference for the decorator.

## Sources

- function-decorators-databricks-on-aws.md

# Citations

1. [function-decorators-databricks-on-aws.md](/references/function-decorators-databricks-on-aws-0ffe82de.md)
