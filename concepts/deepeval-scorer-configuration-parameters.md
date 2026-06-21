---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 862c1de558b5bac3ad5c0b607893d66c67fdd66af4c28067cdd7c6f779337817
  pageDirectory: concepts
  sources:
    - deepeval-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deepeval-scorer-configuration-parameters
    - DSCP
  citations:
    - file: deepeval-scorers-databricks-on-aws.md
title: DeepEval Scorer Configuration Parameters
description: DeepEval scorers accept metric-specific parameters like threshold, model, include_reason, window_size, and strict_mode to customize evaluation behavior.
tags:
  - deepeval
  - configuration
  - scorer
  - parameters
timestamp: "2026-06-19T18:19:33.003Z"
---

# DeepEval Scorer Configuration Parameters

**DeepEval Scorer Configuration Parameters** are the keyword arguments accepted by DeepEval metric constructors when used as scorers within MLflow's evaluation framework. These parameters control the behavior of LLM-based and non-LLM metrics for evaluating retrieval-augmented generation (RAG) systems, agents, conversational AI, and safety.

## Overview

DeepEval scorers are created by passing metric-specific parameters as keyword arguments to the scorer constructor. LLM-based metrics require a `model` parameter to specify which language model performs the evaluation. All parameters are passed at instantiation time and affect how the scorer computes its feedback. ^[deepeval-scorers-databricks-on-aws.md]

## Common Parameters

The following parameters are shared across many DeepEval scorers:

- **`model`** (required for LLM-based metrics): Specifies the language model used for evaluation. Accepts model URIs such as `"databricks:/databricks-gpt-5-mini"` or `"openai:/gpt-4o"`. ^[deepeval-scorers-databricks-on-aws.md]
- **`threshold`**: A float value that sets the pass/fail boundary for the metric. Scores above the threshold are considered passing. ^[deepeval-scorers-databricks-on-aws.md]
- **`include_reason`**: A boolean parameter that, when set to `True`, includes a reasoning explanation alongside the score in the feedback output. ^[deepeval-scorers-databricks-on-aws.md]

## Metric-Specific Parameters

Different DeepEval metrics accept specialized parameters tailored to their evaluation domain. For example, conversational metrics may accept parameters such as:

- **`window_size`**: Controls the number of conversation turns considered during evaluation. ^[deepeval-scorers-databricks-on-aws.md]
- **`strict_mode`**: A boolean that enables stricter evaluation criteria for the metric. ^[deepeval-scorers-databricks-on-aws.md]

For a complete list of metric-specific parameters and advanced usage options, refer to the [DeepEval documentation](https://docs.confident-ai.com/). ^[deepeval-scorers-databricks-on-aws.md]

## Creating Scorers with Configuration

Scorers are instantiated by passing configuration parameters directly to the metric constructor:

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

## Dynamic Scorer Creation

Scorers can also be created dynamically by name using `get_scorer`, which accepts the same configuration parameters:

```python
from mlflow.genai.scorers.deepeval import get_scorer

scorer = get_scorer(
    metric_name="AnswerRelevancy",
    threshold=0.7,
    model="databricks:/databricks-gpt-5-mini",
)
```

^[deepeval-scorers-databricks-on-aws.md]

## Available Scorer Categories

DeepEval provides scorers organized by evaluation domain, each with its own set of configuration parameters:

- **RAG metrics**: Evaluate retrieval quality and answer generation in RAG applications.
- **Agentic metrics**: Evaluate AI agent behavior, including task completion and tool usage.
- **Conversational metrics**: Evaluate multi-turn conversational AI quality.
- **Safety metrics**: Evaluate the safety and responsibility of model outputs.
- **Non-LLM metrics**: Metrics that do not require a language model for evaluation.

^[deepeval-scorers-databricks-on-aws.md]

## Related Concepts

- MLflow Evaluation Framework — The evaluation system that integrates DeepEval scorers.
- DeepEval Metrics — The full catalog of available evaluation metrics.
- [LLM-as-a-Judge Evaluation](/concepts/llm-as-a-judge-evaluation.md) — The paradigm underlying LLM-based scorers.
- RAG Evaluation — Evaluation strategies for retrieval-augmented generation systems.
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) — Evaluation of AI agent behavior and tool usage.

## Sources

- deepeval-scorers-databricks-on-aws.md

# Citations

1. [deepeval-scorers-databricks-on-aws.md](/references/deepeval-scorers-databricks-on-aws-95eb5ac0.md)
