---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ca6aa3fc321ae64dfabf377ab1346f93b434aecabf4b532600da64c2251a25e2
  pageDirectory: concepts
  sources:
    - evaluation-runs-in-mlflow-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - evaluation-run-structure
    - ERS
  citations:
    - file: evaluation-runs-in-mlflow-databricks-on-aws.md
title: Evaluation Run Structure
description: The hierarchical organization of an evaluation run comprising run info, traces with feedback, aggregate metrics, and configuration parameters.
tags:
  - mlflow
  - structure
  - organization
timestamp: "2026-06-19T18:43:44.664Z"
---

```markdown
---
title: Evaluation Run Structure
summary: The hierarchical organization of an evaluation run in MLflow, including run info, traces, feedbacks, aggregate metrics, and parameters.
sources:
  - evaluation-runs-in-mlflow-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:24:55.610Z"
updatedAt: "2026-06-19T10:24:55.610Z"
tags:
  - mlflow
  - evaluation
  - structure
  - organization
aliases:
  - evaluation-run-structure
  - ERS
confidence: 0.97
provenanceState: extracted
inferredParagraphs: 0
---

# Evaluation Run Structure

An **evaluation run** in [[MLflow]] is a specialized [[MLflow Run]] that organizes and stores the results of evaluating a [[MLflow GenAI Evaluate API|GenAI]] application. Each evaluation run aggregates the outputs, quality assessments, and metadata generated when `mlflow.genai.evaluate()` is called on an [[evaluation dataset]] using a prediction function and one or more [[scorers]]. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

## Components of an Evaluation Run

An evaluation run contains four major categories of data:

- **Traces**: One [[Traces|trace]] for each input row in the evaluation dataset. Each trace captures the full execution path of the application for that input, including the inputs, intermediate steps, and final outputs.
- **Feedback**: Quality assessments (also called *feedbacks*) produced by the scorers, attached to each trace. Feedback values can be numeric scores, categorical labels, or free-text justifications.
- **Metrics**: Aggregate statistics computed across all examples, such as means, pass rates, or standard deviations for each scorer.
- **Metadata**: Information about the evaluation configuration, such as the model version, dataset name, and list of scorers used.

The following diagram, adapted from the MLflow documentation, illustrates the nested structure: ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

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

## How Evaluation Runs Are Created

An evaluation run is automatically created when you call `mlflow.genai.evaluate()`. You do not need to manually create a run; the API handles run creation, trace logging, feedback attachment, and metric computation. The run is associated with the [[MLflow Experiment|experiment]] specified in the call (or the active experiment if none is provided). The run ID can be accessed from the returned result object. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

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

## Related Concepts

- [[MLflow Experiment|MLflow Experiments]] – The organizational container that groups related evaluation runs.
- [[MLflow GenAI Evaluation|GenAI Evaluation]] – The broader evaluation workflow for generative AI applications.
- [[Scorers]] – Functions that produce feedback values attached to each trace.
- [[MLflow Trace Structure|Trace Structure]] – Detailed anatomy of a single trace within an evaluation run.
- [[Aggregate Metrics]] – Summary statistics computed across all examples in a run.
- Evaluation Runs vs. Training Runs – Differences between evaluation-oriented and training-oriented MLflow runs.

## Sources

- evaluation-runs-in-mlflow-databricks-on-aws.md
```

# Citations

1. [evaluation-runs-in-mlflow-databricks-on-aws.md](/references/evaluation-runs-in-mlflow-databricks-on-aws-05902839.md)
