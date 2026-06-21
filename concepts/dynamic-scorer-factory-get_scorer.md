---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 884ae5fee52d07c468d6ce9735c96f36f49f3a45578e9ab1485c7bb7313c881f
  pageDirectory: concepts
  sources:
    - deepeval-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dynamic-scorer-factory-get_scorer
    - DSF(
  citations:
    - file: deepeval-scorers-databricks-on-aws.md
title: Dynamic Scorer Factory (get_scorer)
description: MLflow's get_scorer() function enables dynamic creation of DeepEval scorers by passing the metric name as a string parameter.
tags:
  - mlflow
  - deepeval
  - scorer
  - factory-pattern
timestamp: "2026-06-19T18:19:26.261Z"
---

# Dynamic Scorer Factory (get_scorer)

The **Dynamic Scorer Factory** (`get_scorer`) is a function provided by the MLflow DeepEval integration that allows you to dynamically create a scorer by passing the metric name as a string, rather than importing the scorer class directly. This factory pattern enables programmatic selection and instantiation of evaluation metrics at runtime. ^[deepeval-scorers-databricks-on-aws.md]

## Overview

The `get_scorer` function is part of the `mlflow.genai.scorers.deepeval` module. It accepts a `metric_name` parameter as a string, along with any configuration parameters required by the specific metric. This approach is particularly useful when metric selection needs to be determined dynamically, such as from configuration files, user input, or conditional logic. ^[deepeval-scorers-databricks-on-aws.md]

## Usage

To create a scorer dynamically, import `get_scorer` and call it with the metric name and any required parameters:

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

The `get_scorer` function accepts the following parameters:

- **`metric_name`** (string): The name of the DeepEval metric to instantiate. This corresponds to the class name of the metric, such as `"AnswerRelevancy"`, `"Faithfulness"`, or `"TurnRelevancy"`.
- **Additional keyword arguments**: Any parameters required by the specific metric, such as `threshold`, `model`, `include_reason`, `window_size`, or `strict_mode`. These are passed through to the metric constructor. ^[deepeval-scorers-databricks-on-aws.md]

## Available Metrics

The factory can create any of the available DeepEval scorers, including:

- **RAG metrics**: For evaluating retrieval quality and answer generation in [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) applications
- **Agentic metrics**: For evaluating AI agent behavior, including task completion and tool usage
- **Conversational metrics**: For evaluating multi-turn conversational AI quality
- **Safety metrics**: For evaluating the safety and responsibility of model outputs
- **Non-LLM metrics**: For evaluations that do not require a language model

^[deepeval-scorers-databricks-on-aws.md]

## Use Cases

The dynamic scorer factory is particularly useful in the following scenarios:

- **Configuration-driven evaluation**: Loading metric configurations from YAML or JSON files and instantiating scorers dynamically
- **User-selected metrics**: Allowing users to choose which metrics to apply at runtime
- **Conditional evaluation logic**: Selecting different metrics based on model type, domain, or other runtime conditions
- **Automated evaluation pipelines**: Programmatically constructing evaluation workflows without hardcoding metric imports

## Related Concepts

- [DeepEval Scorers](/concepts/deepeval-scorer-api.md) — The full set of evaluation metrics available through the MLflow DeepEval integration
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The broader evaluation framework that uses scorers for model assessment
- [LLM Evaluation Metrics](/concepts/llm-as-a-judge-evaluation-metrics.md) — General concepts for evaluating large language model outputs
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) — A common application pattern evaluated by RAG-specific metrics

## Sources

- deepeval-scorers-databricks-on-aws.md

# Citations

1. [deepeval-scorers-databricks-on-aws.md](/references/deepeval-scorers-databricks-on-aws-95eb5ac0.md)
