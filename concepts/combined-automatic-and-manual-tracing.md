---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4f81908d6ea2a8af5392b8c73280a66cf0d7aa9f0640d4ed4ef43bbfe1ae4c4c
  pageDirectory: concepts
  sources:
    - add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - combined-automatic-and-manual-tracing
    - Manual Tracing and Combined Automatic
    - CAAMT
    - Automatic and manual tracing
  citations:
    - file: add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
title: Combined Automatic and Manual Tracing
description: Hybrid approach that mixes automatic autolog() tracing with manual tracing for complete coverage
tags:
  - mlflow
  - tracing
  - hybrid-approach
timestamp: "2026-06-19T21:59:23.626Z"
---

# Combined Automatic and Manual Tracing

**Combined Automatic and Manual Tracing** is an approach in MLflow that mixes both [Automatic Tracing](/concepts/automatic-tracing.md) and [Manual Tracing](/concepts/manual-tracing.md) within the same application to achieve complete trace coverage. This hybrid strategy allows developers to benefit from the simplicity of automated instrumentation while retaining fine-grained control over custom or complex logic. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Overview

MLflow provides three approaches to tracing Python and [TypeScript SDK](/concepts/mlflow-typescript-tracing-sdk.md) generative AI applications:

- **Automatic**: Add one line (`mlflow.<library>.autolog()`) to automatically capture app logic for 20+ supported libraries. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]
- **Manual**: Designed for custom logic and complex workflows, using [Function Decorator APIs](/concepts/mlflowtrace-function-decorator.md) or low-level APIs. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]
- **Combined**: Mix both approaches for complete coverage. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Recommended Workflow

MLflow recommends starting with automatic tracing as the fastest way to get traces working. Manual tracing can be added later when more control is needed over specific application components. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## When to Use Combined Tracing

Combined tracing is appropriate when:

- You want automated instrumentation for standard library calls (e.g., LangChain, OpenAI, or other supported frameworks)
- You need manual instrumentation for custom logic, complex workflows, or proprietary code paths
- You require complete end-to-end trace coverage across all application components

## Related Concepts

- [Automatic Tracing](/concepts/automatic-tracing.md) — One-line setup for standard library instrumentation
- [Manual Tracing](/concepts/manual-tracing.md) — Granular control using decorator and low-level APIs
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Overall tracing framework for generative AI applications
- Generative AI Application Monitoring — Broader monitoring context for AI applications

## Sources

- add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md

# Citations

1. [add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md](/references/add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws-91d388aa.md)
