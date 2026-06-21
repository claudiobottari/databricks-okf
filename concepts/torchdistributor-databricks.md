---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1aa80dc56a3c14e5e4983d97bef14ef473319d79af5ca3a706cce6f7fb6f42f4
  pageDirectory: concepts
  sources:
    - distributed-training-with-deepspeed-distributor-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - torchdistributor-databricks
  citations:
    - file: distributed-training-with-deepspeed-distributor-databricks-on-aws.md
title: TorchDistributor (Databricks)
description: A base distributed training framework on Databricks for PyTorch models, upon which the DeepSpeed distributor is built.
tags:
  - distributed-training
  - databricks
  - pytorch
timestamp: "2026-06-19T18:37:20.103Z"
---

# TorchDistributor (Databricks)

**TorchDistributor** is a Databricks utility for performing distributed training on PyTorch machine learning models. It serves as the underlying component on which the [DeepSpeed](/concepts/deepspeed.md) distributor is built. The DeepSpeed distributor is a recommended solution for models that require higher compute power but are constrained by GPU memory, and it leverages the TorchDistributor as its foundation. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

The documentation for TorchDistributor is available in the Databricks guide on [Spark PyTorch Distributor](/concepts/torchdistributor.md). ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

## Related Concepts

- [DeepSpeed](/concepts/deepspeed.md) – An optimized distributed training library built on TorchDistributor.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – General approach to scaling ML workloads across multiple devices.
- PyTorch – The deep learning framework used with TorchDistributor.
- [Spark PyTorch Distributor](/concepts/torchdistributor.md) – The broader family of distributed training utilities on Databricks.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – Another memory-efficient training technique available on the platform.

## Sources

- distributed-training-with-deepspeed-distributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-deepspeed-distributor-databricks-on-aws.md](/references/distributed-training-with-deepspeed-distributor-databricks-on-aws-6ba03a5a.md)
