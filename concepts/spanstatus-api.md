---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e6b11d31a401f155c5cfba5800be3ce8298a91128fc6723ebcc5278459b911c2
  pageDirectory: concepts
  sources:
    - span-tracing-with-context-managers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spanstatus-api
    - Span Status
    - SpanStatus
    - SpanStatus and SpanStatusCodes
    - SpanStatusCodes
  citations:
    - file: span-tracing-with-context-managers-databricks-on-aws.md
title: SpanStatus API
description: MLflow SpanStatus objects for defining span completion status (OK/ERROR), with caveats about context manager overwriting status upon exit.
tags:
  - mlflow
  - tracing
  - status
  - observability
timestamp: "2026-06-19T23:05:24.535Z"
---

Based on your request, here is the wiki page for "SpanStatus API", written using only the provided source material.

---

## SpanStatus API

The **SpanStatus API** defines the status of a span within the [MLflow Tracing](/concepts/mlflow-tracing.md) framework. It is part of the `mlflow.entities` module and works alongside the SpanEvent API to provide a complete observability picture for traced code. ^[span-tracing-with-context-managers-databricks-on-aws.md]

### Overview

`SpanStatus` objects represent the completion state of a span — whether the operation succeeded, failed, or encountered another condition. When used with the mlflow.start_span() Context Manager|mlflow.start_span() context manager, note that the context manager overwrites the status upon exit. Specifically, when the context manager exits successfully, the span status is overwritten with `"OK"`. ^[span-tracing-with-context-managers-databricks-on-aws.md]

### Creating Status Objects

You can create `SpanStatus` instances manually using the `SpanStatus` constructor, which accepts a status code and an optional description. ^[span-tracing-with-context-managers-databricks-on-aws.md]

```python
from [[mlflow|MLflow]].entities import SpanStatus, SpanStatusCode

success_status = SpanStatus(SpanStatusCode.OK)

error_status = SpanStatus(
    SpanStatusCode.ERROR,
    description="Failed to connect to database"
)
```

### Setting Status on a Live Span

Use the `set_status()` method on a LiveSpan object to assign a `SpanStatus` object. As a convenience, you can also pass string shortcuts such as `"OK"` or `"ERROR"` directly. ^[span-tracing-with-context-managers-databricks-on-aws.md]

```python
span.set_status(success_status)
# Or use string shortcuts:
span.set_status("OK")
span.set_status("ERROR")
```

**Important**: When using `mlflow.start_span()` as a context manager, the status is overwritten upon exit. A context manager that exits successfully will overwrite any previously set status with `"OK"`. ^[span-tracing-with-context-managers-databricks-on-aws.md]

### Querying Status from Completed Spans

After a trace has been recorded, you can retrieve the status of individual spans by accessing the `status` attribute of each span object. The `` `status_code `` property provides the machine-readable status value. ^[span-tracing-with-context-managers-databricks-on-aws.md]

```python
last_trace_id = [[mlflow|MLflow]].get_last_active_trace_id()
trace = [[mlflow|MLflow]].get_trace(last_trace_id)
for span in trace.data.spans:
    print(span.status.status_code)
```

### Status Codes

The `SpanStatusCode` enum provides the following standard status codes:

- `SpanStatusCode.OK` — The span completed without error.
- `SpanStatusCode.ERROR` — The span encountered an error condition.

A human-readable description can be attached to an error status via the `description` parameter of the `SpanStatus` constructor. ^[span-tracing-with-context-managers-databricks-on-aws.md]

### Related Concepts

- SpanEvent API — Records specific occurrences during a span's lifetime.
- [mlflow.start_span()](/concepts/mlflow-spans.md) — The context manager that creates and manages spans.
- LiveSpan — The object representing an in-progress span.
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The overall tracing framework for GenAI applications.
- Function Decorator Tracing — An alternative approach to span creation using `@mlflow.trace`.

### Sources

- span-tracing-with-context-managers-databricks-on-aws.md

# Citations

1. [span-tracing-with-context-managers-databricks-on-aws.md](/references/span-tracing-with-context-managers-databricks-on-aws-d67ed6d9.md)
