---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7ac948c9693cd56de476741b7e33447e553a8d2bcc358820608592691621ae37
  pageDirectory: concepts
  sources:
    - distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-integration-for-model-storage
    - UCIFMS
  citations:
    - file: distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
title: Unity Catalog Integration for Model Storage
description: Using Databricks Unity Catalog catalogs, schemas, and volumes to store model checkpoints and artifacts, requiring USE CATALOG and USE SCHEMA privileges.
tags:
  - databricks
  - storage
  - mlops
timestamp: "2026-06-19T18:36:41.892Z"
---

# Unity Catalog Integration for Model Storage

**Unity Catalog Integration for Model Storage** refers to the capability to store and manage machine learning model checkpoints, artifacts, and registered models within [Unity Catalog](/concepts/unity-catalog.md) on Databricks. This integration enables centralized governance, lineage tracking, and access control for model artifacts across workspaces.

## Overview

Unity Catalog provides a unified governance layer for data and AI assets. When integrated with model storage, it allows models and their associated checkpoints to be stored in managed locations within Unity Catalog, including catalogs, schemas, and volumes. This integration ensures that model artifacts benefit from the same access control, auditing, and discovery features as other data assets. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Key Components

### Unity Catalog Volumes for Checkpoints

Model checkpoints from distributed training can be saved directly to Unity Catalog volumes. During [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) training, checkpoints are written to a path within a Unity Catalog volume, which provides persistent, governed storage accessible across the Databricks environment. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

The checkpoint directory path follows the pattern:

```
/Volumes/{catalog}/{schema}/{volume}/{model_name}
```

^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

### Unity Catalog Registered Models

Models can be registered in Unity Catalog using a fully qualified three-level name that includes the catalog, schema, and model name:

```
{catalog}.{schema}.{model_name}
```

^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Configuration Requirements

To use Unity Catalog for model storage, users must have appropriate privileges:

- `USE CATALOG` privilege on the specified catalog
- `USE SCHEMA` privilege on the specified schema

These privileges are required to write checkpoints to volumes and register models in Unity Catalog. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Integration with Distributed Training

During distributed training with FSDP on [Serverless GPU Compute](/concepts/serverless-gpu-compute.md), checkpoints are saved to Unity Catalog volumes and logged as [MLflow](/concepts/mlflow.md) artifacts. This provides:

- **Versioning**: Checkpoints are tracked as MLflow artifacts for reproducibility
- **Governance**: Model artifacts inherit Unity Catalog access controls
- **Lineage**: Training runs are linked to their output artifacts

The checkpoint saving process uses PyTorch's distributed checkpoint API (`torch.distributed.checkpoint`) to write state dictionaries containing model weights and optimizer states to the Unity Catalog volume path. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Loading Checkpoints from Unity Catalog

Checkpoints stored in Unity Catalog volumes can be loaded for inference or continued training. When loading outside a distributed training context (without an initialized process group), PyTorch's distributed checkpoint API automatically disables collective operations and loads the checkpoint on a single device. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer for data and AI assets
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Distributed training strategy that benefits from Unity Catalog checkpoint storage
- [MLflow](/concepts/mlflow.md) — Experiment tracking and model registry integration
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — Compute infrastructure for distributed training
- [Model Registry](/concepts/mlflow-model-registry.md) — Version management for registered models
- Data Governance — Access control and auditing for model artifacts

## Sources

- distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md

# Citations

1. [distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md](/references/distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws-e728aa55.md)
