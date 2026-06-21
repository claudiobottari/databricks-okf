---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e9769314bba826e0e9b8896dbe1655e2f46778d822b538de79ce2b9c24d36c10
  pageDirectory: concepts
  sources:
    - deepeval-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - answerrelevancy-scorer
    - Answer Relevance Judge
  citations:
    - file: deepeval-scorers-databricks-on-aws.md
title: AnswerRelevancy Scorer
description: A DeepEval scorer that evaluates how relevant a model's answer is to the given input query, with configurable thresholds and scoring models.
tags:
  - deepeval
  - scorer
  - answer-relevancy
  - llm-evaluation
timestamp: "2026-06-19T18:19:41.353Z"
---

# AnswerRelevancy Scorer

The **AnswerRelevancy Scorer** is a DeepEval metric integrated with [MLflow](/concepts/mlflow.md) that evaluates how relevant an LLM's generated answer is to a given input query. It is one of the DeepEval scorers available through `mlflow.genai.scorers.deepeval` and is categorized under RAG Evaluation metrics for assessing retrieval quality and answer generation in [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) applications. ^[deepeval-scorers-databricks-on-aws.md]

## Overview

The AnswerRelevancy Scorer measures the degree to which a generated response addresses the specific question or input provided. It returns a numeric relevance score and a pass/fail decision based on a configurable threshold. This allows developers to automatically filter out outputs that are off-topic, contain irrelevant information, or fail to properly address the user's query. ^[deepeval-scorers-databricks-on-aws.md]

## Requirements

The `deepeval` package must be installed in the runtime environment. ^[deepeval-scorers-databricks-on-aws.md]

## Usage

### Quick Start

To call an AnswerRelevancy scorer directly:

```python
from mlflow.genai.scorers.deepeval import AnswerRelevancy

scorer = AnswerRelevancy(
    threshold=0.7,
    model="databricks:/databricks-gpt-5-mini"
)

feedback = scorer(
    inputs="What is MLflow?",
    outputs="MLflow is an open-source AI engineering platform for agents and LLMs.",
)

print(feedback.value)            # "yes" or "no"
print(feedback.metadata["score"]) # 0.85
```

^[deepeval-scorers-databricks-on-aws.md]

### Within MLflow Evaluation

To use the scorer within `mlflow.genai.evaluate()`:

```python
import mlflow
from mlflow.genai.scorers.deepeval import AnswerRelevancy

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
        AnswerRelevancy(
            threshold=0.7,
            model="databricks:/databricks-gpt-5-mini"
        ),
    ],
)
```

^[deepeval-scorers-databricks-on-aws.md]

### Return Values

The scorer returns structured feedback with:
- **`value`**: A string (`"yes"` or `"no"`) indicating whether the score meets the configured threshold.
- **`metadata["score"]`**: A numeric relevance score (e.g., `0.85`). ^[deepeval-scorers-databricks-on-aws.md]

## Creating a Scorer by Name

You can dynamically instantiate an AnswerRelevancy scorer using `get_scorer` with the metric name as a string:

```python
from mlflow.genai.scorers.deepeval import get_scorer

scorer = get_scorer(
    metric_name="AnswerRelevancy",
    threshold=0.7,
    model="databricks:/databricks-gpt-5-mini",
)
feedback = scorer(
    inputs="What is MLflow?",
    outputs="MLflow is a platform for ML workflows.",
)
```

^[deepeval-scorers-databricks-on-aws.md]

## Configuration

The AnswerRelevancy scorer accepts metric-specific parameters as keyword arguments to its constructor. As an LLM-based metric, it requires a `model` parameter. Common configuration parameters include:

| Parameter | Type | Description |
|-----------|------|-------------|
| `model` | string | (Required) The LLM model to use for evaluation, e.g., `"databricks:/databricks-gpt-5-mini"` or `"openai:/gpt-4o"`. |
| `threshold` | float | The pass/fail threshold for the relevance score (e.g., `0.7`). |
| `include_reason` | bool | Whether to include a reasoning field in the feedback. |

For metric-specific parameters and advanced usage options, refer to the [DeepEval documentation](https://docs.confident-ai.com/). ^[deepeval-scorers-databricks-on-aws.md]

## Related Concepts

- DeepEval — The evaluation framework that provides this scorer.
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The platform for evaluating and monitoring GenAI applications.
- RAG Evaluation — Broader context of evaluating retrieval-augmented generation systems.
- [Faithfulness Scorer](/concepts/faithfulness-scorer.md) — A complementary DeepEval metric for evaluating factual accuracy.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying scorers for continuous quality monitoring.
- [Answer Correctness Scorer](/concepts/correctness-scorer.md) — A related metric that evaluates factual correctness of answers.

## Sources

- deepeval-scorers-databricks-on-aws.md

# Citations

1. [deepeval-scorers-databricks-on-aws.md](/references/deepeval-scorers-databricks-on-aws-95eb5ac0.md)
