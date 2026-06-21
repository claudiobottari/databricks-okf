---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3e2537c8556e7083061b834ed5a557db4123256c21dea4d189983c191e359c81
  pageDirectory: concepts
  sources:
    - distributed-training-with-deepspeed-distributor-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-runtime-ml-for-deepspeed
    - DRMFD
  citations:
    - file: distributed-training-with-deepspeed-distributor-databricks-on-aws.md
title: Databricks Runtime ML for DeepSpeed
description: Databricks Runtime 14.0 ML or above is required to use the DeepSpeed library and distributor for distributed training.
tags:
  - databricks
  - version-requirements
  - machine-learning
timestamp: "2026-06-19T18:37:44.952Z"
---

## Databricks Runtime ML for DeepSpeed

**Databricks Runtime ML for DeepSpeed** provides a built-in [DeepSpeed](/concepts/deepspeed.md) distributor that enables distributed training of large PyTorch models on the Databricks platform. The DeepSpeed distributor is available starting in **Databricks Runtime 14.0 ML** and is built on top of the [TorchDistributor](/concepts/torchdistributor.md), offering a recommended solution for customers who need higher compute power but are constrained by GPU memory limitations. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

### Key Capabilities

The DeepSpeed library, developed by Microsoft as an open-source project, introduces several optimisations that make training larger models feasible on standard hardware:

- **Optimised memory usage** – reduces the per‑GPU memory footprint of model parameters, gradients, and optimizer states.
- **Reduced communication overhead** – minimises the bandwidth needed for gradient synchronization across GPUs.
- **Advanced pipeline parallelism** – splits model layers across devices to improve throughput and memory efficiency. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

### Typical Use Cases

The DeepSpeed distributor is especially beneficial in the following scenarios:

- **Low GPU memory** – when individual GPUs cannot hold the full model.
- **Large model training** – for models with billions of parameters that exceed the capacity of a single device.
- **Large input data (batch inference)** – when processing batches that are too large to fit into GPU memory simultaneously. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

### Example Notebook

Databricks provides an example notebook that demonstrates how to fine‑tune a **Llama 2 7B Chat** model using the DeepSpeed distributor within Databricks Runtime ML. This notebook serves as a practical starting point for users who want to apply DeepSpeed to their own training workflows. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

### Architecture

The DeepSpeed distributor runs as a wrapper around [TorchDistributor](/concepts/torchdistributor.md), Databricks’ native interface for launching distributed PyTorch jobs. It inherits the same integration with Apache Spark for cluster orchestration while adding DeepSpeed’s memory and communication optimisations. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

### Related Concepts

- [TorchDistributor](/concepts/torchdistributor.md) – the underlying distributed training framework used by the DeepSpeed distributor.
- [DeepSpeed](/concepts/deepspeed.md) – the open-source library that provides memory and performance optimisations.
- PyTorch – the deep learning framework used in conjunction with the distributor.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – the runtime environment that includes the DeepSpeed library.
- [Distributed training](/concepts/workload-yaml-for-distributed-training.md) – general techniques for training models across multiple GPUs or nodes.
- Large language model training – a common application area for DeepSpeed.
- [Batch inference](/concepts/batch-inference-pipelines.md) – a scenario where DeepSpeed’s memory handling is beneficial.

### Sources

- distributed-training-with-deepspeed-distributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-deepspeed-distributor-databricks-on-aws.md](/references/distributed-training-with-deepspeed-distributor-databricks-on-aws-6ba03a5a.md)
