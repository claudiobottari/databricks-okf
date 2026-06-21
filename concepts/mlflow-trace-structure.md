---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 175d63d227289a22b5a823314606694f893da598d830b439e5db83e5c4a92377
  pageDirectory: concepts
  sources:
    - get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-structure
    - MTS
    - MLflow Traces|Trace
    - MLflow Traces|trace
    - Trace Structure
  citations:
    - file: get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md
title: MLflow Trace Structure
description: The hierarchical structure of a trace consisting of root and child spans, each containing attributes (model name, token counts, timing), inputs, and outputs.
tags:
  - tracing
  - spans
  - mlflow
  - observability
timestamp: "2026-06-19T10:45:01.851Z"
---

# MLflow Trace Structure

**MLflow Trace Structure** describes the hierarchical organization of telemetry data captured by [MLflow Tracing](/concepts/mlflow-tracing.md) when observing [GenAI](/concepts/mlflow-genai-evaluate-api.md) applications. A trace is a complete record of a single invocation of an application, composed of nested **spans** that represent distinct operations within that call.

## Overview

When a GenAI application instrumented with [MLflow Tracing](/concepts/mlflow-tracing.md) executes, the system captures a structured trace that logs the application's behavior. The trace provides visibility into what was asked, what response was generated, how long the request took, and how many tokens were used (affecting cost). For more complex applications like RAG systems or multi-step agents, [MLflow Tracing](/concepts/mlflow-tracing.md) reveals the inner workings of each component and step. ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

## Trace Structure

A trace consists of:

- **Root span**: Represents the entry point of the application (e.g., the `my_app(...)` function). It captures the top-level inputs to the application and the final output.
- **Child span(s)**: Represents individual operations within the application (e.g., an OpenAI completion request). These spans capture the intermediate steps and their inputs/outputs.

Each span contains:

- **Attributes**: Metadata such as the model name, token counts, and timing information.
- **Inputs**: The messages or data sent to the operation (e.g., the messages sent to the model).
- **Outputs**: The response received from the operation (e.g., the response from the model).

## Example Trace

In a simple GenAI application, the trace shows:

1. **Root span**: The inputs to the `my_app(...)` function and its final output.
2. **Child span**: The OpenAI completion request, including the model name, token counts, and timing information.

Even this minimal trace surfaces useful information about the application's behavior. ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

## Capturing Traces

Traces are captured by:

- Using the `@mlflow.trace` decorator on Python functions to capture the application's entry point.
- Using `mlflow.openai.autolog()` to automatically instrument calls to the [OpenAI SDK](/concepts/openai-api-compatibility-in-databricks.md).
- Running the application, which produces a trace visible in the MLflow experiment UI under the **Traces** tab.

For details on adding tracing to apps, see [Add traces to applications: automatic and manual tracing](/concepts/combined-automatic-and-manual-tracing.md) and [MLflow Tracing Integrations](/concepts/mlflow-tracing-integrations.md) (more than 20 library integrations). ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The core observability framework for GenAI applications.
- Spans — Individual units of work within a trace.
- Trace Attributes — Metadata captured in each span (model name, token counts, timing).
- [Automatic Instrumentation](/concepts/automatic-tracing.md) — How `mlflow.openai.autolog()` captures OpenAI API calls.
- [Manual Tracing](/concepts/manual-tracing.md) — Using the `@mlflow.trace` decorator for custom function tracing.
- RAG Systems — Complex applications where traces reveal component-level behavior.

## Sources

- get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md

# Citations

1. [get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md](/references/get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws-58181913.md)
