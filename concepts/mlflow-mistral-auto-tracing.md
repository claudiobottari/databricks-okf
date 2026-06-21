---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e8e33ac911dfd5ac3d196cad3d7bad1fd7daeaa2a6d85862106a97d63f9bc5dd
  pageDirectory: concepts
  sources:
    - tracing-mistral-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-mistral-auto-tracing
    - MMAT
  citations:
    - file: tracing-mistral-databricks-on-aws.md
title: MLflow Mistral Auto Tracing
description: Automatic tracing of Mistral AI API calls via mlflow.mistral.autolog() that captures request/response telemetry without manual instrumentation.
tags:
  - mlflow
  - mistral-ai
  - tracing
  - databricks
timestamp: "2026-06-19T23:12:19.108Z"
---

# [MLflow](/concepts/mlflow.md) Mistral Auto Tracing

**MLflow Mistral Auto Tracing** is a feature that automatically captures and logs trace data from [Mistral AI](/concepts/mistral-ai-python-sdk.md) API calls when using the [MLflow](/concepts/mlflow.md) tracing system. By enabling auto tracing, users can monitor Mistral AI model interactions without manually instrumenting each API call. ^[tracing-mistral-databricks-on-aws.md]

## Overview

The [MLflow](/concepts/mlflow.md) Mistral Auto Tracing feature works by wrapping the Mistral AI client with [MLflow](/concepts/mlflow.md)'s tracing functionality. When enabled, it automatically logs key information from Mistral API calls, including request parameters, response data, and performance metrics, to an [MLflow Experiment](/concepts/mlflow-experiment.md). This provides visibility into how Mistral models are being used and how they perform. ^[tracing-mistral-databricks-on-aws.md]

## Enabling Auto Tracing

To enable auto tracing for Mistral AI, call `mlflow.mistral.autolog()` before creating a Mistral client instance. This function activates automatic instrumentation of the Mistral client, causing all subsequent API calls to be traced. ^[tracing-mistral-databricks-on-aws.md]

```python
import [[mlflow|MLflow]]

# Turn on auto tracing for Mistral AI
[[mlflow|MLflow]].mistral.autolog()
```

After calling `autolog()`, any [Mistral AI Client](/concepts/mistral-ai-python-sdk.md) operations performed within the same session are automatically traced. ^[tracing-mistral-databricks-on-aws.md]

## Configuration

After enabling auto tracing, you must configure the [MLflow tracking URI](/concepts/mlflow-tracking-uri.md) and experiment. For Databricks users, the tracking URI should be set to `"databricks"`. This ensures that [Traces](/concepts/traces.md) are logged to the Databricks workspace. ^[tracing-mistral-databricks-on-aws.md]

```python
[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/mistral-demo")
```

## Usage Example

The following example demonstrates a complete workflow with auto tracing enabled: ^[tracing-mistral-databricks-on-aws.md]

```python
import os
from mistralai import Mistral
import [[mlflow|MLflow]]

# Enable auto tracing
[[mlflow|MLflow]].mistral.autolog()

# Configure tracking
[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/mistral-demo")

# Create Mistral client
client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])

# Make an API call — automatically traced
chat_response = client.chat.complete(
    model="mistral-small-latest",
    messages=[
        {
            "role": "user",
            "content": "Who is the best French painter? Answer in one short sentence.",
        },
    ],
)

print(chat_response.choices[0].message)
```

In this example, the `client.chat.complete()` call is automatically traced by [MLflow](/concepts/mlflow.md). The trace captures details such as the model name, messages sent, response content, token usage, and latency. ^[tracing-mistral-databricks-on-aws.md]

## Supported Operations

The auto tracing feature captures [Traces](/concepts/traces.md) for Mistral AI API calls made through the Python client library. When enabled, it instruments the Mistral client to log each API interaction as a trace in [MLflow](/concepts/mlflow.md). This allows users to inspect and compare different model interactions. ^[tracing-mistral-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The core tracing infrastructure that captures and stores trace data.
- [MLflow Autologging](/concepts/mlflow-autologging.md) — The broader mechanism for automatically logging model metrics, parameters, and artifacts.
- [Mistral AI Client](/concepts/mistral-ai-python-sdk.md) — The Python client library for interacting with Mistral AI models.
- [Generative AI Tracing](/concepts/mlflow-genai-tracing.md) — Tracing support for various generative AI providers and models.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit where [Traces](/concepts/traces.md) and run data are stored.

## Sources

- tracing-mistral-databricks-on-aws.md

# Citations

1. [tracing-mistral-databricks-on-aws.md](/references/tracing-mistral-databricks-on-aws-6af10854.md)
