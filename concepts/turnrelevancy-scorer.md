---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 916e2a22401d9cb05eb153632c4c0b090d144da159e91daddc0f31ba641d88eb
  pageDirectory: concepts
  sources:
    - deepeval-scorers-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - turnrelevancy-scorer
  citations:
    - file: deepeval-scorers-databricks-on-aws.md
title: TurnRelevancy Scorer
description: A conversational DeepEval scorer that evaluates relevance in multi-turn dialogue, supporting parameters like window_size and strict_mode.
tags:
  - scorer
  - conversational-ai
  - relevance
timestamp: "2026-06-18T11:47:59.447Z"
---

<!--
title: TurnRelevancy Scorer
summary: A DeepEval conversational metric that evaluates the relevance of each turn in a multi-turn dialogue, ensuring that responses stay on topic and address the user's intent.
sources:
  - deepeval-scorers-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:00:00.000Z"
updatedAt: "2026-06-18T12:00:00.000Z"
tags:
  - deepeval
  - scoring
  - evaluation
  - conversational-ai
  - mlflow
aliases:
  - turn-relevancy-scorer
  - turnrelevancy
confidence: 0.8
provenanceState: extracted
inferredParagraphs: 1
-->

# TurnRelevancy Scorer

The **TurnRelevancy Scorer** is a conversational metric provided by the [DeepEval](https://docs.confident-ai.com/) evaluation framework and integrated into [MLflow](/concepts/mlflow.md) as a built-in scorer. It evaluates the relevance of each individual turn in a multi-turn dialogue, checking whether the model's response stays on topic and properly addresses the user's latest input. ^[deepeval-scorers-databricks-on-aws.md]

This scorer is part of DeepEval's **conversational metrics** category, which focuses on measuring the quality of interactive, multi-turn AI conversations. ^[deepeval-scorers-databricks-on-aws.md]

## Usage[​](#usage "Direct link to Usage")

The TurnRelevancy scorer can be instantiated and used directly, or passed to `mlflow.genai.evaluate()` as a scorer. ^[deepeval-scorers-databricks-on-aws.md]

### Direct invocation

```python
from mlflow.genai.scorers.deepeval import TurnRelevancy

scorer = TurnRelevancy(
    model="openai:/gpt-4o",
    threshold=0.8,
    window_size=3,
    strict_mode=True,
)

feedback = scorer(
    inputs={
        "conversation": [
            {"role": "user", "content": "What is MLflow?"},
            {"role": "assistant", "content": "MLflow is a platform for managing ML workflows."},
            {"role": "user", "content": "Can it handle deep learning?"},
        ],
    },
    outputs="Yes, MLflow supports deep learning frameworks like PyTorch and TensorFlow.",
)
print(feedback.value)    # "yes" or "no"
print(feedback.metadata) # includes score and other details
```

### In evaluation runs

```python
import mlflow
from mlflow.genai.scorers.deepeval import TurnRelevancy

eval_dataset = [
    {
        "inputs": {"conversation": [...]},
        "outputs": "...",
    },
]

results = mlflow.genai.evaluate(
    data=eval_dataset,
    scorers=[TurnRelevancy(model="openai:/gpt-4o", threshold=0.8)],
)
```

## Configuration parameters[​](#configuration-parameters "Direct link to Configuration parameters")

| Parameter | Type | Description |
|-----------|------|-------------|
| `model` | str | The LLM to use for evaluation. Required for LLM‑based metrics. |
| `threshold` | float | The pass/fail threshold for the metric score (e.g., 0.8). |
| `window_size` | int | Number of previous conversation turns to consider when evaluating relevance of the current turn. Larger windows provide more context. |
| `strict_mode` | bool | When `True`, enforces stricter criteria for relevance (e.g., penalising partially off‑topic responses). |

All DeepEval metrics accept metric‑specific keyword arguments; for further options and advanced usage, see the [DeepEval documentation](https://docs.confident-ai.com/). ^[deepeval-scorers-databricks-on-aws.md]

## How it works[​](#how-it-works "Direct link to How it works")

The TurnRelevancy scorer uses an LLM (specified via the `model` parameter) to evaluate whether the latest assistant response is relevant to the user's most recent turn, given the conversation history. It returns a binary pass/fail value (`"yes"` or `"no"`) and a numeric score under `feedback.metadata["score"]`. The `window_size` controls how much of the preceding conversation is provided as context; the `strict_mode` flag adjusts the evaluation severity. ^[deepeval-scorers-databricks-on-aws.md]

## Related concepts[​](#related-concepts "Direct link to Related concepts")

- DeepEval – The evaluation framework that provides this metric.
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – The MLflow subsystem for evaluating generative AI applications.
- [MLflow Scorers](/concepts/mlflow-scorers.md) – The general concept of scoring functions in MLflow evaluation.
- Conversational metrics – The category of metrics focused on multi‑turn dialogue quality.
- [AnswerRelevancy Scorer](/concepts/answerrelevancy-scorer.md) – Another DeepEval metric that evaluates single‑turn relevance.

## Sources[​](#sources "Direct link to Sources")

- deepeval-scorers-databricks-on-aws.md

# Citations

1. [deepeval-scorers-databricks-on-aws.md](/references/deepeval-scorers-databricks-on-aws-95eb5ac0.md)
