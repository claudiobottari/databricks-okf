---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 792f55c32b58c141d99734c812d3fe5ad5a4295861b219f5e1ba4bfde68be4b5
  pageDirectory: concepts
  sources:
    - tracing-groq-databricks-on-aws.md
    - tracing-smolagents-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing
    - MLflow Tracing 101
    - MLflow Tracing API
    - MLflow Tracing SDK
    - Span (MLflow Tracing)
    - Span (MLflow)
    - Tracing
    - span tracing
    - tracing
  citations:
    - file: mlflow-tracing-genai-observability-databricks-on-aws.md
    - file: debug-and-analyze-your-app-with-tracing-databricks-on-aws.md
    - file: trace-concepts-databricks-on-aws.md
    - file: add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
    - file: get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md
    - file: get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md
    - file: tracing-agno-databricks-on-aws.md
    - file: tracing-semantic-kernel-databricks-on-aws.md
    - file: tracing-openai-agents-databricks-on-aws.md
    - file: tracing-groq-databricks-on-aws.md
    - file: tracing-smolagents-databricks-on-aws.md
    - file: evaluate-and-monitor-ai-agents-databricks-on-aws.md
title: MLflow Tracing
description: Framework for recording and analyzing trace data from LLM and AI application calls
tags:
  - mlflow
  - tracing
  - observability
timestamp: "2026-06-19T23:12:12.870Z"
---

```yaml
---
title: [[mlflow|MLflow]] Tracing
summary: Automatic instrumentation of GenAI applications using automatic and [[manual-tracing|Manual Tracing]] approaches to capture execution [[traces|Traces]], spans, and metadata for observability.
sources:
  - add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
  - debug-and-analyze-your-app-with-tracing-databricks-on-aws.md
  - evaluate-and-monitor-ai-agents-databricks-on-aws.md
  - get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md
  - get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md
  - mlflow-3-for-genai-databricks-on-aws.md
  - mlflow-on-databricks-databricks-on-aws.md
  - mlflow-tracing-genai-observability-databricks-on-aws.md
  - trace-concepts-databricks-on-aws.md
  - tracing-agno-databricks-on-aws.md
  - tracing-openai-agents-databricks-on-aws.md
  - tracing-semantic-kernel-databricks-on-aws.md
  - tutorial-connect-your-development-environment-to-mlflow-databricks-on-aws.md
  - tracing-groq-databricks-on-aws.md
  - tracing-smolagents-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T13:48:57.059Z"
updatedAt: "2026-06-19T13:48:57.059Z"
tags:
  - [[mlflow|MLflow]]
  - tracing
  - observability
  - genai
  - debugging
aliases:
  - mlflow-tracing
confidence: 0.95
provenanceState: merged
inferredParagraphs: 0
```

# [MLflow](/concepts/mlflow.md) Tracing

**MLflow Tracing** is an observability feature that captures the complete execution flow of requests through GenAI applications. Unlike traditional logging that records isolated events, tracing creates a detailed map of how data flows through systems and records every operation along the way. It provides end-to-end observability for GenAI applications, including complex agent-based systems, by recording inputs, outputs, intermediate steps, and metadata. ^[mlflow-tracing-genai-observability-databricks-on-aws.md] ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

[MLflow](/concepts/mlflow.md) Tracing provides the data foundation required for evaluation and monitoring. It enables developers to debug and understand application behavior, monitor performance and optimize costs, evaluate and enhance application quality, ensure auditability and compliance, integrate with many popular third‑party frameworks, and use natural language with [Genie Code](/concepts/genie-code.md) to analyze and explore trace data. ^[mlflow-tracing-genai-observability-databricks-on-aws.md]

Tracing supports the full development lifecycle — development, testing, and production — with a unified experience. The same instrumentation works consistently across environments, allowing navigation between the IDE, notebook, and [Production Monitoring](/concepts/production-monitoring.md) dashboard without switching tools or searching through logs. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

## Trace Structure

A trace in [MLflow](/concepts/mlflow.md) comprises two primary objects: *`Trace.info`* (of type `TraceInfo`) and *`Trace.data`* (of type `TraceData`). ^[trace-concepts-databricks-on-aws.md]

