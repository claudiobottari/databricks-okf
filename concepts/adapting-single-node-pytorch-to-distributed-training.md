---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: adc6e538e50737bfa9ae3c82d6d2063b8d4f5cc75ccf3947eff28ef633b5ac6f
  pageDirectory: concepts
  sources:
    - adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - adapting-single-node-pytorch-to-distributed-training
    - ASPTDT
    - Convert single process to distributed training
  citations:
    - file: adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md
title: Adapting Single-Node PyTorch to Distributed Training
description: The process of modifying PyTorch code originally written for single-node training to run in a distributed manner across multiple nodes
tags:
  - pytorch
  - distributed-training
  - migration
timestamp: "2026-06-19T08:51:05.748Z"
---

# Adapting Single-Node PyTorch to Distributed Training

**Adapting single-node PyTorch to distributed training** describes the process of modifying a PyTorch training script that runs on a single machine so that it can execute across multiple GPUs or nodes. This notebook follows the recommended development workflow for distributed deep learning on Databricks, first training the model on a single node, and then adapting the code using [HorovodRunner](/concepts/horovodrunner.md) for distributed training.^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Development Workflow

The recommended workflow for distributed deep learning begins by training the model on a single node. Once the single-node code is correct and performant, it is adapted for distributed execution. This approach allows developers to isolate model-level bugs before introducing the complexity of distributed communication.^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

On Databricks, this workflow is commonly implemented using [HorovodRunner](/concepts/horovodrunner.md), which handles the orchestration of [Horovod](/concepts/horovod.md) workers across a cluster. The notebook "HorovodRunner PyTorch MNIST example notebook" demonstrates this pattern, first training on a single node and then adapting the same code for distributed training with HorovodRunner.^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Related Concepts

- [Horovod](/concepts/horovod.md) — A distributed deep learning framework that abstracts message-passing primitives.
- [HorovodRunner](/concepts/horovodrunner.md) — A Databricks utility for running Horovod jobs on clusters.

## Sources

- adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md

# Citations

1. [adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md](/references/adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws-7a436585.md)
