---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1dc52ae8dbf99a52f0afe0ec016497a5f1d7b221c198d9c0856b8e4def72baa9
  pageDirectory: concepts
  sources:
    - build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gpu-utilization-monitoring-with-mlflow
    - GUMWM
    - GPU Memory
  citations:
    - file: build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
title: GPU Utilization Monitoring with MLflow
description: Using MLflow system tables dashboards to monitor average GPU utilization across experiments and identify inefficient resource usage
tags:
  - mlflow
  - gpu
  - monitoring
  - databricks
timestamp: "2026-06-19T17:41:44.157Z"
---

# GPU Utilization Monitoring with MLflow

**GPU Utilization Monitoring with MLflow** refers to the practice of using [MLflow](/concepts/mlflow.md)-recorded system metrics and Databricks System Tables to build dashboards that track GPU utilization across experiments, helping identify inefficient resource usage across the workspace.

## Overview

MLflow automatically records system metrics such as CPU, memory, and GPU utilization during training runs. By storing these metrics in system tables, you can query them across all experiments in a workspace and build aggregate dashboards. This approach avoids the need to inspect individual runs through the MLflow UI or REST APIs, providing a broader, time‑efficient view of resource usage. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## How to Use the Dashboard

A pre‑built example dashboard (available as a downloadable JSON file) includes a dedicated tab for GPU utilization monitoring. On the fourth tab, you input a metric name — for example, `gpu_utilization` — and the dashboard returns summary statistics across all experiments that recorded that metric, filtered by a user‑defined time window. The dashboard queries [MLflow System Tables](/concepts/mlflow-system-tables.md) to aggregate the data, and you can further customize the queries and visualizations to suit your monitoring requirements. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Example

In a typical scenario, the dashboard might reveal several experiments with an average GPU utilization of less than 10%. Such low utilization indicates that those workloads are underutilizing the GPU and may benefit from optimization, consolidation, or changes in training configuration. This insight helps data science teams prioritize investigations and improve hardware efficiency. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Related Concepts

- [MLflow System Tables](/concepts/mlflow-system-tables.md)
- Databricks Dashboards
- GPU Utilization
- [System Metrics Logging](/concepts/mlflow-system-metrics-monitoring.md)
- [Deep learning best practices on Databricks](/concepts/deep-learning-best-practices-on-databricks.md)
- GPU Scheduling

## Sources

- build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md

# Citations

1. [build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md](/references/build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws-bdd77682.md)
