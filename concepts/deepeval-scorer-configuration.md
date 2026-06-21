---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3aec0773c9b2cf69ac117f879f344a6d6cd9191d73e216b03b286b3d9e033f02
  pageDirectory: concepts
  sources:
    - deepeval-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deepeval-scorer-configuration
    - DSC
  citations:
    - file: deepeval-scorers-databricks-on-aws.md
title: DeepEval Scorer Configuration
description: DeepEval scorers accept metric-specific keyword parameters including model, threshold, include_reason, window_size, and strict_mode for customizing evaluation behavior.
tags:
  - configuration
  - parameters
  - deep-eval
timestamp: "2026-06-19T14:58:44.498Z"
---

# DeepEval Scorer Configuration

**DeepEval Scorer Configuration** describes how to instantiate and parameterize DeepEval metrics for use as scorers in [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md). DeepEval is an evaluation framework for LLM applications that provides metrics for RAG systems, agents, conversational AI, and safety evaluation. MLflow integrates with DeepEval so that these metrics can be used directly in `mlflow.genai.evaluate()` or as standalone evaluators. ^[deepeval-scorers-databricks-on-aws.md]

## Requirements

Install the `deepeval` package:

```bash
pip install deepeval
```

^[deepeval-scorers-databricks-on-aws.md]

## Instantiation

DeepEval scorers are instantiated by importing from `mlflow.genai.scorers.deepeval` and constructing a scorer object. Each scorer accepts metric-specific parameters as keyword arguments to the constructor. LLM-based metrics require a `model` parameter that specifies the model endpoint to use for evaluation. ^[deepeval-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers.deepeval import AnswerRelevancy

scorer = AnswerRelevancy(
    threshold=0.7,
    model="databricks:/databricks-gpt-5-mini"
)
```

The scorer can then be called directly on inputs and outputs, returning a feedback object with a binary pass/fail value (`feedback.value`) and a numeric score (`feedback.metadata["score"]`). ^[deepeval-scorers-databricks-on-aws.md]

## Configuration Parameters

DeepEval scorers accept metric-specific parameters as keyword arguments. The following parameters are commonly supported: ^[deepeval-scorers-databricks-on-aws.md]

| Parameter | Description | Required | Example |
|-----------|-------------|----------|---------|
| `model` | The LLM endpoint for judgment (e.g., `"databricks:/model-name"` or `"openai:/gpt-4o"`) | Yes for LLM-based metrics | `model="databricks:/databricks-gpt-5-mini"` |
| `threshold` | The passing threshold for the metric | No | `threshold=0.7` |
| `include_reason` | Whether to include a reasoning in the output | No | `include_reason=True` |

Metric-specific parameters such as `window_size` or `strict_mode` can also be passed depending on the metric: ^[deepeval-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers.deepeval import TurnRelevancy

conversational_scorer = TurnRelevancy(
    model="openai:/gpt-4o",
    threshold=0.8,
    window_size=3,
    strict_mode=True,
)
```

For a full list of metric-specific parameters and advanced usage options, refer to the [DeepEval documentation](https://docs.confident-ai.com/). ^[deepeval-scorers-databricks-on-aws.md]

## Creating a Scorer by Name

You can dynamically create a scorer at runtime using the `get_scorer` function, passing the metric name as a string: ^[deepeval-scorers-databricks-on-aws.md]

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

## Using Scorers with `mlflow.genai.evaluate()`

DeepEval scorers can be passed as a list to the `scorers` parameter of `mlflow.genai.evaluate()`: ^[deepeval-scorers-databricks-on-aws.md]

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

## Available Metric Categories

DeepEval scorers are grouped into several categories: ^[deepeval-scorers-databricks-on-aws.md]

- **RAG metrics** – Evaluate retrieval quality and answer generation in RAG applications.
- **Agentic metrics** – Evaluate AI agent behavior, including task completion and tool usage.
- **Conversational metrics** – Evaluate multi-turn conversational AI quality.
- **Safety metrics** – Evaluate the safety and responsibility of model outputs.
- **Other metrics** – Additional evaluation dimensions.

Non-LLM metrics are also available and do not require a `model` parameter. ^[deepeval-scorers-databricks-on-aws.md]

## Related Concepts

- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The framework for running offline evaluations
- DeepEval – The underlying open-source evaluation library
- [Custom Judges](/concepts/custom-judges.md) – Creating your own LLM-based evaluators
- MLflow Scoring API – The `mlflow.genai.scorers` module

## Sources

- deepeval-scorers-databricks-on-aws.md

# Citations

1. [deepeval-scorers-databricks-on-aws.md](/references/deepeval-scorers-databricks-on-aws-95eb5ac0.md)
