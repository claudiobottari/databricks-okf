---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ac060f11eeeca253b16bc4b6d9da3c0f0f1b4d93bd0b6a0ae9013543417b0e3c
  pageDirectory: concepts
  sources:
    - distributed-training-with-deepspeed-distributor-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pipeline-parallelism-in-deepspeed
    - PPID
    - Pipeline Parallelism
    - Pipeline parallelism
    - pipeline parallelism
  citations:
    - file: distributed-training-with-deepspeed-distributor-databricks-on-aws.md
title: Pipeline Parallelism in DeepSpeed
description: An advanced parallelism technique in DeepSpeed that partitions model layers across multiple devices to enable training of models that exceed single-device memory capacity.
tags:
  - parallelism
  - deep-learning
  - optimization
timestamp: "2026-06-18T12:08:02.119Z"
---

# Pipeline Parallelism in DeepSpeed

**Pipeline Parallelism in DeepSpeed** refers to the advanced technique for distributing the layers of a deep neural network across multiple devices, enabling training of models that are too large to fit into the memory of a single GPU. The DeepSpeed library, an open-source library developed by Microsoft, includes pipeline parallelism as one of its optimization capabilities. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

## Overview

DeepSpeed’s pipeline parallelism is part of a broader set of optimizations that also include optimized memory usage and reduced communication overhead. These features allow scaling of models and training procedures that would otherwise be unattainable on standard hardware. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

The [DeepSpeed Distributor](/concepts/deepspeed-distributor.md) built on top of the [TorchDistributor](/concepts/torchdistributor.md) is a recommended solution for customers whose models require higher compute power but are limited by memory constraints. Pipeline parallelism directly addresses these constraints by partitioning model layers across GPUs, so each device holds only a subset of the total parameters. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

## How Pipeline Parallelism Works

Pipeline parallelism splits the model into stages, each assigned to a different GPU. During training, micro-batches of data flow sequentially through these stages. While one stage processes a micro-batch, other stages can simultaneously process previous or subsequent micro-batches, improving hardware utilization. The exact implementation details of DeepSpeed’s pipeline parallelism are part of the DeepSpeed library, which is available in Databricks Runtime 14.0 ML and above. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

## Benefits

The primary benefit of pipeline parallelism in DeepSpeed is its ability to handle models that exceed the memory capacity of a single GPU. Combined with other optimizations, it reduces the communication overhead between devices and enables efficient scaling of training across multiple GPUs. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

## Example Scenarios Where Pipeline Parallelism Is Beneficial

The DeepSpeed distributor, which leverages pipeline parallelism, is particularly useful in the following scenarios: ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

- **Low GPU memory** — When available GPU memory is insufficient to hold the entire model.
- **Large model training** — For models with billions of parameters that cannot fit on a single device.
- **Large input data** — For tasks such as batch inference where the input data or intermediate activations are large.

## Sources

- distributed-training-with-deepspeed-distributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-deepspeed-distributor-databricks-on-aws.md](/references/distributed-training-with-deepspeed-distributor-databricks-on-aws-6ba03a5a.md)
