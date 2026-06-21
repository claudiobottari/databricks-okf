---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8657ad703868a9de6ca65b115c826532d7166c9ccf8ff565faf71259496d38da
  pageDirectory: concepts
  sources:
    - distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sharegpt-chat-template-standardization
    - SCTS
  citations:
    - file: distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
title: ShareGPT chat template standardization
description: A data preprocessing step in Unsloth that converts conversational datasets into standardized chat templates (e.g., Llama 3.1 format) before training.
tags:
  - data-preprocessing
  - llm
  - chat-templates
timestamp: "2026-06-19T10:16:05.333Z"
---

Here is the wiki page for "ShareGPT chat template standardization".

---

## ShareGPT Chat Template Standardization

**ShareGPT Chat Template Standardization** refers to the process of converting a dataset of multi-turn conversations from the ShareGPT format into a standardized chat template format that a language model's tokenizer can correctly parse and use for training. This step is essential when fine-tuning models like Llama-3.2 using frameworks such as [Unsloth](/concepts/unsloth.md) or [TRL](/concepts/trl-transformer-reinforcement-learning.md).

## Overview

The ShareGPT dataset format typically represents conversations as a list of exchanges, with each message having a `from` field (indicating the speaker, such as `"user"` or `"assistant"`) and a `value` field (containing the message text). However, models like Llama 3 expect a specific structure for multi-turn dialogues, using special tokens like `<|start_header_id|>` and `<|end_header_id|>` to delineate roles. Standardization is the process of converting between these two representations.

## The `standardize_sharegpt` Function

The `standardize_sharegpt()` function from the `unsloth.chat_templates` module is the primary tool for this standardization. It restructures the dataset so that the `conversations` column—which originally contains a list of dictionaries with `from` and `value` keys—is transformed. After standardization, the function prepares the dataset for subsequent processing with `formatting_prompts_func`. This function then applies the model's chat template to generate the final text for each conversation. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### Typical Workflow

1. **Load the dataset.** The dataset (e.g., `mlabonne/FineTome-100k` in the source) is loaded in the ShareGPT format. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]
2. **Standardize the format.** The `standardize_sharegpt(dataset)` function is called to convert the conversation structure. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]
3. **Apply the chat template.** A `formatting_prompts_func` loops through the standardized conversations and uses `tokenizer.apply_chat_template()` to produce the final formatted text for training. This step ensures the data matches the exact template the model was trained with (e.g., `"llama-3.1"`). ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### Code Example

```python
from unsloth.chat_templates import get_chat_template, standardize_sharegpt

# ... (load model and tokenizer) ...

tokenizer = get_chat_template(
    tokenizer,
    chat_template="llama-3.1",
)

def formatting_prompts_func(examples):
    convos = examples["conversations"]
    texts = [tokenizer.apply_chat_template(convo, tokenize = False, add_generation_prompt = False) for convo in convos]
    return { "text" : texts, }

dataset = load_dataset(DATASET_NAME, split="train")
dataset = standardize_sharegpt(dataset)
dataset = dataset.map(formatting_prompts_func, batched=True,)
```

^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Relationship with `train_on_responses_only`

After standardization and formatting, the `train_on_responses_only` function is often used during the training phase. This function modifies the trainer to calculate the loss only on the assistant's response tokens, ignoring the user's input tokens. It uses the same chat template's role markers (e.g., `<|start_header_id|>user<|end_header_id|>\n\n` and `<|start_header_id|>assistant<|end_header_id|>\n\n`) to identify which parts of the conversation to train on. This ensures the model learns to generate helpful responses rather than just replicating the user's prompt. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Related Concepts

- [Unsloth](/concepts/unsloth.md) – The library providing the `standardize_sharegpt` function.
- Chat Template – The tokenizer's method for structuring multi-turn dialogues.
- Fine-tuning – The broader process of adapting a pre-trained model to a specific task.
- [SFTTrainer](/concepts/sfttrainer.md) – The trainer class from the TRL library used with standardized data.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – Running these standardization and training steps across multiple GPUs.

## Sources

- distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md

# Citations

1. [distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md](/references/distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws-5c6e3457.md)
