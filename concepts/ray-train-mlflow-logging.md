---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9da8b3ad2ef5e0d586a8dba580caed09c7d7736b5af7689fc5b8324a8cf9f77a
  pageDirectory: concepts
  sources:
    - integrate-mlflow-and-ray-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-train-mlflow-logging
    - RTML
    - Ray Tune MLflow Logging
  citations:
    - file: integrate-mlflow-and-ray-databricks-on-aws.md
title: Ray Train MLflow Logging
description: Method for logging Ray Train models to MLflow by reloading from checkpoints and using MLflow model flavors such as PyTorch or TensorFlow.
tags:
  - ray
  - mlflow
  - model-training
timestamp: "2026-06-19T19:11:05.633Z"
---

# Ray Train MLflow Logging

**Ray Train MLflow Logging** refers to the integration pattern for recording models, metrics, and metadata from distributed training runs executed with [Ray Train](/concepts/ray-train-resource-allocation.md) into [MLflow](/concepts/mlflow.md). By combining Ray Train’s distributed training capabilities with MLflow’s experiment tracking, teams can scale their training workloads across multiple GPUs or nodes while maintaining a centralized record of model artifacts and performance. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

## Logging Models from Checkpoints

The simplest and recommended method to log a model trained with Ray Train is to use the **checkpoint** generated at the end of the training run. After the training completes, reload the model in its native deep‑learning framework (e.g., PyTorch or TensorFlow) from the checkpoint, then log it with the appropriate MLflow flavor. This approach ensures the model is stored correctly and is ready for evaluation or deployment. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

```python
result = trainer.fit()
checkpoint = result.checkpoint

with checkpoint.as_directory() as checkpoint_dir:
    # Adjust for your DL framework (e.g., TensorFlow or PyTorch Lightning)
    checkpoint_path = f"{checkpoint_dir}/checkpoint.ckpt"
    model = MyModel.load_from_checkpoint(checkpoint_path)

with mlflow.start_run() as run:
    mlflow.pytorch.log_model(model, "model")
```

If you need to store **multiple models** from a single training run, specify the number of checkpoints to keep in `ray.train.CheckpointConfig`. Each checkpoint can then be read and logged using the same pattern. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

## Logging Training Metrics

Training metrics collected by Ray Train (such as loss and accuracy at each step) are available in the result object’s `metrics_dataframe`. Retrieve this dataframe after fitting and log the metrics to MLflow alongside the model. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

```python
result = trainer.fit()

with mlflow.start_run() as run:
    mlflow.log_metrics(result.metrics_dataframe.to_dict(orient='dict'))
    mlflow.pytorch.log_model(model, "model")
```

## Fault Tolerance and Resource Configuration

MLflow is responsible for tracking the model lifecycle but **does not handle fault tolerance** during training. Fault tolerance (e.g., recovery from node failures) is managed exclusively by Ray Train itself. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

When running [Ray Train](/concepts/ray-train-resource-allocation.md) on Databricks with Spark clusters, you must adjust the `resources_per_worker` setting to prevent resource contention. Specifically, set the number of CPUs for each Ray worker to be **one less** than the total number of CPUs available on a Ray worker node. This reservation ensures that the Ray actor does not occupy all cores, which would cause errors. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

## Related Concepts

- [Ray Train](/concepts/ray-train-resource-allocation.md) – The distributed training framework used to scale model training.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – The component that stores runs, metrics, parameters, and artifacts.
- [CheckpointConfig](/concepts/activation-checkpointing.md) – Ray Train configuration for controlling checkpoint frequency and retention.
- PyTorch MLflow Flavor – The MLflow integration for PyTorch models.
- TensorFlow MLflow Flavor – The MLflow integration for TensorFlow models.
- Ray Tune MLflow Logging – Similar integration for hyperparameter tuning tasks.
- Ray Core MLflow Logging – Logging patterns for general distributed applications.

## Sources

- integrate-mlflow-and-ray-databricks-on-aws.md

# Citations

1. [integrate-mlflow-and-ray-databricks-on-aws.md](/references/integrate-mlflow-and-ray-databricks-on-aws-05a679fb.md)
