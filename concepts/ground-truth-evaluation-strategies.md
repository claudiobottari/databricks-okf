---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 39e5734f6424cba3211982414f528f58c6bef8a2b02bcb90b080debe3e6dee33
  pageDirectory: concepts
  sources:
    - correctness-judge-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ground-truth-evaluation-strategies
    - GTES
  citations:
    - file: correctness-judge-databricks-on-aws.md
title: Ground Truth Evaluation Strategies
description: "Two approaches for evaluating LLM response correctness: expected_facts allows flexible fact-level checking, while expected_response requires more exact response matching."
tags:
  - llm-evaluation
  - evaluation-methods
  - ground-truth
timestamp: "2026-06-19T14:28:03.147Z"
---

# Ground Truth Evaluation Strategies

**Ground Truth Evaluation Strategies** refer to the methods and approaches for assessing the factual correctness of a GenAI application's responses by comparing them against known correct answers or verified facts. These strategies are essential for ensuring that AI-generated outputs are accurate, reliable, and aligned with expected knowledge.

## Overview

Ground truth evaluation involves measuring whether an AI system's response contains the correct information by comparing it against a trusted reference. This reference can take the form of specific facts that must be present in the response, or a complete expected response that the output should match in substance. The choice of strategy depends on the evaluation goals, the flexibility required, and the nature of the task being assessed. ^[correctness-judge-databricks-on-aws.md]

## Core Strategies

### Expected Facts Strategy

The **expected facts strategy** evaluates responses by checking whether they contain a specified set of factual statements. This approach offers flexibility because the response does not need to match a reference answer word-for-word — it only needs to include the key facts. ^[correctness-judge-databricks-on-aws.md]

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
```

This strategy is recommended when the evaluation should tolerate variations in phrasing, structure, or detail, as long as the core factual claims are present. ^[correctness-judge-databricks-on-aws.md]

### Expected Response Strategy

The **expected response strategy** evaluates responses by comparing them against a complete reference answer. This approach is more strict, as the judge assesses whether the generated response aligns with the full expected response. ^[correctness-judge-databricks-on-aws.md]

```python
feedback = correctness_judge(
    inputs={"request": "What is the capital of France?"},
    outputs={"response": "The capital of France is Paris."},
    expectations={"expected_response": "Paris is the capital of France."}
)
```

This strategy is appropriate when there is a single correct answer format and the evaluation requires close alignment with a canonical response. ^[correctness-judge-databricks-on-aws.md]

## Comparison of Strategies

| Strategy | Input Format | Flexibility | Best Use Case |
|----------|-------------|-------------|---------------|
| Expected Facts | List of factual statements | High — allows varied phrasing | Open-ended questions, summarization, knowledge retrieval |
| Expected Response | Complete reference answer | Lower — expects close alignment | Factual queries with single correct answer, Q&A benchmarks |

The expected facts strategy is generally preferred for more flexible evaluation, as it does not penalize responses that convey the same information using different wording or structure. ^[correctness-judge-databricks-on-aws.md]

## Implementation with Built-in Judges

### Using the Correctness Judge

The [Correctness Judge](/concepts/correctness-judge.md) is a built-in [LLM judge](/concepts/llm-judges.md) that supports both ground truth evaluation strategies. It returns a `Feedback` object with:

- **`value`**: `"yes"` if the response is correct, `"no"` if incorrect
- **`rationale`**: A detailed explanation of which facts are supported or missing

^[correctness-judge-databricks-on-aws.md]

### Using with `mlflow.genai.evaluate()`

Both strategies can be used within the [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) framework:

```python
# Using expected_facts
eval_dataset_with_facts = [
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
        },
    }
]

eval_results = mlflow.genai.evaluate(
    data=eval_dataset_with_facts,
    scorers=[Correctness()]
)
```

```python
# Using expected_response
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
    scorers=[Correctness()]
)
```

^[correctness-judge-databricks-on-aws.md]

## Selecting the Judge Model

By default, built-in judges use a Databricks-hosted LLM designed for quality assessments. You can customize the judge model using the `model` argument:

```python
from mlflow.genai.scorers import Correctness

correctness_judge = Correctness(
    model="databricks:/databricks-gpt-5-mini"  # Or any LiteLLM-compatible model
)
```

The model must be specified in the format `<provider>:/<model-name>`, where `<provider>` is a LiteLLM-compatible model provider. If using `databricks` as the provider, the model name corresponds to the serving endpoint name. ^[correctness-judge-databricks-on-aws.md]

## Best Practices

- **Prefer expected facts over expected response** for most use cases, as it provides more flexible and robust evaluation that accommodates natural language variation. ^[correctness-judge-databricks-on-aws.md]
- **Ensure ground truth facts are atomic and verifiable** — each fact should be a single, unambiguous claim that can be independently checked.
- **Cover edge cases in your evaluation dataset** — include examples where the response is partially correct, contains extra information, or omits key facts.
- **Use consistent ground truth across evaluation runs** to enable fair comparison between different agent configurations or model versions.
- **Review judge rationales** to understand why responses passed or failed, which can reveal gaps in the ground truth definitions or the judge's interpretation.

## Related Concepts

- [Correctness Judge](/concepts/correctness-judge.md) — The built-in LLM judge that implements ground truth evaluation
- [LLM Judges](/concepts/llm-judges.md) — AI-based evaluators that assess response quality
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The framework for running evaluations with judges
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Comparing agent variants using consistent evaluation criteria
- [Custom Judges](/concepts/custom-judges.md) — Creating domain-specific evaluators with `make_judge()`
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Structured data used for systematic evaluation

## Sources

- correctness-judge-databricks-on-aws.md

# Citations

1. [correctness-judge-databricks-on-aws.md](/references/correctness-judge-databricks-on-aws-85181199.md)
