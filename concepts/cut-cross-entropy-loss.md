---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 440202194855adada166ce60348b25e3f58943bd7f5326e7b6e3b72052cf7549
  pageDirectory: concepts
  sources:
    - fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cut-cross-entropy-loss
    - CCL
    - Cross-Entropy Loss
  citations:
    - file: fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md
title: Cut Cross-Entropy Loss
description: A memory-efficient loss computation technique for large language models, reducing GPU memory usage during training
tags:
  - machine-learning
  - optimization
  - loss-function
timestamp: "2026-06-18T12:21:37.306Z"
---

# Cut Cross-Entropy Loss

**Cut Cross-Entropy Loss** is a memory-efficient technique for computing the cross-entropy loss during training of large language models. It is implemented in the `cut-cross-entropy` Python package, which is designed to reduce the memory footprint of the loss computation step, enabling more efficient fine-tuning on GPU hardware.^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Usage in Fine-Tuning Pipelines

In practice, Cut Cross-Entropy Loss is integrated into LLM fine-tuning frameworks such as [Axolotl](/concepts/axolotl.md) via a dedicated plugin. For example, when fine-tuning the Olmo3 7B model with [QLoRA](/concepts/qlora-quantized-low-rank-adaptation.md) on multi-GPU serverless compute, the Axolotl configuration includes the plugin `axolotl.integrations.cut_cross_entropy.CutCrossEntropyPlugin`. This plugin replaces the default loss function with the cut-cross-entropy implementation during training.^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

The package is installed from its source repository using `pip` with the `transformers` extra:

```bash
pip install "cut-cross-entropy[transformers] @ git+https://github.com/axolotl-ai-cloud/ml-cross-entropy.git@f4b5712"
```

^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Relationship to Other Techniques

Cut Cross-Entropy Loss complements other memory-saving approaches such as [Flash Attention](/concepts/flash-attention.md) and [gradient checkpointing](/concepts/activation-checkpointing.md). While Flash Attention reduces the memory required by the attention mechanism, cut-cross-entropy focuses specifically on the loss computation step. Together, these techniques allow larger models to fit on available GPU memory and enable longer sequence lengths during training.^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Related Concepts

- Cross-Entropy Loss – The standard loss function used for classification and language modeling
- [QLoRA](/concepts/qlora-quantized-low-rank-adaptation.md) – Quantized Low-Rank Adaptation, a parameter-efficient fine-tuning method
- [Axolotl](/concepts/axolotl.md) – A high-performance framework for LLM post-training
- [Memory-Efficient Training](/concepts/gradient-checkpointing-for-memory-efficient-training.md) – General strategies for reducing GPU memory usage
- [Flash Attention](/concepts/flash-attention.md) – An attention algorithm that reduces memory and speeds up computation

## Sources

- fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md

# Citations

1. [fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md](/references/fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws-c7178be1.md)
