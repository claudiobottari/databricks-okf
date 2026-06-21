---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea74e25ef2f8406140bbaa2f44b176084fb1ee319677f1efa59b198645af9bd0
  pageDirectory: concepts
  sources:
    - read-mlflow-experiments-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - loading-mlflow-experiments-by-id
    - LMEBI
  citations:
    - file: read-mlflow-experiments-databricks-on-aws.md
    - file: inferred from the single‑example syntax; the source says “one or more”
title: Loading MLflow experiments by ID
description: Loading MLflow experiment run data into a Spark DataFrame by passing one or more experiment IDs as a comma-separated string to the mlflow-experiment data source.
tags:
  - databricks
  - mlflow
  - spark
  - data-loading
timestamp: "2026-06-19T20:11:46.979Z"
---

# Loading MLflow Experiments by ID

**Loading MLflow experiments by ID** refers to using the `mlflow-experiment` data source in Apache Spark to read run data from one or more [MLflow experiments](/concepts/mlflow-experiment.md) specified by their unique workspace experiment IDs. This approach is commonly used for analyzing training run results, comparing metrics across experiments, and building dashboards on top of experiment history. ^[read-mlflow-experiments-databricks-on-aws.md]

## Prerequisites

Reading MLflow experiment run data requires Databricks Runtime 6.0 ML and above. ^[read-mlflow-experiments-databricks-on-aws.md]

## Usage

To load data from one or more workspace experiments, pass the experiment IDs as a comma‑separated string to the `load()` method. ^[read-mlflow-experiments-databricks-on-aws.md]

### Python

```python
df = spark.read.format("mlflow-experiment").load("3270527066281272")
display(df)
```

### Scala

```scala
val df = spark.read.format("mlflow-experiment").load("3270527066281272")
display(df)
```

### Loading multiple experiments by ID

A comma‑separated string of multiple experiment IDs can be supplied to `load()`; the resulting DataFrame will contain run data from all specified experiments. ^[inferred from the single‑example syntax; the source says “one or more”]

### Alternatives for loading by ID

- **Notebook experiment**: Calling `load()` with no arguments loads data from the current notebook’s experiment. ^[read-mlflow-experiments-databricks-on-aws.md]
- **Experiment name**: Resolve the name to an ID using the MLflow client, then pass the ID to `load()`:
  ```python
  expId = mlflow.get_experiment_by_name("/Shared/diabetes_experiment/").experiment_id
  df = spark.read.format("mlflow-experiment").load(expId)
  ```
  ^[read-mlflow-experiments-databricks-on-aws.md]

### Filtering after loading

After loading experiment data, you can apply standard DataFrame filter expressions on metrics and parameters. For example:

```python
df = spark.read.format("mlflow-experiment").load("3270527066281272")
filtered_df = df.filter("metrics.loss < 0.01 AND params.learning_rate > '0.001'")
display(filtered_df)
```

^[read-mlflow-experiments-databricks-on-aws.md]

## Output Schema

The `mlflow-experiment` data source returns a fixed schema, independent of the experiment loaded: ^[read-mlflow-experiments-databricks-on-aws.md]

```text
root
|-- run_id: string
|-- experiment_id: string
|-- metrics: map
|   |-- key: string
|   |-- value: double
|-- params: map
|   |-- key: string
|   |-- value: string
|-- tags: map
|   |-- key: string
|   |-- value: string
|-- start_time: timestamp
|-- end_time: timestamp
|-- status: string
|-- artifact_uri: string
```

The fields include:
- `run_id` – unique identifier for the [MLflow Run](/concepts/mlflow-run.md).
- `experiment_id` – the experiment the run belongs to.
- `metrics` – map of metric names to double values (e.g., `loss`, `accuracy`).
- `params` – map of parameter names to string values (e.g., `learning_rate`, `batch_size`).
- `tags` – map of tag keys to values.
- `start_time` / `end_time` – timestamps of the run.
- `status` – run status (e.g., `FINISHED`, `FAILED`).
- `artifact_uri` – URI of the run’s artifact location.

## Related Concepts

- Read MLflow experiments – Overview of reading experiment data.
- Organize training runs with MLflow experiments – Managing experiments.
- Read OpenSharing shared tables using Spark DataFrames – Alternative for Delta Sharing data.
- Spark DataFrame API – General data loading and transformation.

## Sources

- read-mlflow-experiments-databricks-on-aws.md

# Citations

1. [read-mlflow-experiments-databricks-on-aws.md](/references/read-mlflow-experiments-databricks-on-aws-4b461305.md)
2. inferred from the single‑example syntax; the source says “one or more”
