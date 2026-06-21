---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1badc7a90cc6362a72b5999dcc1624b736762cbcac1b2932d618cd4aa8af2e73
  pageDirectory: concepts
  sources:
    - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-openai-autologging-and-tracing
    - Tracing and MLflow OpenAI Autologging
    - MOAAT
  citations:
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
      start: 17
      end: 18
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
      start: 17
      end: 22
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
      start: 49
      end: 55
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
      start: 30
      end: 33
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
      start: 49
      end: 59
title: MLflow OpenAI Autologging and Tracing
description: Automatic instrumentation of OpenAI API calls via mlflow.openai.autolog() and @mlflow.trace decorator for capturing LLM request/response traces during evaluation.
tags:
  - mlflow
  - tracing
  - observability
timestamp: "2026-06-19T13:49:32.653Z"
---

# MLflow OpenAI Autologging and Tracing

**MLflow OpenAI Autologging and Tracing** refers to the automated instrumentation of OpenAI API calls and the use of the `@mlflow.trace` decorator to capture execution traces for GenAI applications built with the OpenAI SDK or compatible endpoints.

## Overview

MLflow provides a `mlflow.openai.autolog()` method that enables automatic tracing of calls made through the OpenAI Python client. When activated, MLflow records the inputs, outputs, and metadata of OpenAI API requests without requiring manual instrumentation. This tracing is part of the broader [MLflow Tracing](/concepts/mlflow-tracing.md) system for GenAI applications.^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md#L17-L18]

## Enabling OpenAI Autologging

To enable automatic tracing, call `mlflow.openai.autolog()` before making any OpenAI API requests. The following example shows the typical setup:

```python
import mlflow
from openai import OpenAI

mlflow.openai.autolog()
```

After autologging is enabled, every subsequent OpenAI client call (e.g., `client.chat.completions.create()`) is automatically traced and its details are recorded in the active MLflow trace.^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md#L17-L22]

## Tracing with `@mlflow.trace`

Custom Python functions that orchestrate LLM calls can be further instrumented using the `@mlflow.trace` decorator. This decorator records the function’s inputs and outputs as a trace span, providing a richer view of the application’s execution flow beyond the raw API calls.

```python
@mlflow.trace
def generate_game(template: str):
    response = client.chat.completions.create(...)
    return response.choices[0].message.content
```

Using `@mlflow.trace` alongside `mlflow.openai.autolog()` allows developers to see both the high‑level function call and the underlying OpenAI API request within the same trace.^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md#L49-L55]

## Viewing Traces

Traces captured through autologging and the `@mlflow.trace` decorator can be inspected directly in the notebook output or in the MLflow Experiment UI. This visibility is especially useful during the evaluation and iterative refinement of GenAI applications.^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md#L30-L33]

## Relation to GenAI Evaluation

Automatic tracing and the `@mlflow.trace` decorator are commonly used together with `mlflow.genai.evaluate()` to assess and compare GenAI application behavior across different prompts or configurations. The recorded traces provide a detailed context that evaluators, such as [Custom Judges](/concepts/custom-judges.md), can use to assess not only final outputs but also intermediate reasoning and tool usage.^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md#L49-L59]

## Related Concepts

- [MLflow Autologging](/concepts/mlflow-autologging.md) – General autologging support for other frameworks (e.g., scikit-learn, PyTorch).
- [MLflow Tracing](/concepts/mlflow-tracing.md) – The underlying trace capture system for GenAI.
- [GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – Using MLflow to evaluate and compare GenAI applications.
- OpenAI SDK Integration – How MLflow integrates with the OpenAI Python client.

## Sources

- 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md

# Citations

1. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md:17-18](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
2. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md:17-22](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
3. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md:49-55](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
4. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md:30-33](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
5. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md:49-59](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