- **`TraceInfo`** provides lightweight metadata about the trace’s origin, status, and execution time. It also holds tags — user‑, session‑, and developer‑provided key‑value pairs used for searching or filtering [Traces](/concepts/traces.md). ^[trace-concepts-databricks-on-aws.md]
- **`TraceData`** is a container of Span objects that capture the application’s step‑by‑step execution from input to output. Each span records requests and responses, latency measurements, LLM messages and tool parameters, retrieved documents and context, and metadata. Spans form a hierarchical tree structure through parent‑child connections. ^[trace-concepts-databricks-on-aws.md]

[MLflow](/concepts/mlflow.md) [Traces](/concepts/traces.md) are compatible with OpenTelemetry specifications while extending the OpenTelemetry model with GenAI‑specific structures and attributes. ^[trace-concepts-databricks-on-aws.md]

### Tags

Tags are mutable key‑value pairs attached to [Traces](/concepts/traces.md). [MLflow](/concepts/mlflow.md) defines standard tags for common use cases:

- `mlflow.trace.session` – Session identifier for grouping related [Traces](/concepts/traces.md).
- `mlflow.trace.user` – User identifier for tracking per‑user interactions.
- `mlflow.source.name` – Entry point or script that generated the trace.
- `mlflow.source.git.commit` – Git commit hash of the source code (if applicable).
- `mlflow.source.type` – Source type (`PROJECT`, `NOTEBOOK`, etc.).

Custom tags can also be added for specific needs. ^[trace-concepts-databricks-on-aws.md]

## Active vs. Finished [Traces](/concepts/traces.md)

An **active trace** is a trace that [MLflow](/concepts/mlflow.md) is currently writing, for example, while a function decorated with `@mlflow.trace` is running. After the decorated function exits, the trace is **finished**, but it can still be annotated with new data. ^[trace-concepts-databricks-on-aws.md]

To work with active or recent [Traces](/concepts/traces.md), use `mlflow.get_active_trace_id()` to return the ID of the currently active trace, and `mlflow.get_last_active_trace_id()` to return the ID of the most recent finished trace. ^[trace-concepts-databricks-on-aws.md]

## Instrumentation

[MLflow](/concepts/mlflow.md) provides three approaches to add tracing to Python and TypeScript applications: ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

- **Automatic** – Add one line (`mlflow.<library>.autolog()`) to automatically capture app logic for 20+ supported libraries. Common integrations include OpenAI (`mlflow.openai.autolog()`), LangChain/LangGraph (`mlflow.langchain.autolog()`), LiteLLM (`mlflow.litellm.autolog()`), Semantic Kernel (`mlflow.semantic_kernel.autolog()`), Agno (`mlflow.agno.autolog()`), Groq (`mlflow.groq.autolog()`), [Smolagents](/concepts/smolagents.md) (`mlflow.[Smolagents](/concepts/smolagents.md).autolog()`), and Databricks Foundation Models. Note that for these integrations, only synchronous calls are traced; asynchronous and streaming methods are not captured. ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md] ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md] ^[tracing-agno-databricks-on-aws.md] ^[tracing-semantic-kernel-databricks-on-aws.md] ^[tracing-openai-agents-databricks-on-aws.md] ^[tracing-groq-databricks-on-aws.md] ^[tracing-smolagents-databricks-on-aws.md]

- **Manual** – Use the `@mlflow.trace` decorator to trace any Python function, and `mlflow.start_span()` to create child spans for more detailed insights within a function. Designed for custom logic and complex workflows. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md] ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

- **Combined** – Mix both approaches for complete coverage. Start with [Automatic Tracing](/concepts/automatic-tracing.md) for the fastest path to [Traces](/concepts/traces.md), then add [Manual Tracing](/concepts/manual-tracing.md) when more control is needed. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

On serverless compute clusters, [Autologging for GenAI Tracing](/concepts/autologging-for-genai-tracing.md) frameworks is not automatically enabled — it must be explicitly called via the appropriate `mlflow.<library>.autolog()` function. ^[tracing-agno-databricks-on-aws.md] ^[tracing-semantic-kernel-databricks-on-aws.md] ^[tracing-groq-databricks-on-aws.md] ^[tracing-smolagents-databricks-on-aws.md]

