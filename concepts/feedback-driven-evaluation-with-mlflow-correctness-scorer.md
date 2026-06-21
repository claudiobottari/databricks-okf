---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c6e057ce810ee836c9ec9eb66bff83964d15b0616b97348c8c49bdd49c0f8279
  pageDirectory: concepts
  sources:
    - 10-minute-demo-collect-human-feedback-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feedback-driven-evaluation-with-mlflow-correctness-scorer
    - FEWMCS
  citations:
    - file: 10-minute-demo-collect-human-feedback-databricks-on-aws.md
title: Feedback-Driven Evaluation with MLflow Correctness Scorer
description: Using expert-provided expected_response labels to quantitatively evaluate GenAI app outputs against ground truth using MLflow's Correctness scorer within mlflow.genai.evaluate()
tags:
  - mlflow
  - evaluation
  - correctness
  - quality-metrics
timestamp: "2026-06-19T21:53:41.477Z"
---

Here is the wiki page for "Feedback-Driven Evaluation with MLflow Correctness Scorer", written based solely on the provided source material.

---

## Feedback-Driven Evaluation with MLflow Correctness Scorer

**Feedback-Driven Evaluation with MLflow Correctness Scorer** refers to a methodology for quantitatively assessing a GenAI application by comparing its outputs against human-validated ground truth. The process leverages [MLflow Tracing](/concepts/mlflow-tracing.md) to collect feedback from end users, developers, and domain experts, then uses that expert feedback as the reference standard within MLflow’s `Correctness` scorer. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Overview

The MLflow `Correctness` scorer is a built-in metric for evaluating the factual accuracy of a model’s response. When used in a feedback-driven workflow, the scorer compares the application’s output (`prediction`) against an `expected_response` that has been curated or validated by a human expert. This transforms subjective review into a quantitative, reproducible evaluation score. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Evaluation Workflow

The full feedback-driven evaluation pipeline involves three phases:

1. **Collect feedback from multiple sources** — End-user feedback (e.g., thumbs up/down) is captured via `mlflow.log_feedback()`. Developers add annotations or scores in the UI. Domain experts provide structured assessments through a labeling session.
2. **Obtain an expert-defined `expected_response`** — Through a labeling session, expert reviewers submit their own version of the ideal answer as an `expected_response` label. This serves as the ground truth for the `Correctness` scorer.
3. **Run the evaluation** — The `Correctness` scorer compares the application’s output to the expert-provided `expected_response`. The result is a numeric score indicating how well the app’s responses align with expert expectations.

### Code Example

After collecting expert labels from a labeling session, the following code evaluates the application using the `Correctness` scorer: ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Correctness

# Retrieve labeled traces from a labeling session
labeled_traces = mlflow.search_traces(
    run_id=labeling_session.mlflow_run_id,  # Labeling sessions are MLflow Runs
)

# Evaluate the app against expert expectations
eval_results = mlflow.genai.evaluate(
    data=labeled_traces,
    predict_fn=my_chatbot,  # The GenAI app being evaluated
    scorers=[Correctness()]  # Compares outputs to expected_response
)
```

The `Correctness` scorer automatically looks for an `expected_response` column in the evaluation data. The data for this column is populated by the expert reviewer when they submit their ideal answer during the labeling session. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Best Practices

Databricks recommends adding labeled traces to an [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md) to provide version tracking and lineage for the evaluation data. This ensures reproducibility and traceability of evaluation results over time. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The mechanism for instrumenting and capturing GenAI application calls and their associated metadata.
- [Human Feedback Collection](/concepts/mlflow-human-feedback-collection.md) — The process of gathering assessments from end users, developers, and domain experts.
- [Labeling Session](/concepts/labeling-session.md) — A structured review process where domain experts assess model outputs and provide ground-truth labels.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The broader framework for running scorers and comparing model performance.
- [Correctness Scorer](/concepts/correctness-scorer.md) — The specific scorer that measures factual accuracy against a reference answer.

### Sources

- 10-minute-demo-collect-human-feedback-databricks-on-aws.md

# Citations

1. [10-minute-demo-collect-human-feedback-databricks-on-aws.md](/references/10-minute-demo-collect-human-feedback-databricks-on-aws-3f033604.md)
