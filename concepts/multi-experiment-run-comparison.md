---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3eb2453ad26f43985fa35c23f7a9f80b6304d095239f67923d02b7ec8e95a31d
  pageDirectory: concepts
  sources:
    - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-experiment-run-comparison
    - MRC
    - Experiment Comparison
  citations:
    - file: compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
title: Multi-Experiment Run Comparison
description: Ability to display and compare runs from multiple experiments in the MLflow Chart View, enabling cross-experiment analysis.
tags:
  - mlflow
  - experiment-tracking
  - comparison
timestamp: "2026-06-19T09:19:04.678Z"
---

# Multi-Experiment Run Comparison

**Multi-Experiment Run Comparison** refers to the ability to visualize and analyze [MLflow](/concepts/mlflow.md) runs that originate from different experiments side by side. This feature helps data scientists and ML engineers evaluate model performance across multiple experiment configurations, parameter sweeps, or team efforts within a single chart view.

## Overview

The MLflow UI provides a chart view that can include runs from one or more experiments. While the default chart view displays the most recent 10 runs of the current experiment, users can expand the selection to include runs from other experiments. The chart view supports numerous customization options, including filtering, sorting, grouping, and creating new chart types such as parallel coordinates plots. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

With [MLflow 3](/concepts/mlflow-3.md), these comparison features are also available for models from the **Models** tab. For more details, see [Track and compare models using MLflow Logged Models](/concepts/mlflow-loggedmodel.md). ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Accessing Multi-Experiment Comparison

To display runs from multiple experiments, use the **Compare runs from multiple experiments** link available on the experiment details page. This link opens a dedicated interface where you can select additional experiments and include their runs in the current chart view. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Chart View Capabilities

Once runs from multiple experiments are loaded, the chart view behaves identically to a single-experiment comparison view. You can:

- **Select runs to display**: Control which runs appear on the charts by clicking the show/hide icon next to each run. Runs shown are indicated by a colored dot; hidden runs are grayed out. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]
- **Manage runs**: Check boxes next to runs to delete, compare, or add or edit tags. When one or more runs are checked, buttons for **Delete**, **Compare**, and **Add tags** appear. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]
- **Filter runs**: Use the search field to filter runs based on parameter or metric values, or by tag. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]
- **Sort runs**: Change the sort order of runs shown in the charts using the **Sort** dropdown menu, selecting a parameter to sort by. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]
- **Group runs**: Group runs by one or more parameter values using the **Group by** dropdown menu. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]
- **Create new visualizations**: Add new charts (including parallel coordinates plots) by clicking **Add chart**. Charts can be moved, resized, edited, deleted, or downloaded via the chart's kebab menu. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

### Parallel Coordinates Chart

A [Parallel Coordinates Plot](/concepts/parallel-coordinates-plot.md) is especially useful for understanding the effect of parameter settings on model performance and investigating relationships between parameters and metrics. To create one, select **Parallel coordinates** from the **Add chart** menu and choose the parameters and metrics to examine. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Using System Tables for Comparison

MLflow metadata for experiments and runs is also available in system tables. You can leverage Databricks SQL and all the lakehouse tooling Databricks offers to visualize experiment data across multiple experiments. See the [MLflow system tables reference](/concepts/mlflow-system-tables.md) for further details. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md) – The organizational unit for runs.
- [View training results with MLflow runs](/concepts/filtering-and-sorting-mlflow-runs.md) – The runs list page.
- Compare runs – Comparing runs within a single experiment.
- [MLflow Logged Models](/concepts/mlflow-loggedmodel.md) – Model-level comparison in MLflow 3.
- [Parallel Coordinates Plot](/concepts/parallel-coordinates-plot.md) – A chart type for multi-parameter analysis.

## Sources

- compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md

# Citations

1. [compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md](/references/compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws-ab27c56a.md)
