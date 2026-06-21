---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 81158856583c5faf526ccc2e47e88e4c9055d5176ddb37c024acb95c919dac67
  pageDirectory: concepts
  sources:
    - distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-model-registration-with-mlflow
    - UCMRWM
  citations:
    - file: distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
title: Unity Catalog Model Registration with MLflow
description: The workflow for registering finetuned LLMs into Databricks Unity Catalog via MLflow, including model versioning, metadata tagging, and merging LoRA adapters into the base model for deployment.
tags:
  - mlflow
  - model-registry
  - databricks
  - mlep
timestamp: "2026-06-19T18:33:49.155Z"
---

# Unity Catalog Model Registration with MLflow

**Unity Catalog Model Registration with MLflow** is the workflow for saving fine‑tuned models—especially LoRA‑adapted large language models—into [Unity Catalog](/concepts/unity-catalog.md) using [MLflow](/concepts/mlflow.md) tracking and model registry APIs. This enables centralized model governance, versioning, and deployment.

## Overview

After distributed fine‑tuning, the trained adapter weights must be merged back into the base model and logged to MLflow with a Unity Catalog destination. The registration process uses `mlflow.transformers.log_model()` with the `registered_model_name` parameter set to the three‑level Unity Catalog path (`catalog.schema.model_name`). MLflow automatically version‑manages the registered model, producing a model URI and a version number that downstream consumers can use for inference or further training. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Prerequisites

Before registration, the Unity Catalog location must be configured. Typical parameters include:

- **Catalog** (e.g., `main`)
- **Schema** (e.g., `default`)
- **Model name** (e.g., `llama-3_2-3b`)

These are often set as Databricks notebook widgets to make the workflow reusable across environments. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Registration Workflow for LoRA Models

For LoRA‑fine‑tuned models, registration requires merging the adapter weights into the base model before logging. The steps are:

1. **Load the base model** from Hugging Face (e.g., `AutoModelForCausalLM.from_pretrained`).
2. **Load the tokenizer** (e.g., `AutoTokenizer.from_pretrained`).
3. **Load the LoRA adapter** using `PeftModel.from_pretrained(base_model, adapter_dir)`.
4. **Merge the LoRA weights** into the base model by calling `peft_model.merge_and_unload()`, which returns a model without PEFT wrappers.
5. **Create a component dictionary** containing the merged model and tokenizer.
6. **Log and register** the model using `mlflow.transformers.log_model()` with the `registered_model_name` set to the Unity Catalog path.

The notebook also specifies the MLflow task as `"llm/v1/chat"` and attaches metadata such as the pretrained model name and model family. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Example Code

The following code snippet (adapted from the distributed fine‑tuning notebook) shows the registration portion:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
import mlflow

# Load base model and tokenizer
base_model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# Load LoRA adapter and merge
peft_model = PeftModel.from_pretrained(base_model, OUTPUT_DIR)
merged_model = peft_model.merge_and_unload()

# Build components dict for MLflow
components = {
    "model": merged_model,
    "tokenizer": tokenizer,
}

# Full Unity Catalog path
full_model_name = f"{UC_CATALOG}.{UC_SCHEMA}.{UC_MODEL_NAME}"
task = "llm/v1/chat"

# Log and register
with mlflow.start_run(run_id=run_id):
    model_info = mlflow.transformers.log_model(
        transformers_model=components,
        name="model",
        task=task,
        registered_model_name=full_model_name,
        metadata={
            "task": task,
            "pretrained_model_name": MODEL_NAME,
            "databricks_model_family": "Llama3.2",
        },
    )

print(f"✓ Model successfully registered: {full_model_name}")
print(f"✓ MLflow model URI: {model_info.model_uri}")
print(f"✓ Model version: {model_info.registered_model_version}")
```

^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Output and Verification

After successful registration, MLflow returns:

- **MLflow model URI** (e.g. `runs:/<run-id>/model`)
- **Registered model version** (assigned automatically by Unity Catalog)

These identifiers are printed so that downstream consumers can load the model for serving or further fine‑tuning. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Best Practices

- Use descriptive model names that reflect the architecture and dataset.
- Always merge LoRA adapters into the base model before registration; do not log the adapter alone.
- Provide a `task` string (e.g. `"llm/v1/chat"`) to enable automatic model serving configuration.
- Attach metadata for provenance, such as the base model name and model family.
- Configure Unity Catalog parameters as notebook widgets for portability across workspaces and environments.

## Related Concepts

- LoRA Fine-Tuning — Parameter‑efficient adaptation technique.
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — The underlying registry that tracks model versions.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer for data and AI assets.
- [Model Serving](/concepts/model-serving.md) — Deploying registered models to inference endpoints.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Multi‑GPU fine‑tuning with frameworks like Unsloth.

## Sources

- distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md

# Citations

1. [distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md](/references/distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws-5c6e3457.md)
