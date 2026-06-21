---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eecbbf0e0c0158605053eb6c71f8d47748024b3e9b36487b26a2735d39f079d7
  pageDirectory: concepts
  sources:
    - add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - manual-tracing-for-mlflow
    - MTFM
  citations:
    - file: add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
title: Manual Tracing for MLflow
description: Manual approach to tracing designed for custom logic and complex workflows using function decorators or low-level APIs
tags:
  - mlflow
  - tracing
  - manual-instrumentation
timestamp: "2026-06-19T21:59:20.448Z"
---

# Manual Tracing for MLflow

**Manual Tracing for MLflow** is an approach to instrumenting generative AI applications where developers explicitly define which code paths, function calls, and workflow steps are captured as traces. Unlike [Automatic Tracing for MLflow](/concepts/automatic-tracing-mlflow.md), manual tracing gives developers fine-grained control over trace content, making it suitable for custom logic and complex workflows. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Overview

Manual tracing is designed for scenarios where automatic instrumentation is insufficient or where developers need precise control over what gets traced. It supports both Python and TypeScript applications through two API styles: [Function Decorator APIs](/concepts/mlflowtrace-function-decorator.md) and [Low-Level Tracing APIs](/concepts/common-pitfalls-of-low-level-tracing-apis.md). ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## When to Use Manual Tracing

Manual tracing is recommended when:

- You have custom logic that is not covered by the 20+ supported libraries for automatic tracing.
- You need to trace complex workflows with branching, retries, or conditional execution.
- You want to control which specific function calls or code blocks appear in traces.
- You need to add custom metadata, attributes, or spans to your traces.

Start with [Automatic Tracing for MLflow](/concepts/automatic-tracing-mlflow.md) as it is the fastest way to get traces working. Add manual tracing later if you need more control. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## API Styles

### Function Decorator APIs

The Function Decorator approach uses Python decorators to mark functions for tracing. This is the simpler of the two manual tracing methods and is well-suited for tracing individual function calls within a workflow. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

### Low-Level APIs

The low-level APIs provide more granular control over trace creation, span management, and metadata attachment. This approach is designed for complex workflows where you need to manually start and end spans, add attributes, and manage trace context. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Combined Approach

Manual tracing can be combined with automatic tracing for complete coverage. In this approach, automatic tracing handles the standard library calls while manual tracing captures custom logic and workflow orchestration. This is documented under [Combine Manual and Automatic Tracing](/concepts/combined-manual-and-automatic-tracing.md). ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Related Concepts

- [Automatic Tracing for MLflow](/concepts/automatic-tracing-mlflow.md) — One-line instrumentation for supported libraries
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Overview of the tracing system
- [Function Decorator APIs](/concepts/mlflowtrace-function-decorator.md) — Decorator-based manual tracing
- [Low-Level Tracing APIs](/concepts/common-pitfalls-of-low-level-tracing-apis.md) — Fine-grained trace control
- [Combine Manual and Automatic Tracing](/concepts/combined-manual-and-automatic-tracing.md) — Using both approaches together
- Supported Libraries for MLflow Tracing — Libraries compatible with automatic tracing
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizational unit for runs and traces

## Sources

- add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md

# Citations

1. [add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md](/references/add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws-91d388aa.md)
