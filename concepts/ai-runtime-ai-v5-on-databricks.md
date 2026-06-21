---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea2fdd6f133656effb423e6121d3443402b82ebfcecdded6862801e45653bdfc
  pageDirectory: concepts
  sources:
    - distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-ai-v5-on-databricks
    - AR(VOD
    - Generative AI on Databricks
  citations:
    - file: distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
title: AI Runtime (AI v5) on Databricks
description: Databricks' pre-configured environment for AI workloads, bundling Unsloth, TRL, PEFT, bitsandbytes, xformers, and other LLM finetuning dependencies.
tags:
  - databricks
  - environment
  - machine-learning
timestamp: "2026-06-19T10:15:59.425Z"
---

# AI Runtime (AI v5) on Databricks

**AI Runtime (AI v5)** is a pre-configured environment in Databricks designed for deep learning and generative AI workloads. It includes the Unsloth library and its supporting stack, enabling efficient fine-tuning of LLMs such as Llama‑3.2‑3B on multi‑GPU clusters.

## Overview

AI Runtime (commonly referred to as AI v5) is one of the base environment options in Databricks. When selected together with an appropriate GPU accelerator (e.g., 8× H100), it provides all necessary dependencies for distributed training without requiring additional package installations. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Included Libraries

The AI v5 environment ships with Unsloth and its supporting stack, which includes:

- `unsloth` – Optimized fast fine-tuning library
- `unsloth_zoo` – Model zoo utilities for Unsloth
- `trl` – Transformer Reinforcement Learning library
- `peft` – Parameter‑Efficient Fine‑Tuning
- `bitsandbytes` – Quantization and low‑precision operations
- `xformers` – Memory‑efficient attention mechanisms
- `einops` – Einstein‑style tensor operations

^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Usage

To use AI Runtime v5, select it as the **Base environment** when configuring a Databricks cluster or notebook environment, then choose an appropriate GPU accelerator (e.g., `8xH100`). After applying, the environment is ready for distributed fine‑tuning workloads such as the Llama‑3.2‑3B example notebook. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Key Features

- **No manual setup**: All Unsloth dependencies are pre‑installed, reducing setup time.
- **Distributed training support**: Works with the `serverless_gpu` library and its `@distributed` decorator to scale across multiple GPUs.
- **Integration with MLflow and Unity Catalog**: Models fine‑tuned in AI v5 can be logged and registered directly to [Unity Catalog](/concepts/unity-catalog.md) for governance and deployment.
- **Optimized for performance**: Includes Liger Kernels, LoRA, and quantization support (4‑bit and 8‑bit) out of the box. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Related Concepts

- [Unsloth](/concepts/unsloth.md) – The core library for fast LLM fine‑tuning included in AI v5.
- [Serverless GPU on Databricks](/concepts/serverless-gpu-compute-on-databricks.md) – The infrastructure layer that provisions GPU clusters for distributed training.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – Scaling model training across multiple GPUs or nodes.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – The traditional ML runtime; AI Runtime is a newer, AI‑focused variant.
- [Unity Catalog](/concepts/unity-catalog.md) – Governance and model registry integration.

## Sources

- distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md

# Citations

1. [distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md](/references/distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws-5c6e3457.md)
