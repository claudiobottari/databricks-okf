---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eb573f81ba6b765025fe2b415dfb778e8cbc6bb5ee433e93f4af8014629ae015
  pageDirectory: concepts
  sources:
    - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-run-selection-and-batch-operations
    - Batch Operations and MLflow Run Selection
    - MRSABO
  citations:
    - file: compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
title: MLflow Run Selection and Batch Operations
description: The ability to select multiple runs in the MLflow UI to perform batch operations such as deletion, comparison, or tag management.
tags:
  - mlflow
  - visualization
  - runs
timestamp: "2026-06-19T17:47:54.075Z"
---

# [MLflow Run](/concepts/mlflow-run.md) Selection and Batch Operations

**MLflow Run Selection and Batch Operations** refers to the functionality within the MLflow UI that allows users to manage, compare, and perform batch actions on multiple runs from an experiment. These features enable efficient analysis of model training experiments by selecting runs for visualization, filtering, sorting, grouping, and performing bulk operations like deletion and tagging.

## Selecting Runs for Display

The chart view page in MLflow displays a collection of charts comparing runs from an experiment. By default, charts on this page show the most recent 10 runs. Users can adjust which runs appear by clicking the **Show run icon** at the top of the runs list. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

Available display options include:
- Show the first 10 runs
- Show the first 20 runs  
- Show all runs

Runs that are shown on charts are indicated by a colored dot, while hidden runs appear with a grayed-out dot. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Batch Operations on Runs

To perform batch operations, select one or more runs by checking the box next to each run. When runs are selected, the **Delete**, **Compare**, and **Add tags** buttons become visible, enabling bulk actions. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

Available batch operations include:
- **Delete** - Remove selected runs from the experiment
- **Compare** - Open the Compare runs view for detailed analysis
- **Add/Edit tags** - Apply or modify tags on selected runs

## Filtering and Sorting Runs

Use the search field near the **Chart view** icon to filter runs based on parameter or metric values, or by tags. The sort order of runs shown in charts can be changed by selecting a parameter from the **Sort** dropdown menu. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Grouping Runs

To group runs by parameter value, select one or more parameters from the **Group by** dropdown menu. This allows for organized comparison of runs sharing common characteristics. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Creating Visualizations

Users can create new charts to visualize run data. The **Parallel coordinates chart** is particularly useful for understanding how parameter settings affect model performance, and for investigating relationships between parameters and metrics. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

### Parallel Coordinates Chart

To create a parallel coordinates plot:
1. Click **Add chart** and select **Parallel coordinates** from the dropdown menu
2. In the dialog, select the parameters and metrics to investigate
3. The resulting visualization highlights parameter combinations that produce high or low metric values

## Related Concepts

- Compare runs - Detailed view for comparing multiple runs
- [MLflow experiments](/concepts/mlflow-experiment.md) - Organizational unit for runs and evaluations
- [Chart view](/concepts/mlflow-chart-view.md) - Visualization page for run comparisons
- [MLflow tags](/concepts/mlflow-trace-tags.md) - Metadata annotations for runs

## Sources

- compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md

# Citations

1. [compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md](/references/compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws-ab27c56a.md)
