---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 45828698180aa405aab871b8acfcf90bd8d8914aefd5f0b93b76775d79b94834
  pageDirectory: concepts
  sources:
    - add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
    - manual-tracing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - manual-tracing
    - Manual MLflow Tracing
    - Manual spans
  citations:
    - file: manual-tracing-databricks-on-aws.md
    - file: add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
title: Manual Tracing
description: An MLflow tracing approach designed for custom logic and complex workflows, offering Function Decorator APIs and low-level APIs for fine-grained control over what gets traced.
tags:
  - mlflow
  - manual-tracing
  - instrumentation
timestamp: "2026-06-19T17:28:00.587Z"
---

# Manual Tracing

**Manual tracing** is an approach to adding traces to Python and TypeScript generative AI applications that gives developers complete control over instrumentation, unlike [Automatic Tracing](/concepts/automatic-tracing.md) which captures logic automatically with a single line of code. ^[manual-tracing-databricks-on-aws.md]

While automatic tracing provides instant observability for supported frameworks, manual tracing is designed for custom logic and complex workflows, allowing you to define exactly which parts of your code to trace, create custom hierarchies of spans, and control span boundaries and relationships. ^[manual-tracing-databricks-on-aws.md]

## When to Use Manual Tracing

Manual tracing is the right choice when you need:

- **Fine-grained control over trace structure** – define exactly which parts of your code to trace, create custom hierarchies of spans, and control span boundaries and relationships. ^[manual-tracing-databricks-on-aws.md]
- **Custom framework instrumentation** – instrument proprietary or internal frameworks, add tracing to custom LLM wrappers, or support new libraries before official integration. ^[manual-tracing-databricks-on-aws.md]
- **Advanced workflow scenarios** – multi-threaded or async operations, streaming responses with custom aggregation, complex nested operations, and custom trace metadata and attributes. ^[manual-tracing-databricks-on-aws.md]

## Which API to Use

MLflow’s manual tracing provides two API options:

- **[Function Decorator APIs](/concepts/mlflowtrace-function-decorator.md)** – for declaratively wrapping functions with tracing.
- **Low-Level APIs** – for programmatic control over span creation and lifecycle.

Choose the approach that best fits your instrumentation needs. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md, manual-tracing-databricks-on-aws.md]

## Combined Approach

Manual tracing can be combined with automatic tracing for complete coverage. The recommendation is to start with automatic tracing (the fastest way to get traces working) and add manual tracing later if you need more control. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Related Concepts

- [Automatic Tracing](/concepts/automatic-tracing.md)
- [Combined Tracing](/concepts/combined-tracing.md)
- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [Function Decorator APIs](/concepts/mlflowtrace-function-decorator.md)
- Low-Level APIs
- GenAI Application Instrumentation

## Sources

- manual-tracing-databricks-on-aws.md
- add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md

# Citations

1. [manual-tracing-databricks-on-aws.md](/references/manual-tracing-databricks-on-aws-15119927.md)
2. [add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md](/references/add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws-91d388aa.md)
