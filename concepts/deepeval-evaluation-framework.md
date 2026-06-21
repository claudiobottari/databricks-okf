---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9348914fc3c6b4529e5b7a038ffb7b4bddfc8096a0d4f0b5a4768b6a348ec7e9
  pageDirectory: concepts
  sources:
    - deepeval-scorers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deepeval-evaluation-framework
    - DEF
  citations:
    - file: deepeval-scorers-databricks-on-aws.md
title: DeepEval Evaluation Framework
description: A comprehensive evaluation framework for LLM applications that provides metrics for RAG systems, agents, conversational AI, and safety evaluation.
tags:
  - llm-evaluation
  - framework
  - deep-eval
timestamp: "2026-06-18T11:47:15.007Z"
---

# DeepEval Evaluation Framework

**DeepEval** is a comprehensive evaluation framework for LLM applications that provides metrics for RAG systems, agents, conversational AI, and safety evaluation. It integrates with [MLflow GenAI](/concepts/mlflow-3-for-genai.md) so that DeepEval metrics can be used as scorers within the MLflow evaluation ecosystem. ^[deepeval-scorers-databricks-on-aws.md]

## Overview

DeepEval offers a structured approach to evaluating LLM-based applications across multiple dimensions of quality. The framework includes specialized metrics for different use cases — retrieval-augmented generation (RAG), agentic behavior, multi-turn conversation, safety, and general quality assessment. When integrated with MLflow, these metrics can be used both as standalone scorers and within `mlflow.genai.evaluate()` for systematic offline evaluation. ^[deepeval-scorers-databricks-on-aws.md]

## Requirements

To use DeepEval scorers with MLflow, install the `deepeval` package. ^[deepeval-scorers-databricks-on-aws.md]

## Available DeepEval Scorers

### RAG Metrics

These scorers evaluate retrieval quality and answer generation in retrieval-augmented generation applications. ^[deepeval-scorers-databricks-on-aws.md]

### Agentic Metrics

These scorers evaluate AI agent behavior, including task completion and tool usage. ^[deepeval-scorers-databricks-on-aws.md]

### Conversational Metrics

These scorers evaluate multi-turn conversational AI quality. ^[deepeval-scorers-databricks-on-aws.md]

### Safety Metrics

These scorers evaluate the safety and responsibility of model outputs. ^[deepeval-scorers-databricks-on-aws.md]

### Other Metrics

DeepEval also provides additional general-purpose metrics and non-LLM metrics that do not require a language model for evaluation. ^[deepeval-scorers-databricks-on-aws.md]

## Integration with MLflow

### Direct Scorer Calls

DeepEval scorers can be instantiated and called directly. Each scorer accepts standard evaluation parameters such as `inputs` and `outputs`, and returns feedback with a value and metadata including a numerical score: ^[deepeval-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers.deepeval import AnswerRelevancy

scorer = AnswerRelevancy(threshold=0.7, model="databricks:/databricks-gpt-5-mini")
feedback = scorer(
    inputs="What is MLflow?",
    outputs="MLflow is an open-source AI engineering platform for agents and LLMs.",
)
print(feedback.value)       # "yes" or "no"
print(feedback.metadata["score"])  # 0.85
```

^[deepeval-scorers-databricks-on-aws.md]

### Using with `mlflow.genai.evaluate()`

DeepEval scorers can be passed as part of the `scorers` parameter in [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md), enabling systematic evaluation across an entire dataset: ^[deepeval-scorers-databricks-on-aws.md]

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

### Dynamic Scorer Creation

Scorers can be created dynamically by name using the `get_scorer` function, passing the metric name as a string: ^[deepeval-scorers-databricks-on-aws.md]

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

DeepEval scorers accept metric-specific parameters as keyword arguments to the constructor. LLM-based metrics require a `model` parameter specifying the judge model to use. Common parameters like `threshold` and `include_reason` are available across metrics, while metric-specific parameters vary: ^[deepeval-scorers-databricks-on-aws.md]

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

For metric-specific parameters and advanced usage options, refer to the [DeepEval documentation](https://docs.confident-ai.com/). ^[deepeval-scorers-databricks-on-aws.md]

## Related Concepts

- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The MLflow ecosystem for generative AI evaluation and monitoring
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` API for systematic offline assessment
- [Custom Judges](/concepts/custom-judges.md) — LLM-based scorers for custom evaluation criteria
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Using judges to compare agent variants
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying scorers for continuous quality monitoring

## Sources

- deepeval-scorers-databricks-on-aws.md

# Citations

1. [deepeval-scorers-databricks-on-aws.md](/references/deepeval-scorers-databricks-on-aws-95eb5ac0.md)
