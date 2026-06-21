---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d0f9d9f80cb6bd73c0a4c2ac56ba9287945601d3e114248fa1479ecef9e684c4
  pageDirectory: concepts
  sources:
    - best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - single-node-gpu-clusters-for-deep-learning-development
    - SNGCFDLD
  citations:
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
title: Single Node GPU Clusters for Deep Learning Development
description: Using a single driver-only GPU cluster for fast, cost-effective iterative deep learning model development before scaling to distributed training
tags:
  - databricks
  - deep-learning
  - infrastructure
  - gpu
timestamp: "2026-06-18T14:33:15.291Z"
---

# Single Node GPU Clusters for Deep Learning Development

**Single Node GPU Clusters** refer to compute clusters with a single driver node (no worker nodes) that are equipped with one or more GPUs. They are a recommended starting point for deep learning model development on Databricks, particularly during fast, iterative experimentation and for training models on small- to medium-size datasets. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Overview

A Single Node cluster is a driver-only cluster that runs all computation on a single machine. For deep learning development, a single node with 4 GPUs is typically faster and more cost-effective than 4 worker nodes with 1 GPU each, because distributed training incurs network communication overhead. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## When to Use Single Node GPU Clusters

Single Node GPU clusters are a good option during the following phases of deep learning development: ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

- Fast, iterative experimentation and prototyping
- Training models on small- to medium-size datasets
- Developing and debugging model architectures or training logic before scaling up

If the dataset is large enough to make training slow on a single machine, consider moving to distributed training across multiple nodes. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Performance Considerations

### A100 GPUs

A100 GPUs are an efficient choice for many deep learning tasks, including training and tuning [large language models](/concepts/large-language-models-llms-on-databricks.md), natural language processing, object detection and classification, and recommendation engines. Databricks supports A100 GPUs on all clouds. Note that A100 GPUs usually have limited availability, so contact your cloud provider for resource allocation or consider reserving capacity in advance. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### GPU Scheduling

To maximize GPU utilization for deep learning training and inference, optimize GPU scheduling. See the documentation on GPU scheduling for details. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Environment and Resource Management

### Using Cluster Policies

Administrators can create cluster policies to guide data scientists toward appropriate cluster configurations, such as recommending a Single Node cluster for development work and an autoscaling cluster for large production jobs. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Development Environment Customization

Databricks provides several ways to customize the development environment on single node clusters: ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

- Use notebook-scoped Python libraries or R libraries to install specific package versions without affecting other cluster users.
- Install libraries at the cluster level to standardize versions across a team or project.
- Set up a Databricks job to ensure repeated tasks run in a consistent, unchanging environment.

## Training on Single Node GPU Clusters

### Recommended Configuration

Databricks recommends using [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) and [MLflow Tracking](/concepts/mlflow-tracking.md) with [autologging](/concepts/mlflow-autologging.md) for all model training. A Single Node GPU cluster is typically fastest and most cost-effective for model development. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Monitoring Training

- **TensorBoard** is preinstalled in Databricks Runtime ML and can be used within a notebook or in a separate tab. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]
- **Cluster metrics** are available in all Databricks runtimes. Examine network, processor, and memory usage to inspect for bottlenecks. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Performance Optimization

Several optimization techniques are applicable on single node GPU clusters: ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

- **Early stopping** monitors validation metrics and stops training when improvement plateaus. Each deep learning library provides a native API (e.g., TensorFlow/Keras EarlyStopping, PyTorch Lightning EarlyStopping).
- **Batch size tuning** helps optimize GPU utilization. If the batch size is too small, calculations cannot fully use GPU capabilities. Adjust batch size in conjunction with learning rate; a common rule of thumb is: when increasing batch size by *n*, increase learning rate by sqrt(*n*).
- **Transfer learning** starts with a previously trained model and modifies it for the target application, significantly reducing training and tuning time.

## Transitioning to Distributed Training

When a dataset becomes too large for effective single-node training, move to distributed training across multiple nodes. Databricks Runtime ML includes several tools to facilitate this transition: ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

- [TorchDistributor](/concepts/torchdistributor.md) — An open-source module in PySpark for distributed training with PyTorch on Spark clusters
- [DeepSpeed](/concepts/deepspeed.md) — A deep learning optimization library
- Ray — A framework for distributed computing
- [Optuna](/concepts/optuna.md) — A hyperparameter optimization framework that can parallelize training

## Related Concepts

- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- GPU Clusters
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- [MLflow Tracking](/concepts/mlflow-tracking.md)
- Batch Size Tuning
- Early Stopping
- [Transfer Learning](/concepts/transfer-learning.md)
- Cluster Policies

## Sources

- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md

# Citations

1. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
