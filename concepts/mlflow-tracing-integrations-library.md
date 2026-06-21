---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3f5eca1d21cff88f0b31bb19256e4d8a7f76c13c2f49efe41a4e6da4f60e48bf
  pageDirectory: concepts
  sources:
    - get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-integrations-library
    - MTIL
  citations:
    - file: get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md
title: MLflow Tracing integrations library
description: A collection of 20+ pre-built library integrations that provide automatic tracing for popular frameworks used in GenAI applications.
tags:
  - mlflow
  - tracing
  - integrations
  - libraries
timestamp: "2026-06-19T18:59:42.219Z"
---

# [MLflow Tracing](/concepts/mlflow-tracing.md) integrations library

The **MLflow Tracing integrations library** is a collection of automatic instrumentation hooks that add [MLflow Tracing](/concepts/mlflow-tracing.md) to over 20 popular libraries used in GenAI application development. It is one of the primary resources for adding tracing to an application, alongside the manual tracing guide. ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

## Overview

When building GenAI applications—such as RAG systems or multi-step agents—developers often rely on external SDKs and frameworks. The integrations library provides "automatic tracing integrations" for these libraries, meaning that after enabling the integration, all calls made through the library are automatically captured as trace spans. This eliminates the need to manually add tracing code for each interaction. ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

## Usage

To instrument an application, a developer can refer to the integrations guide after setting up their environment. For example, using `mlflow.openai.autolog()` automatically traces all calls made with the OpenAI Python client. The same pattern is available for the other supported libraries. Detailed instructions for each integration are provided in the [MLflow Tracing](/concepts/mlflow-tracing.md) integrations documentation](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/). ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

## Benefits

Using the integrations library gives developers immediate insight into the behavior of their application, including:

- What inputs were sent to each library call.
- What outputs were returned.
- Latency and timing information.
- Token usage (where applicable, e.g., for LLM calls).

For complex multi-step applications, these automatic traces reveal the inner workings of each component without requiring manual annotation. ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

## Related concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The core tracing framework that the integrations library feeds into.
- [MLflow autolog](/concepts/mlflow-autologging.md) – The mechanism used by many integrations to automatically capture traces.
- [MLflow experiments](/concepts/mlflow-experiment.md) – The organizational container where traces are stored.
- [GenAI applications on Databricks](/concepts/genai-app-evaluation-workflow-on-databricks.md) – The typical use case for the integrations library.

## Sources

- get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md

# Citations

1. [get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md](/references/get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws-860f2761.md)
