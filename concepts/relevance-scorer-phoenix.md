---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 99f6df0360edf2b1818c079030d94aa32b8111a53bf917fac63ea4bf143ef4a3
  pageDirectory: concepts
  sources:
    - arize-phoenix-scorers-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - relevance-scorer-phoenix
    - RS(
  citations:
    - file: arize-phoenix-scorers-databricks-on-aws.md
title: Relevance scorer (Phoenix)
description: An Arize Phoenix scorer used within MLflow GenAI evaluation that measures how relevant an LLM's response is to the given query and context.
tags:
  - llm-evaluation
  - relevance-scoring
  - mlflow
timestamp: "2026-06-19T09:03:11.008Z"
---

# Relevance scorer (Phoenix)

The **Relevance scorer (Phoenix)** is a pre-built LLM-as-judge scorer available in MLflow’s GenAI evaluation framework. It measures how relevant a model’s output is to the input and supporting context, using a Phoenix-based evaluator. The scorer is imported from `mlflow.genai.scorers.phoenix` and is intended for use with `mlflow.genai.evaluate()`.^[arize-phoenix-scorers-databricks-on-aws.md]

## Usage

The `Relevance` scorer is instantiated with a `model` parameter that specifies which LLM to use as the judge. Below is a typical evaluation setup:^[arize-phoenix-scorers-databricks-on-aws.md]

```python
import mlflow
from mlflow.genai.scorers.phoenix import Hallucination, Relevance

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

results = mlflow.genai.evaluate(
    data=eval_dataset,
    scorers=[
        Hallucination(model="databricks:/databricks-gpt-5-mini"),
        Relevance(model="databricks:/databricks-gpt-5-mini"),
    ],
)
```

In the example above, each row provides the `query` (as `inputs`), the generated `outputs`, and an `expectations` dictionary containing a `context` field. The `Relevance` scorer uses that context—together with the query and output—to judge relevance. Multiple scorers (e.g., `Hallucination` and `Relevance`) can be passed in the same call.^[arize-phoenix-scorers-databricks-on-aws.md]

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `model`   | `str` | The model identifier used as the judge, e.g., `"databricks:/databricks-gpt-5-mini"`. The model endpoint must be accessible from the evaluation environment. |

The `model` argument is required. ^[arize-phoenix-scorers-databricks-on-aws.md]

## Integration with MLflow Evaluation

The `Relevance` scorer is designed to be passed into the `scorers` parameter of `mlflow.genai.evaluate()`. It runs automatically on every row in the evaluation dataset, returning a numeric or categorical score for relevance. The scorer can be combined with other Phoenix-based scorers (like `Hallucination`) or custom scorers.^[arize-phoenix-scorers-databricks-on-aws.md]

## Related Concepts

- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The framework in which Phoenix scorers are used.
- [Hallucination scorer (Phoenix)](/concepts/hallucination-scorer-phoenix.md) – A companion scorer for detecting hallucinations.
- [LLM-as-judge](/concepts/llm-as-a-judge.md) – The paradigm behind Phoenix scorers.
- Phoenix scorers on Databricks – Overview of all available Phoenix-based scorers.
- [GenAI agent evaluation](/concepts/genai-agent-evaluation-workflow.md) – Broader context for evaluating agent outputs.

## Sources

- arize-phoenix-scorers-databricks-on-aws.md

# Citations

1. [arize-phoenix-scorers-databricks-on-aws.md](/references/arize-phoenix-scorers-databricks-on-aws-53f4b817.md)
