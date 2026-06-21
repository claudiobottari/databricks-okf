---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 078ea4d34c500410432e8392af46d77777af94afa9dbce7c27c45c85517dc022
  pageDirectory: concepts
  sources:
    - 10-minute-demo-collect-human-feedback-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-correctness-scorer
    - MCS
  citations:
    - file: 10-minute-demo-collect-human-feedback-databricks-on-aws.md
title: MLflow Correctness Scorer
description: An evaluation scorer that quantitatively compares GenAI app outputs against expert-provided expected responses to measure factual alignment.
tags:
  - mlflow
  - evaluation
  - scorers
  - correctness
timestamp: "2026-06-19T17:22:29.159Z"
---

```markdown
---
title: MLflow Correctness Scorer
summary: An evaluation scorer (mlflow.genai.scorers.Correctness) that compares GenAI app outputs against expert-provided expected responses to produce quantitative correctness metrics.
sources:
  - 10-minute-demo-collect-human-feedback-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:34:26.707Z"
updatedAt: "2026-06-19T08:45:49.312Z"
tags:
  - mlflow
  - evaluation
  - correctness
  - scoring
aliases:
  - mlflow-correctness-scorer
  - MCS
confidence: 1.0
provenanceState: extracted
inferredParagraphs: 0
---

# MLflow Correctness Scorer

The MLflow Correctness Scorer is a built-in evaluation metric from `mlflow.genai.scorers` that measures the factual accuracy of a model's outputs by comparing them against expert-provided reference answers.^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Overview

The `Correctness` scorer is imported from `mlflow.genai.scorers` and is used with `mlflow.genai.evaluate()` to provide quantitative feedback on how well a model's outputs align with expert expectations. It is designed to work with labeled traces where domain experts have supplied an ideal response as the ground truth.^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## How It Works

The Correctness scorer compares a model's generated output against an `expected_response` field present in the evaluation data. When used in a human feedback workflow, expert reviewers supply the ideal answer to a query during a labeling session, and the scorer measures how closely the model's actual output matches that ideal response.^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Typical Workflow

1. **Create a labeling session** – Define label schemas to collect expected responses from domain experts.
2. **Add traces to the session** – Send the traces (containing the app's inputs and outputs) to the session for review.
3. **Collect expert feedback** – Experts use the Review App to assess the outputs and provide `expected_response` labels.
4. **Retrieve labeled traces** – Use `mlflow.search_traces()` with the labeling session's run ID to obtain traces that contain expert annotations.
5. **Evaluate against expectations** – Pass the labeled traces and the model's prediction function to `mlflow.genai.evaluate()` with the Correctness scorer.^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Usage Example

The following example demonstrates collecting traces with expert-provided expected responses and evaluating the model using the Correctness scorer:

```python
from mlflow.genai.scorers import Correctness

# Get traces from a labeling session
labeled_traces = mlflow.search_traces(
    run_id=labeling_session.mlflow_run_id,
)

# Evaluate your app against expert expectations
eval_results = mlflow.genai.evaluate(
    data=labeled_traces,
    predict_fn=my_chatbot,
    scorers=[Correctness()]
)
```

^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Integration with Labeling Sessions

The Correctness scorer is designed to work with MLflow's labeling infrastructure. When domain experts review model responses through the [[MLflow Review App]] and provide ideal answers, those answers become the `expected_response` labels. The scorer then uses these labels to produce a quantitative assessment of model quality.^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Related Concepts

- [[MLflow Human Feedback Collection|Human Feedback Collection]] – The process of gathering end-user, developer, and expert feedback on GenAI app outputs.
- [[MLflow GenAI Evaluation]] – The broader framework for evaluating generative AI applications.
- [[Labeling Sessions]] – Structured review sessions where experts provide ground truth annotations.
- [[MLflow Trace|MLflow Traces]] – Recorded execution traces that capture model inputs, outputs, and metadata for evaluation.
- [[Correctness (scorer)]] – The specific scoring function used for correctness evaluation.

## Sources

- [10-minute-demo-collect-human-feedback-databricks-on-aws.md]
```

# Citations

1. [10-minute-demo-collect-human-feedback-databricks-on-aws.md](/references/10-minute-demo-collect-human-feedback-databricks-on-aws-3f033604.md)
