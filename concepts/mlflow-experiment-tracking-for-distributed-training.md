---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e38856b7f6b38207ad1639663d50a5c80adccb6bfb202f65cd14a2d3c9cf8e74
  pageDirectory: concepts
  sources:
    - distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-experiment-tracking-for-distributed-training
    - METFDT
  citations:
    - file: distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
title: MLflow Experiment Tracking for Distributed Training
description: Integrating MLflow to log metrics (loss values), artifacts (checkpoints), and run metadata during distributed multi-GPU training sessions for experiment tracking and reproducibility.
tags:
  - mlflow
  - experiment-tracking
  - distributed-training
timestamp: "2026-06-19T10:18:56.929Z"
---

# MLflow Experiment Tracking for Distributed Training

**MLflow Experiment Tracking for Distributed Training** refers to the practice of using MLflow to log metrics, parameters, and artifacts during distributed model training workloads. When training large models across multiple GPUs or nodes, MLflow provides a centralized record of training progress, enabling reproducibility, comparison of runs, and debugging. The example demonstrated in the provided source uses [PyTorch FSDP](/concepts/pytorch-fully-sharded-data-parallel-fsdp.md) on [Databricks Serverless GPU Compute](/concepts/databricks-serverless-gpu-compute.md) with MLflow to track loss metrics and save distributed checkpoints.^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Overview

In a distributed training loop, MLflow is initialized by calling `mlflow.start_run()` with a descriptive run name. Metrics such as loss per batch and average loss per epoch are logged with `mlflow.log_metric()`. At the end of training, `mlflow.end_run()` finalizes the run. This setup ensures that all training metadata is captured in a single experiment for later analysis.^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Key Logged Metrics

The following metrics are logged during training:

- **Per-batch loss**: `mlflow.log_metric(key='loss', value=loss.item(), step=batch_idx)` records the loss value at each training step, allowing detailed visualization of training dynamics.^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]
- **Average epoch loss**: After each epoch, the average loss is computed and logged as `mlflow.log_metric(key='avg_loss', value=avg_loss)`, providing a summarized view of training progress per epoch.^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Artifact Logging

Checkpoints saved during training are logged as MLflow artifacts. After writing a checkpoint to disk (using PyTorch’s distributed checkpoint API), `mlflow.log_artifacts()` stores the checkpoint directory under a path such as `checkpoints/step{batch_idx}`. This makes each checkpoint versioned and accessible through the MLflow UI or API.^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Setting Up MLflow in the Distributed Training Function

In the provided example, MLflow is set up inside the training function that is decorated with `@distributed(gpus=NUM_WORKERS, gpu_type=GPUType.H100)`. The following code snippet illustrates the pattern:

```python
@distributed(gpus=NUM_WORKERS, gpu_type=GPUType.H100)
def run_fsdp_training(num_workers=NUM_WORKERS):
    import mlflow
    mlflow.start_run(run_name='fsdp_example')
    # ... training logic ...
    mlflow.end_run()
```

The `mlflow.start_run()` call is placed before the main training loop. The run name helps distinguish different training runs in the experiment UI. The `mlflow.log_metric()` calls are inside the training loop to record loss at each batch and after each epoch. After each checkpoint save, `mlflow.log_artifacts()` uploads the checkpoint files. Finally, `mlflow.end_run()` is called after the training loop completes.^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Considerations for Distributed Contexts

In the source example, MLflow logging occurs inside the training function that runs on all worker ranks. While the code does not explicitly restrict logging to a single rank (e.g., rank 0), best practice in distributed training is to log only from one rank to avoid duplicate metric entries. The example does demonstrate conditionally printing output only from rank 0 with `if rank == 0:`, suggesting that logging could be similarly scoped. Checkpoint artifact logging is performed on all ranks by default, but the checkpoint data is identical across ranks because distributed checkpointing ensures consistency.^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Reproducibility and Comparison

By logging metrics and artifacts in MLflow, each distributed training run becomes fully reproducible. The experiment UI allows side-by-side comparison of different runs (e.g., varying learning rates or FSDP configurations) using the logged loss curves and checkpoint artifacts. This makes MLflow an essential component of any distributed training pipeline on Databricks.^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Related Concepts

- Distributed Training with FSDP
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- Checkpointing in PyTorch FSDP
- [Databricks Machine Learning Runtime](/concepts/databricks-runtime-for-machine-learning-ml.md)

## Sources

- distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md

# Citations

1. [distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md](/references/distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws-e728aa55.md)
