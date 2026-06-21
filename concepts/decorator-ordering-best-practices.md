---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3721fe9e1bdd2239cc322e11c7b1cbee042d7d055b9c1d501a3152f6719d70ff
  pageDirectory: concepts
  sources:
    - function-decorators-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - decorator-ordering-best-practices
    - DOBP
  citations:
    - file: function-decorators-databricks-on-aws.md
title: Decorator Ordering Best Practices
description: When combining @mlflow.trace with other decorators (e.g., from web frameworks), @mlflow.trace must be the outermost decorator to ensure complete observability of the function's execution.
tags:
  - mlflow
  - tracing
  - decorator
  - best-practices
timestamp: "2026-06-19T18:56:25.966Z"
---

# Decorator Ordering Best Practices

**Decorator Ordering Best Practices** refers to the recommended pattern for placing the [`@mlflow.trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.trace) decorator when multiple decorators are applied to a single function. Correct ordering ensures complete observability, accurate execution timing, and proper capture of inputs and outputs by [MLflow Tracing](/concepts/mlflow-tracing.md).

## Overview

When a Python function uses more than one decorator, the order in which decorators are stacked matters. For tracing to work correctly, `@mlflow.trace` should generally be the **outermost** decorator (the one at the very top of the decorator stack). This placement guarantees that MLflow can observe the entire execution of the function, including any behavior introduced by inner decorators (for example, timing wrappers, web framework routing, or input validation). ^[function-decorators-databricks-on-aws.md]

## Why Order Matters

If `@mlflow.trace` is not the outermost decorator, its visibility into the function’s execution may be limited or incorrect. Common consequences include:

- **Incomplete traces**: The span may not capture the full execution time or the modifications made by inner decorators.
- **Misrepresented inputs/outputs**: Changes to arguments or return values applied by inner wrappers may occur after MLflow has already recorded them, leading to inaccurate span attributes.
- **Masked exceptions**: Exceptions raised by inner decorators may not be recorded as span events if they occur before MLflow’s span logic is invoked.

^[function-decorators-databricks-on-aws.md]

## Recommended Ordering

The recommended pattern is:

```python
@mlflow.trace(name="my_decorated_function_correct_order")
@simple_timing_decorator
# @another_framework_decorator  # e.g., @app.route("/mypath") from Flask
def my_complex_function(x, y):
    # Function logic here
    time.sleep(0.1)  # Simulate work
    return x + y
```

In this example, `@mlflow.trace` is outermost. It wraps the entire decorated function, so any timing, logging, or transformation performed by `@simple_timing_decorator` is visible within the MLflow span. ^[function-decorators-databricks-on-aws.md]

## Incorrect Ordering (Anti-Pattern)

Do not place `@mlflow.trace` under other decorators:

```python
@simple_timing_decorator
@mlflow.trace(name="my_decorated_function_incorrect_order")
# @another_framework_decorator
def my_other_complex_function(x, y):
    time.sleep(0.1)
    return x * y
```

Here, `@mlflow.trace` is applied before `@simple_timing_decorator`. The timing wrapper adds its own execution overhead after MLflow’s span has already ended, so the trace may not reflect the total execution time accurately. Similarly, if the inner decorator modifies inputs or outputs, those modifications happen outside the MLflow span’s view. ^[function-decorators-databricks-on-aws.md]

## Best Practices Summary

| Practice | Description |
|----------|-------------|
| **Place `@mlflow.trace` outermost** | Always stack `@mlflow.trace` as the first decorator (top-most) when combining it with other decorators. |
| **Be aware of decorator semantics** | Inner decorators are executed first (from bottom to top). Outer decorators wrap the whole execution chain. |
| **Test with and without tracing** | Verify that the order does not alter the function’s behavior beyond tracing. |
| **Document ordering decisions** | In code reviews or comments, note why `@mlflow.trace` is placed where it is, especially when framework decorators are involved. |

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – Overview of MLflow’s distributed tracing capabilities
- [@mlflow.trace decorator](/concepts/mlflowtrace-decorator.md) – The primary manual tracing decorator
- Span Concepts – Types and attributes of tracing spans
- [Manual Tracing](/concepts/manual-tracing.md) – Other methods for creating spans (context managers, low-level APIs)
- [Auto-tracing](/concepts/automatic-tracing.md) – Automatic instrumentation for popular libraries

## Sources

- function-decorators-databricks-on-aws.md

# Citations

1. [function-decorators-databricks-on-aws.md](/references/function-decorators-databricks-on-aws-0ffe82de.md)
