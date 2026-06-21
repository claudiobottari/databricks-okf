---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 50f2c4aadf2de1061bf2894494d51cf56df5808050e68c49b86dbe93e5065a46
  pageDirectory: concepts
  sources:
    - deepeval-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-deepeval-scorer-integration
    - MSI
  citations:
    - file: deepeval-scorers-databricks-on-aws.md
title: MLflow-DeepEval Scorer Integration
description: MLflow integrates with DeepEval to allow using DeepEval metrics as MLflow scorers for LLM evaluation workflows.
tags:
  - mlflow
  - deepeval
  - llm-evaluation
  - integration
timestamp: "2026-06-19T18:19:17.691Z"
---

# MLflow-DeepEval Scorer Integration

**MLflow-DeepEval Scorer Integration** allows users to incorporate [DeepEval](https://docs.confident-ai.com/) evaluation metrics as scorers within MLflow's evaluation framework. DeepEval is a comprehensive evaluation framework for LLM applications that provides metrics for [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) systems, agents, conversational AI, and safety evaluation. Through this integration, MLflow users can leverage DeepEval metrics directly in their evaluation workflows without switching between tools. ^[deepeval-scorers-databricks-on-aws.md]

## Requirements

To use DeepEval scorers in MLflow, install the `deepeval` package. No additional configuration is required beyond installing the package and having access to a supported language model. ^[deepeval-scorers-databricks-on-aws.md]

## Quick Start

### Direct Scoring

You can call a DeepEval scorer directly to evaluate a single input-output pair:

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

### Using with `mlflow.genai.evaluate()`

DeepEval scorers can be integrated into batch evaluation using `mlflow.genai.evaluate()`:

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

## Available Scorer Categories

### RAG Metrics

These scorers evaluate retrieval quality and answer generation in retrieval-augmented generation applications. Use them when assessing the quality of RAG systems. ^[deepeval-scorers-databricks-on-aws.md]

### Agentic Metrics

These scorers evaluate AI agent behavior, including task completion and tool usage. Suitable for evaluating AI agents and their operational effectiveness. ^[deepeval-scorers-databricks-on-aws.md]

### Conversational Metrics

These scorers evaluate multi-turn conversational AI quality. Use them for Conversational AI systems that maintain context across multiple interactions. ^[deepeval-scorers-databricks-on-aws.md]

### Safety Metrics

These scorers evaluate the safety and responsibility of model outputs. They help ensure that LLM safety standards are met. ^[deepeval-scorers-databricks-on-aws.md]

### Other Metrics

Additional DeepEval metrics that do not fall into the above categories are also available. ^[deepeval-scorers-databricks-on-aws.md]

### Non-LLM Metrics

DeepEval provides metrics that do not require an underlying language model for computation. ^[deepeval-scorers-databricks-on-aws.md]

## Dynamic Scorer Creation

You can dynamically create a scorer by name using `get_scorer`, which accepts the metric name as a string parameter:

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

DeepEval scorers accept metric-specific parameters as keyword arguments to the constructor. LLM-based metrics require a `model` parameter specifying which language model to use for evaluation:

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

- MLflow Evaluation Framework — The broader evaluation system that integrates third-party scorers
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) — Application type evaluated by RAG-specific DeepEval metrics
- [LLM Evaluation Metrics](/concepts/llm-as-a-judge-evaluation-metrics.md) — General concepts around evaluating large language model outputs
- AI Agents — Application types evaluated by agentic DeepEval metrics
- Conversational AI — Application types evaluated by conversational DeepEval metrics
- LLM Safety — Safety considerations evaluated by DeepEval safety metrics

## Sources

- deepeval-scorers-databricks-on-aws.md

# Citations

1. [deepeval-scorers-databricks-on-aws.md](/references/deepeval-scorers-databricks-on-aws-95eb5ac0.md)
