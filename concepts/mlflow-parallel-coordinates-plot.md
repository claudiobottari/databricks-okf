---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 75a4bf39a028bd8ac10a14420c412b6224908c0a9763f9a3c62aca390284ecf8
  pageDirectory: concepts
  sources:
    - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-parallel-coordinates-plot
    - MPCP
  citations:
    - file: compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
title: MLflow Parallel Coordinates Plot
description: A chart type in MLflow that visualizes relationships between multiple parameters and metrics across runs, helping identify parameter settings that influence model performance.
tags:
  - mlflow
  - visualization
  - hyperparameter-tuning
timestamp: "2026-06-18T11:02:58.589Z"
---

# MLflow Parallel Coordinates Plot

The **parallel coordinates plot** is a visualization available in the MLflow UI that helps investigate the effect of parameter settings on model performance and explore relationships between parameters and metrics. It is part of the **Chart view** page, which can display runs from an experiment or, with [MLflow 3](/concepts/mlflow-3.md), logged models from the **Models** tab. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Creating a parallel coordinates plot

To add a parallel coordinates plot in the MLflow Chart view:

1. Click **Add chart**.
2. From the dropdown menu, select **Parallel coordinates**.
3. In the dialog, select the parameters and metrics you want to investigate.

The plot then renders with each selected parameter and metric as a vertical axis, and each run (or model) represented as a line crossing those axes at the values recorded for that run.

^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Interpreting the plot

In a parallel coordinates plot, runs that share similar parameter settings or metric outcomes form visible clusters of lines. For example, the runs highlighted in the black boxes in the example plot suggest that lower values for `max_depth` result in higher values for the metric `auc`. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

![Example parallel coordinates plot showing the relationship between max_depth and auc.](https://docs.databricks.com/aws/en/assets/images/parallel-coord-plot-f39e2027c85d0bfbce0c6c44b79d9e49.png)

## Related concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md) — the container for runs that can be compared in charts
- [MLflow Runs](/concepts/mlflow-run.md) — individual training executions that appear as lines in the plot
- Compare MLflow Runs — the general workflow for side-by-side run comparison
- [MLflow UI](/concepts/mlflow.md) — the web interface providing the Chart view and all its visualizations
- [Parallel coordinates](/concepts/parallel-coordinates-plot.md) — a general statistical visualization technique for multi-dimensional data

## Sources

- compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md

# Citations

1. [compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md](/references/compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws-ab27c56a.md)
