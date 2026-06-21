---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cbeef613096aa759d351b1def946dd1d331dfcbb583f85eb0b10cab0c4bdd7d3
  pageDirectory: concepts
  sources:
    - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-models-tab-visualizations
    - MMTV
    - mlflow-3-models-tab-visualization
    - M3MTV
  citations:
    - file: compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
title: MLflow Models Tab Visualizations
description: Chart view features available for comparing models from the Models tab in MLflow 3, extending the same visualization tools used for experiment runs.
tags:
  - mlflow
  - model-registry
  - visualization
timestamp: "2026-06-19T14:20:02.691Z"
---

# MLflow Models Tab Visualizations

**MLflow Models Tab Visualizations** provide a comprehensive set of charting and graphing tools for comparing and analyzing logged models within the MLflow UI. With MLflow 3, these visualization features are available from the **Models** tab, enabling users to examine model performance, track experiments, and derive insights from logged model metadata.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Overview

The chart view page in the '''Models''' tab displays a collection of charts comparing the runs of an experiment. You can customize this page by selecting runs to include, modifying existing charts, and creating new charts. MLflow metadata for experiments and runs is also available in [MLflow System Tables](/concepts/mlflow-system-tables.md), where you can leverage Databricks SQL and the lakehouse tooling offered by Databricks to visualize your experiment data.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

To display the chart view page, click the '''Chart view''' icon on the [MLflow Experiment](/concepts/mlflow-experiment.md) details page.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

For information about the runs list page, see View Training Results with MLflow Runs. To display runs from multiple experiments, see [Compare Runs from Multiple Experiments](/concepts/comparing-runs-from-multiple-experiments.md).^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Chart Overview

By default, charts on this page show the most recent 10 runs. As you roll your cursor over the lines on a chart, details for that run appear. You can move or resize a chart, or enlarge it to full screen. A kebab menu at the upper-right of the chart lets you edit, delete, or download the chart.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Select Runs to Display

To select the number of runs to display, click the run icon at the top of the list of runs. Runs that are shown on the charts are indicated by a colored dot, while runs not shown are indicated by a grayed-out dot.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Manage Runs

To delete, compare, or add or remove tags from a run, check the box next to the left of the run(s). When one or more runs is checked, the '''Delete''', '''Compare''', and '''Add tags''' buttons appear. For details about the comparing runs page, see Compare Runs.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Filter Runs

Use the search field to the right of the '''Chart view''' icon to filter runs based on parameter or metric values, or by tag. For details, see Filter Runs.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Sort Runs

To change the sort order of runs shown in the charts, select the parameter to sort by from the '''Sort''' dropdown menu.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Group Runs

To group runs by parameter value, select one or more parameters from the '''Group by''' dropdown menu.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Create New Visualizations

To add a chart, click '''Add chart''' and select the type of chart to add from the dropdown menu.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

### Parallel Coordinates Chart

A '''parallel coordinates plot''' is useful in understanding the effect of parameter settings on model performance and investigating relationships between Parameters and Metrics. To create a parallel coordinates plot, select '''Parallel coordinates''' from the menu. In the dialog, select the parameters and metrics to investigate. In this visualization, runs highlighted in black boxes suggest that lower values for a certain parameter result in higher values for a given metric.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Related Concepts

- [Track and Compare Models Using MLflow Logged Models](/concepts/mlflow-loggedmodel.md)
- [MLflow System Tables Reference](/concepts/mlflow-system-tables.md)
- [Comparing Runs from Multiple Experiments](/concepts/comparing-runs-from-multiple-experiments.md)
- Filter Runs
- [Chart View](/concepts/mlflow-chart-view.md)
- [Parallel Coordinates Plot](/concepts/parallel-coordinates-plot.md)

## Sources

- compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md

# Citations

1. [compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md](/references/compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws-ab27c56a.md)
