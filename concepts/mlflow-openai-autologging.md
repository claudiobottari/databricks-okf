---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b407026cb47fc5323605bc2083d56481f4bbab524df489993a5dbb4ee36ca090
  pageDirectory: concepts
  sources:
    - develop-code-based-scorers-databricks-on-aws.md
    - tutorial-trace-and-analyze-users-and-environments-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-openai-autologging
    - MOA
    - OpenAI Autologging
    - OpenAI autologging
    - OpenAI Autolog
    - OpenAI autolog
  citations:
    - file: develop-code-based-scorers-databricks-on-aws.md
    - file: tutorial-trace-and-analyze-users-and-environments-databricks-on-aws.md
title: MLflow OpenAI Autologging
description: Automatic instrumentation of OpenAI client calls via mlflow.openai.autolog() to capture traces for GenAI evaluation.
tags:
  - mlflow
  - openai
  - tracing
  - autolog
timestamp: "2026-06-19T15:11:44.797Z"
---

# MLflow OpenAI Autologging

**MLflow OpenAI Autologging** is a feature of MLflow that automatically instruments applications using the OpenAI Python client, capturing trace data for every call made through the client. It is enabled by calling `mlflow.openai.autolog()` and is a key tool for observability in GenAI applications.

## Overview

When `mlflow.openai.autolog()` is called, MLflow automatically records MLflow Traces for all subsequent OpenAI API calls made within the application. This includes the inputs (prompts, messages), outputs (responses), execution duration, and any errors that occur. ^[develop-code-based-scorers-databricks-on-aws.md, tutorial-trace-and-analyze-users-and-environments-databricks-on-aws.md]

Autologging is particularly useful during development and evaluation of GenAI applications. The generated traces can later be used as inputs to scorers for evaluation, allowing developers to iterate on metrics without re-running the application. ^[develop-code-based-scorers-databricks-on-aws.md]

## Enabling Autologging

To enable OpenAI autologging, call `mlflow.openai.autolog()` before making any OpenAI API calls. This works with any OpenAI client, including the `DatabricksOpenAI` client used to connect to Databricks-hosted foundation models. ^[develop-code-based-scorers-databricks-on-aws.md, tutorial-trace-and-analyze-users-and-environments-databricks-on-aws.md]

```python
import mlflow
mlflow.openai.autolog()
```

The autologging is typically combined with the `@mlflow.trace` decorator on application functions to create a complete trace hierarchy. Autologging captures the internal OpenAI call, while the decorator traces the higher-level application logic. ^[tutorial-trace-and-analyze-users-and-environments-databricks-on-aws.md]

## Usage in Development Workflow

In the code-based scorer development workflow, `mlflow.openai.autolog()` is used during the initial trace generation phase. After setting up autologging, the application is run against an evaluation dataset using `mlflow.genai.evaluate()`. The resulting traces are stored and can be queried using `mlflow.search_traces()`. Developers can then iterate on their scorers by passing the stored traces directly to `evaluate()`, without needing to re-run the application. ^[develop-code-based-scorers-databricks-on-aws.md]

## Requirements

The `mlflow[databricks]` package should be updated to version 3.1 or later for the best GenAI experience. The `openai` Python package is also required when using the OpenAI client. ^[develop-code-based-scorers-databricks-on-aws.md]

```python
%pip install -q --upgrade "mlflow[databricks]>=3.1" openai
```

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The underlying tracing framework that captures execution data.
- [MLflow GenAI Evaluate](/concepts/mlflow-genai-evaluation.md) – Evaluation function that uses traces for metrics computation.
- [Code-based Scorers](/concepts/code-based-scorers.md) – Custom metrics evaluated against stored traces.
- mlflow.search_traces() API|Search Traces Programmatically – Querying traces using `mlflow.search_traces()`.
- [Add Context to Traces](/concepts/best-practices-for-adding-context-to-mlflow-traces.md) – Enhancing traces with custom metadata and tags using `mlflow.update_current_trace()`.
- [Databricks-hosted foundation models](/concepts/databricks-hosted-foundation-models.md) – Models accessible through the Databricks OpenAI client.

## Sources

- develop-code-based-scorers-databricks-on-aws.md
- tutorial-trace-and-analyze-users-and-environments-databricks-on-aws.md

# Citations

1. [develop-code-based-scorers-databricks-on-aws.md](/references/develop-code-based-scorers-databricks-on-aws-4fba7668.md)
2. [tutorial-trace-and-analyze-users-and-environments-databricks-on-aws.md](/references/tutorial-trace-and-analyze-users-and-environments-databricks-on-aws-7504deef.md)
