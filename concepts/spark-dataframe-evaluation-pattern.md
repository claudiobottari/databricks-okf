---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 738283d21ce0b20030242523a28d4fedc0cd88c2622bbe860ec2f2b9cb6e5022
  pageDirectory: concepts
  sources:
    - mlflow-evaluation-examples-for-genai-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark-dataframe-evaluation-pattern
    - SDEP
    - Spark DataFrame
  citations:
    - file: mlflow-evaluation-examples-for-genai-databricks-on-aws.md
title: Spark DataFrame Evaluation Pattern
description: Using Spark DataFrames for large-scale GenAI evaluation when data resides in Delta Lake or Unity Catalog.
tags:
  - mlflow
  - evaluation
  - spark
timestamp: "2026-06-19T19:38:26.306Z"
---

# Spark DataFrame Evaluation Pattern

The **Spark DataFrame Evaluation Pattern** is a usage pattern in [MLflow](/concepts/mlflow.md) GenAI evaluation where the input data is sourced from a [Spark DataFrame](/concepts/spark-dataframe-evaluation-pattern.md) rather than from in-memory Python structures. This pattern is suitable for large-scale evaluations, production pipelines, and scenarios where evaluation data already resides in [Delta Lake](/concepts/delta-lake.md) or [Unity Catalog](/concepts/unity-catalog.md).

## Overview

When evaluating a GenAI application at scale, the evaluation data often lives in distributed storage rather than in local memory. The Spark DataFrame Evaluation Pattern allows you to pass a Spark DataFrame directly to `mlflow.genai.evaluate()`, enabling distributed evaluation without materializing the data in the driver process. ^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

## Usage

The pattern is straightforward: you load or reference a Spark DataFrame from any Spark-compatible source and pass it as the `data` parameter to `mlflow.genai.evaluate()`. The [GenAI evaluation](/concepts/mlflow-genai-evaluation.md) framework handles the distributed reading and processing of the data. ^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

### Loading from Delta Lake or Unity Catalog

```python
import mlflow
from mlflow.genai.scorers import Safety, RelevanceToQuery
from my_app import agent  # Your GenAI app with tracing

# Load evaluation data from a Delta table in Unity Catalog
eval_df = spark.table("catalog.schema.evaluation_data")

# Run evaluation
results = mlflow.genai.evaluate(
    data=eval_df,
    predict_fn=agent,
    scorers=[Safety(), RelevanceToQuery()],
)
```

^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

### Loading from Other Spark-Compatible Sources

```python
# Load from any Spark-compatible source
eval_df = spark.read.parquet("path/to/evaluation/data")

results = mlflow.genai.evaluate(
    data=eval_df,
    predict_fn=agent,
    scorers=[Safety(), RelevanceToQuery()],
)
```

^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

## Schema Requirements

The Spark DataFrame must comply with the [Evaluation Dataset Schema](/concepts/evaluation-dataset-schema.md) defined by MLflow GenAI. This ensures that the evaluation framework can correctly parse the input data, expectations, and metadata for each evaluation record. ^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

## When to Use This Pattern

The Spark DataFrame Evaluation Pattern is useful in the following scenarios:

- The evaluation data already exists in [Delta Lake](/concepts/delta-lake.md) or Unity Catalog
- You need to process large datasets that do not fit in driver memory
- You want to filter records from an [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md) before running evaluation
- You are integrating evaluation into an existing Spark-based data pipeline

^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

## Comparison with Other Data Patterns

The Spark DataFrame approach complements other evaluation data patterns:

- **[MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md)** (recommended for production): Provides versioning, lineage tracking, and Unity Catalog integration
- **List of dictionaries**: Suitable for quick prototyping with fewer than 100 examples
- **Pandas DataFrame**: Suitable for small datasets (fewer than 100 examples) and existing data science workflows

The Spark DataFrame pattern is distinct in that it is the only pattern designed for truly large-scale evaluation where data must be processed in a distributed fashion. ^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

## Related Concepts

- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The framework for evaluating GenAI applications
- [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md) — Versioned evaluation datasets with lineage tracking
- [Delta Lake](/concepts/delta-lake.md) — Storage format commonly used for evaluation data
- [Unity Catalog](/concepts/unity-catalog.md) — Catalog system for managing evaluation data
- [GenAI Scorers](/concepts/mlflow-genai-scorers.md) — Scoring functions used alongside evaluation data patterns
- Predict Function Patterns — Common patterns for `predict_fn` in evaluations

## Sources

- mlflow-evaluation-examples-for-genai-databricks-on-aws.md

# Citations

1. [mlflow-evaluation-examples-for-genai-databricks-on-aws.md](/references/mlflow-evaluation-examples-for-genai-databricks-on-aws-2da85b83.md)
