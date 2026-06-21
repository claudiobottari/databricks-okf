---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 243a338305974d2421f7ba1b31c28aa56ed466ca5bdbb26593ca050e0994426f
  pageDirectory: concepts
  sources:
    - experiment-tracking-and-observability-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gpu-resources-monitoring-pane
    - GRMP
    - GPU resource monitoring
    - GPU resources pane
  citations:
    - file: experiment-tracking-and-observability-databricks-on-aws.md
title: GPU Resources Monitoring Pane
description: A Databricks notebook side pane that displays per-GPU utilization, memory usage, and temperature metrics for AI Runtime workloads, polling every 10 seconds with 2 hours of history.
tags:
  - gpu
  - monitoring
  - observability
timestamp: "2026-06-19T18:45:16.188Z"
---

# GPU Resources Monitoring Pane

The **GPU Resources Monitoring Pane** is a real-time dashboard in [AI Runtime](/concepts/ai-runtime.md) that displays GPU health, utilization, and performance metrics while your code executes. It supports both single-node and multi-node workloads and is accessible directly from the notebook interface. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Accessing the Pane

To open the GPU Resources pane, connect your notebook to [AI Runtime](/concepts/ai-runtime.md), then click the **GPU resources** icon (chip icon) in the right side pane. The pane appears and begins displaying metrics automatically. ^[experiment-tracking-and-observability-databricks-on-aws.md]

![GPU resources pane showing utilization, memory, and temperature metrics for each GPU.](https://docs.databricks.com/aws/en/assets/images/gpu-resources-panel-16e1691e01f494715a6aeb3b22f3d387.png)

## Displayed Metrics

The pane shows the following metrics for each GPU: ^[experiment-tracking-and-observability-databricks-on-aws.md]

| Metric | Description |
|--------|-------------|
| GPU Utilization | Percentage of GPU compute capacity being used |
| GPU Memory Usage | Amount of GPU memory consumed |
| Temperature | Thermal reading of the GPU |

## Data Collection and History

The pane polls metrics every 10 seconds and retains up to 2 hours of historical data. You can click the **Refresh** icon to fetch the latest values immediately. After 5 minutes of inactivity, the pane automatically pauses monitoring; reopening the pane resumes the data collection. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Use Cases

- **Training optimization** — Monitor GPU utilization to detect underutilization or bottlenecks during model training.
- **Memory management** — Track memory usage to identify out-of-memory conditions and adjust batch sizes or model parallelism.
- **Thermal monitoring** — Observe temperature trends to prevent thermal throttling or hardware damage during prolonged workloads.
- **Multi-node debugging** — Compare metrics across nodes in distributed training to identify node-level performance disparities.

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) — The compute runtime that provides GPU resources for single-node and distributed workloads
- [MLflow Integration in AI Runtime](/concepts/mlflow-integration-in-ai-runtime.md) — Experiment tracking and metric visualization alongside GPU monitoring
- Model Checkpointing — Saving model state during training, which interacts with GPU memory usage
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) — Serverless GPU configuration with eight H100 GPUs
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) — Large model training that benefits from GPU monitoring

## Sources

- experiment-tracking-and-observability-databricks-on-aws.md

# Citations

1. [experiment-tracking-and-observability-databricks-on-aws.md](/references/experiment-tracking-and-observability-databricks-on-aws-4c27cc68.md)
