---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3f4bd6b1350f528046a4e95d53fa1a4ea7edf7b5bf49b42ac89923a7b3c8ecda
  pageDirectory: concepts
  sources:
    - fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lora-adapter-merging-pattern
    - LAMP
  citations:
    - file: fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md
title: LoRA Adapter Merging Pattern
description: The process of merging a trained LoRA adapter with the base model to produce a standalone combined model for deployment
tags:
  - machine-learning
  - model-deployment
  - peft
timestamp: "2026-06-18T12:21:51.627Z"
---

# LoRA Adapter Merging Pattern

The **LoRA Adapter Merging Pattern** is a post-training technique in which a trained [Low-Rank Adaptation (LoRA)](/concepts/low-rank-adaptation-lora.md) adapter is combined with the base model to produce a single, self-contained model artifact. Merging eliminates the need for separate adapter weights and runtime adapter loading, simplifying deployment and inference pipelines. The pattern is commonly used after fine-tuning workflows that produce LoRA adapters—such as [QLoRA](/concepts/qlora-quantized-low-rank-adaptation.md) training—when the final model must be served without dependency on the adapter infrastructure.

## Overview

After fine-tuning a large language model using LoRA or [QLoRA](/concepts/qlora-quantized-low-rank-adaptation.md), the training output is typically a set of adapter weights stored separately from the base model. To make the model usable for inference in environments that do not support adapter loading (or to reduce operational complexity), the adapter is merged into the base model by applying the low-rank updates to the original parameter matrix, then removing the PEFT (Parameter-Efficient Fine-Tuning) wrapper so the model can be loaded as a standard `AutoModelForCausalLM`. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Implementation Steps

### Load the Base Model

The base model is loaded using `transformers.AutoModelForCausalLM` from the original HuggingFace identifier or local checkpoint. No adapter flags are needed at this stage—the base model must be the same architecture the LoRA was fine-tuned on. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

### Load the LoRA Adapter

The trained adapter is loaded using `peft.PeftModel.from_pretrained(base_model, adapter_dir)`, which attaches the LoRA weights to the base model. The adapter directory is typically the `output_dir` where the fine-tuning job saved its checkpoints. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

### Merge and Unload

The `merge_and_unload()` method on the `PeftModel` applies the LoRA scaling to the base model's weights and removes the PEFT wrapper, returning a standard transformers model. After this operation, the model no longer requires the `peft` library for inference. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

```python
peft_model = PeftModel.from_pretrained(base_model, adapter_dir)
merged_model = peft_model.merge_and_unload()
merged_model.generation_config.temperature = None
merged_model.generation_config.top_p = None
```

### Register the Merged Model

The merged model is then logged to [MLflow](/concepts/mlflow.md) using `mlflow.transformers.log_model()` and registered in [Unity Catalog](/concepts/unity-catalog.md) for deployment. Storing the merged artifact avoids the need for a separate adapter-serving infrastructure. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Hardware Considerations

Merging a LoRA adapter requires GPU memory sufficient to hold both the base model and the adapter weights simultaneously. In the Olmo3 7B example, H100 GPUs are required; smaller GPU types (such as T4 or A10) may fail with CUDA out-of-memory errors during the merge step. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Common Use Cases

- **Model serving without PEFT runtime**: Deployment environments that use `mlflow.transformers` or similar pipelines expect a full model, not a base+adapter pair. Merging produces a single artifact that matches that expectation.
- **Model registration in Unity Catalog**: Unity Catalog models registered via MLflow must be self-contained. A merged model can be registered with a single `registered_model_name` without extra adapter metadata.
- **Reuse of base model with multiple adapters**: When training multiple LoRA configurations against the same base model, each configuration can be merged independently into a separate copy of the base model, allowing A/B comparison in production without runtime adapter switching.

## Related Concepts

- [LoRA Adapter](/concepts/low-rank-adaptation-lora.md) — The fine-tuning technique that produces the adapter weights to be merged
- Model Merging — A broader category of techniques for combining model weights
- [QLoRA](/concepts/qlora-quantized-low-rank-adaptation.md) — Quantized LoRA that is frequently followed by a merge step
- PEFT — The HuggingFace library that provides the `merge_and_unload()` API
- MLflow Model Registration — The process of registering a merged model in the model registry
- [Unity Catalog](/concepts/unity-catalog.md) — The catalog where merged models are stored for deployment
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The compute environment used for the merge step

## Sources

- fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md

# Citations

1. [fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md](/references/fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws-c7178be1.md)
