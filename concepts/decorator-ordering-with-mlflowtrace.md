---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c19e969fc5382612a89c3834c73a0e25180d515b704dbc638f6968f20848ab29
  pageDirectory: concepts
  sources:
    - function-decorators-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - decorator-ordering-with-mlflowtrace
    - DOW@
  citations:
    - file: function-decorators-databricks-on-aws.md
title: Decorator ordering with @mlflow.trace
description: The @mlflow.trace decorator must be the outermost decorator when combined with other decorators to ensure complete observability of function execution.
tags:
  - mlflow
  - tracing
  - best-practices
timestamp: "2026-06-18T12:27:28.855Z"
---

# Decorator ordering with `@mlflow.trace`

**Decorator ordering with `@mlflow.trace`** refers to the placement of the `@mlflow.trace` decorator relative to other decorators applied to the same function. Correct ordering is essential for MLflow to capture the complete execution of the function, including the behavior of any inner decorators. ^[function-decorators-databricks-on-aws.md]

## Correct ordering

The `@mlflow.trace` decorator should generally be the **outermost** decorator — the one placed at the very top of the decorator stack. This ensures that MLflow can observe the entire wrapped function call, including any modifications made by inner decorators (such as timing, logging, or framework‑specific decorators). ^[function-decorators-databricks-on-aws.md]

When `@mlflow.trace` is outermost, the trace captures:
- The function’s name, inputs, and outputs after all inner decorators have run.
- The total execution time, including time added by inner decorators.
- Exceptions raised from any part of the decorated call chain. ^[function-decorators-databricks-on-aws.md]

## Incorrect ordering

If `@mlflow.trace` is **not** the outermost decorator — for example, it is placed below another decorator — its visibility into the function’s execution may be limited or incorrect. The resulting trace might:
- Not reflect modifications to inputs or outputs made by outer decorators.
- Fail to account for the time consumed by outer decorators.
- Produce incomplete or misleading span data. ^[function-decorators-databricks-on-aws.md]

## Example

The following conceptual example illustrates correct and incorrect ordering. The `simple_timing_decorator` is a hypothetical wrapper that measures execution time. ^[function-decorators-databricks-on-aws.md]

```python
import mlflow
import functools
import time

def simple_timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f}s")
        return result
    return wrapper

# Correct order: @mlflow.trace is outermost
@mlflow.trace(name="my_decorated_function_correct_order")
@simple_timing_decorator
def my_complex_function(x, y):
    time.sleep(0.1)
    return x + y

# Incorrect order: @mlflow.trace is NOT outermost
@simple_timing_decorator
@mlflow.trace(name="my_decorated_function_incorrect_order")
def my_other_complex_function(x, y):
    time.sleep(0.1)
    return x * y
```

In the correct version, MLflow records the full execution of `my_complex_function`, including the time and any input/output transformations introduced by `simple_timing_decorator`. In the incorrect version, the trace may omit or misrepresent those aspects. ^[function-decorators-databricks-on-aws.md]

## Best practice

When using ``@mlflow.trace`` alongside decorators from web frameworks (e.g., `@app.route` from Flask) or other custom wrappers, always place `@mlflow.trace` as the outermost decorator to ensure complete observability. ^[function-decorators-databricks-on-aws.md]

## Related concepts

- @mlflow.trace — The decorator for creating spans
- Span tracing with context managers — Manual span creation for finer control
- Auto‑tracing integrations — Combining manual and automatic tracing
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Overview of the tracing subsystem

## Sources

- function-decorators-databricks-on-aws.md

# Citations

1. [function-decorators-databricks-on-aws.md](/references/function-decorators-databricks-on-aws-0ffe82de.md)
