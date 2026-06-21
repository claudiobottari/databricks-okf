---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7b3fccdd361d901d86d4f0f684bd254f0c86b48a35f97c767c8e00e6d1ad791e
  pageDirectory: concepts
  sources:
    - automatic-tracing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3-prerequisites-for-genai-tracing
    - M3PFGT
  citations:
    - file: automatic-tracing-databricks-on-aws.md
title: MLflow 3 Prerequisites for GenAI Tracing
description: System and package requirements for using MLflow 3's GenAI tracing capabilities, including mlflow[databricks]>=3.1 and framework-specific SDKs.
tags:
  - mlflow
  - setup
  - prerequisites
timestamp: "2026-06-19T09:06:05.420Z"
---

# MLflow 3 Prerequisites for GenAI Tracing

**MLflow 3 Prerequisites for GenAI Tracing** describes the software and configuration requirements needed to enable automatic tracing of generative AI applications using MLflow 3. Databricks recommends MLflow 3 for the latest [GenAI Tracing](/concepts/mlflow-genai-tracing.md) capabilities. ^[automatic-tracing-databricks-on-aws.md]

## MLflow Version Requirement

Install the MLflow package with Databricks support and GenAI features. The recommended minimum version is:

```
mlflow[databricks]>=3.1
```

This package provides core MLflow functionality, GenAI tracing features, and Databricks connectivity. ^[automatic-tracing-databricks-on-aws.md]

## Integration-Specific Packages

You must also install the SDK for each LLM provider or framework you intend to trace. For example, to use the OpenAI integration:

```
openai>=1.0.0
```

Additional libraries (e.g., `langchain`, `anthropic`) should be installed as needed for the specific integrations you want to trace. ^[automatic-tracing-databricks-on-aws.md]

## Installation Command

Run the following in a Databricks notebook (or similar environment) to install the basic requirements:

```python
%pip install --upgrade "mlflow[databricks]>=3.1" openai>=1.0.0
# Also install libraries you want to trace (langchain, anthropic, etc.)
dbutils.library.restartPython()
```

The `dbutils.library.restartPython()` call ensures the newly installed packages are available in the current session. ^[automatic-tracing-databricks-on-aws.md]

## Credential Configuration

Set any necessary LLM API keys as environment variables before enabling autologging. For example, in a Databricks notebook:

```python
import os
os.environ["OPENAI_API_KEY"] = "your-api-key"
# Add other provider keys as needed
# os.environ["ANTHROPIC_API_KEY"] = "your-api-key"
# os.environ["MISTRAL_API_KEY"] = "your-api-key"
```

When using Databricks Foundation Model APIs, you can rely on Databricks authentication by setting the tracking URI to `"databricks"`. ^[automatic-tracing-databricks-on-aws.md]

## Serverless Compute Cluster Note

On serverless compute clusters, autologging for GenAI tracing frameworks is **not automatically enabled**. You must explicitly enable autologging by calling the appropriate `mlflow.<library>.autolog()` function for the specific integrations you want to trace. ^[automatic-tracing-databricks-on-aws.md]

## Related Concepts

- [Automatic Tracing](/concepts/automatic-tracing.md) – How to add one line of code to trace GenAI apps.
- [Manual Tracing with Decorators](/concepts/mlflowtrace-decorator.md) – Adding custom spans to auto-traced workflows.
- [Supported Tracing Integrations](/concepts/mlflow-supported-tracing-libraries.md) – 20+ libraries and frameworks supported out of the box.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – Pre-built runtime with MLflow and GPU support.
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – Overview of MLflow’s generative AI features.

## Sources

- automatic-tracing-databricks-on-aws.md

# Citations

1. [automatic-tracing-databricks-on-aws.md](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
