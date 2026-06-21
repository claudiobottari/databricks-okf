---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 173f9b3dbfb0864e3fcd97e19bcd64b6184b3704fc88fa12867a6160b27e9661
  pageDirectory: concepts
  sources:
    - tracing-faq-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-multi-threading-behavior
    - MTMB
  citations:
    - file: tracing-faq-databricks-on-aws.md
title: MLflow Tracing Multi-threading Behavior
description: MLflow Tracing uses Python ContextVar, causing each thread to have its own trace context by default; additional steps are needed to combine multi-threaded traces into a single trace.
tags:
  - mlflow
  - tracing
  - multi-threading
  - python
timestamp: "2026-06-19T23:11:30.150Z"
---

# [MLflow Tracing](/concepts/mlflow-tracing.md) Multi-threading Behavior

**MLflow Tracing Multi-threading Behavior** describes how [MLflow Tracing](/concepts/mlflow-tracing.md) operates when used in multi-threaded Python applications. By default, [MLflow Tracing](/concepts/mlflow-tracing.md) uses Python's `ContextVar` mechanism to manage trace context, which means each thread maintains its own independent trace context. This results in [Traces](/concepts/traces.md) being split into multiple separate [Traces](/concepts/traces.md) when functions are executed across different threads. ^[tracing-faq-databricks-on-aws.md]

## Default Behavior: [Traces](/concepts/traces.md) Are Split by Thread

Because `ContextVar` is thread-local in Python, each thread has its own trace context by default. When a multi-threaded application calls traced functions from different threads, [MLflow](/concepts/mlflow.md) creates a separate trace for each thread rather than combining the spans into a single unified trace. ^[tracing-faq-databricks-on-aws.md]

This behavior is important to understand when instrumenting applications that use threading, thread pools, or asynchronous task executors, as the resulting [Traces](/concepts/traces.md) may not present a complete end-to-end view of the operation.

## Combining [Traces](/concepts/traces.md) into a Single Trace

[MLflow](/concepts/mlflow.md) provides mechanisms to generate a single unified trace for multi-threaded workloads, though it requires additional steps beyond standard single-threaded instrumentation. ^[tracing-faq-databricks-on-aws.md]

The recommended approach is to use the [MLflow Tracing @trace Decorator](/concepts/mlflowtrace-decorator.md) with multi-threading support. For detailed implementation guidance, see the [Multi-threading](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/manual-tracing/function-decorator#multi-threading) section in the [MLflow](/concepts/mlflow.md) documentation.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The overall tracing framework for instrumenting ML applications
- [MLflow Trace Timeout](/concepts/mlflow-trace-timeout-mechanism.md) — Controls to prevent [Traces](/concepts/traces.md) from being stuck "in progress"
- [MLflow Tracing Latency Overhead](/concepts/mlflow-tracing-latency-overhead.md) — Performance considerations for tracing
- MLflow ContextVar — The underlying Python mechanism for trace context propagation

## Sources

- tracing-faq-databricks-on-aws.md

# Citations

1. [tracing-faq-databricks-on-aws.md](/references/tracing-faq-databricks-on-aws-83ee1878.md)
