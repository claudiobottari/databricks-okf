---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1a8da5092c0165772f652bb58399f2720864bdcef55cc7a954842aebb5869e5c
  pageDirectory: concepts
  sources:
    - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-run-management-actions
    - MRMA
  citations:
    - file: compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
title: MLflow Run Management Actions
description: Operations for managing MLflow runs including deletion, comparison, and tag management through a checkbox-based selection interface in the chart view.
tags:
  - mlflow
  - experiment-tracking
  - workflow
timestamp: "2026-06-18T11:02:58.572Z"
---

# [MLflow Run](/concepts/mlflow-run.md) Management Actions

**MLflow Run Management Actions** are the operations available in the MLflow UI for organizing, filtering, comparing, and visualizing experiment runs. These actions allow data scientists and ML engineers to manage the lifecycle of training runs, identify optimal model configurations, and investigate relationships between parameters and metrics.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Selecting Runs to Display

By default, charts on the chart view page show the most recent 10 runs. To select the number of runs to display, click the show-run icon at the top of the list of runs. You can choose to show the first 10, 20, or all runs.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

Runs that are shown on the charts are indicated by a colored dot, while runs not shown are indicated by a grayed-out dot.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Managing Runs

To delete, compare, or add or remove tags from a run, check the box next to the left of the run(s). When one or more runs is checked, the **Delete**, **Compare**, and **Add tags** buttons appear.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

For details about the comparing runs page, see Compare MLflow Runs.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Filtering Runs

Use the search field to the right of the **Chart view** icon to filter runs based on parameter or metric values or by tag. For details, see Filter MLflow Runs.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Sorting Runs

To change the sort order of runs shown in the charts, select the parameter to sort by from the **Sort** dropdown menu.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Grouping Runs

To group runs by parameter value, select one or more parameters from the **Group by** dropdown menu.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Creating Visualizations

To add a chart, click **Add chart**, and select the type of chart to add from the dropdown menu.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

### Parallel Coordinates Chart

A parallel coordinates plot is useful in understanding the effect of parameter settings on model performance and investigating relationships between parameters and metrics. To create a parallel coordinates plot, select **Parallel coordinates** from the menu. In the dialog, select the parameters and metrics to investigate.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Chart Interaction and Customization

As you roll your cursor over the lines on a chart, details for that run appear. You can move or resize a chart, or enlarge it to full screen. A kebab menu at the upper-right of the chart lets you edit, delete, or download the chart.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Displaying Runs from Multiple Experiments

To display runs from multiple experiments, see [Compare Runs from Multiple Experiments](/concepts/comparing-runs-from-multiple-experiments.md).^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## MLflow Metadata in System Tables

MLflow metadata for experiments and runs is also available in system tables, where you can leverage Databricks SQL and all the lakehouse tooling Databricks offers to visualize your experiment data. See [MLflow System Tables Reference](/concepts/mlflow-system-tables.md) for further details.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for grouping related runs
- [MLflow Runs](/concepts/mlflow-run.md) — Individual training executions tracked by MLflow
- [MLflow Logged Models](/concepts/mlflow-loggedmodel.md) — Models tracked and compared using MLflow
- [MLflow UI](/concepts/mlflow.md) — The web interface for viewing and managing experiments
- Compare MLflow Runs — Detailed comparison of selected runs
- View Training Results with MLflow Runs — The runs list page overview

## Sources

- compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md

# Citations

1. [compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md](/references/compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws-ab27c56a.md)
