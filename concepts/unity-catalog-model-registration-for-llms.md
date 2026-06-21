---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dd8f06e3cfd16fce38dee12965bd84aee8185b6b3231a2f98700705bef879201
  pageDirectory: concepts
  sources:
    - distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-model-registration-for-llms
    - UCMRFL
  citations:
    - file: distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
title: Unity Catalog model registration for LLMs
description: The pattern of registering fine-tuned LLMs into Databricks Unity Catalog for governance, versioning, and deployment, including merging LoRA adapters into the base model.
tags:
  - mlops
  - model-registry
  - databricks
  - governance
timestamp: "2026-06-19T10:16:05.601Z"
---

Here is the wiki page for "Unity Catalog model registration for LLMs", written based solely on the provided source material.

---

## Unity Catalog Model Registration for LLMs

**Unity Catalog model registration for LLMs** is the process of saving a trained or fine-tuned large language model (LLM) into [Unity Catalog](/concepts/unity-catalog.md) for governance, versioning, and deployment. This is typically performed after training or fine-tuning is complete, using [MLflow](/concepts/mlflow.md) to log the model artifacts and register them as a model in Unity Catalog.

### Overview

After training an LLM — for example, fine-tuning Llama-3.2-3B with Unsloth on multiple GPUs — the model artifacts must be saved and registered for production use. The recommended approach combines MLflow Tracking for artifact logging and Unity Catalog for model governance and lifecycle management. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### Model Registration Strategy

The registration process follows a three-step strategy:

1. **MLflow Tracking**: Log model artifacts and metadata to an [MLflow Run](/concepts/mlflow-run.md).
2. **Unity Catalog Registration**: Register the model in Unity Catalog for governance and deployment.
3. **Model Versioning**: Automatic versioning is applied for model lifecycle management, with complete model information captured for reproducibility. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### Prerequisites

Before registering a model, you need:

- A trained or fine-tuned LLM (e.g., a LoRA adapter merged into a base model).
- A Unity Catalog [Catalog and Schema](/concepts/catalog-and-schema.md) where the model will be registered.
- The MLflow library and appropriate permissions to write to Unity Catalog.

### Registration Process

#### 1. Load the Trained Model

For LoRA fine-tuned models, you must load both the base model and the adapter, then merge them into a single model for registration: ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

# Load base model
base_model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    trust_remote_code=True
)

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# Load LoRA adapter and merge into base model
adapter_dir = OUTPUT_DIR
peft_model = PeftModel.from_pretrained(base_model, adapter_dir)
merged_model = peft_model.merge_and_unload()

components = {
    "model": merged_model,
    "tokenizer": tokenizer,
}
```

#### 2. Define the Unity Catalog Model Name

The model name follows the Unity Catalog three-level namespace: `catalog.schema.model_name`. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

```python
full_model_name = f"{UC_CATALOG}.{UC_SCHEMA}.{UC_MODEL_NAME}"
```

#### 3. Log and Register the Model with MLflow

Use `mlflow.transformers.log_model()` to log the model components and register them in Unity Catalog. The `task` parameter should be set to `"llm/v1/chat"` for chat-based LLMs. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

```python
import mlflow

task = "llm/v1/chat"

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
```

### Output

After successful registration, the following information is available: ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

- **Unity Catalog Path**: The full three-level name (e.g., `main.default.llama-3_2-3b`).
- **MLflow Model URI**: The URI for the logged model artifacts.
- **Model Version**: The automatically assigned version number.

### Best Practices

- **Merge LoRA adapters before registration**: For LoRA fine-tuned models, merge the adapter into the base model using `merge_and_unload()` to create a standalone model. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]
- **Include metadata**: Add relevant metadata such as the pretrained model name, task type, and model family for reproducibility and discoverability. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]
- **Use the correct task type**: Set `task="llm/v1/chat"` for chat-based LLMs to ensure proper inference serving configuration. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### Related Concepts

- MLflow Model Registration — The general process of registering models with MLflow.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer for data and AI assets.
- LoRA Fine-Tuning — Parameter-efficient fine-tuning technique commonly used with LLMs.
- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md) — Deploying registered models for inference.
- [MLflow Transformers Flavor](/concepts/mlflow-transformers-flavor.md) — The MLflow flavor used for logging transformer-based models.

### Sources

- distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md

# Citations

1. [distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md](/references/distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws-5c6e3457.md)
