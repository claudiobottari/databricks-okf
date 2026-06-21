---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5e6472eadadcb62c367f45828c3f516c37acfda86208d6263d5437c8de16f3ab
  pageDirectory: concepts
  sources:
    - low-level-client-apis-advanced-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-state-management-across-application-components
    - TSMAAC
  citations:
    - file: low-level-client-apis-advanced-databricks-on-aws.md
title: Trace State Management Across Application Components
description: Pattern for managing active trace state using a stack-based approach, allowing nested traces and clean propagation across application components.
tags:
  - architecture
  - tracing
  - state-management
timestamp: "2026-06-19T19:18:24.858Z"
---

# Trace State Management Across Application Components

**Trace State Management** refers to the practice of coordinating the creation, nesting, and completion of traces and spans across different parts of a distributed application. When using low-level client APIs such as [`MlflowClient`], managing trace state becomes a manual responsibility. A dedicated state manager pattern ensures that traces are properly started, nested, and closed regardless of how complex the application control flow is. ^[low-level-client-apis-advanced-databricks-on-aws.md]

## Purpose

In complex applications, multiple components may each need to contribute to a single trace, or a component may need to create its own independent trace. Without centralized state management, spans can be left orphaned or traces left incomplete. A trace state manager provides a single point of coordination, maintaining a stack of active traces so that every `start_trace` or `start_span` call has a guaranteed matching `end_trace` or `end_span` call. ^[low-level-client-apis-advanced-databricks-on-aws.md]

## The `TraceStateManager` Pattern

The source material presents a `TraceStateManager` class that encapsulates this logic. The manager holds a reference to an `MlflowClient` instance and an internal stack of active trace/span objects. ^[low-level-client-apis-advanced-databricks-on-aws.md]

Key methods:

- **`current_trace`** (property): Returns the trace or span at the top of the active stack, representing the most recently started span that has not yet been ended.
- **`push_trace(name, **kwargs)`**: Starts a new trace or child span. If there is already an active trace (i.e., the stack is non-empty), it creates a child span under that active trace. Otherwise, it creates a new root trace. The newly created span is pushed onto the stack.
- **`pop_trace(**kwargs)`**: Ends the current trace or span. It pops the top of the stack, and then decides whether to call `end_span` or `end_trace` based on whether the stack still has a parent. If the stack still contains a parent span, the popped span is ended as a child span; otherwise, it is ended as a root trace.

```python
class TraceStateManager:
    """Manage trace state across application components"""
    def __init__(self):
        self.client = MlflowClient()
        self._trace_stack = []

    @property
    def current_trace(self):
        """Get current active trace"""
        return self._trace_stack[-1] if self._trace_stack else None

    def push_trace(self, name: str, **kwargs):
        """Start a new trace and push to stack"""
        if self.current_trace:
            span = self.client.start_span(
                name=name,
                request_id=self.current_trace.request_id,
                parent_id=self.current_trace.span_id,
                **kwargs
            )
        else:
            span = self.client.start_trace(name=name, **kwargs)
        self._trace_stack.append(span)
        return span

    def pop_trace(self, **kwargs):
        """End current trace and pop from stack"""
        if not self._trace_stack:
            return
        span = self._trace_stack.pop()
        if self._trace_stack:
            self.client.end_span(
                request_id=span.request_id,
                span_id=span.span_id,
                **kwargs
            )
        else:
            self.client.end_trace(
                request_id=span.request_id,
                **kwargs
            )
```

^[low-level-client-apis-advanced-databricks-on-aws.md]

## Usage Across Components

The `TraceStateManager` can be shared across application components, allowing each component to push its own spans onto the same trace stack. For example, a data retrieval component, a processing component, and a reporting component can each call `push_trace` to add a span, and then `pop_trace` when they finish. As long as the stack discipline is maintained (LIFO order), the resulting trace will reflect the correct nesting hierarchy. ^[low-level-client-apis-advanced-databricks-on-aws.md]

## Important Considerations

- **Thread safety**: Client APIs are not thread‑safe by default. If the `TraceStateManager` is used in a multi‑threaded context, external synchronization mechanisms must be added. ^[low-level-client-apis-advanced-databricks-on-aws.md]
- **Stack discipline**: Every `push_trace` must be matched by a corresponding `pop_trace`. The source material recommends using context managers or try/finally blocks to guarantee closure even when exceptions occur. ^[low-level-client-apis-advanced-databricks-on-aws.md]
- **Custom trace IDs**: The manager can be extended to support custom trace ID generation (e.g., based on user IDs or business operations) by overriding the trace name or adding attributes during `push_trace`. ^[low-level-client-apis-advanced-databricks-on-aws.md]

## Related Concepts

- Low-Level Client APIs — The APIs that require manual trace lifecycle management.
- MlflowClient — The client object used to interact with the [MLflow Tracing](/concepts/mlflow-tracing.md) service.
- [Trace Lifecycle](/concepts/scorer-lifecycle.md) — The strict lifecycle (start span → end span → end trace) that state management enforces.
- [Function Decorator APIs](/concepts/mlflowtrace-function-decorator.md) — An alternative, higher‑level approach that automates trace management.
- Context Managers for Trace Safety — A best practice for ensuring spans are always closed.

## Sources

- low-level-client-apis-advanced-databricks-on-aws.md

# Citations

1. [low-level-client-apis-advanced-databricks-on-aws.md](/references/low-level-client-apis-advanced-databricks-on-aws-881056bc.md)
