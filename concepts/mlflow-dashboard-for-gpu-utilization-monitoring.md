---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 17b1ca9e389e1e821f0e28c5b8618dd88de38bd8abb812746e400b19028a2a73
  pageDirectory: concepts
  sources:
    - build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-dashboard-for-gpu-utilization-monitoring
    - MDFGUM
  citations:
    - file: build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
title: MLflow Dashboard for GPU Utilization Monitoring
description: A dashboard pattern for monitoring average GPU utilization and other system metrics across MLflow experiments within a time window, using system tables to identify inefficient resource usage.
tags:
  - mlflow
  - gpu
  - monitoring
  - dashboards
timestamp: "2026-06-18T10:53:47.317Z"
---

# MLflow Dashboard for GPU Utilization Monitoring

**MLflow Dashboard for GPU Utilization Monitoring** is a [Databricks dashboard](/concepts/databricks-dashboard-importexport.md) that uses [MLflow System Tables](/concepts/mlflow-system-tables.md) to compute and display aggregate GPU utilization statistics across all experiments in a workspace. By ingesting [system metrics](/concepts/mlflow-system-metrics.md) recorded by MLflow during training runs—such as `gpu_utilization`—the dashboard enables data science and MLOps teams to quickly locate experiments or individual runs with inefficient GPU usage (e.g., average utilization below 10%) without manually inspecting each run in the MLflow UI or making repeated REST API calls. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

The dashboard is typically created from the [example dashboard JSON file](https://docs.databricks.com/aws/en/assets/files/mlflow_system_tables_dashboard.lvdash-c47a9bd31724e4ee62a78acffc600d0b.json) provided by Databricks. After importing the file into the workspace, users can navigate to the fourth tab, enter a metric name (e.g., `gpu_utilization`, `cpu_utilization`, `memory_utilization`), and select a time window. The dashboard then returns summary statistics—such as average utilization—for every experiment that logged that metric in the given period. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

The underlying data is sourced from the system tables for MLflow (`mlflow_experiments`, `mlflow_runs`, `mlflow_metrics`). By aggregating across runs, the dashboard highlights experiments with low average GPU utilization—for example, those below 10%—which may warrant investigation into code optimizations, larger batch sizes, or more appropriate instance types to improve resource efficiency. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

This approach scales beyond the single-run view of the MLflow UI, providing a workspace-wide perspective on resource consumption. The dashboard can be extended to monitor CPU, memory, or other system-level metrics, offering a unified view of utilization efficiency across all experiments. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md)
- System Tables
- Databricks Dashboards
- [GPU Utilization Metrics](/concepts/gpu-utilization-monitoring-dashboard.md)
- [MLflow System Metrics](/concepts/mlflow-system-metrics.md)

## Sources

- build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md

# Citations

1. [build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md](/references/build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws-bdd77682.md)
