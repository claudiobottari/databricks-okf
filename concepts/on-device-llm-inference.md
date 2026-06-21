---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 87ee93c591ff5cc79f7209a97ae60ea0627100f578eaf20fe6febd428466fb28
  pageDirectory: concepts
  sources:
    - tracing-ollama-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - on-device-llm-inference
    - OLI
  citations:
    - file: tracing-ollama-databricks-on-aws.md
title: On-Device LLM Inference
description: The paradigm of running large language models locally on user devices rather than relying on cloud-hosted inference APIs, with privacy and latency benefits.
tags:
  - llm
  - local-inference
  - privacy
  - edge-computing
timestamp: "2026-06-19T23:12:55.795Z"
---

# On-Device LLM Inference

**On-Device LLM Inference** refers to running large language models (LLMs) directly on a user's local hardware rather than on remote cloud servers. This approach enables private, offline-capable AI applications by executing model inference on devices such as laptops, desktops, or edge hardware.

## Overview

On-device LLM inference allows users to run LLMs locally without sending data to external APIs. This provides benefits in privacy, latency, and offline availability. Platforms like [Ollama](/concepts/ollama.md) serve as infrastructure for running LLMs locally, supporting models such as Llama 3.2, Gemma 2, Mistral, and Code Llama.^[tracing-ollama-databricks-on-aws.md]

## Integration with [MLflow Tracing](/concepts/mlflow-tracing.md)

On-device LLM inference can be monitored and debugged using [MLflow Tracing](/concepts/mlflow-tracing.md). Since local LLM endpoints served by [Ollama](/concepts/ollama.md) are compatible with the OpenAI API, users can enable tracing for [Ollama](/concepts/ollama.md) by calling `mlflow.openai.autolog()`. Any LLM interactions via [Ollama](/concepts/ollama.md) will then be recorded to the active [MLflow Experiment](/concepts/mlflow-experiment.md).^[tracing-ollama-databricks-on-aws.md]

### Enabling Tracing

To enable tracing for on-device LLM inference with [Ollama](/concepts/ollama.md):

```python
import [[mlflow|MLflow]]

# Enable auto-tracing for OpenAI SDK
[[mlflow|MLflow]].openai.autolog()

# Set up [[mlflow-tracking|MLflow Tracking]] on Databricks
[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/ollama-demo")
```

^[tracing-ollama-databricks-on-aws.md]

**Note:** On serverless compute clusters, [Autologging for GenAI Tracing](/concepts/autologging-for-genai-tracing.md) frameworks is not automatically enabled. You must explicitly enable autologging by calling the appropriate `mlflow.<library>.autolog()` function for the specific integrations you want to trace.^[tracing-ollama-databricks-on-aws.md]

### Querying a Local Model

To query a locally running LLM through [Ollama](/concepts/ollama.md) and capture [Traces](/concepts/traces.md):

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",  # The local [[ollama|Ollama]] REST endpoint
    api_key="dummy",  # Required to instantiate OpenAI client, it can be a random string
)

response = client.chat.completions.create(
    model="llama3.2:1b",
    messages=[
        {"role": "system", "content": "You are a science teacher."},
        {"role": "user", "content": "Why is the sky blue?"},
    ],
)
```

^[tracing-ollama-databricks-on-aws.md]

### Disabling Tracing

Auto tracing for on-device LLM inference can be disabled globally by calling `mlflow.openai.autolog(disable=True)` or `mlflow.autolog(disable=True)`.^[tracing-ollama-databricks-on-aws.md]

## Use Cases

- **Privacy-sensitive applications:** Data never leaves the local device.
- **Offline environments:** No internet connection required for inference.
- **Development and testing:** Prototype locally before deploying to production.

## Related Concepts

- [Ollama](/concepts/ollama.md) — Open-source platform for running LLMs locally.
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Framework for capturing and organizing trace data.
- Local LLM Deployment — Running models on edge or personal devices.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — Cloud-based alternative for GPU-accelerated inference.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) — Serverless GPU setup for large model workloads.

## Sources

- tracing-ollama-databricks-on-aws.md

# Citations

1. [tracing-ollama-databricks-on-aws.md](/references/tracing-ollama-databricks-on-aws-d0fc7add.md)
