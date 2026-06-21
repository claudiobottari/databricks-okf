---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a61d8e6776907c158ea0a01efe1113579e844159f79d8efafc8c4bbcdda64939
  pageDirectory: concepts
  sources:
    - finetune-llama-32-3b-with-unsloth-databricks-on-aws.md
  confidence: 0.92
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - response-only-training-with-chat-templates
    - RTWCT
  citations:
    - file: finetune-llama-32-3b-with-unsloth-databricks-on-aws.md
title: Response-Only Training with Chat Templates
description: A training strategy that masks or ignores user/prompt tokens during supervised fine-tuning, so the model only learns to predict assistant responses, improving training efficiency and focus.
tags:
  - machine-learning
  - training
  - nlp
timestamp: "2026-06-18T12:22:46.259Z"
---

# Response-Only Training with Chat Templates

**Response-Only Training with Chat Templates** is a fine-tuning technique that limits the model's loss computation and gradient updates to only the assistant-generated response portions of a conversation, rather than the entire input. This approach ensures the model learns exclusively from the desired output patterns while ignoring user prompts, leading to more efficient training and better alignment with chat-style tasks.

## Overview

In supervised fine-tuning (SFT) for conversational models, each training example typically consists of a multi-turn conversation formatted using a chat template. Without response-only training, the model would be trained to predict every token in the sequence, including user queries and system prompts. Response-only training masks the loss on all non-response tokens, so the model is only optimized to generate the assistant's replies.^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## How It Works

Response-only training relies on two components: a **chat template** and a **loss-masking function**.

1. **Chat Template:** A structured format that wraps conversation turns with special tokens, such as `<|start_header_id|>user<|end_header_id|>` for user inputs and `<|start_header_id|>assistant<|end_header_id|>` for assistant responses. The template is applied to the raw conversation data before training.^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

2. **Loss Masking:** After tokenizing the formatted text, the training framework sets a mask that zeroes out the loss contribution for tokens belonging to the instruction (user) portion. The model's parameters are updated only based on errors in the response tokens.^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Benefits

- **Improved Training Efficiency:** The model focuses capacity on learning to generate correct assistant responses, reducing wasted computation on predictable input tokens.
- **Better Alignment:** Prevents the model from memorizing user queries or system prompts, which do not appear in the same form during inference.
- **Faster Convergence:** By reducing the number of tokens per example that contribute to loss, the effective learning signal is concentrated, often leading to faster convergence.

## Implementation with Unsloth

The [Unsloth](/concepts/unsloth.md) library provides a dedicated function `train_on_responses_only` to apply response-only training when using the `SFTTrainer` from the TRL library. This function accepts the trainer object, the token strings that demarcate instruction and response regions, and applies the appropriate loss mask.

### Example from Llama-3.2-3B Fine-Tuning

In the Databricks notebook for fine-tuning Llama-3.2-3B with Unsloth, the process includes:

1. **Setting a chat template** using Unsloth's `get_chat_template`:
   ```python
   tokenizer = get_chat_template(tokenizer, chat_template="llama-3.1")
   ```
2. **Formatting the dataset** by applying the template to each conversation:
   ```python
   def formatting_prompts_func(examples):
       convos = examples["conversations"]
       texts = [tokenizer.apply_chat_template(convo, tokenize=False, add_generation_prompt=False) for convo in convos]
       return {"text": texts}
   ```
3. **Creating the SFTTrainer** and then wrapping it with `train_on_responses_only`:
   ```python
   from unsloth.chat_templates import train_on_responses_only
   
   trainer = train_on_responses_only(
       trainer,
       instruction_part="<|start_header_id|>user<|end_header_id|>\n\n",
       response_part="<|start_header_id|>assistant<|end_header_id|>\n\n",
       num_proc=1
   )
   ```

After this step, the trainer will compute the loss only on the tokens that follow the `response_part` marker.^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## When to Use

Response-only training is the standard practice for supervised fine-tuning of chat-oriented LLMs. It is especially important when the training data includes long user instructions or multi-turn conversations, as it prevents the model from spending capacity on reconstructing the user's side of the dialog. Most SFT frameworks for chat models, including [TRL's SFTTrainer](/concepts/trl-sfttrainer.md) and [Axolotl](/concepts/axolotl.md), support similar loss-masking mechanisms.

## Related Concepts

- [Supervised Fine-Tuning (SFT)](/concepts/supervised-fine-tuning-sft.md) — The broader training paradigm
- Chat Templates — The formatting mechanism for conversation data
- Loss Masking — The general technique of ignoring certain tokens during training
- [Unsloth](/concepts/unsloth.md) — The library providing optimized training utilities
- LoRA — Parameter-efficient fine-tuning often used alongside response-only training
- MLflow Integration — Tracking training experiments with MLflow

## Sources

- finetune-llama-32-3b-with-unsloth-databricks-on-aws.md

# Citations

1. [finetune-llama-32-3b-with-unsloth-databricks-on-aws.md](/references/finetune-llama-32-3b-with-unsloth-databricks-on-aws-83073ff0.md)
