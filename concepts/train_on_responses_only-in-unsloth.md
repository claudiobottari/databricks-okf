---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a1714749548e7acfdfea7360b33e55ec7f8bf7c2fbf1b4ab61f54d72138c13e0
  pageDirectory: concepts
  sources:
    - distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - train_on_responses_only-in-unsloth
    - TIU
  citations:
    - file: distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
title: train_on_responses_only in Unsloth
description: A technique that masks out user/instruction tokens during training so the model only learns from assistant responses, improving fine-tuning quality for chat models.
tags:
  - llm-finetuning
  - training-technique
  - unsloth
timestamp: "2026-06-19T10:16:10.667Z"
---

# train_on_responses_only in Unsloth

**`train_on_responses_only`** is a function from the `unsloth.chat_templates` module in the [Unsloth](/concepts/unsloth.md) library. It wraps an `SFTTrainer` (originally from the `trl` library) and modifies its behavior so that the model’s loss is computed **only over the response (assistant) tokens**, ignoring the instruction (user) tokens. This prevents the model from learning to predict the user’s input and focuses fine-tuning on generating high-quality answers. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Usage

The function is typically called right before `trainer.train()`. It accepts the trainer object, the string patterns that mark the beginning of instruction and response turns, and a `num_proc` argument for preprocessing parallelism. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

```python
from unsloth.chat_templates import train_on_responses_only

trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=dataset,
    # ... other SFTTrainer arguments
)

trainer = train_on_responses_only(
    trainer,
    instruction_part="<|start_header_id|>user<|end_header_id|>\n\n",
    response_part="<|start_header_id|>assistant<|end_header_id|>\n\n",
    num_proc=1
)

trainer.train()
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `trainer` | An instance of `trl.SFTTrainer` (or compatible trainer). |
| `instruction_part` | The string that identifies the start of a user (instruction) turn in the chat template. Only the response part is kept for training. |
| `response_part` | The string that identifies the start of an assistant (response) turn. |
| `num_proc` | Number of processes used during preprocessing of the dataset. Default is often 1. |

## Use Case

`train_on_responses_only` is used in [Supervised Fine-Tuning (SFT)](/concepts/supervised-fine-tuning-sft.md) of chat-based language models, where the training data consists of multi-turn conversations. By masking out the loss on user turns, the model learns to generate helpful and coherent assistant replies without being penalized for the user’s messages. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

In practice, the function is often employed after setting up a chat template with `get_chat_template()` from the same module.

## Related Concepts

- [SFTTrainer](/concepts/sfttrainer.md) — The trainer class from `trl` used for supervised fine-tuning.
- [Unsloth](/concepts/unsloth.md) — The optimized training library that provides `train_on_responses_only`.
- Chat Templates — How tokenizers structure conversation turns.
- LoRA — Low-Rank Adaptation, often used together with this function to reduce memory.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — The function works seamlessly in multi-GPU setups (e.g., with `@distributed`).

## Sources

- distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md

# Citations

1. [distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md](/references/distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws-5c6e3457.md)
