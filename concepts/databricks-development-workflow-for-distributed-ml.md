---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4de8ef235e4615d83eb517aa94b4bbac84187b5391328460c733025f9d8cf351
  pageDirectory: concepts
  sources:
    - adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-development-workflow-for-distributed-ml
    - DDWFDM
  citations:
    - file: adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md
title: Databricks Development Workflow for Distributed ML
description: Recommended methodology on Databricks for iteratively developing machine learning models by starting with single-node training before scaling to distributed execution
tags:
  - workflow
  - databricks
  - machine-learning
timestamp: "2026-06-18T10:38:48.953Z"
---

# Databricks Development Workflow for Distributed ML

The recommended development workflow for distributed machine learning on Databricks follows a two-phase approach: first develop and debug the model on a single node, then adapt the code for distributed training using [HorovodRunner](/concepts/horovodrunner.md). This iterative pattern reduces complexity during early experimentation and leverages scalable infrastructure only after the model logic is verified. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Workflow Steps

1. **Single‑node training** – Implement and test the model on a single worker node (e.g., using PyTorch on a single GPU). This allows rapid debugging of model architecture, data pipelines, and loss functions without the overhead of distributed synchronization.
2. **Adapt for distributed training** – Once the single‑node version produces correct results, refactor the training code to use [HorovodRunner](/concepts/horovodrunner.md) with [Horovod](/concepts/horovod.md). HorovodRunner handles gradient synchronization across multiple workers, enabling seamless scaling to multiple GPUs or nodes.

This workflow is demonstrated in the HorovodRunner PyTorch MNIST example notebook, which first trains a PyTorch model on a single node and then adapts the same code for distributed execution using HorovodRunner. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Benefits

- **Faster iteration** – Debugging on a single node avoids the complexity of distributed state management, making it easier to identify and fix issues early.
- **Minimal code changes** – HorovodRunner requires only a few modifications to the single‑node training script (e.g., wrapping the training loop) to enable distributed training.
- **Scalability** – Once the single‑node version is stable, the same logic can be scaled across many GPUs without redesigning the model.

## Related Concepts

- [HorovodRunner](/concepts/horovodrunner.md) – Databricks API for distributed deep learning with Horovod.
- [Horovod](/concepts/horovod.md) – Distributed training framework for TensorFlow, PyTorch, and MXNet.
- PyTorch – Deep learning framework used in the example.
- [Distributed Deep Learning](/concepts/distributed-deep-learning-on-databricks.md) – General concept of training models across multiple workers.
- [Single‑Node Training](/concepts/single-node-gpu-training-on-databricks.md) – The initial phase of the development workflow.

## Sources

- adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md

# Citations

1. [adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md](/references/adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws-7a436585.md)
