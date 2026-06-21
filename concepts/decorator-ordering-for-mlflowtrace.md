---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b79746ae99387dc5d0a1656d206a43bdd891ac6bb8810bdb366c8db712f35c07
  pageDirectory: concepts
  sources:
    - function-decorators-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - decorator-ordering-for-mlflowtrace
    - DOF@
    - decorator-ordering-with-mlflowtrace
    - DOW@
  citations:
    - file: function-decorators-databricks-on-aws.md
title: Decorator Ordering for @mlflow.trace
description: The rule that @mlflow.trace must be the outermost decorator when combined with other decorators to ensure complete observability of function execution.
tags:
  - mlflow
  - tracing
  - decorators
  - best-practices
timestamp: "2026-06-19T10:41:17.128Z"
---

# Decorator Ordering for @mlflow.trace

**Decorator Ordering for @mlflow.trace** refers to the required placement of the `@mlflow.trace` decorator relative to other decorators on a Python function. To achieve complete observability, `@mlflow.trace` should generally be the **outermost** decorator (the one closest to the function definition, applied last). ^[function-decorators-databricks-on-aws.md]

## Importance of Correct Ordering

When multiple decorators are applied to a single function, the order in which they are stacked determines the execution flow. Placing `@mlflow.trace` as the outermost decorator ensures that MLflow can capture the entire execution of the function — including the behavior, input/output modifications, and execution time added by inner decorators. ^[function-decorators-databricks-on-aws.md]

If `@mlflow.trace` is not the outermost decorator, its visibility into the function's execution may be limited or incorrect. This can lead to incomplete traces, misrepresentation of inputs and outputs, or inaccurate execution time measurements. ^[function-decorators-databricks-on-aws.md]

## Correct vs. Incorrect Ordering

### Correct Order — `@mlflow.trace` is Outermost

In this configuration, MLflow observes the entire execution chain, including the modifications and timing introduced by inner decorators (e.g., a `simple_timing_decorator`, a web framework route such as `@app.route("/mypath")` from Flask). ^[function-decorators-databricks-on-aws.md]

```python
import mlflow
import functools
import time

@mlflow.trace(name="my_decorated_function_correct_order")
@simple_timing_decorator
# @another_framework_decorator  # e.g., @app.route("/mypath")
def my_complex_function(x, y):
    time.sleep(0.1)
    return x + y
```

### Incorrect Order — `@mlflow.trace` is Not Outermost

If `@mlflow.trace` sits below another decorator, the outer decorator's work (e.g., timing, input transformation) occurs outside MLflow's view. The captured trace may not accurately reflect the total execution time and might miss modifications to inputs or outputs made by the outer decorator before `@mlflow.trace` sees them. ^[function-decorators-databricks-on-aws.md]

```python
# Incorrect order: @mlflow.trace is NOT outermost
@simple_timing_decorator
@mlflow.trace(name="my_decorated_function_incorrect_order")
def my_other_complex_function(x, y):
    time.sleep(0.1)
    return x * y
```

## How Decorator Stacking Works

In Python, decorators are applied **bottom-up**: the decorator closest to the function executes first (innermost). When stacked:

```python
@outer_decorator
@inner_decorator
def my_func():
    pass
```

The order of execution is: `outer_decorator(inner_decorator(my_func))`. Thus, `@mlflow.trace` should be placed at the top of the stack so that it wraps all lower decorators and can instrument their full behavior. ^[function-decorators-databricks-on-aws.md]

## Key Principles

- **Place `@mlflow.trace` at the very top** of the decorator stack, above any other decorators (e.g., timing, caching, web framework routes).
- **Ensure full visibility**: Only when `@mlflow.trace` is outermost can it capture the complete inputs, outputs, and execution time — including contributions from inner decorators.
- **Test after reordering**: If adding `@mlflow.trace` to an existing function that already has decorators, verify the ordering is correct to avoid incomplete observability.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The observability framework that `@mlflow.trace` participates in.
- [Function Decorators](/concepts/mlflowtrace-function-decorator.md) – General guidance on using `@mlflow.trace` as a decorator.
- Span Concepts – Understanding span types and attributes.
- [Manual Tracing](/concepts/manual-tracing.md) – Other ways to instrument code manually.
- [Auto-Tracing](/concepts/automatic-tracing.md) – Automatic instrumentation for supported frameworks.

## Sources

- function-decorators-databricks-on-aws.md

# Citations

1. [function-decorators-databricks-on-aws.md](/references/function-decorators-databricks-on-aws-0ffe82de.md)
