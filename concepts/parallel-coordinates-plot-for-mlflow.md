---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8edc4df9b939894b0653e0ddd14f323bf45dc003d1bfc55dff57e61f645f8282
  pageDirectory: concepts
  sources:
    - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - parallel-coordinates-plot-for-mlflow
    - PCPFM
  citations:
    - file: compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
title: Parallel Coordinates Plot for MLflow
description: A parallel coordinates visualization in MLflow that helps understand relationships between parameter settings and model performance metrics.
tags:
  - mlflow
  - visualization
  - data-analysis
timestamp: "2026-06-18T14:40:10.652Z"
---

# Parallel Coordinates Plot for MLflow

A **Parallel Coordinates Plot** is a visualization available in the [MLflow](/concepts/mlflow.md) UI that helps you understand the effect of parameter settings on model performance and investigate relationships between parameters and metrics. It displays multiple dimensions (parameters and metrics) as parallel axes, with each run represented as a line connecting its values across those axes. By inspecting the lines, you can identify patterns, such as which parameter ranges tend to produce better metric values. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

This chart type is part of the **Chart view** page, which shows a collection of charts comparing the runs of an experiment. With [MLflow 3](/concepts/mlflow-3.md), these chart features are also available for models from the **Models** tab (see [Track and compare models using MLflow Logged Models](/concepts/mlflow-loggedmodel.md)). ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Creating a Parallel Coordinates Plot

To create a parallel coordinates plot in the MLflow UI:

1. Navigate to the **Chart view** on the experiment details page (or the **Models** tab in MLflow 3).
2. Click **Add chart** and select **Parallel coordinates** from the dropdown menu.
3. In the dialog, select the **parameters** and **metrics** you want to investigate. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

The resulting plot shows each parameter or metric as a vertical axis. Each run is drawn as a line that crosses each axis at the run’s corresponding value. The lines are color-coded by a selected metric, making it easy to spot which parameter combinations produce high or low metric values. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Example Interpretation

In the example from the documentation, the runs highlighted in black boxes suggest that lower values for `max_depth` result in higher values for the metric `auc`. Such insights help you narrow down promising hyperparameter regions for future experiments. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Related Concepts

- [MLflow experiments](/concepts/mlflow-experiment.md) — The container for runs that appear in parallel coordinates plots
- [MLflow runs](/concepts/mlflow-run.md) — Individual training executions that supply the data points
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) — The common use case for parallel coordinates analysis
- [Chart view](/concepts/mlflow-chart-view.md) — The dashboard where parallel coordinates and other charts are displayed
- Compare MLflow runs — Techniques for side-by-side run comparison
- [MLflow System Tables](/concepts/mlflow-system-tables.md) — Programmatic access to experiment metadata for custom visualization

## Sources

- compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md

# Citations

1. [compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md](/references/compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws-ab27c56a.md)
