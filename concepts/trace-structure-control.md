---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 59a3c0da01e473c0128b7fcfe43bf810b14c16b711c026973dd98d676336acc8
  pageDirectory: concepts
  sources:
    - manual-tracing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-structure-control
    - TSC
  citations:
    - file: manual-tracing-databricks-on-aws.md
title: Trace Structure Control
description: The ability to define exactly which code segments are traced, create custom span hierarchies, and control span boundaries and relationships in GenAI applications.
tags:
  - observability
  - tracing
  - instrumentation
timestamp: "2026-06-19T19:29:42.417Z"
---

# Trace Structure Control

**Trace Structure Control** refers to the ability to define the exact hierarchy, boundaries, and relationships between spans when manually instrumenting GenAI applications with [MLflow Tracing](/concepts/mlflow-tracing.md). This capability gives developers fine-grained control over the structure of traces, enabling detailed monitoring and debugging of complex production applications. ^[manual-tracing-databricks-on-aws.md]

## Overview

When using manual tracing, developers can define exactly which parts of their code generate spans, create custom hierarchies of spans, and control span boundaries and relationships. This is distinct from automatic tracing, which provides instant observability for supported frameworks but does not offer the same level of structural control. ^[manual-tracing-databricks-on-aws.md]

## When to Use Trace Structure Control

Fine-grained control over trace structure is essential in several scenarios: ^[manual-tracing-databricks-on-aws.md]

- **Defining trace boundaries**: Specify exactly which parts of your code to trace, rather than relying on automatic instrumentation.
- **Creating custom span hierarchies**: Build nested span structures that reflect your application's logical flow.
- **Controlling span relationships**: Define how spans relate to one another within a trace.

## Advanced Use Cases

Trace structure control is particularly valuable for advanced workflow scenarios that automatic tracing cannot adequately capture: ^[manual-tracing-databricks-on-aws.md]

- **Multi-threaded or async operations**: Manually create and manage spans across concurrent execution contexts.
- **Streaming responses with custom aggregation**: Structure traces around streaming data processing where span boundaries must align with logical aggregation points.
- **Complex nested operations**: Represent deeply nested function calls or pipeline stages with appropriate parent-child span relationships.
- **Custom trace metadata and attributes**: Attach application-specific information to spans at precise points in the trace hierarchy.

## Custom Framework Instrumentation

Manual tracing is also the recommended approach when instrumenting proprietary or internal frameworks that lack automatic support: ^[manual-tracing-databricks-on-aws.md]

- Instrument custom LLM wrappers with appropriate span structures.
- Add tracing to new libraries before official integration is available.
- Decorate internal framework components with consistent span naming and hierarchy.

## Comparison with Automatic Tracing

Automatic tracing provides instant observability for supported frameworks without requiring code changes. Manual tracing with structure control, by contrast, requires explicit instrumentation but offers complete flexibility. Choose manual tracing when your application requires detailed monitoring and debugging capabilities that automatic instrumentation cannot provide. ^[manual-tracing-databricks-on-aws.md]

## Related Concepts

- [Automatic Tracing](/concepts/automatic-tracing.md) — Instant observability for supported frameworks without code changes
- [Span Hierarchy](/concepts/trace-span-hierarchy.md) — The parent-child structure of spans within a trace
- Span Boundaries — The start and end points that define individual spans
- Application Instrumentation — The broader practice of adding observability to applications
- [GenAI Application Monitoring](/concepts/mlflow-genai-production-monitoring.md) — Monitoring and debugging generative AI applications

## Sources

- manual-tracing-databricks-on-aws.md

# Citations

1. [manual-tracing-databricks-on-aws.md](/references/manual-tracing-databricks-on-aws-15119927.md)
