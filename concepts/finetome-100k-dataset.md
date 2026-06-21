---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3f8f90a7049bd20d012842d4093bd5b65f571d3df6a7476eaeb416f1bf8dffc1
  pageDirectory: concepts
  sources:
    - finetune-llama-32-3b-with-unsloth-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - finetome-100k-dataset
    - FineTome-100k
  citations:
    - file: finetune-llama-32-3b-with-unsloth-databricks-on-aws.md
title: FineTome-100k Dataset
description: A large-scale instruction-following dataset (100k examples) created by mlabonne, used for supervised fine-tuning of language models, formatted in the ShareGPT conversation format.
tags:
  - datasets
  - nlp
  - instruction-tuning
timestamp: "2026-06-19T18:52:18.851Z"
---

Here is the wiki page for "FineTome-100k Dataset", written based solely on the provided source material.

---

## FineTome-100k Dataset

**FineTome-100k** is a supervised fine-tuning (SFT) dataset used to train large language models. It is hosted on Hugging Face under the name `mlabonne/FineTome-100k` and contains approximately 100,000 conversational examples. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Format

The dataset uses the ShareGPT format, where each example consists of a "conversations" field containing a list of alternating user and assistant messages. Before training, the dataset is standardized and each conversation is formatted into a single text sequence using an LLM-specific chat template (such as the Llama-3.1 chat template). ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Usage

During supervised fine-tuning, the `train_on_responses_only` technique is commonly applied. This configures the trainer to compute the loss only on the assistant's response tokens, masking the tokens in the user's prompt. This ensures the model learns to generate appropriate replies rather than memorizing the input queries. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

The FineTome-100k dataset is the default training dataset used in Databricks tutorials for fine-tuning models like Llama-3.2-3B-Instruct using the [Unsloth](/concepts/unsloth.md) library. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Related Concepts

- [Supervised Fine-Tuning (SFT)](/concepts/supervised-fine-tuning-sft.md)
- [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md)
- [ShareGPT Format](/concepts/sharegpt-dataset-format-standardization.md)
- [MLflow](/concepts/mlflow.md)
- [Unity Catalog](/concepts/unity-catalog.md)

## Sources

- finetune-llama-32-3b-with-unsloth-databricks-on-aws.md

# Citations

1. [finetune-llama-32-3b-with-unsloth-databricks-on-aws.md](/references/finetune-llama-32-3b-with-unsloth-databricks-on-aws-83073ff0.md)
