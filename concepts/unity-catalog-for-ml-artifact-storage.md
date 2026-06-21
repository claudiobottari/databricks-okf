---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c32d1b26d06d94e8055e644d2d740b44f5085363a9d05a05a087a182577e2d93
  pageDirectory: concepts
  sources:
    - distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-for-ml-artifact-storage
    - UCFMAS
  citations:
    - file: distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
title: Unity Catalog for ML Artifact Storage
description: Using Databricks Unity Catalog volumes as a storage location for saving and versioning machine learning artifacts such as model checkpoints, enabling integration with catalog-level access control and governance.
tags:
  - databricks
  - mlops
  - storage
timestamp: "2026-06-19T10:20:10.565Z"
---

# Unity Catalog for ML Artifact Storage

**Unity Catalog for ML Artifact Storage** refers to the use of Databricks' Unity Catalog as a centralized repository for storing, governing, and tracking machine learning artifacts — including trained models, distributed checkpoints, and experiment outputs. By leveraging Unity Catalog volumes and the [Unity Catalog Model Registry](/concepts/unity-catalog-model-registry.md), teams can apply unified governance, access control, versioning, and lineage tracking across their ML assets. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## How It Works

Unity Catalog integrates with [MLflow](/concepts/mlflow.md) to log and store ML artifacts. During distributed training (e.g., with [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) on serverless GPU compute), model checkpoints are saved to a Unity Catalog volume, and the final model is registered in the Unity Catalog model registry. Checkpoints are automatically logged as MLflow artifacts for versioning and reproducibility. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

### Configuring Locations

A user must specify the Unity Catalog catalog, schema, volume, and model name to define where artifacts are stored. This is typically done at the start of a training notebook using widgets or configuration variables. The checkpoint directory path follows the standard Unity Catalog volume path format. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

```python
dbutils.widgets.text("uc_catalog", "main")
dbutils.widgets.text("uc_schema", "default")
dbutils.widgets.text("model_name", "transformer_fsdp")
dbutils.widgets.text("uc_volume", "checkpoints")
UC_CATALOG = dbutils.widgets.get("uc_catalog")
UC_SCHEMA = dbutils.widgets.get("uc_schema")
UC_VOLUME = dbutils.widgets.get("uc_volume")
MODEL_NAME = dbutils.widgets.get("model_name")
UC_MODEL_NAME = f"{UC_CATALOG}.{UC_SCHEMA}.{MODEL_NAME}"
```

The checkpoint directory path is constructed as `/Volumes/{UC_CATALOG}/{UC_SCHEMA}/{UC_VOLUME}/{MODEL_NAME}`. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

### Saving and Logging Artifacts

During training, after each set of batches, the model state is saved as a distributed checkpoint to the Unity Catalog volume using PyTorch's distributed checkpoint API. The checkpoint artifacts are then logged to the active [MLflow Run](/concepts/mlflow-run.md) via `mlflow.log_artifacts()`, ensuring they are tracked alongside metrics and parameters. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

```python
dcp.save(state_dict, storage_writer=writer, checkpoint_id=f"{CHECKPOINT_DIR}/step{batch_idx}")
mlflow.log_artifacts(f'{CHECKPOINT_DIR}/step{batch_idx}', artifact_path=f'checkpoints/step{batch_idx}')
```

## Requirements

To use Unity Catalog for artifact storage, the user must have the `USE CATALOG` and `USE SCHEMA` privileges on the specified [Catalog and Schema](/concepts/catalog-and-schema.md). The Unity Catalog volume must exist and be accessible for writing checkpoints. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Benefits

- **Centralized Governance** – All ML artifacts are stored in Unity Catalog, inheriting its fine-grained access controls, audit logging, and data lineage. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]
- **Reproducibility** – Checkpoints are versioned as MLflow artifacts, and models are registered in the Unity Catalog model registry with full provenance. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]
- **Seamless Integration** – The storage path uses Unity Catalog's volume location, making it easy to reference artifacts across notebooks, jobs, and serving endpoints. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]
- **Unified Experience** – ML artifacts coexist with other governed data assets (tables, files, models) within the same Unity Catalog namespace, enabling consistent discovery and access patterns. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Use Cases

### Distributed Training Checkpointing

In distributed training workflows using PyTorch FSDP on serverless GPU compute, checkpoints are saved periodically to Unity Catalog volumes during training. These checkpoints capture the full distributed state (model parameters, gradients, optimizer states) across all workers and can be loaded later for inference or continued training. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

### Experiment Tracking with MLflow

By logging checkpoint artifacts to MLflow runs, practitioners can associate specific checkpoints with training runs, hyperparameters, and performance metrics. This creates a full audit trail of model development. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

### Model Registration and Deployment

After training completes, models can be registered in the Unity Catalog model registry from the stored artifacts, enabling controlled promotion through staging and production environments. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The underlying governance platform.
- Unity Catalog Volumes – The storage layer used for checkpoint artifacts.
- [Unity Catalog Model Registry](/concepts/unity-catalog-model-registry.md) – For registering and versioning models.
- [MLflow](/concepts/mlflow.md) – The experiment tracking and artifact logging framework.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – The compute environment where distributed training runs.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – The training paradigm that produces these artifacts.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – A common distributed training strategy that benefits from UC artifact storage.
- Checkpointing – The practice of saving model state during training for fault tolerance and reproducibility.
- [ABAC GRANT Policies](/concepts/abac-grant-policy.md) – For dynamically controlling access to registered models.
- [ABAC Column Mask Policies](/concepts/abac-column-mask-policy.md) – For governing sensitive data used in ML pipelines.

## Sources

- distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md

# Citations

1. [distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md](/references/distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws-e728aa55.md)
