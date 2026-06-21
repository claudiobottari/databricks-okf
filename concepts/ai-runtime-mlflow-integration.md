---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b9e7e536bd5bf7d7335c97354dd0f9f04149dafb800ca6af0dad1243e8f8d0b3
  pageDirectory: concepts
  sources:
    - experiment-tracking-and-observability-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-mlflow-integration
    - ARMI
  citations:
    - file: experiment-tracking-and-observability-databricks-on-aws.md
title: AI Runtime MLflow Integration
description: Native integration of MLflow with Databricks AI Runtime for experiment tracking, model logging, and metric visualization, including autologging, custom run naming, and experiment configuration.
tags:
  - machine-learning
  - experiment-tracking
  - mlflow
timestamp: "2026-06-19T10:26:07.532Z"
---

# AI Runtime MLflow Integration

**AI Runtime MLflow Integration** refers to the native embedding of [MLflow](/concepts/mlflow.md) within the [AI Runtime](/concepts/ai-runtime.md) for single-node tasks on Databricks. This integration provides experiment tracking, model logging, metric visualization, and model checkpointing capabilities across both single-node and multi-node GPU workloads. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Overview

AI Runtime includes MLflow as a core component, enabling seamless tracking of machine learning experiments without additional configuration. The integration supports autologging for popular frameworks and provides a unified experiment UI for monitoring training metrics, parameters, and artifacts. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Setup Recommendations

### MLflow Version

Upgrade MLflow to version 3.7 or newer and follow the deep learning workflow patterns for optimal performance with AI Runtime. ^[experiment-tracking-and-observability-databricks-on-aws.md]

### Autologging for PyTorch Lightning

Enable autologging to automatically capture metrics, parameters, and models:

```python
import mlflow
mlflow.pytorch.autolog()
```

### Customizing Run Names

Control your [MLflow Run](/concepts/mlflow-run.md) name by encapsulating model training code within the `mlflow.start_run()` API scope. Use the `run_name` parameter to set custom names:

```python
mlflow.start_run(run_name="your-custom-name")
```

For third-party libraries that support MLflow (e.g., Hugging Face Transformers), use their built-in `run_name` parameter. Otherwise, the default run name is `jobTaskRun-xxxxx`. ^[experiment-tracking-and-observability-databricks-on-aws.md]

### Serverless GPU Experiment Name

The [Serverless GPU API](/concepts/serverless-gpu-api.md) automatically launches an MLflow experiment with the default name `/Users/{WORKSPACE_USER}/{get_notebook_name()}`. Override this by setting the `MLFLOW_EXPERIMENT_NAME` environment variable with an absolute path:

```python
import os
os.environ["MLFLOW_EXPERIMENT_NAME"] = "/Users/<username>/my-experiment"
```

^[experiment-tracking-and-observability-databricks-on-aws.md]

### Resuming Previous Training

Resume training from a previous run by setting the `MLFLOW_RUN_ID` from the earlier run:

```python
mlflow.start_run(run_id="<previous-run-id>")
```

^[experiment-tracking-and-observability-databricks-on-aws.md]

### Setting Metric Step Limits

Set the `step` parameter in `MLFlowLogger` to reasonable batch numbers. MLflow has a limit of 10 million metric steps—logging every single batch on large training runs can hit this limit. See Resource limits for details. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Viewing Logs

- **Notebook output** — Standard output and errors from training code appear in the notebook cell output.
- **MLflow logs** — The MLflow experiment UI displays training metrics, parameters, and artifacts.

^[experiment-tracking-and-observability-databricks-on-aws.md]

## Model Checkpointing

For distributed training, save and load model checkpoints asynchronously to Unity Catalog volumes, which provide the same governance as other Unity Catalog objects. Use `UCVolumeWriter` and `UCVolumeReader` from the `serverless_gpu.data` package with the [Torch Distributed Checkpoint (DCP)](/concepts/pytorch-distributed-checkpoint-dcp.md) API. ^[experiment-tracking-and-observability-databricks-on-aws.md]

These storage backends stage all I/O through a fast local directory (`/tmp`, which is NVMe-backed on serverless GPU nodes) and upload to or download from the Unity Catalog volume, which is faster than writing checkpoint shards directly to the FUSE mount. Metadata atomicity is preserved: the writer publishes the `.metadata` file only after its data shards finish uploading. ^[experiment-tracking-and-observability-databricks-on-aws.md]

### Upload Checkpoints Asynchronously

To upload checkpoints in the background while training continues, pass a `UCVolumeWriter` as the `storage_writer` to `dcp.async_save`. Asynchronous saves require a CPU backend on the process group, so initialize it with `torch.distributed.init_process_group(backend="cpu:gloo,cuda:nccl", ...)`: ^[experiment-tracking-and-observability-databricks-on-aws.md]

```python
import torch.distributed.checkpoint as dcp
from serverless_gpu.data import UCVolumeWriter

checkpoint_path = "/Volumes/my_catalog/my_schema/model/checkpoints"
writer = UCVolumeWriter(checkpoint_path)
future = dcp.async_save(state_dict, storage_writer=writer)
# ...continue training...
future.result()  # blocks until the upload lands on the UC volume
```

### Load Checkpoints with UCVolumeReader

```python
from serverless_gpu.data import UCVolumeReader
reader = UCVolumeReader(checkpoint_path)
dcp.load(state_dict, storage_reader=reader)
```

^[experiment-tracking-and-observability-databricks-on-aws.md]

### Data Pipeline Checkpointing

A model checkpoint captures model and optimizer state, but not the position of your data pipeline within the dataset. Account for this by restarting from an epoch boundary, or tracking processed samples or shards in your own training state so you can skip them on resume. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Monitor GPU Resources

Use the **GPU resources** pane to monitor GPU health and utilization while your code runs on AI Runtime. The pane supports both single-node and multi-node workloads. ^[experiment-tracking-and-observability-databricks-on-aws.md]

To open the pane, connect your notebook to AI Runtime, then click the **GPU resources** icon in the right side pane. ^[experiment-tracking-and-observability-databricks-on-aws.md]

The pane displays the following metrics for each GPU:
- GPU utilization percentage
- GPU memory usage
- Temperature

The pane polls metrics every 10 seconds and retains up to 2 hours of history. Click **Refresh** to fetch the latest values immediately. After 5 minutes of inactivity, the pane pauses; reopen it to resume monitoring. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Multi-user Collaboration

- Store shared code (e.g., helper modules or environment YAML files) in `/Workspace/Shared` instead of user-specific folders.
- For code in active development, use Git folders in user-specific folders and push to remote Git repos.
- Collaborators can share and comment on notebooks.

^[experiment-tracking-and-observability-databricks-on-aws.md]

## Related Concepts

- [MLflow](/concepts/mlflow.md) — The open-source platform for experiment tracking and model management
- [AI Runtime](/concepts/ai-runtime.md) — The Databricks runtime for single-node and multi-node AI workloads
- [Unity Catalog](/concepts/unity-catalog.md) — The governance and metadata layer for Databricks objects
- [Torch Distributed Checkpoint](/concepts/pytorch-distributed-checkpoint-dcp.md) — PyTorch's API for distributed model checkpointing
- [Serverless GPU API](/concepts/serverless-gpu-api.md) — The API for serverless GPU training on Databricks
- Deep Learning Workflow Patterns — Best practices for MLflow-based deep learning workflows

## Sources

- experiment-tracking-and-observability-databricks-on-aws.md

# Citations

1. [experiment-tracking-and-observability-databricks-on-aws.md](/references/experiment-tracking-and-observability-databricks-on-aws-4c27cc68.md)
