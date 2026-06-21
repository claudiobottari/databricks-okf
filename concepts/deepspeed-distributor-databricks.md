---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a571f061c2b20a2f3658d6d2b66b21607f8272b19aea680238403ce9dd832f1c
  pageDirectory: concepts
  sources:
    - distributed-training-with-deepspeed-distributor-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deepspeed-distributor-databricks
    - DD(
  citations:
    - file: distributed-training-with-deepspeed-distributor-databricks-on-aws.md
title: DeepSpeed Distributor (Databricks)
description: A Databricks solution for distributed PyTorch training built on top of TorchDistributor, using the DeepSpeed library to overcome GPU memory constraints and scale large model training.
tags:
  - distributed-training
  - databricks
  - pytorch
timestamp: "2026-06-19T18:37:46.117Z"
---

## DeepSpeed Distributor (Databricks)

The **DeepSpeed distributor** is a distributed training wrapper on Databricks that integrates the open-source [DeepSpeed library](https://github.com/deepspeedai/DeepSpeed) with PyTorch model training. Built on top of the [TorchDistributor](/concepts/torchdistributor.md), it is a recommended solution for training PyTorch ML models that require higher compute power but are limited by GPU memory constraints. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

### Overview

The DeepSpeed library, developed by Microsoft, is an open-source optimization suite that offers optimized memory usage, reduced communication overhead, and advanced pipeline parallelism. These features enable scaling of models and training procedures that would otherwise be unattainable on standard hardware. The DeepSpeed distributor is available in [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) 14.0 ML or above. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

### Benefits

The DeepSpeed distributor is particularly beneficial in the following scenarios: ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

- **Low GPU memory** – DeepSpeed’s memory optimizations allow training of models that require more memory than available on standard hardware.
- **Large model training** – Models with billions of parameters can be trained more efficiently.
- **Large input data** – For use cases like batch inference where input batches are large, the distributor helps manage memory and communication efficiently.

### Example Notebook

Databricks provides a notebook example that demonstrates fine-tuning Llama 2 7B Chat using the DeepSpeed distributor. This notebook illustrates how to set up and run distributed training with the DeepSpeed distributor in the Databricks environment. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

### Related Concepts

- [TorchDistributor](/concepts/torchdistributor.md) – The base distributor on which DeepSpeed distributor is built.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – General concept of training across multiple GPUs or nodes.
- PyTorch – The deep learning framework supported by the distributor.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The runtime environment that includes DeepSpeed.
- Llama 2 – An example large language model that benefits from DeepSpeed.

### Sources

- distributed-training-with-deepspeed-distributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-deepspeed-distributor-databricks-on-aws.md](/references/distributed-training-with-deepspeed-distributor-databricks-on-aws-6ba03a5a.md)
