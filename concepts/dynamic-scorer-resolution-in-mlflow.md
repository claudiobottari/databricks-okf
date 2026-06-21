---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 818f8a1760ced4e4e8f168d1618733e55b439151c54378e9c6e1572859d5e7de
  pageDirectory: concepts
  sources:
    - deepeval-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dynamic-scorer-resolution-in-mlflow
    - DSRIM
  citations:
    - file: deepeval-scorers-databricks-on-aws.md
title: Dynamic Scorer Resolution in MLflow
description: MLflow's get_scorer factory function allows creating DeepEval scorers dynamically by passing a metric name as a string parameter.
tags:
  - mlflow
  - factory-pattern
  - api
timestamp: "2026-06-19T14:58:37.882Z"
---

## Dynamic Scorer Resolution in MLflow

**Dynamic Scorer Resolution** refers to the ability to select and instantiate an evaluation scorer at runtime by using a metric name string, rather than importing the scorer class directly. This enables flexible and configurable evaluation pipelines where the metric to use can be determined after code is written, for example based on user input or experiment metadata.

### Overview

MLflow integrates with third-party evaluation frameworks such as DeepEval to provide a wide range of scorers for LLM applications. While scorers can be directly instantiated by importing their class (e.g., `AnswerRelevancy`), they can also be resolved dynamically using a name-based lookup. This dynamic resolution simplifies switching between metrics without changing import statements or hard-coding scorer constructors. ^[deepeval-scorers-databricks-on-aws.md]

### Dynamic Scorer Creation by Name

The function `mlflow.genai.scorers.deepeval.get_scorer()` accepts a metric name as a string and returns a fully configured scorer instance. All other constructor parameters (such as `threshold` and `model`) are passed as keyword arguments to the function. ^[deepeval-scorers-databricks-on-aws.md]

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

The `metric_name` must match one of the available metric classes in the DeepEval integration (e.g., `AnswerRelevancy`, `Faithfulness`, `TurnRelevancy`). This approach allows scorers to be selected from a configuration file, an API response, or a dynamic list without prior knowledge of the metric class. ^[deepeval-scorers-databricks-on-aws.md]

### Configuration

Scorers created dynamically accept the same metric-specific parameters as their directly instantiated counterparts. LLM-based metrics require a `model` parameter, which can be a Databricks endpoint (`databricks:/model-name`), an OpenAI endpoint (`openai:/model-name`), or another supported provider. Additional parameters such as `threshold`, `include_reason`, and metric‑specific options (e.g., `window_size`, `strict_mode`) can be passed as keyword arguments. ^[deepeval-scorers-databricks-on-aws.md]

Parameter validation and defaults are defined by the underlying DeepEval library; see the [DeepEval documentation](https://docs.confident-ai.com/) for details on each metric’s supported parameters. ^[deepeval-scorers-databricks-on-aws.md]

### Benefits

- **Flexibility:** The evaluation metric can be chosen at runtime, enabling A/B testing, dynamic experimentation, or user‑configurable dashboards.
- **Code simplicity:** A single code path can handle many metrics without nested imports or conditional logic.
- **Extensibility:** New metrics added to the DeepEval library become available through `get_scorer()` without code changes in the application (as long as they are registered by the library).

### Related Concepts

- [DeepEval scorers](/concepts/deepeval-scorer-api.md) – Full list of available metrics and their usage.
- MLflow evaluate – The evaluation API that accepts scorers dynamically.
- [Scorer in MLflow](/concepts/scorers-mlflow-genai.md) – General concept of evaluation scorers in the MLflow framework.
- Configuration-driven evaluation – Pattern where metrics are specified in config files.

### Sources

- deepeval-scorers-databricks-on-aws.md

# Citations

1. [deepeval-scorers-databricks-on-aws.md](/references/deepeval-scorers-databricks-on-aws-95eb5ac0.md)
