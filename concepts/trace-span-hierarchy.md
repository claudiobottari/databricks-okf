---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c75e2cea25650978b854b2fb22018e933b66e40a9a86e5f58bc6241b60bd0394
  pageDirectory: concepts
  sources:
    - get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - trace-span-hierarchy
    - TSH
    - Span Hierarchies
    - Span Hierarchy
    - Span hierarchy
    - trace-span-hierarchy-root-and-child-spans
    - child spans) and Trace span hierarchy (root
    - TSH(ACS
  citations:
    - file: get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md
title: Trace span hierarchy
description: The parent-child structure of spans within an MLflow trace, where a root span (e.g., an application entry point function) can contain child spans (e.g., individual LLM API calls), providing hierarchical visibility into application execution.
tags:
  - tracing
  - observability
  - span
  - hierarchy
timestamp: "2026-06-19T10:44:17.300Z"
---

# Trace Span Hierarchy

**Trace span hierarchy** refers to the parent-child relationship structure formed by spans within a single [[MLflow Trace]]. This hierarchical organization captures the nested execution flow of a GenAI application, where each span represents a unit of work and spans can contain child spans that represent sub-operations.

## Overview

In [MLflow Tracing](/concepts/mlflow-tracing.md), a trace is composed of multiple spans organized in a tree-like hierarchy. The root span represents the top-level entry point of an application, while child spans represent nested function calls or operations that occur within that context. This structure enables detailed observability into complex GenAI workflows. ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

## Structure

### Root Span

The root span is the topmost span in the hierarchy and represents the primary entry point of the application. It captures the overall inputs and outputs of the traced function. For example, when using the `@mlflow.trace` decorator on a function, that function becomes the root span. ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

### Child Spans

Child spans are nested within parent spans and represent sub-operations that occur during execution. These can be automatically generated through library integrations (such as `mlflow.openai.autolog()`) or manually created using the `@mlflow.trace` decorator on helper functions. ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

## Example Hierarchy

A typical trace for a simple GenAI application might have the following structure:

```
Root span: my_app(input)
└── Child span: OpenAI completion request
    ├── Attributes: model name, token counts, timing
    ├── Inputs: messages sent to the model
    └── Outputs: response received from the model
```

^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

## Benefits of Span Hierarchy

The hierarchical structure provides valuable insights into application behavior, including:

- **What was asked**: The input passed to the root span
- **What response was generated**: The output from the root span
- **How long the request took**: Timing information at each span level
- **How many tokens were used**: Cost-related metrics captured in child spans

^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

For more complex applications like [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) systems or multi-step agents, the span hierarchy reveals the inner workings of each component and step, making it easier to debug and optimize performance. ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

## Related Concepts

- [[MLflow Trace]] — The complete record of an application execution
- [Span Attributes](/concepts/span-attributes-and-search.md) — Metadata associated with each span
- [Manual Tracing](/concepts/manual-tracing.md) — Using the `@mlflow.trace` decorator to create custom spans
- [Automatic Tracing](/concepts/automatic-tracing.md) — Library integrations that automatically create child spans
- [Tracing Instrumentation](/concepts/automatic-vs-manual-tracing-instrumentation.md) — Methods for adding tracing to applications

## Sources

- get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md

# Citations

1. [get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md](/references/get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws-860f2761.md)
