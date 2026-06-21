---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 58403a096bde0dbfb9f973b3206948548e659ee3526d379a2398874bcf68ebb3
  pageDirectory: concepts
  sources:
    - image-classification-using-convolutional-neural-networks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-volumes-for-model-checkpointing
    - UCVFMC
  citations:
    - file: image-classification-using-convolutional-neural-networks-databricks-on-aws.md
title: Unity Catalog Volumes for Model Checkpointing
description: Using Unity Catalog Volumes to store and load PyTorch model checkpoints via paths like /Volumes/{catalog}/{schema}/{volume}/{model_name}, integrated with torch.distributed.checkpoint.
tags:
  - databricks
  - unity-catalog
  - checkpointing
  - storage
timestamp: "2026-06-19T19:08:52.651Z"
---

# Unity Catalog Volumes for Model Checkpointing

**Unity Catalog Volumes for Model Checkpointing** refers to the practice of using [Unity Catalog](/concepts/unity-catalog.md) Volumes as persistent storage locations for saving and loading model checkpoints during training workflows on Databricks. This approach enables structured, catalog-based checkpoint management that integrates with Databricks' governance and discovery capabilities.

## Overview

When training deep learning models, checkpointing is critical for saving model state periodically so that training can be resumed from a specific point in case of interruption or for evaluation purposes. [Unity Catalog](/concepts/unity-catalog.md) Volumes provide a governed storage layer that can be used to store these checkpoints. The checkpoint path follows a standard format: `/Volumes/{uc_catalog}/{uc_schema}/{uc_volume}/{uc_model_name}`.^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

## Configuration

To use Unity Catalog Volumes for checkpointing, you first configure the storage location using widget parameters or environment variables that specify:

- **Catalog**: The Unity Catalog catalog name
- **Schema**: The schema (database) within the catalog
- **Volume**: The volume dedicated to storing checkpoint files
- **Model name**: A subdirectory within the volume for the specific model

These values construct the full checkpoint path used throughout the training workflow. The volume directory must exist before training begins.^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

## Checkpointing with PyTorch Distributed Checkpoint (DCP)

For PyTorch workflows, checkpoints can be saved and loaded using [PyTorch Distributed Checkpoint (DCP)](/concepts/pytorch-distributed-checkpoint-dcp.md). This approach supports both single-GPU and distributed training scenarios. The recommended pattern involves creating an `AppState` wrapper class that implements the `Stateful` protocol, which automatically handles state dictionary management for both model and optimizer states.^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

### Saving Checkpoints

Checkpoints are saved using `dcp.save()` with a state dictionary containing the `AppState` object. This is typically done after each training epoch to capture the most recent model and optimizer states.^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

### Loading Checkpoints

To resume training or evaluate a model, checkpoints are loaded using `dcp.load()` with the same checkpoint path. The `AppState.load_state_dict()` method restores the model and optimizer to their saved states.^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

## Benefits

Using Unity Catalog Volumes for checkpointing provides several advantages:

- **Governed storage**: Checkpoints are stored within Unity Catalog's governance framework, enabling access control and data lineage
- **Centralized management**: All model checkpoints are organized within a single catalog structure
- **Discovery**: Checkpoints can be discovered and accessed through Unity Catalog interfaces
- **Resumability**: Training can be interrupted and resumed from the latest checkpoint without losing progress

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance and metadata layer for Databricks assets
- Model Checkpointing — General concepts and best practices for saving model state
- [PyTorch Distributed Checkpoint (DCP)](/concepts/pytorch-distributed-checkpoint-dcp.md) — The PyTorch API for distributed checkpointing
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — Compute infrastructure compatible with Unity Catalog volume checkpoints
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Experiment tracking that can be used alongside volume-based checkpointing

## Sources

- image-classification-using-convolutional-neural-networks-databricks-on-aws.md

# Citations

1. [image-classification-using-convolutional-neural-networks-databricks-on-aws.md](/references/image-classification-using-convolutional-neural-networks-databricks-on-aws-0a8afbcf.md)
