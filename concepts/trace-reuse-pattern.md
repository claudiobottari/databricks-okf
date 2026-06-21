---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0d64ee288b6ef63d3600930a7a61756a08816cadbbb2143c42aec1fe8887a095
  pageDirectory: concepts
  sources:
    - develop-code-based-scorers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-reuse-pattern
    - TRP
  citations:
    - file: develop-code-based-scorers-databricks-on-aws.md
title: Trace Reuse Pattern
description: Technique of passing a Pandas DataFrame of previously stored traces directly to mlflow.genai.evaluate() to enable rapid iteration on scorers without re-running the full application.
tags:
  - mlflow
  - optimization
  - tracing
  - evaluation
timestamp: "2026-06-18T15:27:40.530Z"
---

# Trace Reuse Pattern

The **Trace Reuse Pattern** is a developer workflow in MLflow Evaluation for GenAI that allows you to iterate on [Code-based Scorers](/concepts/code-based-scorers.md) without re-running your entire generative AI application. By generating traces once, then reusing those stored traces as the input for subsequent evaluations, you can develop and refine scorers much more quickly. ^[develop-code-based-scorers-databricks-on-aws.md]

## Overview

When building custom [[scorers]] for GenAI evaluation, you often need to refine the scoring logic multiple times. The trace reuse pattern decouples the generation of evaluation data (traces) from the scoring step. Instead of calling your application’s `predict_fn` each time you change a scorer, you run the application once to produce a set of [Traces](/concepts/traces.md) (recorded by [MLflow Tracing](/concepts/mlflow-tracing.md)), and then evaluate those same traces repeatedly against your evolving scorer. This eliminates the overhead of re-running model inference and preserves a consistent dataset for comparison. ^[develop-code-based-scorers-databricks-on-aws.md]

## Workflow

The pattern consists of four steps: ^[develop-code-based-scorers-databricks-on-aws.md]

### Step 1: Define evaluation data

Create a list of inputs (e.g., conversation histories or prompts) that represent the scenarios you want to test. This dataset is used both for trace generation and later for scoring. ^[develop-code-based-scorers-databricks-on-aws.md]

### Step 2: Generate traces from your application

Use `mlflow.genai.evaluate()` with a placeholder scorer (e.g., a simple metric that returns a constant) and your application’s `predict_fn`. The evaluation runs the application on each data point and records the full execution trace (including LLM calls, tool invocations, and outputs) in the [MLflow tracking server](/concepts/remote-mlflow-tracking-server.md). ^[develop-code-based-scorers-databricks-on-aws.md]

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

### Step 3: Query and store the resulting traces

Retrieve the traces using `mlflow.search_traces()` with the run ID from the evaluation. This returns a Pandas DataFrame that contains all the input, output, and intermediate data for each evaluation row. ^[develop-code-based-scorers-databricks-on-aws.md]

```python
generated_traces = mlflow.search_traces(run_id=eval_results.run_id)
```

### Step 4: Iterate on your scorer using the stored traces

Pass the DataFrame of traces directly to `mlflow.genai.evaluate()` — this time without a `predict_fn`. Because the traces already contain the application’s responses, the evaluator only runs the scorers on the precomputed data. You can modify the scorer logic and call `evaluate()` again, always using the same trace dataset. ^[develop-code-based-scorers-databricks-on-aws.md]

```python
@scorer
def response_length(outputs: str) -> int:
    return len(outputs)

mlflow.genai.evaluate(
    data=generated_traces,
    scorers=[response_length],
)
```

## Benefits

- **Faster iteration** – No need to re-run the application, which can be expensive or slow (e.g., when calling paid LLM APIs). ^[develop-code-based-scorers-databricks-on-aws.md]
- **Consistent baseline** – All scorer versions are evaluated on the exact same set of traces, making comparisons fair and reproducible. ^[develop-code-based-scorers-databricks-on-aws.md]
- **Simpler debugging** – You can focus on scorer logic without worrying about changes in application behavior between runs. ^[develop-code-based-scorers-databricks-on-aws.md]

## Related Concepts

- [Code-based Scorers](/concepts/code-based-scorers.md) – The custom metrics defined with the `@scorer` decorator.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – The mechanism that captures execution traces automatically.
- [Evaluation Dataset](/concepts/evaluation-dataset.md) – The inputs and expected outputs used for evaluation.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying finished scorers to monitor live traffic.
- [Custom LLM Judges](/concepts/custom-llm-judges.md) – Alternative semantic evaluation using LLM-as-a-judge metrics.

## Sources

- develop-code-based-scorers-databricks-on-aws.md

# Citations

1. [develop-code-based-scorers-databricks-on-aws.md](/references/develop-code-based-scorers-databricks-on-aws-4fba7668.md)
