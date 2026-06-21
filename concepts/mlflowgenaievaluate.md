---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a7291c8f8226ceae488e2c1f04dd9814204eb82351080c66e647cb28f3781243
  pageDirectory: concepts
  sources:
    - evaluation-runs-in-mlflow-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflowgenaievaluate
    - MLflow Evaluate
    - MLflow GenAI Evaluate
    - MLflow `evaluate`
    - MLflow evaluate
    - MLflow genai evaluate
    - MLflow genai evaluate()
    - MLflow genai.evaluate()
    - mlflow.evaluate
    - mlflow.evaluate()
  citations:
    - file: evaluation-runs-in-mlflow-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
    - file: develop-code-based-scorers-databricks-on-aws.md
title: mlflow.genai.evaluate()
description: The Python API function that automatically creates an evaluation run when called with a dataset, prediction function, and scorers.
tags:
  - mlflow
  - api
  - evaluation
timestamp: "2026-06-19T18:43:48.378Z"
---

# `mlflow.genai.evaluate()`

The `mlflow.genai.evaluate()` function is the primary API for evaluating GenAI applications in [MLflow](/concepts/mlflow.md). When called, it automatically creates an evaluation run that organizes and stores the results of assessing your GenAI app's quality and performance against test data. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

## Overview

`mlflow.genai.evaluate()` evaluates a GenAI application by running it against a test dataset and applying one or more scorers or judges to assess the quality of the outputs. The function returns an evaluation result object that contains traces, feedback, aggregate metrics, and metadata. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

The evaluation dataset can be provided as a list of dictionaries, a Pandas DataFrame, or a DataFrame of previously generated traces. Each entry can include `inputs` (passed to the application) and optional `expectations` that judges can reference for correctness checking. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md, develop-code-based-scorers-databricks-on-aws.md]

## Syntax

```python
import mlflow

results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=my_app,
    scorers=[correctness_scorer, safety_scorer],
    experiment_name="my_app_evaluations"
)
```

^[evaluation-runs-in-mlflow-databricks-on-aws.md]

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `data` | Dataset (list, DataFrame, or traces DataFrame) | The evaluation dataset containing inputs to test against. Each entry typically includes `inputs` and may include `expectations` for judges to reference. Can also be a Pandas DataFrame of previously generated traces for fast iteration. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md, develop-code-based-scorers-databricks-on-aws.md] |
| `predict_fn` | Callable (optional) | The GenAI application function to evaluate. Takes a single input from the dataset and returns an output. Can be omitted when evaluating against precomputed traces. ^[develop-code-based-scorers-databricks-on-aws.md] |
| `scorers` | List of scorers or judges | One or more quality assessment functions (such as [Custom Judges](/concepts/custom-judges.md) or code-based scorers) to apply to each output. At least one scorer is required when generating new traces. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md, develop-code-based-scorers-databricks-on-aws.md] |
| `experiment_name` | str (optional) | The name of the [MLflow Experiment](/concepts/mlflow-experiment.md) to log the evaluation run under. If not specified, uses the active experiment. |

## Return Value

The function returns an evaluation result object with the following properties:

```python
# Access the run ID
print(f"Evaluation run ID: {results.run_id}")
```

^[evaluation-runs-in-mlflow-databricks-on-aws.md]

The result object provides access to:
- `run_id`: The unique identifier for the evaluation run.
- Per-trace feedback values from each scorer.
- Aggregate metrics (e.g., mean correctness, pass rates).
- Full execution traces for each input.

## Evaluation Run Structure

When `mlflow.genai.evaluate()` is called, it automatically creates an evaluation run with the following structure:

^[evaluation-runs-in-mlflow-databricks-on-aws.md]

