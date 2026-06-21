---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 03396af0b9341ecbf7d0bb359d14a1a695ab8f6a8f559da642ba250f23c47813
  pageDirectory: concepts
  sources:
    - distributed-training-with-deepspeed-distributor-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deepspeed-library
  citations:
    - file: distributed-training-with-deepspeed-distributor-databricks-on-aws.md
title: DeepSpeed Library
description: An open-source library developed by Microsoft that offers optimized memory usage, reduced communication overhead, and advanced pipeline parallelism for scaling model training on standard hardware.
tags:
  - deep-learning
  - optimization
  - microsoft
timestamp: "2026-06-19T18:37:18.484Z"
---

# DeepSpeed Library

**DeepSpeed** is an open-source deep learning optimization library developed by Microsoft for training large-scale machine learning models. It provides optimized memory usage, reduced communication overhead, and advanced pipeline parallelism that enable scaling of models and training procedures that would otherwise be unattainable on standard hardware. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

## Availability

The DeepSpeed library is available in Databricks Runtime 14.0 ML or above. It is a recommended solution for customers whose models require higher compute power but are limited by memory constraints. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

## Key Features

DeepSpeed offers the following optimization features:

- **Optimized memory usage** – Reduces the memory footprint of large models, allowing them to fit on available hardware.
- **Reduced communication overhead** – Minimizes the communication cost between distributed workers, improving scalability.
- **Advanced pipeline parallelism** – Enables efficient partitioning of model layers across multiple devices for parallel processing.

^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

## Use Cases

The DeepSpeed distributor is particularly beneficial in the following scenarios:

- **Low GPU memory** – When available GPU memory is insufficient to hold the entire model.
- **Large model training** – When training models that exceed the memory capacity of a single GPU.
- **Large input data** – During batch inference or other scenarios involving large input sizes.

^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

## Relationship to TorchDistributor

The DeepSpeed distributor is built on top of [TorchDistributor](/concepts/torchdistributor.md), which provides the underlying distributed training infrastructure for PyTorch ML models on Databricks. This integration allows users to leverage DeepSpeed's optimizations within the familiar distributed training framework. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

## Training with DeepSpeed

Distributed training with the DeepSpeed distributor follows patterns similar to other distributed training approaches on Databricks, but with DeepSpeed-specific configuration for memory optimization and parallelism. The library handles the distribution of model states, gradients, and optimizer states across available devices. An example notebook demonstrating how to fine-tune Llama 2 7B Chat using the DeepSpeed distributor is available in the Databricks documentation. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

## Related Concepts

- [TorchDistributor](/concepts/torchdistributor.md) – The underlying distributed training framework for PyTorch on Databricks.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – General concepts for training models across multiple nodes and GPUs.
- [PyTorch on Databricks](/concepts/pytorch-on-databricks.md) – Using the PyTorch machine learning framework within Databricks environments.
- [Pipeline Parallelism](/concepts/pipeline-parallelism-in-deepspeed.md) – A parallelism strategy for distributing model layers across devices.
- Model Parallelism – Techniques for splitting large models across multiple GPUs.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The ML-optimized runtime that includes DeepSpeed.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – An alternative distributed training approach for large models that also addresses memory constraints.
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) – The parameter scale at which memory-optimized training techniques like DeepSpeed become essential.

## Sources

- distributed-training-with-deepspeed-distributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-deepspeed-distributor-databricks-on-aws.md](/references/distributed-training-with-deepspeed-distributor-databricks-on-aws-6ba03a5a.md)
