---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 88505abe4e42341efa6233d47d2cadf816d87f321b7c6fb6d6f7947c37911ed9
  pageDirectory: concepts
  sources:
    - distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pytorch-lightning-trainer-for-distributed-training
    - PLTFDT
  citations:
    - file: distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
title: PyTorch Lightning Trainer for Distributed Training
description: Using Lightning's Trainer API with DDP strategy to distribute two-tower model training across multiple GPUs.
tags:
  - distributed-training
  - pytorch-lightning
  - deep-learning
timestamp: "2026-06-19T10:16:36.580Z"
---

Here is the wiki page for "PyTorch Lightning Trainer for Distributed Training", written based solely on the provided source material.

---

# PyTorch Lightning Trainer for Distributed Training

**PyTorch Lightning Trainer for Distributed Training** refers to the use of PyTorch Lightning's `Trainer` API to orchestrate distributed training across multiple GPUs. The `Trainer` abstracts away the complexities of distributed computing, enabling scalable training workflows for deep learning models, particularly in the context of large-scale recommendation systems and other GPU-intensive tasks.

## Overview

The PyTorch Lightning `Trainer` provides a high-level interface for managing the training loop, including automatic handling of device placement, gradient accumulation, checkpointing, and logging. For distributed training, the `Trainer` supports various strategies, most notably [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md), which synchronizes gradients across multiple GPUs during each training step. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Key Concepts

### The Trainer API

The `Trainer` is the core orchestrator in PyTorch Lightning. It manages the entire training lifecycle, abstracting away low-level operations like loop construction, device management, and logging. Users define their model as a `LightningModule` and pass it to the `Trainer`, which handles the rest. Common configuration parameters include `max_epochs`, `accelerator`, `devices`, and `strategy`. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

```python
trainer = Trainer(
    max_epochs=3,
    accelerator="gpu",
    strategy="ddp",
    devices=8,
    log_every_n_steps=20,
    logger=mlflow_logger,
    callbacks=callbacks,
)
```

### DDP Strategy for Multi-GPU Training

The `strategy="ddp"` argument configures the `Trainer` to use Distributed Data Parallel, where each GPU maintains its own copy of the model and processes a subset of the batch. Gradients are synchronized across all devices after each forward-backward pass. This strategy is well-suited for models that fit within a single GPU's memory but require faster training through data parallelism. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Distributed Training on Databricks Serverless GPU

### Infrastructure Setup

On Databricks, distributed training with PyTorch Lightning can be launched on serverless GPU compute using the `@distributed` decorator from the `serverless_gpu` Python library. This decorator handles GPU allocation and distribution across multiple accelerators. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

```python
from serverless_gpu import distributed

@distributed(gpus=8, gpu_type="H100")
def training_function(args, cat_cols, emb_counts, device, train_data, val_data, checkpoint_path):
    # Model creation, dataloader setup, Trainer configuration
    trainer = Trainer(
        max_epochs=args.epochs,
        accelerator="gpu",
        strategy="ddp",
        devices=8,
        log_every_n_steps=20,
        logger=mlflow_logger,
        callbacks=callbacks,
    )
    trainer.fit(model, train_dataloaders=train_dataloader, val_dataloaders=eval_dataloader)
    return result
```

To use this infrastructure, configure the notebook to use a serverless GPU compute with the appropriate accelerator (e.g., **8xH100**) and environment (e.g., **AI v5**). ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

### Device Management

The `Trainer` automatically manages device placement. When configured with `accelerator="gpu"` and `devices=8`, it distributes the model across all eight GPUs. The `DeviceStatsMonitor` callback can be used to track GPU resource utilization during training. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Callbacks for Distributed Training

PyTorch Lightning callbacks provide hooks into the training lifecycle. Commonly used callbacks in distributed settings include:

- **`ModelCheckpoint`**: Saves model checkpoints based on monitored metrics (e.g., `val_auroc`) and can save both the best and last model state. With `save_last=True`, it enables easy retrieval of the final checkpoint. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]
- **`LearningRateMonitor`**: Logs the learning rate at specified intervals for debugging and visualization. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]
- **`DeviceStatsMonitor`**: Tracks GPU memory usage and other device statistics during training. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

```python
ckpt_cb = ModelCheckpoint(
    dirpath=checkpoint_path,
    monitor="val_auroc",
    mode="max",
    save_top_k=1,
    save_last=True,
    filename="{epoch}-{val_auroc:.4f}",
)

callbacks = [
    LearningRateMonitor(logging_interval="step"),
    DeviceStatsMonitor(),
    ckpt_cb,
]
```

## Logging with MLflow

The `MLFlowLogger` integrates MLflow tracking with PyTorch Lightning, automatically logging metrics, parameters, and model artifacts. When combined with `mlflow.pytorch.autolog()`, training metrics such as loss and AUROC are tracked across distributed workers. The `Trainer` also exposes the MLflow `run_id` for post-training analysis and model registration. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

```python
mlflow_logger = MLFlowLogger(
    experiment_name=experiment_path,
    log_model="all",
)

# Retrieving run ID after training
run_id = trainer.logger.run_id
```

## Metric Synchronization in Distributed Settings

When using DDP, each GPU calculates metrics independently. To ensure consistent logging across all devices, use `sync_dist=True` in the `self.log()` calls within the `LightningModule`. This synchronizes metrics across all processes before logging. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

```python
self.log("val_loss", loss, on_step=False, on_epoch=True, prog_bar=True, logger=True, sync_dist=True)
self.log("val_auroc", self.val_auroc, on_step=False, on_epoch=True, prog_bar=True, logger=True, sync_dist=True)
```

## Model Registration and Serving

After distributed training, the trained model can be registered to MLflow for serving. A common pattern is to wrap the PyTorch Lightning model in a `PythonModel` (PyFunc) that provides a simplified inference interface. This wrapper handles input preprocessing and output transformation, making the model deployable through MLflow Model Serving. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

```python
class TwoTowerWrapper(PythonModel):
    def predict(self, model_input: Dict[str, List]) -> List[float]:
        batch = {key: torch.tensor(value) for key, value in model_input.items()}
        with torch.no_grad():
            output = self.two_tower_model(batch).cpu()
        output = torch.sigmoid(output)
        return output.tolist()
```

## Best Practices

- **Use the `@distributed` decorator** for automatic GPU allocation on Databricks serverless GPU infrastructure. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]
- **Enable autologging** with `mlflow.pytorch.autolog()` to capture all training metrics without manual instrumentation. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]
- **Configure checkpointing** with `save_last=True` to always have a recoverable checkpoint, and monitor a validation metric to save the best model. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]
- **Use `sync_dist=True`** in metric logging calls when training with DDP to ensure accurate aggregate metrics. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]
- **Set up MLflow experiment tracking** before training to enable experiment comparison and model lineage. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Related Concepts

- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) — The framework providing the `Trainer` and `LightningModule` abstractions
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — The distributed strategy commonly used with the Lightning Trainer
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Experiment logging and model registry integration
- [Serverless GPU on Databricks](/concepts/serverless-gpu-compute-on-databricks.md) — The compute infrastructure for multi-GPU training
- Model Checkpointing — Saving and restoring model state during training
- [Two-Tower Recommendation Model](/concepts/two-tower-recommendation-model.md) — An example model architecture trained with the Lightning Trainer

## Sources

- distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md

# Citations

1. [distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md](/references/distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws-093d5979.md)
