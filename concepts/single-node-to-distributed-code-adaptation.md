---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 109ad3030088530567d0299e8f9b1fb3af70cdc7fbb777f4aa4498db3c45cf35
  pageDirectory: concepts
  sources:
    - adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - single-node-to-distributed-code-adaptation
    - SNTDCA
  citations:
    - file: adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md
title: Single Node to Distributed Code Adaptation
description: The process of modifying single-node PyTorch training code to work in a distributed environment using HorovodRunner, following Databricks' recommended development workflow
tags:
  - code-migration
  - pytorch
  - distributed-training
timestamp: "2026-06-19T13:53:00.586Z"
---

# Single Node to Distributed Code Adaptation

**Single Node to Distributed Code Adaptation** refers to the recommended development workflow for performing distributed training of machine learning models, starting with a single-node implementation and then refactoring it to run across multiple GPUs or nodes. This approach allows developers to iterate quickly on a local configuration before dealing with the complexities of distributed systems. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Overview

The typical workflow involves two phases:

1. **Single-node training** — Develop and debug the model code on a single GPU or CPU.
2. **Distributed adaptation** — Modify the code to leverage multiple workers using a distributed training framework such as [HorovodRunner](/concepts/horovodrunner.md).

This pattern is especially common when using PyTorch for deep learning tasks like image classification on the MNIST dataset. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Adaptation with HorovodRunner

On Databricks, the [HorovodRunner](/concepts/horovodrunner.md) utility is used to adapt single-node PyTorch code for distributed execution. HorovodRunner wraps a training function and distributes it across a cluster of workers, handling communication and synchronization via Horovod’s allreduce operations. The developer only needs to make targeted changes — such as broadcasting initial model parameters and splitting the dataset — rather than rewriting the entire training loop. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

### Example: HorovodRunner PyTorch MNIST

A dedicated notebook demonstrates the full adaptation process:

- It first trains a simple PyTorch model on the MNIST dataset using a single node.
- It then refactors the training code to run with `HorovodRunner` for distributed execution.

The notebook follows the development workflow recommended by Databricks for moving from single-node to distributed deep learning. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Related Concepts

- [HorovodRunner](/concepts/horovodrunner.md)
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- PyTorch
- MNIST
- [Development Workflow](/concepts/horovodrunner-development-workflow.md)
- [Horovod](/concepts/horovod.md)

## Sources

- adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md

# Citations

1. [adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md](/references/adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws-7a436585.md)
