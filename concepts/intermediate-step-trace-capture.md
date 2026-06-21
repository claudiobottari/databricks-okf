---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e4f7de511fc25e750d2239f178df3cf125b04c5b189c2150ffc75a481d58ddd7
  pageDirectory: concepts
  sources:
    - debug-and-analyze-your-app-with-tracing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - intermediate-step-trace-capture
    - ISTC
  citations:
    - file: debug-and-analyze-your-app-with-tracing-databricks-on-aws.md
title: Intermediate Step Trace Capture
description: The practice of examining inputs, outputs, and metadata for each intermediate step in a GenAI pipeline (retrieval, tool calls, LLM interactions) for debugging and analysis.
tags:
  - observability
  - debugging
  - genai
timestamp: "2026-06-19T18:16:26.761Z"
---

# Intermediate Step Trace Capture

**Intermediate Step Trace Capture** is a capability of [MLflow Tracing](/concepts/mlflow-tracing.md) that records the inputs, outputs, and metadata for each individual step within an application's execution flow, including retrievals, tool calls, and LLM interactions. This fine-grained capture enables detailed debugging and analysis of complex [GenAI](/concepts/mlflow-genai-evaluate-api.md) applications across development and production environments. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

## Overview

[MLflow Tracing](/concepts/mlflow-tracing.md) captures the complete request-response cycle of an application, tracking both input/output data and the full execution flow. By recording intermediate steps, developers can visualize and understand their application's logic and decision-making process at a granular level. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

The tracing system captures metadata for each intermediate step, including:
- Inputs and outputs for each operation
- Execution timing and latency
- Error information when issues occur
- Operational metrics like resource utilization

^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

## Use Cases

### Development Debugging

In development environments, intermediate step trace capture provides detailed visibility into what happens beneath the abstractions of GenAI libraries. This helps developers precisely identify where issues or unexpected behaviors occur within complex pipelines. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

### Production Monitoring

In production, traces capture errors and operational metrics like latency at each step, aiding in quick diagnostics and real-time monitoring. This enables teams to debug issues as they occur in live environments. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

## Unified Development and Production Experience

[MLflow Tracing](/concepts/mlflow-tracing.md) offers a unified experience between development and production: once an application is instrumented, tracing works consistently in both environments. This allows developers to navigate traces seamlessly within their preferred environment—whether in an IDE, notebook, or production monitoring dashboard—without needing to switch between multiple tools or search through overwhelming logs. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

## Performance and Cost Optimization

By capturing operational metrics at each intermediate step, tracing enables teams to:

- Track and identify performance bottlenecks within complex pipelines
- Monitor resource utilization to ensure efficient operation
- Optimize cost efficiency by understanding where resources or tokens are consumed
- Identify areas for performance improvement in code or model interactions

^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

## Integration with OpenTelemetry

Intermediate step trace capture is compatible with OpenTelemetry, an industry-standard observability specification. This compatibility allows trace data to be exported to various services in an existing observability stack. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

## Analysis with Genie Code

[Genie Code](/concepts/genie-code.md) provides a natural language interface for exploring and debugging captured traces. Users can ask questions such as "Are there any error traces in this experiment?" or "What's the P95 latency for my traces?" to analyze the captured intermediate step data without writing queries or navigating multiple UI pages. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

Genie Code has read access to traces, sessions, evaluation runs, scorers, datasets, labeling sessions, and related data, enabling users to go from a high-level question to root cause analysis in a single conversation. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing framework that provides intermediate step capture capabilities
- [Trace Export](/concepts/mlflow-trace-data-export.md) — Exporting trace data to external observability systems
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) — Evaluating agent performance using trace data
- [User Feedback Collection](/concepts/end-user-feedback-collection-via-sdk.md) — Correlating user feedback with captured traces

## Sources

- debug-and-analyze-your-app-with-tracing-databricks-on-aws.md

# Citations

1. [debug-and-analyze-your-app-with-tracing-databricks-on-aws.md](/references/debug-and-analyze-your-app-with-tracing-databricks-on-aws-d9c92247.md)
