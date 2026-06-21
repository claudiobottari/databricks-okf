---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dd13a60aebc9e203b3f943349f68127628fb9970f7e47369a49b9a78b29afb75
  pageDirectory: concepts
  sources:
    - ragas-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ragas-retrieval-augmented-generation-assessment
    - R(AGA
    - RAGAS
  citations:
    - file: ragas-scorers-databricks-on-aws.md
title: RAGAS (Retrieval Augmented Generation Assessment)
description: An evaluation framework for LLM applications that assesses retrieval quality, answer generation, agent behavior, and text similarity.
tags:
  - evaluation
  - LLM
  - RAG
timestamp: "2026-06-19T20:06:33.374Z"
---

# RAGAS (Retrieval Augmented Generation Assessment)

**RAGAS** (Retrieval Augmented Generation Assessment) is an evaluation framework for LLM applications. It provides metrics for assessing retrieval quality, answer generation, agent behavior, and text similarity. [MLflow](/concepts/mlflow.md) integrates with RAGAS so that users can employ RAGAS metrics as scorers for evaluating LLM-based systems. ^[ragas-scorers-databricks-on-aws.md]

## Requirements

To use RAGAS scorers in MLflow, the `ragas` Python package must be installed. ^[ragas-scorers-databricks-on-aws.md]

## Quick Start

A RAGAS scorer can be called directly by instantiating a metric class and passing a trace object. The scorer returns a `feedback` object with a numeric `value` (between 0.0 and 1.0) and a `rationale` explaining the score. ^[ragas-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers.ragas import Faithfulness

scorer = Faithfulness(model="databricks:/databricks-gpt-5-mini")
feedback = scorer(trace=trace)
print(feedback.value)   # Score between 0.0 and 1.0
print(feedback.rationale)  # Explanation of the score
```

^[ragas-scorers-databricks-on-aws.md]

Multiple scorers can be applied together using `mlflow.genai.evaluate()` with a dataset of traces: ^[ragas-scorers-databricks-on-aws.md]

```python
import mlflow
from mlflow.genai.scorers.ragas import Faithfulness, ContextPrecision

traces = mlflow.search_traces()
results = mlflow.genai.evaluate(
    data=traces,
    scorers=[
        Faithfulness(model="databricks:/databricks-gpt-5-mini"),
        ContextPrecision(model="databricks:/databricks-gpt-5-mini"),
    ],
)
```

## Available RAGAS Scorers

RAGAS scorers are grouped by evaluation category.

### RAG Metrics

These scorers evaluate retrieval quality and answer generation in [RAG|retrieval-augmented generation](/concepts/retrieval-augmented-generation-rag.md) applications — for example, faithfulness of the answer to retrieved context and precision of the retrieved context. ^[ragas-scorers-databricks-on-aws.md]

### Agent and Tool Use Metrics

These scorers evaluate AI agent behavior, including tool invocation accuracy and goal achievement. ^[ragas-scorers-databricks-on-aws.md]

### Natural Language Comparison

These scorers compare generated text against expected output using both semantic and deterministic methods. ^[ragas-scorers-databricks-on-aws.md]

### General Purpose

These scorers provide flexible, customizable evaluation logic. ^[ragas-scorers-databricks-on-aws.md]

### Other Tasks

Additional scorers are available for other evaluation tasks. ^[ragas-scorers-databricks-on-aws.md]

## Create a Scorer by Name

A scorer can be dynamically created by passing the metric name as a string to `get_scorer`: ^[ragas-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers.ragas import get_scorer

scorer = get_scorer(
    metric_name="Faithfulness",
    model="databricks:/databricks-gpt-5-mini",
)
feedback = scorer(trace=trace)
```

## Configuration

RAGAS scorers accept metric-specific parameters as keyword arguments to the constructor. LLM-based metrics require a `model` parameter; non-LLM metrics do not. ^[ragas-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers.ragas import Faithfulness, ExactMatch

# LLM-based metric with model specification
scorer = Faithfulness(model="databricks:/databricks-gpt-5-mini")

# Non-LLM metric (no model required)
deterministic_scorer = ExactMatch()
```

For metric-specific parameters and advanced usage options, refer to the [RAGAS documentation](https://docs.ragas.io/). ^[ragas-scorers-databricks-on-aws.md]

## Related Concepts

- [MLflow](/concepts/mlflow.md) — Platform that integrates RAGAS scorers for evaluation and monitoring.
- [RAG (Retrieval Augmented Generation)](/concepts/retrieval-augmented-generation-rag.md) — The paradigm evaluated by RAG metrics.
- [LLM Evaluation](/concepts/llm-as-a-judge-evaluation.md) — Broader category of evaluating large language model outputs.
- [Trace](/concepts/traces.md) — MLflow data structure representing a sequence of operations in an LLM application.
- [GenAI Evaluate](/concepts/mlflow-genai-evaluation.md) — MLflow API for evaluating generative AI models and traces.

## Sources

- ragas-scorers-databricks-on-aws.md

# Citations

1. [ragas-scorers-databricks-on-aws.md](/references/ragas-scorers-databricks-on-aws-5240ee43.md)
