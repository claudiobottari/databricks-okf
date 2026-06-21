---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 00bfcaa35ac790c1935e7a2260f678c1d6f95ee67c7a4408eb5cfb68994b37bc
  pageDirectory: concepts
  sources:
    - experiment-tracking-and-observability-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-integration-with-ai-runtime
    - MIWAR
  citations:
    - file: experiment-tracking-and-observability-databricks-on-aws.md
title: MLflow Integration with AI Runtime
description: AI Runtime natively integrates with MLflow for experiment tracking, metric visualization, and model logging, with support for autologging, custom run names, and environment variable configuration.
tags:
  - mlflow
  - experiment-tracking
  - databricks
timestamp: "2026-06-19T18:45:03.774Z"
---

## MLflow Integration with AI Runtime

**MLflow Integration with AI Runtime** refers to the native, built-in support for [MLflow](/concepts/mlflow.md) experiment tracking, model logging, and metric visualization when using Databricks AI Runtime for both single-node and multi-GPU workloads. AI Runtime for single-node tasks is in Public Preview; the distributed training API for multi-GPU workloads remains in Beta. ^[experiment-tracking-and-observability-databricks-on-aws.md]

### Setup and Configuration

To get the most out of MLflow on AI Runtime, upgrade MLflow to version 3.7 or newer and follow the recommended deep learning workflow patterns. ^[experiment-tracking-and-observability-databricks-on-aws.md]

**Autologging** — Enable automatic logging for PyTorch Lightning by calling:

```python
import mlflow
mlflow.pytorch.autolog()
```

^[experiment-tracking-and-observability-databricks-on-aws.md]

**Custom run names** — Encapsulate training code within `mlflow.start_run()` and set the `run_name` parameter:

```python
mlflow.start_run(run_name="your-custom-name")
```

This also works with third‑party libraries that support MLflow, such as Hugging Face Transformers:

```python
from transformers import TrainingArguments
args = TrainingArguments(
    report_to="mlflow",
    run_name="llama7b-sft-lr3e5",
    logging_steps=50,
)
```

Otherwise, the default run name is `jobTaskRun-xxxxx`. ^[experiment-tracking-and-observability-databricks-on-aws.md]

**Experiment name** — The Serverless GPU API automatically launches an MLflow experiment with the default name `/Users/{WORKSPACE_USER}/{get_notebook_name()}`. Override it with the environment variable `MLFLOW_EXPERIMENT_NAME`, which must be an absolute path:

```python
import os
os.environ["MLFLOW_EXPERIMENT_NAME"] = "/Users/<username>/my-experiment"
```

^[experiment-tracking-and-observability-databricks-on-aws.md]

**Resume training** — Set the `MLFLOW_RUN_ID` from a previous run to continue logging to the same run:

```python
mlflow.start_run(run_id="<previous-run-id>")
```

^[experiment-tracking-and-observability-databricks-on-aws.md]

**Metric logging limit** — MLflow enforces a limit of 10 million metric steps per run. On large training runs, logging every single batch can hit this limit. Set the `step` parameter in `MLFlowLogger` to a reasonable batch number (e.g., every 50 steps) to avoid exceeding the limit. ^[experiment-tracking-and-observability-databricks-on-aws.md]

### Viewing Logs

Logs are available in two places:

- **Notebook output** — Standard output and errors from training code appear in the notebook cell output.
- **MLflow logs** — The MLflow experiment UI displays training metrics, parameters, and artifacts.

^[experiment-tracking-and-observability-databricks-on-aws.md]

### Model Checkpointing

For distributed training, AI Runtime recommends saving and loading model checkpoints asynchronously to Unity Catalog volumes using the `UCVolumeWriter` and `UCVolumeReader` classes from the `serverless_gpu.data` package with the [Torch Distributed Checkpoint](/concepts/pytorch-distributed-checkpoint-dcp.md) (DCP) API. These storage backends stage all I/O through a fast local directory (`/tmp`, which is NVMe‑backed on serverless GPU nodes) and upload to or download from the Unity Catalog volume, which is faster than writing checkpoint shards directly to the FUSE mount. Metadata atomicity is preserved: the writer publishes the `.metadata` file only after its data shards finish uploading. ^[experiment-tracking-and-observability-databricks-on-aws.md]

