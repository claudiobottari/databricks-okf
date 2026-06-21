---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3f1491bd84627f91e7a4bc4944bee9e593d4b0f2f38439e649c36b4588589881
  pageDirectory: concepts
  sources:
    - fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
  confidence: 0.92
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mxfp4-quantization-for-model-loading
    - MQFML
  citations:
    - file: fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
title: Mxfp4 Quantization for Model Loading
description: A 4-bit floating point quantization format used to reduce memory footprint when loading large models (e.g., 120B parameters) into GPU memory during fine-tuning.
tags:
  - quantization
  - memory-optimization
  - deep-learning
timestamp: "2026-06-19T18:51:45.334Z"
---

# Mxfp4 Quantization for Model Loading

**Mxfp4 Quantization for Model Loading** is a memory-reduction technique used when loading large [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md) for [Fine-Tuning](/concepts/supervised-fine-tuning-sft.md) on [Serverless GPU Compute](/concepts/serverless-gpu-compute.md). It leverages the MXFP4 (Microscaling Floating Point 4-bit) data format to reduce the memory footprint of model weights during the loading process.

## Overview

When loading a model that is too large to fit into GPU memory in its native precision (e.g., bfloat16), MXFP4 quantization can be applied at load time to compress the model weights. The model is loaded in 4-bit precision and then dequantized back to the working precision on the target device. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Implementation

MXFP4 quantization is configured through the `Mxfp4Config` class from the Hugging Face `transformers` library. The key parameter is `dequantize`, which when set to `True`, loads the model in 4-bit format and immediately dequantizes it for training or inference. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

```python
from transformers import Mxfp4Config

quantization_config = Mxfp4Config(dequantize=True)
model = AutoModelForCausalLM.from_pretrained(
    HF_MODEL_NAME,
    dtype=torch.bfloat16,
    quantization_config=quantization_config,
    low_cpu_mem_usage=True,
)
```

The `low_cpu_mem_usage=True` flag is also recommended alongside MXFP4 quantization to further reduce host memory requirements when loading massive checkpoint files. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Use Case

MXFP4 quantization is particularly valuable for loading very large models (e.g., 120B parameters) onto [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) nodes. Without quantization, the raw bfloat16 weights of a 120B-parameter model would require approximately 240 GB of host memory for loading, far exceeding typical single-node CPU memory. MXFP4 reduces this to roughly 60 GB during the load phase. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Limitations

- MXFP4 quantization is applied **only during model loading**. After dequantization, the model operates in the specified working precision (e.g., bfloat16). It is not a training-time quantization technique. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]
- The `attn_implementation` and `use_cache` parameters must be set appropriately (e.g., `"eager"` and `False` respectively) when using MXFP4 loading in combination with gradient checkpointing. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – Used alongside MXFP4 loading to distribute the dequantized model across GPUs
- [Low-Rank Adaptation (LoRA)](/concepts/low-rank-adaptation-lora.md) – Fine-tuning technique often paired with quantized model loading
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – Alternative parallelism strategy for model training
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – Infrastructure where MXFP4 loading is commonly used
- Model Quantization – Broader concept of reducing numerical precision for efficiency

## Sources

- fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md

# Citations

1. [fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md](/references/fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws-9fff83fc.md)
