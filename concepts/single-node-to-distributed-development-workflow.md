---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8d1ca045d03297fcf6c60a725defeb397e864e8de418267f03eb8373c63e56e9
  pageDirectory: concepts
  sources:
    - adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - single-node-to-distributed-development-workflow
    - SDW
  citations:
    - file: adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md
title: Single-node-to-distributed development workflow
description: "A recommended development pattern for distributed training: first train and validate on a single node, then adapt the code for distributed execution using HorovodRunner."
tags:
  - workflow
  - best-practices
  - distributed-training
timestamp: "2026-06-19T21:57:36.786Z"
---

Here is the wiki page for "Single-node-to-distributed development workflow", written based solely on the provided source material.

---

## Single-node-to-distributed development workflow

The **single-node-to-distributed development workflow** is a recommended approach for adapting machine learning training code to run across multiple GPUs or nodes. The workflow starts by training the model on a single node, then incrementally adapts the code for distributed training using a framework like [HorovodRunner](/concepts/horovodrunner.md). ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

### Overview

The core principle is to first get the training script working correctly on a single node before adding complexity. This allows developers to validate model logic, hyperparameters, and data pipelines in a simpler environment. Once the single-node version is stable, the code is adapted to use distributed training primitives. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

### Recommended Approach

The notebook "Adapt single node PyTorch to distributed deep learning" demonstrates this workflow explicitly. It first shows how to train the model on a single node using standard PyTorch, and then how to adapt that code using HorovodRunner for distributed training. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

### Best Practices

- **Start small**: Train on a single node to debug the model architecture, loss function, and data loading.
- **Add distribution incrementally**: After the single-node version works, introduce distributed communication primitives.
- **Use higher-level abstractions**: Tools like HorovodRunner simplify the transition by wrapping low-level communication details.

### Related Concepts

- [HorovodRunner](/concepts/horovodrunner.md) – Distributed deep learning with Horovod on Databricks.
- [Horovod](/concepts/horovod.md) – Distributed training framework used by HorovodRunner.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – PyTorch's native distributed training approach.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – Memory-efficient distributed training for large models.
- [MNIST example](/concepts/mnist-tensorflow-keras-example.md) – A common benchmark dataset used in distributed training tutorials.

### Sources

- adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md

# Citations

1. [adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md](/references/adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws-7a436585.md)
