---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5c5ea6224fe0ab1e522bdc51975ce23752920df6df4a9d7ba3889cd176cfc3d0
  pageDirectory: concepts
  sources:
    - function-decorators-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-threaded-tracing-in-mlflow
    - MTIM
    - multi-threaded-tracing-with-contextvar
    - MTWC
  citations:
    - file: function-decorators-databricks-on-aws.md
title: Multi-threaded tracing in MLflow
description: MLflow Tracing is thread-safe with ContextVar isolation per thread, requiring manual context copying via contextvars.copy_context() and ctx.run() to propagate traces across threads.
tags:
  - mlflow
  - tracing
  - concurrency
  - threading
timestamp: "2026-06-18T12:27:41.625Z"
---

# Multi-threaded tracing in MLflow

**Multi-threaded tracing** in [MLflow](/concepts/mlflow.md) refers to the ability to instrument and observe functions that execute across multiple threads, while preserving the parent-child span relationships that make traces meaningful. By default, [MLflow Tracing](/concepts/mlflow-tracing.md) is thread-safe: each thread maintains its own isolated span context, so traces from different threads do not interfere with each other. However, creating a trace that spans multiple threads (i.e., a single trace whose child spans run on worker threads) requires explicit handling of Python’s `ContextVar` mechanism. ^[function-decorators-databricks-on-aws.md]

## How it works

MLflow uses Python’s built‑in `contextvars.ContextVar` to store the current span context. By design, `ContextVar` values are **not** automatically propagated across threads; each new thread starts with a fresh context. To let a worker thread inherit the parent trace from the main thread, you must manually copy the context using `contextvars.copy_context()` and then execute the worker function inside that copied context via `context.run()`. ^[function-decorators-databricks-on-aws.md]

## Example: ThreadPoolExecutor with manual context copying

The following example demonstrates multi‑threaded tracing using `ThreadPoolExecutor`. The key steps are:
1. Call `contextvars.copy_context()` in the main thread.
2. Submit the worker function to the executor using `ctx.run(worker, argument)`.

```python
import contextvars
from concurrent.futures import ThreadPoolExecutor, as_completed
import mlflow
from mlflow.entities import SpanType
import openai

client = openai.OpenAI()

# Enable [[mlflow-tracing|MLflow Tracing]] for OpenAI
mlflow.openai.autolog()

@mlflow.trace
def worker(question: str) -> str:
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": question},
    ]
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.1,
        max_tokens=100,
    )
    return response.choices[0].message.content

@mlflow.trace
def main(questions: list[str]) -> list[str]:
    results = []
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = []
        for question in questions:
            ctx = contextvars.copy_context()
            futures.append(executor.submit(ctx.run, worker, question))
        for future in as_completed(futures):
            results.append(future.result())
    return results

questions = [
    "What is the capital of France?",
    "What is the capital of Germany?",
]
main(questions)
```

Without the `ctx.run(...)` wrapper, each worker thread would operate in its own context, and the spans generated inside `worker` would **not** be nested under the `main` span. With the manual context copy, the trace correctly shows the parent‑child relationship. ^[function-decorators-databricks-on-aws.md]

## Async tasks: no manual copying needed

In contrast to threads, `ContextVar` values are automatically copied to **asynchronous** tasks. If your concurrent workload is I/O‑bound, using `asyncio` may be simpler than multi‑threading, because you do not need to manually propagate the context. ^[function-decorators-databricks-on-aws.md]

## Prerequisites

- MLflow 3.x (or MLflow 2.x) with `mlflow[databricks]` ≥ 3.1.
- The [`@mlflow.trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.trace) decorator must be the outermost decorator when combined with other decorators. ^[function-decorators-databricks-on-aws.md]

## Related concepts

- [Manual tracing with function decorators](/concepts/manual-tracing.md) – The `@mlflow.trace` decorator and its parameters.
- mlflow.start_span() Context Manager|Span context and propagation – How MLflow maintains parent‑child relationships.
- Auto‑tracing integrations – Built‑in tracing for libraries such as OpenAI.
- ContextVar in Python – The standard mechanism for context‑local state.
- [Async tracing in MLflow](/concepts/async-anthropic-tracing-in-mlflow.md) – Tracing for `asyncio`‑based code.

## Sources

- function-decorators-databricks-on-aws.md (section “Multi‑threading”, from line 225 to line 290).

# Citations

1. [function-decorators-databricks-on-aws.md](/references/function-decorators-databricks-on-aws-0ffe82de.md)
