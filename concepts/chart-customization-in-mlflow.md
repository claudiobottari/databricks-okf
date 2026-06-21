---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cbcfbd59c4ac98197bf95a8fc21918f6d1439d4fd93b9f8405c14ef5975e4c8f
  pageDirectory: concepts
  sources:
    - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - chart-customization-in-mlflow
    - CCIM
  citations:
    - file: compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
title: Chart Customization in MLflow
description: Ability to add, move, resize, edit, delete, and download charts in the MLflow Chart View, including full-screen mode and kebab menu controls.
tags:
  - mlflow
  - visualization
  - user-interface
timestamp: "2026-06-19T09:18:42.977Z"
---

# Chart Customization in MLflow

**Chart Customization in MLflow** refers to the ability to configure and create visualizations for comparing runs and models in the MLflow UI. The chart view page provides a collection of charts that can be tailored by selecting which runs to display, editing existing charts, and adding new chart types. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

With [MLflow 3](/concepts/mlflow-3.md), these chart customization features are also available for models from the **Models** tab, enabling side-by-side comparison of logged models. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Chart overview

By default, charts show the most recent 10 runs. Hovering over a line displays details for that run. Charts can be moved, resized, or enlarged to full screen. A kebab menu in the upper-right corner allows editing, deleting, or downloading a chart. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

![Chart controls including move, resize, and kebab menu.](https://docs.databricks.com/aws/en/assets/images/chart-controls-c801d1423fad98b81eec9e2250438b9e.png)

## Selecting runs to display

To choose which runs appear on the charts, use the show/hide icon above the run list. The dropdown lets you show the first 10, 20, or all runs. Runs that are shown are indicated by a colored dot; hidden runs are shown with a grayed-out dot. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Managing runs

Select the checkbox next to one or more runs to reveal actions: **Delete**, **Compare**, and **Add tags**. The **Compare** button opens the dedicated run comparison page. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Filtering runs

Use the search field to filter runs based on parameter or metric values, or by tag. This narrows the set of runs shown in the charts. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Sorting runs

Select a parameter from the **Sort** dropdown menu to change the order in which runs are displayed. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Grouping runs

To group runs by a parameter value, choose one or more parameters from the **Group by** dropdown menu. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Creating new visualizations

Click **Add chart** and select a chart type from the dropdown. The page supports standard chart types as well as a parallel coordinates chart. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

### Parallel coordinates chart

A [Parallel Coordinates Plot](/concepts/parallel-coordinates-plot.md) helps understand the effect of parameter settings on model performance and investigate relationships between parameters and metrics. To create one, select **Parallel coordinates** from the menu and choose the parameters and metrics to investigate. The visualization highlights runs that share certain parameter ranges, making it easy to spot patterns—for example, that lower values of `max_depth` result in higher values of `auc`. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

![Example parallel coordinates plot.](https://docs.databricks.com/aws/en/assets/images/parallel-coord-plot-f39e2027c85d0bfbce0c6c44b79d9e49.png)

## Alternative visualization using system tables

MLflow metadata for experiments and runs is also available in [MLflow System Tables](/concepts/mlflow-system-tables.md), where you can use Databricks SQL and all the lakehouse tooling to create custom visualizations of experiment data. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Related concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md)
- [MLflow Runs](/concepts/mlflow-run.md)
- [MLflow Logged Models](/concepts/mlflow-loggedmodel.md)
- [Parallel Coordinates Chart](/concepts/parallel-coordinates-chart-in-mlflow.md)
- Databricks SQL

## Sources

- compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md

# Citations

1. [compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md](/references/compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws-ab27c56a.md)
