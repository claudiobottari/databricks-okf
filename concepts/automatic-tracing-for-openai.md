---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: db3b53e7344f7f67f5ecad8ad627a01567bbf779effd40a3ab5b2616a229ca16
  pageDirectory: concepts
  sources:
    - instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automatic-tracing-for-openai
    - ATFO
    - Auto-Tracing for OpenAI
    - Auto-tracing for OpenAI
    - auto-tracing for OpenAI
  citations:
    - file: instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md
title: Automatic Tracing for OpenAI
description: One-line integration that automatically traces OpenAI SDK calls by wrapping the client with the tracedOpenAI function from the mlflow-openai package.
tags:
  - openai
  - automatic-instrumentation
  - llm
timestamp: "2026-06-19T19:10:37.637Z"
---

# Automatic Tracing for OpenAI

**Automatic Tracing for OpenAI** is a feature of the [MLflow Tracing TypeScript SDK](/concepts/mlflow-tracing-typescript-sdk.md) that enables automatic instrumentation of OpenAI SDK calls with minimal code changes. By wrapping the OpenAI client with the `tracedOpenAI` function, developers can capture detailed telemetry data — including inputs, outputs, latency, and error information — for every OpenAI API invocation without modifying existing application logic. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

## Overview

The [MLflow Tracing](/concepts/mlflow-tracing.md) TypeScript SDK provides automatic tracing for supported libraries. Currently, the SDK supports automatic tracing for the [OpenAI SDK](/concepts/openai-api-compatibility-in-databricks.md). When enabled, each call to the OpenAI client (such as chat completions) is automatically captured as a trace span, enabling observability into GenAI application behavior. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

## Requirements

To use automatic tracing for OpenAI, you need:

- `mlflow-tracing` from the [npm registry](https://www.npmjs.com/package/mlflow-tracing)
- `mlflow-openai` from the [npm registry](https://www.npmjs.com/package/mlflow-openai)
- Node.js 14 or above
- A Databricks workspace with access to [MLflow Experiments](/concepts/mlflow-experiment.md)

^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

## Setup

### Install the packages

```bash
npm install mlflow-tracing
npm install mlflow-openai
```

^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

### Initialize the SDK

Before using automatic tracing, initialize the [MLflow Tracing](/concepts/mlflow-tracing.md) SDK with your Databricks workspace and experiment ID:

```typescript
import * as mlflow from 'mlflow-tracing';

mlflow.init({
  trackingUri: 'databricks',
  experimentId: '<your-experiment-id>',
});
```

^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

### Wrap the OpenAI client

Import the `tracedOpenAI` function from `mlflow-openai` and wrap your OpenAI client instance:

```typescript
import { OpenAI } from 'openai';
import { tracedOpenAI } from 'mlflow-openai';

// Wrap the OpenAI client with the tracedOpenAI function
const client = tracedOpenAI(new OpenAI());

// Invoke the client as usual
const response = await client.chat.completions.create({
  model: 'gpt-4o-mini',
  messages: [
    { role: 'system', content: 'You are a helpful weather assistant.' },
    { role: 'user', content: "What's the weather like in Seattle?" },
  ],
});
```

^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

## How It Works

Once the OpenAI client is wrapped with `tracedOpenAI`, every API call made through that client is automatically traced. MLflow captures:

- Input arguments (e.g., model name, messages, parameters)
- Return values (e.g., generated responses)
- Exception information if an error is thrown
- Latency metrics

The traced data is sent to the configured Databricks workspace and associated with the specified MLflow Experiment, where it can be viewed and analyzed in the Trace UI. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

## Comparison with Manual Tracing

Automatic tracing requires only one additional line of code (the `tracedOpenAI` wrapper) and works with existing OpenAI SDK usage patterns. In contrast, [Manual Tracing](/concepts/manual-tracing.md) requires explicitly wrapping individual functions with `mlflow.trace()` or using the `@trace` decorator. Automatic tracing is ideal for quickly adding observability to OpenAI-based applications, while manual tracing provides finer-grained control over what gets captured. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The broader tracing framework for GenAI applications
- [Manual Tracing](/concepts/manual-tracing.md) — Alternative approach for instrumenting custom functions and code blocks
- Trace UI — The interface for viewing and analyzing captured traces
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for traces and runs
- [OpenAI SDK](/concepts/openai-api-compatibility-in-databricks.md) — The library being automatically instrumented
- Span — The fundamental unit of work captured in a trace

## Sources

- instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md

# Citations

1. [instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md](/references/instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws-1c7052f5.md)
