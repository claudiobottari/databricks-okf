---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b5962703738e2f455215dc9a11c80022c1f167e591feb5e5a2c28573141402f7
  pageDirectory: concepts
  sources:
    - experiment-tracking-and-observability-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-logging
    - ARL
  citations:
    - file: experiment-tracking-and-observability-databricks-on-aws.md
title: AI Runtime Logging
description: "AI Runtime provides two logging channels: notebook cell output for stdout/stderr and the MLflow experiment UI for training metrics, parameters, and artifacts."
tags:
  - logging
  - observability
  - mlflow
timestamp: "2026-06-19T18:45:35.276Z"
---

# AI Runtime Logging

**AI Runtime Logging** refers to the mechanisms for capturing, viewing, and monitoring log output from training workloads running on [AI Runtime (Databricks)](/concepts/ai-runtime.md), including standard output, errors, training metrics, and GPU resource metrics.

## Viewing Logs

AI Runtime provides two primary channels for viewing logs during training:

- **Notebook output** — Standard output and errors from training code appear directly in the notebook cell output as the code executes. ^[experiment-tracking-and-observability-databricks-on-aws.md]
- **MLflow logs** — Training metrics, parameters, and artifacts are displayed in the [MLflow](/concepts/mlflow.md) experiment UI, providing a structured view of experiment history. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## GPU Resource Monitoring

AI Runtime includes a dedicated **GPU resources** pane for real-time monitoring of GPU health and utilization during training. This pane supports both single-node and multi-node workloads. ^[experiment-tracking-and-observability-databricks-on-aws.md]

To open the pane, connect a notebook to AI Runtime, then click the chip icon (**GPU resources**) in the right side pane. ^[experiment-tracking-and-observability-databricks-on-aws.md]

The pane displays the following metrics for each GPU:
- GPU utilization percentage
- GPU memory usage
- Temperature

The pane polls metrics every 10 seconds and retains up to 2 hours of history. Click the **Refresh** icon to fetch the latest values immediately. After 5 minutes of inactivity, the pane pauses; reopen it to resume monitoring. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## MLflow Logging Configuration

AI Runtime integrates natively with [MLflow](/concepts/mlflow.md) for experiment tracking and metric logging. Several configuration recommendations ensure effective logging:

- Upgrade MLflow to version 3.7 or newer and follow deep learning workflow patterns. ^[experiment-tracking-and-observability-databricks-on-aws.md]
- Enable autologging for PyTorch Lightning using `mlflow.pytorch.autolog()`. ^[experiment-tracking-and-observability-databricks-on-aws.md]
- Customize [MLflow Run](/concepts/mlflow-run.md) names by encapsulating training code within `mlflow.start_run()` with the `run_name` parameter. The default run name is `jobTaskRun-xxxxx`. ^[experiment-tracking-and-observability-databricks-on-aws.md]
- The Serverless GPU API automatically launches an MLflow experiment with a default name based on the workspace user and notebook name. Override this using the `MLFLOW_EXPERIMENT_NAME` environment variable with an absolute path. ^[experiment-tracking-and-observability-databricks-on-aws.md]
- Resume previous training by setting the `MLFLOW_RUN_ID` from an earlier run. ^[experiment-tracking-and-observability-databricks-on-aws.md]

### Metric Step Limits

When setting the `step` parameter in `MLFlowLogger`, use reasonable batch numbers. MLflow has a limit of 10 million metric steps — logging every single batch on large training runs can hit this limit. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md)
- [AI Runtime (Databricks)](/concepts/ai-runtime.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- Model Checkpointing
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)

## Sources

- experiment-tracking-and-observability-databricks-on-aws.md

# Citations

1. [experiment-tracking-and-observability-databricks-on-aws.md](/references/experiment-tracking-and-observability-databricks-on-aws-4c27cc68.md)
