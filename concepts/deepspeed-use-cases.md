---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 20a14bce41814721245ff812c00856561e5f88c5a52b6422eac1e8c93d05a268
  pageDirectory: concepts
  sources:
    - distributed-training-with-deepspeed-distributor-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deepspeed-use-cases
    - DUC
  citations:
    - file: distributed-training-with-deepspeed-distributor-databricks-on-aws.md
title: DeepSpeed Use Cases
description: The DeepSpeed distributor is beneficial for scenarios with low GPU memory, large model training, and large input data such as batch inference.
tags:
  - use-cases
  - distributed-training
  - gpu-optimization
timestamp: "2026-06-19T18:37:40.132Z"
---

Here is the updated wiki page for "DeepSpeed Use Cases", written solely from the provided source material.

---
title: DeepSpeed Use Cases
summary: The primary scenarios where DeepSpeed distributor is beneficial include low GPU memory situations, large model training, and large input data processing such as batch inference.
sources:
  - distributed-training-with-deepspeed-distributor-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T15:33:41.251Z"
updatedAt: "2026-06-18T15:33:41.251Z"
tags:
  - use-cases
  - machine-learning
  - gpu
aliases:
  - deepspeed-use-cases
  - DUC
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# DeepSpeed Use Cases

**DeepSpeed Use Cases** describes the scenarios where the [DeepSpeed](/concepts/deepspeed.md) library is particularly beneficial for distributed training of PyTorch ML models. The DeepSpeed distributor, built on top of [TorchDistributor](/concepts/torchdistributor.md), is recommended for customers whose models require higher compute power but are limited by memory constraints.^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

### When to Use DeepSpeed

The following are example scenarios where the DeepSpeed distributor provides clear advantages over standard distributed training approaches.^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

#### Low GPU Memory

DeepSpeed is beneficial when GPU memory is limited. Through techniques such as [ZeRO optimization](/concepts/deepspeed-zero-stage-3-optimization.md), DeepSpeed shards optimizer states, gradients, and parameters across GPUs, drastically reducing the per-GPU memory footprint. This allows models to be trained on hardware that would otherwise be unable to accommodate them.^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

> **Note:** While the source mentions “optimized memory usage” as a general capability, the specific reference to ZeRO optimization is an inference based on known DeepSpeed features; no direct citation is available for the ZeRO term in this source.

#### Large Model Training

DeepSpeed is well-suited for training large models that exceed the memory capacity of a single GPU. Its advanced features, such as optimized memory usage and pipeline parallelism, allow for scaling of models and training procedures that would otherwise be unattainable on standard hardware. The library is available in [Databricks Runtime 14.0 ML](/concepts/databricks-runtime-140-ml.md) or above.^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

#### Batch Inference with Large Input Data

During [batch inference](/concepts/batch-inference-on-databricks.md), when input data is very large, DeepSpeed can manage the increased memory demands efficiently. This makes it a strong choice for production inference pipelines that need to process large volumes of data concurrently.^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

### Key Capabilities

The DeepSpeed library offers several capabilities that make it effective for these use cases:^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

- **Optimized memory usage** – Reduces the memory required to train large models.
- **Reduced communication overhead** – Minimizes the time spent synchronizing gradients and parameters between GPUs.
- **Advanced pipeline parallelism** – Allows different parts of a model to be processed on different GPUs simultaneously, further improving efficiency.

### Example

The provided source includes a notebook example demonstrating how to fine-tune Llama 2 7B Chat using the DeepSpeed distributor on Databricks.^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

### Related Concepts

- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- [TorchDistributor](/concepts/torchdistributor.md)
- [ZeRO Optimization](/concepts/deepspeed-zero-stage-3-optimization.md)
- [Pipeline Parallelism](/concepts/pipeline-parallelism-in-deepspeed.md)
- Batch Inference
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)

### Sources

- distributed-training-with-deepspeed-distributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-deepspeed-distributor-databricks-on-aws.md](/references/distributed-training-with-deepspeed-distributor-databricks-on-aws-6ba03a5a.md)
