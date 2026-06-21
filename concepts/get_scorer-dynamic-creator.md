---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dd9a28fef3d819cb9e850df694199db8ef0dcaf8e42fc64d2c3d639f5854ba29
  pageDirectory: concepts
  sources:
    - ragas-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - get_scorer-dynamic-creator
    - GDC
  citations:
    - file: ragas-scorers-databricks-on-aws.md
title: get_scorer Dynamic Creator
description: A function in mlflow.genai.scorers.ragas that allows creating a RAGAS scorer at runtime by passing the metric name as a string, enabling dynamic evaluation workflows.
tags:
  - MLflow
  - API
  - dynamic-configuration
timestamp: "2026-06-19T20:06:53.007Z"
---

## `get_scorer` Dynamic Creator

The `get_scorer` function provides a way to dynamically create a [RAGAS scorer](/concepts/ragas-scorers-in-mlflow.md) by specifying the metric name as a string. This is useful when the scorer type is not known until runtime or when building evaluation pipelines that select metrics programmatically.

### Usage

To use `get_scorer`, import it from `mlflow.genai.scorers.ragas` and pass the metric name along with any required arguments (such as the `model` parameter for LLM-based metrics). The function returns a scorer object that can then be invoked on a trace.

```python
from mlflow.genai.scorers.ragas import get_scorer

scorer = get_scorer(
    metric_name="Faithfulness",
    model="databricks:/databricks-gpt-5-mini",
)
feedback = scorer(trace=trace)
```

^[ragas-scorers-databricks-on-aws.md]

The metric name must match one of the available RAGAS scorer class names. The function is designed to work with both LLM-based and non-LLM metrics. For non-LLM metrics, the `model` parameter is not required.

### Context

`get_scorer` is part of the `mlflow.genai.scorers.ragas` module, which integrates the [RAGAS](/concepts/ragas-retrieval-augmented-generation-assessment.md) evaluation framework with [MLflow](/concepts/mlflow.md). It enables the same set of metrics available through direct constructor calls (e.g., `Faithfulness()`, `ExactMatch()`) but with a dynamic, string-based interface. ^[ragas-scorers-databricks-on-aws.md]

This dynamic creation is particularly useful when building automated evaluation systems that read metric configurations from a file, database, or user input.

### Related Concepts

- [RAGAS scorers](/concepts/ragas-scorers-in-mlflow.md) — The full set of available metrics (RAG, agent, natural language, general purpose).
- [MLflow evaluation](/concepts/mlflow-evaluation-ui.md) — The broader MLflow evaluation workflow, including `mlflow.genai.evaluate()`.
- Faithfulness — An example of a specific scorer that can be created via `get_scorer`.
- [RAGAS](/concepts/ragas-retrieval-augmented-generation-assessment.md) — The underlying retrieval-augmented generation assessment framework.

### Sources

- ragas-scorers-databricks-on-aws.md

# Citations

1. [ragas-scorers-databricks-on-aws.md](/references/ragas-scorers-databricks-on-aws-5240ee43.md)
