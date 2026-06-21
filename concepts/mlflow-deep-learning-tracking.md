---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5afe9eba3b16a119b556f46932751ea47be26bdc8e99951ce79b81c05f1fe5e6
  pageDirectory: concepts
  sources:
    - deep-learning-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-deep-learning-tracking
    - MDLT
    - Deep Learning Training Logging
  citations:
    - file: deep-learning-databricks-on-aws.md
title: MLflow deep learning tracking
description: Using MLflow on Databricks to track deep learning training runs and model development, providing experiment tracking essential for iterative deep learning workflows.
tags:
  - mlflow
  - tracking
  - deep-learning
timestamp: "2026-06-18T11:46:30.175Z"
---

# MLflow Deep Learning Tracking

**MLflow Deep Learning Tracking** refers to the practice of using [MLflow Tracking](/concepts/mlflow-tracking.md) to log, monitor, and compare metrics, parameters, artifacts, and model checkpoints during deep learning training runs on Databricks. It is a core component of the MLflow ecosystem and is especially vital for the iterative nature of deep learning model development. ^[deep-learning-databricks-on-aws.md]

## Overview

Databricks uses MLflow to track deep learning training runs and model development. Because deep learning workflows often involve many experiments with varying hyperparameters, architectures, and datasets, systematic tracking is essential for reproducibility and progress comparison. MLflow Tracking provides the infrastructure to log every run, record key metrics (e.g., loss, accuracy), store model checkpoints, and compare results across experiments. ^[deep-learning-databricks-on-aws.md]

## Integration with Deep Learning Frameworks

Databricks Runtime ML includes PyTorch, TensorFlow, and supporting tools like TensorBoard, all pre-installed and ready for use. MLflow Tracking integrates seamlessly with these libraries:

- **PyTorch**: Log PyTorch training runs via MLflow’s `autolog` or custom logging. For an end-to-end tutorial, see the [MLflow 3 Deep Learning Workflow](/concepts/mlflow-3-deep-learning-workflow.md) notebook. ^[deep-learning-databricks-on-aws.md]
- **TensorFlow**: Use TensorBoard for visualization while logging runs to MLflow. MLflow can capture TensorFlow metrics and artifacts automatically. ^[deep-learning-databricks-on-aws.md]

## Distributed Training Tracking

For distributed training workloads—such as those using Ray, TorchDistributor, or DeepSpeed—MLflow Tracking can aggregate logs from multiple workers into a single run. This enables unified visibility into the performance of multi-GPU and multi-node deep learning jobs. ^[deep-learning-databricks-on-aws.md]

## Best Practices

- **Enable autologging**: Use `mlflow.pytorch.autolog()` or `mlflow.tensorflow.autolog()` to automatically capture metrics, parameters, and models during training.
- **Log checkpoints**: Save model checkpoints as MLflow artifacts to enable rollback and experiment comparison.
- **Tag runs**: Use tags to annotate runs with meaningful metadata (e.g., dataset version, model architecture) for easier filtering and retrieval.
- **Compare runs**: Leverage MLflow’s UI to compare metrics across multiple deep learning runs, identifying the best configuration quickly.

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) — The underlying system for logging and querying experiments
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The pre-configured runtime that includes deep learning frameworks and MLflow
- [PyTorch on Databricks](/concepts/pytorch-on-databricks.md) — Running PyTorch training with MLflow tracking
- [TensorFlow on Databricks](/concepts/tensorflow-on-databricks.md) — Running TensorFlow training with MLflow tracking
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Scaling deep learning across multiple GPUs or nodes
- [MLflow Autologging](/concepts/mlflow-autologging.md) — Automatic capture of training metrics and models

## Sources

- deep-learning-databricks-on-aws.md

# Citations

1. [deep-learning-databricks-on-aws.md](/references/deep-learning-databricks-on-aws-50a1d868.md)
