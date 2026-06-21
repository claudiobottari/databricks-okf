---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fcd300f81fb6c9db64c246290f8b5a515841832828febe23f2868da33f812154
  pageDirectory: concepts
  sources:
    - add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-approach-selection-guide
    - MTASG
  citations:
    - file: add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
title: MLflow Tracing Approach Selection Guide
description: Guidance on choosing between automatic, manual, or combined tracing, recommending starting with automatic tracing for fastest results
tags:
  - mlflow
  - tracing
  - best-practices
timestamp: "2026-06-19T08:53:40.627Z"
---

---
title: [MLflow Tracing](/concepts/mlflow-tracing.md) Approach Selection Guide
summary: A guide to choosing between automatic, manual, or combined tracing in MLflow for generative AI applications, based on the level of control and complexity needed.
sources:
  - add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T15:00:00.000Z"
updatedAt: "2026-06-18T15:00:00.000Z"
tags:
  - mlflow
  - tracing
  - generative-ai
  - instrumentation
  - observability
aliases:
  - mlflow-tracing-approach-selection-guide
  - M-TASG
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# [MLflow Tracing](/concepts/mlflow-tracing.md) Approach Selection Guide

The **MLflow Tracing Approach Selection Guide** helps developers choose the right instrumentation strategy for adding [Traces](/concepts/traces.md) to their generative AI applications. MLflow offers three approaches to tracing for Python (and TypeScript): automatic, manual, and combined. The choice depends on the level of control required and the complexity of the application logic.

## Overview

[MLflow Tracing](/concepts/mlflow-tracing.md) captures the execution path of a generative AI application, recording inputs, outputs, and intermediate steps for debugging, monitoring, and evaluation. There are three complementary approaches: ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

- **Automatic** – Fastest setup; one line of code captures traces for 20+ supported libraries.
- **Manual** – Full control over what is traced; designed for custom logic and complex workflows.
- **Combined** – Mix both approaches for complete coverage.

## Automatic Tracing

Automatic tracing is the recommended starting point. By adding a single line such as `mlflow.<library>.autolog()`, MLflow automatically captures traces from over 20 supported integrations (e.g., OpenAI, LangChain, Hugging Face). This approach is ideal for standard, library-based workflows where you want to get traces working as quickly as possible. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

### When to Use Automatic Tracing

- You are using supported libraries and need minimal code changes.
- You want to quickly prototype tracing for debugging or evaluation.
- You do not require granular control over what gets traced.

## Manual Tracing

Manual tracing is designed for applications with custom logic or complex workflows that are not fully covered by automatic instrumentation. MLflow provides two APIs for manual tracing: a [function decorator API](/concepts/mlflowtrace-function-decorator.md) and a low-level API. These allow you to explicitly annotate functions or spans, control what data is recorded, and structure traces to match your application’s architecture. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

### When to Use Manual Tracing

- Your application uses custom callbacks, chains, or non-standard orchestration patterns.
- You need to trace specific components with detailed context (e.g., intermediate reasoning steps).
- You want to exclude certain library calls from traces to reduce noise.

## Combined Tracing

Combined tracing uses automatic instrumentation as a base and supplements it with manual annotations for custom logic. This approach provides the best of both worlds: broad coverage from autologging plus fine‑grained control where needed. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

### When to Use Combined Tracing

- You have a standard pipeline built on supported libraries but also custom processing steps.
- You want to automatically capture library calls while manually instrumenting business‑specific logic.
- You are iterating from a simple prototype toward a production application.

## Selection Guide

The following table summarizes the decision criteria:

| Approach | Setup Effort | Control Level | Best For |
|---|---|---|---|
| Automatic | Low (one line) | Low | Fast onboarding, standard library usage |
| Manual | Medium to High | High | Custom logic, complex workflows |
| Combined | Medium | Medium‑High | Blended library + custom code |

Start with automatic tracing; it is the fastest way to get traces working. Add manual tracing later only if you need more control over the captured data. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – Overview of tracing in MLflow.
- Supported Integrations for Automatic Tracing – List of libraries support by autolog.
- Function Decorator API – Decorator‑based manual tracing.
- [Low-level API for Manual Tracing](/concepts/manual-tracing-apis.md) – Fine‑grained span control.
- [Evaluating Traces](/concepts/evaluation-traces.md) – Using traces for offline quality evaluation.

## Sources

- add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md

# Citations

1. [add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md](/references/add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws-91d388aa.md)
