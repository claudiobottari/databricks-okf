---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2c6c236cde332afa09a97abb2543f77f348e85cfab2d5a5ad6736f37ed885e0a
  pageDirectory: concepts
  sources:
    - develop-code-based-scorers-databricks-on-aws.md
  confidence: 0.94
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-autologging-for-genai
    - MAFG
  citations:
    - file: develop-code-based-scorers-databricks-on-aws.md
title: MLflow Autologging for GenAI
description: Automatic instrumentation via mlflow.openai.autolog() that captures application execution traces (inputs, outputs) for use in MLflow Evaluation and monitoring.
tags:
  - MLflow
  - instrumentation
  - tracing
  - GenAI
timestamp: "2026-06-19T18:31:08.224Z"
---

# [MLflow Autologging](/concepts/mlflow-autologging.md) for GenAI

**MLflow Autologging for GenAI** is a feature of [MLflow](/concepts/mlflow.md) that automatically instruments generative AI applications with [MLflow Tracing](/concepts/mlflow-tracing.md), enabling developers to capture traces of model interactions without manual instrumentation. This capability is particularly useful during the development of code-based scorers for MLflow Evaluation for GenAI, as the recorded traces serve as inputs to evaluation metrics. ^[develop-code-based-scorers-databricks-on-aws.md]

## Overview

When enabled, [MLflow Autologging](/concepts/mlflow-autologging.md) for GenAI automatically records traces of API calls made through supported client libraries, such as the OpenAI client. These traces capture the inputs, outputs, and metadata of each interaction, providing a detailed record of the application's behavior. ^[develop-code-based-scorers-databricks-on-aws.md]

The primary use case for this feature is the iterative development of custom evaluation metrics. By generating traces once and then reusing them across multiple evaluation runs, developers can iterate on their scorers without needing to re-run the entire application each time. ^[develop-code-based-scorers-databricks-on-aws.md]

## Enabling Autologging

To enable autologging for OpenAI-based applications, call `mlflow.openai.autolog()` before making any API calls. This call automatically instruments the application with [MLflow Tracing](/concepts/mlflow-tracing.md). ^[develop-code-based-scorers-databricks-on-aws.md]

```python
import mlflow
mlflow.openai.autolog()
```

For applications running outside of Databricks, you must also set up MLflow tracking to a Databricks workspace using `mlflow.set_tracking_uri("databricks")`. In Databricks notebooks, the experiment defaults to the notebook experiment. ^[develop-code-based-scorers-databricks-on-aws.md]

## Developer Workflow

The recommended workflow for developing code-based scorers with autologging consists of four steps: ^[develop-code-based-scorers-databricks-on-aws.md]

1. **Define evaluation data** — Create a dataset of inputs for the application to process.
2. **Generate traces from your app** — Run `mlflow.genai.evaluate()` with a placeholder scorer to produce traces. The autologging instrumentation captures each interaction automatically.
3. **Query and store the resulting traces** — Use `mlflow.search_traces()` to retrieve the generated traces as a Pandas DataFrame.
4. **Iterate on your scorer** — Pass the stored traces DataFrame directly to `mlflow.genai.evaluate()` as the input dataset, allowing rapid iteration on metric logic without re-running the application.

## Trace Visualization

After generating traces, Databricks Notebooks display trace visualizations as part of cell results. The LLM's response generated during evaluation appears in the notebook Trace UI's **Outputs** field and in the MLflow Experiment UI's **Response** column. ^[develop-code-based-scorers-databricks-on-aws.md]

## Requirements

- `mlflow[databricks]` version 3.1 or later for the best GenAI experience. ^[develop-code-based-scorers-databricks-on-aws.md]
- The `openai` package for applications using the OpenAI client. ^[develop-code-based-scorers-databricks-on-aws.md]
- The `databricks-openai` package for connecting to Databricks-hosted LLMs. ^[develop-code-based-scorers-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The underlying instrumentation framework that captures trace data.
- MLflow Evaluation for GenAI — The evaluation framework that consumes traces for metric computation.
- [Code-based Scorers](/concepts/code-based-scorers.md) — Custom evaluation metrics that can be iterated on using stored traces.
- [MLflow experiments](/concepts/mlflow-experiment.md) — The organizational unit where traces and evaluation results are stored.
- mlflow.search_traces()|MLflow search_traces — The API used to retrieve stored traces for reuse.

## Sources

- develop-code-based-scorers-databricks-on-aws.md

# Citations

1. [develop-code-based-scorers-databricks-on-aws.md](/references/develop-code-based-scorers-databricks-on-aws-4fba7668.md)
