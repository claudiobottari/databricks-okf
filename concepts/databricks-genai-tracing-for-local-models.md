---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f89ed36fb1d04c584906148b99b1095ffc0bb27f9dc1c54d93ff12aa8df6773f
  pageDirectory: concepts
  sources:
    - tracing-ollama-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-genai-tracing-for-local-models
    - DGTFLM
  citations:
    - file: tracing-ollama-databricks-on-aws.md
title: Databricks GenAI Tracing for Local Models
description: Pattern for tracing locally-run Ollama models within Databricks by setting the MLflow tracking URI to 'databricks' and enabling OpenAI autologging on serverless compute clusters.
tags:
  - databricks
  - tracing
  - genai
  - mlflow
timestamp: "2026-06-19T23:12:51.239Z"
---

Here is the wiki page for "Databricks GenAI Tracing for Local Models".

## Databricks GenAI Tracing for Local Models

**Databricks GenAI Tracing for Local Models** refers to the capability to capture and record trace data from large language models (LLMs) running on local infrastructure, such as a developer’s workstation, and ingest those [Traces](/concepts/traces.md) into [MLflow Experiments](/concepts/mlflow.md) on Databricks for observability and debugging. This capability is primarily demonstrated through support for [Ollama](/concepts/ollama.md), an open-source platform that serves local LLMs via an API compatible with the OpenAI API.

### Overview

[Ollama](/concepts/ollama.md) allows users to run LLMs like Llama 3.2, Gemma 2, Mistral, and Code Llama locally on their own devices. Because [Ollama](/concepts/ollama.md)'s local endpoint is compatible with the OpenAI API, tracing is enabled through `mlflow.openai.autolog()`. Once autologging is active, any LLM interaction made through the OpenAI SDK against a local [Ollama](/concepts/ollama.md) endpoint is automatically recorded as a trace in the currently active [MLflow Experiment](/concepts/mlflow-experiment.md) on Databricks. ^[tracing-ollama-databricks-on-aws.md]

### Enabling Tracing with Autolog

To trace local model interactions:

1.  Run the [Ollama](/concepts/ollama.md) server with your desired LLM model.
2.  Enable auto-tracing for the OpenAI SDK by calling `mlflow.openai.autolog()`.
3.  Set up the [MLflow tracking URI](/concepts/mlflow-tracking-uri.md) to point to Databricks and select or create an experiment.

After these steps, any `client.chat.completions.create()` call made against the local [Ollama](/concepts/ollama.md) endpoint (`http://localhost:11434/v1`) will be automatically traced and visible in the [MLflow](/concepts/mlflow.md) UI. The API key provided to the OpenAI client is a dummy string (e.g., `"dummy"`); [Ollama](/concepts/ollama.md) does not require a real API key. ^[tracing-ollama-databricks-on-aws.md]

### Important Considerations

On [serverless compute clusters](/concepts/serverless-gpu-compute.md), [Autologging for GenAI Tracing](/concepts/autologging-for-genai-tracing.md) frameworks is **not** automatically enabled. You must explicitly call the appropriate `mlflow.<library>.autolog()` function for each integration you want to trace. ^[tracing-ollama-databricks-on-aws.md]

### Disabling Auto-Tracing

Auto-tracing for [Ollama](/concepts/ollama.md) can be disabled globally by calling `mlflow.openai.autolog(disable=True)` or `mlflow.autolog(disable=True)`. ^[tracing-ollama-databricks-on-aws.md]

### Related Concepts

- [Ollama](/concepts/ollama.md)
- [MLflow Tracking](/concepts/mlflow-tracking.md)
- [GenAI Tracing](/concepts/mlflow-genai-tracing.md)
- OpenAI API
- [Local Model Serving](/concepts/local-model-serving-simulation.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)

## Sources

- tracing-ollama-databricks-on-aws.md

# Citations

1. [tracing-ollama-databricks-on-aws.md](/references/tracing-ollama-databricks-on-aws-d0fc7add.md)
