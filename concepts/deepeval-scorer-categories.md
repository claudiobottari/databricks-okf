---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: adf1cc749625f9902775ec1ec0e4bb12a6d85b22d6854a2f4d1c120fac613a15
  pageDirectory: concepts
  sources:
    - deepeval-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deepeval-scorer-categories
    - DSC
    - DeepEval scorers#Available DeepEval scorers
  citations:
    - file: deepeval-scorers-databricks-on-aws.md
title: DeepEval Scorer Categories
description: "DeepEval provides five categories of scorers: RAG metrics, agentic metrics, conversational metrics, safety metrics, and non-LLM metrics."
tags:
  - deepeval
  - llm-evaluation
  - metrics
  - taxonomy
timestamp: "2026-06-19T18:19:25.941Z"
---

```markdown
---
title: DeepEval Scorer Categories
summary: "DeepEval provides five categories of scorers: RAG metrics, Agentic metrics, Conversational metrics, Safety metrics, and Non-LLM metrics, plus an Other metrics group."
sources:
  - deepeval-scorers-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T22:00:00.000Z"
updatedAt: "2026-06-19T22:00:00.000Z"
tags:
  - llm-evaluation
  - taxonomy
  - deep-eval
aliases:
  - deepeval-scorer-categories
  - DSC
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# DeepEval Scorer Categories

**DeepEval Scorer Categories** groups the evaluation metrics provided by [DeepEval](https://docs.confident-ai.com/), a comprehensive framework for LLM application evaluation, when used through the MLflow integration. The categories organize metrics by the type of task they assess: retrieval-augmented generation (RAG), agent behavior, conversational AI, safety, and non-LLM criteria. ^[deepeval-scorers-databricks-on-aws.md]

## Overview

DeepEval metrics are integrated into MLflow as third-party scorers, enabling developers to use them directly with `mlflow.genai.evaluate()` or as standalone scorers. Each metric belongs to a category based on the aspect of LLM performance it measures. ^[deepeval-scorers-databricks-on-aws.md]

## Available Categories

The integration categorizes metrics as follows: ^[deepeval-scorers-databricks-on-aws.md]

| Category | Description |
|----------|-------------|
| **RAG metrics** | Evaluate retrieval quality and answer generation in [[retrieval-augmented generation (RAG)]] applications. |
| **Agentic metrics** | Evaluate AI agent behavior, including task completion and tool usage. |
| **Conversational metrics** | Evaluate multi-turn conversational AI quality. |
| **Safety metrics** | Evaluate the safety and responsibility of model outputs. |
| **Other metrics** | Additional metrics not falling into the above categories. |
| **Non-LLM metrics** | Metrics that do not rely on an LLM judge for scoring. |

For the complete list of individual metrics within each category, see the [DeepEval documentation](https://docs.confident-ai.com/). ^[deepeval-scorers-databricks-on-aws.md]

## Creating a Scorer by Name

You can dynamically create any DeepEval scorer using `get_scorer()`, passing the metric name as a string. This allows referencing a scorer from any category at runtime. ^[deepeval-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers.deepeval import get_scorer

scorer = get_scorer(
    metric_name="AnswerRelevancy",   # RAG metric
    threshold=0.7,
    model="databricks:/databricks-gpt-5-mini",
)
```

## Configuration

DeepEval scorers accept metric-specific parameters as keyword arguments to the constructor. LLM-based metrics require a `model` parameter. The integration supports both Databricks-hosted models (using the `databricks:/` URI scheme) and external providers like OpenAI. ^[deepeval-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers.deepeval import AnswerRelevancy, TurnRelevancy

# LLM-based metric (RAG category)
scorer = AnswerRelevancy(
    model="databricks:/databricks-gpt-5-mini",
    threshold=0.7,
    include_reason=True,
)

# Conversational metric (conversational category)
conversational_scorer = TurnRelevancy(
    model="openai:/gpt-4o",
    threshold=0.8,
    window_size=3,
    strict_mode=True,
)
```

## Related Concepts

- [[MLflow GenAI evaluation]] – The framework that hosts DeepEval scorers.
- [[Third-Party Scorers in MLflow GenAI|Third-party scorers]] – Other integration options for custom and external evaluators.
- [[Evaluation Run|RAG evaluation]] – Evaluating retrieval and generation pipelines.
- [[MLflow Agent Evaluation|Agent evaluation]] – Assessing tool usage and task completion in AI agents.
- LLM safety evaluation – Using safety metrics for responsible AI.
- DeepEval – The upstream framework providing these metrics.

## Sources

- deepeval-scorers-databricks-on-aws.md
```

# Citations

1. [deepeval-scorers-databricks-on-aws.md](/references/deepeval-scorers-databricks-on-aws-95eb5ac0.md)
