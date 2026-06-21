---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e3b9449daf4e446395601366447de8db25c23e732b21cdec43f9127a03aa91a2
  pageDirectory: concepts
  sources:
    - fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - capybara-dataset
  citations:
    - file: fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
title: Capybara Dataset
description: A conversational AI training dataset from the TRL library used for supervised fine-tuning of language models
tags:
  - dataset
  - llm
  - conversational-ai
timestamp: "2026-06-19T10:34:21.613Z"
---

# Capybara Dataset

The **Capybara Dataset** is a conversational AI dataset used for supervised fine-tuning (SFT) of large language models. It is available through the TRL (Transformers Reinforcement Learning) library and is commonly used for training chat-oriented models.^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Overview

The Capybara dataset is designed for conversational AI training and is distributed as part of the TRL library's dataset collection. It provides structured conversation data suitable for fine-tuning models on dialogue tasks.^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Usage in Training

The dataset is loaded directly from the TRL library using the `load_dataset()` function from the HuggingFace `datasets` library. It is typically split into training and test sets for model evaluation.^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

```python
from datasets import load_dataset

dataset = load_dataset("trl-lib/Capybara")
train_dataset = dataset["train"]
eval_dataset = dataset["test"] if "test" in dataset else None
```

## Application Example

The Capybara dataset has been used in demonstration workflows for fine-tuning models such as Llama 3.2 1B on [Databricks AI Runtime](/concepts/databricks-ai-runtime.md). In these workflows, the dataset provides conversational examples that are formatted according to a chat schema, with user messages and expected assistant responses.^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Related Concepts

- [Supervised Fine-Tuning (SFT)](/concepts/supervised-fine-tuning-sft.md) — The training paradigm for which this dataset is used
- TRL Library — The library that provides access to the Capybara dataset
- [HuggingFace Datasets](/concepts/hugging-face-datasets-on-databricks.md) — The framework used to load and process the dataset
- Conversational AI — The domain of application for models trained on this dataset
- Llama 3.2 1B — A model that has been fine-tuned using the Capybara dataset

## Sources

- fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md

# Citations

1. [fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md](/references/fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws-4a3f88ec.md)
