---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 710ced17e79e4513073267fa1619ec79941d273114956808c0f79a85c6203f40
  pageDirectory: concepts
  sources:
    - function-decorators-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-threading-with-mlflow-tracing
    - MWMT
  citations:
    - file: function-decorators-databricks-on-aws.md
title: Multi-threading with MLflow Tracing
description: Thread-safe tracing in MLflow using ContextVar, requiring manual context copying across threads via contextvars.copy_context() for correct parent-child span relationships.
tags:
  - mlflow
  - tracing
  - concurrency
  - thread-safety
timestamp: "2026-06-19T10:41:34.896Z"
---

# Multi-threading with [MLflow Tracing](/concepts/mlflow-tracing.md)

**Multi-threading with MLflow Tracing** refers to the ability to use MLflow’s tracing infrastructure in a multi-threaded Python application while maintaining correct span hierarchy and thread isolation. MLflow’s tracing is thread-safe, meaning traces are isolated by default per thread. However, because MLflow uses Python’s built-in `ContextVar` mechanism — which is **not** automatically propagated across threads — manually copying the context from the main thread to a worker thread is required to create a trace that spans multiple threads. ^[function-decorators-databricks-on-aws.md]

## How to Enable Cross-Thread Tracing

To trace operations that execute across threads, you must copy the current tracing context from the parent thread and run the child function inside that copied context. The following pattern using `contextvars.copy_context()` and `ctx.run()` achieves this: ^[function-decorators-databricks-on-aws.md]

```python
import contextvars
from concurrent.futures import ThreadPoolExecutor, as_completed
import mlflow

@mlflow.trace
def worker(question: str) -> str:
    # ... LLM call, etc.
    return response

@mlflow.trace
def main(questions: list[str]) -> list[str]:
    results = []
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = []
        for question in questions:
            ctx = contextvars.copy_context()            # Step 1: copy context
            futures.append(executor.submit(ctx.run, worker, question))  # Step 2: run in copied context
        for future in as_completed(futures):
            results.append(future.result())
    return results
```

^[function-decorators-databricks-on-aws.md]

This approach ensures that spans created in the worker threads are correctly linked to the parent trace, enabling a unified view of the concurrent execution in the MLflow UI.

## asyncio: No Manual Copy Needed

In contrast to threading, `ContextVar` is automatically copied to **async** tasks. Therefore, when using `asyncio` for concurrent I/O-bound work, no manual `copy_context()` is required — traces propagate correctly without additional steps. This makes `asyncio` a simpler alternative for many concurrent tracing scenarios. ^[function-decorators-databricks-on-aws.md]

## Best Practices

- Use `contextvars.copy_context()` and `ctx.run()` whenever spawning threads (via `ThreadPoolExecutor`, `threading.Thread`, etc.) inside a traced function.
- Prefer `asyncio` for concurrent I/O-bound tasks to avoid manual context management.
- Ensure that worker functions are decorated with `@mlflow.trace` so their spans are captured.
- Test that traces appear as a single tree in the MLflow UI rather than isolated per thread.

## Related Concepts

- [@mlflow.trace decorator](/concepts/mlflowtrace-decorator.md) – The primary way to instrument functions.
- Span Tracing – Manual span creation with context managers.
- [Auto-tracing](/concepts/automatic-tracing.md) – Automatic instrumentation of supported frameworks.
- ContextVar – Python’s mechanism for thread-local context, used by MLflow.

## Sources

- function-decorators-databricks-on-aws.md

# Citations

1. [function-decorators-databricks-on-aws.md](/references/function-decorators-databricks-on-aws-0ffe82de.md)
