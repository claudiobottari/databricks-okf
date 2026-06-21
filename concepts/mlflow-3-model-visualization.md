---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7250a52a097715fc70903d6d36419dccd9648c702d46ca1112d2aac083ccc444
  pageDirectory: concepts
  sources:
    - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3-model-visualization
    - M3MV
  citations:
    - file: compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
title: MLflow 3 Model Visualization
description: New capabilities in MLflow 3 that extend chart view features from experiment runs to models on the Models tab, allowing visual comparison of logged models.
tags:
  - mlflow
  - mlflow-3
  - models
  - visualization
timestamp: "2026-06-19T17:47:42.920Z"
---

---
title: MLflow 3 Model Visualization
summary: Extension of chart-view features to the Models tab in MLflow 3, enabling comparison of logged models using the same visualization tools previously available only for experiment runs.
sources:
  - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:03:12.845Z"
updatedAt: "2026-06-18T11:03:12.845Z"
tags:
  - mlflow
  - model-registry
  - visualization
aliases:
  - mlflow-3-model-visualization
  - M3MV
confidence: 1.0
provenanceState: extracted
inferredParagraphs: 0
---

# MLflow 3 Model Visualization

**MLflow 3 Model Visualization** refers to the set of graphical tools in the MLflow UI that let you compare and analyze [MLflow Logged Models](/concepts/mlflow-loggedmodel.md) using interactive charts. With MLflow 3, the chart view and comparison features that were originally available only for experiment runs have been extended to models on the **Models** tab. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Accessing the chart view for models

To display the chart view for models, navigate to the **Models** tab in the MLflow UI and click the **Chart view** icon. The page shows a collection of charts comparing the logged models of an experiment. You can customize this page by selecting which models to include, modifying existing charts, and creating new ones. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Selecting models to display

By default, charts show the most recent 10 models. To change the number of models displayed, use the **Show runs** control at the top of the list of models. You can choose to show the first 10, 20, or all models. Runs that are shown on the charts are indicated by a colored dot; hidden runs appear grayed out. As you roll your cursor over the lines on a chart, details for that model appear. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Managing models

Select one or more models by checking the box next to their name. When models are selected, buttons appear to **Delete**, **Compare**, or **Add tags** to the selected models. The comparison page shows side-by-side metrics, parameters, and tags for the selected models. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Filtering, sorting, and grouping

Use the search field to the right of the **Chart view** icon to filter models based on parameter values, metric values, or tags. To change the sort order of models shown in the charts, select a parameter from the **Sort** dropdown menu. To group models by parameter value, select one or more parameters from the **Group by** dropdown menu. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Creating new visualizations

Click **Add chart** and select a chart type from the dropdown menu to add a new visualization to the page. Available chart types include line charts, scatter plots, bar charts, and **parallel coordinates** plots. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

### Parallel coordinates chart

A parallel coordinates plot helps you understand the effect of parameter settings on model performance and investigate relationships between parameters and metrics. To create one, select **Parallel coordinates** from the menu, then choose the parameters and metrics to include in the dialog. The resulting chart highlights combinations of parameter values that produce high or low metric values. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Chart customization

You can move or resize any chart, or enlarge it to full screen. A kebab menu at the upper-right of each chart lets you edit, delete, or download the chart as an image. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Integration with system tables

MLflow metadata for experiments and runs is also available in [system tables](/concepts/mlflow-system-tables.md). You can query these tables using Databricks SQL and use the full lakehouse toolset to create custom visualizations of your experiment data. See the MLflow system tables reference for further details. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Related concepts

- [MLflow](/concepts/mlflow.md) – The open-source ML lifecycle platform
- [MLflow Runs](/concepts/mlflow-run.md) – Individual training executions within an experiment
- [MLflow Logged Models](/concepts/mlflow-loggedmodel.md) – Models registered from runs, now comparable via charts
- Databricks SQL – Query engine for exploring MLflow system tables
- System tables – Built-in tables for account-level metadata, including MLflow

## Sources

- compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md

# Citations

1. [compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md](/references/compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws-ab27c56a.md)
