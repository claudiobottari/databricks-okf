---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 95efe2b4fd872de4b9c7d4970dedd8f9c78fa806cb1fc470b487b4822554bfc9
  pageDirectory: concepts
  sources:
    - tracing-faq-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-enable-and-disable-api
    - Disable API and MLflow Tracing Enable
    - MTEADA
  citations:
    - file: tracing-faq-databricks-on-aws.md
title: MLflow Tracing Enable and Disable API
description: mlflow.tracing.disable() ceases trace data collection and mlflow.tracing.enable() re-enables tracing for instrumented models.
tags:
  - mlflow
  - tracing
  - api
  - configuration
timestamp: "2026-06-19T23:11:44.229Z"
---

# [MLflow Tracing](/concepts/mlflow-tracing.md) Enable and Disable API

The **MLflow Tracing Enable and Disable API** provides functions to temporarily suspend or resume the collection of trace data in [MLflow Tracing](/concepts/mlflow-tracing.md). These APIs are useful for controlling tracing behavior during development or testing without modifying instrumentation code.

## Overview

[MLflow Tracing](/concepts/mlflow-tracing.md) collects spans and metrics from instrumented models and agents for debugging and monitoring. To reduce overhead or avoid logging unwanted data, users can programmatically disable tracing using `mlflow.tracing.disable()` and re-enable it later with `mlflow.tracing.enable()`. ^[tracing-faq-databricks-on-aws.md]

## `mlflow.tracing.disable()`

The `mlflow.tracing.disable()` API ceases all collection of trace data from within [MLflow](/concepts/mlflow.md). When called, no new spans are recorded, and no trace data is logged to the [MLflow Tracking Service](/concepts/remote-mlflow-tracking-server.md). ^[tracing-faq-databricks-on-aws.md]

This function is intended for temporary disabling; tracing is not persistent across sessions unless explicitly re-enabled. ^[tracing-faq-databricks-on-aws.md]

## `mlflow.tracing.enable()`

The `mlflow.tracing.enable()` API re‑enables tracing functionality after it has been temporarily disabled. Once called, instrumented models and functions will again have their [Traces](/concepts/traces.md) collected and logged. ^[tracing-faq-databricks-on-aws.md]

If tracing was never disabled, calling `enable()` has no effect. ^[tracing-faq-databricks-on-aws.md]

## Usage Notes

- Both APIs are found in the `mlflow.tracing` module. Their exact signatures are not detailed in the FAQ, but they are called without arguments in typical use. ^[tracing-faq-databricks-on-aws.md]
- Disabling tracing is often used to suppress logging during non‑critical execution paths or to benchmark application latency without trace overhead. ^[tracing-faq-databricks-on-aws.md]
- Disabling does not affect previously completed [Traces](/concepts/traces.md); it only prevents new trace data from being collected. ^[tracing-faq-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – Overview of the tracing framework.
- [MLflow Tracking Service](/concepts/remote-mlflow-tracking-server.md) – Backend where trace data is logged.
- Instrumented Models – Models that have been wrapped to produce [Traces](/concepts/traces.md).
- [MLFLOW_TRACE_TIMEOUT_SECONDS](/concepts/mlflow-trace-timeout-mechanism.md) – A related control for halting long‑running [Traces](/concepts/traces.md).

## Sources

- tracing-faq-databricks-on-aws.md

# Citations

1. [tracing-faq-databricks-on-aws.md](/references/tracing-faq-databricks-on-aws-83ee1878.md)
