---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cef6c7b266569d3004883e1bfa6eaf438a284a2405ee4705065ea835af23cd06
  pageDirectory: concepts
  sources:
    - low-level-client-apis-advanced-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - common-pitfalls-of-low-level-tracing-apis
    - CPOLTA
    - Low-Level Tracing API
    - Low-Level Tracing APIs
  citations:
    - file: low-level-client-apis-advanced-databricks-on-aws.md
title: Common Pitfalls of Low-Level Tracing APIs
description: List of frequent mistakes when using client APIs including forgetting to end spans, incorrect parent-child relationships, mixing API levels, hardcoding IDs, and thread safety issues.
tags:
  - troubleshooting
  - best-practices
timestamp: "2026-06-19T19:19:12.656Z"
---

# Common Pitfalls of Low-Level Tracing APIs

**Common Pitfalls of Low-Level Tracing APIs** are a set of frequent mistakes that developers encounter when using the [`MlflowClient`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.client.html#mlflow.client.MlflowClient) low-level APIs for manual trace lifecycle management. These pitfalls arise because the client APIs require explicit control over span creation, closure, and hierarchy, unlike higher-level decorator or context-manager approaches. Understanding these pitfalls is essential to producing reliable, complete traces. ^[low-level-client-apis-advanced-databricks-on-aws.md]

## Pitfall 1: Forgetting to End Spans

Every `start_trace` or `start_span` call must have a corresponding `end_trace` or `end_span` call. Failing to close spans results in incomplete traces that are difficult to debug. The standard mitigation is to use `try/finally` blocks or, better, create custom context managers that guarantee the span is always ended, even when an exception occurs. ^[low-level-client-apis-advanced-databricks-on-aws.md]

## Pitfall 2: Incorrect Parent-Child Relationships

Spans in a trace form a hierarchy defined by the `parent_id` parameter. Providing an incorrect `parent_id` or `request_id` can produce a malformed span tree, making the trace’s timing and dependency data misleading. Always double-check that child spans reference the correct parent span ID and that all spans within a trace share the same `request_id`. ^[low-level-client-apis-advanced-databricks-on-aws.md]

## Pitfall 3: Mixing High-Level and Low-Level APIs

Low-level client APIs and high-level APIs (such as the `@mlflow.trace` decorator or `mlflow.start_span` context managers) do not interoperate. Combining both in the same application can lead to unexpected behavior, including duplicate spans, lost context, or incomplete traces. Choose one approach per application or module and stick with it consistently. ^[low-level-client-apis-advanced-databricks-on-aws.md]

## Pitfall 4: Hardcoding Trace IDs

The low-level API allows custom trace IDs via the `request_id` parameter, but hardcoding them (e.g., using a constant string) risks collisions and defeats the purpose of unique identification. Always generate unique identifiers dynamically, either by calling `uuid.uuid4()` or by implementing a custom ID generation scheme that incorporates business-specific fields such as user ID, timestamp, or operation name. ^[low-level-client-apis-advanced-databricks-on-aws.md]

## Pitfall 5: Ignoring Thread Safety

Client API methods are **not thread-safe by default**. In multi-threaded or concurrent applications, simultaneous calls to `start_span`, `end_span`, or `end_trace` can corrupt internal state, leading to lost or overlapping spans. Use explicit locking mechanisms (e.g., threading locks) or thread-local storage to isolate trace operations per thread. Alternatively, design your application to process each trace on a single thread. ^[low-level-client-apis-advanced-databricks-on-aws.md]

## Best Practices to Avoid Pitfalls

- **Use context managers** to encapsulate span lifecycle and guarantee closure, even on exceptions. ^[low-level-client-apis-advanced-databricks-on-aws.md]
- **Implement trace state management** with a stack-based manager (e.g., `TraceStateManager`) to keep track of active traces and spans, preventing orphaned spans. ^[low-level-client-apis-advanced-databricks-on-aws.md]
- **Add meaningful attributes** to spans (such as model name, temperature, prompt template) instead of generic attributes like `{"step": 1, "data": "some data"}`. This enriches traces for debugging and analysis. ^[low-level-client-apis-advanced-databricks-on-aws.md]

## Related Concepts

- MlflowClient – The low-level API used for manual trace lifecycle.
- Trace lifecycle – The strict sequence of start/end calls that must be followed.
- [Span hierarchy](/concepts/trace-span-hierarchy.md) – Parent-child relationships between spans.
- [Function Decorator APIs](/concepts/mlflowtrace-function-decorator.md) – The higher-level alternative that avoids these pitfalls.
- Context managers – Python constructs that guarantee resource cleanup.

## Sources

- low-level-client-apis-advanced-databricks-on-aws.md

# Citations

1. [low-level-client-apis-advanced-databricks-on-aws.md](/references/low-level-client-apis-advanced-databricks-on-aws-881056bc.md)
