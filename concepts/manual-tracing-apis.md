---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f1629d8007b119510193cfa451c48aa60fef1413a84d6c5f4a1bb01c04498998
  pageDirectory: concepts
  sources:
    - instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - manual-tracing-apis
    - MTA
    - Low-level API for Manual Tracing
    - Manual Tracing with Client APIs
  citations:
    - file: instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md
title: Manual Tracing APIs
description: "Four manual tracing approaches: trace() for functions, @trace decorator for class methods, withSpan() for code blocks, and explicit startSpan/endSpan for full lifecycle control."
tags:
  - tracing
  - manual-instrumentation
  - development
timestamp: "2026-06-19T19:10:46.023Z"
---

---
title: Manual Tracing APIs
summary: MLflow provides several manual tracing APIs for TypeScript/JavaScript that give developers fine-grained control over span creation.
sources:
  - instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md
kind: concept
createdAt: 2026-06-25T00:00:00.000Z
updatedAt: 2026-06-25T00:00:00.000Z
tags:
  - mlflow
  - tracing
  - typescript-sdk
aliases:
  - manual-tracing-apis
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Manual Tracing APIs

The **Manual Tracing APIs** in the [MLflow Tracing](/concepts/mlflow-tracing.md) TypeScript SDK let developers explicitly define spans to instrument their Node.js applications. These APIs provide fine-grained control over what is captured in a [Trace](/concepts/traces.md), including the ability to wrap individual functions, class methods, blocks of code, and explicitly manage the span lifecycle. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

Manual tracing is useful when automatic tracing (e.g., via `tracedOpenAI`) does not cover a specific library or when developers need to trace custom business logic. Each manual tracing API automatically captures input arguments, return values, exception information (if thrown), and latency. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

## The `trace` API

The `trace` API is used to wrap a named or anonymous function so that every invocation produces a Span. The developer passes the function and an options object containing a name for the span.

```typescript
import * as mlflow from 'mlflow-tracing';

const getWeather = async (city: string) => {
  return `The weather in ${city} is sunny`;
};

const tracedGetWeather = mlflow.trace(getWeather, { name: 'get-weather' });
const result = await tracedGetWeather('San Francisco');
```

On each call to the traced function, MLflow creates a span that records the inputs, outputs, any exceptions, and the execution latency. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

### Capturing Nested Function Calls

When multiple functions are traced and called from one another, MLflow automatically generates a trace with multiple spans whose structure reflects the nesting. For example:

```typescript
const sum = mlflow.trace((a: number, b: number) => a + b, { name: 'sum' });
const multiply = mlflow.trace((a: number, b: number) => a * b, { name: 'multiply' });

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

The resulting trace shows a root span `compute-area` with child spans `sum` and two invocations of `multiply`. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

## The `@trace` Decorator

TypeScript 5.0+ supports decorators, and MLflow provides a `@trace` decorator to trace class methods easily. The decorator accepts options such as the span type.

```typescript
import * as mlflow from 'mlflow-tracing';

class MyClass {
  @mlflow.trace({ spanType: mlflow.SpanType.LLM })
  generateText(prompt: string) {
    return "It's sunny in Seattle!";
  }
}
```

Every call to the decorated method creates a span that captures inputs, outputs, exceptions, and latency. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

## The `withSpan` API

The `withSpan` API traces a block of code rather than a function. It accepts an async callback and an options object with a name, span type, and inputs.

```typescript
import * as mlflow from 'mlflow-tracing';

const question = "What's the weather like in Seattle?";
const result = await mlflow.withSpan(
  async (span: mlflow.Span) => {
    return "It's sunny in Seattle!";
  },
  {
    name: 'generateText',
    spanType: mlflow.SpanType.TOOL,
    inputs: { prompt: question },
  },
);
```

The span is automatically closed when the callback completes, recording the return value as outputs. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

## Explicit Span Creation and Termination

For maximum control over the span lifecycle, developers can create a span with `mlflow.startSpan` and end it explicitly with `span.end`.

```typescript
import * as mlflow from 'mlflow-tracing';

const span = mlflow.startSpan({
  name: 'generateText',
  spanType: mlflow.SpanType.LLM,
  inputs: { prompt: question },
});

span.end({
  outputs: { answer: "It's sunny in Seattle!" },
  status: 'OK',
});
```

This approach is useful when span boundaries do not align with function or block boundaries. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – Overview of the tracing system.
- [Automatic Tracing](/concepts/automatic-tracing.md) – Pre-built integrations for libraries like OpenAI.
- Span – The fundamental unit of work in a trace.
- [Trace](/concepts/traces.md) – A collection of spans representing a request flow.
- [Add Context to Traces](/concepts/best-practices-for-adding-context-to-mlflow-traces.md) – Grouping traces by user sessions.
- [TypeScript SDK](/concepts/mlflow-typescript-tracing-sdk.md) – The package `mlflow-tracing` used for instrumentation.

## Sources

- instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md

# Citations

1. [instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md](/references/instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws-1c7052f5.md)
