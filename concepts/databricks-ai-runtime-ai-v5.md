---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8f904f674cec0496a4d8fefe803714b6816bba12ff7df343b1a27b19c0c5abcd
  pageDirectory: concepts
  sources:
    - distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-ai-runtime-ai-v5
    - DAR(V
  citations:
    - file: distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
title: Databricks AI Runtime (AI v5)
description: A Databricks environment image pre-packaged with AI/ML libraries including Unsloth, TRL, PEFT, bitsandbytes, xformers, and einops, eliminating manual installations.
tags:
  - databricks
  - runtime
  - machine-learning
  - infrastructure
timestamp: "2026-06-18T15:30:35.204Z"
---

---  
title: Databricks AI Runtime (AI v5)  
summary: Databricks' preconfigured environment for AI workloads that includes Unsloth, TRL, PEFT, bitsandbytes, xformers, einops, and supports 8xH100 GPU accelerators.  
sources:  
  - distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md  
kind: concept  
createdAt: "2026-06-18T12:04:07.106Z"  
updatedAt: "2026-06-18T12:04:07.106Z"  
tags:  
  - databricks  
  - infrastructure  
  - runtime  
aliases:  
  - databricks-ai-runtime-ai-v5  
  - DAR(V  
confidence: 0.95  
provenanceState: extracted  
inferredParagraphs: 1  
---  

# Databricks AI Runtime (AI v5)

The **Databricks AI Runtime (AI v5)** is a pre-configured base environment designed for GPU-accelerated machine learning workloads, particularly fine-tuning large language models. It bundles a curated stack of common deep learning and optimization libraries so that users can start training without manual dependency installation. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Included Libraries

AI v5 ships with [Unsloth](/concepts/unsloth.md) and its supporting ecosystem:

- `unsloth` – library for fast LLM fine-tuning
- `unsloth_zoo` – model zoo utilities
- `trl` – Transformer Reinforcement Learning
- `peft` – Parameter-Efficient Fine-Tuning (e.g., LoRA)
- `bitsandbytes` – quantization support
- `xformers` – memory-efficient attention
- `einops` – tensor operations

No additional `pip install` is required for these packages when the AI v5 environment is selected. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Usage

AI v5 is available as a base environment option in Databricks compute clusters. To use it:

1. In the cluster configuration panel, set **Base environment** to **AI v5**.
2. Select the desired accelerator (e.g., 8xH100). Provisioning may take several minutes.

The environment is typically chosen for distributed fine-tuning workflows that leverage multiple GPUs, such as training the Llama-3.2-3B model with Unsloth on 8 H100 GPUs. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Related Concepts

- [Unsloth](/concepts/unsloth.md) – core library for fast LLM fine‑tuning  
- [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md) – parameter‑efficient fine‑tuning technique  
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – scaling across multiple GPUs  
- [serverless_gpu](/concepts/serverless-gpu-compute.md) – Databricks library for distributed GPU execution  
- [MLflow](/concepts/mlflow.md) – experiment tracking and model registry  
- Llama-3.2-3B – example model fine‑tuned with AI v5  

## Sources

- distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md

# Citations

1. [distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md](/references/distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws-5c6e3457.md)
