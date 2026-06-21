---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9f8d5195bd886317de13d047e1afea46c4c120fd16d17cefb7b7343c860d4a94
  pageDirectory: concepts
  sources:
    - automatic-tracing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3-dependency-for-genai-tracing
    - M3DFGT
  citations:
    - file: automatic-tracing-databricks-on-aws.md
title: MLflow 3 Dependency for GenAI Tracing
description: Requirement for MLflow 3.x (specifically mlflow[databricks]>=3.1) to access the latest GenAI tracing capabilities, including automatic and manual tracing features.
tags:
  - mlflow
  - versioning
  - dependencies
  - setup
timestamp: "2026-06-19T22:10:56.475Z"
---

# MLflow 3 Dependency for GenAI Tracing

**MLflow 3 Dependency for GenAI Tracing** refers to the requirement that MLflow version 3.1 or higher be installed to enable the full set of generative AI (GenAI) tracing capabilities on Databricks. Automatic tracing of LLM calls, agent workflows, and multi-framework integrations depends on this version as a baseline.

## Overview

Databricks recommends MLflow 3 for the latest GenAI tracing features. To use automatic tracing with supported LLM frameworks, you must install the MLflow package with the `databricks` extra at version 3.1 or above. This version includes core GenAI functionality and Databricks connectivity required for tracing to work. ^[automatic-tracing-databricks-on-aws.md]

The required installation command is:

```python
%pip install --upgrade "mlflow[databricks]>=3.1"
```

This installs MLflow 3.1+ along with Databricks-specific integrations. You may also need to install additional SDKs depending on the LLM provider you want to trace (for example, `openai>=1.0.0`, `langchain`, `anthropic`, etc.). ^[automatic-tracing-databricks-on-aws.md]

## Why Version 3.1+ Is Required

MLflow 3.1 introduces the `mlflow.<library>.autolog()` API, which is the primary mechanism for enabling automatic tracing. The autolog functions for GenAI frameworks — such as `mlflow.openai.autolog()`, `mlflow.langchain.autolog()`, and integrations for 20+ other libraries — are only available starting with MLflow 3. ^[automatic-tracing-databricks-on-aws.md]

Without this version, calls to `mlflow.<library>.autolog()` will fail, and GenAI traces will not be generated automatically.

## Explicit Enablement on Serverless Compute

On serverless compute clusters, autologging for GenAI tracing frameworks is **not automatically enabled**, even with MLflow 3 installed. You must explicitly call the appropriate `mlflow.<library>.autolog()` function for each integration you want to trace. This is a key difference from standard Databricks compute, where autologging may be enabled by default. ^[automatic-tracing-databricks-on-aws.md]

## Usage Pattern

After installing MLflow 3.1+, the typical workflow is:

1. Install the MLflow package with the `databricks` extra.
2. Install any provider SDKs you need (OpenAI, LangChain, Anthropic, Mistral, etc.).
3. Set LLM API keys in environment variables.
4. Call `mlflow.set_tracking_uri("databricks")` to point to your Databricks workspace.
5. Call `mlflow.<library>.autolog()` to enable tracing for your chosen frameworks.
6. Run your GenAI application — traces are automatically captured.

Example for OpenAI:

```python
%pip install --upgrade "mlflow[databricks]>=3.1" openai>=1.0.0
dbutils.library.restartPython()

import mlflow
import os

os.environ["OPENAI_API_KEY"] = "your-api-key"
mlflow.set_tracking_uri("databricks")
mlflow.set_experiment("/Shared/my-experiment")
mlflow.openai.autolog()

# Now all OpenAI API calls are automatically traced
```

^[automatic-tracing-databricks-on-aws.md]

## Related Concepts

- [Automatic Tracing](/concepts/automatic-tracing.md) — The mechanism enabled by MLflow 3 autolog functions
- [Manual Tracing with Decorators](/concepts/mlflowtrace-decorator.md) — An alternative approach using `@mlflow.trace`
- [Supported Tracing Integrations](/concepts/mlflow-supported-tracing-libraries.md) — The 20+ libraries and frameworks compatible with automatic tracing
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — A compute type where autologging must be explicitly enabled
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for storing traces

## Sources

- automatic-tracing-databricks-on-aws.md

# Citations

1. [automatic-tracing-databricks-on-aws.md](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
