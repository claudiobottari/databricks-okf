---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b83dabc317e762d47f8419cc12c53924ce48e7a7a2f0aa2329a50bddcfaaecaa
  pageDirectory: concepts
  sources:
    - distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - chat-template-processing-with-unsloth
    - CTPWU
  citations:
    - file: distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
title: Chat Template Processing with Unsloth
description: The pipeline for converting conversational datasets (ShareGPT format) into model‑specific chat template text using Unsloth's get_chat_template and standardize_sharegpt utilities.
tags:
  - data-processing
  - llm
  - templates
timestamp: "2026-06-18T12:04:04.368Z"
---

```markdown
# Chat Template Processing with Unsloth

**Chat Template Processing with Unsloth** refers to the set of utilities provided by the [[Unsloth]] library for handling conversation-style datasets and applying chat templates during fine-tuning of large language models (LLMs). These tools streamline the preparation of datasets that follow multi-turn dialogue formats, such as those using the ShareGPT schema, and enable targeted training on assistant responses only.

## Overview

When fine-tuning instruction-following or chat models, raw data typically consists of conversations with alternating user and assistant turns. Unsloth offers functions to:

- Standardize datasets into a common format (`standardize_sharegpt`).
- Apply a tokenizer’s chat template to convert conversation dictionaries into a single text string (`get_chat_template`).
- Restrict training loss to the assistant response portions (`train_on_responses_only`).

These functions integrate with Hugging Face Transformers and [[TRL (Transformer Reinforcement Learning) Library|TRL]] and must be imported before the `trl` library to avoid compatibility issues. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Key Functions

### `get_chat_template`

Applies a specific chat template (e.g., `"llama-3.1"`) to the tokenizer. This ensures that when `tokenizer.apply_chat_template()` is called later, it uses the correct format for the target model family.

```python
from unsloth.chat_templates import get_chat_template

tokenizer = get_chat_template(
    tokenizer,
    chat_template="llama-3.1",
)
```

After this call, the tokenizer will format conversations with the appropriate special tokens and role markers for Llama 3.1-style chat. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### `standardize_sharegpt`

Converts a dataset into the standardized ShareGPT format, which uses a `"conversations"` column containing a list of messages with `"from"` and `"value"` keys. This is a prerequisite for subsequent processing steps.

```python
dataset = standardize_sharegpt(dataset)
```

^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### `train_on_responses_only`

Wraps an [[SFTTrainer]] so that the loss is computed only on the assistant's response tokens, ignoring the user instructions. This prevents the model from being penalized for correctly imitating the user’s input and focuses learning on generating helpful replies.

```python
from unsloth.chat_templates import train_on_responses_only

trainer = train_on_responses_only(
    trainer,
    instruction_part="<|start_header_id|>user<|end_header_id|>\n\n",
    response_part="<|start_header_id|>assistant<|end_header_id|>\n\n",
    num_proc=1,
)
```

The `instruction_part` and `response_part` strings must match the delimiters used by the applied chat template. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Chat Template Standardization

A typical pipeline for processing a conversation dataset with Unsloth looks like:

1. Load the dataset (e.g., `"mlabonne/FineTome-100k"`).
2. Call `standardize_sharegpt(dataset)` to ensure the dataset uses the expected column structure.
3. Define a formatting function that applies `tokenizer.apply_chat_template()` to each conversation’s `"conversations"` field.
4. Map the formatting function over the dataset with `dataset.map()`.

Example formatting function:

```python
def formatting_prompts_func(examples):
    convos = examples["conversations"]
    texts = [
        tokenizer.apply_chat_template(
            convo, tokenize=False, add_generation_prompt=False
        )
        for convo in convos
    ]
    return {"text": texts}
```

^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Training on Responses Only

After applying the chat template and formatting the dataset, `train_on_responses_only` modifies the trainer to mask the loss on tokens that belong to the instruction part. This technique is known as **response-only fine-tuning** or **loss masking**. It has been shown to improve model quality for chat tasks by preventing the model from learning to simply repeat the user message.

The function requires the exact tokens that mark the start of the instruction and the response, which are determined by the chat template applied earlier (e.g., Llama 3.1‑style tags). ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Best Practices

- **Import Unsloth before TRL:** `from unsloth import FastLanguageModel` must appear before any import from `trl` to prevent compatibility errors. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]
- **Ensure chat template alignment:** The delimiters passed to `train_on_responses_only` must exactly match those produced by the tokenizer after `get_chat_template`. Mismatch tokens will cause the loss masking to fail silently.
- **Use `standardize_sharegpt` on raw datasets:** If your dataset does not already use the ShareGPT schema, this function normalizes it, making the subsequent formatting step safe.
- **Test formatting on a few examples:** Before launching a full training run, verify that `apply_chat_template` produces the expected text with correct role markers.

## Related Concepts

- [[Unsloth]] — The library providing these utilities
- [[LLM fine-tuning on Databricks|Fine-tuning LLMs]] — Overview of the fine-tuning process
- LoRA — Parameter-efficient fine-tuning method often used with Unsloth
- [[SFTTrainer]] — The TRL trainer used for supervised fine-tuning
- Chat Templates — Hugging Face tokenizer functionality for conversational models
- ShareGPT — Common format for multi-turn conversation datasets

## Sources

- distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
```

# Citations

1. [distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md](/references/distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws-5c6e3457.md)
