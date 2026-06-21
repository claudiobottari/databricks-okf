---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 067aaabf6acd4cafd42faf61174213ebfdba39d74a070525b820e419ba68a850
  pageDirectory: concepts
  sources:
    - distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pytorch-lightning-with-torchrec-for-distributed-training
    - PLWTFDT
  citations:
    - file: distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
title: PyTorch Lightning with TorchRec for Distributed Training
description: Combining PyTorch Lightning's Trainer API with TorchRec's embedding modules for scalable, multi-GPU training of recommendation models using DDP strategy.
tags:
  - machine-learning
  - distributed-training
  - pytorch
timestamp: "2026-06-19T18:34:22.620Z"
---

# PyTorch Lightning with TorchRec for Distributed Training

**PyTorch Lightning with TorchRec for Distributed Training** is an approach to building and training large-scale recommendation models – specifically [Two-Tower Recommendation Model](/concepts/two-tower-recommendation-model.md)s – by combining the high-level training interface of [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) with the embedding and sparse‑feature infrastructure of TorchRec. This combination allows developers to write scalable, multi‑GPU training code that runs on [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) hardware using Databricks Serverless GPU compute. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Overview

The pattern demonstrated in the Databricks example notebook uses the `pytorch_lightning.Trainer` API to orchestrate training, validation, checkpointing, and logging. TorchRec provides the building blocks for handling large categorical feature embeddings: `EmbeddingBagConfig`, `EmbeddingBagCollection`, `KeyedJaggedTensor`, and `KeyedOptimizerWrapper`. The model is a two‑tower architecture (query tower and candidate tower) that learns separate embeddings for users and items, then computes a similarity score. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

Distributed training across multiple GPUs is achieved through the `@distributed` decorator from the `serverless_gpu` Python library. When applied to the training function, the decorator launches the function on 8 H100 GPUs (single node) and automatically handles process coordination. Inside the function, the Lightning `Trainer` is configured with `strategy="ddp"` and `devices=8`, enabling [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) training. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Key Components

### 1. Environment Setup

The notebook is attached to **Serverless GPU** compute with the **8xH100** accelerator and the **AI v5** environment. Additional packages (`torchrec`, `fbgemm-gpu`, `torchaudio`) are installed via `%pip`. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

### 2. Dataset and Preprocessing

The example uses the [Learning from Sets](https://files.grouplens.org/datasets/learning-from-sets-2019/) dataset. The data is sorted, user IDs are encoded, ratings are binarised (≥ mean → 1, else 0), and the dataset is split 70/21/9 into train/validation/test. A custom `RecDataset` class wraps the DataFrame, and `get_dataloader` creates standard PyTorch `DataLoader`s. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

### 3. Model Definition

The model comprises two parts:

- **`TwoTowerModel`** (a `nn.Module`): accepts an `EmbeddingBagCollection` and two MLP projections. In the forward pass, it pools embeddings for query and candidate features, then projects each tower through its own MLP.
- **`LitTwoTower`** (a `pl.LightningModule`): wraps the `TwoTowerModel`, defines the loss function (`BCEWithLogitsLoss`), training/validation steps, metric computation (`AUROC`), and optimiser configuration using `KeyedOptimizerWrapper`. It also includes a helper method `_transform_to_torchrec_batch` that converts a dictionary batch into a TorchRec `Batch` object with a `KeyedJaggedTensor` for sparse features. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

### 4. Distributed Training Function

The core training function is decorated with `@distributed(gpus=8, gpu_type="H100")`. Inside the function:

- The model is created on the current device.
- [MLflow Autologging](/concepts/mlflow-autologging.md) is enabled.
- A Lightning `Trainer` is instantiated with `accelerator="gpu"`, `strategy="ddp"`, `devices=8`, and callbacks for learning‑rate monitoring, device statistics, and model checkpointing.
- `trainer.fit()` is called, after which the function returns the [MLflow Run](/concepts/mlflow-run.md) ID and checkpoint paths. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

### 5. Inference and Model Registration

After training, the best checkpoint is loaded and tested on a few batches. The model is then wrapped in an MLflow `PythonModel` (called `TwoTowerWrapper`) that takes dictionary input and returns list outputs. A model signature is inferred and the model is logged to MLflow, then registered in Unity Catalog under `<catalog>.<schema>.two_tower_model`. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Benefits

- **Abstraction**: PyTorch Lightning handles the training loop, logging, and DDP boilerplate, while TorchRec handles embedding management and optimiser keying.
- **Scalability**: The `@distributed` decorator transparently launches the training on all 8 H100 GPUs, making it easy to scale without manual process management.
- **Modularity**: The two‑tower architecture cleanly separates query and candidate towers, making the model suitable for retrieval‑style recommendation systems.

## Related Concepts

- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md)
- TorchRec
- [Two-Tower Recommendation Model](/concepts/two-tower-recommendation-model.md)
- [EmbeddingBagCollection](/concepts/torchrec-embeddingbagcollection.md)
- KeyedJaggedTensor
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [MLflow](/concepts/mlflow.md)

## Sources

- distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md

# Citations

1. [distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md](/references/distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws-093d5979.md)
