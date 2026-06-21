---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 27dd37f086cc184c2ab7b4336d51117038e25ff507ce0086fda87a4ffce71b30
  pageDirectory: concepts
  sources:
    - build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-dashboard-for-run-details
    - MDFRD
    - MLflow UI run details page
  citations:
    - file: build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
title: MLflow Dashboard for Run Details
description: A dashboard pattern that reproduces MLflow UI run details (tags, parameters, metric graphs) from system table data using customizable SQL queries.
tags:
  - mlflow
  - dashboards
  - visualization
timestamp: "2026-06-18T14:33:51.835Z"
---

# MLflow Dashboard for Run Details

**MLflow Dashboard for Run Details** is a prebuilt dashboard that visualizes MLflow experiment and run metadata from [system tables](/concepts/mlflow-system-tables.md) in Databricks, replicating the information shown on the [MLflow Run](/concepts/mlflow-run.md) details page. It provides an alternative to using the MLflow UI or REST APIs, which would require extensive iteration to obtain the same analytical view. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Overview

Using MLflow metadata stored in system tables, users can build dashboards to analyze MLflow experiments and runs across an entire workspace. The example dashboard for run details contains a skeleton of data that reproduces what is shown on the run details page in the MLflow UI. For a given experiment ID, run ID, and metric name, it displays run details along with tags, parameters, and a metric graph. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Getting Started

### Importing the Dashboard

To start visualizing MLflow data, download the [example dashboard JSON file](https://docs.databricks.com/aws/en/assets/files/mlflow_system_tables_dashboard.lvdash-c47a9bd31724e4ee62a78acffc600d0b.json) and [import it into your workspace](https://docs.databricks.com/aws/en/dashboards/automate/import-export#import). The dashboard can also be imported from a JSON file definition available in this [GitHub Gist](https://gist.github.com/ian-ack-db/684a83040a557f92f1668449c0df75df). ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

### Finding Experiment and Run IDs

You can obtain the experiment ID and run ID from the [MLflow Run](/concepts/mlflow-run.md) details page, both from the UI and from the URL itself:
```
https://<workspace>.databricks.com/ml/experiments/<experiment_id>/runs/<run_id>
```
^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

### Using the Dashboard

After importing the dashboard, navigate to it from the left navigation menu. Use the input boxes at the top to filter for the relevant run and experiment within your workspace to plot. The dashboard includes multiple tabs and visualizations that you can explore and modify to meet your needs. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Features

The dashboard for run details includes:

- **Run details**: Display of core run information
- **Tags and parameters**: Visual representation of logged tags and parameters
- **Metric graphs**: Time-series plotting of metrics for the specified run

You can explore the underlying queries and change the plots as needed. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Additional Dashboard Tabs

### GPU Utilization Monitoring

The dashboard also includes a tab where you can input a metric name to get summary statistics across all experiments with that metric within a given time window. This is useful for monitoring [MLflow System Metrics](/concepts/mlflow-system-metrics.md) recorded across your workspace, such as GPU utilization, CPU usage, or memory efficiency. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

In the example, you can identify experiments with an average GPU utilization of less than 10% that may warrant investigation. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Benefits

Using dashboards built from system tables provides several advantages over the MLflow UI:

- **Workspace-wide analysis**: View experiments and runs from the entire workspace, not just individual experiments
- **Customizable visualizations**: Modify queries and plots to meet specific analytical needs
- **Time-based filtering**: Analyze metrics across specified time windows
- **Aggregate statistics**: Compute summary statistics across multiple experiments

## Related Concepts

- [MLflow System Tables](/concepts/mlflow-system-tables.md) — The underlying data source for dashboard queries
- Databricks Dashboards — The dashboard platform used to visualize MLflow metadata
- [MLflow Runs](/concepts/mlflow-run.md) — The fundamental unit of logged experiments
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Logical grouping of related MLflow runs
- [MLflow Tracking](/concepts/mlflow-tracking.md) — The core logging component that produces the metadata

## Sources

- build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md

# Citations

1. [build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md](/references/build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws-bdd77682.md)
