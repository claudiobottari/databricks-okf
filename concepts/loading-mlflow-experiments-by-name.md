---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b30d2cf8f4ca86e88b332df5226e0c20b20fa5cc2907ca5b1bdf744d56cd34a9
  pageDirectory: concepts
  sources:
    - read-mlflow-experiments-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - loading-mlflow-experiments-by-name
    - LMEBN
  citations:
    - file: read-mlflow-experiments-databricks-on-aws.md
title: Loading MLflow experiments by name
description: Resolving an MLflow experiment name to an ID using mlflow.get_experiment_by_name() and then passing that ID to the mlflow-experiment data source.
tags:
  - databricks
  - mlflow
  - spark
  - data-loading
timestamp: "2026-06-19T20:11:51.358Z"
---

#Loading MLflow experiments by name

The `mlflow-experiment` data source provides a Spark DataFrameReader API for loading MLflow experiment run data into a DataFrame. Users commonly use it to analyze training run results, compare metrics across experiments, and build dashboards on top of experiment history. ^[read-mlflow-experiments-databricks-on-aws.md]

## Prerequisites

Reading MLflow experiment run data requires Databricks Runtime 6.0 ML and above. ^[read-mlflow-experiments-databricks-on-aws.md]

## Usage: Loading by experiment name

To load data from a specific workspace experiment using its name (rather than its ID), first resolve the name to an experiment ID using the MLflow client. Then pass that ID to the `load()` method of the `mlflow-experiment` data source.

The following Python example loads data from the experiment named `/Shared/diabetes_experiment/`:

```python
expId = mlflow.get_experiment_by_name("/Shared/diabetes_experiment/").experiment_id
df = spark.read.format("mlflow-experiment").load(expId)
display(df)
```

^[read-mlflow-experiments-databricks-on-aws.md]

This approach is useful when you want to reference an experiment by a human‑readable path rather than a numeric ID. The same pattern works in Scala using the equivalent MLflow client method.

## Alternative loading methods

- **From the notebook experiment:** call `load()` with no arguments to load data from the current notebook’s attached experiment. ^[read-mlflow-experiments-databricks-on-aws.md]
- **Using experiment IDs:** pass one or more experiment IDs as a comma‑separated string to `load()`. ^[read-mlflow-experiments-databricks-on-aws.md]

After loading, you can filter the DataFrame using standard Spark filter expressions, for example:

```python
filtered_df = df.filter("metrics.loss < 0.01 AND params.learning_rate > '0.001'")
```

^[read-mlflow-experiments-databricks-on-aws.md]

## Output schema

The schema returned by the `mlflow-experiment` data source is fixed, regardless of the experiment loaded:

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

## Related concepts

- [MLflow experiments](/concepts/mlflow-experiment.md) – Organize training runs with MLflow experiments.
- Spark DataFrame API – Standard interface for reading and transforming data.
- [mlflow-experiment data source](/concepts/mlflow-experiment-data-source.md) – General documentation for the data source.
- Organize training runs with MLflow experiments – Detailed guide on experiment management.
- [OpenSharing shared tables](/concepts/opensharing-share.md) – Alternative method for reading experiment data shared via Delta Sharing.

## Sources

- read-mlflow-experiments-databricks-on-aws.md

# Citations

1. [read-mlflow-experiments-databricks-on-aws.md](/references/read-mlflow-experiments-databricks-on-aws-4b461305.md)
