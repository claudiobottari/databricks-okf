---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e5ff7c0edd6d7d30901d0935cef0840bc681a8ccaebb134def81e441d1d639c1
  pageDirectory: concepts
  sources:
    - deep-learning-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-for-deep-learning-tracking
    - MFDLT
  citations:
    - file: deep-learning-databricks-on-aws.md
title: MLflow for Deep Learning Tracking
description: Using MLflow on Databricks to track iterative deep learning training runs, model development, and experiment logging.
tags:
  - mlflow
  - databricks
  - experiment-tracking
timestamp: "2026-06-18T15:13:42.100Z"
---

# MLflow for Deep Learning Tracking

**MLflow for Deep Learning Tracking** refers to the use of the [MLflow Tracking](/concepts/mlflow-tracking.md) component to log, compare, and manage experiments when training deep learning models on Databricks. Because deep learning projects are highly iterative — involving many hyperparameter trials, architecture changes, and distributed training runs — systematic tracking is essential for reproducibility and model selection. ^[deep-learning-databricks-on-aws.md]

## Overview

MLflow provides a lightweight, framework-agnostic API that integrates naturally with deep learning workflows. On Databricks, MLflow is automatically available in [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md), which includes PyTorch, TensorFlow, and other common libraries. MLflow can log parameters, metrics, artifacts (such as model checkpoints or plots), and source versions from any training run. ^[deep-learning-databricks-on-aws.md]

## Key Capabilities

### Experiment Organization

Each training run is recorded as an **MLflow Run** under an **MLflow Experiment**. Practitioners group related runs into a single experiment to compare results side-by-side in the Databricks UI. ^[deep-learning-databricks-on-aws.md]

### Automatic Logging

MLflow supports automatic logging for both PyTorch and TensorFlow via `mlflow.pytorch.autolog()` and `mlflow.tensorflow.autolog()`. This captures loss curves, metrics, and hyperparameters with no manual instrumentation. For a full end‑to‑end example using PyTorch, see the [MLflow 3 Deep Learning Workflow](/concepts/mlflow-3-deep-learning-workflow.md) tutorial notebook. ^[deep-learning-databricks-on-aws.md]

### Distributed Training Tracking

Distributed training strategies such as [TorchDistributor](/concepts/torchdistributor.md), [DeepSpeed](/concepts/deepspeed.md), or Ray can be tracked seamlessly: each worker’s metrics are aggregated and logged to a single [MLflow Run](/concepts/mlflow-run.md), preserving the full history of the distributed job. ^[deep-learning-databricks-on-aws.md]

### Model Registry Integration

After a deep learning run finishes, the best model can be registered in the [MLflow Model Registry](/concepts/mlflow-model-registry.md) for staging, approval, and deployment — all from the same UI used for tracking. ^[deep-learning-databricks-on-aws.md]

## Usage Example

```python
import mlflow
import torch
import torch.nn as nn

mlflow.set_experiment("deep-learning-experiment")

with mlflow.start_run() as run:
    # Log hyperparameters
    mlflow.log_params({"lr": 0.001, "epochs": 10})

    # Train model ...
    model = nn.Linear(10, 2)

    # Log metrics per epoch
    for epoch in range(10):
        loss = train_one_epoch(model)
        mlflow.log_metric("loss", loss, step=epoch)

    # Log model artifact
    mlflow.pytorch.log_model(model, "model")
```

## Related Wikis

- [MLflow Experiments](/concepts/mlflow-experiment.md) – Organize and compare runs.
- MLflow Metrics and Parameters – Key tracking primitives.
- [PyTorch on Databricks](/concepts/pytorch-on-databricks.md) – Deep learning framework integration.
- [TensorFlow on Databricks](/concepts/tensorflow-on-databricks.md) – Alternative framework tracking.
- [Distributed Training on Databricks](/concepts/distributed-training-on-databricks.md) – Scaling with MLflow.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – Preconfigured environment.
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) – Model lifecycle management.

## Sources

- deep-learning-databricks-on-aws.md

# Citations

1. [deep-learning-databricks-on-aws.md](/references/deep-learning-databricks-on-aws-50a1d868.md)
