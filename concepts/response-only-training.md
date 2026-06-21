---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 818d03b2eb9033f56eb839344f19f786c36d973c188a1aa4469b1377a6588c87
  pageDirectory: concepts
  sources:
    - finetune-llama-32-3b-with-unsloth-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - response-only-training
  citations:
    - file: finetune-llama-32-3b-with-unsloth-databricks-on-aws.md
title: Response-Only Training
description: A training technique that masks out user/instruction tokens during supervised fine-tuning so the model only learns from assistant responses, improving training efficiency.
tags:
  - machine-learning
  - fine-tuning
  - training-optimization
timestamp: "2026-06-19T18:52:13.850Z"
---

# Response-Only Training

**Response-Only Training** is a technique used in [Supervised Fine-Tuning (SFT)](/concepts/supervised-fine-tuning-sft.md) of chat models where the model learns only from the assistant's response tokens, ignoring the user prompt or instruction tokens during loss computation. This ensures that the model is not penalized for failing to predict the user's input, which is not part of the model's own generation. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## How It Works

In a standard chat conversation, each training example consists of both a user instruction and an assistant response. Response-only training identifies which tokens belong to the instruction (the prompt) and which belong to the response. By masking the loss on the instruction tokens, the model's gradients are computed only from the response portion, allowing the model to focus entirely on learning the desired assistant behavior. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Benefits

- **Improved training efficiency**: Because the model does not waste capacity on predicting the user's input, training can converge faster and use compute resources more effectively. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]
- **Focused learning**: The model learns to generate appropriate assistant responses without being influenced by the need to reconstruct the prompt. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Implementation with Unsloth

The [Unsloth](/concepts/unsloth.md) library provides the `train_on_responses_only` function to apply response-only training to an `SFTTrainer`. The function requires the user to specify the text patterns that separate the instruction part from the response part — for example, using the chat template delimiters such as `<|start_header_id|>user<|end_header_id|>\n\n` for instructions and `<|start_header_id|>assistant<|end_header_id|>\n\n` for responses. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

```python
trainer = train_on_responses_only(
    trainer,
    instruction_part = "<|start_header_id|>user<|end_header_id|>\n\n",
    response_part = "<|start_header_id|>assistant<|end_header_id|>\n\n",
    num_proc=1
)
```

After this call, the trainer computes the loss only on tokens that follow the response pattern, omitting the user instruction tokens from the loss. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Related Concepts

- [Supervised Fine-Tuning (SFT)](/concepts/supervised-fine-tuning-sft.md)
- [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md)
- Chat Templates
- [Unsloth](/concepts/unsloth.md)
- [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md)

## Sources

- finetune-llama-32-3b-with-unsloth-databricks-on-aws.md

# Citations

1. [finetune-llama-32-3b-with-unsloth-databricks-on-aws.md](/references/finetune-llama-32-3b-with-unsloth-databricks-on-aws-83073ff0.md)
