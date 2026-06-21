---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ed8cb4a678f232ff02ddc70c731910954fb3d4dbeca0a1adc772c6adb2fcd9e7
  pageDirectory: concepts
  sources:
    - mlflow-tracing-genai-observability-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - end-to-end-trace-recording
    - ETR
  citations:
    - file: mlflow-tracing-genai-observability-databricks-on-aws.md
title: End-to-End Trace Recording
description: The practice of capturing complete execution flows including inputs, outputs, intermediate steps, and metadata for GenAI applications.
tags:
  - tracing
  - debugging
  - observability
  - metadata
timestamp: "2026-06-19T19:40:54.821Z"
---

---
title: End-to-End Trace Recording
summary: [MLflow Tracing](/concepts/mlflow-tracing.md) provides end-to-end observability for GenAI applications by recording inputs, outputs, intermediate steps, and metadata.
sources:
  - mlflow-tracing-genai-observability-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:16:22.176Z"
updatedAt: "2026-06-18T08:16:22.176Z"
tags:
  - mlflow
  - tracing
  - observability
  - genai
aliases:
  - end-to-end-trace-recording
  - E2ETR
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# End-to-End Trace Recording

**End-to-End Trace Recording** is a capability of [MLflow Tracing](/concepts/mlflow-tracing.md) that provides full observability into [GenAI](/concepts/mlflow-genai-evaluate-api.md) applications, including complex [agent-based systems](/concepts/agent-based-system-observability.md). It captures the complete execution path of a request — from initial input through all intermediate steps to final output — along with associated metadata. This enables developers to understand, debug, monitor, and evaluate application behavior at a granular level. ^[mlflow-tracing-genai-observability-databricks-on-aws.md]

## Key Capabilities

End-to-End Trace Recording records the following data for each request:

- **Inputs** – the prompt or data provided to the application.
- **Outputs** – the final response generated.
- **Intermediate steps** – internal calls, tool invocations, or sub‑agent decisions.
- **Metadata** – timing, resource usage, model names, and other contextual attributes.

^[mlflow-tracing-genai-observability-databricks-on-aws.md]

## Use Cases

Tracing enables several practical workflows:

- **Debugging** – Identify where and why a request fails or produces unexpected results.
- **Performance monitoring** – Measure latency and resource consumption across steps.
- **Cost optimization** – Track token usage and invocation patterns.
- **Production monitoring** – Continuously observe deployed applications.
- **Quality evaluation** – Assess and improve application outputs based on trace data.
- **Auditability and compliance** – Maintain a detailed record of application decisions for review.

Additionally, tracing integrates with many popular third‑party frameworks, allowing teams to use familiar tools for analysis. Users can also leverage [Genie Code](/concepts/genie-code.md) to analyze, debug, and explore trace data using natural language queries. ^[mlflow-tracing-genai-observability-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The overarching feature that provides trace recording.
- [GenAI Observability](/concepts/genai-observability.md) – Broader monitoring and analysis of generative AI applications.
- Agent-based Systems – Complex workflows that benefit from detailed tracing.
- [Trace Data](/concepts/tracedata.md) – The collected records of application execution.
- [Genie Code](/concepts/genie-code.md) – Natural‑language interface for exploring traces.

## Sources

- mlflow-tracing-genai-observability-databricks-on-aws.md

# Citations

1. [mlflow-tracing-genai-observability-databricks-on-aws.md](/references/mlflow-tracing-genai-observability-databricks-on-aws-9bbb7d89.md)
