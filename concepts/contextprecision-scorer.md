---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e3c71d56eeaf3f3175526bf0b7487c79f93b9964449237b8a446642a35355f18
  pageDirectory: concepts
  sources:
    - ragas-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - contextprecision-scorer
    - Context Precision
    - ContextPrecision
  citations:
    - file: ragas-scorers-databricks-on-aws.md
title: ContextPrecision Scorer
description: A RAGAS scorer that evaluates retrieval quality by measuring how much of the retrieved context is relevant to the query.
tags:
  - evaluation
  - RAG
  - retrieval
timestamp: "2026-06-19T20:06:51.810Z"
---

# ContextPrecision Scorer

The **ContextPrecision Scorer** is a [RAGAS](/concepts/ragas-retrieval-augmented-generation-assessment.md) evaluation metric that measures the precision of retrieved context in [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) applications. It is available as an MLflow scorer for evaluating retrieval quality in LLM applications. ^[ragas-scorers-databricks-on-aws.md]

## Overview

ContextPrecision evaluates how well the retrieved context supports the generated answer. It is one of several RAG metrics provided by the RAGAS evaluation framework and is categorized as a retrieval quality metric within the RAGAS scoring system. ^[ragas-scorers-databricks-on-aws.md]

## Usage

The ContextPrecision Scorer is available through the `mlflow.genai.scorers.ragas` module. Like other LLM-based RAGAS scorers, it requires a `model` parameter to be specified during initialization. ^[ragas-scorers-databricks-on-aws.md]

### Direct Scoring

To call a ContextPrecision scorer directly on a trace:

```python
from mlflow.genai.scorers.ragas import ContextPrecision

scorer = ContextPrecision(model="databricks:/databricks-gpt-5-mini")
feedback = scorer(trace=trace)

print(feedback.value)   # Score between 0.0 and 1.0
print(feedback.rationale)  # Explanation of the score
```

^[ragas-scorers-databricks-on-aws.md]

### Using with mlflow.genai.evaluate()

ContextPrecision can be used as part of a multi-scorer evaluation:

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

^[ragas-scorers-databricks-on-aws.md]

### Dynamic Creation

The scorer can also be created dynamically using `get_scorer`:

```python
from mlflow.genai.scorers.ragas import get_scorer

scorer = get_scorer(
    metric_name="ContextPrecision",
    model="databricks:/databricks-gpt-5-mini",
)
feedback = scorer(trace=trace)
```

^[ragas-scorers-databricks-on-aws.md]

## Requirements

To use the ContextPrecision scorer, the `ragas` package must be installed in the environment. ^[ragas-scorers-databricks-on-aws.md]

## Related Concepts

- [RAGAS](/concepts/ragas-retrieval-augmented-generation-assessment.md) — The evaluation framework that provides the ContextPrecision metric
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The evaluation framework that integrates RAGAS scorers
- RAG metrics — The category of scorers that includes ContextPrecision
- [Faithfulness Scorer](/concepts/faithfulness-scorer.md) — A complementary RAGAS scorer that evaluates answer accuracy
- ContextRecall Scorer — Another RAGAS metric for evaluating retrieved context completeness
- [LLM Evaluation](/concepts/llm-as-a-judge-evaluation.md) — Broader context for scoring LLM applications

## Sources

- ragas-scorers-databricks-on-aws.md

# Citations

1. [ragas-scorers-databricks-on-aws.md](/references/ragas-scorers-databricks-on-aws-5240ee43.md)
