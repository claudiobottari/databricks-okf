---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 963e427183f12864a7054e0daf870fa05aad8f509681e24e2fd41d8b7258f8d8
  pageDirectory: concepts
  sources:
    - distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - littwotower-lightning-module-wrapping-twotowermodel
    - LLMWT
  citations:
    - file: distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
title: "LitTwoTower: Lightning Module Wrapping TwoTowerModel"
description: A PyTorch Lightning module that wraps the TwoTowerModel with BCE loss, AUROC metrics, and batch transformation from DataFrame rows to TorchRec Batch objects.
tags:
  - pytorch-lightning
  - recommender-systems
  - software-engineering
timestamp: "2026-06-19T10:16:54.178Z"
---

# LitTwoTower: Lightning Module Wrapping TwoTowerModel

**LitTwoTower** is a [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) module that wraps a [TwoTowerModel](/concepts/two-tower-recommendation-model.md) for distributed training of two‑tower recommendation systems. It is designed to work with TorchRec’s `EmbeddingBagCollection` and provides standard training, validation, and optimization hooks compatible with the Lightning `Trainer` API. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Overview

The `LitTwoTower` class inherits from `pl.LightningModule` and encapsulates the following responsibilities:

- **Forward pass:** Accepts a dictionary batch containing user IDs, movie IDs, and labels; transforms the categorical columns into a `KeyedJaggedTensor` (via `_transform_to_torchrec_batch`), passes them through the underlying `TwoTowerModel` to obtain query and candidate embeddings, and computes a dot‑product logit. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]
- **Loss:** Uses `nn.BCEWithLogitsLoss` for binary classification (rating above mean). ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]
- **Metrics:** Tracks `train_auroc` and `val_auroc` using `torchmetrics.classification.AUROC` with a `"binary"` task. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]
- **Optimizer:** Configures a `KeyedOptimizerWrapper` that wraps the two‑tower model parameters with Adam. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]
- **Logging:** Logs training and validation loss and AUROC at step/epoch level with `sync_dist=True` for multi‑GPU support. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Constructor

```python
class LitTwoTower(pl.LightningModule):
    def __init__(
        self,
        two_tower: nn.Module,
        device: torch.device,
        emb_counts: Optional[List[int]],
        cat_cols: List[str],
        lr: float = 1e-3,
    ) -> None:
```

Parameters:
- `two_tower` – An instance of [TwoTowerModel](/concepts/two-tower-recommendation-model.md) (or any `nn.Module` with the same interface).
- `device` – The device on which the model resides.
- `emb_counts` – A list of embedding table sizes (one per categorical column) used during batch transformation.
- `cat_cols` – Names of the categorical columns (e.g., `["userId", "movieId"]`).
- `lr` – Learning rate passed to the optimizer.

The constructor calls `self.save_hyperparameters(ignore=["two_tower", "device"])` so that hyperparameters are automatically tracked by MLflow without storing the model object or device. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Key Methods

### `forward(batch)`

Takes a dictionary with keys `"userId"`, `"movieId"`, and `"label"`. It transforms the batch into a `torchrec.Batch` via `_transform_to_torchrec_batch`, runs the two‑tower model, and returns the dot‑product logit as a 1‑D tensor. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

### `training_step(batch, batch_idx)`

Computes the forward pass, calculates BCE loss, updates the training AUROC metric, and logs `train_loss` (on‑step and on‑epoch) and `train_auroc` (on‑epoch) using `sync_dist=True`. Returns the loss tensor. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

### `validation_step(batch, batch_idx)`

Similar to `training_step` but logs `val_loss` and `val_auroc` at epoch level only. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

### `configure_optimizers()`

Returns a `KeyedOptimizerWrapper` (from TorchRec) that wraps `self.two_tower.named_parameters()` with `torch.optim.Adam` at the configured learning rate. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

### `_transform_to_torchrec_batch(batch, num_embeddings_per_feature)`

Converts a dictionary batch (with raw integer IDs) into a `torchrec.Batch`. For each categorical column, it takes the modulo of the ID with the embedding table size (to ensure indices are within bounds), builds a `KeyedJaggedTensor` with length‑1 sequences, and returns a `Batch` object containing `dense_features`, `sparse_features`, and `labels`. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Usage in Distributed Training

`LitTwoTower` is typically used with the PyTorch Lightning `Trainer` and the Databricks serverless GPU `@distributed` decorator to train across multiple GPUs. In the example notebook, the training function uses `strategy="ddp"` and `devices=8` on H100 GPUs. The `LitTwoTower` module is created by `create_two_tower_model()` which instantiates `EmbeddingBagConfig`s, an `EmbeddingBagCollection`, a base `TwoTowerModel`, and wraps it with `LitTwoTower`. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Related Concepts

- [TwoTowerModel](/concepts/two-tower-recommendation-model.md) – The underlying neural network that computes query and candidate embeddings.
- TorchRec – A PyTorch library for large‑scale recommendation systems, providing `EmbeddingBagCollection` and `KeyedJaggedTensor`.
- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) – The framework that `LitTwoTower` extends.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – The strategy used in the example for multi‑GPU training.
- MLflow Logging – Integrated through `MLFlowLogger` and `mlflow.pytorch.autolog()`.
- AUROC – The evaluation metric used in `LitTwoTower`.
- KeyedOptimizerWrapper – A TorchRec optimizer wrapper used for parameter‑keyed optimization.

## Sources

- distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md

# Citations

1. [distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md](/references/distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws-093d5979.md)
