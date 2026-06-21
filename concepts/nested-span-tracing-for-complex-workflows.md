---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1535273dcd6d0c87e7f690c1aed2caa5e0632d7cf228834540dac7c8b993f6a6
  pageDirectory: concepts
  sources:
    - function-decorators-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - nested-span-tracing-for-complex-workflows
    - NSTFCW
  citations:
    - file: function-decorators-databricks-on-aws.md
title: Nested span tracing for complex workflows
description: Using @mlflow.trace decorators in combination with mlflow.start_span() context managers to create hierarchical parent-child span structures for multi-step pipelines.
tags:
  - mlflow
  - tracing
  - workflows
  - nested-spans
timestamp: "2026-06-18T12:27:44.446Z"
---

Here is the wiki page for "Nested span tracing for complex workflows", based solely on the provided source material.

---

## Nested span tracing for complex workflows

**Nested span tracing** is a technique for instrumenting complex multi-step workflows — such as data pipelines, retrieval-augmented generation (RAG) chains, or agent orchestration — by creating hierarchical spans that capture the relationship between a parent operation and its child steps. This approach provides detailed execution visibility while preserving the overall structure of the workflow.

### Overview

In a complex workflow with multiple steps, a single flat span often obscures where time is spent or where errors occur. Nested spans allow you to model the workflow as a tree of spans, where a root span represents the entire pipeline and child spans represent individual phases such as extraction, transformation, and loading. ^[function-decorators-databricks-on-aws.md]

### Implementation

Nested spans can be created using the `@mlflow.trace` decorator on sub-functions, or by manually opening spans inside a parent function using `mlflow.start_span()`. MLflow automatically detects the parent-child relationships between functions, making the decorator approach compatible with auto-tracing integrations. ^[function-decorators-databricks-on-aws.md]

#### Using `with mlflow.start_span()` for Explicit Nesting

For a multi-phase data pipeline, you can open named child spans within the root function:

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

Each child span captures its own inputs, outputs, and execution time, while the parent span shows the total duration of the pipeline.

### Benefits

- **Granular observability**: Each phase of the workflow is independently traceable, making it easy to identify bottlenecks or failures within a specific step.
- **Structured debugging**: When an exception occurs in a child span, the trace shows exactly which step failed, along with partial data captured up to that point. ^[function-decorators-databricks-on-aws.md]
- **Performance analysis**: The hierarchical view in the MLflow UI allows you to compare the latency of individual phases across different runs.

### Integration with Auto-Tracing

Nested spans created with decorated functions or context managers work seamlessly alongside MLflow's auto-tracing capabilities. See [Automatic Tracing](/concepts/automatic-tracing.md) for details on combining manual and automatic instrumentation. ^[function-decorators-databricks-on-aws.md]

### Streaming Workflows

Nested span tracing also supports generator-based workflows. A span for a streaming function starts when the returned iterator begins to be consumed and ends when the iterator is exhausted or raises an exception. Child spans inside a streaming generator follow the same nesting rules. ^[function-decorators-databricks-on-aws.md]

### Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The overarching tracing framework
- Span — The fundamental unit of traced execution
- Function decorators — The `@mlflow.trace` decorator for instrumentation
- [Auto-tracing](/concepts/automatic-tracing.md) — Automatic instrumentation of supported libraries
- Multi-threading support — Tracing across threads with context propagation

### Sources

- function-decorators-databricks-on-aws.md

# Citations

1. [function-decorators-databricks-on-aws.md](/references/function-decorators-databricks-on-aws-0ffe82de.md)
