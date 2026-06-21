---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 900608cf046dde92f500c080eb1d52499108041213495bc87979b06ec1a9d109
  pageDirectory: concepts
  sources:
    - deepeval-scorers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - non-llm-metrics-in-deepeval
    - NMID
  citations:
    - file: deepeval-scorers-databricks-on-aws.md
title: Non-LLM Metrics in DeepEval
description: A category of DeepEval metrics that do not require an LLM as a judge, enabling evaluation without calling a language model.
tags:
  - deepeval
  - metrics
  - non-llm
  - evaluation
timestamp: "2026-06-19T18:19:43.575Z"
---

# Non-LLM Metrics in DeepEval

**Non-LLM Metrics in DeepEval** are evaluation metrics provided by the [DeepEval](https://docs.confident-ai.com/) framework that do not rely on a language model to compute their scores. These metrics complement the LLM-based metrics (such as `AnswerRelevancy` and `Faithfulness`) and cover a variety of evaluation dimensions for LLM applications, including retrieval quality, agent behavior, conversational quality, and safety. ^[deepeval-scorers-databricks-on-aws.md]

## Overview

DeepEval integrates with [MLflow](/concepts/mlflow.md) through the `mlflow.genai.scorers.deepeval` module. Users can instantiate non‑LLM metrics as scorer objects and use them directly or inside `mlflow.genai.evaluate()` just like any other DeepEval scorer. Non‑LLM metrics accept metric‑specific configuration parameters (e.g., `threshold`, `include_reason`) but do not require a `model` argument, because they do not call an external LLM to produce a judgment. ^[deepeval-scorers-databricks-on-aws.md]

## Available Categories of Non‑LLM Metrics

DeepEval structures its metrics into several categories. The non‑LLM metrics are listed under the “Non‑LLM metrics” heading in the framework documentation. While the specific metric names are not enumerated in the MLflow integration documentation, the categories that **may** contain non‑LLM metrics include:

- RAG Evaluation|RAG metrics – evaluate retrieval quality and answer generation in retrieval‑augmented generation systems.
- Agent Evaluation|Agentic metrics – evaluate AI agent behavior, including task completion and tool usage.
- [Conversational AI Evaluation|Conversational metrics](/concepts/conversation-evaluation.md) – evaluate multi‑turn conversational AI quality.
- Safety Evaluation|Safety metrics – evaluate the safety and responsibility of model outputs.
- **Other metrics** – a catch‑all category for additional evaluation dimensions.

*Note: Not all metrics in these categories are necessarily non‑LLM; some may still rely on an LLM. The DeepEval documentation should be consulted for the definitive list of non‑LLM metrics.* ^[deepeval-scorers-databricks-on-aws.md]

## Usage

Non‑LLM metric scorers are created identically to LLM‑based scorers, except that the `model` parameter is omitted. For example, a hypothetical non‑LLM scorer called `Toxicity` (a safety metric) might be instantiated as:

```python
from mlflow.genai.scorers.deepeval import Toxicity

scorer = Toxicity(threshold=0.5)
```

Such a scorer can then be used in evaluations:

```python
import mlflow
from mlflow.genai.scorers.deepeval import Toxicity, AnswerRelevancy

eval_dataset = [
    {"inputs": "What is MLflow?", "outputs": "MLflow is an open‑source platform."},
]

results = mlflow.genai.evaluate(
    data=eval_dataset,
    scorers=[
        Toxicity(threshold=0.5),
        AnswerRelevancy(threshold=0.7, model="databricks:/databricks-gpt-5-mini"),
    ],
)
```

The exact metric name must be confirmed from the DeepEval documentation. ^[deepeval-scorers-databricks-on-aws.md]

## Related Concepts

- DeepEval – The evaluation framework that provides these metrics.
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – The MLflow module that integrates DeepEval scorers.
- [LLM Evaluation Metrics](/concepts/llm-as-a-judge-evaluation-metrics.md) – LLM‑based metrics that do require a `model` argument.
- RAG Evaluation – Evaluation of retrieval‑augmented generation systems.
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) – Evaluation of AI agent behavior.
- [Conversational AI Evaluation](/concepts/conversation-evaluation.md) – Evaluation of multi‑turn chatbots.
- Safety Evaluation – Evaluation of model output safety.

## Sources

- deepeval-scorers-databricks-on-aws.md

# Citations

1. [deepeval-scorers-databricks-on-aws.md](/references/deepeval-scorers-databricks-on-aws-95eb5ac0.md)
