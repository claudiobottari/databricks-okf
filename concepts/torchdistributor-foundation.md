---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f2115352b4f05dff97930adffea6cf54edb0c24b73c6c1d043f0aa402c6344d3
  pageDirectory: concepts
  sources:
    - distributed-training-with-deepspeed-distributor-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - torchdistributor-foundation
  citations:
    - file: distributed-training-with-deepspeed-distributor-databricks-on-aws.md
title: TorchDistributor Foundation
description: The DeepSpeed distributor is built on top of TorchDistributor, which is Databricks' native Spark-based PyTorch distributed training solution.
tags:
  - databricks
  - pytorch
  - architecture
timestamp: "2026-06-18T15:33:49.586Z"
---

# TorchDistributor Foundation

**TorchDistributor Foundation** refers to the underlying distributed training framework that provides the core primitives for scaling PyTorch ML models across multiple GPUs and nodes. It serves as the base layer upon which higher-level distributors, such as the [DeepSpeed](/concepts/deepspeed.md) distributor, are built. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

## Overview

TorchDistributor is the foundational distributed training utility in the Databricks ecosystem. The DeepSpeed distributor is explicitly "built on top of TorchDistributor," meaning that DeepSpeed leverages TorchDistributor’s core distributed training capabilities while layering on advanced memory optimizations like [ZeRO optimization](/concepts/deepspeed-zero-stage-3.md), gradient checkpointing, and pipeline parallelism. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

## Relationship to DeepSpeed Distributor

The DeepSpeed distributor is a recommended solution for customers whose models "require higher compute power, but are limited by memory constraints." Because it is built on TorchDistributor, the TorchDistributor Foundation provides the essential distributed training infrastructure, while DeepSpeed extends it with reduced communication overhead and advanced parallelism techniques. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

## Supported Scenarios

Although TorchDistributor is a low-level framework, the scenarios where it is beneficial are those addressed by the DeepSpeed distributor built on top of it, including:

- Low GPU memory availability.
- Large model training.
- Large input data, such as during batch inference.

These scenarios illustrate the memory and scaling challenges that TorchDistributor (via DeepSpeed) helps overcome. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

## Availability

TorchDistributor is available as part of the distributed training infrastructure in Databricks Runtime. The DeepSpeed library, which builds on TorchDistributor, is available in Databricks Runtime 14.0 ML or above. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

## Related Concepts

- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- [DeepSpeed Distributor](/concepts/deepspeed-distributor.md)
- [PyTorch Distributed Data Parallel](/concepts/distributed-data-parallel-ddp.md)
- [ZeRO Optimization](/concepts/deepspeed-zero-stage-3.md)
- Model Parallelism

## Sources

- distributed-training-with-deepspeed-distributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-deepspeed-distributor-databricks-on-aws.md](/references/distributed-training-with-deepspeed-distributor-databricks-on-aws-6ba03a5a.md)
