---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f431df743a285cf2f20b666268d2681fec048a0466be0b8e44273277b1408020
  pageDirectory: concepts
  sources:
    - function-decorators-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - span-customization-via-decorator-parameters
    - SCVDP
  citations:
    - file: function-decorators-databricks-on-aws.md
title: Span Customization via Decorator Parameters
description: The @mlflow.trace decorator accepts name, span_type, and attributes parameters to customize spans, and allows dynamic attribute updates via mlflow.get_current_active_span().
tags:
  - mlflow
  - tracing
  - customization
timestamp: "2026-06-19T18:56:22.311Z"
---

# Span Customization via Decorator Parameters

The `@mlflow.trace` decorator allows you to customize the Span created for any traced function through its parameters. This is the simplest path to adding tracing with minimal code changes, and it supports both static configuration at decoration time and dynamic updates during execution. ^[function-decorators-databricks-on-aws.md]

## Static Parameters

The decorator accepts three primary arguments that define the span's metadata:

- **`name`** – Overrides the span name from the default (the name of the decorated function) to a custom string.
- **`span_type`** – Sets the type of span. Use one of the built-in Span Types or any arbitrary string.
- **`attributes`** – Adds custom key‑value pairs (attributes) to the span.

Example usage:

```python
@mlflow.trace(
    name="call-local-llm",
    span_type=SpanType.LLM,
    attributes={"model": "gpt-4o-mini"}
)
def invoke(prompt: str):
    return client.invoke(messages=[...], model="gpt-4o-mini")
```

^[function-decorators-databricks-on-aws.md]

## Dynamic Customization

When you need to set attributes that are only known at runtime, you can update the active span inside the function body using `mlflow.get_current_active_span()`. This method returns the LiveSpan object created by the decorator, allowing you to call `set_attributes()` on it. ^[function-decorators-databricks-on-aws.md]

```python
@mlflow.trace(span_type=SpanType.LLM)
def invoke(prompt: str):
    model_id = "gpt-4o-mini"
    span = mlflow.get_current_active_span()
    span.set_attributes({"model": model_id})
    return client.invoke(messages=[...], model=model_id)
```

## Customizing Request/Response Previews

For traces that represent end‑to‑end interactions, you can control what appears in the **Request** and **Response** columns of the MLflow UI by calling `mlflow.update_current_trace()` with the parameters `request_preview` and `response_preview`. This is useful when the default truncated preview does not show the most relevant information. ^[function-decorators-databricks-on-aws.md]

```python
@mlflow.trace(name="Summarization Pipeline")
def summarize_document(document_content: str, user_instructions: str):
    request_p = f"Doc: {document_content[:30]}... Instr: {user_instructions[:30]}..."
    mlflow.update_current_trace(request_preview=request_p)
    # ... perform LLM call ...
    summary = "..."  # generated summary
    response_p = f"Summary: {summary[:50]}..."
    mlflow.update_current_trace(response_preview=response_p)
    return summary
```

## Streaming Outputs and Output Reducers

When a traced function is a generator (returning an iterator), the decorator, since MLflow 2.20.2, captures all yielded values as a list in the span's output. You can provide an `output_reducer` parameter – a callable that aggregates the list into a single result. Common patterns include token aggregation, metrics aggregation, and error collection. ^[function-decorators-databricks-on-aws.md]

```python
@mlflow.trace(output_reducer=lambda x: "".join(x))
def stream_text():
    for word in ["Hello", " ", "World", "!"]:
        yield word
# Span output -> "Hello World!"
```

The raw yielded values remain visible in the **Events** tab of the span UI for debugging. ^[function-decorators-databricks-on-aws.md]

## Exception Handling

If an exception is raised during execution of a traced function, the span captures a partial execution and records the exception details as span events. The UI indicates that the invocation was not successful. ^[function-decorators-databricks-on-aws.md]

## Compatibility with Other Decorators

When using `@mlflow.trace` together with other decorators (e.g., from web frameworks), it must be the **outermost** decorator (the one placed highest) to ensure full visibility into the function's execution, including modifications made by inner decorators. ^[function-decorators-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – Overview of the tracing system.
- LiveSpan – API for dynamically updating a span.
- Span Types – Built‑in types for different spans.
- [Auto‑tracing](/concepts/mlflow-automatic-tracing.md) – Automatic instrumentation of popular libraries.
- [Output Reducer](/concepts/output-reducers.md) – Pattern for aggregating streaming outputs.

## Sources

- function-decorators-databricks-on-aws.md

# Citations

1. [function-decorators-databricks-on-aws.md](/references/function-decorators-databricks-on-aws-0ffe82de.md)
