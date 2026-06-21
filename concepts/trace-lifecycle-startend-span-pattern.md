---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 081195b4d03a8183cc29bcc3e1cd3c636fc0891287cd8cabb4193c06af69fb1a
  pageDirectory: concepts
  sources:
    - low-level-client-apis-advanced-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-lifecycle-startend-span-pattern
    - TL(SP
  citations:
    - file: low-level-client-apis-advanced-databricks-on-aws.md
title: Trace Lifecycle (start/end span pattern)
description: Every trace follows a strict lifecycle where start_trace and start_span calls must have corresponding end_trace or end_span calls, managed in LIFO order.
tags:
  - tracing
  - lifecycle
  - best-practices
timestamp: "2026-06-19T19:28:23.566Z"
---

---

## Trace Lifecycle (start/end span pattern)

The **Trace Lifecycle (start/end span pattern)** is the explicit sequence of API calls required to create, manage, and complete a [trace](/concepts/traces.md) and its constituent span|spans when using the MlflowClient low-level APIs. Unlike high-level decorators or context managers, this pattern forces the developer to manually call `start_trace`, `start_span`, `end_span`, and `end_trace` in the correct order, and enforces that every start has a matching end. ^[low-level-client-apis-advanced-databricks-on-aws.md]

### Core concepts

#### Trace lifecycle

Every trace follows a strict lifecycle:

1. **Start Trace** – creates the root span.
2. **Start Span 1** – a child of the root.
3. **Start Span 2** – a child of Span 1 (or sibling).
4. **End Span 2** – closes the deepest span first.
5. **End Span 1** – closes the parent.
6. **End Trace** – closes the root span, completing the trace.

Spans must be ended in reverse order of creation (LIFO). Every `start_trace` or `start_span` call must eventually have a corresponding `end_trace` or `end_span` call; failing to close spans results in incomplete traces. ^[low-level-client-apis-advanced-databricks-on-aws.md]

#### Key identifiers

- `request_id` – links a span to its trace.
- `span_id` – uniquely identifies a span and is used to define parent-child relationships via `parent_id`.
- `parent_id` – indicates the parent span within the same trace.

These identifiers are critical when building span hierarchies manually. ^[low-level-client-apis-advanced-databricks-on-aws.md]

### Getting started

Initialize an `MlflowClient` (optionally with a custom `tracking_uri`), then call:

```python
root_span = client.start_trace(
    name="my_application_flow",
    inputs={"user_id": "123", "action": "generate_report"},
    attributes={"environment": "production", "version": "1.0.0"}
)
request_id = root_span.request_id
```

Child spans are added with `client.start_span()`:

```python
data_span = client.start_span(
    name="fetch_user_data",
    request_id=request_id,
    parent_id=root_span.span_id,
    inputs={"user_id": "123"},
    attributes={"database": "users_db", "query_type": "select"}
)
```

Spans are closed with `client.end_span()`, passing `request_id` and `span_id` plus optional outputs and status. The root span is closed with `client.end_trace()`. ^[low-level-client-apis-advanced-databricks-on-aws.md]

### Practical examples

#### Error handling

Wrap entire operations in try/except to ensure traces complete even on failure. The source code shows a pattern that ends child spans with `"ERROR"` status and re-raises, then ends the trace with error attributes. ^[low-level-client-apis-advanced-databricks-on-aws.md]

#### Custom trace management

A custom `TraceManager` can generate business‑specific trace IDs and stack active traces. The source provides an implementation that pushes/pops traces and automatically creates child spans when a trace is already active. ^[low-level-client-apis-advanced-databricks-on-aws.md]

#### Batch processing with nested spans

Iterate over items, create a span per item, then within each item start validation and transformation sub‑spans. Errors are caught and the item span is ended with `"ERROR"`. ^[low-level-client-apis-advanced-databricks-on-aws.md]

### Best practices

- **Use context managers for safety** – wrap `start_span`/`end_span` in a custom context manager to guarantee closure, even on exceptions.
- **Implement trace state management** – maintain a stack of active traces/spans so components can easily attach child spans.
- **Add meaningful attributes** – enrich spans with model names, prompt templates, user tiers, etc., rather than generic step numbers. ^[low-level-client-apis-advanced-databricks-on-aws.md]

### Common pitfalls

- **Forgetting to end spans** – always use try/finally or context managers.
- **Incorrect parent-child relationships** – double-check `span_id` and `parent_id` values.
- **Mixing high-level and low-level APIs** – they do not interoperate.
- **Hardcoding trace IDs** – always generate unique IDs.
- **Ignoring thread safety** – client APIs are not thread-safe by default. ^[low-level-client-apis-advanced-databricks-on-aws.md]

### When to use client APIs

**Use client APIs for:** custom trace ID schemes, integration with existing trace systems, complex lifecycle management, advanced span hierarchies, custom trace state management. ^[low-level-client-apis-advanced-databricks-on-aws.md]

**Avoid client APIs for:** simple function tracing (use `@mlflow.trace`), local Python applications (use context managers), quick prototyping (use high-level APIs), integration with auto-tracing. ^[low-level-client-apis-advanced-databricks-on-aws.md]

### Related concepts

- MlflowClient – the class that exposes the start/end span methods.
- [Trace](/concepts/traces.md) – the overall container for a set of spans.
- Span – a single unit of work within a trace.
- [Function Decorator APIs](/concepts/mlflowtrace-function-decorator.md) – the higher-level alternative for simple tracing.
- [Manual Tracing](/concepts/manual-tracing.md) – broader topic covering all explicit instrumentation approaches.

### Sources

- low-level-client-apis-advanced-databricks-on-aws.md

# Citations

1. [low-level-client-apis-advanced-databricks-on-aws.md](/references/low-level-client-apis-advanced-databricks-on-aws-881056bc.md)
