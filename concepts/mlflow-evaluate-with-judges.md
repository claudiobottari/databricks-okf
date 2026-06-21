---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f7e839a506f2fc85c3eea5753fc40dcf9b79d9d4ead4956e44a0130275862de7
  pageDirectory: concepts
  sources:
    - correctness-judge-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-evaluate-with-judges
    - MEWJ
  citations:
    - file: correctness-judge-databricks-on-aws.md
title: MLflow evaluate with Judges
description: The pattern of using mlflow.genai.evaluate() with a dataset and one or more scorer/judge instances to perform comprehensive GenAI application evaluation.
tags:
  - mlflow
  - evaluation
  - workflow
timestamp: "2026-06-18T14:46:18.248Z"
---

# MLflow Evaluate with Judges

**MLflow evaluate with Judges** refers to the use of LLM-based judges as scorers within the `mlflow.genai.evaluate()` API to assess the quality of GenAI application outputs. Judges are automated evaluators that compare responses against criteria such as factual correctness, and they return structured feedback including a score and a rationale.

## Overview

Judges are invoked as part of the evaluation pipeline by passing one or more scorer objects to the `scorers` parameter of `mlflow.genai.evaluate()`. Each judge analyzes a set of inputs and outputs (and optionally expectations) and produces a rating. This enables systematic, reproducible quality assessment without requiring human annotation for every evaluation run. ^[correctness-judge-databricks-on-aws.md]

## Example: The Correctness Judge

The `Correctness` judge is a built-in judge that evaluates whether a response is factually correct by comparing it against provided ground truth information, either as a list of `expected_facts` or as an `expected_response`. It is designed for evaluating application responses against known correct answers. ^[correctness-judge-databricks-on-aws.md]

### Usage with `mlflow.genai.evaluate()`

```python
from mlflow.genai.scorers import Correctness

# Define an evaluation dataset with expectations
eval_dataset = [
    {
        "inputs": {"query": "What is MLflow?"},
        "outputs": {"response": "MLflow is the largest open source AI engineering platform."},
        "expectations": {"expected_facts": ["MLflow is open-source", "MLflow is an AI engineering platform"]}
    }
]

# Run evaluation with the Correctness judge
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    scorers=[Correctness()]
)
```

^[correctness-judge-databricks-on-aws.md]

The judge returns a `Feedback` object per evaluation row containing:
- **`value`**: `"yes"` if the response is correct, `"no"` if incorrect.
- **`rationale`**: A detailed explanation of which facts are supported or missing.

^[correctness-judge-databricks-on-aws.md]

### Choosing Between `expected_facts` and `expected_response`

Using `expected_facts` (a list of key facts) allows more flexible evaluation because the response does not need to match word-for-word—it only needs to contain the key facts. `expected_response` is an alternative that provides a full expected answer. ^[correctness-judge-databricks-on-aws.md]

## Selecting the LLM that Powers the Judge

By default, built‑in judges use a Databricks‑hosted LLM. You can change the judge model by using the `model` argument when instantiating the judge. The model must be specified in the format `<provider>:/<model-name>`, where `<provider>` is a LiteLLM‑compatible model provider. For example, to use a different judge model:

```python
correctness_judge = Correctness(
    model="databricks:/databricks-gpt-5-mini"
)
```

^[correctness-judge-databricks-on-aws.md]

## Interpreting Results

The judge’s output can be collected from the evaluation results object. The `value` field provides a binary or categorical rating, while `rationale` explains the reasoning. This information can be used to compare different model versions or agent configurations. ^[correctness-judge-databricks-on-aws.md]

## Related Judges and Extensions

The source material references other built‑in judges and the ability to [create custom judges](/concepts/custom-judges.md) for domain‑specific evaluations. For a complete list of built‑in judges, see the MLflow documentation on quality evaluation judges. ^[correctness-judge-databricks-on-aws.md]

## Prerequisites

To use judges with MLflow evaluation:

1. Install MLflow and required packages: `%pip install --upgrade "mlflow[databricks]>=3.4.0"`
2. Create an MLflow experiment following the setup your environment quickstart.

^[correctness-judge-databricks-on-aws.md]

## Related Concepts

- [Built-in Judges](/concepts/built-in-judges.md) – Pre‑configured LLM judges for common quality metrics.
- [Custom Judges](/concepts/custom-judges.md) – Build domain‑specific evaluation judges using `make_judge()`.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The `mlflow.genai.evaluate()` API for offline assessment.
- GenAI Agent Evaluation – Applying judges to evaluate agent behavior.
- Human Feedback Alignment – Improving judge accuracy with expert annotations.

## Sources

- correctness-judge-databricks-on-aws.md

# Citations

1. [correctness-judge-databricks-on-aws.md](/references/correctness-judge-databricks-on-aws-85181199.md)
