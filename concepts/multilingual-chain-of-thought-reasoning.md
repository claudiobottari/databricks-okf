---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 669c3fa67fb66dd3cc94119b4e57e31e7060ce30cdbce25f86cacc5de9f24cee
  pageDirectory: concepts
  sources:
    - distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - multilingual-chain-of-thought-reasoning
    - MCR
  citations:
    - file: distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
title: Multilingual chain-of-thought reasoning
description: Capability of a language model to perform internal reasoning in one language while generating responses in another, enabled by multilingual CoT datasets
tags:
  - machine-learning
  - reasoning
  - multilingual
timestamp: "2026-06-18T15:29:17.196Z"
---

# Multilingual Chain-of-Thought Reasoning

**Multilingual Chain-of-Thought Reasoning** refers to a language model’s ability to perform step-by-step reasoning (chain-of-thought) in one language while responding to prompts in a different language. This capability is developed by fine-tuning a base model on datasets containing translated reasoning chains in multiple languages, enabling cross-lingual inference. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## Dataset: Multilingual-Thinking

The dataset used for this purpose, **HuggingFaceH4/Multilingual-Thinking**, has been specifically curated with translated chain-of-thoughts in multiple languages. By default, the fine-tuning notebook for [[gpt-oss-20b|OpenAI gpt-oss-20b]] uses this dataset to train the model to reason in a language specified via a system prompt while responding to users in any language. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## Fine-Tuning Approach

The model is fine-tuned using parameter-efficient techniques such as LoRA (Low-Rank Adaptation) combined with [MXFP4 Quantization](/concepts/mxfp4-quantization.md) to reduce memory requirements. Distributed training across 8 H100 GPUs applies the dataset to the 20B-parameter model. At inference time, the system prompt `"reasoning language: {language}"` controls the internal reasoning language. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## Example: Cross-Language Reasoning

After fine-tuning, the model can be tested by setting the reasoning language to one language and providing a user prompt in another. The following example demonstrates German internal reasoning with a Spanish query: ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

- **Reasoning language**: German (set via `SYSTEM_PROMPT = "reasoning language: German"`)
- **User prompt**: `"¿Cuál es el capital de Australia?"` (Spanish for “What is the capital of Australia?”)
- **Expected behavior**: The model performs chain-of-thought reasoning in German and generates a response that may incorporate both languages.

The inference code applies the chat template with system and user messages, then generates tokens using a temperature of 0.6, producing output that demonstrates cross-lingual reasoning ability. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## Applications

Multilingual chain-of-thought reasoning enables global AI assistants that can think in a preferred reasoning language (e.g., for consistency or regulatory reasons) while serving users in their native languages. It also supports multilingual evaluation and auditing of reasoning traces in a single language.

## Related Concepts

- Chain-of-Thought Prompting
- [Parameter-Efficient Fine-Tuning](/concepts/parameter-efficient-fine-tuning-peft.md)
- LoRA
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [Model Serving](/concepts/model-serving.md)

## Sources

- distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md

# Citations

1. [distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md](/references/distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws-7ee24e1a.md)
