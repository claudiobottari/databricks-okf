---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 93996c8dc22b8d74c0d5c902c8a9c509d997ec8a90197bff5da2987324cebad3
  pageDirectory: concepts
  sources:
    - debug-and-analyze-your-app-with-tracing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - performance-and-cost-monitoring-via-traces
    - Cost Monitoring via Traces and Performance
    - PACMVT
    - performance-and-cost-optimization-via-traces
    - Cost Optimization via Traces and Performance
    - PACOVT
    - performance-and-cost-optimization-via-tracing
    - Cost Optimization via Tracing and Performance
  citations:
    - file: debug-and-analyze-your-app-with-tracing-databricks-on-aws.md
title: Performance and Cost Monitoring via Traces
description: Using MLflow Tracing to capture operational metrics like latency, cost, and resource utilization at each step of GenAI application execution to identify bottlenecks and optimize efficiency.
tags:
  - observability
  - performance-monitoring
  - cost-optimization
timestamp: "2026-06-19T18:16:09.004Z"
---

## Performance and Cost Monitoring via Traces

**Performance and Cost Monitoring via Traces** refers to the use of [MLflow Tracing](/concepts/mlflow-tracing.md) to capture and analyze operational metrics — such as latency, cost, and resource utilization — at each step of a GenAI application's execution. This capability enables teams to identify performance bottlenecks, optimize resource consumption, and manage cost efficiency within complex pipelines. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

### Key Capabilities

[MLflow Tracing](/concepts/mlflow-tracing.md) captures operational metrics alongside the execution flow of a request. These metrics allow developers to:

- Track latency at each intermediate step (e.g., retrieval, tool calls, LLM interactions) to pinpoint bottlenecks.
- Monitor resource utilization (e.g., GPU memory, CPU) to ensure efficient operation.
- Understand where tokens or compute resources are consumed in order to optimize cost efficiency.
- Identify areas for performance improvement in code or model interactions. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

This trace-level observability works consistently in both development and production environments, providing a unified view without switching between tools. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

### Integration with OpenTelemetry

[MLflow Tracing](/concepts/mlflow-tracing.md) is compatible with OpenTelemetry, an industry-standard observability specification. This compatibility allows trace data to be exported to various monitoring services in an existing observability stack, enabling centralized performance and cost dashboards. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

### Analyzing Traces with Genie Code

[Genie Code](/concepts/genie-code.md) provides a natural language interface for exploring and debugging traces. Instead of writing custom queries, users can ask questions such as:

- "Are there any error traces in this experiment?"
- "What's the P95 latency for my traces?"

Genie Code has read access to traces, sessions, evaluation runs, scorers, datasets, and labeling sessions, enabling root-cause analysis from a single conversational interface. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

### Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [OpenTelemetry Export](/concepts/mlflow-opentelemetry-metrics-export.md)
- [Genie Code for Agent Observability](/concepts/genie-code-for-agent-observability.md)
- [User Feedback on Traces](/concepts/user-feedback-collection-in-mlflow-tracing.md)
- Quality Evaluation via Traces

### Sources

- debug-and-analyze-your-app-with-tracing-databricks-on-aws.md

# Citations

1. [debug-and-analyze-your-app-with-tracing-databricks-on-aws.md](/references/debug-and-analyze-your-app-with-tracing-databricks-on-aws-d9c92247.md)
