---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7a28db443ef66f42eeec4b6ed9a310aa910386944f661f600aeca894174f12ee
  pageDirectory: concepts
  sources:
    - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-system-tables-for-visualization
    - MSTFV
  citations:
    - file: compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
title: MLflow System Tables for Visualization
description: Databricks system tables that expose MLflow metadata for experiments and runs, enabling custom visualizations using Databricks SQL and lakehouse tooling.
tags:
  - mlflow
  - databricks
  - visualization
  - system-tables
timestamp: "2026-06-19T17:47:34.192Z"
---

# MLflow System Tables for Visualization

**MLflow System Tables for Visualization** refers to the metadata tables in Databricks that store experiment and run data from MLflow. These system tables can be queried using Databricks SQL and visualized using the full suite of lakehouse tooling that Databricks offers, providing an alternative to the built-in chart views in the MLflow UI for comparing runs and models.

## Overview

MLflow metadata for experiments and runs is available in system tables, where you can leverage Databricks SQL and all the lakehouse tooling Databricks offers to visualize experiment data. This enables more flexible and powerful analysis of ML experiment results compared to the default MLflow UI visualizations. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Accessing MLflow System Tables

For specific details on the table schemas and available fields, see the [MLflow system tables reference](/concepts/mlflow-system-tables.md) in the Databricks documentation. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## MLflow UI Chart View (for Comparison)

The MLflow UI provides a chart view page that shows a collection of charts comparing runs of an experiment. With [MLflow 3](/concepts/mlflow-3.md), these features are also available for models from the **Models** tab. Users can customize this page by: ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

- Selecting runs to include or exclude from display
- Modifying existing charts
- Creating new chart types, including parallel coordinates plots
- Filtering runs based on parameter or metric values
- Sorting runs by parameters
- Grouping runs by parameter values

### Chart Types Available in the MLflow UI

The MLflow chart view supports several visualization types: ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

- Standard line charts showing metric values across runs
- Parallel coordinates plots for understanding the effect of parameter settings on model performance and investigating relationships between parameters and metrics
- Scatter plots and other chart types available through the **Add chart** menu

## Advantages of Using System Tables

While the MLflow UI provides convenient built-in visualization capabilities, using system tables offers additional flexibility not available in the default UI:

- Query experiment data directly using Databricks SQL
- Combine MLflow data with other data sources in the lakehouse
- Create custom dashboards and reports
- Perform complex aggregations and analyses
- Integrate with external visualization tools

## Use Cases

- Advanced analytics on experiment results beyond UI support
- Custom dashboards for monitoring model training pipelines
- Cross-experiment analysis across multiple experiments
- Historical tracking of trends over time
- Integration with other operational data for comprehensive ML workflow insights

## Related Concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md)
- [MLflow Runs](/concepts/mlflow-run.md)
- Databricks SQL
- Lakehouse Architecture
- Compare MLflow Runs and Models
- [MLflow System Tables Reference](/concepts/mlflow-system-tables.md)

## Sources

- compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md

# Citations

1. [compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md](/references/compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws-ab27c56a.md)
