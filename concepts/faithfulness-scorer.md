---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 79c6c418219a95e8e5cd2c98ae19aade77dd62c898d4ba7221b012c42b5a4281
  pageDirectory: concepts
  sources:
    - ragas-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - faithfulness-scorer
  citations:
    - file: ragas-scorers-databricks-on-aws.md
    - file: deepeval-scorers-databricks-on-aws.md
title: Faithfulness Scorer
description: A RAGAS scorer that measures the factual consistency between the generated answer and the retrieved context, producing a score between 0.0 and 1.0 with an explanation.
tags:
  - evaluation
  - LLM
  - factuality
timestamp: "2026-06-19T20:07:19.520Z"
---

# Faithfulness Scorer

The **Faithfulness Scorer** is an [LLM-as-a-Judge](/concepts/llm-as-a-judge.md) metric that evaluates whether an AI-generated response contains claims that are directly supported by the provided context or source material. It detects hallucinations, unsupported assertions, and contradictions between the response and the reference information.

## Overview

Faithfulness scoring measures the factual consistency between a model's output and the context it was given. A low faithfulness score indicates that the response includes information not present in the source material, misrepresents the source, or fabricates details — a pattern commonly referred to as hallucination. The scorer returns a numerical score between 0.0 and 1.0, where 1.0 represents complete faithfulness and 0.0 represents no faithfulness. ^[ragas-scorers-databricks-on-aws.md]

Faithfulness can be evaluated using either the [RAGAS](/concepts/ragas-retrieval-augmented-generation-assessment.md) framework or the DeepEval framework, both of which are integrated with [MLflow GenAI](/concepts/mlflow-3-for-genai.md) as scorers for evaluation workflows. ^[ragas-scorers-databricks-on-aws.md, deepeval-scorers-databricks-on-aws.md]

## Using Faithfulness with RAGAS

### Requirements

Install the `ragas` package to use the RAGAS implementation of Faithfulness. ^[ragas-scorers-databricks-on-aws.md]

### Usage

The RAGAS Faithfulness scorer accepts a `trace` parameter and requires a `model` parameter specifying the LLM used for judging. ^[ragas-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers.ragas import Faithfulness

scorer = Faithfulness(model="databricks:/databricks-gpt-5-mini")
feedback = scorer(trace=trace)
print(feedback.value)  # Score between 0.0 and 1.0
print(feedback.rationale)  # Explanation of the score
```

To use the Faithfulness scorer with `mlflow.genai.evaluate()`: ^[ragas-scorers-databricks-on-aws.md]

```python
import mlflow
from mlflow.genai.scorers.ragas import Faithfulness

traces = mlflow.search_traces()
results = mlflow.genai.evaluate(
    data=traces,
    scorers=[
        Faithfulness(model="databricks:/databricks-gpt-5-mini"),
    ],
)
```

## Using Faithfulness with DeepEval

### Requirements

Install the `deepeval` package to use the DeepEval implementation of Faithfulness. ^[deepeval-scorers-databricks-on-aws.md]

### Usage

The DeepEval Faithfulness scorer accepts `inputs` and `outputs` parameters and requires a `model` parameter. It also accepts a `threshold` parameter that determines the pass/fail boundary. ^[deepeval-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers.deepeval import Faithfulness

scorer = Faithfulness(
    threshold=0.8,
    model="databricks:/databricks-gpt-5-mini",
)
feedback = scorer(
    inputs="What is MLflow?",
    outputs="MLflow is an open-source AI engineering platform for agents and LLMs.",
)
print(feedback.value)  # "yes" or "no"
print(feedback.metadata["score"])  # Numerical score
```

To use the Faithfulness scorer with `mlflow.genai.evaluate()`: ^[deepeval-scorers-databricks-on-aws.md]

```python
import mlflow
from mlflow.genai.scorers.deepeval import Faithfulness

eval_dataset = [
    {
        "inputs": {"query": "What is MLflow?"},
        "outputs": "MLflow is an open-source AI engineering platform for agents and LLMs.",
    },
    {
        "inputs": {"query": "How do I track experiments?"},
        "outputs": "You can use mlflow.start_run() to begin tracking experiments.",
    },
]

results = mlflow.genai.evaluate(
    data=eval_dataset,
    scorers=[
        Faithfulness(threshold=0.8, model="databricks:/databricks-gpt-5-mini"),
    ],
)
```

## Configuration

### RAGAS Faithfulness

| Parameter | Type | Description |
|-----------|------|-------------|
| `model` | `str` | The LLM used to judge faithfulness. Required. |
| `trace` | `object` | The execution trace containing context and response. |

^[ragas-scorers-databricks-on-aws.md]

### DeepEval Faithfulness

| Parameter | Type | Description |
|-----------|------|-------------|
| `model` | `str` | The LLM used to judge faithfulness. Required. |
| `threshold` | `float` | The pass/fail threshold for the binary verdict. |
| `include_reason` | `bool` | Whether to include a reasoning explanation. |

^[deepeval-scorers-databricks-on-aws.md]

## Comparison of Implementations

| Aspect | RAGAS Faithfulness | DeepEval Faithfulness |
|--------|-------------------|----------------------|
| Input format | `trace` (execution trace) | `inputs` and `outputs` (text) |
| Output format | Continuous score (0.0–1.0) | Binary verdict + numerical score |
| Rationale | Included in `feedback.rationale` | Optional via `include_reason` |
| Model parameter | Required | Required |

For metric-specific parameters and advanced usage options, see the [RAGAS documentation](https://docs.ragas.io/) or the [DeepEval documentation](https://docs.confident-ai.com/). ^[ragas-scorers-databricks-on-aws.md, deepeval-scorers-databricks-on-aws.md]

## Best Practices

- **Provide sufficient context.** Faithfulness scoring requires that the source context contains enough information to verify the response's claims. ^[ragas-scorers-databricks-on-aws.md]
- **Use a capable judge model.** The judging LLM should be sufficiently powerful (e.g., GPT-4 class) to accurately detect unsupported claims. ^[ragas-scorers-databricks-on-aws.md]
- **Set an appropriate threshold.** When using the DeepEval implementation, choose a threshold that aligns with your application's tolerance for hallucination. ^[deepeval-scorers-databricks-on-aws.md]
- **Combine with other metrics.** Faithfulness is often used alongside other metrics like Context Precision and Answer Relevancy for a comprehensive evaluation. ^[ragas-scorers-databricks-on-aws.md]

## Related Concepts

- [LLM-as-a-Judge](/concepts/llm-as-a-judge.md) — The evaluation paradigm underlying faithfulness scoring
- [RAGAS](/concepts/ragas-retrieval-augmented-generation-assessment.md) — The evaluation framework providing one implementation of faithfulness scoring
- DeepEval — The evaluation framework providing another implementation of faithfulness scoring
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The platform for running evaluations with scorers
- Context Precision — A complementary metric evaluating retrieval quality
- Answer Relevancy — A complementary metric evaluating response relevance
- [Hallucination Detection](/concepts/hallucination-scorer.md) — The broader problem space that faithfulness scoring addresses

## Sources

- ragas-scorers-databricks-on-aws.md
- deepeval-scorers-databricks-on-aws.md

# Citations

1. [ragas-scorers-databricks-on-aws.md](/references/ragas-scorers-databricks-on-aws-5240ee43.md)
2. [deepeval-scorers-databricks-on-aws.md](/references/deepeval-scorers-databricks-on-aws-95eb5ac0.md)
