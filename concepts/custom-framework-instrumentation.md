---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1f99133a9675708d3b34e010771d6a7c3ddedc85812929436c0a3b81d7391742
  pageDirectory: concepts
  sources:
    - manual-tracing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-framework-instrumentation
    - CFI
  citations:
    - file: manual-tracing-databricks-on-aws.md
title: Custom Framework Instrumentation
description: The capability to add tracing to proprietary or internal frameworks, custom LLM wrappers, and new libraries that lack official MLflow integration.
tags:
  - observability
  - instrumentation
  - mlflow
timestamp: "2026-06-19T19:29:54.467Z"
---

## Custom Framework Instrumentation

**Custom Framework Instrumentation** is a use case of [Manual Tracing](/concepts/manual-tracing.md) that enables developers to add observability to GenAI applications using proprietary internal frameworks, custom LLM wrappers, or libraries that do not yet have official integration with MLflow's [Automatic Tracing](/concepts/automatic-tracing.md). ^[manual-tracing-databricks-on-aws.md]

### When to Use Custom Framework Instrumentation

Manual tracing provides the flexibility needed for custom framework instrumentation. It is the right choice when you need to:

- **Instrument proprietary or internal frameworks** – Add tracing to frameworks that are developed in-house and are not covered by MLflow’s built-in auto-instrumentation. ^[manual-tracing-databricks-on-aws.md]
- **Add tracing to custom LLM wrappers** – If you wrap an LLM API or model with custom logic (e.g., caching, retries, prompt templates), manual tracing lets you capture those custom calls as spans. ^[manual-tracing-databricks-on-aws.md]
- **Support new libraries before official integration** – Use manual tracing to instrument a newly released library or an open-source package that does not yet have an MLflow auto-tracing integration. ^[manual-tracing-databricks-on-aws.md]

### Relation to Manual Tracing

Custom framework instrumentation is one of the key scenarios where manual tracing is preferred over automatic tracing. While automatic tracing provides instant observability for supported frameworks, manual tracing gives complete control over which parts of the code are traced, the structure and hierarchy of spans, and what metadata is recorded. This control is essential for production-ready applications that require detailed monitoring and debugging. ^[manual-tracing-databricks-on-aws.md]

### Related Concepts

- [Manual Tracing](/concepts/manual-tracing.md) – The broader technique that includes custom framework instrumentation.
- [Automatic Tracing](/concepts/automatic-tracing.md) – The alternative approach for supported frameworks.
- [MLflow](/concepts/mlflow.md) – The platform that provides the tracing APIs.
- [Trace](/concepts/traces.md) – The overall record of an application execution path.
- Span – A single unit of work within a trace.
- LLM wrappers – Custom code that adds functionality to LLM API calls.

### Sources

- manual-tracing-databricks-on-aws.md

# Citations

1. [manual-tracing-databricks-on-aws.md](/references/manual-tracing-databricks-on-aws-15119927.md)
