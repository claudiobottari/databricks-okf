---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 31ee9821207a5ea31f01f470d5e19bb5dd8283d5576703623d50810e51c27a3a
  pageDirectory: concepts
  sources:
    - build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-dashboards-from-system-tables
    - MDFST
    - Build dashboards with MLflow metadata in system tables
  citations:
    - file: build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
title: MLflow Dashboards from System Tables
description: Building and using Databricks dashboards that query MLflow system tables to visualize experiment results, run details, and system metrics across a workspace.
tags:
  - mlflow
  - databricks
  - dashboards
timestamp: "2026-06-19T09:10:12.507Z"
---

## MLflow Dashboards from System Tables

**MLflow Dashboards from System Tables** are Lakeview Dashboards that use MLflow metadata stored in System Tables (Databricks) to analyze and monitor experiments, runs, metrics, and system-level resource utilization across an entire [Databricks Workspace](/concepts/workspace-feature-store-ui.md). By leveraging system tables instead of the [MLflow UI](/concepts/mlflow.md) or REST APIs, you can avoid extensive iteration and build reusable, customizable visualizations. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

### Overview

System tables store MLflow metadata (experiments, runs, tags, parameters, metrics, system metrics) in a queryable format. Using these tables, you can build dashboards that provide insights over many runs and experiments at once — something that would be time-consuming with the per‑run MLflow UI. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

Databricks provides an example dashboard (JSON file) that you can [import into your workspace](https://docs.databricks.com/aws/en/dashboards/automate/import-export#import). The dashboard skeleton includes input boxes to filter by experiment ID, run ID, and metric name. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

### Dashboard for Single Run Details

The example dashboard includes a view that replicates the run details page from the MLflow UI. Given an experiment ID, run ID, and metric name, it displays:

- Run details (tags, parameters, metric values)
- A metric graph over time

You obtain the experiment ID and run ID from the run details page URL: `https://<workspace>.databricks.com/ml/experiments/<experiment_id>/runs/<run_id>`. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

![Run experiment IDs in the MLflow UI](https://docs.databricks.com/aws/en/assets/images/run-experiment-ids-a370fb107de18540b3be8505e7dec9c5.png)

After importing the dashboard, use the input boxes at the top to filter for the relevant run and experiment. The included queries and plots can be modified to suit your needs. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

![Run details dashboard](https://docs.databricks.com/aws/en/assets/images/dashboard-run-details-7e80c6353e0efb82d838f0cf2ddbc1ad.png)

### Dashboard to Monitor Average GPU Utilization Across Experiments

A separate tab in the example dashboard lets you input a metric name and get summary statistics across all experiments that recorded that metric within a given time window. This is especially useful for monitoring [system metrics](/concepts/mlflow-system-metrics.md) — such as CPU, memory, or GPU utilization — that [MLflow Tracking](/concepts/mlflow-tracking.md) records automatically. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

For example, you can track average GPU utilization across experiments and identify runs with inefficient resource usage (e.g., average GPU utilization below 10%) for further investigation. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

![Average GPU utilization dashboard](https://docs.databricks.com/aws/en/assets/images/dashboard-gpu-utilization-6d32069b826aad9ed769ef394b34dd76.png)

### Getting Started

1. Download the example dashboard JSON from the [Databricks documentation](https://docs.databricks.com/aws/en/assets/files/mlflow_system_tables_dashboard.lvdash-c47a9bd31724e4ee62a78acffc600d0b.json) (or from [this gist](https://gist.github.com/ian-ack-db/684a83040a557f92f1668449c0df75df)).
2. Import it into your workspace via the [Dashboard Import/Export](/concepts/databricks-dashboard-importexport.md) feature.
3. Use the input boxes to filter by experiment ID, run ID, and metric name.
4. Modify the underlying SQL queries and visualizations to match your analysis requirements.

### Related Concepts

- System Tables (Databricks) – The underlying storage for MLflow metadata.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – The component that logs parameters, metrics, and system metrics.
- Lakeview Dashboards – The dashboard engine used to build these visualizations.
- [System Metrics](/concepts/mlflow-system-metrics.md) – CPU, memory, GPU utilization, and other resource metrics logged by MLflow.
- [GPU Utilization Monitoring](/concepts/gpu-utilization-monitoring-dashboard.md) – A specific use case for the dashboard.

### Sources

- build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md

# Citations

1. [build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md](/references/build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws-bdd77682.md)
