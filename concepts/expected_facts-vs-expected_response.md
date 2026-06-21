---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0c442ebd1e8f494523500d582a76ef440307d1c2cdb506d96a4e8f023427c52a
  pageDirectory: concepts
  sources:
    - correctness-judge-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - expected_facts-vs-expected_response
    - EVE
    - EXPECTED_FACTS
    - EXPECTED_RESPONSE
    - Expected Facts
    - Expected Response
    - expected facts
  citations:
    - file: correctness-judge-databricks-on-aws.md
title: expected_facts vs expected_response
description: "Two alternative ground-truth parameters for the Correctness judge: expected_facts allows flexible fact-checking without requiring word-for-word matching, while expected_response requires a closer match to a reference answer."
tags:
  - llm-evaluation
  - mlflow
  - parameters
timestamp: "2026-06-19T17:54:04.035Z"
---

```markdown
---
title: expected_facts vs expected_response
summary: "Comparison of the two ground-truth formats for the Correctness judge: expected_facts (flexible, fact-level) vs expected_response (complete reference)."
sources:
  - correctness-judge-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T15:00:00.000Z"
updatedAt: "2026-06-19T15:00:00.000Z"
tags:
  - evaluation
  - genai
  - llm-judges
aliases:
  - expected_facts-vs-expected_response
  - EVE
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# expected_facts vs expected_response

**expected_facts** and **expected_response** are two alternative ground-truth formats for the [[Correctness judge]] in [[MLflow GenAI Evaluation]]. Both serve as reference data against which the judge compares an application's output to assess factual correctness, but they differ in flexibility and granularity.

## Overview

The `Correctness` judge evaluates whether a GenAI application's response is factually correct by comparing it against provided ground truth information. You can supply this ground truth using either `expected_facts` or `expected_response`, depending on the flexibility you need for the evaluation.^[correctness-judge-databricks-on-aws.md]

## expected_facts

`expected_facts` is a list of individual factual statements that the judge checks against the application's response. The judge determines whether each fact is supported or contradicted by the response.

### Advantages

- **More flexible evaluation**: The response doesn't need to match word‑for‑word — it just needs to contain the key facts.^[correctness-judge-databricks-on-aws.md]
- **Granular assessment**: The judge can identify which specific facts are present or missing in the response.
- **Tolerant of phrasing differences**: The judge recognizes factual correctness even when the response uses different wording or structure.

### Usage example

```python
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
```

^[correctness-judge-databricks-on-aws.md]

## expected_response

`expected_response` is a single reference response string that the judge compares against the application's output. The judge evaluates whether the actual response matches the expected response in content.

### Usage example

```python
feedback = correctness_judge(
    inputs={"request": "What is the capital of France?"},
    outputs={"response": "The capital of France is Paris."},
    expectations={"expected_response": "Paris is the capital of France."}
)
```

^[correctness-judge-databricks-on-aws.md]

## When to Use Each

| Criterion | expected_facts | expected_response |
|-----------|---------------|-------------------|
| **Flexibility** | High — checks for key facts regardless of phrasing | Lower — compares against a complete reference |
| **Granularity** | Per‑fact — identifies which facts are present or missing | Holistic — single comparison against the full response |
| **Best for** | Open‑ended questions where multiple valid phrasings exist | Questions with a single correct answer format |
| **Tolerance** | Accepts paraphrasing and different sentence structure | May be more sensitive to phrasing differences |

## Recommendation

The documentation recommends using `expected_facts` rather than `expected_response` for more flexible evaluation — the response doesn't need to match word‑for‑word, just contain the key facts.^[correctness-judge-databricks-on-aws.md]

## Using with mlflow.genai.evaluate()

Both formats work within the `mlflow.genai.evaluate()` function by including the expectations in the evaluation dataset.

### Using expected_facts

```python
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

### Using expected_response

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
    scorers=[Correctness()]
)
```

^[correctness-judge-databricks-on-aws.md]

## Judge Output

Regardless of which format you use, the [[Correctness judge]] returns a `Feedback` object with:
- **`value`**: "yes" if response is correct, "no" if incorrect
- **`rationale`**: Detailed explanation of which facts are supported or missing

^[correctness-judge-databricks-on-aws.md]

## Related Concepts

- [[Correctness judge]] — The built‑in LLM judge that evaluates against these ground truth formats.
- [[MLflow Evaluation UI|MLflow Evaluation]] — The evaluation framework that uses these judges.
- Judges for GenAI Evaluation — Overview of all judge types.
- [[Custom Judges]] — Building domain‑specific evaluation judges.
- [[Ground Truth in LLM Evaluation|Ground Truth in GenAI Evaluation]] — Broader context for using reference data.

## Sources

- correctness-judge-databricks-on-aws.md
```

# Citations

1. [correctness-judge-databricks-on-aws.md](/references/correctness-judge-databricks-on-aws-85181199.md)
