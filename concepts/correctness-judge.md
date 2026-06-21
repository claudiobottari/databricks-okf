---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e0f61f2390f6af29e6f87ae42281149ac162b1d37f747cb2ea7ce5a0a670681e
  pageDirectory: concepts
  sources:
    - correctness-judge-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - correctness-judge
  citations:
    - file: correctness-judge-databricks-on-aws.md
title: Correctness Judge
description: An MLflow built-in LLM judge that evaluates whether a GenAI application's response is factually correct by comparing it against ground truth information (expected_facts or expected_response).
tags:
  - llm-evaluation
  - factual-correctness
  - mlflow
  - genai
timestamp: "2026-06-19T14:28:25.765Z"
---

Here is the wiki page for **Correctness Judge**, based solely on the provided source material.

---

## Correctness Judge

The **Correctness Judge** is a built-in [LLM judge](/concepts/llm-judges.md) in [MLflow](/concepts/mlflow.md) that evaluates whether a GenAI application's response is factually correct by comparing it against provided ground truth information. It accepts either `expected_facts` (a list of factual claims) or `expected_response` (a full reference answer) to determine correctness. ^[correctness-judge-databricks-on-aws.md]

## Overview

This judge is designed for assessing application outputs against known correct answers. It is part of MLflow's GenAI evaluation toolkit and returns a structured [Feedback (MLflow)|Feedback](/concepts/mlflow-feedback-object.md) object with a binary verdict (`value`) and a detailed justification (`rationale`). ^[correctness-judge-databricks-on-aws.md]

## Prerequisites

To use the Correctness judge, you must:

1. Install MLflow and required packages:
   ```python
   %pip install --upgrade "mlflow[databricks]>=3.4.0"
   dbutils.library.restartPython()
   ```
2. Create an MLflow experiment by following the [setup your environment quickstart](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment). ^[correctness-judge-databricks-on-aws.md]

## Usage Examples

The Correctness judge can be invoked directly or used with `mlflow.genai.evaluate()`.

### Invoke Directly

```python
from mlflow.genai.scorers import Correctness

correctness_judge = Correctness()

# Example 1: Response contains expected facts
feedback = correctness_judge(
    inputs={"request": "What is MLflow?"},
    outputs={"response": "MLflow is the largest open source AI engineering platform for agents, LLMs, and ML models."},
    expectations={
        "expected_facts": [
            "MLflow is open-source",
            "MLflow is an AI engineering platform"
        ]
    })
print(feedback.value)  # "yes"
print(feedback.rationale)  # Explanation of which facts are supported

# Example 2: Response missing or contradicting facts
feedback = correctness_judge(
    inputs={"request": "When was MLflow released?"},
    outputs={"response": "MLflow was released in 2017."},
    expectations={"expected_facts": ["MLflow was released in June 2018"]})

# Example 3: Using expected_response instead of expected_facts
feedback = correctness_judge(
    inputs={"request": "What is the capital of France?"},
    outputs={"response": "The capital of France is Paris."},
    expectations={"expected_response": "Paris is the capital of France."})
```

### Use with `evaluate()`

```python
eval_dataset_with_response = [
    {
        "inputs": {"query": "What is MLflow?"},
        "outputs": {
            "response": "MLflow is the largest open source AI engineering platform for agents, LLMs, and ML models."
        },
        "expectations": {
            "expected_response": "MLflow is the largest open source AI engineering platform for agents, LLMs, and ML models. MLflow enables teams of all sizes to debug, evaluate, monitor, and optimize their AI applications."
        },
    }
]

eval_results = mlflow.genai.evaluate(
    data=eval_dataset_with_response,
    scorers=[Correctness()])
```

> **Tip:** Use `expected_facts` rather than `expected_response` for more flexible evaluation — the response does not need to match word-for-word; it only needs to contain the key facts. ^[correctness-judge-databricks-on-aws.md]

## Selecting the LLM That Powers the Judge

By default, built-in judges use a Databricks-hosted LLM designed for quality assessments. You can change the judge model using the `model` argument when creating the judge. The model must be specified in the format `<provider>:/<model-name>`, where `<provider>` is a LiteLLM-compatible provider. For `databricks` provider, the model name is the same as the serving endpoint name.

```python
from mlflow.genai.scorers import Correctness

# Use a different judge model
correctness_judge = Correctness(
    model="databricks:/databricks-gpt-5-mini"  # Or any LiteLLM-compatible model
)

eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    scorers=[correctness_judge])
```

^[correctness-judge-databricks-on-aws.md]

## Interpreting Results

The judge returns a [Feedback (MLflow)|Feedback](/concepts/mlflow-feedback-object.md) object with two fields:

- **`value`**: `"yes"` if the response is correct, `"no"` if incorrect.
- **`rationale`**: A detailed explanation of which facts are supported or missing. ^[correctness-judge-databricks-on-aws.md]

## Related Concepts

- [MLflow evaluation](/concepts/mlflow-evaluation-ui.md) — Use judges in comprehensive application evaluation
- [LLM Judges](/concepts/llm-judges.md) — Overview of built-in quality evaluation judges
- [Custom Judges](/concepts/custom-judges.md) — Build domain-specific evaluation judges
- [Scorer (MLflow)](/concepts/scorers-mlflow-genai.md) — Mechanism for registering and running judges
- Feedback (MLflow) — The structured output object returned by judges

## Sources

- correctness-judge-databricks-on-aws.md

# Citations

1. [correctness-judge-databricks-on-aws.md](/references/correctness-judge-databricks-on-aws-85181199.md)
