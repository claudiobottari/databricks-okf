---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6088502d830d7aa1f3b18ab823ca6b09056a191cd04f3e5d749c56b44825fb63
  pageDirectory: concepts
  sources:
    - low-level-client-apis-advanced-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - safe-span-management-with-context-managers
    - SSMWCM
  citations:
    - file: low-level-client-apis-advanced-databricks-on-aws.md
title: Safe Span Management with Context Managers
description: Pattern for using Python context managers (contextlib.contextmanager) to ensure spans are always properly closed, even when exceptions occur.
tags:
  - python
  - best-practices
  - error-handling
timestamp: "2026-06-19T19:19:04.037Z"
---

# Safe Span Management with Context Managers

**Safe Span Management with Context Managers** is a pattern for ensuring that every span opened via the low-level `MlflowClient` APIs is correctly closed, even when exceptions occur. By wrapping start/end calls in a context manager, developers eliminate the risk of incomplete or orphaned spans — a common pitfall when managing trace lifecycles manually. ^[low-level-client-apis-advanced-databricks-on-aws.md]

## Motivation

When using the `MlflowClient` to create traces and spans, the library imposes a strict lifecycle: every `start_trace` or `start_span` call must have a corresponding `end_trace` or `end_span` call. Failing to close a span results in incomplete traces that cannot be analyzed. Manual try/finally blocks are error-prone, especially in complex applications with nested branches or early returns. A context manager automates the close logic and guarantees cleanup whether the wrapped code succeeds or raises. ^[low-level-client-apis-advanced-databricks-on-aws.md]

## Implementation

The recommended approach from the Databricks documentation is to create a custom context manager that:

1. Starts a span using `client.start_span()` (or `client.start_trace()` for root spans).
2. Yields the span to the caller.
3. On normal exit, ends the span with status `"OK"`.
4. On exception, ends the span with status `"ERROR"` and attaches the error message as an attribute.

The following example defines a reusable `traced_span` context manager: ^[low-level-client-apis-advanced-databricks-on-aws.md]

```python
from contextlib import contextmanager

@contextmanager
def traced_span(client, name, request_id, parent_id=None, **kwargs):
    """Context manager for safe span management"""
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

Usage becomes straightforward and safe: ^[low-level-client-apis-advanced-databricks-on-aws.md]

```python
with traced_span(client, "my_operation", request_id, parent_id) as span:
    result = perform_operation()
```

## Best Practices

- **Use context managers for all spans**, including root traces. The same pattern can be adapted for `client.start_trace` / `client.end_trace` to ensure complete traces.
- **Maintain a trace stack** when dealing with deeply nested workflows. The documentation suggests a `TraceStateManager` that pushes and pops spans using a stack, ensuring correct parent–child relationships.
- **Add meaningful attributes** inside the context manager to enrich the span with debugging context (e.g., model name, temperature, user tier).
- **Avoid mixing high-level and low-level APIs** — context managers are part of the low-level client API and do not interoperate with the `@mlflow.trace` decorator or auto-tracing. ^[low-level-client-apis-advanced-databricks-on-aws.md]

The context‑manager pattern is especially valuable in batch processing, multi‑step LLM workflows, and any scenario where spans are created in loops or conditional branches. ^[low-level-client-apis-advanced-databricks-on-aws.md]

## Related Concepts

- [Trace Lifecycle](/concepts/scorer-lifecycle.md) – The strict start/end lifecycle that context managers help enforce.
- Low-Level Client APIs – The API surface that provides `start_span` and `end_span`.
- Custom Trace Management – Advanced patterns for managing trace IDs and state across components.
- Error Handling in Traces – Properly recording exceptions and statuses in spans.
- Distributed Tracing – The broader observability practice that MLflow traces support.

## Sources

- low-level-client-apis-advanced-databricks-on-aws.md

# Citations

1. [low-level-client-apis-advanced-databricks-on-aws.md](/references/low-level-client-apis-advanced-databricks-on-aws-881056bc.md)
