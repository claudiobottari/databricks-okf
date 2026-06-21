---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f88d63cec85621f18daa3ab30f8d3f15442d235e979da3feb8998618f0976225
  pageDirectory: concepts
  sources:
    - deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - distributed-training-development-workflow-on-databricks
    - DTDWOD
  citations:
    - file: deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md
title: Distributed training development workflow on Databricks
description: The recommended workflow pattern for developing and running distributed deep learning jobs on Databricks using HorovodRunner, including data preparation and notebook-based execution.
tags:
  - workflow
  - databricks
  - distributed-training
  - best-practice
timestamp: "2026-06-19T14:58:48.470Z"
---

# Distributed Training Development Workflow on Databricks

**Distributed Training Development Workflow on Databricks** refers to the recommended iterative process for developing, testing, and scaling deep learning models using distributed training frameworks like [Horovod](/concepts/horovod.md) on Databricks clusters. This workflow emphasizes local development and validation before scaling to multi-node training.

## Overview

The distributed training development workflow on Databricks follows a progressive scaling approach: start with a single-node implementation, validate correctness on small data, then scale to distributed multi-node training using [HorovodRunner](/concepts/horovodrunner.md). This minimizes debugging time and resource waste. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

## Development Workflow Steps

### Step 1: Prepare Data

Before running distributed training, data must be prepared and accessible from all worker nodes. This typically involves loading data into [Delta Lake](/concepts/delta-lake.md) or DBFS so that each worker can read its shard without bottlenecks. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

### Step 2: Prototype on a Single Node

Start by implementing the model (e.g., TensorFlow + Keras) and running it on a small dataset on a single node. This step validates the model architecture, preprocessing logic, and training loop before adding distributed complexity. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

### Step 3: Validate on Full Data

Once the prototype runs correctly, train on the full dataset on a single node. This confirms that data loading pipelines, memory usage, and model performance behave as expected at full scale. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

### Step 4: Convert to Distributed Training

Refactor the single-node training code to use [HorovodRunner](/concepts/horovodrunner.md) for distributed execution. The key changes involve:

- Wrapping the training function inside a Python function that HorovodRunner can execute on multiple workers.
- Distributing the dataset across workers (each worker processes a unique shard).
- Using [Horovod](/concepts/horovod.md) operations like `hvd.DistributedOptimizer` to synchronize gradients.

### Step 5: Tune and Scale

After verifying distributed training works correctly, iterate on hyperparameters and scale to more GPUs or nodes. HorovodRunner can scale from a few workers on a single node to dozens across multiple workers. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

## Key Considerations

### Data Distribution

Each worker in a distributed training setup must process different data to achieve meaningful parallelism. Use dataset sharding — typically by assigning a unique subset of the training data to each worker based on `hvd.rank()`. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

### Learning Rate Scaling

When using multiple workers, the effective batch size increases. A common practice is to scale the learning rate linearly: `learning_rate * hvd.size()`. Some frameworks like [Horovod](/concepts/horovod.md) provide automatic learning rate scaling through their optimizers. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

### Synchronization

Horovod synchronizes gradients across all workers after each batch using allreduce operations. This ensures model consistency but introduces communication overhead. The BroadcastGlobalVariablesCallback ensures all workers start with identical initial weights. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

## Example Implementation

The following notebook demonstrates the complete distributed training development workflow using TensorFlow, Keras, and [HorovodRunner](/concepts/horovodrunner.md) for an MNIST digit classification model:

- **Single-node prototype**: Train on 1,000 samples to validate the model.
- **Full single-node training**: Train on the complete MNIST dataset.
- **Distributed training**: Use `HorovodRunner(np=4)` with 4 workers, including gradient synchronization and metric averaging.

## Best Practices

- **Start small.** Always validate on a small subset of data before scaling to full distributed training. This saves compute resources and debugging time. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]
- **Monitor worker utilization.** Ensure all workers are actively training and not waiting on data loading or I/O bottlenecks. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]
- **Use [MLflow](/concepts/mlflow.md) for tracking.** Log parameters, metrics, and models from each training run to compare distributed and single-node results. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]
- **Checkpoint strategically.** Use Horovod's checkpointing callbacks to save model weights from rank 0, avoiding duplicate checkpoints. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

## Related Concepts

- [HorovodRunner](/concepts/horovodrunner.md) — Databricks' API for running Horovod distributed training
- [Horovod](/concepts/horovod.md) — The distributed training framework that provides gradient synchronization
- [Distributed Deep Learning](/concepts/distributed-deep-learning-on-databricks.md) — General concepts of scaling neural network training
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Experiment tracking for distributed training runs
- GPU Clusters — Hardware configuration for distributed training on Databricks
- [MNIST with TensorFlow and Keras](/concepts/mnist-with-tensorflow-and-keras-on-databricks.md) — Example implementation following this workflow
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) — GPU configuration for distributed training workloads
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) — GPU type commonly used for large-scale training

## Sources

- deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md

# Citations

1. [deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md](/references/deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws-06d44e07.md)
