---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c6d3b418d8638e9b822e88b358205a38fe514bb1199ffaaaa5a772a928943ee4
  pageDirectory: concepts
  sources:
    - multi-gpu-distributed-training-databricks-on-aws.md
    - multi-gpu-workload-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - deepspeed-on-databricks
    - DOD
    - DeepSpeed on Databricks AI Runtime
  citations:
    - file: multi-gpu-workload-databricks-on-aws.md
    - file: multi-gpu-distributed-training-databricks-on-aws.md
title: DeepSpeed on Databricks
description: A parallelism technique from Microsoft that provides ZeRO optimization stages and other memory-saving strategies for large-scale training on Databricks.
tags:
  - parallelism
  - deep-learning
  - databricks
timestamp: "2026-06-19T19:47:32.045Z"
---

# DeepSpeed on Databricks

**DeepSpeed** is Microsoft’s optimization library for large‑model training and is one of the three parallelism techniques natively supported on Databricks for multi‑GPU distributed workloads. ^[multi-gpu-workload-databricks-on-aws.md, multi-gpu-distributed-training-databricks-on-aws.md]

## Overview

On Databricks, DeepSpeed can be used with the serverless_gpu Python API to distribute training across multiple GPUs. The API supports DeepSpeed alongside [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) and [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md). ^[multi-gpu-workload-databricks-on-aws.md]

DeepSpeed is particularly suited for large models that benefit from advanced memory optimization techniques, such as ZeRO (Zero Redundancy Optimizer). ^[multi-gpu-workload-databricks-on-aws.md] (Note: ZeRO is mentioned as part of DeepSpeed's capabilities, though the source only describes it as “Microsoft’s optimization library for large model training”.)

## Infrastructure Requirements

Multi‑GPU distributed training with DeepSpeed requires an **8xH100 accelerator**, which provisions a single node with eight NVIDIA H100 80 GB GPUs. When using the `@distributed` decorator, you must set `gpus=8` and `gpu_type='H100'`. ^[multi-gpu-workload-databricks-on-aws.md]

## Using DeepSpeed with the `@distributed` Decorator

The `serverless_gpu` library provides a `@distributed` decorator that handles resource provisioning, environment setup, and workload distribution. To use DeepSpeed:

1. Import `serverless_gpu` and the `distributed` decorator.
2. Decorate your training function with `@distributed(gpus=8, gpu_type='H100')`.
3. Inside the function, initialize DeepSpeed engine and training logic.

A general pattern for using any supported parallelism library (including DeepSpeed) is shown in the [official quick‑start guide](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/distributed-training#quick-start). The same API also supports DeepSpeed directly. ^[multi-gpu-workload-databricks-on-aws.md]

For a complete DeepSpeed example, see the Multi-GPU distributed training examples notebook. ^[multi-gpu-distributed-training-databricks-on-aws.md]

## Related Concepts

- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The underlying infrastructure that provisions GPUs on demand.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) — The specific GPU setup used for multi‑node distributed training.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — A simpler data‑parallelism technique for models that fit in GPU memory.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — A memory‑efficient sharding technique, an alternative to DeepSpeed.

## Sources

- multi-gpu-workload-databricks-on-aws.md
- multi-gpu-distributed-training-databricks-on-aws.md

# Citations

1. [multi-gpu-workload-databricks-on-aws.md](/references/multi-gpu-workload-databricks-on-aws-c6af01f5.md)
2. [multi-gpu-distributed-training-databricks-on-aws.md](/references/multi-gpu-distributed-training-databricks-on-aws-acaa7a08.md)
