---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a9b65d8f03d457648a9cbfd4ae9bb051778a9f4f1d3a917dc532d4c027c4f592
  pageDirectory: concepts
  sources:
    - read-mlflow-experiments-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-experiment-output-schema
    - MEOS
  citations:
    - file: read-mlflow-experiments-databricks-on-aws.md
title: MLflow experiment output schema
description: The fixed schema returned by the mlflow-experiment data source, including run_id, experiment_id, metrics (map), params (map), tags (map), start_time, end_time, status, and artifact_uri.
tags:
  - databricks
  - mlflow
  - schema
timestamp: "2026-06-19T20:11:38.446Z"
---

# MLflow Experiment Output Schema

The **MLflow experiment output schema** is the fixed set of columns that the `mlflow-experiment` Spark DataFrameReader returns when loading run data from an [MLflow Experiment](/concepts/mlflow-experiment.md). This schema is consistent regardless of which experiment is queried, enabling users to write generic analysis and dashboarding code against experiment history. ^[read-mlflow-experiments-databricks-on-aws.md]

## Schema Definition

The schema returned by `df = spark.read.format("mlflow-experiment").load(...)` contains the following columns:

| Column name       | Type                | Description |
|-------------------|---------------------|-------------|
| `run_id`          | `string`            | Unique identifier for the [MLflow Run](/concepts/mlflow-run.md) |
| `experiment_id`   | `string`            | Identifier of the experiment that contains the run |
| `metrics`         | `map<string, double>` | Mapping of metric names to their numeric values |
| `params`          | `map<string, string>` | Mapping of parameter names to their string values |
| `tags`            | `map<string, string>` | Mapping of tag names to their string values |
| `start_time`      | `timestamp`         | When the run started |
| `end_time`        | `timestamp`         | When the run ended |
| `status`          | `string`            | Run status (e.g., "FINISHED", "FAILED", "RUNNING") |
| `artifact_uri`    | `string`            | URI location of the run's artifacts |

All fields are of type string or map, except `start_time` and `end_time`, which are timestamps, and the values in the `metrics` map, which are doubles. ^[read-mlflow-experiments-databricks-on-aws.md]

## Usage Context

Users can load experiment data with no arguments (to read the current notebook’s experiment), by a comma‑separated list of experiment IDs, or by resolving an experiment name via the MLflow client. After loading, standard DataFrame filter expressions work on the nested columns — for example, `df.filter("metrics.loss < 0.01 AND params.learning_rate > '0.001'")` — enabling flexible querying across runs. ^[read-mlflow-experiments-databricks-on-aws.md]

## Related Concepts

- [MLflow experiments](/concepts/mlflow-experiment.md) – The organizational container for training runs.
- [Spark DataFrame](/concepts/spark-dataframe-evaluation-pattern.md) – The object into which the experiment data is loaded.
- [mlflow-experiment data source](/concepts/mlflow-experiment-data-source.md) – The DataFrameReader format name.
- Organize training runs with MLflow experiments – Official documentation for experiment usage.

## Sources

- read-mlflow-experiments-databricks-on-aws.md

# Citations

1. [read-mlflow-experiments-databricks-on-aws.md](/references/read-mlflow-experiments-databricks-on-aws-4b461305.md)
