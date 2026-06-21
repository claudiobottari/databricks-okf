---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 38bb77152f4fe720ff0b4cdf4866b6da3550e58be0ba0b67c93546d112e428c3
  pageDirectory: concepts
  sources:
    - arize-phoenix-scorers-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hallucination-scorer-phoenix
    - HS(
  citations:
    - file: arize-phoenix-scorers-databricks-on-aws.md
title: Hallucination scorer (Phoenix)
description: An Arize Phoenix scorer used within MLflow GenAI evaluation that detects factual inaccuracies or fabricated information in LLM outputs relative to provided context.
tags:
  - llm-evaluation
  - hallucination-detection
  - mlflow
timestamp: "2026-06-19T09:03:09.232Z"
---

# Hallucination scorer (Phoenix)

The **Hallucination scorer (Phoenix)** is a pre-built [MLflow GenAI](/concepts/mlflow-3-for-genai.md) scorer that detects whether a model’s output contains information unsupported by a provided reference context. It is part of the [Phoenix scorers](/concepts/arize-phoenix-scorers.md) library and is imported from `mlflow.genai.scorers.phoenix`. ^[arize-phoenix-scorers-databricks-on-aws.md]

## Usage

The scorer is instantiated with a model identifier — typically a [Databricks serving endpoint](/concepts/databricks-model-serving-endpoint.md) — and passed to `mlflow.genai.evaluate()` alongside an evaluation dataset. Each record in the dataset must include:

- `inputs`: the user query or conversation history.
- `outputs`: the model response to evaluate.
- `expectations`: a dictionary that contains a `context` key. The context provides the ground-truth information against which hallucination is measured.

For example:

```python
from mlflow.genai.scorers.phoenix import Hallucination

eval_dataset = [
    {
        "inputs": {"query": "What is MLflow?"},
        "outputs": "MLflow is an open-source AI engineering platform for agents and LLMs.",
        "expectations": {
            "context": "MLflow is an ML platform for experiment tracking and model deployment."
        },
    },
]

results = mlflow.genai.evaluate(
    data=eval_dataset,
    scorers=[
        Hallucination(model="databricks:/databricks-gpt-5-mini"),
    ],
)
```

^[arize-phoenix-scorers-databricks-on-aws.md]

## Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `model`   | Yes      | A Databricks model serving endpoint (e.g., `databricks:/databricks-gpt-5-mini`) used by the scorer to evaluate hallucination. ^[arize-phoenix-scorers-databricks-on-aws.md] |

## Relation to the evaluation dataset

The scorer relies on the `context` field inside each record’s `expectations` dictionary. It compares the generated `outputs` against this reference context to flag statements that are not supported. ^[arize-phoenix-scorers-databricks-on-aws.md]

## Related concepts

- [Relevance scorer (Phoenix)](/concepts/relevance-scorer-phoenix.md) — another Phoenix scorer that measures how relevant the output is to the query.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — the framework that orchestrates offline evaluation using scorers.
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — the structure expected by MLflow GenAI scorers.
- Hallucination detection — general techniques for identifying unsupported content.

## Sources

- arize-phoenix-scorers-databricks-on-aws.md

# Citations

1. [arize-phoenix-scorers-databricks-on-aws.md](/references/arize-phoenix-scorers-databricks-on-aws-53f4b817.md)
