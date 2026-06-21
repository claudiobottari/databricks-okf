---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a2f5cfb06bc2603db211a9683f499af4df2c3bcd27cb4e2d536a14f83772173d
  pageDirectory: concepts
  sources:
    - evaluation-runs-in-mlflow-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-evaluation-run
    - MER
  citations:
    - file: evaluation-runs-in-mlflow-databricks-on-aws.md
title: MLflow Evaluation Run
description: An MLflow run that organizes and stores the results of evaluating a GenAI app, including traces, feedback, metrics, and metadata.
tags:
  - mlflow
  - evaluation
  - genai
timestamp: "2026-06-19T18:43:19.091Z"
---

# MLflow Evaluation Run

An **MLflow Evaluation Run** is a specialized [MLflow Run](/concepts/mlflow-run.md) that organizes and stores the results of evaluating a [Generative AI](/concepts/mlflow-tracing-for-generative-ai.md) application. It is automatically created when the `mlflow.genai.evaluate()` function is called. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

## Contents of an Evaluation Run

An evaluation run groups together the following components: ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

- **Traces**: One [[MLflow Trace]] for each input in the evaluation dataset. Each trace records the inputs (e.g., a question) and outputs (e.g., the model’s response) for a single evaluation example.
- **Feedback**: Quality assessments from [[Scorers]] that are attached to each trace. Each scorer produces a numeric or categorical score for that example.
- **Metrics**: Aggregate statistics computed across all evaluated examples, such as mean correctness or pass rate.
- **Metadata**: Information about the evaluation configuration, including the model version, dataset name, and list of scorers used.

## How to Create an Evaluation Run

An evaluation run is created implicitly when you call `mlflow.genai.evaluate()`. You provide an evaluation dataset, a prediction function (or model), and a list of scorers. The function returns a results object from which you can access the run ID. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

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

## Evaluation Run Structure

An evaluation run has a hierarchical structure comprising run-level information, individual traces, aggregate metrics, and parameters. The following tree illustrates the components: ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

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

## Related Concepts

- [MLflow Run](/concepts/mlflow-run.md) – The generic container for a unit of MLflow work.
- [[MLflow Trace]] – A record of a single prediction or evaluation request.
- [[Scorers|Scorer]] – A function that assesses the quality of a model output.
- [GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The overall process of evaluating generative AI applications.
- [mlflow.genai.evaluate()](/concepts/mlflowgenaievaluate.md) – The API that creates evaluation runs.

## Sources

- evaluation-runs-in-mlflow-databricks-on-aws.md

# Citations

1. [evaluation-runs-in-mlflow-databricks-on-aws.md](/references/evaluation-runs-in-mlflow-databricks-on-aws-05902839.md)
