---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ef4b51e71aed933a82d73006f8839f2819f3c5891d9260b4ba2fd666df3d29c8
  pageDirectory: concepts
  sources:
    - read-mlflow-experiments-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - notebook-experiment-in-databricks
    - NEID
    - Notebook Experiment
    - Notebook Experiments
    - Notebook experiment
    - notebook experiment
  citations:
    - file: read-mlflow-experiments-databricks-on-aws.md
title: Notebook experiment in Databricks
description: Each Databricks notebook has an associated MLflow experiment; its run data can be loaded by calling load() with no arguments on the mlflow-experiment data source.
tags:
  - databricks
  - mlflow
  - notebooks
timestamp: "2026-06-19T20:11:53.515Z"
---

# Notebook Experiment in Databricks

A **Notebook Experiment in Databricks** is the default MLflow experiment associated with a Databricks notebook. When you run code in a notebook that uses MLflow tracking, the run data is automatically logged to this experiment without requiring explicit experiment creation or specification.

## Overview

Every Databricks notebook is automatically linked to a corresponding MLflow experiment. This experiment is created implicitly when you first run MLflow tracking code within the notebook. The notebook experiment serves as the default destination for all logged metrics, parameters, tags, and artifacts generated during notebook execution. ^[read-mlflow-experiments-databricks-on-aws.md]

## Accessing the Notebook Experiment

The primary method for loading data from a notebook experiment is through the `mlflow-experiment` Spark DataFrameReader API. This API provides a convenient way to transform MLflow experiment run data into a DataFrame for analysis. ^[read-mlflow-experiments-databricks-on-aws.md]

### Loading Data with No Arguments

To load data from the current notebook's experiment, call `load()` with no arguments:

```python
df = spark.read.format("mlflow-experiment").load()
display(df)
```

This loads all run data from the experiment associated with the notebook currently being executed. ^[read-mlflow-experiments-databricks-on-aws.md]

## Use Cases

Notebook experiments are commonly used for:

- Analyzing training run results directly within the notebook
- Comparing metrics and parameters across multiple runs
- Building dashboards on top of experiment history
- Iterative experimentation during model development

## Output Schema

The `mlflow-experiment` data source returns a fixed schema regardless of the specific experiment loaded:

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

## Working with the Experiment Data

### Filtering by Metrics and Parameters

After loading experiment data, you can apply standard DataFrame filter expressions to query across metrics and parameters:

```python
df = spark.read.format("mlflow-experiment").load("3270527066281272")
filtered_df = df.filter("metrics.loss < 0.01 AND params.learning_rate > '0.001'")
display(filtered_df)
```

This filtering capability enables targeted analysis of specific model configurations or performance thresholds. ^[read-mlflow-experiments-databricks-on-aws.md]

## Prerequisites

Reading MLflow experiment run data using the `mlflow-experiment` data source requires Databricks Runtime 6.0 ML and above. ^[read-mlflow-experiments-databricks-on-aws.md]

## Related Concepts

- [MLflow experiments](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs and their metadata
- [MLflow Tracking](/concepts/mlflow-tracking.md) — The core API for logging parameters, metrics, and artifacts
- [Data Profiling in Databricks](/concepts/data-profiling-in-databricks.md) — Statistical analysis of datasets, which can be applied to experiment data
- [MLflow Run](/concepts/mlflow-run.md) — A single execution of model training code
- [Delta Sharing](/concepts/delta-sharing.md) — Alternative data sharing mechanism for accessing experiment data across workspaces

## Sources

- read-mlflow-experiments-databricks-on-aws.md

# Citations

1. [read-mlflow-experiments-databricks-on-aws.md](/references/read-mlflow-experiments-databricks-on-aws-4b461305.md)