```
Evaluation Run
├── Run Info
│   ├── run_id: unique identifier
│   ├── experiment_id: which experiment it belongs to
│   ├── start_time: when evaluation began
│   └── status: success/failed
├── Traces (one per dataset row)
│   ├── Trace 1
│   │   ├── inputs: {"question": "What is MLflow?"}
│   │   ├── outputs: {"response": "MLflow is..."}
│   │   └── feedbacks: [correctness: 0.8, relevance: 1.0]
│   ├── Trace 2
│   └── ...
├── Aggregate Metrics
│   ├── correctness_mean: 0.85
│   ├── relevance_mean: 0.92
│   └── safety_pass_rate: 1.0
└── Parameters
    ├── model_version: "v2.1"
    ├── dataset_name: "qa_test_v1"
    └── scorers: ["correctness", "relevance", "safety"]
```

## Common Use Cases

### A/B Comparison of Agent Configurations

Call `mlflow.genai.evaluate()` separately on each variant of an agent configuration and compare the resulting scores across the same evaluation dataset. This allows you to quantify the impact of changes — such as system prompt modifications, tool selection, or model choice — before promoting a configuration to production. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
# Evaluate Configuration A
result_a = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=agent_a,
    scorers=[issue_resolution_judge, expected_behaviors_judge],
)

# Evaluate Configuration B
result_b = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=agent_b,
    scorers=[issue_resolution_judge, expected_behaviors_judge],
)
```

^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Fast Iteration on Code-Based Scorers

Generate traces once using a placeholder scorer, then pass the resulting traces DataFrame directly to `evaluate()` without a `predict_fn`. This allows you to iterate quickly on your custom metric logic without rerunning the entire application. ^[develop-code-based-scorers-databricks-on-aws.md]

```python
# Step 1: Generate traces with a placeholder scorer
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=sample_app,
    scorers=[placeholder_metric]
)

# Step 2: Store the traces
generated_traces = mlflow.search_traces(run_id=eval_results.run_id)

# Step 3: Iterate on your scorer using stored traces
mlflow.genai.evaluate(
    data=generated_traces,
    scorers=[response_length],
)
```

^[develop-code-based-scorers-databricks-on-aws.md]

## Types of Scorers

### LLM-Based Judges (Custom Judges)

Created with `make_judge()`, these are LLM-based scorers that evaluate outputs against specific quality criteria. They return `mlflow.entities.Feedback` objects with structured rating values. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Code-Based Scorers

Defined with the `@scorer` decorator, these are custom Python functions that compute metrics programmatically. They are useful for deterministic measurements like response length or format validation. ^[develop-code-based-scorers-databricks-on-aws.md]

### Input/Output Judges vs. Trace-Based Judges

- **Input/Output judges** evaluate the agent's behavior by analyzing conversation history (inputs) and agent responses (outputs). These are the most common type of judge. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- **Trace-based judges** analyze the full execution trace of an agent call, including tool invocations, intermediate reasoning steps, and their results. To create a trace-based judge, include `{{ trace }}` in the judge's instructions. Trace-based judges require a model specification. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Related Concepts

- [Evaluation runs in MLflow](/concepts/evaluation-run-mlflow.md) — The runs created by `mlflow.genai.evaluate()`
- GenAI agent — Applications evaluated using this API
- [Custom Judges](/concepts/custom-judges.md) — LLM-based scorers created with `make_judge()`
- make_judge()|Make Judge API — The `make_judge()` function for creating custom evaluators
- [Code-based Scorers](/concepts/code-based-scorers.md) — Programmatic metrics created with the `@scorer` decorator
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Comparing agent variants using separate evaluation runs
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying judges for continuous quality monitoring
- [MLflow experiments](/concepts/mlflow-experiment.md) — The organizational unit for grouping evaluation runs

## Sources

- evaluation-runs-in-mlflow-databricks-on-aws.md
- create-a-custom-judge-using-make_judge-databricks-on-aws.md
- develop-code-based-scorers-databricks-on-aws.md

# Citations

1. [evaluation-runs-in-mlflow-databricks-on-aws.md](/references/evaluation-runs-in-mlflow-databricks-on-aws-05902839.md)
2. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
3. [develop-code-based-scorers-databricks-on-aws.md](/references/develop-code-based-scorers-databricks-on-aws-4fba7668.md)
