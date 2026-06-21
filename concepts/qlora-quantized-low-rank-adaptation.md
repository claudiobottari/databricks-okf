---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 033ce5edd34d2e6c8dedee5b29d4067e9aa9e34b9ad431f16d70c05f4e09aa66
  pageDirectory: concepts
  sources:
    - fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - qlora-quantized-low-rank-adaptation
    - Q(LA
    - Q-LoRA
    - QLoRA
  citations:
    - file: fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md
title: QLoRA (Quantized Low-Rank Adaptation)
description: A parameter-efficient fine-tuning technique that combines 4-bit quantization with low-rank adapter matrices to enable efficient LLM fine-tuning on consumer-grade hardware
tags:
  - machine-learning
  - fine-tuning
  - optimization
timestamp: "2026-06-19T18:51:05.172Z"
---

# QLoRA (Quantized Low-Rank Adaptation)

**QLoRA (Quantized Low-Rank Adaptation)** is a parameter-efficient fine-tuning technique that combines 4‑bit base-model quantization with low‑rank adapters (LoRA) to reduce memory usage while retaining most of the fine‑tuning quality. QLoRA enables fine‑tuning of large language models (LLMs) such as Olmo3 7B on consumer‑grade GPUs and multi‑GPU serverless infrastructure where full‑precision training is infeasible. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## How It Works

QLoRA builds on LoRA by first quantizing the base model’s weights to 4‑bit precision (configured via `load_in_4bit=True`). This step drastically reduces the memory footprint of the frozen base model. During training, only low‑rank adapter matrices are updated; the base model weights remain untouched. The adapters are applied to selected linear projection layers, such as `q_proj`, `v_proj`, `k_proj`, and `o_proj`. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

Typical QLoRA hyperparameters include a LoRA rank of 32 (`lora_r=32`) and a scaling factor of 16 (`lora_alpha=16`), with a dropout of 0.05 to regularize the adapters. The quantization is often paired with the [Cut Cross Entropy](/concepts/cut-cross-entropy.md) package for memory‑efficient loss computation. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Benefits

- **Reduced memory footprint**: 4‑bit quantization of the base model lowers GPU memory requirements compared to 16‑bit or 8‑bit training, allowing larger models to fit on available hardware. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]
- **Parameter efficiency**: Only the low‑rank adapters (a tiny fraction of the base model’s parameters) are updated, which speeds up training and simplifies checkpoint storage. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]
- **Compatibility with multi‑GPU setups**: QLoRA works well with distributed training frameworks such as [Axolotl](/concepts/axolotl.md)’s `@distributed` decorator on [Databricks Serverless GPU](/concepts/databricks-serverless-gpu.md) compute, scaling easily across 8 H100 GPUs. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Usage with Axolotl

The [Axolotl](/concepts/axolotl.md) training framework natively supports QLoRA. A typical configuration includes:

- Setting `load_in_4bit=True` and `adapter="qlora"`. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]
- Defining LoRA target modules (`lora_target_modules`), such as `gate_proj`, `down_proj`, `up_proj`, `q_proj`, `v_proj`, `k_proj`, and `o_proj`. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]
- Using `lora_target_linear=True` to automatically apply adapters to all linear layers. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

Additional training settings include a cosine learning rate scheduler with a learning rate of 0.0002, gradient accumulation over 4 steps, and the `adamw_bnb_8bit` optimizer. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Databricks Integration

On the Databricks platform, QLoRA fine‑tuning with Axolotl integrates with:

- [MLflow](/concepts/mlflow.md) for experiment tracking (`use_mlflow=True`, `mlflow_tracking_uri="databricks"`). ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]
- [Unity Catalog](/concepts/unity-catalog.md) volumes for checkpoint storage and model registration. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]
- [Scaled Dot Product Attention (SDPA)](/concepts/scaled-dot-product-attention-sdpa.md) (`attn_implementation="sdpa"`) for efficient attention computation, with optional [Flash Attention](/concepts/flash-attention.md) support. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

After training, the LoRA adapter is merged with the base model using `peft_model.merge_and_unload()` and registered as a Unity Catalog model for deployment. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Related Concepts

- LoRA – Low‑Rank Adaptation, the foundation of QLoRA.
- [Quantization](/concepts/mxfp4-quantization.md) – Reducing model weight precision (e.g., 4‑bit).
- [Axolotl](/concepts/axolotl.md) – High‑performance LLM post‑training framework.
- [Cut Cross Entropy](/concepts/cut-cross-entropy.md) – Memory‑efficient loss computation.
- [MLflow](/concepts/mlflow.md) – Experiment tracking and model registry.
- [Unity Catalog](/concepts/unity-catalog.md) – Governance and model registration.
- [Flash Attention](/concepts/flash-attention.md) – Efficient attention mechanism.
- [Scaled Dot Product Attention (SDPA)](/concepts/scaled-dot-product-attention-sdpa.md) – Attention implementation compatible with QLoRA.

## Sources

- fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md

# Citations

1. [fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md](/references/fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws-c7178be1.md)
