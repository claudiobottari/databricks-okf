---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 88b311fd8ae9a786a69f03ae6e8d80730fba5f50092c488fdab2f24634eaddde
  pageDirectory: concepts
  sources:
    - correctness-judge-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ground-truth-comparison-strategies
    - GTCS
  citations:
    - file: correctness-judge-databricks-on-aws.md
title: Ground Truth Comparison Strategies
description: "Two approaches for providing ground truth to the Correctness judge: expected_facts (list of atomic facts) for flexible matching, and expected_response (full expected answer) for stricter comparison."
tags:
  - mlflow
  - llm-evaluation
  - evaluation-strategy
timestamp: "2026-06-18T11:11:48.666Z"
---

# Ground Truth Comparison Strategies

**Ground Truth Comparison Strategies** are approaches used by [LLM-as-a-Judge](/concepts/llm-as-a-judge.md) scorers to evaluate the factual correctness of a GenAI application's response against known correct reference information. These strategies are central to the [Correctness Judge](/concepts/correctness-judge.md), a built-in MLflow judge that compares application outputs against either a set of expected facts or a complete expected response to determine if the response is factually accurate.^[correctness-judge-databricks-on-aws.md]

## Overview

Ground truth comparison enables automated evaluation of whether a GenAI application generates factually correct answers. Rather than evaluating stylistic quality or adherence to instructions, these strategies focus on whether the content of the response matches a pre-defined set of facts or a reference answer. ^[correctness-judge-databricks-on-aws.md]

The comparison is performed by an LLM judge that returns a structured `Feedback` object with two components:

- **`value`**: `"yes"` if the response is factually correct, `"no"` if it contains inaccuracies or omits required facts.
- **`rationale`**: A detailed explanation of which facts are supported by the response and which are missing or contradicted.

^[correctness-judge-databricks-on-aws.md]

## Two Comparison Strategies

### Expected Facts Strategy

The `expected_facts` strategy evaluates a response by checking whether it contains a specified set of atomic facts, regardless of exact wording. This approach provides more flexible evaluation because the response does not need to match the reference text word-for-word—it only needs to include the key factual claims that the evaluator considers essential.^[correctness-judge-databricks-on-aws.md]

**Example usage:**

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
print(feedback.value)  # "yes"
print(feedback.rationale)  # Explanation of which facts are supported
```

^[correctness-judge-databricks-on-aws.md]

When a response is missing or contradicts required facts, the judge returns `"no"` with a rationale explaining what was incorrect or absent:

```python
feedback = correctness_judge(
    inputs={"request": "When was MLflow released?"},
    outputs={"response": "MLflow was released in 2017."},
    expectations={"expected_facts": ["MLflow was released in June 2018"]}
)
# Returns value="no"
```

^[correctness-judge-databricks-on-aws.md]

### Expected Response Strategy

The `expected_response` strategy compares the application's output against a complete reference answer. This is a stricter comparison than `expected_facts`, as it evaluates whether the response aligns with the full reference text. However, word-for-word matching is not required—the LLM judge evaluates semantic equivalence.^[correctness-judge-databricks-on-aws.md]

**Example usage:**

```python
feedback = correctness_judge(
    inputs={"request": "What is the capital of France?"},
    outputs={"response": "The capital of France is Paris."},
    expectations={"expected_response": "Paris is the capital of France."}
)
# Returns value="yes" (semantically equivalent)
```

^[correctness-judge-databricks-on-aws.md]

## Selecting the Right Strategy

The documentation provides guidance on when to use each strategy:^[correctness-judge-databricks-on-aws.md]

| Strategy | When to Use | Advantages |
|---|---|---|
| `expected_facts` | When the key factual requirements are known but the exact response wording is flexible | More flexible evaluation; response only needs to contain key facts, not match exact phrasing |
| `expected_response` | When a complete reference answer is available and semantic alignment matters | Captures completeness and phrasing alignment beyond just factual inclusion |

The `expected_facts` strategy is generally preferred as it provides more flexible evaluation—the response does not need to match word-for-word, only contain the key facts.^[correctness-judge-databricks-on-aws.md]

## Using Strategies with `mlflow.genai.evaluate()`

Ground truth comparison strategies can also be used with the `mlflow.genai.evaluate()` API for batch evaluation. Each row in the evaluation dataset includes an `expectations` field that contains either `expected_facts` or `expected_response`:^[correctness-judge-databricks-on-aws.md]

```python
eval_dataset = [
    {
        "inputs": {"query": "What is MLflow?"},
        "outputs": {
            "response": "MLflow is the largest open source AI engineering platform for agents, LLMs, and ML models."
        },
        "expectations": {
            "expected_facts": [
                "MLflow is open-source",
                "MLflow is an AI engineering platform"
            ]
        }
    }
]

eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    scorers=[Correctness()]
)
```

^[correctness-judge-databricks-on-aws.md]

## Customizing the Judge Model

By default, built-in judges use a Databricks-hosted LLM designed for GenAI quality assessments. You can change the judge model by using the `model` argument when creating the judge. The model must be specified in the format `<provider>:/<model-name>`, where `<provider>` is a LiteLLM-compatible model provider. If using `databricks` as the provider, the model name is the same as the serving endpoint name.^[correctness-judge-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Correctness

# Use a different judge model
correctness_judge = Correctness(
    model="databricks:/databricks-gpt-5-mini"  # Or any LiteLLM-compatible model
)

# Use in evaluation
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    scorers=[correctness_judge]
)
```

^[correctness-judge-databricks-on-aws.md]

## Best Practices

### Prefer `expected_facts` over `expected_response`

Using `expected_facts` rather than `expected_response` provides more flexible evaluation—the response does not need to match word-for-word, just contain the key facts. This is particularly important for generative applications where verbatim repetition is neither expected nor desirable.^[correctness-judge-databricks-on-aws.md]

### Design Atomic Facts

Break ground truth into small, testable atomic facts. Each fact should be a single, verifiable claim that is either present or absent in the response. Avoid combining multiple assertions into one fact, as this makes it harder to identify which specific information the response is missing.^[correctness-judge-databricks-on-aws.md]

### Include Complete Reference Material

When using `expected_response`, include a response that contains all the information the application should convey. The judge will evaluate whether the application's output is semantically aligned with this reference, so completeness of the reference matters.^[correctness-judge-databricks-on-aws.md]

### Use Consistent Ground Truth Across Evaluations

For meaningful trend analysis, use the same ground truth facts across evaluation runs on the same type of query. Changing the ground truth between runs makes it impossible to compare correctness scores over time.^[correctness-judge-databricks-on-aws.md]

## Related Concepts

- [Correctness Judge](/concepts/correctness-judge.md) — The built-in MLflow judge that implements ground truth comparison strategies
- [LLM-as-a-Judge](/concepts/llm-as-a-judge.md) — The paradigm of using language models as evaluators
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The broader evaluation framework for GenAI applications
- [Synthetic Evaluation Set Generation](/concepts/synthetic-evaluation-data-generation.md) — Automated creation of evaluation datasets with ground truth
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) — Evaluation workflows that can benefit from ground truth comparison
- Feedback (MLflow) — The structured output object returned by scorers including judges

## Sources

- correctness-judge-databricks-on-aws.md

# Citations

1. [correctness-judge-databricks-on-aws.md](/references/correctness-judge-databricks-on-aws-85181199.md)
