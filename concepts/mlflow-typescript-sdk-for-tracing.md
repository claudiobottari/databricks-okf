---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e91ef3a8accd461d51af88a898a04d2459928dc2ac0b6fca2c60f3c233e3e924
  pageDirectory: concepts
  sources:
    - add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-typescript-sdk-for-tracing
    - MTSFT
    - TypeScript SDK for MLflow Tracing
  citations:
    - file: add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
title: MLflow TypeScript SDK for Tracing
description: TypeScript-based APIs in MLflow for instrumenting generative AI applications with tracing, providing similar capabilities to the Python SDK.
tags:
  - mlflow
  - typescript-sdk
  - tracing
timestamp: "2026-06-19T17:28:04.117Z"
---

# MLflow TypeScript SDK for Tracing

The **MLflow TypeScript SDK for Tracing** provides tracing capabilities for TypeScript generative AI applications. It supports the same three tracing approaches available in the Python SDK: automatic, manual, and combined. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Available Approaches

### Automatic Tracing
Add a single line of code (equivalent to `mlflow.<library>.autolog()` in Python) to automatically capture app logic for over 20 supported libraries. This is the fastest way to get traces working. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

### Manual Tracing
Designed for custom logic and complex workflows, manual tracing gives you full control over what gets traced. It can be implemented using function decorator APIs or low-level APIs. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

### Combined Tracing
Mix automatic and manual tracing approaches together for complete coverage of your application’s execution. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Getting Started Recommendations

Databricks recommends starting with automatic tracing because it is the quickest way to begin generating traces. You can add manual tracing later if you need more fine-grained control over what is captured. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

For detailed usage instructions, refer to the [TypeScript SDK documentation](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/typescript-sdk). ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Related Concepts

- [Automatic Tracing in MLflow](/concepts/automatic-tracing-mlflow.md)
- [Manual Tracing in MLflow](/concepts/manual-tracing-mlflow.md)
- MLflow Tracing Overview
- Generative AI Application Monitoring

## Sources

- add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md

# Citations

1. [add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md](/references/add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws-91d388aa.md)
