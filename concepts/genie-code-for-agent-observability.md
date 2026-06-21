---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c86d519fc926691479415e7266c86876e24675f9992b6c6912b7c3209be7dd12
  pageDirectory: concepts
  sources:
    - mlflow-tracing-genai-observability-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genie-code-for-agent-observability
    - GCFAO
  citations:
    - file: debug-and-analyze-your-app-with-tracing-databricks-on-aws.md
    - file: mlflow-tracing-genai-observability-databricks-on-aws.md
title: Genie Code for Agent Observability
description: A natural language interface for analyzing traces, debugging errors, and exploring evaluation data in MLflow Tracing.
tags:
  - natural-language
  - debugging
  - observability
  - genai
timestamp: "2026-06-19T19:40:39.886Z"
---

Here is the wiki page for "Genie Code for Agent Observability", written based solely on the provided source material.

---

## Genie Code for Agent Observability

**Genie Code for Agent Observability** is a natural language interface within [MLflow Tracing](/concepts/mlflow-tracing.md) that enables users to explore, debug, and analyze the behavior of [GenAI](/concepts/mlflow-genai-evaluate-api.md) applications and agents. Instead of writing complex queries or navigating multiple UI screens, users can ask high-level questions in plain English and receive immediate answers about application performance, errors, and evaluation results. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md, mlflow-tracing-genai-observability-databricks-on-aws.md]

### Capabilities

Genie Code has read access to a broad set of [MLflow](/concepts/mlflow.md) data, including traces, sessions, evaluation runs, scorers, datasets, and labeling sessions. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md] This allows users to progress from a high-level question — such as "What's the P95 latency for my traces?" — to a detailed root cause analysis within a single conversation. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

The interface is particularly useful for:

- **Error identification**: Asking questions like "Are there any error traces in this experiment?" to quickly surface failures. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]
- **Performance analysis**: Querying latency percentiles, cost metrics, and resource utilization at each step of an application's execution. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

### Role in [MLflow Tracing](/concepts/mlflow-tracing.md)

[MLflow Tracing](/concepts/mlflow-tracing.md) provides end-to-end observability for GenAI applications by capturing the complete request-response cycle, intermediate steps (e.g., retrieval, tool calls, LLM interactions), and metadata. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md, mlflow-tracing-genai-observability-databricks-on-aws.md] Genie Code serves as the conversational access layer on top of this trace data, making it possible to explore traces using natural language and to use the same interface across development and production environments. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

### Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The underlying observability system that records trace data.
- GenAI applications — The type of applications that Genie Code is designed to observe.
- [Agent evaluation](/concepts/mlflow-agent-evaluation.md) — Evaluation workflows whose results are accessible via Genie Code.
- User feedback collection — Feedback data that Genie Code can read alongside traces.
- Quality evaluations — Evaluation results that can be queried within a Genie Code conversation.

### Sources

- debug-and-analyze-your-app-with-tracing-databricks-on-aws.md
- mlflow-tracing-genai-observability-databricks-on-aws.md

# Citations

1. [debug-and-analyze-your-app-with-tracing-databricks-on-aws.md](/references/debug-and-analyze-your-app-with-tracing-databricks-on-aws-d9c92247.md)
2. [mlflow-tracing-genai-observability-databricks-on-aws.md](/references/mlflow-tracing-genai-observability-databricks-on-aws-9bbb7d89.md)
