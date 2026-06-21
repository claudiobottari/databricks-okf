---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4a0ff3bb8fb8ebaa72b4e21e5815cbbec0f45f89f270066e3b7f05de14def643
  pageDirectory: concepts
  sources:
    - function-decorators-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-threaded-tracing-with-contextvar
    - MTWC
  citations:
    - file: function-decorators-databricks-on-aws.md
title: Multi-threaded Tracing with ContextVar
description: MLflow Tracing is thread-safe using Python's ContextVar mechanism, but requires manual context copying via contextvars.copy_context() when spawning traces across threads with ThreadPoolExecutor.
tags:
  - mlflow
  - tracing
  - multi-threading
  - concurrency
timestamp: "2026-06-19T18:56:32.760Z"
---

## Multi-threaded Tracing with ContextVar

[MLflow Tracing](/concepts/mlflow-tracing.md) uses Python's built-in ContextVar mechanism to provide thread-safe trace isolation. By default, each thread maintains its own tracing context, which prevents trace data from mixing between threads. However, `ContextVar` is not automatically propagated across threads when using Python's `threading` or `ThreadPoolExecutor`. This means that when a worker thread is spawned, the tracing context from the main thread is lost, and any spans created inside the worker thread will not be correctly parented to the calling trace. ^[function-decorators-databricks-on-aws.md]

### Propagation with Threads

To enable multi-threaded tracing where a single trace spans multiple threads, the context must be manually copied from the main thread and applied to the worker thread. The `contextvars.copy_context()` function captures the current `ContextVar` state, and `ctx.run()` executes a function within that captured context. ^[function-decorators-databricks-on-aws.md]

The following example demonstrates this pattern using `ThreadPoolExecutor`:

```python
import contextvars
from concurrent.futures import ThreadPoolExecutor, as_completed
import mlflow

@mlflow.trace
def worker(question: str) -> str:
    # This function runs in a worker thread with the copied context
    # ... OpenAI call or other traced operations ...

@mlflow.trace
def main(questions: list[str]) -> list[str]:
    results = []
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = []
        for question in questions:
            ctx = contextvars.copy_context()          # Step 1
            futures.append(executor.submit(ctx.run, worker, question))  # Step 2
        for future in as_completed(futures):
            results.append(future.result())
    return results
```

The two key steps are: (1) calling `copy_context()` to capture the current tracing context, and (2) passing `ctx.run` as the first argument to `executor.submit`, followed by the function and its arguments. This ensures that the worker function executes within the same tracing context as the caller. ^[function-decorators-databricks-on-aws.md]

### Context Propagation in Async Code

In contrast, `ContextVar` is automatically copied to async tasks when using `asyncio`. Therefore, you do **not** need to manually propagate context when using `asyncio` for concurrent I/O-bound tasks. The automatic propagation makes `asyncio` a simpler alternative for multi-threaded tracing scenarios in Python. ^[function-decorators-databricks-on-aws.md]

### Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – Overview of the tracing system
- ContextVar – Python’s mechanism for context variable isolation
- ThreadPoolExecutor – Thread-based parallelism
- asyncio – Async/await concurrency
- Manual Tracing with Function Decorators – The `@mlflow.trace` decorator

### Sources

- function-decorators-databricks-on-aws.md

# Citations

1. [function-decorators-databricks-on-aws.md](/references/function-decorators-databricks-on-aws-0ffe82de.md)
