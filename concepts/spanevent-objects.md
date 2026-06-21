---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f205313c5db36cf6302e91088f8154ebed0a99bb5064b5a1a36f6886015e89e8
  pageDirectory: concepts
  sources:
    - span-tracing-with-context-managers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spanevent-objects
    - Span Events
    - SpanEvents
  citations:
    - file: span-tracing-with-context-managers-databricks-on-aws.md
title: SpanEvent Objects
description: MLflow SpanEvent objects that record specific occurrences during a span's lifetime, supporting timestamped events, custom attributes, and exception-derived events.
tags:
  - mlflow
  - tracing
  - events
  - observability
timestamp: "2026-06-19T23:05:25.084Z"
---

## SpanEvent Objects

**SpanEvent objects** are a core component of manual [span tracing](/concepts/mlflow-tracing.md) in [MLflow](/concepts/mlflow.md). They record specific occurrences — such as validation completions, data checkpoints, or exceptions — that happen during a span’s lifetime. Events attach additional structured context to a span without modifying the span’s primary inputs or outputs. ^[span-tracing-with-context-managers-databricks-on-aws.md]

### Creating SpanEvent Objects

A `SpanEvent` is instantiated from the [`mlflow.entities.SpanEvent`](https://[MLflow](/concepts/mlflow.md).org/docs/latest/api_reference/python_api/[MLflow](/concepts/mlflow.md).entities.html#mlflow.entities.SpanEvent) class. The event must have a `name` and can optionally include a `timestamp` (in nanoseconds) and an `attributes` dictionary. Three common creation patterns are:

1. **With the current timestamp** – If no timestamp is provided, the event is recorded at the time of creation.
2. **With a specific timestamp** – Pass the `timestamp` parameter as an integer in nanoseconds (e.g., `int(time.time() * 1e9)`).
3. **From an exception** – Use the class method `SpanEvent.from_exception(e)`, which automatically produces an event named `"exception"` and populates `attributes` with `exception.message`, `exception.type`, and `exception.stacktrace`. ^[span-tracing-with-context-managers-databricks-on-aws.md]

### Adding Events to a Span

Once created, a `SpanEvent` is attached to the currently active span using `span.add_event(event)`. The span must be an active LiveSpan object, which is obtained either from the `mlflow.start_span()` context manager or from `mlflow.get_current_active_span()`. ^[span-tracing-with-context-managers-databricks-on-aws.md]

### Attributes

The `attributes` field is a dictionary that can contain arbitrary key-value pairs. For events created from exceptions, the attributes are automatically set to include the exception’s message, type, and stack trace. Users can define custom attributes to capture any domain-specific information relevant to the event. ^[span-tracing-with-context-managers-databricks-on-aws.md]

### Example Usage

```python
import [[mlflow|MLflow]]
from [[mlflow|MLflow]].entities import SpanEvent, SpanType

with [[mlflow|MLflow]].start_span(name="manual_span", span_type=SpanType.CHAIN) as span:
    # Create an event with current timestamp
    event = SpanEvent(
        name="validation_completed",
        attributes={
            "records_validated": 1000,
            "errors_found": 3,
            "validation_type": "schema"
        }
    )
    span.add_event(event)

    # Create an event from an exception
    try:
        raise ValueError("Invalid input format")
    except Exception as e:
        error_event = SpanEvent.from_exception(e)
        span = [[mlflow|MLflow]].get_current_active_span()
        span.add_event(error_event)
```

### Related Concepts

- LiveSpan – The span object returned by `mlflow.start_span()` to which events are added.
- mlflow.start_span() Context Manager|Span Tracing with Context Managers – The broader mechanism for creating spans and attaching events.
- [SpanStatus](/concepts/spanstatus-api.md) – Defines the status of a span (e.g., OK, ERROR).
- Function Decorator Tracing – An alternative way to [Trace Spans](/concepts/trace-spans.md) without manually managing events.

### Sources

- span-tracing-with-context-managers-databricks-on-aws.md

# Citations

1. [span-tracing-with-context-managers-databricks-on-aws.md](/references/span-tracing-with-context-managers-databricks-on-aws-d67ed6d9.md)
