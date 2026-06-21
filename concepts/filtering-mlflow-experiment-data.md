---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 20cd8fc30e3889c80cd440d490c4776215c95048e2ef20f1051983292ccdcde3
  pageDirectory: concepts
  sources:
    - read-mlflow-experiments-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - filtering-mlflow-experiment-data
    - FMED
  citations:
    - file: read-mlflow-experiments-databricks-on-aws.md
title: Filtering MLflow experiment data
description: Using Spark DataFrame filter expressions on metrics and params columns (e.g., 'metrics.loss < 0.01') after loading experiment data via the mlflow-experiment data source.
tags:
  - databricks
  - mlflow
  - spark
  - filtering
timestamp: "2026-06-19T20:11:49.243Z"
---

# Filtering MLflow experiment data

**Filtering MLflow experiment data** refers to the process of loading training run results from an [MLflow Experiment](/concepts/mlflow-experiment.md) into an Apache Spark DataFrame and then applying filter expressions to select specific runs based on their recorded metrics, parameters, or tags. This technique enables users to analyze training run results, compare metrics across experiments, and build dashboards on top of experiment history. ^[read-mlflow-experiments-databricks-on-aws.md]

## Prerequisites

Reading and filtering MLflow experiment run data requires Databricks Runtime 6.0 ML and above. ^[read-mlflow-experiments-databricks-on-aws.md]

## Loading experiment data

Before filtering, you must load data from an MLflow experiment into a Spark DataFrame using the `mlflow-experiment` data source format. There are several ways to specify which experiment to load:

- **From the current notebook's experiment**: Call `load()` with no arguments.
- **By experiment ID**: Pass one or more experiment IDs as a comma-separated string to `load()`.
- **By experiment name**: Resolve the name to an ID using the MLflow client, then pass the ID to `load()`.

After loading, the `display()` function can be used to visualize the DataFrame. ^[read-mlflow-experiments-databricks-on-aws.md]

## Filtering with DataFrame expressions

Once experiment data is loaded into a Spark DataFrame, you can apply standard DataFrame filter expressions to query across metrics and parameters. Metrics are stored in a nested map column where values are doubles, and parameters are stored in a nested map column where values are strings. ^[read-mlflow-experiments-databricks-on-aws.md]

### Filtering on metrics

Since the `metrics` column is a map with string keys and double values, filters access individual metrics using dot notation. For example, to select only runs where the recorded loss is less than 0.01:

```python
df = spark.read.format("mlflow-experiment").load("3270527066281272")
filtered_df = df.filter("metrics.loss < 0.01")
```

^[read-mlflow-experiments-databricks-on-aws.md]

### Filtering on parameters

Parameters are stored as a map with string values, so comparisons must use string expressions. For example, to filter runs where the learning rate is greater than 0.001:

```python
filtered_df = df.filter("params.learning_rate > '0.001'")
```

^[read-mlflow-experiments-databricks-on-aws.md]

### Combining multiple conditions

You can combine filters on metrics and parameters in a single filter expression using logical operators. For example, to find runs with low loss and a specific learning rate:

```python
filtered_df = df.filter("metrics.loss < 0.01 AND params.learning_rate > '0.001'")
```

^[read-mlflow-experiments-databricks-on-aws.md]

## Output schema

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

This fixed schema means that the column structure is always the same regardless of which experiment is loaded — only the data within the map columns changes based on the metrics and parameters recorded for each experiment. ^[read-mlflow-experiments-databricks-on-aws.md]

## Additional filtering capabilities

Beyond metrics and parameters, you can also filter on other columns in the schema, such as:

- **`status`**: Filter by run status (e.g., `"FINISHED"`, `"FAILED"`, `"RUNNING"`).
- **`start_time`** and **`end_time`**: Filter by timestamp ranges.
- **`tags`**: Filter on experiment tags, which follow the same map structure as metrics and parameters.

## Related concepts

- [MLflow experiments](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs.
- [MLflow Tracking](/concepts/mlflow-tracking.md) — The broader system for logging and querying runs.
- Spark DataFrame API — The underlying API used for filtering.
- [Data Profiling](/concepts/data-profiling.md) — Another technique for analyzing dataset statistics.

## Sources

- read-mlflow-experiments-databricks-on-aws.md

# Citations

1. [read-mlflow-experiments-databricks-on-aws.md](/references/read-mlflow-experiments-databricks-on-aws-4b461305.md)
