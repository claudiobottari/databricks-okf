---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c0b2afaafa560aa73828c686de1fe2c748fdc4c0a09ea6ca64404555762158af
  pageDirectory: concepts
  sources:
    - build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gpu-utilization-monitoring-dashboard
    - GUMD
    - GPU Utilization Monitoring
    - GPU utilization monitoring
    - GPU Utilization Dashboard
    - GPU Utilization Metrics
    - gpu-utilization-monitoring-with-mlflow
    - GUMWM
    - GPU Memory
  citations:
    - file: build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
title: GPU Utilization Monitoring Dashboard
description: A Databricks dashboard for monitoring average GPU utilization across MLflow experiments, helping identify inefficient resource usage across a workspace.
tags:
  - mlflow
  - dashboards
  - gpu
  - monitoring
timestamp: "2026-06-19T14:10:13.616Z"
---

# GPU Utilization Monitoring Dashboard

The **GPU Utilization Monitoring Dashboard** is a custom Databricks dashboard that leverages MLflow metadata stored in [system tables](/concepts/mlflow-system-tables.md) to monitor average GPU utilization across experiments in a workspace. It helps data scientists and ML engineers identify inefficient GPU usage — such as experiments running with less than 10% average utilization — so they can investigate and optimize resource allocation. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Overview

The dashboard is built on top of [MLflow System Tables](/concepts/mlflow-system-tables.md) which capture system metrics recorded by MLflow during runs, including CPU, memory, and GPU utilization. By querying this data across all experiments in a workspace, the dashboard provides summary statistics for a given metric over a specified time window, making it easier to surface underutilized GPUs without manually inspecting individual runs. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Usage

The GPU Utilization Monitoring Dashboard is available as the fourth tab in the example dashboard described in the Databricks documentation. To use it:

1. Import the [example dashboard JSON](https://docs.databricks.com/aws/en/assets/files/mlflow_system_tables_dashboard.lvdash-c47a9bd31724e4ee62a78acffc600d0b.json) into your workspace.
2. Navigate to the fourth tab labeled for system metrics.
3. Input a **metric name** — for example, `gpu_utilization` (as recorded by MLflow’s system metrics logging).
4. The dashboard then displays summary statistics (e.g., average GPU utilization) across all experiments that recorded that metric within the selected time window.

The dashboard can be customized by editing the underlying queries and plots to suit specific monitoring needs. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Interpretation

A low average GPU utilization — such as below 10% — suggests that GPU resources are not being fully used. This may indicate problems like inefficient data loading, small batch sizes, or incorrectly sized clusters. The dashboard enables teams to quickly detect such patterns and take corrective action. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Related Concepts

- [MLflow System Tables](/concepts/mlflow-system-tables.md) — The underlying data source for the dashboard.
- Dashboard monitoring for ML experiments — General approach to visualizing experiment metadata.
- System metrics logging in MLflow — How MLflow records CPU, memory, and GPU utilization.
- [MLflow UI](/concepts/mlflow.md) — Alternative interface for viewing run details.
- GPU utilization optimization — Best practices for improving GPU efficiency.

## Sources

- build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md

# Citations

1. [build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md](/references/build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws-bdd77682.md)
