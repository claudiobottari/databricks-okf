---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7e876b3a055f541ade41ff178c9934dc3074c489737641f51cd1e07c00a30773
  pageDirectory: concepts
  sources:
    - fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - capybara-dataset-for-conversational-ai-training
    - CDFCAT
  citations:
    - file: fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
title: Capybara Dataset for Conversational AI Training
description: A dataset from the TRL library used for conversational AI training, employed as the training dataset in the supervised fine-tuning example for Llama 3.2 1B.
tags:
  - dataset
  - conversational-ai
  - trl
timestamp: "2026-06-19T18:51:17.286Z"
---

# Capybara Dataset for Conversational AI Training

The **Capybara Dataset for Conversational AI Training** is a dataset used for supervised fine-tuning (SFT) of large language models, particularly for conversational AI applications. It is available through the [TRL (Transformers Reinforcement Learning)](/concepts/trl-transformers-reinforcement-learning.md) library and is designed to train models on conversational interactions. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Overview

The dataset, referenced as `trl-lib/Capybara`, is used as a training dataset for fine-tuning models like Llama 3.2 1B Instruct. In the context of conversational AI training, the dataset is loaded and formatted using chat templates that structure the data into user and assistant roles. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

The Capybara dataset contains both `train` and `test` splits, allowing for evaluation of model performance during training. The training process uses the SFTTrainer from the TRL library to fine-tune models on this dataset, with evaluation metrics such as `eval_loss` used to determine the best model checkpoint. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Usage in Fine-Tuning Workflows

When used with the TRL SFTTrainer, the Capybara dataset is typically:

1. Loaded using the `load_dataset` function from the HuggingFace `datasets` library
2. Tokenized using a model-specific tokenizer with proper chat formatting
3. Passed to the trainer for supervised fine-tuning on conversational tasks

The dataset is well-suited for training on H100 GPU Support on Databricks hardware, as demonstrated in example notebooks that use [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) with [DeepSpeed](/concepts/deepspeed.md) ZeRO Stage 3 optimization for efficient distributed training. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Training Configuration

In typical fine-tuning workflows using the Capybara dataset, training is configured with:

- **Loss metric**: `eval_loss` is used as the primary evaluation metric
- **Model selection**: The best model checkpoint is selected based on lowest evaluation loss
- **Formatting**: Conversations are formatted using a chat template scheme with "User:" and "Response:" markers

After training, models fine-tuned on the Capybara dataset can be registered in [Unity Catalog](/concepts/unity-catalog.md) and deployed to [Model Serving](/concepts/model-serving.md) endpoints for conversational AI applications. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Related Concepts

- [Supervised Fine-Tuning (SFT)](/concepts/supervised-fine-tuning-sft.md) — The training technique used with this dataset
- [TRL (Transformers Reinforcement Learning)](/concepts/trl-transformers-reinforcement-learning.md) — The library that provides the SFTTrainer
- Llama 3.2 1B — An example base model fine-tuned on this dataset
- [HuggingFace Datasets](/concepts/hugging-face-datasets-on-databricks.md) — The library used to load the dataset
- Conversational AI Models — The broader category of models trained on this dataset

## Sources

- fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md

# Citations

1. [fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md](/references/fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws-4a3f88ec.md)
