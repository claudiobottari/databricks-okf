---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4ed0f3d3b878a9fbe5277efc05a317c1c6f1e0ffdb9c5035c03939e2dc689862
  pageDirectory: concepts
  sources:
    - evaluate-genai-apps-during-development-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-evaluation-datasets
    - MED
    - Building MLflow Evaluation Datasets
    - Building MLflow evaluation datasets
    - build MLflow evaluation datasets
  citations:
    - file: evaluate-genai-apps-during-development-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: MLflow Evaluation Datasets
description: Structured test data used as input for GenAI evaluations, available in formats like EvaluationDataset, list of dicts, Pandas DataFrame, or Spark DataFrame.
tags:
  - mlflow
  - evaluation
  - datasets
timestamp: "2026-06-18T12:12:57.351Z"
---

# MLflow Evaluation Datasets

**MLflow Evaluation Datasets** are structured collections of test inputs — and optionally expected outputs — used to evaluate GenAI applications in the MLflow evaluation framework. They serve as the `data` parameter in [`mlflow.genai.evaluate()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.evaluate) and provide the foundation for systematic, reproducible quality assessment across development, staging, and production environments. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Purpose

Evaluation datasets enable structured, repeatable testing of GenAI applications. Instead of manually checking outputs one by one, you feed a curated dataset into `mlflow.genai.evaluate()`, which runs your app against each test case and automatically scores the results using [[scorers]] or [LLM Judges](/concepts/llm-judges.md). ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

This makes it easier to compare versions, track improvements, and share results across teams. The same evaluation dataset can be reused for [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) to quantify the impact of changes before promoting a configuration to production. ^[evaluate-genai-apps-during-development-databricks-on-aws.md, create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Supported Formats

The `data` parameter accepts evaluation data in the following formats: ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

| Format | Description |
|--------|-------------|
| `EvaluationDataset` (recommended) | Structured dataset object that enforces schema validation and tracks lineage of each record |
| List of dictionaries | A Python list where each dictionary represents one test case |
| Pandas DataFrame | A DataFrame where each row represents one test case |
| Spark DataFrame | A Spark DataFrame where each row represents one test case |

Databricks recommends using an `EvaluationDataset` as it enforces schema validation and provides lineage tracking. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Schema

When the data argument is provided as a DataFrame or list of dictionaries, it must follow a specific schema that is consistent with the schema used by `EvaluationDataset`. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

### For Direct Evaluation

Direct evaluation calls your GenAI app during evaluation. The dataset must contain `inputs` dictionaries: ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

```python
data = [
    {"inputs": {"question": "What is MLflow?"}},
    {"inputs": {"question": "How do I get started?"}},
]
```

The `inputs` keys are passed as keyword arguments to the `predict_fn`. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

### For Answer Sheet Evaluation

Answer sheet evaluation uses pre-computed outputs or existing traces. The dataset can include: ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

**Inputs and outputs:**

```python
data = [
    {
        "inputs": {"question": "What is MLflow?"},
        "outputs": {"response": "MLflow is an open-source platform..."},
    },
]
```

**Existing traces:**

```python
traces = mlflow.search_traces(filter_string="trace.status = 'OK'")
data = traces
```

## Using `EvaluationDataset`

The `mlflow.genai.datasets.EvaluationDataset` class provides a recommended way to define evaluation data with schema validation and lineage tracking. See [Building MLflow evaluation datasets](/concepts/mlflow-evaluation-datasets.md) for more details. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Links to Evaluation Modes

The format of your evaluation dataset determines which evaluation mode you can use: ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

- **Direct evaluation (recommended):** MLflow calls your app directly using the `inputs` from the dataset and generates traces for evaluation. Requires a `predict_fn`.
- **Answer sheet evaluation:** You provide pre-computed outputs or existing traces. MLflow scores the outputs without calling your app.

## Best Practices

- **Use a representative dataset.** Test cases should reflect the range of real-world inputs your app will encounter in production. See [Evaluate GenAI applications at development](/concepts/genai-application-evaluation-lifecycle.md). ^[evaluate-genai-apps-during-development-databricks-on-aws.md]
- **Reuse datasets across configurations.** Running the same evaluation dataset against multiple agent configurations with consistent judges enables fair [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md).
- **Use `EvaluationDataset`** to benefit from schema validation and lineage tracking.
- **Include expectations for richer evaluation.** The dataset can optionally include `expectations` that judges can reference for more accurate scoring.

## Related Concepts

- [Evaluate GenAI applications at development](/concepts/genai-application-evaluation-lifecycle.md) — Overview of the evaluation framework
- [Building MLflow evaluation datasets](/concepts/mlflow-evaluation-datasets.md) — Creating structured test data
- [[Scorers]] — Quality metrics applied to evaluation results
- [Evaluation runs in MLflow](/concepts/evaluation-run-mlflow.md) — Results storage and comparison
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Comparing configurations using shared datasets
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Reusing evaluation datasets in production

## Sources

- evaluate-genai-apps-during-development-databricks-on-aws.md
- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [evaluate-genai-apps-during-development-databricks-on-aws.md](/references/evaluate-genai-apps-during-development-databricks-on-aws-373c1693.md)
2. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
