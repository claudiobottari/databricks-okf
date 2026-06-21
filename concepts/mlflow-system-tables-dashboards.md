---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 55ba5425b04f4923e9f282757fd9e4cd8874a131a1e3467fdefc6686d78ffb49
  pageDirectory: concepts
  sources:
    - build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-system-tables-dashboards
    - MSTD
    - Usage Dashboards
  citations:
    - file: build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
title: MLflow System Tables Dashboards
description: Building dashboards from MLflow metadata stored in Databricks system tables to analyze experiments and runs across an entire workspace
tags:
  - mlflow
  - dashboards
  - databricks
  - system-tables
timestamp: "2026-06-19T17:41:28.496Z"
---

Here is the wiki page for "MLflow System Tables Dashboards", based solely on the provided source material.

---

## MLflow System Tables Dashboards

**MLflow System Tables Dashboards** are visual dashboards built using the metadata stored in [MLflow System Tables](/concepts/mlflow-system-tables.md). These dashboards allow you to analyze MLflow experiments and runs across an entire workspace, providing a more efficient method for overview and monitoring than the standard MLflow UI or REST APIs. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

### Purpose

The existing MLflow UI and REST APIs require extensive, time-consuming iteration to perform broad analysis across multiple experiments and runs. Dashboards built on system tables solve this by enabling the creation of rich visualizations for metrics and metadata across the entire workspace in a single view. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

### Available Dashboards

#### Single Run Details Dashboard

Databricks provides an [example dashboard](https://docs.databricks.com/aws/en/assets/files/mlflow_system_tables_dashboard.lvdash-c47a9bd31724e4ee62a78acffc600d0b.json) that replicates the information shown on the run details page of the [MLflow UI](/concepts/mlflow.md). This dashboard can be downloaded as a JSON file and imported into a workspace. It contains skeleton data and is designed to display run details, tags, parameters, and a metric graph for a given experiment ID, run ID, and metric name. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

The experiment ID and run ID required to use the dashboard can be found on the run details page in the MLflow UI or directly in the URL:
`https://<workspace>.databricks.com/ml/experiments/<experiment_id>/runs/<run_id>`.

After importing the dashboard, users can filter for the relevant run and experiment using input boxes at the top of the dashboard. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

#### Average GPU Utilization Monitor

A separate tab within the example dashboard allows users to input a metric name and view summary statistics across all experiments that have recorded that metric within a given time window. This feature is useful for monitoring [system metrics](/concepts/mlflow-system-metrics.md)—such as CPU, memory, or GPU utilization—recorded by MLflow across the workspace. For instance, the dashboard can surface experiments with an average GPU utilization of less than 10%, which may warrant further investigation. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

### Related Concepts

- [MLflow System Tables](/concepts/mlflow-system-tables.md)
- [MLflow Tracking](/concepts/mlflow-tracking.md)
- [System Metrics](/concepts/mlflow-system-metrics.md)
- Databricks Dashboards
- [MLflow Experiments](/concepts/mlflow-experiment.md)

### Sources

- build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md

# Citations

1. [build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md](/references/build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws-bdd77682.md)
