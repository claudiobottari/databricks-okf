---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d88730a98d790bc5a60a8dfff318172dba0dc474f72870f9f1d5e2e41a723ed2
  pageDirectory: concepts
  sources:
    - add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-manual-tracing
    - MMT
  citations:
    - file: add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
title: MLflow Manual Tracing
description: Manual approach using function decorator APIs or low-level APIs for custom logic and complex workflow tracing.
tags:
  - mlflow
  - tracing
  - instrumentation
timestamp: "2026-06-19T13:54:10.879Z"
---

---
title: MLflow Manual Tracing
summary: Fine-grained control over trace instrumentation for custom logic and complex workflows using Function Decorator APIs or low-level APIs
sources:
  - add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:40:32.713Z"
updatedAt: "2026-06-18T10:40:32.713Z"
tags:
  - mlflow
  - tracing
  - python
  - typescript
aliases:
  - mlflow-manual-tracing
  - MMT
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 1
---

# MLflow Manual Tracing

**MLflow Manual Tracing** is an explicit instrumentation approach for capturing traces in custom or complex generative AI applications. Unlike [Automatic Tracing](/concepts/automatic-tracing.md), where a single call to `mlflow.<library>.autolog()` automatically captures logic from more than 20 supported libraries, manual tracing gives you full control over what is traced and how the trace hierarchy is structured. It is available for both Python and TypeScript applications. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Overview

Manual tracing is designed for workflows that involve custom logic, multi-step chains, branching, or other patterns not covered by automatic instrumentation. You can instrument your application using either of two APIs:^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

- **Function Decorator APIs** — Apply a decorator to any function you want traced. Each decorated function call becomes a Span nested inside the parent trace.
- **Low-level APIs** — Start and end spans manually using `start_span()` / `end_span()` calls, giving you fine-grained control over trace structure and metadata.

## When to Use Manual Tracing

Start with automatic tracing because it is the fastest way to get traces working. Add manual tracing later if you need more control, for example when:^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

- Your application uses libraries not covered by [MLflow Tracing Integrations](/concepts/mlflow-tracing-integrations.md).
- You need to trace only specific parts of a complex pipeline, not the entire execution.
- You want to attach custom attributes, inputs, outputs, or structured metadata to individual spans.
- You are building a multi-step agent or retrieval-augmented generation (RAG) system where the control flow is not captured by automatic instrumentation.

## Implementation Approaches

### Function Decorator APIs

Apply a decorator (e.g., `@mlflow.span()` or `@mlflow.trace()`) to any function. The function’s inputs and outputs are automatically recorded, and the span is linked to the current active trace. This is the simplest manual approach and works well for most custom logic. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

### Low-Level APIs

Use `mlflow.start_span()` to create a span, set its attributes, input, output, and later call `mlflow.end_span()` to close it. This approach is useful when you need to create spans outside the scope of a function call, for example inside a loop or a callback. It also allows you to set span status or record exceptions. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Combined Approach

You can mix automatic and manual tracing in the same application. For instance, enable `mlflow.autolog()` to capture calls to supported libraries, then add manual decorators or low-level spans around custom orchestration logic. The two approaches produce a single unified trace, giving you complete coverage without losing detail. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Best Practices

- Start with automatic tracing to get baseline traces, then layer manual instrumentation only where needed.
- Use function decorators whenever possible; they require less boilerplate than low-level APIs.
- Keep span names descriptive and consistent to make traces easier to read in the MLflow UI.
- Set the `span_type` attribute to classify spans (e.g., `CHAIN`, `LLM`, `TOOL`, `RETRIEVER`) for better filtering and analysis.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The overall tracing framework
- [Automatic Tracing](/concepts/automatic-tracing.md) — One-line instrumentation for supported libraries
- Spans — Individual units of work within a trace
- [Function Decorator APIs](/concepts/mlflowtrace-function-decorator.md) — Decorator-based manual tracing
- Low-Level APIs — Programmatic span creation
- [MLflow Tracing Integrations](/concepts/mlflow-tracing-integrations.md) — Supported libraries for automatic tracing

## Sources

- add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md

# Citations

1. [add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md](/references/add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws-91d388aa.md)
