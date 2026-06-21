---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 342a7d81ec25b0b75253cd1d83178b887b4c74aabf3c248e0d0e9bd5703918aa
  pageDirectory: concepts
  sources:
    - ragas-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - llm-based-vs-non-llm-ragas-scorers
    - LVNRS
  citations:
    - file: ragas-scorers-databricks-on-aws.md
title: LLM-based vs Non-LLM RAGAS Scorers
description: RAGAS scorers divide into LLM-based metrics that require a model parameter (e.g., Faithfulness) and non-LLM deterministic metrics that need no model (e.g., ExactMatch).
tags:
  - evaluation
  - configuration
  - LLM
timestamp: "2026-06-19T20:07:03.364Z"
---

# LLM-based vs Non-LLM RAGAS Scorers

**LLM-based vs Non-LLM RAGAS Scorers** distinguishes two categories of scorers provided by the [RAGAS](/concepts/ragas-retrieval-augmented-generation-assessment.md) (Retrieval Augmented Generation Assessment) evaluation framework as integrated with [MLflow](/concepts/mlflow.md). The key difference lies in whether the scorer requires a language model (LLM) to compute its score.

## Definition

RAGAS scorers are metrics used to evaluate the quality of LLM applications, including retrieval quality, answer generation, agent behavior, and text similarity. MLflow exposes these metrics as scorers for use with `mlflow.genai.evaluate()`. ^[ragas-scorers-databricks-on-aws.md]

## Core Distinction

### LLM-based Scorers

LLM-based scorers rely on a language model to produce the evaluation score. They require a `model` parameter to be specified when constructing the scorer. The model is typically a Databricks endpoint (e.g., `databricks:/databricks-gpt-5-mini`) or another compatible LLM. ^[ragas-scorers-databricks-on-aws.md]

**Example:**
```python
from mlflow.genai.scorers.ragas import Faithfulness
scorer = Faithfulness(model="databricks:/databricks-gpt-5-mini")
```

### Non-LLM Scorers

Non-LLM scorers do not require a language model. They use deterministic, rule-based, or heuristic methods (such as exact string matching) to compute scores. These scorers are constructed without a `model` parameter. ^[ragas-scorers-databricks-on-aws.md]

**Example:**
```python
from mlflow.genai.scorers.ragas import ExactMatch
deterministic_scorer = ExactMatch()  # No model required
```

## Configuration

When creating any RAGAS scorer, you can pass metric‑specific parameters as keyword arguments to the constructor. The presence or absence of the `model` parameter is the primary indicator of whether the scorer is LLM‑based:

- **LLM‑based metrics** → require `model`.
- **Non‑LLM metrics** → do not require `model`.

For metric‑specific parameters and advanced usage, consult the [RAGAS documentation](https://docs.ragas.io/). ^[ragas-scorers-databricks-on-aws.md]

## Dynamic Scorer Creation

You can create a scorer dynamically by name using the `get_scorer` function. The same model‑parameter rule applies: if the named metric is LLM‑based, `model` must be supplied; if non‑LLM, `model` is omitted. ^[ragas-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers.ragas import get_scorer
scorer = get_scorer(metric_name="Faithfulness", model="databricks:/databricks-gpt-5-mini")
```

## Categories of Available Scorers

The RAGAS integration provides scorers in several categories (see the Available RAGAS Scorers page for the full list). Both LLM‑based and non‑LLM scorers may appear within each category:

- RAG metrics
- Agent and tool use metrics
- Natural language comparison (includes both semantic — typically LLM‑based — and deterministic methods like ExactMatch)
- General purpose
- Other tasks

## Related Concepts

- [RAGAS](/concepts/ragas-retrieval-augmented-generation-assessment.md) – The underlying evaluation framework.
- [MLflow](/concepts/mlflow.md) – The platform that integrates RAGAS scorers.
- Faithfulness – An example of an LLM‑based scorer.
- ExactMatch – An example of a non‑LLM scorer.
- [mlflow.genai.evaluate()](/concepts/mlflowgenaievaluate.md) – Function that accepts a list of scorers.
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) – Relevant when the LLM endpoint requires a budget policy.

## Sources

- ragas-scorers-databricks-on-aws.md

# Citations

1. [ragas-scorers-databricks-on-aws.md](/references/ragas-scorers-databricks-on-aws-5240ee43.md)
