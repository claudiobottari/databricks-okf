---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ba838adb9a7a5b23d139782fb4278cd725fbce7d6ad420813104c8bd1479afea
  pageDirectory: concepts
  sources:
    - debug-and-analyze-your-app-with-tracing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - inputoutput-tracking
    - Raw Inputs/Outputs Tab (MLflow UI)
  citations:
    - file: debug-and-analyze-your-app-with-tracing-databricks-on-aws.md
title: Input/Output Tracking
description: The practice of capturing inputs, outputs, and metadata for each intermediate step in a GenAI application pipeline (retrieval, tool calls, LLM interactions) to enable debugging and analysis.
tags:
  - observability
  - debugging
  - genai
timestamp: "2026-06-19T14:55:23.878Z"
---

# Input/Output Tracking

**Input/Output Tracking** is a feature of [MLflow Tracing](/concepts/mlflow-tracing.md) that captures the complete request–response cycle of an application. By recording the inputs and outputs of each intermediate step — such as retrieval calls, tool invocations, and LLM interactions — it enables deep visibility into the execution flow and decision-making process. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

## Overview

Input/Output Tracking forms the core of trace-based debugging. When a trace is created, MLflow records the exact inputs provided to each step and the outputs (including any errors) that are returned. This data is stored alongside step-level metadata such as latency, cost, and resource utilization, making it possible to reconstruct the full path of a request. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

The tracking works consistently in both development and production environments. Developers can examine traces in their IDE or notebook, while production teams can inspect live traces on a monitoring dashboard, all without re‑instrumenting the application. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

## How It Works

When a GenAI application is instrumented with [MLflow Tracing](/concepts/mlflow-tracing.md), each function or service call in the pipeline automatically captures:

- The **input** sent to the step (e.g., a prompt, a query, or tool arguments).
- The **output** returned by the step (e.g., a model response, a retrieval result, or an error).
- **Metadata** such as latency, token counts, or cost (if configured).

These records are organized into a trace that can be inspected via the MLflow UI or exported to observability tools using the OpenTelemetry integration. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

## Benefits

- **Precise debugging in development** – Identify exactly where a pipeline breaks or produces unexpected behavior by examining step-by-step inputs and outputs. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]
- **Real-time monitoring in production** – Detect errors or performance regressions by reviewing the inputs and outputs of live requests. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]
- **Performance and cost analysis** – Combine input/output data with latency and cost metrics to diagnose bottlenecks and optimize resource usage. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]
- **Integration with Genie Code** – Use natural language queries to search for traces with specific input patterns or error outputs. ^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The overarching tracing system that includes Input/Output Tracking.
- OpenTelemetry Integration — Exporting traces to external observability stacks.
- [Genie Code for Agent Observability](/concepts/genie-code-for-agent-observability.md) — Natural language analysis of traces.
- [User Feedback](/concepts/multi-dimensional-user-feedback.md) — Collecting human ratings on outputs.
- [Quality Evaluations](/concepts/evaluation-runs.md) — Automated assessment of output quality.

## Sources

- debug-and-analyze-your-app-with-tracing-databricks-on-aws.md

# Citations

1. [debug-and-analyze-your-app-with-tracing-databricks-on-aws.md](/references/debug-and-analyze-your-app-with-tracing-databricks-on-aws-d9c92247.md)
