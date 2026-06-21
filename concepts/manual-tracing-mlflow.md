---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2fd7b363f8ec55072a71bb96c1a1e5946d234301c687c609e46d6d73a9c89e86
  pageDirectory: concepts
  sources:
    - add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - manual-tracing-mlflow
    - MT(
    - Manual Tracing in MLflow
    - Manual Tracing with MLflow
    - Manual Tracing with @mlflow.trace
    - Manual tracing with function decorators
  citations:
    - file: add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
title: Manual Tracing (MLflow)
description: Approach for tracing custom logic and complex workflows using Function Decorator APIs or low-level APIs for fine-grained control.
tags:
  - mlflow
  - tracing
  - observability
timestamp: "2026-06-18T14:19:42.304Z"
---

# Manual Tracing (MLflow)

**Manual Tracing** is an approach in [MLflow Tracing](/concepts/mlflow-tracing.md) that gives you fine-grained control over which parts of your [generative AI application](/concepts/tracing-for-generative-ai-applications.md) logic are captured as traces. It is designed for custom logic and complex workflows where automatic tracing is insufficient. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Overview

MLflow provides three approaches to instrument Python and TypeScript applications: automatic, manual, and combined. Manual tracing is intended for scenarios where you need to trace custom logic or multi-step workflows that are not automatically captured by the built-in library integrations. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## APIs for Manual Tracing

Manual tracing can be implemented using two sets of APIs:

- **[Function Decorator APIs](/concepts/mlflowtrace-function-decorator.md)** – Apply a decorator (e.g., `@mlflow.trace()`) to individual functions to automatically capture their inputs, outputs, and execution duration as spans in a trace.
- **Low-Level APIs** – Use a programmatic API (e.g., `mlflow.start_span()` / `mlflow.end_span()`) to create and manage spans explicitly, offering the maximum level of control over the trace structure.

Both API families are available for Python and TypeScript. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## When to Use Manual Tracing

Start with [Automatic Tracing (MLflow)](/concepts/automatic-tracing-mlflow.md), which requires only a single line (`mlflow.<library>.autolog()`) and works with 20+ supported libraries. If you need to trace custom logic that falls outside those library integrations, add manual tracing on top of — or instead of — automatic tracing. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Combining Manual and Automatic Tracing

Manual and automatic tracing can be mixed within the same application. This combined approach provides complete coverage: automatic tracing handles library-internal calls, while manual tracing captures the custom orchestration logic that ties those calls together. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Related Concepts

- [Automatic Tracing (MLflow)](/concepts/automatic-tracing-mlflow.md)
- [Combined Tracing](/concepts/combined-tracing.md)
- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [Function Decorator APIs](/concepts/mlflowtrace-function-decorator.md)
- [Low-Level Tracing APIs](/concepts/common-pitfalls-of-low-level-tracing-apis.md)
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md)

## Sources

- add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md

# Citations

1. [add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md](/references/add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws-91d388aa.md)
