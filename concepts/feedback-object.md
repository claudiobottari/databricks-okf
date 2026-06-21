---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 33e1583ca6d24853477b1001f97a11d812e48c31eec02239f48d723dbfec6f54
  pageDirectory: concepts
  sources:
    - correctness-judge-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feedback-object
    - Feedback
    - Feedback Entity
  citations:
    - file: correctness-judge-databricks-on-aws.md
title: Feedback Object
description: The return type of the Correctness judge containing a binary 'value' ('yes'/'no') indicating correctness and a 'rationale' string explaining which facts are supported or missing.
tags:
  - llm-evaluation
  - mlflow
  - api
timestamp: "2026-06-19T17:54:18.408Z"
---

# Feedback Object

The **Feedback object** is the standardized return type of [LLM judge](/concepts/llm-judges.md) evaluations in MLflow. It encapsulates the judgment result and a human-readable explanation, enabling structured processing of assessment outcomes.

## Structure

A `Feedback` object contains two fields:

- **`value`**: A string representing the judgment. For the [Correctness Judge](/concepts/correctness-judge.md), the value is `"yes"` if the evaluated response is factually correct, or `"no"` if it is incorrect. ^[correctness-judge-databricks-on-aws.md]
- **`rationale`**: A detailed explanation supporting the judgment. For the correctness judge, the rationale describes which expected facts are supported or missing. ^[correctness-judge-databricks-on-aws.md]

## Usage in the Correctness Judge

The `Feedback` object is returned when a built-in judge is invoked directly or used inside `mlflow.genai.evaluate()`. The following example demonstrates direct invocation with the correctness judge:

```python
from mlflow.genai.scorers import Correctness

correctness_judge = Correctness()

feedback = correctness_judge(
    inputs={"request": "What is MLflow?"},
    outputs={"response": "MLflow is the largest open source AI engineering platform for agents, LLMs, and ML models."},
    expectations={
        "expected_facts": [
            "MLflow is open-source",
            "MLflow is an AI engineering platform"
        ]
    }
)

print(feedback.value)   # "yes"
print(feedback.rationale)  # Explanation of which facts are supported
```

^[correctness-judge-databricks-on-aws.md]

When the response is missing or contradicts the expected facts, `feedback.value` is `"no"`. The same pattern applies when using `expected_response` instead of `expected_facts`. ^[correctness-judge-databricks-on-aws.md]

## Judge Customization

The LLM that powers the judge can be changed using the `model` argument. The returned object remains a `Feedback` object regardless of the underlying model. ^[correctness-judge-databricks-on-aws.md]

## See also

- [LLM Judges](/concepts/llm-judges.md) – Overview of built-in and custom judges
- [Correctness Judge](/concepts/correctness-judge.md) – Evaluates factual correctness against ground truth
- [Custom Judges](/concepts/custom-judges.md) – Creating domain-specific judges with `make_judge()`
- [MLflow evaluation](/concepts/mlflow-evaluation-ui.md) – Using judges in comprehensive application evaluation

## Sources

- correctness-judge-databricks-on-aws.md

# Citations

1. [correctness-judge-databricks-on-aws.md](/references/correctness-judge-databricks-on-aws-85181199.md)
