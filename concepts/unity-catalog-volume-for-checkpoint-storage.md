---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e7a7af34d0a2378ca71eb55d0266f0e808fd4543e5376c0aa48e5925fd68af7d
  pageDirectory: concepts
  sources:
    - distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-volume-for-checkpoint-storage
    - UCVFCS
  citations:
    - file: distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
title: Unity Catalog Volume for Checkpoint Storage
description: A Databricks pattern for storing distributed training checkpoints in Unity Catalog volumes, enabling versioned, governed storage of model artifacts that integrates with MLflow and the Databricks ecosystem.
tags:
  - databricks
  - data-governance
  - model-storage
timestamp: "2026-06-18T12:07:23.051Z"
---

# Unity Catalog Volume for Checkpoint Storage

**Unity Catalog Volume for Checkpoint Storage** refers to the practice of using a [Unity Catalog](/concepts/unity-catalog.md) volume as the persistent storage location for model checkpoints generated during distributed training on Databricks. Checkpoints — snapshots of model parameters, optimizer state, and training metadata — are saved to a volume path and can be logged as [MLflow](/concepts/mlflow.md) artifacts for versioning, reproducibility, and later inference or continued training.

## Overview

When training large models with distributed strategies such as [PyTorch FSDP](/concepts/pytorch-fully-sharded-data-parallel-fsdp.md), checkpoints must be stored in a location accessible by all worker processes. Unity Catalog volumes provide a governed, schema-organized file store that integrates with Databricks’ data governance and MLflow tracking. By saving checkpoints to a Unity Catalog volume, teams ensure that checkpoint data is discoverable, auditable, and reusable across experiments. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Configuration

### Prerequisites

- Access to a Unity Catalog [Metastore](/concepts/metastore.md).
- `USE CATALOG` and `USE SCHEMA` privileges on the [Catalog and Schema](/concepts/catalog-and-schema.md) where the volume resides.
- A Unity Catalog volume (created via Catalog Explorer or SQL `CREATE VOLUME`).

### Setting Up Checkpoint Storage

In a notebook, you can configure the volume path using workspace widgets:

```python
dbutils.widgets.text("uc_catalog", "main")
dbutils.widgets.text("uc_schema", "default")
dbutils.widgets.text("uc_volume", "checkpoints")
dbutils.widgets.text("model_name", "transformer_fsdp")

UC_CATALOG = dbutils.widgets.get("uc_catalog")
UC_SCHEMA = dbutils.widgets.get("uc_schema")
UC_VOLUME = dbutils.widgets.get("uc_volume")
MODEL_NAME = dbutils.widgets.get("model_name")
```

Then construct the checkpoint directory path:

```python
CHECKPOINT_DIR = f"/Volumes/{UC_CATALOG}/{UC_SCHEMA}/{UC_VOLUME}/{MODEL_NAME}"
```

This path can be used directly with PyTorch distributed checkpoint APIs (e.g., `torch.distributed.checkpoint.save`) or any file-based checkpoint mechanism. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Saving and Loading Checkpoints

### Saving During Training

Inside a distributed training function, use the volume path with a writer that persists checkpoints. The example below saves checkpoints periodically and logs them as MLflow artifacts:

```python
from torch.distributed.checkpoint import FileSystemWriter as StorageWriter
import torch.distributed.checkpoint as dcp

writer = StorageWriter(cache_staged_state_dict=False, path=CHECKPOINT_DIR)
state_dict = { 'app': AppState(model, optimizer) }
dcp.save(state_dict, storage_writer=writer, checkpoint_id=f"{CHECKPOINT_DIR}/step{batch_idx}")

# Log to MLflow for traceability
mlflow.log_artifacts(f'{CHECKPOINT_DIR}/step{batch_idx}', artifact_path=f'checkpoints/step{batch_idx}')
```

^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

### Loading a Checkpoint

To load a checkpoint for inference or continued training, use `dcp.load()` with the volume path. Because no process group is initialized outside the distributed context, collective operations are automatically disabled:

```python
model = SimpleTransformer(input_dim=512, num_layers=4, num_classes=10)
optimizer = optim.AdamW(model.parameters(), lr=0.001, weight_decay=0.01)
state_dict = { 'app': AppState(model, optimizer) }

dcp.load(state_dict=state_dict, checkpoint_id=f'{CHECKPOINT_DIR}/step0')
model.load_state_dict(state_dict['app'].state_dict()['model'])
```

^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Benefits

- **Governed storage:** Checkpoints are stored in Unity Catalog, inheriting access controls and audit logging.
- **MLflow integration:** Checkpoints can be logged as artifacts, linking them to specific MLflow runs for experiment tracking.
- **Reproducibility:** The volume path is deterministic and can be reconstructed from experiment metadata, enabling downstream inference pipelines to locate the correct checkpoint.
- **Scalability:** Volume storage works across multiple worker nodes in distributed training, unlike local filesystems.

## Best Practices

- **Use a dedicated volume per model family** to avoid namespace collisions and simplify cleanup.
- **Log checkpoints as MLflow artifacts** to preserve provenance. The checkpoint directory path can be recorded as a parameter or tag on the [MLflow Run](/concepts/mlflow-run.md).
- **Set appropriate retention policies** on the volume to avoid accumulating stale checkpoints. Unity Catalog volumes support lifecycle management.
- **Grant `USE CATALOG` and `USE SCHEMA`** to service principals or users who need to read checkpoints for inference.

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that provides volumes.
- [MLflow Tracking](/concepts/mlflow-tracking.md) — For logging checkpoint artifacts and experiment metadata.
- [PyTorch FSDP](/concepts/pytorch-fully-sharded-data-parallel-fsdp.md) — Distributed training strategy that uses checkpoint storage.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The compute environment where checkpoint storage is configured.
- [Distributed Checkpointing](/concepts/pytorch-distributed-checkpoint-dcp.md) — Broader concept of saving state across multiple workers.
- Volume (Unity Catalog) — The securable object type used for file storage.

## Sources

- distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md

# Citations

1. [distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md](/references/distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws-e728aa55.md)
