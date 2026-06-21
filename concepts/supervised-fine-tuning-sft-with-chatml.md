---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 789cc1bcf780407192c509643b9eb0c57b23fc92bed0812bef2154554675438d
  pageDirectory: concepts
  sources:
    - lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md
  confidence: 0.94
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - supervised-fine-tuning-sft-with-chatml
    - SF(WC
  citations:
    - file: lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md
title: Supervised Fine-Tuning (SFT) with ChatML
description: The process of fine-tuning a causal language model on structured conversational datasets using the ChatML format for instruction-following behavior.
tags:
  - machine-learning
  - fine-tuning
  - conversational-ai
timestamp: "2026-06-19T19:18:57.043Z"
---

# Supervised Fine-Tuning (SFT) with ChatML

**Supervised Fine-Tuning (SFT) with ChatML** is a technique for adapting a pre-trained large language model (LLM) to follow conversational instructions by training it on structured dialogue data formatted using the **ChatML** (Chat Markup Language) template. On Databricks, this approach is commonly paired with parameter-efficient methods such as LoRA and optimized kernels (e.g., [Liger Kernels](/concepts/liger-kernels.md)) to reduce memory and training time.

## Overview

In supervised fine-tuning, a pre-trained model is further trained on labeled examples to improve its performance on a specific task. When the task is conversational – such as instruction following or chatbot interaction – the training data is often formatted using a chat template that marks speaker turns and system instructions. ChatML provides a standardized structure for this, using special tokens like `<|im_start|>` and `<|im_end|>` to delineate roles (system, user, assistant) and message boundaries. ^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

## Applying ChatML for SFT

In the Databricks environment, applying ChatML to an SFT pipeline typically involves two steps:

1. **Loading the base model and tokenizer** – The model (e.g., `Qwen/Qwen2-0.5B`) and its tokenizer are loaded from Hugging Face. ^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]
2. **Setting up the chat format** – If the tokenizer does not already have a chat template, the `setup_chat_format` function from the [TRL](/concepts/trl-transformer-reinforcement-learning-library.md) library is called with `format="chatml"`. This applies the ChatML token structure so that dataset conversations are correctly tokenized and interpreted by the model during training. ^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

The following snippet illustrates the setup:

```python
from trl import setup_chat_format

if tokenizer.chat_template is None:
    model, tokenizer = setup_chat_format(model, tokenizer, format="chatml")
```

This ensures that every training example from a conversational dataset (such as the `trl-lib/Capybara` dataset) is automatically formatted with ChatML role markers, enabling the model to learn proper turn‑taking and instruction‑following behavior. ^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

## Training Pipeline

Once the ChatML format is applied, the model can be trained using [TRL](/concepts/trl-transformer-reinforcement-learning-library.md)’s `SFTTrainer`. The trainer handles the supervised fine‑tuning loop and can be configured with:

- **LoRA adapters** – Freezing the base model and training only small adapter matrices on the attention and MLP layers, reducing trainable parameters by ~99%. ^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]
- **Liger Kernels** – Fused GPU operations that reduce memory usage by up to 80%, enabling larger batch sizes or larger models on a single GPU. ^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]
- **Mixed precision (FP16)** – Faster computation while maintaining model quality. ^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

After training, the model (or LoRA adapters) can be saved and registered in [Unity Catalog](/concepts/unity-catalog.md) for governance and deployment, with the task type set to `llm/v1/chat` to denote its conversational purpose. ^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

## Benefits of ChatML for SFT

- **Structured conversations** – ChatML clearly separates system instructions, user inputs, and assistant responses, which helps the model learn to respect role boundaries. ^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]
- **Data consistency** – Applying the same chat template to all training examples ensures that the tokenizer processes each example uniformly, avoiding common issues with padding and attention masks. ^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]
- **Interoperability** – Models fine‑tuned with ChatML can be directly deployed to inference endpoints that expect chat‑formatted requests, such as the `llm/v1/chat` task in Databricks Model Serving. ^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

## Related Concepts

- [Supervised Fine-Tuning (SFT)](/concepts/supervised-fine-tuning-sft.md)
- ChatML
- LoRA
- [Liger Kernels](/concepts/liger-kernels.md)
- [TRL](/concepts/trl-transformer-reinforcement-learning-library.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Model Serving](/concepts/model-serving.md)

## Sources

- lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md

# Citations

1. [lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md](/references/lora-fine-tuning-of-qwen2-05b-databricks-on-aws-e40ade8f.md)
