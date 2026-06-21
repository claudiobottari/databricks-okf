---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 65debac87f372ee7a359a65658c9bba6a941b4279bdb63b0d6b052b5c873d217
  pageDirectory: concepts
  sources:
    - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-for-llms
    - MTFL
  citations:
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
    - file: tracing-litellm-databricks-on-aws.md
title: MLflow Tracing for LLMs
description: Automatic instrumentation of LLM API calls using mlflow.openai.autolog() and @mlflow.trace decorator to capture inputs, outputs, and metadata for observability.
tags:
  - mlflow
  - observability
  - llm-tracing
timestamp: "2026-06-19T17:23:00.663Z"
---

```yaml
---
title: [[mlflow-tracing|MLflow Tracing]] for LLMs
summary: Automatic instrumentation of LLM calls using mlflow.openai.autolog() and @mlflow.trace to capture inputs, outputs, and metadata for observability.
sources:
  - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
  - tracing-litellm-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T08:47:08.459Z"
updatedAt: "2026-06-19T08:47:08.459Z"
tags:
  - mlflow
  - tracing
  - observability
aliases:
  - mlflow-tracing-for-llms
  - MTFL
confidence: 0.95
provenanceState: merged
inferredParagraphs: 0
---

# [[mlflow-tracing|MLflow Tracing]] for LLMs

**MLflow Tracing** is a feature of [[MLflow]] that captures detailed execution traces for [[Large language models (LLMs) on Databricks|Large Language Model (LLM)]] applications, recording information about API calls, prompts, responses, latencies, token usage, and other metadata. This enables developers to debug, observe, and analyze the behavior of GenAI applications during development and production.

## Overview

[[mlflow-tracing|MLflow Tracing]] provides automatic instrumentation for popular LLM frameworks and providers, capturing trace data without requiring manual instrumentation of each API call. Traces are logged to the active [[MLflow Experiment]], making them available for review in the MLflow UI alongside evaluation results and other experiment metadata.^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md, tracing-litellm-databricks-on-aws.md]

## How Tracing Works

[[mlflow-tracing|MLflow Tracing]] works by wrapping LLM API calls with span tracking. Each trace captures:

- **Prompts and completion responses** — The input sent to the model and the output it returns.^[tracing-litellm-databricks-on-aws.md]
- **Latencies** — How long each API call takes.^[tracing-litellm-databricks-on-aws.md]
- **Metadata** — Information about the LLM provider, such as model name and endpoint URL.^[tracing-litellm-databricks-on-aws.md]
- **Token usage and cost** — The number of tokens consumed and estimated billing.^[tracing-litellm-databricks-on-aws.md]
- **Cache hits** — Whether a response was served from a cache.^[tracing-litellm-databricks-on-aws.md]
- **Exceptions** — Any errors raised during the call.^[tracing-litellm-databricks-on-aws.md]

## Enabling Tracing

### Automatic Tracing with `mlflow.openai.autolog()`

For applications using the OpenAI Python client, you can enable automatic tracing by calling `mlflow.openai.autolog()` at the start of your notebook or script. This captures all subsequent calls to the OpenAI API, including chat completions, embedding requests, and image generations. The call must be made before any API calls are executed.^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

```python
mlflow.openai.autolog()
```

After this call, every interaction through the OpenAI client is automatically traced without needing to wrap individual functions.^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### Automatic Tracing with `@mlflow.trace` Decorator

For custom functions that call an LLM (either directly or through a wrapper), you can enable tracing by decorating the function with `@mlflow.trace`:^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

```python
@mlflow.trace
def generate_game(template: str):
    response = client.chat.completions.create(
        model="databricks-claude-sonnet-4-5",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": template},
        ],
    )
    return response.choices[0].message.content
```

This captures traces for every invocation of the decorated function, including the inputs, outputs, and any child LLM calls made within the function.^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### Automatic Tracing for LiteLLM

LiteLLM is an open-source LLM Gateway that provides a unified interface for accessing 100+ LLMs. MLflow provides automatic tracing for LiteLLM through the `mlflow.litellm.autolog()` function.^[tracing-litellm-databricks-on-aws.md]

```python
import mlflow
import litellm

# Enable auto-tracing for LiteLLM
mlflow.litellm.autolog()

# Set up MLflow tracking on Databricks
mlflow.set_tracking_uri("databricks")
mlflow.set_experiment("/Shared/litellm-demo")

# Call an LLM using LiteLLM
response = litellm.completion(
    model="claude-3-5-sonnet-20241022",
    messages=[{"role": "user", "content": "Hey! how's it going?"}],
)
```

[[mlflow-tracing|MLflow Tracing]] supports both synchronous and asynchronous LiteLLM APIs, as well as streaming responses. For streaming, MLflow records the concatenated output from stream chunks as a span output.^[tracing-litellm-databricks-on-aws.md]

### On Serverless Compute

On serverless compute clusters, autologging is not automatically enabled. You must explicitly call `mlflow.litellm.autolog()` to enable automatic tracing for LiteLLM integrations.^[tracing-litellm-databricks-on-aws.md]

## Disabling Tracing

Auto-tracing for LiteLLM can be disabled globally by calling `mlflow.litellm.autolog(disable=True)` or `mlflow.autolog(disable=True)`.^[tracing-litellm-databricks-on-aws.md]

## Viewing Traces

Traces can be viewed in the MLflow UI, accessible from within notebooks or through the Experiments sidebar. The Trace UI allows you to inspect individual spans, review inputs and outputs, and analyze performance metrics.^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

When using the `@mlflow.trace` decorator in a Databricks notebook, trace information appears inline in the cell output, providing immediate visibility into LLM interactions.^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Use Cases

- **Debugging** — Inspect exact prompts and responses to diagnose unexpected model behavior.
- **Observability** — Monitor latency and token usage to understand cost and performance characteristics of your application.
- **Evaluation** — Combine tracing with [[MLflow Evaluation UI|MLflow Evaluation]] to measure the quality of LLM outputs alongside execution metadata.
- **Iterative development** — Compare traces across different prompt versions and configurations to refine application behavior.

## Related Concepts

- [[MLflow Evaluation UI|MLflow Evaluation]] — Measuring the quality of GenAI application outputs
- [[MLflow Experiment|MLflow Experiments]] — Organizing runs, traces, and evaluation results
- LiteLLM — A unified LLM gateway that integrates with [[mlflow-tracing|MLflow Tracing]]
- [[MLflow Autologging|MLflow Autolog]] — General automatic logging for ML frameworks
- [[GenAI Agent Observability|GenAI Agents]] — Applications that can benefit from trace-based debugging

## Sources

- 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
- tracing-litellm-databricks-on-aws.md
```

# Citations

1. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
2. [tracing-litellm-databricks-on-aws.md](/references/tracing-litellm-databricks-on-aws-7988ec5e.md)
