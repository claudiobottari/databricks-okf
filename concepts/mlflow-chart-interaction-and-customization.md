---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ff6e62eba5ca28522a13116717a9c8174676373a98bb292807a3f85b9ebceb3a
  pageDirectory: concepts
  sources:
    - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-chart-interaction-and-customization
    - Customization and MLflow Chart Interaction
    - MCIAC
  citations:
    - file: compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
title: MLflow Chart Interaction and Customization
description: Interactive features of MLflow charts including hover details, move/resize/fullscreen controls, and edit/delete/download options via a kebab menu.
tags:
  - mlflow
  - visualization
  - ui
timestamp: "2026-06-19T17:47:52.138Z"
---

## MLflow Chart Interaction and Customization

MLflow provides a chart view page that displays a collection of charts comparing the runs of an experiment. Users can customize this page by selecting which runs to include, modifying existing charts, and creating new visualizations. With MLflow 3, these chart features are also available for models from the **Models** tab. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

### Accessing the Chart View

To open the chart view, click the **Chart view** icon on the experiment details page. The runs list page is the alternative for viewing training results; for details see [MLflow runs](/concepts/mlflow-run.md). To compare runs from multiple experiments, refer to the [compare runs from multiple experiments](https://docs.databricks.com/aws/en/mlflow/runs#compare-runs-from-multiple-expts) documentation. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

### Chart Interaction

By default, charts display the most recent 10 runs. Rolling the cursor over a chart line shows details for that run. Users can move or resize a chart, or enlarge it to full screen. A kebab menu (upper-right of each chart) provides options to edit, delete, or download the chart. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

### Selecting Runs

To control which runs appear on the charts, click the show‑run icon at the top of the runs list. The menu lets you show the first 10, first 20, or all runs. Runs that are displayed are indicated by a colored dot; hidden runs have a grayed‑out dot. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

### Managing Runs

Select one or more runs by checking the box to the left of each run. When at least one run is selected, the **Delete**, **Compare**, and **Add tags** buttons become available. See the compare runs documentation for more details about the comparing‑runs page. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

### Filtering and Sorting Runs

Use the search field to the right of the **Chart view** icon to filter runs based on parameter values, metric values, or tags. The **Sort** dropdown menu changes the sort order of runs displayed in the charts; select the parameter by which to sort. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

### Grouping Runs

To group runs by a parameter value, select one or more parameters from the **Group by** dropdown menu. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

### Creating New Visualizations

Click **Add chart** and choose a chart type from the dropdown menu. Available types include the **parallel coordinates chart**, which helps explore relationships between parameters and metrics, and to understand how parameter settings affect model performance. In the parallel coordinates dialog, select the parameters and metrics to investigate; highlighted lines in the plot show runs that fall into a selected range, aiding in hyperparameter analysis. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

### Alternative: Using System Tables

Beyond the UI, MLflow metadata for experiments and runs is also available in [system tables](/concepts/mlflow-system-tables.md). You can leverage Databricks SQL and the full lakehouse tooling to visualize experiment data. See the [MLflow system tables reference](https://docs.databricks.com/aws/en/admin/system-tables/mlflow) for details. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Related Concepts

- [MLflow experiments](/concepts/mlflow-experiment.md)
- [MLflow runs](/concepts/mlflow-run.md)
- Compare runs
- System tables
- Databricks SQL

## Sources

- compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md

# Citations

1. [compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md](/references/compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws-ab27c56a.md)
