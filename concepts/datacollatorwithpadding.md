---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 53ac88c17ac186056fdee893d4bf99aedd23a92d95bdfeb63abb9a85266dd608
  pageDirectory: concepts
  sources:
    - fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - datacollatorwithpadding
    - Data collator
    - data collator
  citations:
    - file: fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
title: DataCollatorWithPadding
description: A Hugging Face data collator that dynamically pads input sequences to the longest sequence in each batch during training, providing a memory-efficient alternative to static padding.
tags:
  - huggingface
  - data-processing
  - training
timestamp: "2026-06-19T10:32:22.225Z"
---

# DataCollatorWithPadding

**DataCollatorWithPadding** is a utility from the Hugging Face `transformers` library that dynamically pads input sequences in a batch to the same length during training and evaluation. It ensures that all samples in a mini-batch have uniform dimensions, which is required for efficient tensor operations on GPUs.

## Overview

When fine-tuning Transformer models, raw text is tokenized into sequences of varying lengths. Mini-batches in PyTorch or TensorFlow require all tensors in a batch to have the same shape. `DataCollatorWithPadding` addresses this by padding shorter sequences to match the longest sequence in each batch. It provides good baseline performance for text classification tasks and is commonly used with the Hugging Face `Trainer` class. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

The collator accepts a tokenizer instance and uses its padding token and configuration to automatically determine the padding strategy. It can pad to the maximum length in the batch (dynamic padding) or to a fixed length if specified.

## Usage in Training Configuration

`DataCollatorWithPadding` is typically instantiated with the tokenizer used for preprocessing and then passed to the `Trainer`:

```python
from transformers import DataCollatorWithPadding, Trainer, TrainingArguments

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
data_collator = DataCollatorWithPadding(tokenizer)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_test_dataset["train"],
    eval_dataset=train_test_dataset["test"],
    compute_metrics=compute_metrics,
    data_collator=data_collator,
)
```

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

The `Trainer` automatically invokes the collator on each batch during training and evaluation, making it transparent to the user.

## Related Concepts

- Tokenizer – Converts raw text into model‑compatible input IDs and attention masks.
- Trainer – The Hugging Face training loop that orchestrates model training, evaluation, and logging.
- [TrainingArguments](/concepts/trainingarguments-configuration.md) – Configuration class for specifying hyperparameters like batch size, learning rate, and evaluation strategy.
- Batching and Padding – General deep learning concepts for constructing uniform mini‑batches.
- [Fine-tuning Hugging Face models](/concepts/single-gpu-fine-tuning-with-hugging-face-on-databricks.md) – End‑to‑end process for adapting pre‑trained models to specific tasks.

## Sources

- fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md

# Citations

1. [fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md](/references/fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws-e2c49846.md)
