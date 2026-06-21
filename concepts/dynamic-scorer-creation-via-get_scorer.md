---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2481dafb839db1ca1a7bde10cae80ec593ddd6357a7a6be9065ea6775b600470
  pageDirectory: concepts
  sources:
    - deepeval-scorers-databricks-on-aws.md
    - ragas-scorers-databricks-on-aws.md
    - trulens-scorers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - dynamic-scorer-creation-via-get_scorer
    - DSCVG
  citations:
    - file: deepeval-scorers-databricks-on-aws.md
    - file: ragas-scorers-databricks-on-aws.md
    - file: trulens-scorers-databricks-on-aws.md
title: Dynamic Scorer Creation via get_scorer
description: DeepEval scorers can be created dynamically at runtime by passing the metric name as a string to the get_scorer function.
tags:
  - api
  - dynamic-creation
  - scorer
timestamp: "2026-06-18T11:47:39.444Z"
---

# Dynamic Scorer Creation via `get_scorer`

**Dynamic Scorer Creation via `get_scorer`** refers to the ability to instantiate a scorer from the DeepEval, [RAGAS](/concepts/ragas-retrieval-augmented-generation-assessment.md), or TruLens integrations by passing the metric name as a string, rather than importing the scorer class directly. This approach allows you to select evaluation metrics programmatically — for example, based on configuration files, user input, or experiment metadata — without hardcoding specific scorer classes.^[deepeval-scorers-databricks-on-aws.md, ragas-scorers-databricks-on-aws.md, trulens-scorers-databricks-on-aws.md]

## How It Works

Each third-party scorer module in MLflow provides a `get_scorer` function. You pass the desired metric name as a string (`metric_name`), along with any required keyword arguments such as `model` or `threshold`. The function returns an instantiated scorer object that can be called directly or passed to `mlflow.genai.evaluate()`.^[deepeval-scorers-databricks-on-aws.md, ragas-scorers-databricks-on-aws.md, trulens-scorers-databricks-on-aws.md]

### Generic Pattern

```python
from mlflow.genai.scorers.<framework> import get_scorer

scorer = get_scorer(
    metric_name="<MetricClass>",
    model="<model-uri>",
    # additional framework-specific kwargs
)
```

## Usage Examples

### DeepEval

The DeepEval integration provides a `get_scorer` function in `mlflow.genai.scorers.deepeval`. The following example creates an `AnswerRelevancy` scorer:^[deepeval-scorers-databricks-on-aws.md]

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

### RAGAS

The RAGAS integration provides a `get_scorer` function in `mlflow.genai.scorers.ragas`. The following example creates a `Faithfulness` scorer:^[ragas-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers.ragas import get_scorer

scorer = get_scorer(
    metric_name="Faithfulness",
    model="databricks:/databricks-gpt-5-mini",
)
feedback = scorer(trace=trace)
```

### TruLens

The TruLens integration provides a `get_scorer` function in `mlflow.genai.scorers.trulens`. The following example creates a `Groundedness` scorer:^[trulens-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers.trulens import get_scorer

scorer = get_scorer(
    metric_name="Groundedness",
    model="openai:/gpt-5-mini",
)
feedback = scorer(
    inputs="What is MLflow?",
    outputs="MLflow is a platform for ML workflows.",
    expectations={"context": "MLflow is an ML platform."},
)
```

## Configuration

The `get_scorer` function accepts the same keyword arguments as the corresponding scorer class constructor. Common parameters include:

| Parameter | Description | Applies to |
|-----------|-------------|------------|
| `model` | The LLM model to use for evaluation (e.g., `"databricks:/databricks-gpt-5-mini"`, `"openai:/gpt-4o"`). Required for LLM-based metrics. | DeepEval, RAGAS, TruLens |
| `threshold` | The pass/fail threshold for the scorer. Defaults vary by metric. | DeepEval, TruLens |
| `include_reason` | Whether to include a reasoning string in the feedback. | DeepEval |
| `strict_mode` | Enables stricter evaluation criteria. | DeepEval |

For metric-specific parameters, refer to the documentation of the respective framework: [DeepEval scorers](/concepts/deepeval-scorer-api.md), [RAGAS scorers](/concepts/ragas-scorers-in-mlflow.md), [TruLens scorers](/concepts/trulens-scorers-integration.md).

## Available Metric Names

The `metric_name` string must match the class name of an available scorer. The full lists are documented in the individual framework pages:

- [DeepEval scorers#Available DeepEval scorers](/concepts/deepeval-scorer-categories.md)
- [RAGAS scorers#Available RAGAS scorers](/concepts/ragas-scorers-in-mlflow.md)
- [TruLens scorers#Available TruLens scorers](/concepts/trulens-scorers-integration.md)

## Use Cases

- **Configuration-driven evaluation:** Store metric names in a YAML or JSON file and create scorers dynamically without changing code.
- **Experiment orchestration:** Programmatically iterate over multiple metrics to compare their results.
- **Parameter sweeps:** Vary `threshold`, `model`, or other parameters while keeping the metric fixed.
- **Custom pipelines:** Assemble evaluation pipelines where the set of scorers is determined at runtime based on experiment metadata.

## Related Concepts

- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The overall evaluation framework using scorers.
- [Third-party Scorers](/concepts/third-party-scorers-in-mlflow-genai.md) — Overview of integrating DeepEval, RAGAS, TruLens.
- [Scorer Registration](/concepts/scorer-registration-and-registry.md) — How to register custom scorers for production monitoring.
- MLflow Evaluation API — The `mlflow.genai.evaluate()` function that consumes scorers.

## Sources

- deepeval-scorers-databricks-on-aws.md
- ragas-scorers-databricks-on-aws.md
- trulens-scorers-databricks-on-aws.md

# Citations

1. [deepeval-scorers-databricks-on-aws.md](/references/deepeval-scorers-databricks-on-aws-95eb5ac0.md)
2. [ragas-scorers-databricks-on-aws.md](/references/ragas-scorers-databricks-on-aws-5240ee43.md)
3. [trulens-scorers-databricks-on-aws.md](/references/trulens-scorers-databricks-on-aws-ae1e6065.md)
