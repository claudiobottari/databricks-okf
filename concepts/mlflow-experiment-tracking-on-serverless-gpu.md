---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ab9d331abb54089f1dc60c1042465f7c7d089d8d3cf0639becd2db2b25a77774
  pageDirectory: concepts
  sources:
    - distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-experiment-tracking-on-serverless-gpu
    - METOSG
  citations:
    - file: distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: MLflow Experiment Tracking on Serverless GPU
description: Logging training metrics (loss, avg_loss), artifacts (checkpoints), and run metadata to MLflow during distributed training on serverless GPU compute for experiment tracking and reproducibility.
tags:
  - mlflow
  - experiment-tracking
  - databricks
timestamp: "2026-06-19T18:37:39.079Z"
---

# MLflow Experiment Tracking on Serverless GPU

**MLflow Experiment Tracking on Serverless GPU** refers to the practice of using [MLflow](/concepts/mlflow.md) to log, monitor, and manage machine learning experiments that run on Databricks serverless GPU compute. This integration enables distributed training workflows — such as those using [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — to automatically capture metrics, parameters, artifacts, and model checkpoints for reproducibility and comparison. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Overview

When running distributed training on serverless GPU compute, MLflow can be used to log training metrics such as loss values, save model checkpoints as artifacts, and record hyperparameters. The MLflow tracking integration works seamlessly within the distributed training function, where each training process can log metrics that are aggregated for the overall run. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

A typical workflow involves starting an [MLflow Run](/concepts/mlflow-run.md) inside the distributed training function, logging metrics during each training epoch or batch step, and ending the run upon completion. This allows teams to compare different training configurations, track progress over time, and version models and checkpoints. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Logging Metrics

Inside a distributed training function, MLflow can log scalar metrics on a per-batch or per-epoch basis. For example, the training loss for each batch can be logged with the following pattern:

```python
import mlflow

mlflow.start_run(run_name='fsdp_example')
for batch_idx, (data, target) in enumerate(dataloader):
    # ... forward pass and loss calculation ...
    mlflow.log_metric(key='loss', value=loss.item(), step=batch_idx)
mlflow.end_run()
```

^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

At the end of each epoch, the average loss can also be logged:

```python
mlflow.log_metric(key='avg_loss', value=avg_loss)
```

This provides a high-level view of training progress over time. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Logging Artifacts and Checkpoints

MLflow can log checkpoint files as artifacts, enabling versioning and retrieval of model states from specific training steps. After saving a distributed checkpoint (e.g., using PyTorch's distributed checkpoint API), the checkpoint directory can be logged as an MLflow artifact:

```python
mlflow.log_artifacts(f'{CHECKPOINT_DIR}/step{batch_idx}', artifact_path=f'checkpoints/step{batch_idx}')
```

This allows later loading of the checkpoint for inference or continued training. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Experiment Organization with Tags

MLflow experiments can be tagged with budget policy information to control serverless workload spending. The tag `mlflow.workload_creation_policy_id` on an experiment directs MLflow to use a specific [Serverless Budget Policy](/concepts/serverless-budget-policy.md) for serverless workloads it creates, such as scheduled scorers or evaluations. This is set programmatically:

```python
mlflow.set_experiment_tag(
    experiment_id="<your-experiment-id>",
    key="mlflow.workload_creation_policy_id",
    value="<your-policy-id>",
)
```

^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Error Handling: 403 PERMISSION_DENIED

If a workspace disables the default serverless budget policy and no fallback policy is available, MLflow returns a `403 PERMISSION_DENIED` error when attempting to run serverless workloads (such as scheduled scorers or agent evaluations) against an experiment. The error message reads:

```
403 Client Error: Forbidden
PERMISSION_DENIED: Unable to use fallback policies, please manually select a policy.
```

Setting a budget policy on the experiment resolves this issue. Users must have permission to use the policy they assign. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Best Practices

- Start an [MLflow Run](/concepts/mlflow-run.md) at the beginning of the distributed training function to capture all logs in a single run context. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]
- Log checkpoints periodically (e.g., every N batches) so that intermediate model states are available for recovery or analysis. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]
- Use experiment tags to associate budget policies with specific experiments for serverless workloads. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]
- Verify that the experiment's budget policy is set before deploying serverless workloads that require it to avoid permission errors. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Related Concepts

- [MLflow experiments](/concepts/mlflow-experiment.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md)
- 403 PERMISSION_DENIED Serverless Budget Policy Error
- Checkpointing

## Sources

- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
- distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md

# Citations

1. [distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md](/references/distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws-e728aa55.md)
2. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
