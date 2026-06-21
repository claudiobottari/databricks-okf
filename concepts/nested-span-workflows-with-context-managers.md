---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1fcf6bffb6d95ce7bcdca2af250a10cbd1e391b13f1c96536b48c07ee5a32921
  pageDirectory: concepts
  sources:
    - function-decorators-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - nested-span-workflows-with-context-managers
    - NSWWCM
  citations:
    - file: function-decorators-databricks-on-aws.md
title: Nested Span Workflows with Context Managers
description: Using mlflow.start_span() as a context manager within a @mlflow.trace-decorated function to create nested spans for complex, multi-step workflows like data pipelines.
tags:
  - mlflow
  - tracing
  - nested-spans
  - workflows
timestamp: "2026-06-19T18:57:01.029Z"
---

# Nested Span Workflows with Context Managers

**Nested Span Workflows with Context Managers** is a manual tracing pattern in MLflow that allows you to create hierarchical spans for multi-step processes using Python's `with` statement. This approach provides granular control over span creation and lifecycle, enabling detailed observability of complex workflows.^[function-decorators-databricks-on-aws.md]

## Overview

While the [@mlflow.trace Function Decorator](/concepts/mlflowtrace-function-decorator.md) is the simplest way to add tracing to individual functions, nested span workflows using context managers give you finer control over span boundaries and metadata. This pattern is particularly useful for complex workflows with multiple distinct phases, where you need to create parent-child relationships between spans and attach custom inputs or outputs at each level.^[function-decorators-databricks-on-aws.md]

## Basic Pattern

To create nested spans, use `mlflow.start_span()` as a context manager within a function that is itself traced (typically with `@mlflow.trace`). The parent span is created by the outer decorator, and child spans are created inside `with` blocks:^[function-decorators-databricks-on-aws.md]

```python
@mlflow.trace(name="data_pipeline")
def process_data_pipeline(data_source: str):
    # Extract phase
    with mlflow.start_span(name="extract") as extract_span:
        raw_data = extract_from_source(data_source)
        extract_span.set_outputs({"record_count": len(raw_data)})

    # Transform phase
    with mlflow.start_span(name="transform") as transform_span:
        transformed = apply_transformations(raw_data)
        transform_span.set_outputs({"transformed_count": len(transformed)})

    # Load phase
    with mlflow.start_span(name="load") as load_span:
        result = load_to_destination(transformed)
        load_span.set_outputs({"status": "success"})

    return result
```

^[function-decorators-databricks-on-aws.md]

## Key Features

### Automatic Parent-Child Relationship
When `mlflow.start_span()` is called inside an already-traced function, MLflow automatically detects the parent-child relationship. The outer `@mlflow.trace` decorator creates the root span, and each context manager creates a child span under it. This creates a hierarchical trace tree in the MLflow UI.^[function-decorators-databricks-on-aws.md]

### Custom Span Metadata
Each nested span created with `mlflow.start_span()` can be customized using the returned `LiveSpan` object. You can set attributes, inputs, and outputs on each span independently:^[function-decorators-databricks-on-aws.md]

```python
with mlflow.start_span(name="custom_phase") as span:
    span.set_attributes({"model": "gpt-4", "temperature": 0.7})
    span.set_inputs({"prompt": user_input})
    result = process_step(user_input)
    span.set_outputs({"result_length": len(result)})
```

### Error Handling
If an exception occurs within a context manager block, the span will be marked as failed and the error details will be captured as span events. This allows you to identify exactly which phase of a workflow encountered an issue.^[function-decorators-databricks-on-aws.md]

## Use Cases

### Complex Data Pipelines
For ETL or data processing workflows with distinct extraction, transformation, and loading phases, nested spans provide visibility into the duration and success of each stage.

### Multi-Step LLM Workflows
When building applications that chain multiple LLM calls (e.g., retrieval-augmented generation), nested spans help track each interaction separately within the overall request context.

### Orchestration Layers
For orchestrators that coordinate multiple sub-tasks or microservices, nested spans create a clear call hierarchy for debugging latency or failure points.

## Differences from Function Decorators

| Feature | `@mlflow.trace` Decorator | `mlflow.start_span()` Context Manager |
|---|---|---|
| Scope | Wraps entire function | Wraps specific code block |
| Granularity | Function-level | Block-level |
| Control | Less fine-grained | High (can set inputs/outputs inline) |
| Nesting | Auto-detects calls between traced functions | Manual `with` blocks |
| Best for | Simple function tracing | Complex multi-step workflows |

^[function-decorators-databricks-on-aws.md]

## Combining with Other Patterns

Nested span workflows can be combined with [Auto-Tracing](/concepts/automatic-tracing.md) and [Manual Tracing with Client APIs](/concepts/manual-tracing-apis.md) for comprehensive observability. The `mlflow.get_current_active_span()` API is available inside context manager blocks to dynamically modify the current span.^[function-decorators-databricks-on-aws.md]

## Related Concepts

- [@mlflow.trace Function Decorator](/concepts/mlflowtrace-function-decorator.md) — Simpler approach for function-level tracing
- Span Tracing — General concept of tracing code blocks
- [Manual Tracing with Client APIs](/concepts/manual-tracing-apis.md) — Low-level control for advanced scenarios
- [Debug and Observe with Traces](/concepts/genai-trace-analysis-and-debugging.md) — How to use traced applications for debugging

## Sources

- function-decorators-databricks-on-aws.md

# Citations

1. [function-decorators-databricks-on-aws.md](/references/function-decorators-databricks-on-aws-0ffe82de.md)
