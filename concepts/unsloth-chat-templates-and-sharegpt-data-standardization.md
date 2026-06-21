---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b54993cd94fe26d115b882afaa97f989470c8c929dfe1a34fa0a5c3dc182be51
  pageDirectory: concepts
  sources:
    - distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unsloth-chat-templates-and-sharegpt-data-standardization
    - ShareGPT Data Standardization and Unsloth Chat Templates
    - UCTASDS
  citations:
    - file: distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
title: Unsloth Chat Templates and ShareGPT Data Standardization
description: Unsloth provides utilities like get_chat_template and standardize_sharegpt to convert conversational datasets into a standardized chat format (e.g., Llama 3.1) for training.
tags:
  - machine-learning
  - data-processing
  - chat-templates
  - unsloth
timestamp: "2026-06-18T15:30:28.030Z"
---

# Unsloth Chat Templates and ShareGPT Data Standardization

Unsloth provides a set of utilities for handling chat templates and standardising conversation datasets, primarily through the `unsloth.chat_templates` module. These functions are designed to prepare data for fine-tuning large language models (LLMs) using the [SFTTrainer](/concepts/sfttrainer.md) from the TRL library. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## `get_chat_template`

The `get_chat_template` function applies a specific chat template to a tokenizer. In practice, it is called with the tokenizer and the desired template name (e.g., `"llama-3.1"`). This ensures that the tokeniser inserts the correct control tokens (e.g., `<|start_header_id|>`, `<|end_header_id|>`) when formatting conversations, matching the expected input format of the base model. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

```python
from unsloth.chat_templates import get_chat_template

tokenizer = get_chat_template(
    tokenizer,
    chat_template="llama-3.1",
)
```

## `standardize_sharegpt`

The `standardize_sharegpt` function normalises a dataset that follows the ShareGPT conversation format. ShareGPT datasets typically contain a `"conversations"` column with alternating user and assistant messages. This function restructures the data so it can be processed uniformly by formatting functions and the trainer. It is applied before any template-based formatting. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

```python
dataset = standardize_sharegpt(dataset)
```

The standardised dataset is then passed through a user-defined formatting function (e.g., one that calls `tokenizer.apply_chat_template`) to produce the final text column used for training. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## `train_on_responses_only`

The `train_on_responses_only` function configures an `SFTTrainer` so that during training the language modelling loss is computed only on the assistant’s response tokens, not on the instruction or system prompt tokens. This is common practice in instruction tuning to prevent the model from simply memorising the user’s input. The function takes the trainer and the tokens that mark the beginning of the instruction part and the response part. For the LLaMA 3.1 chat template, these are: ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

- `instruction_part`: `"<|start_header_id|>user<|end_header_id|>\n\n"`
- `response_part`: `"<|start_header_id|>assistant<|end_header_id|>\n\n"`

```python
trainer = train_on_responses_only(
    trainer,
    instruction_part="<|start_header_id|>user<|end_header_id|>\n\n",
    response_part="<|start_header_id|>assistant<|end_header_id|>\n\n",
    num_proc=1
)
```

## Typical Workflow

A common pipeline for fine-tuning a chat model with Unsloth involves:

1. Load a base model and tokenizer.
2. Apply a chat template to the tokenizer via `get_chat_template`.
3. Load a ShareGPT‑formatted dataset.
4. Call `standardize_sharegpt` on the dataset.
5. Map a formatting function that calls `tokenizer.apply_chat_template` to produce a `"text"` column.
6. Create an `SFTTrainer` with the formatted dataset.
7. Wrap the trainer with `train_on_responses_only` to mask the loss on instruction tokens.
8. Train and save the model. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Related Concepts

- ShareGPT – The conversation data format used as input to `standardize_sharegpt`.
- [SFTTrainer](/concepts/sfttrainer.md) – The TRL trainer that consumes the formatted dataset.
- Chat Templates – Tokeniser‑level formatting schemes (e.g., LLaMA 3.1) applied via `get_chat_template`.
- LoRA Fine-Tuning – The parameter‑efficient fine‑tuning method commonly combined with these utilities.

## Sources

- distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md

# Citations

1. [distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md](/references/distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws-5c6e3457.md)
