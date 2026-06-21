---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 489b891e29dd178e85b7066009822db0ff2a36f3cf0d3727924dd0e03277c67a
  pageDirectory: concepts
  sources:
    - instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - nested-function-tracing
    - NFT
  citations:
    - file: instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md
title: Nested Function Tracing
description: When traced functions call other traced functions, MLflow generates a hierarchical trace where parent-child span structure mirrors the call graph.
tags:
  - tracing
  - nesting
  - call-graph
timestamp: "2026-06-19T19:10:48.322Z"
---

# Nested Function Tracing

**Nested Function Tracing** is a feature of [MLflow Tracing](/concepts/mlflow-tracing.md) that automatically captures the hierarchical relationship between function calls when tracing instrumented code. When multiple traced functions are called within one another, MLflow generates a trace with multiple spans whose structure mirrors the nesting of the function calls. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

## Overview

When you trace nested functions using the `mlflow.trace()` API, MLflow automatically creates a parent-child span hierarchy. Each traced function invocation produces a span that captures input arguments, return values, exception information (if thrown), and latency. The span structure reflects the call stack, making it possible to visualize how high-level operations decompose into lower-level steps. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

## Example

The following TypeScript example demonstrates nested function tracing with three traced functions: `sum`, `multiply`, and `computeArea`. The `computeArea` function calls both `sum` and `multiply` internally: ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

```typescript
const sum = mlflow.trace(
  (a: number, b: number) => {
    return a + b;
  },
  { name: 'sum' },
);

const multiply = mlflow.trace(
  (a: number, b: number) => {
    return a * b;
  },
  { name: 'multiply' },
);

const computeArea = mlflow.trace(
  (a: number, b: number, h: number) => {
    const sumOfBase = sum(a, b);
    const area = multiply(sumOfBase, h);
    return multiply(area, 0.5);
  },
  { name: 'compute-area' },
);

computeArea(1, 2, 3);
```

The resulting trace has the following span hierarchy: ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

```
- compute-area
  - sum (a=1, b=2)
  - multiply (a=3, b=3)
  - multiply (a=9, b=0.5)
```

## Benefits

Nested function tracing provides several advantages for debugging and observability: ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

- **Hierarchical visibility**: See how high-level operations break down into sub-operations.
- **Per-span metrics**: Each nested span captures its own latency, inputs, outputs, and errors independently.
- **Root cause analysis**: Identify which specific sub-operation caused a failure or performance bottleneck in a complex workflow.

## Related APIs

Nested function tracing is supported through the following [MLflow Tracing TypeScript SDK](/concepts/mlflow-tracing-typescript-sdk.md) APIs: ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

- **`mlflow.trace()`** — Wraps a named or anonymous function to create a traced function that participates in nesting.
- **`@mlflow.trace` decorator** — Traces class methods and automatically nests them when called from other traced methods.
- **`mlflow.withSpan()`** — Traces a block of code and nests it within the current span context.
- **`mlflow.startSpan()` / `span.end()`** — Provides explicit control over span lifecycle for custom nesting scenarios.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The broader tracing framework for GenAI applications.
- Span — The fundamental unit of work in a trace, representing a single operation.
- [Trace](/concepts/traces.md) — The complete record of a request's journey through an application.
- [Automatic Tracing](/concepts/automatic-tracing.md) — Tracing that requires minimal code changes by wrapping supported libraries like OpenAI.
- [Manual Tracing](/concepts/manual-tracing.md) — Tracing that uses explicit APIs like `trace()`, `withSpan()`, or decorators.

## Sources

- instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md

# Citations

1. [instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md](/references/instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws-1c7052f5.md)
