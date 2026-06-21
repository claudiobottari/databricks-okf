---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c8edafd2b4fe06a5e387e7dd4016ac74039d3e754f9b101aa464309050030521
  pageDirectory: concepts
  sources:
    - develop-code-based-scorers-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - reusing-stored-traces-for-scorer-iteration
    - RSTFSI
  citations:
    - file: develop-code-based-scorers-databricks-on-aws.md
title: Reusing Stored Traces for Scorer Iteration
description: Technique of passing a Pandas DataFrame of precomputed traces directly to mlflow.genai.evaluate() as the input dataset, allowing scorer iteration without re-running the original application.
tags:
  - mlflow
  - optimization
  - workflow
  - evaluation
timestamp: "2026-06-19T10:14:14.653Z"
---

# Reusing Stored Traces for Scorer Iteration

**Reusing Stored Traces for Scorer Iteration** is a development workflow in MLflow Evaluation for GenAI that allows you to iterate on [Code-based Scorers](/concepts/code-based-scorers.md) without re-running your entire application. By storing traces from a single application run and reusing them across multiple scorer iterations, you can significantly speed up the evaluation cycle.

## Overview

When developing custom scorers for evaluating GenAI agents or applications, the typical workflow requires running the full application for each change to a scorer. This is time-consuming, especially for complex agents with expensive LLM calls. The stored traces workflow decouples trace generation from scorer evaluation: you run your application once to generate traces, then iterate on your scorers using those stored traces. ^[develop-code-based-scorers-databricks-on-aws.md]

## Workflow

The workflow consists of four main steps:

### Step 1: Define Evaluation Data

Create an evaluation dataset containing the inputs you want to test. For a question-answering app, this might include simple questions or multi-message conversations. ^[develop-code-based-scorers-databricks-on-aws.md]

```python
eval_dataset = [
    {
        "inputs": {
            "messages": [
                {"role": "user", "content": "How much does a microwave cost?"},
            ]
        },
    },
    {
        "inputs": {
            "messages": [
                {"role": "user", "content": "Can I return the microwave I bought 2 months ago?"},
            ]
        },
    },
]
```

### Step 2: Generate Traces from Your App

Use `mlflow.genai.evaluate()` to run your application against the evaluation dataset and generate traces. Since `evaluate()` requires at least one scorer, define a placeholder scorer for this initial run. ^[develop-code-based-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers import scorer

@scorer
def placeholder_metric() -> int:
    return 1

eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=sample_app,
    scorers=[placeholder_metric]
)
```

After this step, you have one trace in your experiment for each row in the evaluation dataset. The [MLflow Tracing](/concepts/mlflow-tracing.md) infrastructure automatically records the application's execution as part of the `@mlflow.traced` function calls. ^[develop-code-based-scorers-databricks-on-aws.md]

### Step 3: Query and Store the Resulting Traces

Store the generated traces in a local variable using `mlflow.search_traces()`, which returns a Pandas DataFrame of traces. ^[develop-code-based-scorers-databricks-on-aws.md]

```python
generated_traces = mlflow.search_traces(run_id=eval_results.run_id)
```

### Step 4: Iterate on Your Scorer Using Stored Traces

Pass the Pandas DataFrame of traces directly to `evaluate()` as an input dataset. This allows you to quickly iterate on your metric without re-running your app. Note the absence of the `predict_fn` parameter — since the traces already contain the application's outputs, no re-execution is needed. ^[develop-code-based-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers import scorer

@scorer
def response_length(outputs: str) -> int:
    # Implement your actual metric logic here.
    return len(outputs)

mlflow.genai.evaluate(
    data=generated_traces,
    scorers=[response_length],
)
```

## Benefits

- **Faster iteration cycles**: Scorer development becomes nearly instantaneous since each iteration skips the expensive application execution step. ^[develop-code-based-scorers-databricks-on-aws.md]
- **Consistent evaluation data**: All scorer iterations evaluate against the same trace data, ensuring that differences in scores reflect changes in the scorer logic rather than variability in the application's output. ^[develop-code-based-scorers-databricks-on-aws.md]
- **Reduced API costs**: By generating traces only once, you avoid repeated LLM API calls during scorer development. ^[develop-code-based-scorers-databricks-on-aws.md]

## Prerequisites

To use this workflow:

- Update `mlflow[databricks]` to version 3.1 or later for the best GenAI experience. ^[develop-code-based-scorers-databricks-on-aws.md]
- Configure [MLflow Tracing](/concepts/mlflow-tracing.md) — for example, using `mlflow.openai.autolog()` or the `@mlflow.traced` decorator — to automatically instrument your application and capture traces. ^[develop-code-based-scorers-databricks-on-aws.md]
- Set up experiment tracking, either by running within a Databricks notebook (which defaults to the notebook experiment) or by manually calling `mlflow.set_experiment()`. ^[develop-code-based-scorers-databricks-on-aws.md]

## Related Concepts

- [Code-based Scorers](/concepts/code-based-scorers.md) — The `@scorer` decorator and `Scorer` class for defining evaluation metrics
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Automatic instrumentation that captures execution traces
- [Custom LLM Scorers](/concepts/custom-judge-scorers.md) — Semantic evaluation using LLM-as-a-judge metrics
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying scorers for continuous monitoring
- [Build Evaluation Datasets](/concepts/evaluation-datasets.md) — Creating test data for your scorers
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` API for offline assessment

## Sources

- develop-code-based-scorers-databricks-on-aws.md

# Citations

1. [develop-code-based-scorers-databricks-on-aws.md](/references/develop-code-based-scorers-databricks-on-aws-4fba7668.md)
