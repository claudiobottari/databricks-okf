---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: da0d617253344880787012f551fc23518e21cf80cd870c07c81432f74d9163cf
  pageDirectory: concepts
  sources:
    - arize-phoenix-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-evaluation-dataset-format
    - MGEDF
  citations:
    - file: arize-phoenix-scorers-databricks-on-aws.md
title: MLflow GenAI Evaluation Dataset Format
description: Structure for evaluation datasets in MLflow GenAI, requiring inputs, outputs, and expectations (with context) fields
tags:
  - mlflow
  - data-format
  - evaluation
timestamp: "2026-06-19T22:08:18.143Z"
---

# MLflow GenAI Evaluation Dataset Format

The **MLflow GenAI Evaluation Dataset Format** defines the structure of evaluation datasets used with `mlflow.genai.evaluate()` for assessing generative AI models, including large language models (LLMs) and agent-based systems. This format supports structured input-output pairs with optional expectation fields for comparison against ground truth.

## Dataset Structure

An evaluation dataset is a list of dictionaries, where each dictionary represents a single evaluation record (or "row"). Each record must contain `inputs` and `outputs` fields, and may optionally include an `expectations` field for computing accuracy or similarity metrics against reference data. ^[arize-phoenix-scorers-databricks-on-aws.md]

### Required Fields

- **`inputs`**: A dictionary containing the prompt or query passed to the model. The keys within this dictionary depend on the model signature and the scorers being used.
- **`outputs`**: A string containing the model's response or generated output for the corresponding inputs.

### Optional Fields

- **`expectations`**: A dictionary containing reference or ground-truth data used by scorers to evaluate the quality of the model's output. Commonly includes a `context` key providing supporting information for metrics like [Hallucination Detection](/concepts/hallucination-scorer.md) and Relevance Scoring.

## Example

The following example shows an evaluation dataset with two records, each containing inputs, outputs, and expectations:

```python
eval_dataset = [
    {
        "inputs": {"query": "What is MLflow?"},
        "outputs": "MLflow is an open-source AI engineering platform for agents and LLMs.",
        "expectations": {
            "context": "MLflow is an ML platform for experiment tracking and model deployment."
        },
    },
    {
        "inputs": {"query": "How do I track experiments?"},
        "outputs": "You can use mlflow.start_run() to begin tracking experiments.",
        "expectations": {
            "context": "MLflow provides APIs like mlflow.start_run() for experiment tracking."
        },
    },
]
```

^[arize-phoenix-scorers-databricks-on-aws.md]

## Usage with `mlflow.genai.evaluate()`

The dataset is passed as the `data` parameter to `mlflow.genai.evaluate()`, along with a list of scorers. The scorers access the appropriate fields from each record to compute evaluation metrics. For example, the `Hallucination` scorer uses the `inputs` query and `expectations.context` to determine whether the `outputs` contain hallucinated information, while the `Relevance` scorer assesses how well the `outputs` relate to the `inputs` query given the `expectations.context`. ^[arize-phoenix-scorers-databricks-on-aws.md]

```python
results = mlflow.genai.evaluate(
    data=eval_dataset,
    scorers=[
        Hallucination(model="databricks:/databricks-gpt-5-mini"),
        Relevance(model="databricks:/databricks-gpt-5-mini"),
    ],
)
```

## Field Semantics by Scorer Type

The meaning and required structure of fields may vary depending on the specific scorers used. Below are common conventions:

| Field | Purpose | Common Scorers Using This Field |
|---|---|---|
| `inputs.query` | The user query or prompt | Hallucination, Relevance |
| `outputs` | The model-generated response | Hallucination, Relevance |
| `expectations.context` | Reference context or ground truth | Hallucination, Relevance |

Scorers from different providers (such as [Arize Phoenix Scorers](/concepts/arize-phoenix-scorers.md)) may define additional or alternative field expectations. Always consult the specific scorer's documentation for exact field requirements.

## Related Concepts

- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The overall evaluation framework for generative AI models.
- [Hallucination Detection](/concepts/hallucination-scorer.md) — A metric that identifies whether model outputs contradict provided context.
- Relevance Scoring — A metric that measures how relevant model outputs are to the given query.
- [Arize Phoenix Scorers](/concepts/arize-phoenix-scorers.md) — A set of third-party scorers available for MLflow GenAI evaluation.
- [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md) — The foundational experiment management system underlying MLflow evaluations.
- [GenAI Scorers](/concepts/mlflow-genai-scorers.md) — The general mechanism for defining evaluation metrics in MLflow.

## Sources

- arize-phoenix-scorers-databricks-on-aws.md

# Citations

1. [arize-phoenix-scorers-databricks-on-aws.md](/references/arize-phoenix-scorers-databricks-on-aws-53f4b817.md)
