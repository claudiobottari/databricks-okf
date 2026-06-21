---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c0e22593885942aa264a273a512381e6a7f8d8a8652564c17edc2047dbb44e5b
  pageDirectory: concepts
  sources:
    - distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lightningmodule-with-auroc-metrics-for-recommendation
    - LWAMFR
  citations:
    - file: distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
title: LightningModule with AUROC Metrics for Recommendation
description: Using PyTorch Lightning's LightningModule pattern with torchmetrics AUROC to encapsulate training, validation, and logging for binary relevance prediction in recommender systems.
tags:
  - pytorch-lightning
  - evaluation
  - recommender-systems
timestamp: "2026-06-19T18:35:05.314Z"
---

#LightningModule with AUROC Metrics for Recommendation

**LightningModule with AUROC Metrics for Recommendation** refers to a design pattern that uses the [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) `LightningModule` together with AUROC metrics from TorchMetrics to train and evaluate a [Two-Tower Recommendation Model](/concepts/two-tower-recommendation-model.md). This approach simplifies distributed training on multiple GPUs while providing interpretable binary classification metrics.

## Overview

The pattern is demonstrated in a Databricks notebook that trains a two-tower recommendation model on the Learning from Sets dataset. The model is implemented as a `pl.LightningModule` subclass named `LitTwoTower` and uses `torchmetrics.classification.AUROC` to compute the Area Under the Receiver Operating Characteristic curve for both training and validation phases. The binary classification task is derived from binarised user-item ratings. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Key Components

### LightningModule (`LitTwoTower`)

`LitTwoTower` is a `pl.LightningModule` that wraps a `TwoTowerModel` — a neural network composed of two embedding towers (query and candidate) built with TorchRec components. The module defines:

- **`forward`**: Accepts a batch dictionary, transforms it into a TorchRec `Batch`, computes query and candidate embeddings, and returns logits from the dot product of the two embeddings. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]
- **`training_step`**: Calls `forward`, computes a BCEWithLogitsLoss loss, updates the training AUROC metric, and logs `train_loss` (per step and per epoch) and `train_auroc` (per epoch). ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]
- **`validation_step`**: Similar to `training_step`, but logs `val_loss` and `val_auroc` only at the epoch level. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]
- **`configure_optimizers`**: Sets up a `KeyedOptimizerWrapper` wrapping `torch.optim.Adam` for the model parameters. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

The `save_hyperparameters` method is called, ignoring the model and device arguments, to automatically log hyperparameters to MLflow. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

### AUROC Metrics

Two instances of `AUROC(task="binary")` are created in `__init__`:

- `self.train_auroc` — updated in `training_step`.
- `self.val_auroc` — updated in `validation_step`.

Both metrics are logged using `self.log` with `sync_dist=True` to ensure correct aggregation across GPUs in [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) training. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Training Configuration

The training configuration is defined in a dataclass `Args` with parameters:

- `epochs`: number of training epochs (default 3).
- `embedding_dim`: dimension of the embedding vectors (default 128).
- `layer_sizes`: hidden layer sizes for the MLP projections (default `[128, 64]`).
- `learning_rate`: optimizer learning rate (default 0.01).
- `batch_size`: minibatch size (default 1024). ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

The dataset is split into 70% training, 21% validation, and 9% test sets. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Distributed Training Strategy

The training is launched using the `@distributed` decorator from the `serverless_gpu` library on a single node with eight H100 GPUs. The PyTorch Lightning Trainer is configured with:

- `accelerator="gpu"`
- `strategy="ddp"` (Distributed Data Parallel)
- `devices=8`

The `training_function` decorated with `@distributed(gpus=8, gpu_type="H100")` creates the model, dataloaders, callbacks, and trainer, then calls `trainer.fit()`. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

### Callbacks

Three callbacks are used:

- `LearningRateMonitor`: logs learning rate at each step.
- `DeviceStatsMonitor`: records device resource usage.
- `ModelCheckpoint`: saves the best model based on `val_auroc` (higher is better, `mode="max"`) and keeps the last checkpoint. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Model Evaluation and Checkpointing

After training, the best checkpoint is selected by searching logged models ordered by `metrics.accuracy` (the source uses `accuracy` in `search_logged_models`, but the checkpoint is monitored on `val_auroc`). The best model is loaded from MLflow and tested on a small number of test batches. Predictions are passed through `torch.sigmoid` to obtain probabilities. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Serving and Registration

To simplify serving, the model is wrapped in a custom [MLflow PythonModel](/concepts/custom-mlflow-pythonmodel.md) called `TwoTowerWrapper`. This wrapper accepts a dictionary of lists and returns a list of sigmoid scores, hiding the TorchRec batch transformations. An MLflow signature and input example are inferred, and the model is registered to the Unity Catalog model registry under `<catalog>.<schema>.two_tower_model`. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Related Concepts

- [Two-Tower Recommendation Model](/concepts/two-tower-recommendation-model.md)
- PyTorch Lightning Trainer
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- TorchMetrics AUROC
- [TorchRec EmbeddingBagCollection](/concepts/torchrec-embeddingbagcollection.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- MLflow PyFunc Model

## Sources

- distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md

# Citations

1. [distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md](/references/distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws-093d5979.md)
