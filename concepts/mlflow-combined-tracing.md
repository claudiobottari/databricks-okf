---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7d30316ca9fb06b67b616ca72561bb3085e95f56527057d2879235e8d38ff621
  pageDirectory: concepts
  sources:
    - add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-combined-tracing
    - MCT
  citations:
    - file: add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
title: MLflow Combined Tracing
description: Hybrid approach mixing automatic and manual tracing to achieve complete coverage of application traces
tags:
  - mlflow
  - tracing
  - python
timestamp: "2026-06-19T08:54:14.069Z"
---

Here is the wiki page for "MLflow Combined Tracing".

---

# MLflow Combined Tracing

**MLflow Combined Tracing** refers to the practice of using both [Automatic Tracing](/concepts/automatic-tracing.md) and [Manual Tracing](/concepts/manual-tracing.md) together within the same generative AI application. This approach gives you the speed of automatic instrumentation while retaining fine-grained control over custom or complex logic.

## Overview

MLflow provides three tracing approaches for Python and TypeScript applications:

- **Automatic** – Add a single call such as `mlflow.<library>.autolog()` to automatically capture traces for 20+ [supported libraries](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/).
- **Manual** – Designed for custom workflows; control what gets traced using function decorator APIs or low‑level APIs.
- **Combined** – Mix both approaches for complete coverage. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## How Combined Tracing Works

In combined mode you enable `autolog()` for one or more supported libraries to capture standard interactions (e.g., OpenAI API calls, LangChain chains) automatically. Simultaneously, you add manual tracing — via decorators like `@mlflow.trace` or the lower-level `start_span()` API — around custom business logic or any code path not covered by autolog. The resulting trace is a unified tree of spans that includes both automatically captured segments and manually instrumented steps.

Unlike pure automatic tracing, combined tracing allows you to instrument every part of your application — not just the 20+ libraries that MLflow supports out-of-the-box.

## When to Use Combined Tracing

- **Fast prototyping, then refinement** – Start with automatic tracing to get immediate visibility. Add manual tracing later when you need to instrument custom preprocessing, post‑processing, or proprietary model calls that autolog does not capture. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]
- **Partial library coverage** – If only some of the libraries you use are supported by autolog, combined tracing lets you manually trace the unsupported ones while keeping autolog for the rest.
- **Granular control plus convenience** – You want autolog for major framework calls but also need to add custom attributes, create nested spans for non‑standard operations, or omit certain spans from automatic capture.

## Getting Started

1. **Enable automatic tracing** for the libraries you use – for example, `mlflow.openai.autolog()` or `mlflow.langchain.autolog()`.
2. **Add manual instrumentation** around custom code using the [`@mlflow.trace` decorator](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/manual-tracing/function-decorator) or the [`start_span()` low‑level API](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/manual-tracing/low-level-api).
3. **Run your application** – traces are automatically logged to the active MLflow experiment, combining both sources.

No special configuration is needed to "combine" the two approaches; autolog and manual instrumentation coexist naturally as long as they are active in the same session.

## Best Practices

- **Start with automatic tracing** – it is the fastest way to get traces working. Add manual tracing only when you identify gaps in coverage. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]
- **Use consistent span naming** between automatic and manual spans to make trace trees easier to read.
- **Avoid double instrumentation** – if a library is already covered by autolog, do not also wrap its calls with manual tracing, as that can create duplicate spans.

## Related Concepts

- [Automatic Tracing](/concepts/automatic-tracing.md) – One‑line instrumentation for supported libraries.
- [Manual Tracing](/concepts/manual-tracing.md) – Custom instrumentation via decorators or low‑level APIs.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – The overarching framework for capturing traces.
- Spans – Individual operations within a trace.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – Where traces are stored and organized.

## Sources

- add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md

# Citations

1. [add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md](/references/add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws-91d388aa.md)
