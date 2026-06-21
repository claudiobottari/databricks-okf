---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 18e712b3bdbc1b405c48d6018502ae5a94857c7f75051fb0b80db2205e5a646b
  pageDirectory: concepts
  sources:
    - fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cut-cross-entropy
    - CCE
  citations:
    - file: fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md
title: Cut Cross Entropy
description: A memory-efficient loss computation technique for large language models that reduces GPU memory usage during training by avoiding materialization of the full logit matrix
tags:
  - optimization
  - deep-learning
  - memory-efficiency
timestamp: "2026-06-19T18:51:42.880Z"
---

# Cut Cross-Entropy

**Cut Cross-Entropy** is a memory-efficient loss computation library for large language models that reduces GPU memory consumption during training by optimizing how cross-entropy loss is calculated in the backward pass. It is integrated with the [Axolotl](/concepts/axolotl.md) training framework through a plugin system. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Overview

Cross-entropy loss is a fundamental component in training language models, where the model predicts the next token in a sequence. For large models with massive vocabularies, the standard cross-entropy computation can consume significant GPU memory. Cut Cross-Entropy addresses this by using memory-efficient algorithms that avoid materializing the full logit tensor during the backward pass, making it particularly valuable for memory-constrained training environments. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Installation

Cut Cross-Entropy is available as a Python package and can be installed directly from its GitHub repository. For integration with the Transformers library, the `[transformers]` extra variant should be used. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

```bash
%pip install "cut-cross-entropy[transformers] @ git+https://github.com/axolotl-ai-cloud/ml-cross-entropy.git@f4b5712"
```

## Integration with Axolotl

In the Axolotl training framework, Cut Cross-Entropy is registered as a plugin that can be enabled in the training configuration. This allows the framework to apply the memory-efficient loss computation during model training without requiring manual integration of the loss function. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

The plugin is enabled by adding it to the `plugins` list in the Axolotl configuration:

```python
config = DictDefault(
    ...
    plugins=[
        "axolotl.integrations.cut_cross_entropy.CutCrossEntropyPlugin"
    ],
    ...
)
```

## Use Cases

Cut Cross-Entropy is particularly valuable for:

- **Large vocabulary models**: Models with extensive vocabularies where computing full logits for all tokens is memory-prohibitive.
- **Memory-constrained environments**: Training on GPU instances with limited memory, where every optimization helps fit larger batch sizes or model sizes.
- **Multi-GPU training**: Distributed training setups where memory efficiency per GPU is critical for scaling.

The technique is commonly used alongside [QLoRA](/concepts/qlora-quantized-low-rank-adaptation.md) (Quantized Low-Rank Adaptation) for efficient fine-tuning of large language models, as demonstrated in the Olmo3 7B Instruct model fine-tuning workflow on Databricks serverless GPU compute. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Related Concepts

- Cross-Entropy Loss — The standard loss function for language model training
- [Axolotl](/concepts/axolotl.md) — Training framework that integrates Cut Cross-Entropy as a plugin
- [QLoRA](/concepts/qlora-quantized-low-rank-adaptation.md) — Quantized Low-Rank Adaptation, often used alongside Cut Cross-Entropy
- [Memory-Efficient Training](/concepts/gradient-checkpointing-for-memory-efficient-training.md) — Broader category of techniques for reducing GPU memory usage
- [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md) — Primary models benefiting from this optimization

## Sources

- fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md

# Citations

1. [fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md](/references/fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws-c7178be1.md)
