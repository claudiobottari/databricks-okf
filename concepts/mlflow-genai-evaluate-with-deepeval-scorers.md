---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 671693c5b16b93360fb3088ad87ff82d7fb49ca3a4f55f8de47275a5eda02bf3
  pageDirectory: concepts
  sources:
    - deepeval-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-evaluate-with-deepeval-scorers
    - MGEWDS
  citations:
    - file: deepeval-scorers-databricks-on-aws.md
title: MLflow genai evaluate() with DeepEval Scorers
description: DeepEval scorers can be used as part of the mlflow.genai.evaluate() pipeline to evaluate datasets of inputs and outputs.
tags:
  - mlflow
  - deepeval
  - evaluation
  - genai
timestamp: "2026-06-19T18:19:38.608Z"
---

# MLflow genai evaluate() with DeepEval Scorers

**MLflow genai evaluate() with DeepEval Scorers** describes the integration between MLflow’s `mlflow.genai.evaluate()` function and DeepEval, a comprehensive evaluation framework for LLM applications. Through this integration, you can use any DeepEval metric — covering RAG, agentic, conversational, safety, and other categories — as a scorer inside an MLflow evaluation run. ^[deepeval-scorers-databricks-on-aws.md]

## Overview

DeepEval provides metrics for evaluating [retrieval-augmented generation](/concepts/retrieval-augmented-generation-rag.md) (RAG) systems, AI agents, conversational AI, and LLM safety. MLflow exposes these metrics as scorer objects that can be passed directly to `mlflow.genai.evaluate()` or called standalone. ^[deepeval-scorers-databricks-on-aws.md]

## Requirements

To use DeepEval scorers with MLflow, install the `deepeval` package:

```bash
pip install deepeval
```

^[deepeval-scorers-databricks-on-aws.md]

## Quick start

### Calling a DeepEval scorer directly

Individual scorers can be instantiated and called like functions. The following example creates an `AnswerRelevancy` scorer and evaluates a single input/output pair:

```python
from mlflow.genai.scorers.deepeval import AnswerRelevancy

scorer = AnswerRelevancy(threshold=0.7, model="databricks:/databricks-gpt-5-mini")
feedback = scorer(
    inputs="What is MLflow?",
    outputs="MLflow is an open-source AI engineering platform for agents and LLMs.",
)
print(feedback.value)   # "yes" or "no"
print(feedback.metadata["score"])  # 0.85
```

^[deepeval-scorers-databricks-on-aws.md]

### Using scorers with `mlflow.genai.evaluate()`

DeepEval scorers can be passed in a list to the `scorers` parameter of `mlflow.genai.evaluate()`. Each scorer is an instance of a DeepEval metric class. The `data` argument supplies an evaluation dataset as a list of dictionaries with `inputs` and `outputs` keys:

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

## Available DeepEval scorers

DeepEval metrics are grouped into several categories. Each category has its own set of scorer classes that can be imported from `mlflow.genai.scorers.deepeval`.

### RAG metrics

These scorers evaluate [retrieval-augmented generation](/concepts/retrieval-augmented-generation-rag.md) quality, including retrieval relevance and answer faithfulness. ^[deepeval-scorers-databricks-on-aws.md]

### Agentic metrics

These scorers assess AI agent behavior, such as task completion and tool usage correctness. ^[deepeval-scorers-databricks-on-aws.md]

### Conversational metrics

These scorers measure multi-turn [conversational AI](/concepts/conversation-evaluation.md) quality, including relevance across turns. ^[deepeval-scorers-databricks-on-aws.md]

### Safety metrics

These scorers evaluate the LLM safety evaluation|safety and responsibility of model outputs. ^[deepeval-scorers-databricks-on-aws.md]

### Other metrics

Additional DeepEval metrics that do not fit into the above categories are available under “Other metrics”. ^[deepeval-scorers-databricks-on-aws.md]

### Non-LLM metrics

DeepEval also provides metrics that do not rely on an underlying LLM. ^[deepeval-scorers-databricks-on-aws.md]

## Create a scorer by name

Instead of importing a specific scorer class, you can dynamically create any DeepEval scorer using the `get_scorer` function with the metric name as a string:

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

DeepEval scorers accept metric-specific parameters as keyword arguments to the constructor. LLM-based metrics require a `model` parameter that specifies which model to use for evaluation. Common parameters include `threshold`, `include_reason`, and metric‑specific options:

```python
from mlflow.genai.scorers.deepeval import AnswerRelevancy, TurnRelevancy

# LLM-based metric with common parameters
scorer = AnswerRelevancy(
    model="databricks:/databricks-gpt-5-mini",
    threshold=0.7,
    include_reason=True,
)

# Metric-specific parameters for a conversational scorer
conversational_scorer = TurnRelevancy(
    model="openai:/gpt-4o",
    threshold=0.8,
    window_size=3,
    strict_mode=True,
)
```

For a complete list of metric-specific parameters and advanced usage options, see the DeepEval documentation. ^[deepeval-scorers-databricks-on-aws.md]

## Related Concepts

- [MLflow genai evaluate()](/concepts/mlflowgenaievaluate.md)
- DeepEval
- [LLM evaluation](/concepts/llm-as-a-judge-evaluation.md)
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md)
- AI agents
- Conversational AI
- LLM safety evaluation

## Sources

- deepeval-scorers-databricks-on-aws.md

# Citations

1. [deepeval-scorers-databricks-on-aws.md](/references/deepeval-scorers-databricks-on-aws-95eb5ac0.md)
