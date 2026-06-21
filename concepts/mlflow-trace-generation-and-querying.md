---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4c73ad896a215236d0da1a945703ef1784daf7dedb54bed599f1f7a022453904
  pageDirectory: concepts
  sources:
    - develop-code-based-scorers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-generation-and-querying
    - Querying and MLflow Trace Generation
    - MTGAQ
  citations:
    - file: develop-code-based-scorers-databricks-on-aws.md
title: MLflow Trace Generation and Querying
description: The process of using mlflow.genai.evaluate() to generate traces from an AI application, then retrieving them as a Pandas DataFrame via mlflow.search_traces() for downstream evaluation.
tags:
  - mlflow
  - tracing
  - evaluation
  - dataframe
timestamp: "2026-06-19T10:13:50.980Z"
---

# MLflow Trace Generation and Querying

**MLflow Trace Generation and Querying** refers to the workflow of creating execution traces from an AI application by running it through evaluation data, then storing and retrieving those traces for iterative metric development and scoring.

## Overview

[MLflow Tracing](/concepts/mlflow-tracing.md) automatically records the execution of instrumented AI applications, capturing inputs, outputs, and intermediate steps for each invocation. When combined with MLflow Evaluation, traces can be generated en masse by calling `mlflow.genai.evaluate()` with a dataset and a placeholder scorer. These traces can then be queried, stored locally, and reused to speed up the iterative development of custom scorers without re-running the application. ^[develop-code-based-scorers-databricks-on-aws.md]

## Generating Traces

### Instrumenting the Application

Applications are instrumented using `mlflow.openai.autolog()`, `@mlflow.trace`, or other tracing decorators provided by MLflow. These annotations ensure that every call to the instrumented function produces a trace that captures the full execution context. ^[develop-code-based-scorers-databricks-on-aws.md]

### Running Evaluation to Produce Traces

To generate traces for multiple inputs simultaneously, pass a list of evaluation data and a placeholder scorer to `mlflow.genai.evaluate()`: ^[develop-code-based-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers import scorer

@scorer
def placeholder_metric() -> int:
    return 1

eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=sample_app,
    scorers=[placeholder_metric],
)
```

This creates one trace in the current experiment for each row in the evaluation dataset. The LLM's response appears in the notebook Trace UI's **Outputs** field and in the MLflow Experiment UI's **Response** column. ^[develop-code-based-scorers-databricks-on-aws.md]

## Querying Traces

### Using `mlflow.search_traces()`

Traces are stored as part of an [MLflow Run](/concepts/mlflow-run.md). The function `mlflow.search_traces()` returns a Pandas DataFrame containing all traces for a given run: ^[develop-code-based-scorers-databricks-on-aws.md]

```python
generated_traces = mlflow.search_traces(run_id=eval_results.run_id)
```

### Trace DataFrame Structure

The returned DataFrame contains one row per trace, with columns that include the trace's inputs, outputs, and metadata. The exact schema depends on the application's instrumentation and the data format used during evaluation. ^[develop-code-based-scorers-databricks-on-aws.md]

## Using Stored Traces for Iterative Development

Once traces are stored in a DataFrame, they can be passed directly as the `data` parameter to `mlflow.genai.evaluate()` — notably without a `predict_fn`: ^[develop-code-based-scorers-databricks-on-aws.md]

```python
mlflow.genai.evaluate(
    data=generated_traces,
    scorers=[response_length],
)
```

This allows a developer to iterate on scorer logic rapidly without re-running the original application. The scorers operate on the pre-computed traces, using the stored inputs and outputs as the basis for evaluation. ^[develop-code-based-scorers-databricks-on-aws.md]

## Benefits

- **Faster iteration cycles**: Modify and test scorers against the same set of traces without incurring the cost or latency of re-running the underlying application. ^[develop-code-based-scorers-databricks-on-aws.md]
- **Reproducible evaluation**: The same traces can be reused across scorer versions, ensuring that changes in scores are due to the scorer logic rather than variance in model outputs. ^[develop-code-based-scorers-databricks-on-aws.md]
- **Offline scoring**: Traces can be generated once in a production-like environment and scored multiple times during development, reducing the load on live model endpoints. ^[develop-code-based-scorers-databricks-on-aws.md]

## Prerequisites

- `mlflow[databricks]>=3.1` (recommended for the best GenAI experience) ^[develop-code-based-scorers-databricks-on-aws.md]
- Instrumented application using `mlflow.openai.autolog()` or manual `@mlflow.trace` decorators ^[develop-code-based-scorers-databricks-on-aws.md]
- Evaluation data defined as a list of dictionaries containing `inputs` ^[develop-code-based-scorers-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The core instrumentation framework that records execution traces
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` API used to generate and score traces
- [Code-based Scorers](/concepts/code-based-scorers.md) — Custom metrics developed using the `@scorer` decorator
- [Custom LLM Judges](/concepts/custom-llm-judges.md) — Semantic evaluation using LLM-as-a-judge metrics
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying scorers for continuous monitoring
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Creating test data for scorer development

## Sources

- develop-code-based-scorers-databricks-on-aws.md

# Citations

1. [develop-code-based-scorers-databricks-on-aws.md](/references/develop-code-based-scorers-databricks-on-aws-4fba7668.md)
