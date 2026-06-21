---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 25555be20893c5de09615adf863dce77bf7cf4a357260037f9eacdb213acabf0
  pageDirectory: concepts
  sources:
    - deepeval-scorers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deepeval-integration-with-mlflow
    - DIWM
  citations:
    - file: deepeval-scorers-databricks-on-aws.md
title: DeepEval Integration with MLflow
description: MLflow integrates with DeepEval so that DeepEval metrics can be used as scorers for LLM evaluation
tags:
  - mlflow
  - deepeval
  - evaluation
  - integration
timestamp: "2026-06-18T15:14:00.558Z"
---

# DeepEval Integration with MLflow

**DeepEval Integration with MLflow** enables you to use [DeepEval](https://docs.confident-ai.com/) evaluation metrics as scorers within MLflow's evaluation framework. DeepEval provides comprehensive metrics for RAG systems, agents, conversational AI, and safety evaluation, which are made available as first-class scorers in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) through the `mlflow.genai.scorers.deepeval` module. ^[deepeval-scorers-databricks-on-aws.md]

## Overview

DeepEval is a comprehensive evaluation framework for LLM applications. MLflow integrates with DeepEval so that you can use DeepEval metrics as scorers in your evaluation workflows. This integration allows you to leverage DeepEval's metric suite alongside MLflow's experiment tracking, model governance, and production monitoring capabilities. ^[deepeval-scorers-databricks-on-aws.md]

## Requirements

To use DeepEval scorers, install the `deepeval` Python package. The scorers are available through the `mlflow.genai.scorers.deepeval` module. ^[deepeval-scorers-databricks-on-aws.md]

## Quick Start

### Direct Scorer Usage

You can call a DeepEval scorer directly by instantiating it and passing inputs and outputs: ^[deepeval-scorers-databricks-on-aws.md]

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

The scorer returns a `feedback` object with a `.value` attribute (a binary "yes"/"no" pass/fail label) and a `.metadata` dictionary containing the numerical score and other details. ^[deepeval-scorers-databricks-on-aws.md]

### Using with `mlflow.genai.evaluate()`

DeepEval scorers integrate seamlessly with [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md): ^[deepeval-scorers-databricks-on-aws.md]

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

## Available DeepEval Scorers

### RAG Metrics

These scorers evaluate retrieval quality and answer generation in retrieval-augmented generation (RAG) applications. ^[deepeval-scorers-databricks-on-aws.md]

### Agentic Metrics

These scorers evaluate AI agent behavior, including task completion and tool usage. ^[deepeval-scorers-databricks-on-aws.md]

### Conversational Metrics

These scorers evaluate multi-turn conversational AI quality. ^[deepeval-scorers-databricks-on-aws.md]

### Safety Metrics

These scorers evaluate the safety and responsibility of model outputs. ^[deepeval-scorers-databricks-on-aws.md]

### Non-LLM Metrics

MLflow also provides access to DeepEval's non-LLM-based metrics. ^[deepeval-scorers-databricks-on-aws.md]

## Creating a Scorer by Name

You can dynamically create a scorer using `get_scorer` by passing the metric name as a string. This is useful when you want to select metrics at runtime or configure evaluation from external sources: ^[deepeval-scorers-databricks-on-aws.md]

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

## Configuration

DeepEval scorers accept metric-specific parameters as keyword arguments to the constructor. LLM-based metrics require a `model` parameter. You can pass common parameters like `threshold`, `include_reason`, and metric-specific parameters: ^[deepeval-scorers-databricks-on-aws.md]

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

For metric-specific parameters and advanced usage options, refer to the [DeepEval documentation](https://docs.confident-ai.com/). ^[deepeval-scorers-databricks-on-aws.md]

## Use Cases

- **RAG pipeline evaluation** — Assess retrieval quality and answer generation using metrics like `ContextRelevancy` and `Faithfulness`. ^[deepeval-scorers-databricks-on-aws.md]
- **Agent evaluation** — Measure task completion and tool usage accuracy. ^[deepeval-scorers-databricks-on-aws.md]
- **Conversational AI evaluation** — Score multi-turn dialogue quality. ^[deepeval-scorers-databricks-on-aws.md]
- **Safety testing** — Check model outputs for harmful content or bias using safety metrics. ^[deepeval-scorers-databricks-on-aws.md]

## Related Concepts

- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The MLflow subsystem for large language model evaluation and monitoring
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — Core evaluation API for LLM applications
- [Custom Judges](/concepts/custom-judges.md) — Creating bespoke LLM-based evaluators with `make_judge()`
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying scorers for continuous quality monitoring
- Third-Party Scorer Integration — Using evaluators from external frameworks

## Sources

- deepeval-scorers-databricks-on-aws.md

# Citations

1. [deepeval-scorers-databricks-on-aws.md](/references/deepeval-scorers-databricks-on-aws-95eb5ac0.md)
