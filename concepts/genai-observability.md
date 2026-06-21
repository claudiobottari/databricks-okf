---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cb0b45980dc5254192c646a5a73e2d13c3ac0c28c26cab9849a1ea814cf95b14
  pageDirectory: concepts
  sources:
    - mlflow-tracing-genai-observability-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genai-observability
    - Agent Observability
    - GenAI application observability
    - LLM Observability
    - Observability Stack
    - Span (observability)
  citations:
    - file: mlflow-tracing-genai-observability-databricks-on-aws.md
title: GenAI Observability
description: The practice of monitoring, debugging, and optimizing generative AI applications through comprehensive trace data and metadata analysis.
tags:
  - observability
  - genai
  - monitoring
  - mlops
timestamp: "2026-06-19T19:40:43.388Z"
---

## GenAI Observability

**GenAI Observability** refers to the practice of gaining end-to-end visibility into the behavior, performance, and quality of generative AI applications. This includes recording inputs, outputs, intermediate steps, and metadata to debug issues, monitor production systems, optimize cost, and ensure compliance. ^[mlflow-tracing-genai-observability-databricks-on-aws.md]

### [MLflow Tracing](/concepts/mlflow-tracing.md)

On Databricks, [MLflow Tracing](/concepts/mlflow-tracing.md) is the primary feature that delivers GenAI observability. It provides end-to-end observability for [GenAI](/concepts/mlflow-genai-evaluate-api.md) applications, including complex [agent-based systems](/concepts/agent-based-system-observability.md). Tracing records every step of an application’s execution, enabling developers to understand how their app behaves in detail. ^[mlflow-tracing-genai-observability-databricks-on-aws.md]

### Key Capabilities

[MLflow Tracing](/concepts/mlflow-tracing.md) supports the following use cases for GenAI observability:

- **Debug and understand your application** – Inspect traces to identify errors, unexpected outputs, or logical flaws in agent workflows. ^[mlflow-tracing-genai-observability-databricks-on-aws.md]
- **Monitor performance and optimize cost** – Track latency, token usage, and cost metrics per trace to identify bottlenecks and reduce expenses. ^[mlflow-tracing-genai-observability-databricks-on-aws.md]
- **Monitor production applications** – Continuously observe deployed GenAI apps to detect regressions, anomalies, or quality degradation. ^[mlflow-tracing-genai-observability-databricks-on-aws.md]
- **Evaluate and enhance application quality** – Use trace data to measure response quality, accuracy, and adherence to guidelines. ^[mlflow-tracing-genai-observability-databricks-on-aws.md]
- **Ensure auditability and compliance** – Retain full execution records for regulatory review, security audits, or internal governance. ^[mlflow-tracing-genai-observability-databricks-on-aws.md]
- **Integrate with third-party frameworks** – Connect tracing to popular frameworks (e.g., LangChain, LlamaIndex) for seamless observability. ^[mlflow-tracing-genai-observability-databricks-on-aws.md]
- **Analyze traces with natural language** – Use [Genie Code](/concepts/genie-code.md) to ask questions about trace data, debug errors, and explore evaluation results using plain English. ^[mlflow-tracing-genai-observability-databricks-on-aws.md]

### Getting Started

To begin with GenAI observability on Databricks, you can:

- Follow the [10-minute tracing demo](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/tracing/tracing-notebook) to set up your first trace. ^[mlflow-tracing-genai-observability-databricks-on-aws.md]
- [Instrument your app](/concepts/mlflow-instrumentation-guidance.md) by choosing between automatic or manual tracing approaches. ^[mlflow-tracing-genai-observability-databricks-on-aws.md]
- Use Genie Code for agent observability and evaluation to explore and analyze trace data conversationally. ^[mlflow-tracing-genai-observability-databricks-on-aws.md]

### Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [GenAI](/concepts/mlflow-genai-evaluate-api.md)
- Agent-based systems
- Observability
- [Genie Code](/concepts/genie-code.md)
- [Production Monitoring](/concepts/production-monitoring.md)
- Cost Optimization
- Compliance

### Sources

- mlflow-tracing-genai-observability-databricks-on-aws.md

# Citations

1. [mlflow-tracing-genai-observability-databricks-on-aws.md](/references/mlflow-tracing-genai-observability-databricks-on-aws-9bbb7d89.md)