**Prerequisites** — `UCVolumeWriter`, `UCVolumeReader`, and `UCVolumeDataset` require GPU environment 5 (Serverless GPU Python API 0.5.16+) or above. ^[experiment-tracking-and-observability-databricks-on-aws.md]

**Checkpoint frequency** — Aim for one checkpoint every 30 minutes to an hour. Tune the interval based on your step time and checkpoint size. ^[experiment-tracking-and-observability-databricks-on-aws.md]

**Asynchronous saves** — To upload checkpoints in the background while training continues, pass a `UCVolumeWriter` as the `storage_writer` to `dcp.async_save`. Asynchronous saves require a CPU backend on the process group, so initialize it with `torch.distributed.init_process_group(backend="cpu:gloo,cuda:nccl", ...)`:

```python
import torch.distributed.checkpoint as dcp
from serverless_gpu.data import UCVolumeWriter

checkpoint_path = "/Volumes/my_catalog/my_schema/model/checkpoints"
writer = UCVolumeWriter(checkpoint_path)
future = dcp.async_save(state_dict, storage_writer=writer)
# ...continue training...
future.result()  # blocks until the upload lands on the UC volume
```

Load a checkpoint with `UCVolumeReader`:

```python
from serverless_gpu.data import UCVolumeReader
reader = UCVolumeReader(checkpoint_path)
dcp.load(state_dict, storage_reader=reader)
```

^[experiment-tracking-and-observability-databricks-on-aws.md]

#### Data pipeline checkpointing

A model checkpoint captures model and optimizer state, but not the position of your data pipeline within the dataset. Therefore, a resumed run cannot fast‑forward to the exact sample where it stopped. Account for this in your resume strategy: restart from an epoch boundary, or track processed samples or shards in your own training state so you can skip them on resume. ^[experiment-tracking-and-observability-databricks-on-aws.md]

### GPU Resource Monitoring

AI Runtime provides a **GPU resources** pane to monitor GPU health and utilization while code runs. To open the pane, connect your notebook to AI Runtime, then click the **GPU resources** icon in the right side pane. The pane displays per‑GPU metrics: utilization percentage, memory usage, and temperature. It polls every 10 seconds and retains up to 2 hours of history. Click **Refresh** to fetch the latest values immediately. After 5 minutes of inactivity the pane pauses; reopen it to resume monitoring. ^[experiment-tracking-and-observability-databricks-on-aws.md]

### Multi‑User Collaboration

- Store shared code (helper modules, environment YAML files) in `/Workspace/Shared` rather than user‑specific folders like `/Workspace/Users/<your_email>/`.
- For code in active development, use [Git folders](/concepts/databricks-git-folders-for-cicd.md) in user‑specific folders and push to remote Git repos. This allows multiple users to have user‑specific clones and branches while sharing a remote repository for version control.
- Collaborators can use Databricks’ notebook sharing and commenting features.

^[experiment-tracking-and-observability-databricks-on-aws.md]

### Related Concepts

- [MLflow](/concepts/mlflow.md) — Open‑source platform for the machine learning lifecycle.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The underlying compute infrastructure for AI Runtime.
- Unity Catalog volumes — Governance‑enabled storage for checkpoint artifacts.
- [Torch Distributed Checkpoint](/concepts/pytorch-distributed-checkpoint-dcp.md) — PyTorch’s checkpointing library for distributed training.
- Deep learning workflow patterns — Recommended practices for MLflow on Databricks.
- Git integration on Databricks — Version control workflows for notebooks and code.

### Sources

- experiment-tracking-and-observability-databricks-on-aws.md

# Citations

1. [experiment-tracking-and-observability-databricks-on-aws.md](/references/experiment-tracking-and-observability-databricks-on-aws-4c27cc68.md)
