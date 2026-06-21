---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 62802a9839fdf009f0b82e06e3145f490d25b3e050e4a13d5bb1707cdf6bcaf4
  pageDirectory: concepts
  sources:
    - migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3-evaluation-data-schema
    - M3EDS
  citations:
    - file: migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md
title: MLflow 3 Evaluation Data Schema
description: "MLflow 3 uses a new data field mapping: inputs (replaces request), outputs (replaces response), and expectations (replaces expected_response, expected_facts, etc.), organized as structured dicts within each evaluation row."
tags:
  - mlflow
  - data-schema
  - evaluation
timestamp: "2026-06-19T19:35:04.764Z"
---

---
title: MLflow 3 Evaluation Data Schema
summary: The structured format for evaluation datasets in MLflow 3, including the `inputs`, `outputs`, and `expectations` fields.
sources:
  - migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T20:00:00.000Z"
updatedAt: "2026-06-19T20:00:00.000Z"
tags:
  - mlflow
  - evaluation
  - data-schema
  - genai
aliases:
  - mlflow-3-evaluation-data-schema
  - M3EDS
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# MLflow 3 Evaluation Data Schema

**MLflow 3 Evaluation Data Schema** defines the structure of the evaluation data passed to `mlflow.genai.evaluate()` and how results are organised. Compared to MLflow 2.x, the field names have changed to a dictionary-based format that separates the model's input, output, and any ground-truth expectations.^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Data Fields

Each evaluation example is a dictionary with three top-level keys:

| Old field (MLflow 2.x) | New field (MLflow 3) | Description |
|------------------------|----------------------|-------------|
| `request`              | `inputs`            | Dictionary of input parameters passed to the predict function. |
| `response`             | `outputs`           | Dictionary of the model's output (e.g., `{"response": "..."}`). |
| `expected_response` (or other `expected*`) | `expectations` | Dictionary of expected values used for ground-truth scorers (e.g., `{"expected_response": "..."}`). |

The `inputs` and `outputs` fields are always dictionaries; they are not plain strings. The `expectations` field is optional and also a dictionary, containing any expected values such as `expected_response` or `guidelines`.^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Using the Schema with a Predict Function

When providing a `predict_fn` to `mlflow.genai.evaluate()`, the keys inside the `inputs` dictionary are expanded as keyword arguments to the predict function. For example, if `inputs` is `{"question": "Tell me about MLflow"}`, the predict function should accept a parameter named `question` and return a dictionary that becomes the `outputs` of that example.^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Accessing Evaluation Results

Evaluation results are stored as [[MLflow Trace|MLflow Traces]] containing assessments. Use `mlflow.search_traces(run_id=results.run_id)` to retrieve the traces. Each trace has an `.info.assessments` list where each assessment object has `name`, `value`, and `rationale` fields.^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Example

```python
eval_data = [
    {
        "inputs": {"request": "What is MLflow?"},
        "outputs": {
            "response": "MLflow is the largest open source AI engineering platform..."
        },
        "expectations": {
            "expected_response": "MLflow is the largest open source AI engineering platform..."
        },
    },
    {
        "inputs": {"request": "What is Databricks?"},
        "outputs": {"response": "Databricks is a unified analytics platform."},
        "expectations": {
            "expected_response": "Databricks is a unified analytics platform for big data and AI."
        },
    },
]
```

This data can be passed directly to `mlflow.genai.evaluate()` along with a list of [[Scorers]].^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Related Concepts

- [MLflow 3 GenAI](/concepts/mlflow-3-for-genai.md) — Overview of the GenAI evaluation framework.
- [[Scorers]] — Functions that produce assessments from evaluation data.
- [[MLflow Trace|MLflow Traces]] — The backend storage for evaluation results.
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) — The predecessor in MLflow 2.x that used a different schema.

## Sources

- migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md

# Citations

1. [migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md](/references/migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws-7eefbe86.md)
