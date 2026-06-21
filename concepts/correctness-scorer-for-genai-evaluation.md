---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2a9bbc535ef99945152c9241b8d515b0e96d105d9073b409f647658b571ade95
  pageDirectory: concepts
  sources:
    - 10-minute-demo-collect-human-feedback-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - correctness-scorer-for-genai-evaluation
    - CSFGE
  citations:
    - file: 10-minute-demo-collect-human-feedback-databricks-on-aws.md
title: Correctness Scorer for GenAI Evaluation
description: MLflow scorer that compares GenAI app outputs against expert-provided expected responses to produce quantitative correctness metrics.
tags:
  - mlflow
  - evaluation
  - correctness
  - genai
timestamp: "2026-06-19T13:48:57.027Z"
---

## Correctness Scorer for GenAI Evaluation

The **Correctness Scorer** is an evaluation metric in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) that measures how well a generative AI application’s outputs align with expert‑defined ground truth. It is used as part of `mlflow.genai.evaluate()` to compare model responses against the `expected_response` labels collected through human feedback workflows. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Overview

After domain experts review traces and provide ground‑truth answers—for example, by filling in an `expected_response` field in a [Labeling Session](/concepts/labeling-session.md)—the Correctness scorer quantifies the agreement between the application’s actual output and that expert‑supplied reference. This gives development teams a quantitative signal of factual accuracy and alignment with expert expectations. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

The scorer is designed to work with traces that have been enriched via the human‑feedback pipeline: end‑user ratings, developer annotations, and expert labeling sessions all feed into the evaluation dataset. The `expected_response` field is the key input for the Correctness scorer. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Usage

The Correctness scorer is imported from `mlflow.genai.scorers` and passed as a list item to the `scorers` parameter of `mlflow.genai.evaluate()`. The evaluation data must contain the input prompts (or traces) and the `expected_response` labels that were collected during expert review. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Correctness

# Retrieve labeled traces from a labeling session
labeled_traces = mlflow.search_traces(
    run_id=labeling_session.mlflow_run_id,
)

# Evaluate the application against expert expectations
eval_results = mlflow.genai.evaluate(
    data=labeled_traces,
    predict_fn=my_chatbot,    # The GenAI app being evaluated
    scorers=[Correctness()],  # Compares outputs to expected_response
)
```

The scorer automatically reads the `expected_response` field from the evaluation records and computes a correctness score for each output. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Relationship to Human Feedback

The Correctness scorer is a natural companion to the human‑feedback collection pipeline. The typical workflow is:

1.  **Instrument** the GenAI app with [MLflow Tracing](/concepts/mlflow-tracing.md).
2.  **Collect end‑user feedback** (e.g., thumbs up/down).
3.  **Add developer annotations** via the UI.
4.  **Create a labeling session** and ask experts to provide ideal responses (`expected_response`).
5.  **Evaluate** the app against those expert responses using the Correctness scorer. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

This creates a closed loop: human insights become quantitative metrics that can be tracked over time and compared across agent configurations.

### Related Concepts

- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The broader evaluation framework in MLflow GenAI.
- [Labeling Session](/concepts/labeling-session.md) – A structured mechanism for collecting expert ground‑truth labels.
- [Human Feedback](/concepts/mlflow-human-feedback-collection.md) – End‑user ratings, developer annotations, and expert reviews.
- expected_facts vs expected_response|Expected Response – The expert‑supplied ideal answer used by the Correctness scorer.
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) – Evaluating GenAI agents on quality criteria.
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) – Comparing variants using consistent judges and metrics.

### Sources

- 10-minute-demo-collect-human-feedback-databricks-on-aws.md

# Citations

1. [10-minute-demo-collect-human-feedback-databricks-on-aws.md](/references/10-minute-demo-collect-human-feedback-databricks-on-aws-3f033604.md)
