---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6c71edd1287124cf5af04890cb415cd9217d2108c4414693ccf0912b80155fcb
  pageDirectory: concepts
  sources:
    - distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-serverless-gpu-with-distributed-decorator
    - DSGW@D
  citations:
    - file: distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
title: Databricks Serverless GPU with @distributed Decorator
description: Databricks serverless GPU compute with a Python decorator (`@distributed`) that transparently launches training across multiple H100 GPUs on a single node.
tags:
  - databricks
  - distributed-training
  - gpu
  - serverless
timestamp: "2026-06-19T10:16:47.321Z"
---

# Databricks Serverless GPU with @distributed Decorator

**Databricks Serverless GPU with @distributed Decorator** is a feature that enables distributed training of deep learning models across multiple GPUs using a simple Python decorator. The `@distributed` decorator, part of the `serverless_gpu` Python library, handles launching and managing training across all GPUs in a serverless GPU compute cluster. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Overview

The `@distributed` decorator provides a streamlined approach to distributed training on [Databricks Serverless GPU](/concepts/databricks-serverless-gpu.md) compute. Rather than manually configuring distributed computing frameworks, developers can wrap their training function with the decorator and specify the number of GPUs and GPU type required. The decorator automatically distributes the training workload across the specified GPUs. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Configuration

To use serverless GPU with the `@distributed` decorator, you must configure your notebook to use serverless GPU compute:

1. Click the **Connect** dropdown at the top of the notebook to open the compute selector.
2. Select **Serverless GPU**.
3. Open the **Environment** panel on the right side.
4. Select the desired accelerator (e.g., **8xH100**).
5. Select an environment version (e.g., **AI v5**).
6. Click **Apply**, then **Confirm**.

After configuration, the notebook is connected to serverless GPU compute, and the `@distributed` decorator handles launching training across all available GPUs. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Usage

### Import

The `@distributed` decorator is imported from the `serverless_gpu` Python library: ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

```python
from serverless_gpu import distributed
```

### Decorator Syntax

Apply the decorator to your training function, specifying the number of GPUs and GPU type: ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

```python
@distributed(gpus=8, gpu_type="H100")
def training_function(args, cat_cols, emb_counts, device, train_data, val_data, checkpoint_path):
    # Training logic using PyTorch Lightning Trainer
    trainer = Trainer(
        max_epochs=args.epochs,
        accelerator="gpu",
        strategy="ddp",
        devices=8,
        # Additional configuration
    )
    trainer.fit(model, train_dataloaders=train_dataloader, val_dataloaders=eval_dataloader)
    return result
```

### Executing Distributed Training

Call the `.distributed()` method on the decorated function to launch the training: ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

```python
result = training_function.distributed()
```

## Integration with PyTorch Lightning

The `@distributed` decorator works particularly well with [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) and the `Trainer` API. When using this combination, the training function typically includes: ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

- A LightningModule defining the model architecture and training logic
- DataLoader instances for training and validation data
- A Trainer configured with `accelerator="gpu"`, `strategy="ddp"` ([Distributed Data Parallel](/concepts/distributed-data-parallel-ddp.md)), and `devices` matching the `@distributed` decorator's GPU count
- Callbacks for logging, checkpointing, and monitoring

## Example: Two Tower Recommendation Model

A practical example of the `@distributed` decorator is distributed training of a [Two-Tower Recommendation Model](/concepts/two-tower-recommendation-model.md) using TorchRec and PyTorch Lightning across 8 H100 GPUs on a single node. The workflow includes: ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

1. Defining the two tower model using `EmbeddingBagCollection` and `MLP` from TorchRec
2. Wrapping the model in a PyTorch Lightning module with BCE loss and AUROC metrics
3. Creating a training function decorated with `@distributed(gpus=8, gpu_type="H100")`
4. Configuring the Lightning `Trainer` with DDP strategy and device count matching the decorator
5. Logging metrics and checkpoints via [MLflow](/concepts/mlflow.md)
6. Registering the trained model for serving

## Related Concepts

- [Serverless GPU](/concepts/serverless-gpu-compute.md) — The compute infrastructure that supports the `@distributed` decorator
- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) — Deep learning framework commonly used with the decorator
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — The parallelization strategy used inside the training function
- TorchRec — PyTorch library for recommendation models
- [Two-Tower Recommendation Model](/concepts/two-tower-recommendation-model.md) — Example model architecture trained with this approach
- [MLflow](/concepts/mlflow.md) — Experiment tracking and model registry integration
- GPU Scheduling — Managing GPU resources for distributed training

## Sources

- distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md

# Citations

1. [distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md](/references/distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws-093d5979.md)
