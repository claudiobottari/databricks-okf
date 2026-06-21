---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2931b2153d9a571fcc765670b6429e96a7272c95b8e0e526b0cf3e4ba28b360b
  pageDirectory: concepts
  sources:
    - add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-for-typescript
    - MTFT
  citations:
    - file: add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
title: MLflow Tracing for TypeScript
description: MLflow tracing support for TypeScript generative AI applications, alongside Python support
tags:
  - mlflow
  - tracing
  - typescript
timestamp: "2026-06-19T08:53:39.382Z"
---

# [MLflow Tracing](/concepts/mlflow-tracing.md) for TypeScript

**MLflow Tracing for TypeScript** enables developers to instrument generative AI applications written in TypeScript with distributed tracing. Tracing captures the full execution flow of an AI system — including model calls, tool invocations, and intermediate reasoning steps — helping developers debug, evaluate, and monitor application behavior.

## Overview

MLflow provides three approaches to adding traces to TypeScript applications, the same approaches available for Python. Developers can choose the method that best fits their use case and level of control needed.^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

### 1. Automatic Tracing

Automatic tracing requires minimal code changes. By calling a library-specific `autolog()` function, MLflow automatically captures traces for supported libraries. This is the fastest way to get traces working in a TypeScript project.^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

### 2. Manual Tracing

Manual tracing is designed for custom logic and complex workflows. Developers control exactly what gets traced using function decorator APIs or low-level APIs. This approach is useful when you need to instrument code that isn't covered by automatic tracing or when you want fine-grained control.^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

### 3. Combined Approach

The combined approach mixes both automatic and manual tracing for complete coverage. Developers can start with automatic tracing to capture the majority of calls and then add manual tracing for specific custom components.^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## When to Use Each Approach

Start with automatic tracing — it is the fastest way to get traces working. Add manual tracing later if you need more control or need to instrument custom logic not captured automatically.^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## TypeScript SDK

[MLflow Tracing](/concepts/mlflow-tracing.md) for TypeScript is available through the MLflow TypeScript SDK. For detailed API documentation and usage examples, see the official [TypeScript SDK documentation](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/typescript-sdk).^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — Overview of MLflow's tracing capabilities
- [Automatic Tracing](/concepts/automatic-tracing.md) — Capturing traces with minimal code
- [Manual Tracing](/concepts/manual-tracing.md) — Fine-grained control over trace instrumentation
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) — Using traces for quality assessment
- [GenAI Agent Tracing](/concepts/mlflow-genai-tracing.md) — Tracing for agent-based applications
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — MLflow's generative AI evaluation and monitoring platform

## Sources

- add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md

# Citations

1. [add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md](/references/add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws-91d388aa.md)
