---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fdefa2c687f7d2f94f629e482f61dc230d75948c0768d1221e16d4b9095d74d2
  pageDirectory: concepts
  sources:
    - deep-learning-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracking-for-deep-learning
    - MTFDL
  citations:
    - file: deep-learning-databricks-on-aws.md
title: MLflow Tracking for Deep Learning
description: Using MLflow on Databricks to track iterative deep learning training runs and model development as part of the MLflow ecosystem.
tags:
  - mlflow
  - tracking
  - deep-learning
  - databricks
timestamp: "2026-06-19T18:18:58.199Z"
---

# MLflow Tracking for Deep Learning

**MLflow Tracking for Deep Learning** refers to the use of [MLflow Tracking](/concepts/mlflow-tracking.md) to log, organize, and compare deep learning training runs and model development. Because deep learning models are data and computation intensive and often require many iterations of experimentation, tracking is a cornerstone of the workflow. ^[deep-learning-databricks-on-aws.md]

## Role in Deep Learning Workflows

Tracking is especially vital for the iterative nature of deep learning. With MLflow, practitioners can compare runs across different hyperparameter settings, network architectures, and training schedules. Databricks integrates MLflow into its environment so that every training run can be automatically or manually logged. ^[deep-learning-databricks-on-aws.md]

## Integration with Deep Learning Frameworks

### PyTorch

PyTorch is included in Databricks Runtime ML and provides GPU accelerated tensor computation and high-level functionalities for building deep learning networks. MLflow integrates with PyTorch to track metrics, parameters, and artifacts during training. For an end-to-end tutorial notebook using PyTorch and MLflow, see the [MLflow 3 Deep Learning Workflow](/concepts/mlflow-3-deep-learning-workflow.md). ^[deep-learning-databricks-on-aws.md]

### TensorFlow

TensorFlow and [TensorBoard](/concepts/tensorboard-on-databricks.md) are included in Databricks Runtime ML. MLflow can capture TensorFlow training metrics alongside TensorBoard logs, providing a unified view of experiment results. ^[deep-learning-databricks-on-aws.md]

## Distributed Training Tracking

When using distributed training techniques such as Ray, [TorchDistributor](/concepts/torchdistributor.md), or [DeepSpeed](/concepts/deepspeed.md), MLflow Tracking remains essential for coordinating and comparing results across distributed runs. Each worker or process can log to the same experiment, enabling comparison of distributed training runs with different configurations. ^[deep-learning-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) – The core component for logging and querying experiment runs.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – Pre-configured environment with deep learning libraries and MLflow.
- Model Development – The iterative process of building and refining deep learning models.
- [Training Runs](/concepts/managing-mlflow-runs.md) – Individual executions of a deep learning training script.
- [Best Practices for Deep Learning on Databricks](/concepts/best-practices-for-deep-learning-on-databricks.md) – Guidance for optimizing deep learning workflows.
- [AI Runtime](/concepts/ai-runtime.md) – Serverless GPU environment for single and multi-node deep learning workloads.

## Sources

- deep-learning-databricks-on-aws.md

# Citations

1. [deep-learning-databricks-on-aws.md](/references/deep-learning-databricks-on-aws-50a1d868.md)
