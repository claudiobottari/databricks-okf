---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b2bc81669f702dbbe90b3d9da1292e5ed72d10f372175bc595930a30066bec96
  pageDirectory: concepts
  sources:
    - low-level-client-apis-advanced-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - batch-processing-with-nested-span-hierarchies
    - BPWNSH
  citations:
    - file: low-level-client-apis-advanced-databricks-on-aws.md
title: Batch Processing with Nested Span Hierarchies
description: Pattern for tracking complex multi-level workflows by creating nested span hierarchies for each item in a batch, with structured error handling per item.
tags:
  - batch-processing
  - tracing
  - workflows
timestamp: "2026-06-19T19:22:01.765Z"
---

# Batch Processing with Nested Span Hierarchies

**Batch Processing with Nested Span Hierarchies** is an advanced pattern for instrumenting complex, multi-level workflows in MLflow using the low-level `MlflowClient` APIs. This approach is essential when an application processes a collection of items, and each item requires multiple sub-operations (such as validation and transformation) that must be tracked as separate spans within a single trace.

## Overview

Unlike simple function tracing (which uses the `@mlflow.trace` decorator), batch processing with nested span hierarchies requires explicit, fine-grained control over the trace lifecycle. The pattern is characterized by:

- A **root trace** representing the entire batch job.
- One or more **item spans** as children of the root, one per item in the batch.
- **Nested sub-spans** beneath each item span for validation, transformation, or other per-item steps.

This style is a primary use case for the MlflowClient low-level API. It is described in detail within the official Databricks documentation under the "Batch processing with nested spans" example. ^[low-level-client-apis-advanced-databricks-on-aws.md]

## When to Use

Use batch processing with nested span hierarchies when:

- You need to track individual items in a batch (e.g., a list of records or files).
- Each item requires multiple sub-operations (validation, transformation, error handling).
- You need explicit control over span IDs, parent-child relationships, and span closure order.
- You are integrating with existing observability or custom trace ID systems.

This pattern is an **advanced** usage of the `MlflowClient` APIs. For simpler cases, prefer the function decorator APIs (`@mlflow.trace`) or context managers. ^[low-level-client-apis-advanced-databricks-on-aws.md]

## Implementing the Pattern

The canonical implementation (from the Databricks documentation) uses `MlflowClient` to manually manage the trace and span lifecycle. The pattern follows a strict lifecycle: start a root trace, then for each item in the batch, start an item span, and optionally start and end sub-spans within it. All spans must be ended in LIFO (Last In, First Out) order. ^[low-level-client-apis-advanced-databricks-on-aws.md]

```python
def batch_processor(items):
    client = MlflowClient()
    root = client.start_trace(
        name="batch_processing",
        inputs={"batch_size": len(items)}
    )
    results = []
    for i, item in enumerate(items):
        item_span = client.start_span(
            name=f"process_item_{i}",
            request_id=root.request_id,
            parent_id=root.span_id,
            inputs={"item_id": item["id"]}
        )
        try:
            validation_span = client.start_span(
                name="validate",
                request_id=root.request_id,
                parent_id=item_span.span_id
            )
            is_valid = validate_item(item)
            client.end_span(
                request_id=validation_span.request_id,
                span_id=validation_span.span_id,
                outputs={"is_valid": is_valid}
            )
            if is_valid:
                process_span = client.start_span(
                    name="transform",
                    request_id=root.request_id,
                    parent_id=item_span.span_id
                )
                result = transform_item(item)
                results.append(result)
                client.end_span(
                    request_id=process_span.request_id,
                    span_id=process_span.span_id,
                    outputs={"transformed": result}
                )
            client.end_span(
                request_id=item_span.request_id,
                span_id=item_span.span_id,
                status="OK"
            )
        except Exception as e:
            client.end_span(
                request_id=item_span.request_id,
                span_id=item_span.span_id,
                status="ERROR",
                attributes={"error": str(e)}
            )
    client.end_trace(
        request_id=root.request_id,
        outputs={
            "processed_count": len(results),
            "success_rate": len(results) / len(items)
        }
    )
    return results
```

## Key Identifiers

When working with nested span hierarchies, two identifiers are critical:

- **`request_id`**: Links a span to its parent trace. Extracted from the root span (e.g., `root_span.request_id`).
- **`span_id`**: Identifies the span itself. Used as the `parent_id` parameter when creating child spans. ^[low-level-client-apis-advanced-databricks-on-aws.md]

## Best Practices

### Use Context Managers for Safety

Because the pattern involves many manual `start_span` and `end_span` calls, it is recommended to wrap span management in a custom context manager to guarantee that spans are always closed, even on error. The documentation provides an example `traced_span` context manager for this purpose. ^[low-level-client-apis-advanced-databricks-on-aws.md]

```python
from contextlib import contextmanager

@contextmanager
def traced_span(client, name, request_id, parent_id=None, **kwargs):
    span = client.start_span(
        name=name,
        request_id=request_id,
        parent_id=parent_id,
        **kwargs
    )
    try:
        yield span
    except Exception as e:
        client.end_span(
            request_id=span.request_id,
            span_id=span.span_id,
            status="ERROR",
            attributes={"error": str(e)}
        )
        raise
    else:
        client.end_span(
            request_id=span.request_id,
            span_id=span.span_id,
            status="OK"
        )
```

### Use TraceStateManager

For applications with deeply nested spans, the documentation recommends a `TraceStateManager` class that uses a stack to track the current trace and manage nesting. ^[low-level-client-apis-advanced-databricks-on-aws.md]

### Avoid Common Pitfalls

- **Forgetting to end spans**: Always use `try`/`finally` or context managers.
- **Incorrect parent-child relationships**: Double-check that you pass the correct `parent_id` (the `span_id` of the parent span).
- **Mixing high-level and low-level APIs**: These APIs do not interoperate.
- **Hardcoding trace IDs**: Always generate unique IDs dynamically.
- **Ignoring thread safety**: The `MlflowClient` APIs are not thread-safe by default. ^[low-level-client-apis-advanced-databricks-on-aws.md]

## Related Concepts

- MlflowClient — The low-level Python client for direct trace management.
- [Trace Lifecycle](/concepts/scorer-lifecycle.md) — The required sequence of start/end calls for traces and spans.
- [Function Decorator APIs](/concepts/mlflowtrace-function-decorator.md) — A simpler alternative for non-batched, non-nested scenarios.
- Context Managers for Safe Span Management — Best practice wrapper for ensuring spans are always closed.
- TraceStateManager — A helper class for managing trace state across nested spans.

## Sources

- low-level-client-apis-advanced-databricks-on-aws.md

# Citations

1. [low-level-client-apis-advanced-databricks-on-aws.md](/references/low-level-client-apis-advanced-databricks-on-aws-881056bc.md)
