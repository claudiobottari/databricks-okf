---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ada198db53fb0e40a947c1f3c760febc7d79e302ee5af8e26ce38ad7031c9772
  pageDirectory: concepts
  sources:
    - add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - mlflow-supported-tracing-libraries
    - MSTL
    - Supported Tracing Integrations
    - supported MLflow tracings libraries
    - supported tracing integrations
  citations:
    - file: add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
title: MLflow Supported Tracing Libraries
description: The collection of 20+ supported libraries that can be automatically instrumented with mlflow.autolog() for tracing.
tags:
  - mlflow
  - tracing
  - integrations
timestamp: "2026-06-18T14:19:55.796Z"
---

## MLflow Supported Tracing Libraries

**MLflow Supported Tracing Libraries** refers to the collection of more than 20 Python and TypeScript generative AI and machine learning libraries for which MLflow provides automatic tracing capabilities. By adding a single line of code — `mlflow.<library>.autolog()` — you can automatically capture traces of your application’s logic without manual instrumentation. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

### Overview

Tracing is an essential part of observability for generative AI applications. MLflow offers three approaches to tracing in Python and TypeScript: automatic, manual, and combined. The automatic approach, which relies on the supported libraries, is the fastest way to get traces working. It is recommended to start with automatic tracing and add manual tracing later when more control over the traced logic is needed. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

### How Automatic Tracing Works

When you call `mlflow.<library>.autolog()`, MLflow automatically instruments the supported library to capture trace data related to the model inference, tool calls, or other operations. This requires no changes to your application code beyond the single `autolog` call. The exact set of libraries and their specific instrumentation details are documented in the [MLflow Tracing](/concepts/mlflow-tracing.md) Integrations reference. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

### List of Supported Libraries

The source material states that there are “20+ [supported libraries]”, but does not enumerate them. For a complete list of supported libraries and their usage, see the official MLflow documentation on [MLflow Tracing Integrations](/concepts/mlflow-tracing-integrations.md) (referenced in the source as a linked page). ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

### Combining Automatic and Manual Tracing

You can combine automatic tracing with manual tracing for complete coverage. Automatic tracing captures events from supported libraries, while [Manual Tracing](/concepts/manual-tracing.md) (using function decorator or low-level APIs) fills in any custom logic not covered by the automatic instrumentation. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

### Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — Overview of the tracing system
- [Manual Tracing](/concepts/manual-tracing.md) — Approaches for custom instrumentation
- Function Decorator API — One method of manual tracing
- [Low-Level Tracing API](/concepts/common-pitfalls-of-low-level-tracing-apis.md) — Another method of manual tracing
- Autolog Documentation — General `autolog` configuration

### Sources

- add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md

# Citations

1. [add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md](/references/add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws-91d388aa.md)
