---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2f8d5ddce24925aa8d4f36224db1bb9ca8d443481a4d863d7b19c66a96ad636f
  pageDirectory: concepts
  sources:
    - evaluation-runs-in-mlflow-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - aggregate-metrics-in-mlflow-evaluation
    - AMIME
  citations:
    - file: evaluation-runs-in-mlflow-databricks-on-aws.md
title: Aggregate Metrics in MLflow Evaluation
description: Summary statistics computed across all evaluated examples in an evaluation run, such as mean correctness, mean relevance, and safety pass rate.
tags:
  - mlflow
  - evaluation
  - metrics
  - statistics
timestamp: "2026-06-19T10:24:51.019Z"
---

Here is the wiki page for "Aggregate Metrics in MLflow Evaluation", written based solely on the provided source material.

---

## Aggregate Metrics in MLflow Evaluation

**Aggregate Metrics** are summary statistics computed across all evaluated examples in an [Evaluation Runs in MLflow|evaluation run](/concepts/evaluation-run-mlflow.md). They provide a high-level overview of your GenAI app's performance, complementing the per-input feedback and traces stored in the same run. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

### Structure

Within an evaluation run, aggregate metrics appear alongside traces and feedback. For example, an evaluation run that scores outputs on correctness, relevance, and safety might produce the following aggregate metrics: ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

```
Aggregate Metrics
├── correctness_mean: 0.85
├── relevance_mean: 0.92
└── safety_pass_rate: 1.0
```

These metrics represent the central tendency or pass/fail rate of the feedback values produced by [scorers](/concepts/scorers-in-mlflow-evaluation.md) across every example in the evaluation dataset.

### How They Are Created

Aggregate metrics are automatically computed when you call `mlflow.genai.evaluate()`. The function runs each input through your app, collects individual feedback scores from each scorer, and then aggregates those scores into summary statistics for the whole run. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

```python
import mlflow

results = mlflow.genai.evaluate(
    data=test_dataset,
    predict_fn=my_app,
    scorers=[correctness_scorer, safety_scorer],
    experiment_name="my_app_evaluations"
)

# Access the run ID — aggregate metrics are stored inside the run
print(f"Evaluation run ID: {results.run_id}")
```

### Relationship to Traces and Feedback

Each trace in the evaluation run contains per-input feedback values (e.g., `correctness: 0.8`, `relevance: 1.0`). Aggregate metrics are the summary statistics computed from those per-input values across all traces in the run. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

```
Evaluation Run
├── Traces (one per dataset row)
│   ├── Trace 1: feedbacks = [correctness: 0.8, relevance: 1.0]
│   ├── Trace 2: feedbacks = [correctness: 0.9, relevance: 0.84]
│   └── ...
├── Aggregate Metrics ← computed from all per-trace feedbacks
│   ├── correctness_mean: 0.85
│   └── relevance_mean: 0.92
```

### Common Aggregate Metrics

While the specific aggregate metrics depend on the scorers you configure, common examples include:

- **Means** (e.g., `correctness_mean`, `relevance_mean`) — average score across all examples for a numeric scorer
- **Pass rates** (e.g., `safety_pass_rate`) — fraction of examples that passed a binary or threshold-based check

### Viewing Aggregate Metrics

Aggregate metrics can be viewed through the [MLflow UI](/concepts/mlflow.md) by opening the evaluation run and inspecting its metrics section. They can also be accessed programmatically via the MLflow [Tracking API](/concepts/mlflow-tracking.md) using the evaluation run's ID.

### Related Concepts

- [Evaluation Runs in MLflow](/concepts/evaluation-run-mlflow.md) — The container for aggregate metrics, traces, and feedback
- [Scorers in MLflow Evaluation](/concepts/scorers-in-mlflow-evaluation.md) — The per-input evaluators whose outputs are aggregated
- [Traces in MLflow Evaluation](/concepts/traces-in-mlflow-evaluation.md) — Per-input execution records that carry individual feedback values
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit that groups related evaluation runs
- [Feedback in MLflow Evaluation](/concepts/feedback-in-mlflow-evaluation.md) — Per-input quality assessments that feed into aggregate metrics

### Sources

- evaluation-runs-in-mlflow-databricks-on-aws.md

# Citations

1. [evaluation-runs-in-mlflow-databricks-on-aws.md](/references/evaluation-runs-in-mlflow-databricks-on-aws-05902839.md)
