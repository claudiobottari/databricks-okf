---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 09c45f7972a1db186cd5fd165a64bff62ef2262341378dc0e298d09b7128f2b7
  pageDirectory: concepts
  sources:
    - tracing-groq-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-groq-autolog
    - MGA
  citations:
    - file: tracing-groq-databricks-on-aws.md
title: MLflow Groq Autolog
description: Automatic trace generation for Groq SDK calls via mlflow.groq.autolog()
tags:
  - mlflow
  - tracing
  - groq
  - databricks
timestamp: "2026-06-19T23:11:52.178Z"
---

# [MLflow](/concepts/mlflow.md) Groq Autolog

**MLflow Groq Autolog** is an integration that enables [Automatic Tracing](/concepts/automatic-tracing.md) of Groq SDK calls through [MLflow Tracing](/concepts/mlflow-tracing.md). When enabled, usage of the Groq SDK is automatically recorded as [Traces](/concepts/traces.md), providing observability into [Large Language Model (LLM)](/concepts/large-language-models-llms-on-databricks.md) interactions during interactive development. ^[tracing-groq-databricks-on-aws.md]

## Overview

The `mlflow.groq.autolog()` function activates automatic trace collection for synchronous calls to the Groq SDK. This allows developers to capture and inspect the inputs, outputs, and performance characteristics of their Groq-powered applications without manual instrumentation. ^[tracing-groq-databricks-on-aws.md]

On serverless compute clusters, autologging is not automatically enabled. You must explicitly call `mlflow.groq.autolog()` to enable [Automatic Tracing](/concepts/automatic-tracing.md) for this integration. ^[tracing-groq-databricks-on-aws.md]

## Supported Operations

Only synchronous calls to the Groq SDK are traced. Asynchronous API calls and streaming methods are not supported and will not generate [Traces](/concepts/traces.md). ^[tracing-groq-databricks-on-aws.md]

## Example Usage

The following example demonstrates basic setup and usage of Groq autologging on Databricks:

```python
import groq
import [[mlflow|MLflow]]

# Turn on auto tracing for Groq
[[mlflow|MLflow]].groq.autolog()

# Set up [[mlflow-tracking|MLflow Tracking]] on Databricks
[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/groq-demo")

client = groq.Groq()

# Use the create method to create new message
message = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of low latency LLMs.",
        }
    ],
)

print(message.choices[0].message.content)
```

^[tracing-groq-databricks-on-aws.md]

## Disabling Auto-Tracing

Auto-tracing for Groq can be disabled globally using either of the following approaches:

- `mlflow.groq.autolog(disable=True)` — Disables tracing specifically for the Groq integration
- `mlflow.autolog(disable=True)` — Disables all [MLflow](/concepts/mlflow.md) auto-logging, including Groq tracing

^[tracing-groq-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The broader tracing system that captures and organizes trace data
- [MLflow Autolog](/concepts/mlflow-autologging.md) — General mechanism for automatic tracking of model training and inference
- Observability for LLM Applications — Using [Traces](/concepts/traces.md) to debug and monitor application behavior
- Quality Evaluation for LLM Apps — Setting up quality assessment for Groq-powered applications

## Sources

- tracing-groq-databricks-on-aws.md

# Citations

1. [tracing-groq-databricks-on-aws.md](/references/tracing-groq-databricks-on-aws-121d088c.md)
