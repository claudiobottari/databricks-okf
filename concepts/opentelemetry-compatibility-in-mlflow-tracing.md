---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c38e2de743e72bd5aa18bad5c68826d97e0fc99c91334edb74a8c6a25a23d22f
  pageDirectory: concepts
  sources:
    - debug-and-analyze-your-app-with-tracing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opentelemetry-compatibility-in-mlflow-tracing
    - OCIMT
  citations:
    - file: debug-and-analyze-your-app-with-tracing-databricks-on-aws.md
title: OpenTelemetry Compatibility in MLflow Tracing
description: MLflow Tracing's integration with the OpenTelemetry standard, allowing export of trace data to existing observability stacks.
tags:
  - observability
  - opentelemetry
  - integration
timestamp: "2026-06-19T18:16:19.435Z"
---

## OpenTelemetry Compatibility in [MLflow Tracing](/concepts/mlflow-tracing.md)

**OpenTelemetry Compatibility in MLflow Tracing** refers to the ability of [MLflow Tracing](/concepts/mlflow-tracing.md) to integrate with the **OpenTelemetry** industry-standard observability specification. This compatibility allows teams to export trace data collected by MLflow to a variety of external services within their existing observability stack. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

### Overview

[MLflow Tracing](/concepts/mlflow-tracing.md) captures the complete request-response cycle and execution flow of applications, providing visibility into intermediate steps such as retrieval, tool calls, and LLM interactions. To extend this capability beyond Databricks' native tooling, [MLflow Tracing](/concepts/mlflow-tracing.md) is compatible with OpenTelemetry, allowing organizations to route trace data to their preferred monitoring and analysis platforms. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

### Capabilities

This OpenTelemetry integration enables teams to:

- **Export trace data** to various services in your existing observability stack. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]
- **Maintain a unified observability strategy** by using the same instrumentation and data format already supported by their organization's infrastructure. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]
- **Monitor performance and optimize costs** by combining MLflow's captured metrics (latency, cost, resource utilization) with the analytics and alerting capabilities of external observability services. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

### Use Cases

Because [MLflow Tracing](/concepts/mlflow-tracing.md) instruments your application once and works consistently in both development and production, OpenTelemetry export allows you to:

- **In Production**: Send real-time trace data to your existing monitoring infrastructure for dashboards, alerting, and long-term storage. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]
- **Across Environments**: Navigate traces seamlessly within your preferred environment — whether your IDE, notebook, or production monitoring dashboard — without switching between multiple tools. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

### Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The core tracing system that captures execution flows and operational metrics.
- OpenTelemetry — The industry-standard observability specification MLflow integrates with.
- [OpenTelemetry Export](/concepts/mlflow-opentelemetry-metrics-export.md) — The detailed documentation on configuring exports.
- [Genie Code](/concepts/genie-code.md) — A natural language interface for analyzing traces, complementary to external observability tools.
- Performance Monitoring for GenAI — Tracking latency, cost, and resource utilization captured by traces.

### Sources

- debug-and-analyze-your-app-with-tracing-databricks-on-aws.md

# Citations

1. [debug-and-analyze-your-app-with-tracing-databricks-on-aws.md](/references/debug-and-analyze-your-app-with-tracing-databricks-on-aws-d9c92247.md)
