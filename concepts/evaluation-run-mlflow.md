---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f2bf896a11a048ca0c25fd74f6151d5d74a1c6a2e6b4e23f6fcd03ca59864219
  pageDirectory: concepts
  sources:
    - evaluation-runs-in-mlflow-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - evaluation-run-mlflow
    - ER(
    - Evaluation Runs in MLflow
    - Evaluation runs in MLflow
    - Evaluation Runs in MLflow|evaluation run
  citations:
    - file: evaluation-runs-in-mlflow-databricks-on-aws.md
title: Evaluation Run (MLflow)
description: An MLflow run that organizes and stores the results of evaluating a GenAI application, including traces, feedback, metrics, and metadata.
tags:
  - mlflow
  - evaluation
  - genai
  - mlops
timestamp: "2026-06-19T10:24:37.267Z"
---

# Evaluation Run (MLflow)

An **Evaluation Run** is an [MLflow Run](/concepts/mlflow-run.md) that organizes and stores the results of evaluating a [GenAI](/concepts/mlflow-genai-evaluate-api.md) application. When you call `mlflow.genai.evaluate()`, MLflow automatically creates an evaluation run to capture all assessment data in a structured format. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

## Structure

An evaluation run contains the following components: ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

- **Traces**: One trace for each input in the evaluation dataset, recording the full execution path of the GenAI app.
- **Feedback**: Quality assessments from scorers attached to each trace, such as correctness, relevance, or safety scores.
- **Metrics**: Aggregate statistics computed across all evaluated examples, including means, pass rates, and other summary measures.
- **Metadata**: Information about the evaluation configuration, including model version, dataset name, and the list of scorers used.

### Example Structure

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

^[evaluation-runs-in-mlflow-databricks-on-aws.md]

## Creating an Evaluation Run

An evaluation run is automatically created when you call `mlflow.genai.evaluate()`. You do not need to create the run manually. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

```python
import mlflow

# This creates an evaluation run
results = mlflow.genai.evaluate(
    data=test_dataset,
    predict_fn=my_app,
    scorers=[correctness_scorer, safety_scorer],
    experiment_name="my_app_evaluations"
)

# Access the run ID
print(f"Evaluation run ID: {results.run_id}")
```

^[evaluation-runs-in-mlflow-databricks-on-aws.md]

## Key Concepts

- **Run ID**: A unique identifier for the evaluation run, accessible via `results.run_id`.
- **Experiment ID**: Identifies which [MLflow Experiment](/concepts/mlflow-experiment.md) the evaluation run belongs to.
- **Status**: Indicates whether the evaluation completed successfully or failed.
- **Start Time**: Timestamp recording when the evaluation began.

## Related Concepts

- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The broader framework for evaluating GenAI applications
- [Traces](/concepts/traces.md) — Execution traces captured for each evaluation input
- [[Scorers]] — Quality assessment functions that produce feedback
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizational units for grouping related runs
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Using evaluation runs to compare agent variants
- [Custom Judges](/concepts/custom-judges.md) — LLM-based scorers used in evaluation runs

## Sources

- evaluation-runs-in-mlflow-databricks-on-aws.md

# Citations

1. [evaluation-runs-in-mlflow-databricks-on-aws.md](/references/evaluation-runs-in-mlflow-databricks-on-aws-05902839.md)
