---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9d5b7e81bfe35ed67bc7035ff6273a2f91a06f44b4f91cd15996c217183a9705
  pageDirectory: concepts
  sources:
    - add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-python-sdk-for-tracing
    - MPSFT
  citations:
    - file: add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
title: MLflow Python SDK for Tracing
description: Python-based APIs in MLflow for instrumenting generative AI applications with tracing, supporting autolog, decorator, and low-level patterns.
tags:
  - mlflow
  - python-sdk
  - tracing
timestamp: "2026-06-19T17:28:00.103Z"
---

## MLflow Python SDK for Tracing

The **MLflow Python SDK for Tracing** provides tools to instrument generative AI and machine learning applications by capturing detailed traces of execution. Traces record the sequence of operations, including inputs, outputs, timing, and metadata, making it easier to debug, monitor, and optimize application behavior.

### Overview

MLflow offers three distinct approaches to add tracing to Python applications: **automatic**, **manual** (via function decorator or low-level APIs), and a **combined** approach that mixes both. These approaches are also available for the MLflow TypeScript SDK. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

### Automatic Tracing

Automatic tracing is the simplest method. By adding a single line of code – `mlflow.<library>.autolog()` – the SDK automatically captures traces for over 20 [supported MLflow tracings libraries](/concepts/mlflow-supported-tracing-libraries.md). This method requires minimal code changes and is the recommended starting point. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

### Manual Tracing

For custom logic or complex workflows where automatic coverage is insufficient, MLflow provides manual tracing APIs. These give the developer fine-grained control over what gets traced.

- **Function Decorator API**: Apply a decorator to specific functions to trace their calls. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]
- **Low-Level API**: Use lower-level tracing primitives to instrument arbitrary code blocks. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

Both APIs allow selective tracing and are designed for situations where automatic tracing cannot capture the necessary detail. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

### Combined Approach

Automatic and manual tracing can be used together for complete coverage. Developers can enable automatic tracing for standard library calls and supplement it with manual traces for custom or non‑standard application logic. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

### Which Approach Should I Use?

MLflow recommends starting with automatic tracing, as it is the fastest way to get traces working. Manual tracing can be added later when more control or detail is needed. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

### Related Concepts

- MLflow Tracing Overview
- [Automatic Tracing with MLflow](/concepts/automatic-tracing-mlflow.md)
- [Manual Tracing with MLflow](/concepts/manual-tracing-mlflow.md)
- [MLflow TypeScript SDK for Tracing](/concepts/mlflow-typescript-sdk-for-tracing.md)

### Sources

- add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md

# Citations

1. [add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md](/references/add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws-91d388aa.md)
