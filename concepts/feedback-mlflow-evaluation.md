---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 326e56499bff92facd44bc7b1cfd15a6ca866efd0c82d8510dbc6e7fd88e7829
  pageDirectory: concepts
  sources:
    - evaluation-runs-in-mlflow-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feedback-mlflow-evaluation
    - F(E
    - Feedback (MLflow entity)
  citations:
    - file: evaluation-runs-in-mlflow-databricks-on-aws.md
title: Feedback (MLflow Evaluation)
description: Quality assessments from scorers attached to individual traces during an evaluation run, representing per-example scores.
tags:
  - mlflow
  - evaluation
  - scoring
  - genai
timestamp: "2026-06-18T12:13:57.051Z"
---

# Feedback (MLflow Evaluation)

**Feedback** in [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) represents the quality assessments produced by scorers during an [Evaluation Run](/concepts/evaluation-run.md). Each feedback value is attached to a specific trace and captures a scorer's judgment about the quality or characteristics of the GenAI application's output for a given input.

## Overview

When you call `mlflow.genai.evaluate()`, each row in your evaluation dataset produces a trace. For each trace, every scorer in the evaluation generates a feedback value — a structured quality assessment of the application's output. These feedback values are stored alongside the trace in the evaluation run, enabling both per-example inspection and aggregate metric computation. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

## Structure

Feedback values are organized within an evaluation run as follows:

- **Per-trace feedback**: Each trace contains a `feedbacks` list with one entry per scorer. Each entry includes the scorer name and its output value.
- **Aggregate metrics**: Feedback values across all traces are aggregated into summary statistics (e.g., mean, pass rate) stored in the evaluation run's metrics. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

```
Evaluation Run
├── Traces (one per dataset row)
│   ├── Trace 1
│   │   ├── inputs: {"question": "What is MLflow?"}
│   │   ├── outputs: {"response": "MLflow is..."}
│   │   └── feedbacks: [correctness: 0.8, relevance: 1.0]
│   ├── Trace 2
│   │   └── feedbacks: [correctness: 0.9, relevance: 0.7]
│   └── ...
└── Aggregate Metrics
    ├── correctness_mean: 0.85
    ├── relevance_mean: 0.92
    └── safety_pass_rate: 1.0
```

## Types of Feedback

### Scorer-Based Feedback

Scorers — such as [Custom Judges](/concepts/custom-judges.md) created with `make_judge()`, or built-in MLflow scorers — produce structured feedback values. The feedback can be numeric (e.g., 0.0 to 1.0), categorical (e.g., "pass" or "fail"), or any type supported by the scorer's output schema. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

For example, a correctness scorer might return a float between 0 and 1, while a compliance scorer might return a boolean or an enumerated category.

### Aggregate Feedback Metrics

After all traces in an evaluation run are scored, MLflow computes aggregate statistics across all feedback values for each scorer. These metrics are stored in the evaluation run's metrics section and can include: ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

- **Mean**: Average score across all examples
- **Pass rate**: Fraction of examples meeting a threshold
- **Standard deviation**: Spread of scores
- **Min/max**: Range of observed values

## Example

```python
import mlflow

results = mlflow.genai.evaluate(
    data=test_dataset,
    predict_fn=my_app,
    scorers=[correctness_scorer, safety_scorer],
    experiment_name="my_app_evaluations",
)

# Access per-trace feedback
for trace in results.traces:
    print(f"Input: {trace.inputs}")
    print(f"Output: {trace.outputs}")
    print(f"Feedback: {trace.feedbacks}")
    # e.g., Feedback: [correctness: 0.8, safety: True]

# Access aggregate metrics
print(f"Mean correctness: {results.metrics['correctness_mean']}")
print(f"Safety pass rate: {results.metrics['safety_pass_rate']}")
```

^[evaluation-runs-in-mlflow-databricks-on-aws.md]

## Use Cases

### Quality Assessment

Feedback enables you to measure how well your GenAI application performs across multiple quality dimensions. By attaching multiple scorers — for example, correctness, relevance, and safety — you can assess the application's output holistically rather than relying on a single metric. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

### Regression Detection

By comparing feedback scores across evaluation runs (e.g., after a model update or prompt change), you can detect regressions in specific quality dimensions before deploying changes to production.

### Debugging Poor Outputs

Per-trace feedback allows you to identify specific inputs where the application underperforms. By locating traces with low feedback scores, you can examine the inputs and outputs to understand failure modes. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

## Related Concepts

- [Evaluation Runs](/concepts/evaluation-runs.md) — The organizational structure containing traces, feedback, and metrics
- [[Scorers]] — Components that produce feedback values during evaluation
- [Custom Judges](/concepts/custom-judges.md) — User-defined LLM-based scorers created with `make_judge()`
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The overall evaluation framework
- [Traces](/concepts/traces.md) — Execution records that feedback values attach to

## Sources

- evaluation-runs-in-mlflow-databricks-on-aws.md

# Citations

1. [evaluation-runs-in-mlflow-databricks-on-aws.md](/references/evaluation-runs-in-mlflow-databricks-on-aws-05902839.md)
