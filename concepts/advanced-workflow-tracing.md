---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cf5703093c2fb1da3dfa0ff994d7910fbb3b31aae7c6992f48fd1ccd5a76d63d
  pageDirectory: concepts
  sources:
    - manual-tracing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - advanced-workflow-tracing
    - AWT
  citations:
    - file: manual-tracing-databricks-on-aws.md
title: Advanced Workflow Tracing
description: Manual tracing support for complex production scenarios including multi-threaded operations, async workflows, streaming responses with custom aggregation, and complex nested operations.
tags:
  - observability
  - tracing
  - workflows
timestamp: "2026-06-19T19:29:49.506Z"
---

# Advanced Workflow Tracing

**Advanced Workflow Tracing** refers to the manual instrumentation of GenAI applications using the [MLflow Tracing API](/concepts/mlflow-tracing.md), giving developers complete control over which code paths are traced, how spans are structured, and what metadata is captured. This approach is contrasted with [Automatic Tracing](/concepts/automatic-tracing.md), which provides instant observability for supported frameworks but limited customization. ^[manual-tracing-databricks-on-aws.md]

## When to Use Advanced Workflow Tracing

Manual tracing is the right choice when you need:

- **Fine-grained control over trace structure** — Define exactly which parts of your code to trace, create custom hierarchies of spans, and control span boundaries and relationships. ^[manual-tracing-databricks-on-aws.md]
- **Custom framework instrumentation** — Instrument proprietary or internal frameworks, add tracing to custom LLM wrappers, or support new libraries before official integration. ^[manual-tracing-databricks-on-aws.md]
- **Advanced workflow scenarios** — Multi-threaded or async operations, streaming responses with custom aggregation, complex nested operations, and custom trace metadata and attributes. ^[manual-tracing-databricks-on-aws.md]

## API Options for Manual Tracing

Choose the right manual tracing approach for your needs. The available APIs include `start_span`, the `@trace` decorator, and the MlflowClient for low-level trace management. ^[manual-tracing-databricks-on-aws.md]

For a complete description of each option, see the Manual Tracing API Reference.

## Related Concepts

- [Automatic Tracing](/concepts/automatic-tracing.md)
- [MLflow Tracing API](/concepts/mlflow-tracing.md)
- Span
- [Trace](/concepts/traces.md)
- GenAI Application Instrumentation

## Sources

- manual-tracing-databricks-on-aws.md

# Citations

1. [manual-tracing-databricks-on-aws.md](/references/manual-tracing-databricks-on-aws-15119927.md)
