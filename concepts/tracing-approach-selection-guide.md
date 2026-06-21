---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3fd085f0eb0801f52f90278fce53205d2ede162dc5f9d5d9cd5c0fb14c5eb2fd
  pageDirectory: concepts
  sources:
    - add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tracing-approach-selection-guide
    - TASG
    - mlflow-tracing-approach-selection-guide
    - MTASG
  citations:
    - file: add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
title: Tracing Approach Selection Guide
description: Recommendation to start with automatic tracing and add manual tracing later when more control is needed
tags:
  - mlflow
  - tracing
  - best-practices
timestamp: "2026-06-19T21:59:32.535Z"
---

# Tracing Approach Selection Guide

The **Tracing Approach Selection Guide** helps determine which [MLflow Tracing](/concepts/mlflow-tracing.md) approach to use when adding observability to Python and TypeScript generative AI applications. MLflow offers three approaches to tracing: automatic, manual, and combined. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Recommended Approach

Start with **automatic tracing** as it is the fastest way to get traces working. Add manual tracing later if you need more control over what gets captured. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Approach Comparison

### Automatic Tracing

Automatic tracing requires a single line of code — `mlflow.<library>.autolog()` — to automatically capture app logic for over 20 supported libraries. This approach is ideal for rapid instrumentation with minimal code changes. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

### Manual Tracing

Manual tracing is designed for custom logic and complex workflows. It provides fine-grained control over what gets traced using [Function Decorator APIs](/concepts/mlflowtrace-function-decorator.md) or low-level APIs. Use this approach when you need to trace specific custom functions or complex orchestration logic that automatic tracing cannot capture. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

### Combined Approach

The combined approach mixes automatic and manual tracing for complete coverage. This allows you to automatically capture standard library interactions while adding manual traces for custom business logic or non-standard integrations. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Decision Flow

1. **Start** with automatic tracing by adding `mlflow.<library>.autolog()`.
2. **Evaluate** whether the captured traces meet your observability needs.
3. **Add manual tracing** if you need to trace custom logic, complex workflows, or unsupported libraries.
4. **Use the combined approach** when you want both automatic coverage and manual control simultaneously.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — Overview of the tracing system
- [Automatic Tracing](/concepts/automatic-tracing.md) — One-line instrumentation for supported libraries
- [Manual Tracing](/concepts/manual-tracing.md) — Custom instrumentation for fine-grained control
- [Function Decorator APIs](/concepts/mlflowtrace-function-decorator.md) — Decorator-based manual tracing
- Low-Level APIs — Programmatic manual tracing with full control
- Supported Libraries — Libraries compatible with automatic tracing

## Sources

- add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md

# Citations

1. [add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md](/references/add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws-91d388aa.md)
