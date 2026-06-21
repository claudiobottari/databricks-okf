---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 53524f9894ba9dee77e6efcdc989c39bd000fa63d7ffeed8961f2d6f6e69c266
  pageDirectory: concepts
  sources:
    - distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-serverless-gpu-compute-configuration
    - DSGCC
  citations:
    - file: distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
title: Databricks Serverless GPU Compute Configuration
description: The workflow to configure a Databricks notebook with serverless GPU compute, including selecting accelerator type (8xH100) and environment (AI v5)
tags:
  - databricks
  - infrastructure
  - gpu-computing
timestamp: "2026-06-18T15:31:29.725Z"
---

# Databricks Serverless GPU Compute Configuration

**Databricks Serverless GPU Compute Configuration** refers to the process of setting up and managing serverless GPU compute resources within Databricks for running deep learning and machine learning workloads. Serverless GPU compute provides on-demand GPU acceleration without the need to manage physical or virtual clusters, enabling scalable training and inference for models ranging from recommendation systems to large language models.

## Overview

Serverless GPU compute in Databricks allows users to run GPU-accelerated workloads without provisioning or managing clusters. The compute is automatically scaled and configured based on workload requirements. Users select an accelerator type (GPU specification), an environment (AI runtime version), and the number of GPUs needed, and Databricks handles the underlying infrastructure. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Key Configuration Options

### Accelerator Selection

When configuring serverless GPU compute, users select the specific GPU type for their workload. Available accelerators include NVIDIA H100, A100, and other supported GPU types. The choice of accelerator depends on the model size, training complexity, and performance requirements. For example, training a [Two-Tower Recommendation Model](/concepts/two-tower-recommendation-model.md) may use 8xH100 GPUs for distributed training. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

### Environment Selection

The **environment** determines the pre-installed libraries and runtime version available for the compute session. Databricks offers AI-optimized environments that include popular deep learning frameworks. For instance, the **AI v5** environment provides libraries like PyTorch, TensorFlow, and MLflow, with additional packages installable via `%pip` commands. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

### Number of GPUs

Users specify the number of GPUs for distributed training. Common configurations include 8 GPUs on a single node. The `serverless_gpu` Python library provides a `@distributed` decorator that handles launching training across all specified GPUs using strategies like [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md). ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Configuration Steps

### Configuring via the Notebook UI

1. Click the **Connect** dropdown at the top of the notebook to open the compute selector.
2. Select **Serverless GPU** as the compute type.
3. Open the **Environment** panel on the right side.
4. Select the desired accelerator (e.g., **8xH100**).
5. Select the environment version (e.g., **AI v5**).
6. Click **Apply**, then **Confirm**.

After configuration, the notebook connects to serverless GPU compute and is ready for distributed training. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Distributed Training with the `@distributed` Decorator

The `serverless_gpu` library provides the `@distributed` decorator to simplify launching distributed training across multiple GPUs. The decorator accepts parameters for the number of GPUs and GPU type.

```python
from serverless_gpu import distributed

@distributed(gpus=8, gpu_type="H100")
def training_function(args, cat_cols, emb_counts, device, train_data, val_data, checkpoint_path):
    # Training logic using PyTorch Lightning Trainer
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

result = training_function.distributed()
```

The decorator automatically distributes the training function across the specified number of GPUs. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Integration with MLflow

Serverless GPU compute integrates with [MLflow](/concepts/mlflow.md) for experiment tracking, model logging, and model registry. When training with PyTorch Lightning, users enable `mlflow.pytorch.autolog()` for automatic metric logging. The `MLFlowLogger` can be configured in the PyTorch Lightning `Trainer` to log runs to a specific experiment path. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

```python
import mlflow

username = spark.sql("SELECT current_user()").first()['current_user()']
experiment_path = f'/Users/{username}/sgc-torchrec-example'
experiment = mlflow.set_experiment(experiment_path)
os.environ["MLFLOW_EXPERIMENT_NAME"] = experiment_path

mlflow_logger = MLFlowLogger(
    experiment_name=experiment_path,
    log_model="all",
)
```

## GPU Availability and Considerations

### Capacity Planning

High-demand GPU types like [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) typically have limited capacity in cloud environments. Databricks recommends contacting your cloud provider for resource allocation or reserving capacity in advance for workloads requiring specific GPU types. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Package Installation

While AI environments include many common libraries, additional packages may need to be installed using `%pip install`. The serverless GPU compute supports custom package installation, and `dbutils.library.restartPython()` can be called after installation to refresh the Python environment. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Best Practices

- **Select appropriate GPU type**: Match the GPU type to the workload size. Smaller models may run efficiently on fewer GPUs or lower-spec accelerators.
- **Use environment-optimized runtimes**: AI-optimized environments include pre-configured deep learning frameworks and reduce setup time.
- **Enable MLflow autologging**: Use `mlflow.pytorch.autolog()` or equivalent for automatic tracking of metrics, parameters, and models.
- **Configure model checkpointing**: Set up `ModelCheckpoint` callbacks in PyTorch Lightning to save the best and last model states during training.
- **Register models for serving**: After training, wrap models with `PythonModel` and use `mlflow.register_model()` to register models for production serving.

## Related Concepts

- GPU Scheduling — Optimizing GPU utilization for distributed training
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Training models across multiple GPUs and nodes
- PyTorch Lightning Trainer — The training framework used in serverless GPU compute
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — Registering and managing trained models
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Advanced distributed training strategy for large models
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — Pre-built runtime with GPU support

## Sources

- distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md

# Citations

1. [distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md](/references/distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws-093d5979.md)
2. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
