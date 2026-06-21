---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 55eeab4dad459c7fa344f56f29e947303cf7087db13ba24453fea4f1f959f65c
  pageDirectory: concepts
  sources:
    - automatic-tracing-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-compute-cluster-autolog-requirements
    - SCCAR
  citations:
    - file: automatic-tracing-databricks-on-aws.md
title: Serverless Compute Cluster Autolog Requirements
description: On Databricks serverless compute clusters, autologging for GenAI tracing frameworks is not automatically enabled and requires explicit calls to mlflow.<library>.autolog().
tags:
  - databricks
  - serverless
  - mlflow
  - configuration
timestamp: "2026-06-19T14:06:22.082Z"
---

# Serverless Compute Cluster Autolog Requirements

**Serverless Compute Cluster Autolog Requirements** describes the mandatory steps to enable [Automatic Tracing](/concepts/automatic-tracing.md) for GenAI applications running on Databricks serverless compute clusters. Unlike classic compute clusters, serverless clusters do not enable model autologging for tracing frameworks by default; users must explicitly activate it for each integration they wish to trace. ^[automatic-tracing-databricks-on-aws.md]

## Overview

[MLflow Tracing](/concepts/mlflow-tracing.md) provides visibility into the execution of generative AI applications by recording spans that capture LLM calls, tool invocations, and custom logic. On Databricks serverless compute clusters, the auto‑tracing feature for GenAI frameworks is **not automatically enabled**. To obtain traces, you must call the appropriate `mlflow.<library>.autolog()` function for each specific library or framework you are using (e.g., OpenAI, LangChain, Anthropic). ^[automatic-tracing-databricks-on-aws.md]

## Key Requirement

The core requirement is an explicit `autolog()` call for every integration you want to trace. For example:

```python
import mlflow
mlflow.openai.autolog()
```

This single line enables automatic tracing for all subsequent OpenAI calls made in the notebook or script. Without it, no spans are generated for that library on serverless compute. ^[automatic-tracing-databricks-on-aws.md]

## Prerequisites

To use automatic tracing on serverless compute clusters, the following conditions must be met:

- **MLflow 3 or later** is recommended for the latest GenAI tracing capabilities. ^[automatic-tracing-databricks-on-aws.md]
- The **`mlflow[databricks]>=3.1`** package must be installed to provide GenAI features and Databricks connectivity. ^[automatic-tracing-databricks-on-aws.md]
- **Integration‑specific SDKs** must be installed for the frameworks you intend to trace (e.g., `openai>=1.0.0`, `langchain`, `anthropic`, etc.). ^[automatic-tracing-databricks-on-aws.md]
- **LLM API credentials** must be configured, typically as environment variables (e.g., `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, or Databricks tokens when using Databricks Foundation Model APIs). ^[automatic-tracing-databricks-on-aws.md]

After installing the required packages, run `dbutils.library.restartPython()` in a Databricks notebook to refresh the Python environment. ^[automatic-tracing-databricks-on-aws.md]

## Enabling Autolog for Multiple Frameworks

Serverless compute clusters support auto‑tracing across more than [20 supported libraries and frameworks](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/). To trace multiple integrations, call `autolog()` for each one:

```python
mlflow.openai.autolog()
mlflow.langchain.autolog()
# Continue for other frameworks as needed
```

When multiple frameworks are used in the same agent, the traces are unified under a single parent span, enabling end‑to‑end visibility. ^[automatic-tracing-databricks-on-aws.md]

## Example

The following example demonstrates the minimum requirements for tracing an OpenAI agent on a serverless compute cluster:

```python
%pip install --upgrade "mlflow[databricks]>=3.1" openai>=1.0.0
dbutils.library.restartPython()

import mlflow
import os
from openai import OpenAI

# Explicitly enable autologging
mlflow.openai.autolog()

# Configure credentials
os.environ["OPENAI_API_KEY"] = "your-api-key"

# Set tracking URI and experiment (optional but recommended)
mlflow.set_tracking_uri("databricks")
mlflow.set_experiment("/Shared/my-experiment")

# Create client and make a traced call
client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "What is MLflow?"}]
)
print(response.choices[0].message.content)
```

After execution, a trace appears in the MLflow experiment containing spans for the OpenAI call. ^[automatic-tracing-databricks-on-aws.md]

## Related Concepts

- [Automatic Tracing](/concepts/automatic-tracing.md) — The general mechanism for instrumenting LLM calls without manual decorators.
- [MLflow GenAI Tracing](/concepts/mlflow-genai-tracing.md) — The full tracing system for generative AI applications.
- [Serverless Compute Clusters](/concepts/serverless-gpu-compute.md) — Databricks compute type where explicit autolog is required.
- [Manual Tracing with Decorators](/concepts/mlflowtrace-decorator.md) — Alternative approach using `@mlflow.trace` for custom spans.
- [Autologging](/concepts/mlflow-autologging.md) — MLflow’s broader model autologging feature (of which tracing autolog is a subset).

## Sources

- automatic-tracing-databricks-on-aws.md

# Citations

1. [automatic-tracing-databricks-on-aws.md](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
