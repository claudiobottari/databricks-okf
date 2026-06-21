---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2eacea869c77c07c12aa2b1bcee5b29cbbca9dfecf75d69005815b72b1e223e7
  pageDirectory: concepts
  sources:
    - ai-runtime-example-notebooks-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - parameter-efficient-fine-tuning-for-llms
    - PFFL
  citations:
    - file: ai-runtime-example-notebooks-databricks-on-aws.md
title: Parameter-Efficient Fine-Tuning for LLMs
description: Techniques for fine-tuning large language models that update only a subset of parameters to reduce computational cost, as demonstrated in Databricks AI Runtime notebooks.
tags:
  - llm
  - fine-tuning
  - deep-learning
timestamp: "2026-06-18T10:44:26.671Z"
---

# Parameter-Efficient Fine-Tuning for LLMs

**Parameter-Efficient Fine-Tuning (PEFT)** refers to a family of techniques for adapting large language models (LLMs) to downstream tasks by updating only a small fraction of the model's parameters, leaving the vast majority of the pre-trained weights frozen. PEFT methods – such as [Low-Rank Adaptation (LoRA)](/concepts/low-rank-adaptation-lora.md), prefix tuning, and adapter layers – drastically reduce the memory and compute required for fine-tuning while often retaining performance comparable to full fine-tuning.

Examples of PEFT for LLMs are available in the [AI Runtime](/concepts/ai-runtime.md) example notebooks, which demonstrate fine-tuning large language models using parameter-efficient methods. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

In the context of [AI Runtime](/concepts/ai-runtime.md), these PEFT examples complement other distributed training patterns like FSDP-based multi-node fine-tuning and Ray Train data-parallel training.

## Benefits

- **Lower memory footprint**: Only a small fraction of parameters (e.g., 0.1–1%) are updated, reducing GPU memory requirements.
- **Faster training**: Fewer gradients to compute and store leads to shorter training cycles.
- **Modular adaptation**: Multiple task-specific adapters can be stored and swapped without copying the full base model.
- **Reduced storage costs**: Each fine-tuned variant is a small adapter file, not a full model copy.

## Related Concepts

- [Low-Rank Adaptation (LoRA)](/concepts/low-rank-adaptation-lora.md) – A widely used PEFT method that injects trainable low-rank matrices into attention layers.
- [Fine-tuning (LLM)](/concepts/supervised-fine-tuning-sft-of-llms.md) – The broader process of adapting a pre-trained LLM to a specific task.
- [AI Runtime](/concepts/ai-runtime.md) – The Databricks compute environment that provides GPU-accelerated example notebooks for PEFT.
- [MLflow](/concepts/mlflow.md) – For tracking PEFT experiments and logging adapters.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – Scaling PEFT across multiple GPUs or nodes.

## Sources

- ai-runtime-example-notebooks-databricks-on-aws.md

# Citations

1. [ai-runtime-example-notebooks-databricks-on-aws.md](/references/ai-runtime-example-notebooks-databricks-on-aws-09849715.md)
