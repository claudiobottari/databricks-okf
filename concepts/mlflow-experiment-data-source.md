---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7a36125eb744d10309fdf4bd285d195793ff74062228575f83af9907aa53f5d2
  pageDirectory: concepts
  sources:
    - read-mlflow-experiments-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-experiment-data-source
    - MDS
  citations:
    - file: read-mlflow-experiments-databricks-on-aws.md
title: mlflow-experiment data source
description: A Spark DataFrameReader API on Databricks that loads MLflow experiment run data into a DataFrame for analysis, comparison, and dashboarding.
tags:
  - databricks
  - mlflow
  - spark
  - data-loading
timestamp: "2026-06-19T20:11:36.979Z"
---

# mlflow-experiment Data Source

The **`mlflow-experiment` data source** is a Spark DataFrameReader API provided by Databricks for loading [MLflow](/concepts/mlflow.md) experiment run data directly into a Spark DataFrame. It enables users to analyze training run results, compare metrics across experiments, and build dashboards on top of experiment history using standard Spark DataFrame operations. ^[read-mlflow-experiments-databricks-on-aws.md]

## Prerequisites

Reading MLflow experiment run data requires Databricks Runtime 6.0 ML and above. ^[read-mlflow-experiments-databricks-on-aws.md]

## Usage

The `mlflow-experiment` data source supports several loading patterns through the Spark DataFrame API.

### Load data from the notebook experiment

To load data from the current notebook's experiment, call `load()` with no arguments:

```python
df = spark.read.format("mlflow-experiment").load()
display(df)
```

^[read-mlflow-experiments-databricks-on-aws.md]

### Load data using experiment IDs

To load data from one or more workspace experiments, pass the experiment IDs as a comma-separated string to `load()`:

```python
df = spark.read.format("mlflow-experiment").load("3270527066281272")
display(df)
```

^[read-mlflow-experiments-databricks-on-aws.md]

### Load data using an experiment name

To load data by experiment name, resolve the name to an ID using the MLflow client, then pass the ID to `load()`:

```python
expId = mlflow.get_experiment_by_name("/Shared/diabetes_experiment/").experiment_id
df = spark.read.format("mlflow-experiment").load(expId)
display(df)
```

^[read-mlflow-experiments-databricks-on-aws.md]

### Filter data based on metrics and parameters

After loading experiment data, use standard DataFrame filter expressions to query across metrics and parameters:

```python
df = spark.read.format("mlflow-experiment").load("3270527066281272")
filtered_df = df.filter("metrics.loss < 0.01 AND params.learning_rate > '0.001'")
display(filtered_df)
```

^[read-mlflow-experiments-databricks-on-aws.md]

## Output Schema

The schema returned by the `mlflow-experiment` data source is fixed regardless of the experiment loaded:

```
root
|-- run_id: string
|-- experiment_id: string
|-- metrics: map
|    |-- key: string
|    |-- value: double
|-- params: map
|    |-- key: string
|    |-- value: string
|-- tags: map
|    |-- key: string
|    |-- value: string
|-- start_time: timestamp
|-- end_time: timestamp
|-- status: string
|-- artifact_uri: string
```

^[read-mlflow-experiments-databricks-on-aws.md]

The schema includes:
- **`run_id`**: Unique identifier for each [MLflow Run](/concepts/mlflow-run.md).
- **`experiment_id`**: Identifier of the parent experiment.
- **`metrics`**: A map of metric names to double values, enabling numerical comparisons across runs.
- **`params`**: A map of parameter names to string values, allowing filtering on hyperparameters.
- **`tags`**: A map of tag keys to string values for metadata filtering.
- **`start_time`** and **`end_time`**: Timestamps indicating when the run started and ended.
- **`status`**: The run status (e.g., FINISHED, FAILED, RUNNING).
- **`artifact_uri`**: URI pointing to the run's artifacts storage location.

## Related Concepts

- [MLflow experiments](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs that this data source reads from.
- [MLflow runs](/concepts/mlflow-run.md) — Individual training executions whose data is exposed through this data source.
- DataFrameReader API — The Spark API used to load data from various formats.
- [Delta Sharing](/concepts/delta-sharing.md) — An alternative data sharing format for reading shared tables with the same DataFrameReader API.

## Sources

- read-mlflow-experiments-databricks-on-aws.md

# Citations

1. [read-mlflow-experiments-databricks-on-aws.md](/references/read-mlflow-experiments-databricks-on-aws-4b461305.md)
