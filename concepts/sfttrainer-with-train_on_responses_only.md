---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f372e605051e737f6928230136af64115947923cbeddfeb3ec63bce43892a3bd
  pageDirectory: concepts
  sources:
    - distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sfttrainer-with-train_on_responses_only
    - SWT
  citations:
    - file: distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
title: SFTTrainer with train_on_responses_only
description: A training approach using TRL's SFTTrainer combined with Unsloth's train_on_responses_only utility to mask instruction parts and train only on assistant responses.
tags:
  - machine-learning
  - training
  - trl
  - supervised-finetuning
timestamp: "2026-06-18T15:30:24.398Z"
---

# SFTTrainer with `train_on_responses_only`

**`SFTTrainer` with `train_on_responses_only`** is a pattern used with the [Unsloth](/concepts/unsloth.md) library to fine-tune a language model so that the loss is computed only on the assistant (response) tokens of a conversation, ignoring the instruction or user turns. This focuses the model’s learning on generating useful completions rather than on predicting the input prompt.

## Source Material

The source material is a Databricks notebook that distributedly fine-tunes `Llama-3.2-3B` using Unsloth and 8 H100 GPUs. The notebook explicitly imports `train_on_responses_only` from `unsloth.chat_templates` and applies it to an `SFTTrainer` instance from the [TRL](/concepts/trl-transformer-reinforcement-learning-library.md) library. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### Import

```python
from unsloth.chat_templates import get_chat_template, standardize_sharegpt, train_on_responses_only
```

### Application

After creating the `SFTTrainer`, the function is called to wrap the trainer and restrict loss computation to the response portion of the training data: ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

```python
trainer = train_on_responses_only(
    trainer,
    instruction_part="<|start_header_id|>user<|end_header_id|>\n\n",
    response_part="<|start_header_id|>assistant<|end_header_id|>\n\n",
    num_proc=1
)
```

## Parameters

Based on the usage in the source, the function accepts:

- **`trainer`** – An existing `SFTTrainer` instance to be modified.
- **`instruction_part`** – The token delimiter that marks the beginning of the user/instruction turn. In the example, this is the Llama 3.1 chat template user header.
- **`response_part`** – The token delimiter that marks the beginning of the assistant/response turn.
- **`num_proc`** – The number of processes to use for pre-processing. In the example, it is set to `1`.

The function configures the trainer to compute the language modeling loss only over tokens that follow the `response_part` delimiter, effectively training the model to produce better assistant replies while ignoring the instruction portion of the loss.

## Context in the Notebook

The notebook uses `train_on_responses_only` after preparing the dataset with `get_chat_template` and `standardize_sharegpt`, and just before calling `trainer.train()`. This is a common workflow in Unsloth-based fine-tuning to prevent the model from overfitting to the prompt structure. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Related Concepts

- [Unsloth](/concepts/unsloth.md) – The library providing `train_on_responses_only`.
- [SFTTrainer](/concepts/sfttrainer.md) – The TRL trainer used for supervised fine-tuning.
- [TRL (Transformer Reinforcement Learning)](/concepts/trl-transformer-reinforcement-learning.md) – The library that defines the base trainer.
- Chat Templates – How conversation turns are structured with special tokens.
- Loss Masking – The general technique of ignoring certain tokens during loss computation.

## Sources

- distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md

# Citations

1. [distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md](/references/distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws-5c6e3457.md)
