---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f6f6b59c1f453829062f959d531e95ad746f6c23c2013f8a6d65bdc011297275
  pageDirectory: concepts
  sources:
    - experiment-tracking-and-observability-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-ai-runtime-observability
    - DARO
  citations:
    - file: experiment-tracking-and-observability-databricks-on-aws.md
title: Databricks AI Runtime Observability
description: Overview of observability features in Databricks AI Runtime including MLflow logging, notebook output, GPU monitoring, and checkpoint management.
tags:
  - observability
  - logging
  - monitoring
  - databricks
timestamp: "2026-06-18T12:15:23.762Z"
---

# Databricks AI Runtime Observability

**Databricks AI Runtime Observability** covers the tools and practices for tracking, logging, and monitoring machine learning workloads running on AI Runtime, including single-node and distributed training. The platform integrates deeply with [MLflow](/concepts/mlflow.md) for experiment tracking, provides built-in log viewers, supports asynchronous model checkpointing to Unity Catalog volumes, and offers a real-time GPU resource dashboard. ^[experiment-tracking-and-observability-databricks-on-aws.md]

---

## MLflow Integration

AI Runtime natively integrates with MLflow for experiment tracking, model logging, and metric visualization. ^[experiment-tracking-and-observability-databricks-on-aws.md]

**Setup recommendations:**

- Upgrade MLflow to version 3.7 or newer and follow the [deep learning workflow patterns](https://docs.databricks.com/aws/en/mlflow/mlflow3-dl-workflow).
- Enable autologging for PyTorch Lightning:
  ```python
  import mlflow
  mlflow.pytorch.autolog()
  ```
- Customize run names by encapsulating training code within `mlflow.start_run(run_name="your-custom-name")`. Otherwise, the default run name is `jobTaskRun-xxxxx`.
- When using Hugging Face Transformers, use the `run_name` parameter in `TrainingArguments`:
  ```python
  from transformers import TrainingArguments
  args = TrainingArguments(
      report_to="mlflow",
      run_name="llama7b-sft-lr3e5",
      logging_steps=50,
  )
  ```
- The Serverless GPU API automatically launches an MLflow experiment with the default name `/Users/{WORKSPACE_USER}/{get_notebook_name()}`. Override it with the environment variable `MLFLOW_EXPERIMENT_NAME` (always use absolute paths).
- Resume a previous training run by setting `MLFLOW_RUN_ID` and calling `mlflow.start_run(run_id="<previous-run-id>")`.
- Set the `step` parameter in `MLFlowLogger` to reasonable batch numbers to avoid hitting the 10 million metric step limit. ^[experiment-tracking-and-observability-databricks-on-aws.md]

---

## Viewing Logs

- **Notebook output** — Standard output and errors from training code appear in the notebook cell output.
- **MLflow logs** — The MLflow experiment UI displays training metrics, parameters, and artifacts. ^[experiment-tracking-and-observability-databricks-on-aws.md]

---

## Model Checkpointing

For distributed training, save and load model checkpoints asynchronously to Unity Catalog volumes using the `UCVolumeWriter` and `UCVolumeReader` classes from the `serverless_gpu.data` package, which work with the [Torch Distributed Checkpoint](/concepts/pytorch-distributed-checkpoint-dcp.md) (DCP) API. These storage backends stage all I/O through a fast local directory (`/tmp`, NVMe-backed on serverless GPU nodes) and upload to or download from the Unity Catalog volume — faster than writing directly to the FUSE mount. Metadata atomicity is preserved: the writer publishes the `.metadata` file only after all data shards finish uploading. ^[experiment-tracking-and-observability-databricks-on-aws.md]

> **Note:** `UCVolumeWriter`, `UCVolumeReader`, and `UCVolumeDataset` require GPU environment 5 or above (Serverless GPU Python API 0.5.16+).

**Checkpointing frequency:** Aim for one checkpoint every 30 minutes to an hour, balancing lost work against I/O overhead.

**Asynchronous save example:**
```python
import torch.distributed.checkpoint as dcp
from serverless_gpu.data import UCVolumeWriter

checkpoint_path = "/Volumes/my_catalog/my_schema/model/checkpoints"
writer = UCVolumeWriter(checkpoint_path)
future = dcp.async_save(state_dict, storage_writer=writer)
# ... continue training ...
future.result()  # blocks until upload completes
```

Asynchronous saves require a CPU backend on the process group, so initialize it with `torch.distributed.init_process_group(backend="cpu:gloo,cuda:nccl", ...)`.

**Load a checkpoint:**
```python
from serverless_gpu.data import UCVolumeReader
reader = UCVolumeReader(checkpoint_path)
dcp.load(state_dict, storage_reader=reader)
```

### Data Pipeline Checkpointing

A model checkpoint captures model and optimizer state, but not the position of the data pipeline within the dataset. When resuming, the training run cannot fast-forward to the exact sample where it stopped. Account for this by restarting from an epoch boundary or by tracking processed samples (or shards) in the training state so they can be skipped on resume. ^[experiment-tracking-and-observability-databricks-on-aws.md]

---

## Monitor GPU Resources

Use the **GPU resources** pane to monitor GPU health and utilization while running code on AI Runtime. The pane supports both single-node and multi-node workloads. To open it, connect a notebook to AI Runtime and click the chip icon (**GPU resources**) in the right side pane. ^[experiment-tracking-and-observability-databricks-on-aws.md]

The pane displays the following metrics for each GPU:
- GPU utilization percentage
- GPU memory usage
- Temperature

Metrics are polled every 10 seconds and up to 2 hours of history are retained. Click **Refresh** to fetch the latest values immediately. After 5 minutes of inactivity, the pane pauses; reopen it to resume monitoring. ^[experiment-tracking-and-observability-databricks-on-aws.md]

---

## Multi-User Collaboration

- Store shared code (helper modules, environment YAML files) in `/Workspace/Shared` rather than user-specific folders.
- For code under active development, use Git folders in user-specific directories (`/Workspace/Users/<email>/`) and push to remote Git repos for version control.
- Collaborators can use notebook sharing and commenting features. ^[experiment-tracking-and-observability-databricks-on-aws.md]

---

## Global Limits

See [Resource limits](https://docs.databricks.com/aws/en/resources/limits) for applicable quotas such as the 10 million metric step limit in MLflow. ^[experiment-tracking-and-observability-databricks-on-aws.md]

---

## Related Concepts

- [MLflow](/concepts/mlflow.md) – Core experiment tracking and model registry
- Unity Catalog volumes – Governed storage for checkpoints and artifacts
- [Torch Distributed Checkpoint](/concepts/pytorch-distributed-checkpoint-dcp.md) – The PyTorch API for saving/loading distributed state
- [Serverless GPU API](/concepts/serverless-gpu-api.md) – Managed GPU compute for AI Runtime
- [GPU resource monitoring](/concepts/gpu-resources-monitoring-pane.md) – Real-time GPU utilization, memory, and temperature
- Deep learning workflow patterns – MLflow best practices for deep learning
- Resource limits – Databricks quotas affecting observability

## Sources

- experiment-tracking-and-observability-databricks-on-aws.md

# Citations

1. [experiment-tracking-and-observability-databricks-on-aws.md](/references/experiment-tracking-and-observability-databricks-on-aws-4c27cc68.md)
