---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 354e513c40d450b14abef3e8956645393a7c493ea5ab3e3cab31ecb895a30fb6
  pageDirectory: concepts
  sources:
    - instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-typescript-sdk
    - MTTS
  citations:
    - file: instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md
title: MLflow Tracing TypeScript SDK
description: An npm package (mlflow-tracing) that brings MLflow Tracing observability to TypeScript and JavaScript Node.js applications with minimal code changes.
tags:
  - instrumentation
  - node.js
  - observability
timestamp: "2026-06-19T19:10:48.939Z"
---

# [MLflow Tracing](/concepts/mlflow-tracing.md) TypeScript SDK

The **MLflow Tracing TypeScript SDK** is an official package (`mlflow-tracing`) available from the npm registry that brings [MLflow Tracing](/concepts/mlflow-tracing.md) capabilities to TypeScript and JavaScript applications. It enables developers to add production-ready observability to [GenAI](/concepts/mlflow-genai-evaluate-api.md) applications with minimal code changes and leverage Databricks' analytics and monitoring platform. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

## Requirements

To use the SDK, you need:

- Node.js 14 or above
- A Databricks workspace with access to [MLflow Experiments](/concepts/mlflow-experiment.md)
- The `mlflow-tracing` package installed from the npm registry

For automatic tracing with OpenAI, you additionally need the `mlflow-openai` package. Databricks recommends installing the latest version of the SDK when developing Node.js applications with tracing. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

## Setup

### Installation

Install the package from the npm registry:

```bash
npm install mlflow-tracing
```

^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

### Authentication

Configure authentication using either environment variables or a `.env` file. In your MLflow Experiment, generate an API key and export the required credentials:

```bash
export DATABRICKS_TOKEN=<databricks-personal-access-token>
export DATABRICKS_HOST=https://<workspace-name>.cloud.databricks.com
```

^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

### Initialization

Initialize the SDK with your experiment ID in your Node.js application:

```typescript
import * as mlflow from 'mlflow-tracing';

mlflow.init({
  trackingUri: 'databricks',
  experimentId: '<your-experiment-id>',
});
```

^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

## Automatic Tracing

The SDK supports automatic tracing for the OpenAI SDK. After installing the `mlflow-openai` package, wrap the OpenAI client with the `tracedOpenAI` function:

```typescript
import * as mlflow from 'mlflow-tracing';
import { OpenAI } from 'openai';
import { tracedOpenAI } from 'mlflow-openai';

mlflow.init({
  trackingUri: 'databricks',
  experimentId: '<your-experiment-id>',
});

const client = tracedOpenAI(new OpenAI());
const response = await client.chat.completions.create({
  model: 'gpt-4o-mini',
  messages: [
    { role: 'system', content: 'You are a helpful weather assistant.' },
    { role: 'user', content: "What's the weather like in Seattle?" },
  ],
});
```

^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

## Manual Tracing

### The `trace` API

Use the `trace` API to wrap individual functions. MLflow automatically captures input arguments, return values, exception information, and latency on each invocation. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

```typescript
const getWeather = async (city: string) => {
  return `The weather in ${city} is sunny`;
};

const tracedGetWeather = mlflow.trace(getWeather, { name: 'get-weather' });
const result = await tracedGetWeather('San Francisco');
```

### Nested Function Calls

When tracing nested functions, MLflow generates a trace with multiple spans that reflect the call hierarchy. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

```typescript
const sum = mlflow.trace((a: number, b: number) => a + b, { name: 'sum' });
const multiply = mlflow.trace((a: number, b: number) => a * b, { name: 'multiply' });

const computeArea = mlflow.trace(
  (a: number, b: number, h: number) => {
    const sumOfBase = sum(a, b);
    return multiply(multiply(sumOfBase, h), 0.5);
  },
  { name: 'compute-area' },
);
```

The trace structure reflects the nesting:

```
- compute-area
  - sum (a=1, b=2)
  - multiply (a=3, b=3)
  - multiply (a=9, b=0.5)
```

### The `@trace` Decorator

TypeScript 5.0+ supports decorators, which the SDK leverages to trace class methods. The decorator captures input arguments, return values, exception information, and latency. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

```typescript
import * as mlflow from 'mlflow-tracing';

class MyClass {
  @mlflow.trace({ spanType: mlflow.SpanType.LLM })
  generateText(prompt: string) {
    return "It's sunny in Seattle!";
  }
}
```

### The `withSpan` API

Use `withSpan` to trace a block of code rather than an entire function. The API accepts an options object for specifying the span name, type, and inputs. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

```typescript
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

### Explicit Span Lifecycle

For fine-grained control, you can create and end spans explicitly using `startSpan` and `end`. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

```typescript
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

## Grouping Traces by Users and Sessions

The SDK supports grouping traces by user sessions, which is useful for applications that maintain multi-turn user interactions. Traces are often generated per-request, but session grouping helps understand an end-user's complete journey and identify issues. See the guide on [adding context to traces](/concepts/best-practices-for-adding-context-to-mlflow-traces.md) for more details. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

## Full-Stack Example

A complete full-stack example demonstrating [MLflow Tracing](/concepts/mlflow-tracing.md) TypeScript SDK usage in a Node.js application is available in the [MLflow GitHub repository](/concepts/databricks-connect-github-repository.md). ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The core tracing capability for observability
- Trace UI — The interface for analyzing application behavior and performance
- Evaluating application quality — Leveraging traces to assess and improve app quality
- [Production Monitoring](/concepts/production-monitoring.md) — Real-time quality metric tracking in production
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs and traces
- Span — The fundamental unit of work in a trace

## Sources

- instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md

# Citations

1. [instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md](/references/instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws-1c7052f5.md)
