---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c0065be2c92c787d66f62b62ff644acb32dcc50829e1c3b6f7fa76683fe5fd45
  pageDirectory: concepts
  sources:
    - function-decorators-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automatic-exception-capture-in-spans
    - AECIS
    - automatic-exception-handling-in-traces
    - AEHIT
  citations:
    - file: function-decorators-databricks-on-aws.md
title: Automatic Exception Capture in Spans
description: When an exception is raised during a traced operation, MLflow captures partial data and records exception details as span events, indicated in the UI as an unsuccessful invocation.
tags:
  - mlflow
  - tracing
  - error-handling
  - debugging
timestamp: "2026-06-19T18:56:45.401Z"
---

# Automatic Exception Capture in Spans

**Automatic Exception Capture in Spans** is a feature of [MLflow Tracing](/concepts/mlflow-tracing.md) that automatically records exceptions raised during execution of a traced function as span events, providing visibility into failures without requiring explicit error-handling code.

## Overview

When an `Exception` is raised during processing of a trace-instrumented operation that uses the [`@mlflow.trace` decorator](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/manual-tracing/function-decorator), MLflow automatically captures the exception and makes it visible in the tracing UI. The invocation is marked as unsuccessful, and partial data captured up to the point of failure remains available for debugging. ^[function-decorators-databricks-on-aws.md]

This behavior applies to both regular functions and generator functions. For generator functions traced with `@mlflow.trace`, the span ends when an exception is raised during iteration, and the captured exception is recorded as a span event. ^[function-decorators-databricks-on-aws.md]

## Recorded Information

When an exception is automatically captured, the following information is included:

- **UI indication**: The trace UI shows that the invocation was not successful.
- **Partial data capture**: Any data collected before the exception occurred remains accessible in the UI.
- **Exception details**: Information about the exception that was raised is included within the **Events** of the partially completed span, aiding identification of where issues are occurring in code. ^[function-decorators-databricks-on-aws.md]

## Related Concepts

- [@mlflow.trace decorator](/concepts/mlflowtrace-decorator.md) – The decorator that enables automatic exception capture
- [MLflow Tracing](/concepts/mlflow-tracing.md) – The broader tracing framework
- [Span Events](/concepts/spanevent-objects.md) – Where exception details are recorded
- [Manual Tracing](/concepts/manual-tracing.md) – Tracing approach using decorators and context managers
- Streaming Outputs – Generator functions that also benefit from automatic exception capture

# Citations

1. [function-decorators-databricks-on-aws.md](/references/function-decorators-databricks-on-aws-0ffe82de.md)
