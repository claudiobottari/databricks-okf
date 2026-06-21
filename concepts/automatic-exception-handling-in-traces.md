---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6b5406c8c901bc982c27782a6147b4d5d9dcd2537558bdab7e2ec52092410dc1
  pageDirectory: concepts
  sources:
    - function-decorators-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automatic-exception-handling-in-traces
    - AEHIT
  citations:
    - file: function-decorators-databricks-on-aws.md
    - file: see also the decorator’s general behavior described in the first paragraph of the source
    - file: see also the “streaming outputs” note about generator spans ending on exception
title: Automatic exception handling in traces
description: If an Exception is raised during a trace-instrumented operation, MLflow captures the partial trace data and records exception details as span events for debugging.
tags:
  - mlflow
  - tracing
  - error-handling
timestamp: "2026-06-18T12:27:41.737Z"
---

# Automatic Exception Handling in Traces

**Automatic exception handling** in [MLflow Tracing](/concepts/mlflow-tracing.md) refers to the built‑in behavior of the [`@mlflow.trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.trace) decorator that captures exceptions raised during the execution of a traced function and records them as span events. This feature aids in debugging by preserving partial trace data and surfacing error details in the UI. ^[function-decorators-databricks-on-aws.md]

## Behavior

When an `Exception` is raised during processing of a trace‑instrumented operation:

- The UI shows an indication that the invocation was not successful.
- A partial capture of the trace data remains available for debugging.
- Details about the exception are stored within the **Events** of the partially completed span, helping to identify where the issue occurred in the code. ^[function-decorators-databricks-on-aws.md]

The decorator captures the function’s name, inputs, outputs, and execution time, and when an exception disrupts the flow, the span is still completed with the error information. This ensures that even failed calls are observable. ^[function-decorators-databricks-on-aws.md, see also the decorator’s general behavior described in the first paragraph of the source]

## Visual Indication

The following animation (from the Databricks documentation) illustrates how a traced invocation that raises an exception is displayed in the UI:

![Trace Error](https://assets.docs.databricks.com/_static/images/mlflow3/tracing/trace-exception.gif) ^[function-decorators-databricks-on-aws.md]

## Usage

Automatic exception handling is enabled by default on any function decorated with `@mlflow.trace`. No additional configuration is required. The feature works with both synchronous and asynchronous functions, as well as with generators (the span remains open until the iterator is exhausted or an exception is raised). ^[function-decorators-databricks-on-aws.md, see also the “streaming outputs” note about generator spans ending on exception]

## Related Concepts

- [Function Decorators](/concepts/mlflowtrace-function-decorator.md) – The base mechanism for adding tracing to functions.
- Span Tracing – Manual creation and editing of spans, including error handling.
- Debug and observe your app – Using traces to diagnose issues.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – Overview of the tracing system.

## Sources

- function-decorators-databricks-on-aws.md

# Citations

1. [function-decorators-databricks-on-aws.md](/references/function-decorators-databricks-on-aws-0ffe82de.md)
2. see also the decorator’s general behavior described in the first paragraph of the source
3. see also the “streaming outputs” note about generator spans ending on exception
