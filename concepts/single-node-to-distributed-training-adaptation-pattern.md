---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 124ba8f12c4f2f001844f9bcf9bc6f7e62afa2f3f10f2357e86b44ec04b43e37
  pageDirectory: concepts
  sources:
    - adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - single-node-to-distributed-training-adaptation-pattern
    - SNTDTAP
  citations:
    - file: adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md
title: Single Node to Distributed Training Adaptation Pattern
description: Recommended development workflow of first training a model on a single node, then adapting the code for distributed training using HorovodRunner
tags:
  - workflow
  - distributed-training
  - best-practice
timestamp: "2026-06-18T10:38:28.233Z"
---

# Single Node to Distributed Training Adaptation Pattern

The **single-node to distributed training adaptation pattern** is a development workflow for scaling machine learning models from a single compute node to a distributed cluster. In the context of Databricks, this pattern uses [HorovodRunner](/concepts/horovodrunner.md) to convert a single‑node PyTorch training script into a distributed training job with minimal code changes. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Development Workflow

The recommended workflow follows two stages: ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

1. **Train on a single node first** – Develop and debug the model training code on one machine (e.g., a single‑driver notebook). This ensures the model logic, data pipeline, and hyperparameters are correct before scaling out.

2. **Adapt for distributed training** – Once the single‑node code works correctly, modify it to run on multiple workers using HorovodRunner. The adaptation typically involves wrapping the training function and adding distributed communication primitives (e.g., broadcasting initial model parameters, averaging gradients across workers).

The notebook **HorovodRunner PyTorch MNIST example** illustrates both stages: a single‑node implementation followed by the distributed adaptation. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Adaptation Steps with HorovodRunner

Adapting a single‑node PyTorch script for distributed training with HorovodRunner generally involves:

1. **Initializing Horovod** – Call `hvd.init()` to set up the distributed environment.
2. **Pinning each worker to a GPU/CPU** – Use `torch.cuda.set_device(hvd.local_rank())` to assign a unique device per worker.
3. **Scaling the learning rate** – Multiply the learning rate by the number of workers to compensate for larger mini‑batches.
4. **Wrapping the optimizer** – Use `hvd.DistributedOptimizer` to synchronize gradients across workers.
5. **Broadcasting initial parameters** – Call `hvd.broadcast_parameters()` to ensure all workers start from the same model state.
6. **Modifying the data loader** – Use `hvd.DistributedSampler` to partition the training data across workers.

HorovodRunner handles the orchestration of multiple worker processes on the cluster, so the data scientist writes a standard Python training function that is invoked by HorovodRunner. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Related Concepts

- [HorovodRunner](/concepts/horovodrunner.md) – Databricks utility for distributed deep learning with Horovod
- PyTorch – Deep learning framework used in the notebook example
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – General concept of parallelizing model training
- MNIST – Example dataset used in the notebook
- [Single Node Training](/concepts/single-node-gpu-training-on-databricks.md) – The baseline workflow before scaling

## Sources

- adapt‑single‑node‑pytorch‑to‑distributed‑deep‑learning‑databricks‑on‑aws.md

# Citations

1. [adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md](/references/adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws-7a436585.md)
