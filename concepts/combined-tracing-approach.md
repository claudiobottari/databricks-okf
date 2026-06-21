---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aae732e1d318bac66fcc5829c73ec71f97e37ade2230cb0e93056db70f1d10f0
  pageDirectory: concepts
  sources:
    - add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - combined-tracing-approach
    - CTA
  citations:
    - file: add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
title: Combined Tracing Approach
description: Mixing automatic and manual tracing to achieve complete coverage of generative AI application traces.
tags:
  - mlflow
  - tracing
  - instrumentation
timestamp: "2026-06-19T13:54:11.025Z"
---

# Combined Tracing Approach

**Combined Tracing Approach** refers to the practice of mixing both [Automatic Tracing](/concepts/automatic-tracing.md) and [Manual Tracing](/concepts/manual-tracing.md) techniques within a single application to achieve complete coverage of trace data for Generative AI applications on the Databricks platform.

## Overview

MLflow provides three approaches to tracing for Python and TypeScript generative AI applications. The combined approach allows developers to leverage the benefits of both automatic and manual tracing simultaneously, ensuring that no application logic goes untraced. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## When to Use the Combined Approach

The recommended workflow is to start with [Automatic Tracing](/concepts/automatic-tracing.md), as it provides the fastest way to get traces working with minimal code changes. Developers can add [Manual Tracing](/concepts/manual-tracing.md) later if they need more control over specific parts of their application logic. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Implementation

### Automatic Tracing

Automatic tracing requires adding a single line of code to enable tracing for 20+ supported libraries:

```python
mlflow.<library>.autolog()
```

This approach automatically captures app logic for supported integrations. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

### Manual Tracing

Manual tracing is designed for custom logic and complex workflows that may not be covered by automatic tracing. Developers can control what gets traced using:

- [Function Decorator APIs](/concepts/mlflowtrace-function-decorator.md) — Decorators that wrap specific functions to trace their execution
- Low-Level APIs — Fine-grained control over trace creation and management

^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

### Combining Both Approaches

By combining automatic and manual tracing, developers ensure comprehensive coverage:

1. Enable automatic tracing with `mlflow.<library>.autolog()` to capture standard library calls
2. Add manual tracing for custom logic, complex workflows, or code paths not covered by automatic tracing
3. Both traces are collected and managed by [MLflow Tracing](/concepts/mlflow-tracing.md) infrastructure

^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The underlying tracing system for generative AI applications
- [GenAI Application Monitoring](/concepts/mlflow-genai-production-monitoring.md) — Broader monitoring capabilities enabled by comprehensive tracing
- [TypeScript SDK for MLflow Tracing](/concepts/mlflow-typescript-sdk-for-tracing.md) — TypeScript support for tracing applications
- Supported Integrations for Automatic Tracing — The 20+ libraries supported by automatic tracing

## Sources

- add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md

# Citations

1. [add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md](/references/add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws-91d388aa.md)
