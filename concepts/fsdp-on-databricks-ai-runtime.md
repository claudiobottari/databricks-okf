---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6007796eb18de103b8f787b60e9b046e903ef6a6111355d44e48a63943c06dc2
  pageDirectory: concepts
  sources:
    - fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - fsdp-on-databricks-ai-runtime
    - FODAR
  citations:
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
title: FSDP on Databricks AI Runtime
description: Notebook-based examples and integration for running FSDP training workloads on Databricks AI Runtime on AWS
tags:
  - databricks
  - aws
  - training
timestamp: "2026-06-18T12:26:49.821Z"
---

# FSDP on Databricks AI Runtime

**FSDP on Databricks AI Runtime** refers to using [PyTorch Fully Sharded Data Parallel (FSDP)](/concepts/pytorch-fully-sharded-data-parallel-fsdp.md) to train large neural network models on GPU clusters managed by [Databricks AI Runtime](/concepts/databricks-ai-runtime.md). FSDP shards model parameters, gradients, and optimizer states across all available GPUs, enabling the training of very large models that would not fit into a single GPU's memory. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## When to Use FSDP

FSDP is recommended when your model is too large to fit in a single GPU's memory, or when you need to train models in the 20B to 120B+ parameter range and require greater memory efficiency than [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) can provide. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

For smaller models that fit comfortably in a single GPU’s memory, DDP offers simpler usage. If you need advanced memory optimization features beyond FSDP, consider DeepSpeed on Databricks AI Runtime|DeepSpeed. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## Examples

Databricks provides notebook examples that demonstrate FSDP training on AI Runtime. These notebooks show concrete configurations and workflows for running FSDP jobs on Databricks clusters with GPU hardware. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## Related Concepts

- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — Alternative distributed training strategy for models that fit in GPU memory
- [DeepSpeed on Databricks AI Runtime](/concepts/deepspeed-on-databricks.md) — Alternative with advanced memory optimization features
- [AI Runtime](/concepts/ai-runtime.md) — The optimized runtime environment for ML workloads on Databricks
- PyTorch FSDP Tutorial — Official PyTorch documentation for FSDP

## Sources

- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md

# Citations

1. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
