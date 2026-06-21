---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 339c9ade590acc4c5f44fd1ae02c25591e171d4532b19f84071b6b9227ba0a54
  pageDirectory: concepts
  sources:
    - 10-minute-demo-collect-human-feedback-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - mlflow-evaluation-dataset-for-versioning
    - MEDFV
    - Evaluation Dataset Versioning
  citations:
    - file: 10-minute-demo-collect-human-feedback-databricks-on-aws.md
title: MLflow Evaluation Dataset for Versioning
description: Recommended practice of packaging labeled traces into an MLflow Evaluation Dataset for version tracking and lineage when evaluating GenAI apps.
tags:
  - mlflow
  - evaluation
  - datasets
  - versioning
timestamp: "2026-06-19T17:22:34.653Z"
---

## MLflow Evaluation Dataset for Versioning

An **MLflow Evaluation Dataset** is a versioned collection of labeled traces that provides tracking and lineage for evaluation data. When human feedback—such as expert annotations—has been collected on [[MLflow Trace|MLflow Traces]], Databricks recommends packaging those labeled traces into an evaluation dataset. This practice ensures that evaluation data has a clear history, making it reproducible and auditable over time. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Purpose and Benefits

Evaluation datasets allow teams to:

- **Track versions** of the labeled data used for model evaluation, so comparisons between different model versions or prompts are grounded in the same reference set.
- **Maintain lineage** by recording where each labeled trace came from (e.g., which labeling session or feedback event created it), enabling traceability from raw feedback to final metrics.
- **Enable reproducible evaluation** by associating a fixed snapshot of ground-truth data with a specific evaluation run. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Typical Workflow

After a labeling session (such as the one created in the [10-minute demo: Collect human feedback](/concepts/mlflow-3-human-feedback-and-labeling.md)) produces expert-ground-truth labels, the recommended next step is to add those labeled traces to an MLflow Evaluation Dataset. The dataset can then be used as the `data` argument in `mlflow.genai.evaluate()`, ensuring that the evaluation has a well-defined, versioned input. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Related Concepts

- [[MLflow Trace|MLflow Traces]] – The core unit of observability that records each GenAI app invocation.
- [Human Feedback](/concepts/mlflow-human-feedback-collection.md) – End-user and expert annotations that form the basis of evaluation datasets.
- [Labeling Session](/concepts/labeling-session.md) – A structured review where experts assign ground-truth labels to traces.
- [Correctness Scorer](/concepts/correctness-scorer.md) – A metric that compares model outputs against labels stored in an evaluation dataset.
- Evaluation Dataset Build Guide – Detailed instructions for creating and managing versioned datasets (see the Databricks documentation).

### Sources

- 10-minute-demo-collect-human-feedback-databricks-on-aws.md

# Citations

1. [10-minute-demo-collect-human-feedback-databricks-on-aws.md](/references/10-minute-demo-collect-human-feedback-databricks-on-aws-3f033604.md)
