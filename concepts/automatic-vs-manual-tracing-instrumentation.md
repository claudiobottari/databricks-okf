---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 61f8aa7129b478806364204d94c2d64fa8cb65515672efa7630e8bf7d1efc096
  pageDirectory: concepts
  sources:
    - mlflow-tracing-genai-observability-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - automatic-vs-manual-tracing-instrumentation
    - AVMTI
    - Automatic Tracing Integrations
    - Automatic tracing integrations
    - Tracing Instrumentation
  citations:
    - file: mlflow-tracing-genai-observability-databricks-on-aws.md
title: Automatic vs Manual Tracing Instrumentation
description: "Two approaches to instrumenting GenAI applications for tracing: automatic (framework-integrated) and manual (developer-defined)."
tags:
  - instrumentation
  - tracing
  - mlflow
  - integration
timestamp: "2026-06-19T19:40:47.763Z"
---

# Automatic vs Manual Tracing Instrumentation

**Automatic vs Manual Tracing Instrumentation** refers to the two approaches available in [MLflow Tracing](/concepts/mlflow-tracing.md) for instrumenting [GenAI](/concepts/mlflow-genai-evaluate-api.md) applications to capture end-to-end observability data. Users can choose between automatic and manual tracing when setting up their application. ^[mlflow-tracing-genai-observability-databricks-on-aws.md]

## Overview

[MLflow Tracing](/concepts/mlflow-tracing.md) provides both automatic and manual instrumentation approaches to record inputs, outputs, intermediate steps, and metadata for GenAI applications, including complex agent-based systems. The choice between automatic and manual tracing allows users to balance ease of setup with fine-grained control over what is traced. ^[mlflow-tracing-genai-observability-databricks-on-aws.md]

## Automatic Tracing

Automatic tracing instruments an application without requiring user code changes. It automatically captures traces based on framework‑specific hooks and predefined instrumentation points. This approach is suitable for quick setup and standard use cases. ^[mlflow-tracing-genai-observability-databricks-on-aws.md]

## Manual Tracing

Manual tracing gives users full control over which operations are traced and what metadata is included. Developers explicitly add instrumentation calls (e.g., `mlflow.trace()`) to the code. This approach is useful when custom logic or sensitive data handling requires selective tracing. ^[mlflow-tracing-genai-observability-databricks-on-aws.md]

## Choosing Between Automatic and Manual Tracing

The official Databricks documentation on *Instrument your app* provides guidance on selecting between the two approaches. Users are advised to review that page to understand the trade‑offs and integration steps for their specific application. ^[mlflow-tracing-genai-observability-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [GenAI Observability](/concepts/genai-observability.md)
- Agent-Based Systems
- [Trace Data Analysis](/concepts/mlflow-trace-analysis.md)

## Sources

- mlflow-tracing-genai-observability-databricks-on-aws.md

# Citations

1. [mlflow-tracing-genai-observability-databricks-on-aws.md](/references/mlflow-tracing-genai-observability-databricks-on-aws-9bbb7d89.md)
