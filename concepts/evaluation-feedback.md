---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cd7558d88a9e4f19b80591369d065c2e7ecd289b77f816da59955c8516f04fc5
  pageDirectory: concepts
  sources:
    - evaluation-runs-in-mlflow-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - evaluation-feedback
  citations:
    - file: evaluation-runs-in-mlflow-databricks-on-aws.md
title: Evaluation Feedback
description: Quality assessments produced by scorers and attached to individual traces within an evaluation run.
tags:
  - mlflow
  - scoring
  - feedback
timestamp: "2026-06-19T18:43:32.432Z"
---

#Evaluation Feedback

**Evaluation Feedback** refers to the quality assessments produced by [[scorers]] that are attached to each [trace](/concepts/traces.md) within an [Evaluation Run](/concepts/evaluation-run.md) in [MLflow](/concepts/mlflow.md). These assessments provide per-input quality scores, enabling detailed analysis of a GenAI application’s performance at the individual example level. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

## Structure

Each evaluation run contains one trace for every input in the evaluation dataset. Each trace, in turn, has a list of **feedbacks** — the outputs of the scorers configured for that evaluation. For example, if an evaluation uses `correctness_scorer` and `safety_scorer`, each trace will have feedback entries for correctness and safety. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

The feedback values are scalar assessments (for instance, a correctness score of 0.8 or a relevance score of 1.0). They are stored alongside the trace’s inputs and outputs as part of the evaluation run’s hierarchical structure:

```
Evaluation Run
├── Traces
│   ├── Trace 1
│   │   ├── inputs: {"question": "What is MLflow?"}
│   │   ├── outputs: {"response": "MLflow is..."}
│   │   └── feedbacks: [correctness: 0.8, relevance: 1.0]
│   ├── Trace 2
│   └── ...
└── Aggregate Metrics (computed from all feedbacks)
```

^[evaluation-runs-in-mlflow-databricks-on-aws.md]

## Role in Evaluation Runs

Feedback is the foundation for computing [Aggregate Metrics](/concepts/aggregate-metrics.md) in an evaluation run. By aggregating feedback scores across all traces (e.g., computing the mean of correctness scores), MLflow produces summary statistics such as `correctness_mean`, `relevance_mean`, and `safety_pass_rate`. These aggregate metrics are then stored in the evaluation run’s metrics section. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

Because feedback is stored per trace, users can drill down into individual examples to understand why the aggregate score is high or low. The feedback is also used for debugging and for comparing different model versions or prompts.

## Related Concepts

- [Evaluation Runs](/concepts/evaluation-runs.md) – The container that organizes feedback, traces, and metrics.
- [Traces](/concepts/traces.md) – Each trace holds one input, the corresponding output, and its feedbacks.
- [[Scorers]] – Functions that produce feedback by assessing quality, safety, or other dimensions.
- [Aggregate Metrics](/concepts/aggregate-metrics.md) – Summary statistics derived from feedback across all traces.
- [MLflow](/concepts/mlflow.md) – The platform that manages evaluation runs and feedback storage.

## Sources

- evaluation-runs-in-mlflow-databricks-on-aws.md

# Citations

1. [evaluation-runs-in-mlflow-databricks-on-aws.md](/references/evaluation-runs-in-mlflow-databricks-on-aws-05902839.md)
