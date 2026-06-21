---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4e73ef305030f10036080d6147623e84446d80dbb0f84a1cd53e2d9d3ca389ea
  pageDirectory: concepts
  sources:
    - build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - monitoring-gpu-utilization-with-mlflow-system-metrics
    - MGUWMSM
  citations:
    - file: build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
title: Monitoring GPU Utilization with MLflow System Metrics
description: Using MLflow-recorded system metrics (GPU, CPU, memory usage) and Databricks dashboards to monitor compute efficiency across experiments, particularly identifying underutilized GPUs.
tags:
  - mlflow
  - gpu
  - monitoring
  - system-metrics
timestamp: "2026-06-19T09:11:13.165Z"
---

# Monitoring GPU Utilization with MLflow System Metrics

**Monitoring GPU Utilization with MLflow System Metrics** refers to the practice of using [MLflow System Metrics](/concepts/mlflow-system-metrics.md)—performance data automatically collected by MLflow during training runs—to analyze and optimize GPU usage across experiments. By building dashboards from this metadata stored in [system tables](/concepts/mlflow-system-tables.md), teams can identify underutilized GPUs, debug performance issues, and reduce infrastructure costs.

## Dashboard-Based Monitoring

A practical approach to monitoring GPU utilization is to build a dashboard using MLflow metadata from system tables. This method offers an efficient alternative to the existing MLflow UI and REST APIs, which would require extensive, time-consuming iteration to produce the same analysis. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

### Average GPU Utilization Dashboard

A dedicated dashboard (available as the fourth tab in [the example dashboard](https://docs.databricks.com/aws/en/assets/files/mlflow_system_tables_dashboard.lvdash-c47a9bd31724e4ee62a78acffc600d0b.json)) provides summary statistics across all experiments that record system metrics. It enables monitoring of inefficient CPU, memory, or GPU utilization across the workspace. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

In the example dashboard, you can input a metric name to see average GPU utilization across all experiments within a given time window. The visualization may reveal experiments with an average GPU utilization of less than 10%—a strong indicator for investigation. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

### Key Dashboard Features

- **Metric input**: Users can specify any system metric name (e.g., `gpu_utilization`) for analysis.
- **Time window filtering**: Restrict the view to a specific time range to focus on recent or historical runs.
- **Aggregate statistics**: The dashboard computes average utilization across all experiments that report the selected metric.
- **Low-utilization detection**: Exposing experiments with sub-10% utilization helps prioritize optimization efforts.

## Use Cases

### Identifying Underutilized GPUs

When GPU capacity is scarce or expensive (e.g., [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md)), detecting underutilized runs helps reallocate resources. Workloads averaging <10% GPU utilization may benefit from consolidation, smaller instance types, or more efficient training strategies. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

### Cost Optimization

By correlating low GPU utilization with job duration, teams can estimate wasted cloud spend. For example, a training run lasting 24 hours on an expensive GPU instance at 5% utilization represents nearly 95% wasted compute cost. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

### Capacity Planning

Aggregate GPU utilization data across experiments helps determine whether existing GPU capacity is sufficient or if additional resources (e.g., more A100 instances) should be requested. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Data Sources

MLflow records system metrics as part of tracking metadata. These metrics are stored in the workspace's system tables, which can be queried using standard SQL or visualized through Databricks dashboards. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Getting Started

1. **Import the example dashboard**: Download the [dashboard JSON file](https://docs.databricks.com/aws/en/assets/files/mlflow_system_tables_dashboard.lvdash-c47a9bd31724e4ee62a78acffc600d0b.json) and import it into your workspace.
2. **Explore the dashboard**: The fourth tab provides the GPU utilization summary. Use the metric name input to analyze specific system metrics.
3. **Customize**: Modify the underlying queries and plots to match your monitoring needs.

## Related Concepts

- [MLflow System Metrics](/concepts/mlflow-system-metrics.md) – Performance metrics automatically recorded during training runs.
- System Tables – Storage location for MLflow metadata across the workspace.
- GPU Scheduling – Optimizing GPU allocation for distributed workloads.
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) – Efficient GPU instances for deep learning.
- [Dashboard for Single Run Details](/concepts/dashboard-for-single-run-details.md) – Companion dashboard for per-run analysis.

## Sources

- build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md

# Citations

1. [build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md](/references/build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws-bdd77682.md)
