---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea182413f07e6b78fe9cf28521d2f64c63cd1d1ff390c1829eab3001c4b41569
  pageDirectory: concepts
  sources:
    - debug-and-analyze-your-app-with-tracing-databricks-on-aws.md
  confidence: 0.92
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opentelemetry-export-for-mlflow-traces
    - OEFMT
    - OpenTelemetry OTLP Exporter
  citations:
    - file: debug-and-analyze-your-app-with-tracing-databricks-on-aws.md
title: OpenTelemetry Export for MLflow Traces
description: Compatibility between MLflow Tracing and the OpenTelemetry industry-standard observability specification, allowing trace data to be exported to existing observability stacks.
tags:
  - observability
  - integration
  - opentelemetry
  - mlflow
timestamp: "2026-06-19T14:55:29.488Z"
---

# OpenTelemetry Export for MLflow Traces

**OpenTelemetry Export for MLflow Traces** is a feature that allows trace data captured by [MLflow Tracing](/concepts/mlflow-tracing.md) to be exported to external observability backends using the OpenTelemetry specification. This enables teams to integrate MLflow traces into their existing observability stack without switching tools or duplicating instrumentation. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

## Overview

[MLflow Tracing](/concepts/mlflow-tracing.md) natively supports OpenTelemetry, an industry-standard observability specification. By leveraging this compatibility, you can direct your trace data to various services such as Datadog, Prometheus, Jaeger, or any other OpenTelemetry-compatible collector. This allows for unified monitoring across both application code and ML workflows. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

## Benefits

- **Export to existing observability stack** – Send traces to your preferred backend without replacing existing instrumentation.
- **Consistent instrumentation** – Author trace logic once using OpenTelemetry APIs; [MLflow Tracing](/concepts/mlflow-tracing.md) automatically integrates with them.
- **Performance and cost analysis** – Combined with MLflow Tracing’s capture of latency, cost, and resource utilization, OpenTelemetry export enables centralized dashboards for debugging and optimization.

For detailed configuration steps, supported exporters, and examples, refer to the official documentation on [OpenTelemetry Export](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/open-telemetry). ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The tracing subsystem that captures request-response cycles and execution flows.
- OpenTelemetry – The open standard for observability data (traces, metrics, logs).
- Debug and analyze your app with tracing – Overview of [MLflow Tracing](/concepts/mlflow-tracing.md) capabilities.
- [Observability Stack](/concepts/genai-observability.md) – Tools and platforms for monitoring distributed systems.
- [Genie Code for Agent Observability](/concepts/genie-code-for-agent-observability.md) – Natural‑language trace analysis using [MLflow Tracing](/concepts/mlflow-tracing.md) data.

## Sources

- debug-and-analyze-your-app-with-tracing-databricks-on-aws.md

# Citations

1. [debug-and-analyze-your-app-with-tracing-databricks-on-aws.md](/references/debug-and-analyze-your-app-with-tracing-databricks-on-aws-d9c92247.md)