## Uses Across Environments

- **In Development** – Tracing provides detailed visibility into what happens beneath the abstractions of GenAI libraries, helping identify where issues or unexpected behaviors occur. It captures the complete request‑response cycle and execution flow. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]
- **In Production** – [Traces](/concepts/traces.md) capture errors and operational metrics like latency at each step, aiding in real‑time diagnostics and quick resolution of production issues. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

## Monitor Performance and Optimize Costs

[MLflow](/concepts/mlflow.md) Tracing captures key operational metrics such as latency, cost, and resource utilization at each step of application execution. This enables tracking performance bottlenecks, monitoring resource utilization, optimizing cost efficiency, and identifying areas for performance improvement. [MLflow](/concepts/mlflow.md) Tracing is compatible with OpenTelemetry, allowing export of trace data to various services in existing observability stacks. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

For integrations such as [Smolagents](/concepts/smolagents.md), [MLflow](/concepts/mlflow.md) logs detailed token usage (input, output, total) per LLM call. This information is available via the `mlflow.chat.tokenUsage` attribute on spans and the `token_usage` field on the trace info object. ^[tracing-smolagents-databricks-on-aws.md]

## Analyze [Traces](/concepts/traces.md) with [Genie Code](/concepts/genie-code.md)

[Genie Code](/concepts/genie-code.md) provides a natural language interface for exploring and debugging [Traces](/concepts/traces.md). Users can ask questions like "Are there any error [Traces](/concepts/traces.md) in this experiment?" or "What's the P95 latency for my [Traces](/concepts/traces.md)?" and get immediate answers. [Genie Code](/concepts/genie-code.md) has read access to [Traces](/concepts/traces.md), sessions, [Evaluation Runs](/concepts/evaluation-runs.md), [[scorers|Scorers]], datasets, [Labeling Sessions](/concepts/labeling-sessions.md), and more. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

## Relationship to Evaluation and Monitoring

Tracing provides the real‑time trace logging foundation for the evaluation and monitoring component of [MLflow 3](/concepts/mlflow-3.md). [Traces](/concepts/traces.md) can be evaluated during development using built‑in or custom [LLM Judges and Scorers](/concepts/llm-judges-and-scorers.md), and [Production Monitoring](/concepts/production-monitoring.md) can reuse the same judges and [[scorers|Scorers]] for consistent evaluation throughout the application lifecycle. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Storage Layout

[MLflow](/concepts/mlflow.md) optimizes trace storage for performance and cost. `TraceInfo` is stored directly in a relational database as indexed rows, enabling fast queries for searching and filtering [Traces](/concepts/traces.md). `TraceData` (spans) is stored in artifact storage to keep queries fast even as trace

# Citations

1. [mlflow-tracing-genai-observability-databricks-on-aws.md](/references/mlflow-tracing-genai-observability-databricks-on-aws-9bbb7d89.md)
2. [debug-and-analyze-your-app-with-tracing-databricks-on-aws.md](/references/debug-and-analyze-your-app-with-tracing-databricks-on-aws-d9c92247.md)
3. [trace-concepts-databricks-on-aws.md](/references/trace-concepts-databricks-on-aws-9723e725.md)
4. [add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md](/references/add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws-91d388aa.md)
5. [get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md](/references/get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws-860f2761.md)
6. [get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md](/references/get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws-58181913.md)
7. [tracing-agno-databricks-on-aws.md](/references/tracing-agno-databricks-on-aws-c7a8a057.md)
8. [tracing-semantic-kernel-databricks-on-aws.md](/references/tracing-semantic-kernel-databricks-on-aws-b5fb97fc.md)
9. [tracing-openai-agents-databricks-on-aws.md](/references/tracing-openai-agents-databricks-on-aws-db457d66.md)
10. [tracing-groq-databricks-on-aws.md](/references/tracing-groq-databricks-on-aws-121d088c.md)
11. [tracing-smolagents-databricks-on-aws.md](/references/tracing-smolagents-databricks-on-aws-485dc1ff.md)
12. [evaluate-and-monitor-ai-agents-databricks-on-aws.md](/references/evaluate-and-monitor-ai-agents-databricks-on-aws-edcafd11.md)
