---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 26e488904f005cccf0f847d33636551d42ae469afc004d22d6bdde72ebfa3767
  pageDirectory: concepts
  sources:
    - fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lora-adapter-merging-workflow
    - LAMW
  citations:
    - file: fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md
title: LoRA Adapter Merging Workflow
description: The process of loading a trained LoRA adapter, merging it with the base model using merge_and_unload(), and registering the combined model for deployment
tags:
  - machine-learning
  - model-deployment
  - peft
timestamp: "2026-06-19T18:51:29.084Z"
---

# LoRA Adapter Merging Workflow

The **LoRA Adapter Merging Workflow** is the process of combining a trained [Low-Rank Adaptation (LoRA)](/concepts/low-rank-adaptation-lora.md) adapter with its base model to produce a single, standalone model suitable for deployment and inference. After fine-tuning a model using [QLoRA](/concepts/qlora-quantized-low-rank-adaptation.md) or standard LoRA, the adapter weights must be merged into the base model before the model can be registered to a model registry like [Unity Catalog](/concepts/unity-catalog.md) or deployed for production use. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Overview

LoRA fine-tuning produces a small set of adapter weights that modify the behavior of a frozen base model. While the adapter can be loaded alongside the base model during training, production deployment typically requires a merged model that incorporates the adapter weights directly into the base model's parameters. This merging step eliminates the dependency on the separate adapter checkpoint and simplifies the deployment pipeline. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Workflow Steps

### 1. Load the Base Model

The first step is to load the original base model using the appropriate model class from the Transformers library. The base model must match the architecture used during LoRA training.

```python
from transformers import AutoModelForCausalLM

HF_MODEL_NAME = "allenai/Olmo-3-7B-Instruct-SFT"
base_model = AutoModelForCausalLM.from_pretrained(
    HF_MODEL_NAME,
    trust_remote_code=True
)
```

^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

### 2. Load the LoRA Adapter

The trained LoRA adapter is loaded from the output directory where it was saved during training. The PEFT library's `PeftModel.from_pretrained()` method loads the adapter weights and applies them on top of the base model.

```python
from peft import PeftModel

adapter_dir = OUTPUT_DIR  # Path to saved adapter checkpoint
peft_model = PeftModel.from_pretrained(base_model, adapter_dir)
```

^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

### 3. Merge and Unload

The `merge_and_unload()` method integrates the LoRA adapter weights into the base model and removes the PEFT wrapper, producing a standalone model with the adapter's modifications permanently applied.

```python
merged_model = peft_model.merge_and_unload()
```

After merging, the model's generation configuration may need adjustment. Common practice is to set `temperature` and `top_p` to `None` to use default sampling behavior. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

```python
merged_model.generation_config.temperature = None
merged_model.generation_config.top_p = None
```

^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

### 4. Register the Merged Model

The merged model can be registered to a model registry such as [Unity Catalog](/concepts/unity-catalog.md) via [MLflow](/concepts/mlflow.md). This typically involves creating a text-generation pipeline and logging it with `mlflow.transformers.log_model()`.

```python
import mlflow
from transformers import pipeline

text_gen_pipe = pipeline(
    task="text-generation",
    model=merged_model,
    tokenizer=tokenizer,
)

with mlflow.start_run(run_id=run_id):
    model_info = mlflow.transformers.log_model(
        transformers_model=text_gen_pipe,
        name="model",
        input_example=["Hello, world!"],
        registered_model_name=full_model_name,
    )
```

^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Hardware Requirements

The merging step requires sufficient GPU memory to load the full base model alongside the adapter. For large models such as Olmo3 7B, this typically requires H100-class GPUs. Attempting to merge on smaller GPUs may result in CUDA out-of-memory errors. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Related Concepts

- [Low-Rank Adaptation (LoRA)](/concepts/low-rank-adaptation-lora.md) — The parameter-efficient fine-tuning technique that produces adapter weights
- [QLoRA](/concepts/qlora-quantized-low-rank-adaptation.md) — Quantized LoRA, which combines 4-bit quantization with LoRA for memory-efficient training
- PEFT — The Hugging Face library for parameter-efficient fine-tuning
- [Axolotl](/concepts/axolotl.md) — A framework for LLM post-training that supports LoRA and QLoRA workflows
- [Unity Catalog](/concepts/unity-catalog.md) — Databricks' unified governance solution for data and AI assets
- [MLflow](/concepts/mlflow.md) — Platform for managing the ML lifecycle, including model registration
- Model Merging — The general concept of combining multiple model components into a single model

## Sources

- fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md

# Citations

1. [fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md](/references/fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws-c7178be1.md)
