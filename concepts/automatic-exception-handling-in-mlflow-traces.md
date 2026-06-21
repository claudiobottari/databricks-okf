---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6421bc46179d894b7512b440d7370ccc72bc16682cdf98deef828f37e2c550e0
  pageDirectory: concepts
  sources:
    - function-decorators-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automatic-exception-handling-in-mlflow-traces
    - AEHIMT
  citations:
    - file: function-decorators-databricks-on-aws.md
title: Automatic Exception Handling in MLflow Traces
description: Built-in capture of exceptions during trace-instrumented operations, showing failure indicators in the UI and recording exception details as span events.
tags:
  - mlflow
  - tracing
  - error-handling
timestamp: "2026-06-19T10:41:51.784Z"
---

# Automatic Exception Handling in MLflow Traces

**Automatic Exception Handling in MLflow Traces** refers to the built-in behavior of the `@mlflow.trace` decorator that captures and surfaces exceptions raised during traced function execution. When an exception occurs, MLflow records the failure without losing the data collected up to that point, making debugging easier. ^[function-decorators-databricks-on-aws.md]

## How It Works

When an `Exception` is raised inside a function instrumented with the `@mlflow.trace` decorator, MLflow does not abort the trace entirely. Instead, it completes the span with a partial capture of the inputs, outputs, and intermediate data that were recorded before the exception. The span is marked as unsuccessful in the trace visualization. ^[function-decorators-databricks-on-aws.md]

## Details Captured

The following information is preserved for debugging:

- **Partial trace data** – any inputs, outputs, and attributes collected before the exception are retained. ^[function-decorators-databricks-on-aws.md]
- **Exception details** – the exception message and stack trace are stored as **Events** on the span. These events are visible in the MLflow Trace UI, allowing you to see exactly where and why the error occurred. ^[function-decorators-databricks-on-aws.md]

## UI Indicators

In the MLflow Trace UI:

- The span (or the overall trace) is visually distinguished as a failed invocation.
- The **Events** tab within the span displays the exception details, including the error message and traceback.

This automatic exception handling applies to any function decorated with `@mlflow.trace`, as well as to functions traced via [auto-tracing integrations](/concepts/mlflow-tracing-integrations.md) that use the same underlying span mechanism. ^[function-decorators-databricks-on-aws.md]

## Benefits

- **No data loss** – even partial executions are recorded, aiding root cause analysis.
- **Centralized debugging** – exception events are co-located with the span’s normal metadata, so you don’t need to search separate logs.
- **Zero configuration** – the behavior is built into the tracing infrastructure; no additional error-handling code is required. ^[function-decorators-databricks-on-aws.md]

## Related Concepts

- [@mlflow.trace decorator](/concepts/mlflowtrace-decorator.md) – the primary way to enable tracing on functions.
- [Span Events](/concepts/spanevent-objects.md) – how exception details are structured within a span.
- Debug & observe your app – using traces to diagnose issues.
- [Manual Tracing](/concepts/manual-tracing.md) – other ways to instrument code with spans.
- [Auto-tracing integrations](/concepts/mlflow-tracing-integrations.md) – tracing for libraries like OpenAI that also benefit from automatic exception capture.

## Sources

- function-decorators-databricks-on-aws.md

# Citations

1. [function-decorators-databricks-on-aws.md](/references/function-decorators-databricks-on-aws-0ffe82de.md)
