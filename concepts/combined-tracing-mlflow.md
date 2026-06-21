---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f0a2deafb60fec4a7fd14104df44e1bfda84f20dcfb0a3abcf459ebadec21aac
  pageDirectory: concepts
  sources:
    - add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - combined-tracing-mlflow
    - CT(
  citations:
    - file: add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
title: Combined Tracing (MLflow)
description: Strategy that mixes automatic and manual tracing approaches for complete coverage of application traces.
tags:
  - mlflow
  - tracing
  - observability
timestamp: "2026-06-18T14:19:48.406Z"
---

# Combined Tracing (MLflow)

**Combined Tracing** in [MLflow](/concepts/mlflow.md) refers to the practice of mixing both automatic and manual tracing approaches within the same generative AI application to achieve complete observability coverage. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Overview

MLflow provides three approaches to tracing for Python and TypeScript generative AI applications: [Automatic Tracing (MLflow)](/concepts/automatic-tracing-mlflow.md), [Manual Tracing (MLflow)](/concepts/manual-tracing-mlflow.md), and Combined Tracing. Combined Tracing is specifically designed for scenarios where neither automatic nor manual tracing alone provides sufficient coverage for the application's full execution path. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## How Combined Tracing Works

Combined Tracing allows developers to use automatic tracing as the baseline for capturing application logic from 20+ supported libraries (via `mlflow.<library>.autolog()`) while simultaneously applying manual tracing techniques for custom logic, complex workflows, and areas where finer-grained control is needed. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

The manual component can be implemented using either:
- [Function Decorator APIs](/concepts/mlflowtrace-function-decorator.md) for simpler instrumentation
- Low-Level APIs for more complex tracing requirements

## When to Use Combined Tracing

Start with automatic tracing, as it is the fastest way to get traces working. Add manual tracing on top of automatic tracing when you need more control over specific portions of the application. This complementary approach ensures complete coverage across both standardized library calls and custom application logic. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Related Concepts

- [Automatic Tracing (MLflow)](/concepts/automatic-tracing-mlflow.md) — The baseline tracing approach for supported libraries
- [Manual Tracing (MLflow)](/concepts/manual-tracing-mlflow.md) — The targeted tracing approach for custom logic
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The broader MLflow ecosystem for generative AI applications
- [Tracing Integrations](/concepts/mlflow-tracing-integrations.md) — The 20+ supported libraries for automatic tracing

## Sources

- add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md

# Citations

1. [add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md](/references/add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws-91d388aa.md)
