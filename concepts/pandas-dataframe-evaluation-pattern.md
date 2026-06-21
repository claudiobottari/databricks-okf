---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 508791b14abc7b0cf1959059f9dce8bae39706b4ed553fe4dda1e92eb4dacfc1
  pageDirectory: concepts
  sources:
    - mlflow-evaluation-examples-for-genai-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pandas-dataframe-evaluation-pattern
    - PDEP
  citations:
    - file: mlflow-evaluation-examples-for-genai-databricks-on-aws.md
title: Pandas DataFrame Evaluation Pattern
description: Using Pandas DataFrames for GenAI evaluation when working with CSV files or existing data science workflows.
tags:
  - mlflow
  - evaluation
  - pandas
timestamp: "2026-06-19T19:38:13.599Z"
---

# Pandas DataFrame Evaluation Pattern

The **Pandas DataFrame Evaluation Pattern** is a method for evaluating [GenAI](/concepts/mlflow-genai-evaluate-api.md) applications using [MLflow](/concepts/mlflow.md)'s evaluation harness with data provided as a Pandas DataFrame. This pattern is useful for quick prototyping, working with small datasets (fewer than 100 examples), and informal development testing, particularly when evaluation data originates from CSV files or existing data science workflows. ^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

## Overview

When using the Pandas DataFrame Evaluation Pattern, you create a Pandas DataFrame where each row represents an evaluation example. The DataFrame must contain an `inputs` column with dictionary values that correspond to the parameters expected by your prediction function. Optionally, you can include an `expectations` column with expected outputs for comparison. ^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

## Basic Usage

The pattern follows a straightforward structure where you construct a DataFrame, define your prediction function, and pass both to `mlflow.genai.evaluate()` along with the desired scorers. ^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

```python
import mlflow
import pandas as pd
from mlflow.genai.scorers import Correctness, Safety
from my_app import agent  # Your GenAI app with tracing

# Create evaluation data as a Pandas DataFrame
eval_df = pd.DataFrame([
    {
        "inputs": {"question": "What is MLflow?"},
        "expectations": {"expected_response": "MLflow is the largest open source AI engineering platform for agents, LLMs, and ML models."}
    },
    {
        "inputs": {"question": "How do I log metrics?"},
        "expectations": {"expected_response": "Use mlflow.log_metric() to log metrics"}
    }
])

# Run evaluation
results = mlflow.genai.evaluate(
    data=eval_df,
    predict_fn=agent,
    scorers=[Correctness(), Safety()],
)
```

^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

## Data Structure Requirements

The DataFrame must comply with the [Evaluation Dataset Schema](/concepts/evaluation-dataset-schema.md). Each row should contain:

- **`inputs`**: A dictionary where keys match the parameter names of your `predict_fn`. For example, if your function accepts a `question` parameter, the `inputs` dictionary should include a `"question"` key. ^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]
- **`expectations`** (optional): A dictionary containing expected outputs, such as `expected_response` or `expected_facts`, used by scorers like Correctness for comparison. ^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

## When to Use

The Pandas DataFrame Evaluation Pattern is appropriate for:

- Quick prototyping and experimentation
- Small datasets (fewer than 100 examples)
- Informal development testing
- Working with data from CSV files or existing data science workflows

For production use cases, consider converting to an [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md), which provides versioning, lineage tracking, and integration with [Unity Catalog](/concepts/unity-catalog.md). ^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

## Comparison with Other Data Patterns

| Pattern | Use Case |
|---------|----------|
| [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md) | Production-ready evaluation with versioning and lineage |
| [List of Dictionaries Pattern](/concepts/list-of-dictionaries-evaluation-pattern.md) | Quick prototyping without DataFrame creation |
| **Pandas DataFrame Evaluation Pattern** | CSV files and existing data science workflows |
| [Spark DataFrame Evaluation Pattern](/concepts/spark-dataframe-evaluation-pattern.md) | Large-scale evaluations with Delta Lake or Unity Catalog |

^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

## Related Concepts

- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The overall evaluation framework for GenAI applications
- Predict Function Patterns — Different ways to structure `predict_fn` for evaluation
- [GenAI Scorers](/concepts/mlflow-genai-scorers.md) — Metrics and scoring functions used in evaluation
- [Evaluation Dataset Schema](/concepts/evaluation-dataset-schema.md) — The required structure for evaluation data

## Sources

- mlflow-evaluation-examples-for-genai-databricks-on-aws.md

# Citations

1. [mlflow-evaluation-examples-for-genai-databricks-on-aws.md](/references/mlflow-evaluation-examples-for-genai-databricks-on-aws-2da85b83.md)
