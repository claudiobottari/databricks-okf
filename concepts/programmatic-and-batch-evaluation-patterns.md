---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7d5e14e92708d2dd7a1a3b29bd084ba26b0d42d03d508203e38a85d98352c497
  pageDirectory: concepts
  sources:
    - deepeval-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - programmatic-and-batch-evaluation-patterns
    - Batch Evaluation Patterns and Programmatic
    - PABEP
    - programmatic checks
  citations:
    - file: deepeval-scorers-databricks-on-aws.md
title: Programmatic and Batch Evaluation Patterns
description: DeepEval scorers can be used both programmatically as standalone scoring functions and in batch mode via mlflow.genai.evaluate() for dataset-level evaluation.
tags:
  - mlflow
  - evaluation
  - patterns
timestamp: "2026-06-19T14:58:44.476Z"
---

# Programmatic and Batch Evaluation Patterns

**Programmatic and Batch Evaluation Patterns** refer to the approaches for running LLM evaluations programmatically using Python APIs and processing multiple evaluation examples in batch. These patterns enable automated, reproducible evaluation workflows integrated into ML pipelines.

## Overview

Programmatic evaluation allows you to define and run evaluations directly from code rather than through a UI. This approach is essential for integrating evaluation into CI/CD pipelines, automated testing, and production monitoring workflows. Batch evaluation extends this concept by processing multiple evaluation examples together, enabling efficient scoring of entire datasets. ^[deepeval-scorers-databricks-on-aws.md]

## Direct Scorer Invocation

The simplest programmatic pattern is calling a scorer directly on individual inputs and outputs. This is useful for ad-hoc evaluation or testing specific examples:

```python
from mlflow.genai.scorers.deepeval import AnswerRelevancy

scorer = AnswerRelevancy(threshold=0.7, model="databricks:/databricks-gpt-5-mini")
feedback = scorer(
    inputs="What is MLflow?",
    outputs="MLflow is an open-source AI engineering platform for agents and LLMs.",
)
print(feedback.value)  # "yes" or "no"
print(feedback.metadata["score"])  # 0.85
```

^[deepeval-scorers-databricks-on-aws.md]

## Batch Evaluation with `mlflow.genai.evaluate()`

For evaluating multiple examples at once, use `mlflow.genai.evaluate()` with a list of evaluation records and one or more scorers. This pattern processes all examples in batch and returns aggregated results:

```python
import mlflow
from mlflow.genai.scorers.deepeval import AnswerRelevancy, Faithfulness

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
        AnswerRelevancy(threshold=0.7, model="databricks:/databricks-gpt-5-mini"),
        Faithfulness(threshold=0.8, model="databricks:/databricks-gpt-5-mini"),
    ],
)
```

^[deepeval-scorers-databricks-on-aws.md]

## Dynamic Scorer Creation

For more flexible programmatic patterns, you can create scorers dynamically by name using `get_scorer()`. This is useful when metric names are determined at runtime or come from configuration:

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

## Scorer Configuration

Scorers accept metric-specific parameters as keyword arguments to the constructor. LLM-based metrics require a `model` parameter specifying which LLM to use for evaluation:

```python
from mlflow.genai.scorers.deepeval import AnswerRelevancy, TurnRelevancy

# LLM-based metric with common parameters
scorer = AnswerRelevancy(
    model="databricks:/databricks-gpt-5-mini",
    threshold=0.7,
    include_reason=True,
)

# Metric-specific parameters
conversational_scorer = TurnRelevancy(
    model="openai:/gpt-4o",
    threshold=0.8,
    window_size=3,
    strict_mode=True,
)
```

^[deepeval-scorers-databricks-on-aws.md]

## Available Scorer Categories

DeepEval provides several categories of scorers that can be used programmatically:

- **RAG metrics** – Evaluate retrieval quality and answer generation in retrieval-augmented generation applications
- **Agentic metrics** – Evaluate AI agent behavior, including task completion and tool usage
- **Conversational metrics** – Evaluate multi-turn conversational AI quality
- **Safety metrics** – Evaluate the safety and responsibility of model outputs
- **Non-LLM metrics** – Metrics that do not require an LLM for evaluation

^[deepeval-scorers-databricks-on-aws.md]

## Related Concepts

- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The broader evaluation framework that supports programmatic patterns
- [LLM-as-a-Judge Evaluation](/concepts/llm-as-a-judge-evaluation.md) – The paradigm underlying many programmatic scorers
- Automated Evaluation Pipelines – CI/CD integration patterns for evaluation
- Scorer Configuration and Thresholds – Configuring scorer parameters and pass/fail thresholds
- [Evaluation Datasets](/concepts/evaluation-datasets.md) – Structuring data for batch evaluation

## Sources

- deepeval-scorers-databricks-on-aws.md

# Citations

1. [deepeval-scorers-databricks-on-aws.md](/references/deepeval-scorers-databricks-on-aws-95eb5ac0.md)
