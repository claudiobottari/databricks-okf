---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aab58928ffa2ad1ff2ea259519878c1bfaa8cfd1c959362d8397377115166b35
  pageDirectory: concepts
  sources:
    - distributed-training-with-deepspeed-distributor-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-runtime-ml-support
    - DRMS
  citations:
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
    - file: distributed-training-with-deepspeed-distributor-databricks-on-aws.md
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
title: Databricks Runtime ML Support
description: DeepSpeed is available in Databricks Runtime 14.0 ML and above, enabling distributed training with DeepSpeed on the Databricks platform.
tags:
  - databricks
  - version-support
  - runtime
timestamp: "2026-06-18T15:34:12.638Z"
---

# Databricks Runtime ML Support

**Databricks Runtime ML Support** refers to the pre-built runtime environment provided by Databricks that is optimized for machine learning and deep learning workloads. It includes GPU support, common deep learning libraries, and integrations with distributed training frameworks.

## Overview

Databricks Runtime for Machine Learning (Databricks Runtime ML) is a pre-configured runtime that includes GPU support and common deep learning libraries, enabling efficient execution of tasks such as training and tuning large language models, natural language processing, object detection and classification, and recommendation engines. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## GPU Support

Databricks Runtime ML supports NVIDIA A100 GPUs across all major cloud providers (AWS, Azure, GCP). These GPUs are recommended for high-performance deep learning tasks. For the complete list of supported GPU instance types, see the Databricks documentation on [supported instance types](https://docs.databricks.com/aws/en/compute/gpu#gpu-list). Availability of A100 GPUs may be limited; Databricks recommends contacting the cloud provider for resource allocation or reserving capacity in advance. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Distributed Training Frameworks

### DeepSpeed

The [DeepSpeed](https://deepspeed.readthedocs.io/en/latest/training.html) library, developed by Microsoft, is available in Databricks Runtime 14.0 ML and above. It provides optimized memory usage, reduced communication overhead, and advanced pipeline parallelism, allowing scaling of models and training procedures that would otherwise be unattainable on standard hardware. The DeepSpeed distributor is built on top of the [TorchDistributor](/concepts/torchdistributor.md) and is recommended for models that require higher compute power but are limited by memory constraints. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

### Fully Sharded Data Parallel (FSDP)

For models in the 20B to 120B+ parameter range, Databricks supports [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) to shard model parameters, gradients, and optimizer states across multiple GPUs, enabling training that would exceed single-GPU memory. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md] (Note: The source document for FSDP was referenced but its full content was not provided in the source material; this claim is drawn from the metadata of the "20B to 120B+ Parameter Model Training" page, which cites that source.)

## Related Concepts

- GPU Scheduling – Optimizing GPU utilization for distributed training and inference.
- [Deep learning best practices on Databricks](/concepts/deep-learning-best-practices-on-databricks.md) – General guidance for deep learning workflows.
- Supported GPU Types on Databricks – Full list of GPU instances available across clouds.
- [TorchDistributor](/concepts/torchdistributor.md) – Foundation for the DeepSpeed distributor on Databricks.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – Sharded data parallelism for large models.

## Sources

- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
- distributed-training-with-deepspeed-distributor-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md

# Citations

1. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
2. [distributed-training-with-deepspeed-distributor-databricks-on-aws.md](/references/distributed-training-with-deepspeed-distributor-databricks-on-aws-6ba03a5a.md)
3. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
