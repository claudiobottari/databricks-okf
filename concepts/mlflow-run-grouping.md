---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3dbcef877d7af130b97b5f55965e5eacd165eb2127adb397faf26a872234d439
  pageDirectory: concepts
  sources:
    - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-run-grouping
    - MRG
  citations:
    - file: compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
title: MLflow Run Grouping
description: Grouping MLflow runs by one or more parameter values using the Group by dropdown to organize chart displays.
tags:
  - mlflow
  - experiment-tracking
  - visualization
timestamp: "2026-06-19T14:19:05.997Z"
---

# [MLflow Run](/concepts/mlflow-run.md) Grouping

**MLflow Run Grouping** is a feature in the MLflow UI that allows users to organize runs within an experiment by one or more parameter values. This grouping capability simplifies the comparison of runs that share similar configuration settings, making it easier to analyze the effect of parameters on model performance. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Usage

Grouping runs is performed from the **Chart view** of an experiment’s detail page. To group runs:

1. Open an MLflow experiment in the UI.
2. Click the **Chart view** icon to display the chart collection.
3. Locate the **Group by** dropdown menu above the chart area.
4. Select one or more parameters to group the runs by their parameter values.

Runs with the same value for the chosen parameter(s) are visually grouped together in the charts, making patterns and outliers more apparent. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Use Cases

Grouping is particularly useful when experimenting with hyperparameters — for example, comparing runs that differ only in learning rate while keeping other parameters constant. By grouping runs by those constant parameters, you can isolate the effect of a single variable. It also helps in investigating relationships between parameters and metrics when combined with other visualizations like [parallel coordinates plots](/concepts/parallel-coordinates-plot.md).

## Related Concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md) – The organizational container for runs.
- [MLflow Runs](/concepts/mlflow-run.md) – Individual executions of a machine learning task.
- [MLflow Chart View](/concepts/mlflow-chart-view.md) – The visualization interface where grouping is available.
- [Filtering MLflow Runs](/concepts/filtering-and-sorting-mlflow-runs.md) – Another way to narrow down the set of runs displayed.
- [Parallel Coordinates Chart](/concepts/parallel-coordinates-chart-in-mlflow.md) – A complementary visualization for multi-parameter analysis.

## Sources

- compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md

# Citations

1. [compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md](/references/compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws-ab27c56a.md)
