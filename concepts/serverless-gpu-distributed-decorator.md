---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 51cb807a4c20760bf18c540b22aa2cbea030864549f1fd63befc0ad29daaecb7
  pageDirectory: concepts
  sources:
    - distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-gpu-distributed-decorator
    - SG@D
    - SGD
  citations:
    - file: distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
title: Serverless GPU @distributed Decorator
description: A Databricks serverless_gpu library decorator that launches PyTorch Lightning training across multiple GPUs on a single node
tags:
  - databricks
  - distributed-computing
  - gpu-computing
timestamp: "2026-06-18T15:31:05.640Z"
---

# Serverless GPU @distributed Decorator

The **Serverless GPU @distributed Decorator** is a Python decorator from the `serverless_gpu` library that enables distributed training across multiple GPUs on Databricks Serverless GPU compute. It simplifies launching multi-GPU training jobs by automatically handling the distribution of training functions across the specified number of GPUs. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Overview

The `@distributed` decorator allows data scientists and ML engineers to scale training workloads across multiple GPUs without manually configuring distributed training infrastructure. When applied to a training function, the decorator manages the launch and coordination of training across all specified GPUs on a single node. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Usage

### Import

The decorator is imported from the `serverless_gpu` Python library:

```python
from serverless_gpu import distributed
```

^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

### Basic Syntax

Apply the `@distributed` decorator to a training function, specifying the number of GPUs and GPU type:

```python
@distributed(gpus=8, gpu_type="H100")
def training_function(args, cat_cols, emb_counts, device, train_data, val_data, checkpoint_path):
    # Training logic using PyTorch Lightning Trainer
    trainer = Trainer(
        max_epochs=args.epochs,
        accelerator="gpu",
        strategy="ddp",
        devices=8,
        # ... other configuration
    )
    trainer.fit(model, train_dataloaders=train_dataloader, val_dataloaders=eval_dataloader)
    return result
```

^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

### Executing the Distributed Function

After defining the decorated function, call the `.distributed()` method to launch the training:

```python
result = training_function.distributed()
```

^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `gpus` | int | Number of GPUs to use for distributed training |
| `gpu_type` | str | Type of GPU (e.g., `"H100"`) |

^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Prerequisites

To use the `@distributed` decorator, configure your notebook to use Serverless GPU compute:

1. Click the **Connect** dropdown to open the compute selector.
2. Select **Serverless GPU**.
3. Open the **Environment** panel.
4. Select the desired accelerator (e.g., **8xH100**).
5. Select the appropriate environment (e.g., **AI v5**).
6. Click **Apply**, then **Confirm**.

^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Integration with PyTorch Lightning

The `@distributed` decorator works seamlessly with [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md)'s `Trainer` API. When using the decorator, configure the Lightning `Trainer` with:

- `accelerator="gpu"`
- `strategy="ddp"` (Distributed Data Parallel)
- `devices=8` (matching the number specified in the decorator)

The decorator handles launching the training across all GPUs, while Lightning manages the distributed training loop, logging, and checkpointing. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Example Workflow

A typical workflow using the `@distributed` decorator includes:

1. **Define training configurations** using dataclasses or dictionaries.
2. **Create the model** using PyTorch Lightning's `LightningModule`.
3. **Define the training function** with the `@distributed` decorator, including data loading, model creation, and Lightning `Trainer` setup.
4. **Execute training** by calling `.distributed()` on the decorated function.
5. **Evaluate results** by loading the best checkpoint and running inference.
6. **Register the model** to [MLflow](/concepts/mlflow.md) for serving.

^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Related Concepts

- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The underlying compute infrastructure for distributed training
- PyTorch Lightning Trainer — The training framework commonly used with the decorator
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — The distributed strategy used with the decorator
- [MLflow Tracking](/concepts/mlflow-tracking.md) — For logging and managing training runs
- GPU Scheduling — Optimizing GPU utilization for distributed workloads
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) — GPU types available for distributed training

## Sources

- distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md

# Citations

1. [distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md](/references/distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws-093d5979.md)
