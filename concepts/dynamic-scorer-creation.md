---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bfc3d848aac5f278e168be9fa6b6ede7028fffddef58febda60af152d65b1806
  pageDirectory: concepts
  sources:
    - deepeval-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dynamic-scorer-creation
    - DSC
  citations:
    - file: deepeval-scorers-databricks-on-aws.md
title: Dynamic Scorer Creation
description: DeepEval scorers can be created dynamically at runtime using get_scorer() by passing the metric name as a string, enabling flexible evaluation pipelines.
tags:
  - api
  - scorers
  - dynamic-creation
timestamp: "2026-06-19T09:58:52.887Z"
---

# Dynamic Scorer Creation

**Dynamic Scorer Creation** refers to the ability to instantiate evaluation scorers at runtime by passing a metric name as a string, rather than importing and instantiating a specific scorer class directly. This pattern is particularly useful when you need to select evaluation metrics dynamically based on configuration, user input, or variable program conditions.

## Overview

In MLflow GenAI evaluation workflows, scorers are typically instantiated by importing a specific class (e.g., `AnswerRelevancy`) and calling its constructor with required parameters. Dynamic creation provides an alternative that decouples metric selection from code structure. ^[deepeval-scorers-databricks-on-aws.md]

Dynamic creation is available through the `get_scorer` function from the `mlflow.genai.scorers.deepeval` module. This function accepts a metric name as a string and returns an instantiated scorer object configured with the parameters you provide. ^[deepeval-scorers-databricks-on-aws.md]

## Usage

To create a scorer dynamically:

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

## Parameters

The `get_scorer` function accepts the metric name as the first argument, followed by metric-specific parameters as keyword arguments. For LLM-based metrics, a `model` parameter is required to specify which language model to use for evaluation. ^[deepeval-scorers-databricks-on-aws.md]

## Benefits

- **Flexibility**: Metrics can be selected from configuration files, environment variables, or runtime logic without changing code structure. ^[deepeval-scorers-databricks-on-aws.md]
- **Reduced boilerplate**: A single function call replaces multiple import statements and constructor calls when working with many different metric types. ^[deepeval-scorers-databricks-on-aws.md]
- **Simplified experimentation**: Makes it straightforward to run evaluation pipelines that compare results across multiple metrics without rewriting the evaluation loop. ^[deepeval-scorers-databricks-on-aws.md]

## Related Concepts

- [DeepEval Scorers](/concepts/deepeval-scorer-api.md) — The full set of available evaluation metrics
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The broader platform for agent and LLM evaluation
- [Custom Judges](/concepts/custom-judges.md) — Alternative approach for creating user-defined evaluation criteria
- Evaluation Pipelines — Programmatic workflows that combine multiple scorers

## Sources

- deepeval-scorers-databricks-on-aws.md

# Citations

1. [deepeval-scorers-databricks-on-aws.md](/references/deepeval-scorers-databricks-on-aws-95eb5ac0.md)
