---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 116dd87bc1565e9c8025d05724f79c31ffd005f7d64d8a0db44b3d25e59a7d06
  pageDirectory: concepts
  sources:
    - fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - olmo3-7b-instruct-model
    - O7IM
  citations:
    - file: fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md
title: Olmo3 7B Instruct Model
description: An open-source 7 billion parameter instruction-tuned language model from Allen AI, used as the base for fine-tuning
tags:
  - llm
  - open-source
  - allen-ai
timestamp: "2026-06-18T12:21:57.820Z"
---

# Olmo3 7B Instruct Model

The **Olmo3 7B Instruct Model** is a 7-billion-parameter instruction-tuned language model developed by Allen AI, available on the HuggingFace Hub as `allenai/Olmo-3-7B-Instruct-SFT`. It is designed for dialogue and instruction-following tasks and can be fine-tuned efficiently with [QLoRA](/concepts/qlora-quantized-low-rank-adaptation.md) (Quantized Low-Rank Adaptation) using the [Axolotl](/concepts/axolotl.md) framework on Databricks serverless GPU compute. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Fine-tuning with Axolotl on Databricks

A typical fine-tuning workflow on Databricks uses [Axolotl](/concepts/axolotl.md) version 0.13.1 with Flash Attention support and the `cut-cross-entropy` package for memory-efficient loss computation. The process requires serverless GPU compute—specifically an 8×H100 accelerator—and an AI v5 environment. The HuggingFace authentication token is retrieved from Databricks secrets to download the base model. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Training Configuration

The training configuration, based on the [olmo3-7b-qlora.yaml](https://github.com/axolotl-ai-cloud/axolotl/blob/main/examples/olmo3/olmo3-7b-qlora.yaml) example, uses the following key parameters:

- **Quantization**: 4-bit (QLoRA)
- **LoRA rank**: 32, **alpha**: 16, **dropout**: 0.05
- **Target modules**: gate_proj, down_proj, up_proj, q_proj, v_proj, k_proj, o_proj (all linear layers)
- **Dataset**: `fozziethebeat/alpaca_messages_2k_test` in chat template format
- **Validation split**: 10% of the dataset
- **Sequence length**: 2048 tokens with sample packing
- **Training**: 1 epoch, micro batch size 2, gradient accumulation 4, maximum 16 steps for the demonstration
- **Optimizer**: AdamW 8-bit, cosine learning rate scheduler, initial learning rate 0.0002, warmup ratio 0.1
- **Attention**: SDPA (Scaled Dot Product Attention) instead of Flash Attention for broader GPU compatibility
- **Gradient checkpointing**: enabled
- **Logging**: MLflow integration (`use_mlflow=True`, `mlflow_tracking_uri="databricks"`, run name `olmo3-7b-qlora-axolotl`)
- **Checkpoint output**: written to a [Unity Catalog](/concepts/unity-catalog.md) volume path

The `CutCrossEntropyPlugin` is enabled to reduce GPU memory usage during training. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Distributed Training Setup

The training job is distributed across 8 H100 GPUs using Databricks’ serverless GPU API. The `@distributed` decorator from `serverless_gpu.launcher` handles multi-GPU orchestration without requiring manual cluster setup. PyTorch CUDA memory allocation is optimized for efficient multi-GPU training. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Model Registration and Deployment

After training, the LoRA adapter is merged into the base model using `PeftModel.merge_and_unload()`. The merged model is then logged to [MLflow](/concepts/mlflow.md) and registered in Unity Catalog via `mlflow.transformers.log_model()`, which creates a registered model version. The registration requires H100 GPU compute to load the model checkpoint; smaller GPUs may cause CUDA out-of-memory errors. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

The resulting Unity Catalog model path follows the format `catalog.schema.model_name`. After registration, the model is available for deployment and inference from Databricks serving endpoints. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Related Concepts

- [Axolotl](/concepts/axolotl.md) – High-performance framework for LLM post-training
- [QLoRA](/concepts/qlora-quantized-low-rank-adaptation.md) – Quantized Low-Rank Adaptation for efficient fine-tuning
- [MLflow](/concepts/mlflow.md) – Experiment tracking and model registry
- [Unity Catalog](/concepts/unity-catalog.md) – Data governance and model lineage
- HuggingFace Hub – Model source repository
- [Databricks Serverless GPU Compute](/concepts/databricks-serverless-gpu.md) – Multi-GPU infrastructure for training
- [Cut Cross Entropy](/concepts/cut-cross-entropy.md) – Memory-efficient loss computation
- [SDPA Attention](/concepts/sdpa-scaled-dot-product-attention.md) – Scaled Dot Product Attention implementation

## Sources

- fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md

# Citations

1. [fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md](/references/fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws-c7178be1.md)
