---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b9fb7ed68456c73da61af7d469448b4c3199d698f68bd4201cadfca1feafdf7f
  pageDirectory: concepts
  sources:
    - instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - span-types-and-lifecycle
    - Lifecycle and Span Types
    - STAL
    - Span Types|Span Type
  citations:
    - file: instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md
title: Span Types and Lifecycle
description: Spans capture input arguments, return values, exception info, and latency; they can be typed (LLM, TOOL, etc.) and organized hierarchically to represent nested function calls.
tags:
  - spans
  - observability
  - telemetry
timestamp: "2026-06-19T19:10:55.861Z"
---

# Span Types and Lifecycle

**Span Types and Lifecycle** refers to the classification and management of individual units of work — called spans — within the [MLflow Tracing](/concepts/mlflow-tracing.md) system. Spans capture the execution of a single operation (e.g. an LLM call, a tool invocation, or a custom function) and together form a trace that represents a complete request flow. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

## Span Types

[MLflow Tracing](/concepts/mlflow-tracing.md) defines multiple span types to categorize the kind of operation being traced. The SDK provides enumerations via `mlflow.SpanType`:

- **`SpanType.LLM`** – Represents a call to a large language model (e.g. OpenAI chat completion). ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]
- **`SpanType.TOOL`** – Represents a tool or function invocation within an agent or application. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

Span types are optional parameters in most tracing APIs and help the Databricks UI correctly classify and display different kinds of operations. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

## Span Lifecycle

A span typically follows a **create → (capture inputs) → (execute) → capture outputs → close** lifecycle. The [MLflow Tracing](/concepts/mlflow-tracing.md) TypeScript SDK provides several APIs to control this lifecycle.

### 1. Automatic Tracing

When using the tracedOpenAI wrapper, the SDK automatically creates and ends spans for every OpenAI API call. The developer does not need to manage the lifecycle manually. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

### 2. Tracing a Function with `mlflow.trace`

The `trace()` API wraps a function so that a span is created for each invocation. The span automatically captures:
- Input arguments
- Return value
- Exception information if thrown
- Latency

The function receives an optional `name` and `spanType`. The span is **automatically ended** when the function completes or throws. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

### 3. Tracing a Class Method with the `@trace` Decorator

TypeScript 5.0+ decorators allow annotating class methods with `@mlflow.trace({ spanType: ... })`. The lifecycle is identical to the function‑level `trace` API: the span opens on method entry and closes on method exit. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

### 4. Tracing a Block of Code with `mlflow.withSpan`

The `withSpan()` API creates a span for an arbitrary async code block. The developer provides the block as a callback that receives the span object. The span is **automatically ended** when the callback completes. Options include `name`, `spanType`, and `inputs`. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

### 5. Explicit Span Management: `startSpan` and `end`

For full control over the span lifecycle, use `mlflow.startSpan()` to create a span with `name`, `spanType`, and `inputs`. The span remains open until the developer calls `span.end()` with `outputs` and a `status` (e.g. `'OK'`). This is useful when the operation’s start and end points are not aligned with a single function or block. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

## Nested Spans

When traced functions call other traced functions (or when a `withSpan` block contains `trace` calls), MLflow automatically builds a **hierarchical trace** where child spans are nested inside their parent span. The resulting trace shows the full call tree with inputs, outputs, and latency at each level. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

## Grouping Traces by Users and Sessions

Real‑world applications often need to group individual traces into longer user sessions. [MLflow Tracing](/concepts/mlflow-tracing.md) supports attaching session and user identifiers to spans, which can be used later to analyse end‑user journeys in the Databricks UI. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The overall observability framework.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The container for storing traces.
- OpenAI — A supported provider for automatic tracing.
- Node.js — The runtime for the TypeScript SDK.
- TracedOpenAI — A convenience wrapper for OpenAI instrumentation.
- Databricks — The platform used for storage and analysis of traces.

## Sources

- instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md

# Citations

1. [instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md](/references/instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws-1c7052f5.md)
