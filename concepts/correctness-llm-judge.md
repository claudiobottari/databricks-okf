---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 78917a5a2f9351f79e3f8f1d0031019a58a70909ec612d5b3e544bd52a0df581
  pageDirectory: concepts
  sources:
    - correctness-judge-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - correctness-llm-judge
    - CLJ
  citations:
    - file: correctness-judge-databricks-on-aws.md
title: Correctness LLM Judge
description: A built-in LLM judge that evaluates whether a GenAI application's response is factually correct by comparing it against provided ground truth information (expected_facts or expected_response).
tags:
  - llm-evaluation
  - genai
  - mlflow
timestamp: "2026-06-19T17:54:27.388Z"
---

Here is the wiki page for "Correctness LLM Judge", written based solely on the provided source material.

---

## Correctness LLM Judge

The **Correctness LLM Judge** is a built-in [LLM-as-judge|judge](/concepts/llm-as-a-judge.md) provided by [MLflow GenAI](/concepts/mlflow-3-for-genai.md) that evaluates whether a GenAI application's response is factually correct. It compares the response against provided ground truth information, either as a list of expected facts (`expected_facts`) or as an expected reference response (`expected_response`). ^[correctness-judge-databricks-on-aws.md]

### Overview

This judge is designed for scenarios where known correct answers exist, such as question-answering, fact verification, or any task where the output must contain specific factual content. It returns a structured `Feedback` object with a value of `"yes"` (response is correct) or `"no"` (response is incorrect), accompanied by a detailed rationale explaining which facts are supported or missing. ^[correctness-judge-databricks-on-aws.md]

### Prerequisites

To use the Correctness judge, you need:

- MLflow version `3.4.0` or later installed with the `databricks` extra: `%pip install --upgrade "mlflow[databricks]>=3.4.0"`
- An MLflow experiment set up following the [setup environment quickstart](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment). ^[correctness-judge-databricks-on-aws.md]

### Usage Examples

**Direct invocation**

The judge can be called directly with `inputs`, `outputs`, and `expectations`: ^[correctness-judge-databricks-on-aws.md]

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
    }
)
print(feedback.value)  # "yes"
print(feedback.rationale)  # Explanation of which facts are supported

# Example 2: Response missing or contradicting facts
feedback = correctness_judge(
    inputs={"request": "When was MLflow released?"},
    outputs={"response": "MLflow was released in 2017."},
    expectations={"expected_facts": ["MLflow was released in June 2018"]}
)
# Returns "no"

# Example 3: Using expected_response instead of expected_facts
feedback = correctness_judge(
    inputs={"request": "What is the capital of France?"},
    outputs={"response": "The capital of France is Paris."},
    expectations={"expected_response": "Paris is the capital of France."}
)
```

**Using `mlflow.genai.evaluate()`**

The judge can also be included in a full evaluation run: ^[correctness-judge-databricks-on-aws.md]

```python
eval_dataset = [
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
    data=eval_dataset,
    scorers=[Correctness()]
)
```

**Choosing between `expected_facts` and `expected_response`**

Use `expected_facts` rather than `expected_response` for more flexible evaluation — the response does not need to match word-for-word; it only needs to contain the key facts listed. ^[correctness-judge-databricks-on-aws.md]

### Selecting the LLM That Powers the Judge

By default, built-in judges use a Databricks-hosted LLM optimized for GenAI quality assessments. You can change the judge model using the `model` argument when creating the judge: ^[correctness-judge-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Correctness

# Use a different judge model (LiteLLM-compatible)
correctness_judge = Correctness(
    model="databricks:/databricks-gpt-5-mini"
)
```

The model must be specified in the format `<provider>:/<model-name>`, where `<provider>` is a LiteLLM-compatible model provider. If using `databricks` as the provider, the model name corresponds to the serving endpoint name. ^[correctness-judge-databricks-on-aws.md]

### Interpreting Results

The judge returns a `Feedback` object containing:

- **`value`**: `"yes"` if the response is factually correct, `"no"` if incorrect.
- **`rationale`**: A detailed explanation of which expected facts are supported or missing in the response. ^[correctness-judge-databricks-on-aws.md]

### Related Concepts

- [Custom Judges](/concepts/custom-judges.md) — Build domain-specific evaluation judges.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — Comprehensive guide to running evaluations.
- Other Built-in Judges — Explore additional quality evaluation judges.
- [LLM-as-judge](/concepts/llm-as-a-judge.md) — The general paradigm of using LLMs for evaluation.

### Sources

- correctness-judge-databricks-on-aws.md

# Citations

1. [correctness-judge-databricks-on-aws.md](/references/correctness-judge-databricks-on-aws-85181199.md)
