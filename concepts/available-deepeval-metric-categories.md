---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 03cc93d1c3de359080a44a1d1e4c04019687ecb96c31494ca612c0b4d94f886c
  pageDirectory: concepts
  sources:
    - deepeval-scorers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - available-deepeval-metric-categories
    - ADMC
  citations:
    - file: deepeval-scorers-databricks-on-aws.md
title: Available DeepEval Metric Categories
description: "DeepEval provides five categories of metrics: RAG, Agentic, Conversational, Safety, and Non-LLM metrics"
tags:
  - metrics
  - categories
  - evaluation
  - llm
timestamp: "2026-06-18T15:14:02.679Z"
---

# Available DeepEval Metric Categories

**Available DeepEval Metric Categories** refers to the groups of evaluation metrics provided by the DeepEval framework that are integrated with MLflow for scoring LLM applications. These categories cover different aspects of LLM performance, including retrieval quality, agent behavior, conversational quality, safety, and more.

## Overview

DeepEval is a comprehensive evaluation framework for LLM applications that provides metrics for RAG systems, agents, conversational AI, and safety evaluation. MLflow integrates with DeepEval so that users can use DeepEval metrics as scorers in their evaluation workflows. ^[deepeval-scorers-databricks-on-aws.md]

## Metric Categories

### RAG Metrics

These scorers evaluate retrieval quality and answer generation in [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) applications. They assess how well the system retrieves relevant context and generates accurate responses based on that context. ^[deepeval-scorers-databricks-on-aws.md]

### Agentic Metrics

These scorers evaluate AI agent behavior, including task completion and tool usage. They measure how effectively an agent performs its designated tasks and whether it uses available tools appropriately. ^[deepeval-scorers-databricks-on-aws.md]

### Conversational Metrics

These scorers evaluate multi-turn [conversational AI](/concepts/conversation-evaluation.md) quality. They assess the coherence, relevance, and quality of responses across multiple turns of dialogue. ^[deepeval-scorers-databricks-on-aws.md]

### Safety Metrics

These scorers evaluate the safety and responsibility of model outputs. They check for harmful, biased, or inappropriate content in generated responses. ^[deepeval-scorers-databricks-on-aws.md]

### Other Metrics

This category includes additional evaluation metrics that do not fall into the primary categories above. ^[deepeval-scorers-databricks-on-aws.md]

### Non-LLM Metrics

These are metrics that do not require an LLM for evaluation. They can be computed using traditional statistical or rule-based approaches. ^[deepeval-scorers-databricks-on-aws.md]

## Using DeepEval Scorers

DeepEval scorers can be used directly or through the `mlflow.genai.evaluate()` API. Each scorer accepts metric-specific parameters as keyword arguments to the constructor. LLM-based metrics require a `model` parameter specifying which model to use for evaluation. ^[deepeval-scorers-databricks-on-aws.md]

### Creating a Scorer by Name

You can dynamically create a scorer using `get_scorer` by passing the metric name as a string: ^[deepeval-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers.deepeval import get_scorer

scorer = get_scorer(
    metric_name="AnswerRelevancy",
    threshold=0.7,
    model="databricks:/databricks-gpt-5-mini",
)
```

## Related Concepts

- [DeepEval Framework](/concepts/deepeval-framework.md) — The underlying evaluation framework
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The MLflow evaluation system that integrates DeepEval
- RAG Evaluation — Evaluating retrieval-augmented generation systems
- LLM Safety Evaluation — Assessing model output safety and responsibility
- [Custom Judges](/concepts/custom-judges.md) — Alternative approach to creating evaluation metrics

## Sources

- deepeval-scorers-databricks-on-aws.md

# Citations

1. [deepeval-scorers-databricks-on-aws.md](/references/deepeval-scorers-databricks-on-aws-95eb5ac0.md)
