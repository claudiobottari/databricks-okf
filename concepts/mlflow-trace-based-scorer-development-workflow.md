---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c84add93aa0f72cb7f3fea963e6c97f08401ea5630a65b8ac158cc485a3e034c
  pageDirectory: concepts
  sources:
    - develop-code-based-scorers-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-based-scorer-development-workflow
    - MTSDW
    - code-based scorer development workflow
  citations:
    - file: develop-code-based-scorers-databricks-on-aws.md
title: MLflow Trace-based Scorer Development Workflow
description: "A four-step iterative workflow for developing scorers: define evaluation data, generate traces, store traces, then iterate on scorers without rerunning the application."
tags:
  - mlflow
  - workflow
  - development
  - tracing
timestamp: "2026-06-18T15:27:29.221Z"
---

# MLflow Trace-based Scorer Development Workflow

The **MLflow Trace-based Scorer Development Workflow** is an iterative development methodology for custom [Code-based Scorers](/concepts/code-based-scorers.md) in MLflow Evaluation for GenAI. It allows developers to generate execution traces from their application once, then repeatedly evaluate new versions of scorers against those stored traces without re‑running the full application. This decouples scorer development from the application runtime, enabling faster iteration cycles.^[develop-code-based-scorers-databricks-on-aws.md]

## Overview

When developing custom scorers, developers often need to refine scoring logic, adjust thresholds, or test new metrics. The standard approach — running the full application for each change — can be slow and resource‑intensive. The trace‑based workflow addresses this by:

1. Defining evaluation data (a set of prompts or conversations).
2. Generating [[MLflow Trace|MLflow Traces]] by running the application once against that data.
3. Storing the traces in a local variable for reuse.
4. Iterating on the scorer and evaluating it against the stored traces using `mlflow.genai.evaluate()`.

This approach ensures that the scoring logic can be adjusted, corrected, or extended without waiting for the underlying application to regenerate output each time.^[develop-code-based-scorers-databricks-on-aws.md]

## Prerequisites: Set up MLflow and define your application

Before starting, install the latest version of `mlflow[databricks]` and any additional dependencies (e.g., `openai` if using an OpenAI client). Enable [MLflow Autologging](/concepts/mlflow-autologging.md) for the OpenAI client (via `mlflow.openai.autolog()`) to automatically instrument application calls and capture traces. If running outside Databricks, set the tracking URI to a Databricks workspace; inside a Databricks notebook, the experiment defaults to the notebook’s experiment.^[develop-code-based-scorers-databricks-on-aws.md]

A simple application, such as a question‑answering function using a Databricks‑hosted LLM, is defined. The function is decorated with `@mlflow.trace` so that every invocation produces a trace.^[develop-code-based-scorers-databricks-on-aws.md]

## Step 1: Define evaluation data

The evaluation data is a list of dictionaries, each containing an `inputs` key with the messages that will be sent to the application. For a chat‑based assistant, this might be a list of conversation turns. The data can include simple single‑turn questions or multi‑turn dialogues.^[develop-code-based-scorers-databricks-on-aws.md]

## Step 2: Generate traces from your app

Use `mlflow.genai.evaluate()` to run the application against the evaluation data. Because `evaluate()` requires at least one scorer, define a placeholder scorer (e.g., a `@scorer` function that returns a constant integer) for this initial run. The evaluation produces one trace for each row of the dataset. These traces are visible in the MLflow Experiment UI and in Databricks notebook cell results.^[develop-code-based-scorers-databricks-on-aws.md]

## Step 3: Query and store the resulting traces

After the evaluation run, retrieve the traces using `mlflow.search_traces(run_id=eval_results.run_id)`. This returns a Pandas DataFrame containing all traces generated during that evaluation. Store this DataFrame in a local variable for later use.^[develop-code-based-scorers-databricks-on-aws.md]

## Step 4: Iterate on the scorer and evaluate using stored traces

Define the actual scorer using the `@scorer` decorator, implementing the metric logic (e.g., response length, keyword presence, or any custom computation). Then call `mlflow.genai.evaluate()` passing the stored DataFrame as the `data` parameter and the new scorer in the `scorers` list. **Do not provide a `predict_fn`** — the traces already contain the application’s outputs. This allows rapid iteration: modify the scorer code, re‑evaluate against the same traces, and compare results without regenerating application outputs.^[develop-code-based-scorers-databricks-on-aws.md]

## Example notebook

The source material includes an example notebook that contains all the code from the tutorial.^[develop-code-based-scorers-databricks-on-aws.md]

## Next steps

After mastering the trace‑based workflow, developers can:

- Explore the Code-based scorer reference for detailed API documentation (signatures, inputs, outputs, error handling, secrets access).
- Use [Custom LLM Judges](/concepts/custom-llm-judges.md) for semantic evaluation via LLM‑as‑a‑judge metrics.
- Deploy scorers to [Production Monitoring](/concepts/production-monitoring.md) for continuous evaluation.
- Build comprehensive [Evaluation Datasets](/concepts/evaluation-datasets.md).^[develop-code-based-scorers-databricks-on-aws.md]

## Related Concepts

- MLflow Evaluation for GenAI
- [Custom scorers](/concepts/custom-scorers-mlflow-genai.md)
- [[MLflow Trace|MLflow Traces]]
- mlflow.search_traces()
- Pandas DataFrame
- [Autologging](/concepts/mlflow-autologging.md)
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)

## Sources

- develop-code-based-scorers-databricks-on-aws.md

# Citations

1. [develop-code-based-scorers-databricks-on-aws.md](/references/develop-code-based-scorers-databricks-on-aws-4fba7668.md)
