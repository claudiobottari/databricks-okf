---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5c596ec767b767d10ee6cd33b27e723fb86b8c1a81194646b201f70e0fd46145
  pageDirectory: concepts
  sources:
    - debug-and-analyze-your-app-with-tracing-databricks-on-aws.md
    - trace-concepts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - opentelemetry-compatibility
    - OpenTelemetry (OTel)
  citations:
    - file: debug-and-analyze-your-app-with-tracing-databricks-on-aws.md
    - file: trace-concepts-databricks-on-aws.md
title: OpenTelemetry Compatibility
description: MLflow Tracing's compatibility with OpenTelemetry, an industry-standard observability specification, enabling export of trace data to existing observability stacks.
tags:
  - observability
  - opentelemetry
  - integration
timestamp: "2026-06-18T11:43:07.847Z"
---

# OpenTelemetry Compatibility

**OpenTelemetry Compatibility** refers to [MLflow Tracing](/concepts/mlflow-tracing.md)'s ability to interoperate with the [OpenTelemetry](https://opentelemetry.io/) industry-standard observability specification, enabling trace data to be exported to existing observability stacks and consumed by OpenTelemetry-compatible tools. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

## Overview

[MLflow Tracing](/concepts/mlflow-tracing.md) is compatible with OpenTelemetry specifications, a widely adopted industry standard for observability. This compatibility allows traces to remain interoperable with other OpenTelemetry-compatible observability tools, while MLflow extends the OpenTelemetry model with GenAI-specific structures and attributes. ^[trace-concepts-databricks-on-aws.md]

The key benefit of OpenTelemetry compatibility is that you can export your trace data to various services in your existing observability stack. This enables teams to leverage their established monitoring infrastructure while gaining the GenAI-specific insights that [MLflow Tracing](/concepts/mlflow-tracing.md) provides. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

## Integration Approach

### Exporting Traces

[MLflow Tracing](/concepts/mlflow-tracing.md) allows you to export trace data to services that support the OpenTelemetry protocol. This means you can send traces from your GenAI application to backend systems such as: ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

- OpenTelemetry Collector
- Jaeger
- Zipkin
- Prometheus
- Datadog
- Other OpenTelemetry-compatible backends

For detailed configuration and setup instructions, see the official documentation on [OpenTelemetry Export](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/open-telemetry). ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

### Trace Structure Alignment

MLflow Traces are structured to be compatible with OpenTelemetry specifications. The trace architecture consists of: ^[trace-concepts-databricks-on-aws.md]

| MLflow Component | OpenTelemetry Equivalent | Purpose |
|------------------|------------------------|---------|
| `TraceInfo` | Trace metadata | Lightweight metadata about the trace's origin, status, and execution time |
| `TraceData` | Trace payload | Container of span objects capturing step-by-step execution |
| Span objects | OpenTelemetry spans | Individual operations in the execution flow |

### GenAI-Specific Extensions

While maintaining compatibility with OpenTelemetry, MLflow extends the standard model with GenAI-specific structures and attributes. This means you get: ^[trace-concepts-databricks-on-aws.md]

- Standard OpenTelemetry trace fields for interoperability
- Additional GenAI-specific attributes for LLM messages, tool parameters, retrieved documents, and context
- Seamless integration with both OpenTelemetry tools and MLflow's native tracing UI

## Benefits of OpenTelemetry Compatibility

### Unified Observability

You can instrument your application once using [MLflow Tracing](/concepts/mlflow-tracing.md), and tracing works consistently in both development and production environments. OpenTelemetry compatibility allows you to navigate traces seamlessly within your preferred environment — whether in your IDE, notebook, or production monitoring dashboard — eliminating the need to switch between multiple tools. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

### Performance and Cost Monitoring

OpenTelemetry compatibility enables you to capture and monitor key operational metrics such as latency, cost, and resource utilization at each step of your application's execution. This allows you to: ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

- Track and identify performance bottlenecks within complex pipelines
- Monitor resource utilization to ensure efficient operation
- Optimize cost efficiency by understanding where resources or tokens are consumed
- Identify areas for performance improvement in code or model interactions

### Full Debugging Experience

By capturing the complete request-response cycle and execution flow, you can examine inputs, outputs, and metadata for each intermediate step (for example, retrieval, tool calls, LLM interactions) alongside associated [user feedback](/concepts/multi-dimensional-user-feedback.md) or the results of quality evaluations. This provides: ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

- **In Development**: Detailed visibility into what happens beneath the abstractions of GenAI libraries, helping you precisely identify where issues or unexpected behaviors occur.
- **In Production**: Real-time monitoring and debugging of issues, with traces capturing errors and operational metrics like latency at each step.

## Trace Structure Details

An MLflow Trace comprises two primary objects that align with OpenTelemetry specifications: ^[trace-concepts-databricks-on-aws.md]

### TraceInfo

[`TraceInfo`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.TraceInfo) provides lightweight metadata about the overall trace, compatible with OpenTelemetry trace metadata standards. Key fields include execution time, status, and tags.

### TraceData

[`TraceData`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.TraceData) is a container of span objects that capture:

- Requests and responses
- Latency measurements
- LLM messages and tool parameters
- Retrieved documents and context
- Metadata and attributes

Spans form a hierarchical structure through parent-child connections, creating a tree that represents your application's execution flow — consistent with the OpenTelemetry span model.

## Tags and Context

Tags are mutable key-value pairs attached to traces for organization and filtering. MLflow defines standard tags aligned with observability best practices: ^[trace-concepts-databricks-on-aws.md]

- `mlflow.trace.session`: Session identifier for grouping related traces
- `mlflow.trace.user`: User identifier for tracking per-user interactions
- `mlflow.source.name`: Entry point or script that generated the trace
- `mlflow.source.git.commit`: Git commit hash of the source code (if applicable)
- `mlflow.source.type`: Source type (`PROJECT`, `NOTEBOOK`, etc.)

You can also add custom tags for your specific needs. See [Add Context to Traces](/concepts/best-practices-for-adding-context-to-mlflow-traces.md) and Attach Custom Tags and Metadata.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing system that provides OpenTelemetry compatibility
- Span Concepts — Individual operations in the trace execution flow
- Trace Architecture — The structure of traces in MLflow
- OpenTelemetry Collector — A vendor-agnostic collector for trace data
- [GenAI Application Monitoring](/concepts/mlflow-genai-production-monitoring.md) — Monitoring GenAI applications with traces
- [User Feedback Collection](/concepts/end-user-feedback-collection-via-sdk.md) — Correlating user feedback with traces

## Sources

- debug-and-analyze-your-app-with-tracing-databricks-on-aws.md
- trace-concepts-databricks-on-aws.md

# Citations

1. [debug-and-analyze-your-app-with-tracing-databricks-on-aws.md](/references/debug-and-analyze-your-app-with-tracing-databricks-on-aws-d9c92247.md)
2. [trace-concepts-databricks-on-aws.md](/references/trace-concepts-databricks-on-aws-9723e725.md)
