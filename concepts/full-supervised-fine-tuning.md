---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fedb44455d920e0ee34324db0c47cbac93c4adb7f1c263e2200c145d6afed07f
  pageDirectory: concepts
  sources:
    - large-language-models-llms-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - full-supervised-fine-tuning
    - FSF
    - Full Fine-Tuning
  citations:
    - file: large-language-models-llms-databricks-on-aws.md
title: Full Supervised Fine-Tuning
description: Complete fine-tuning approach for LLMs where all model parameters are updated during training
tags:
  - machine-learning
  - fine-tuning
  - llm
timestamp: "2026-06-19T19:11:41.898Z"
---

# Full Supervised Fine-Tuning

**Full Supervised Fine-tuning** is an approach to adapting a [Large Language Models (LLMs)|large language model](/concepts/large-language-models-llms-on-databricks.md) (LLM) for a specific task by updating all of the model's parameters using labeled data. It stands in contrast to parameter‑efficient methods that update only a subset of parameters.

## Overview

Within [AI Runtime](/concepts/ai-runtime.md) on Databricks, the platform provides notebook examples that demonstrate various approaches to fine-tuning LLMs. These examples include both parameter‑efficient methods like [Low-Rank Adaptation (LoRA)](/concepts/low-rank-adaptation-lora.md) and full supervised fine-tuning. ^[large-language-models-llms-databricks-on-aws.md]

## Relationship to Other Methods

Full supervised fine-tuning updates every weight in the model, which can produce stronger task‑specific performance but requires significantly more compute and memory compared to parameter‑efficient alternatives such as LoRA. The examples included in AI Runtime cover both families, allowing users to choose the approach that best fits their resource constraints and accuracy requirements. ^[large-language-models-llms-databricks-on-aws.md]

## Availability

The AI Runtime for single‑node fine‑tuning tasks is in **Public Preview**, while the distributed training API for multi‑GPU workloads remains in **Beta**. ^[large-language-models-llms-databricks-on-aws.md] This availability applies to both full supervised fine‑tuning and parameter‑efficient fine‑tuning.

## Related Concepts

- [Low-Rank Adaptation (LoRA)](/concepts/low-rank-adaptation-lora.md)
- [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md)
- [AI Runtime](/concepts/ai-runtime.md)

## Sources

- large-language-models-llms-databricks-on-aws.md

# Citations

1. [large-language-models-llms-databricks-on-aws.md](/references/large-language-models-llms-databricks-on-aws-bfc38cd2.md)
