---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 654b74cf7cd9bb6880e9f20d04a0a7f306beab0fd6d3046cab02e23ae106fb13
  pageDirectory: concepts
  sources:
    - fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md
  confidence: 0.94
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - flash-attention
    - FlashAttention
  citations:
    - file: fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md
      start: 70
      end: 73
    - file: fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md
      start: 142
      end: 142
title: Flash Attention
description: An optimized attention mechanism that accelerates transformer training and inference by reducing memory reads/writes, distributed as a prebuilt wheel to avoid slow compilation from source.
tags:
  - attention-mechanism
  - gpu-optimization
  - transformers
timestamp: "2026-06-19T10:33:09.206Z"
---

# Flash Attention

**Flash Attention** is an optimized attention implementation used in large language model (LLM) training and fine-tuning. In the context of the notebook for fine-tuning Llama 3.1 8B using Mosaic LLM Foundry on Databricks Serverless GPU, Flash Attention is installed as a prebuilt wheel and configured to accelerate the attention computation during distributed training. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md#L70-L73]

## Installation

The notebook installs Flash Attention from a prebuilt wheel **before** installing `llm-foundry[gpu]` so that `pip` reuses the prebuilt binary instead of compiling Flash Attention from source, which would be slow.^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md#L70-L73] The wheel is fetched directly from the GitHub releases of the Flash Attention repository:

```bash
%pip install --no-deps "https://github.com/Dao-AILab/flash-attention/releases/download/v2.7.4.post1/flash_attn-2.7.4.post1+cu12torch2.6cxx11abiFALSE-cp312-cp312-linux_x86_64.whl"
```

## Configuration

Flash Attention is enabled in the YAML training configuration by setting `use_flash_attention_2: true` under the model section. This tells the training framework (LLM Foundry) to use the Flash Attention kernel for efficient self-attention computation.^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md#L142]

```yaml
model:
  use_flash_attention_2: true
```

## Usage Context

Flash Attention is used during the fine‑tuning of a Llama 3.1 8B model with [FSDP (Fully Sharded Data Parallel)](/concepts/fsdp-fully-sharded-data-parallel.md) on 8 H100 GPUs. The training runs on [Databricks Serverless GPU](/concepts/databricks-serverless-gpu.md) compute, and the model checkpoints are saved to [Unity Catalog](/concepts/unity-catalog.md). The notebook metadata describes Flash Attention as an "Optimized attention implementation".^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md#L70-L73]

## Related Concepts

- [Mosaic LLM Foundry](/concepts/mosaic-llm-foundry.md) — The framework that integrates Flash Attention for training and fine‑tuning.
- [FSDP (Fully Sharded Data Parallel)](/concepts/fsdp-fully-sharded-data-parallel.md) — Distributed training strategy used alongside Flash Attention.
- [Databricks Serverless GPU](/concepts/databricks-serverless-gpu.md) — The compute environment where Flash Attention is deployed.
- Llama 3.1 8B — The model that is fine‑tuned with Flash Attention enabled.
- [Fine-tuning Large Language Models](/concepts/fine-tuning-large-language-models-with-ai-runtime.md) — The broader process that benefits from optimized attention.

## Sources

- fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md

# Citations

1. [fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md:70-73](/references/fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws-d6760424.md)
2. [fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md:142-142](/references/fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws-d6760424.md)
