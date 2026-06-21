---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d9737e07fb835b4f2e435ca2da72c13f1beef57109f08184b5c2611aaf2b07e8
  pageDirectory: concepts
  sources:
    - distributed-training-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deepspeed-distributor-on-databricks
    - DDOD
  citations:
    - file: distributed-training-databricks-on-aws.md
title: DeepSpeed Distributor on Databricks
description: A Microsoft open-source library integrated with Databricks for distributed training with optimized memory usage, reduced communication overhead, and pipeline parallelism.
tags:
  - deepspeed
  - distributed-training
  - memory-optimization
timestamp: "2026-06-18T12:04:28.116Z"
---

---
title: DeepSpeed Distributor on Databricks
summary: A distributed training solution built on TorchDistributor that leverages Microsoft’s DeepSpeed library for memory‑optimized, high‑performance training of large neural networks on Databricks clusters.
sources:
  - distributed-training-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:13:19.509Z"
updatedAt: "2026-06-18T08:13:19.509Z"
tags:
  - distributed-training
  - deepspeed
  - pytorch
  - databricks
  - machine-learning
aliases:
  - deepspeed-distributor-on-databricks
  - DSD
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# DeepSpeed Distributor on Databricks

The **DeepSpeed Distributor** is a distributed training component included in [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) that helps you train large neural networks across multiple worker nodes. It is built on top of the [TorchDistributor](/concepts/torchdistributor.md) module in PySpark and is recommended for workloads that require high compute power but are limited by memory constraints. ^[distributed-training-databricks-on-aws.md]

## Overview

DeepSpeed is an open‑source library developed by Microsoft that extends PyTorch with optimizations for large‑scale model training. The DeepSpeed Distributor on Databricks packages these capabilities so that you can run DeepSpeed‑enabled training jobs as Spark jobs, leveraging the same cluster infrastructure used for data processing. ^[distributed-training-databricks-on-aws.md]

## Key Benefits

The DeepSpeed Distributor provides several advantages for memory‑bound training scenarios: ^[distributed-training-databricks-on-aws.md]

- **Optimized memory usage** — Techniques such as ZeRO (Zero Redundancy Optimizer) reduce the memory footprint of model parameters, gradients, and optimizer states.
- **Reduced communication overhead** — Efficient communication patterns minimize the time spent synchronizing gradients across workers.
- **Advanced pipeline parallelism** — Models that do not fit on a single GPU can be split across multiple devices, with stages executed in a pipelined fashion.

## Relationship to TorchDistributor

The DeepSpeed Distributor is built directly on [TorchDistributor](/concepts/torchdistributor.md), an open‑source PySpark module that launches PyTorch training jobs as Spark jobs. Under the hood, TorchDistributor initializes the environment, sets up communication channels, and uses the `torch.distributed.run` CLI command to distribute training across worker nodes. The DeepSpeed Distributor adds DeepSpeed‑specific optimizations on top of this foundation. ^[distributed-training-databricks-on-aws.md]

## When to Use the DeepSpeed Distributor

Databricks generally recommends training neural networks on a single machine because distributed code is more complex and incurs communication overhead. However, you should consider the DeepSpeed Distributor when: ^[distributed-training-databricks-on-aws.md]

- The model size exceeds the memory capacity of a single GPU or node.
- The dataset is too large to fit in memory on a single machine.
- Higher compute power is required but memory becomes the limiting factor.

## Other Distributed Training Options on Databricks

In addition to the DeepSpeed Distributor, [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) includes: ^[distributed-training-databricks-on-aws.md]

- **[TorchDistributor](/concepts/torchdistributor.md)** — For general‑purpose distributed PyTorch training without DeepSpeed optimizations.
- **Ray** — An open‑source framework for parallel compute processing and scaling ML workflows.
- **Spark ML** (via `pyspark.ml.connect`) — For distributed training of Spark ML models, available natively in Databricks Runtime 17.0 and above.

## Getting Started

For detailed instructions on using the DeepSpeed Distributor, see the official Databricks documentation: [Distributed training with DeepSpeed distributor](https://docs.databricks.com/aws/en/machine-learning/train-model/distributed-training/deepspeed). ^[distributed-training-databricks-on-aws.md]

## Sources

- distributed-training-databricks-on-aws.md

# Citations

1. [distributed-training-databricks-on-aws.md](/references/distributed-training-databricks-on-aws-826bf389.md)
