---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8de2847b33904e0e021366c60f2dc2316f98018d5a92588e4f1aa08c45c1336d
  pageDirectory: concepts
  sources:
    - distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-model-registration-for-ml-models
    - UCMRFMM
  citations:
    - file: distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
title: Unity Catalog Model Registration for ML Models
description: The process of registering fine-tuned models in Databricks Unity Catalog for governance, version control, discoverability, and deployment via Model Serving.
tags:
  - databricks
  - model-registry
  - unity-catalog
  - mlops
timestamp: "2026-06-19T15:14:14.772Z"
---

## Unity Catalog Model Registration for ML Models

**Unity Catalog Model Registration for ML Models** refers to the process of storing, governing, and versioning machine learning models in [Unity Catalog](/concepts/unity-catalog.md) using [MLflow](/concepts/mlflow.md). This approach provides a unified namespace for model discovery, access control, and lifecycle management across the Databricks platform.

### Overview

Unity Catalog model registration combines MLflow Tracking (for logging artifacts and metadata) with Unity Catalog (for governance and deployment). It supports automatic model versioning, enabling reproducible model lifecycle management. The registration typically occurs after training is complete and uses the [MLflow Run](/concepts/mlflow-run.md) ID generated during the training run.^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Key Steps

1. **Configure the Unity Catalog namespace** – Before training, specify the catalog, schema, and model name. The final model is registered as `{catalog}.{schema}.{model_name}`.^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
2. **Load the trained model** – For parameter‑efficient fine‑tuning (e.g., LoRA), both the base model and the adapter must be loaded. The adapter is then merged into the base model using `PeftModel.merge_and_unload()`.^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
3. **Assemble model components** – The merged model and its tokenizer are combined into a single dictionary (e.g., `{"model": merged_model, "tokenizer": tokenizer}`).^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
4. **Log and register with MLflow** – Start an [MLflow Run](/concepts/mlflow-run.md) (using the run ID from training) and call `mlflow.transformers.log_model()`. Provide the components, an artifact path, the MLflow task (e.g., `"llm/v1/chat"`), the `registered_model_name` (the full Unity Catalog path), and optional metadata such as the pretrained model name and model family.^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Model Registration Strategy

Unity Catalog model registration offers several benefits:

- **MLflow Tracking** – Logs model artifacts and metadata to a central tracking server.
- **Unity Catalog** – Registers the model for governance, access control, and easy discovery.
- **Model Versioning** – Automatically creates a new version for each registration, enabling rollback and promotion.
- **Metadata** – Complete model information (task, pretrained name, model family) is stored for reproducibility and search.^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Example Code

The following code snippet (adapted from the Qwen2‑0.5B fine‑tuning notebook) demonstrates registration after LoRA training:

```python
import mlflow
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

full_model_name = f"{UC_CATALOG}.{UC_SCHEMA}.{UC_MODEL_NAME}"

# Load base model and LoRA adapter, then merge
base_model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
peft_model = PeftModel.from_pretrained(base_model, adapter_dir)
merged_model = peft_model.merge_and_unload()

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

components = {"model": merged_model, "tokenizer": tokenizer}

with mlflow.start_run(run_id=mlflow_run_id):
    mlflow.transformers.log_model(
        transformers_model=components,
        artifact_path="model",
        task="llm/v1/chat",
        registered_model_name=full_model_name,
        metadata={
            "task": "llm/v1/chat",
            "pretrained_model_name": MODEL_NAME,
            "databricks_model_family": "QwenForCausalLM",
        },
    )
```

After successful registration, MLflow returns a `model_uri` that can be used to load or deploy the model.^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Related Concepts

- [MLflow](/concepts/mlflow.md) – The tracking and logging framework used to orchestrate model registration.
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance layer that stores registered models.
- [Model Serving](/concepts/model-serving.md) – Deploy models from Unity Catalog to inference endpoints.
- LoRA – A parameter‑efficient fine‑tuning technique that produces adapter weights needing special handling during registration.
- PEFT – The Hugging Face library used to load and merge LoRA adapters.
- [MLflow Transformers Flavor](/concepts/mlflow-transformers-flavor.md) – The flavor used to log Hugging Face transformer models.
- Model Versioning – Automatic version management in Unity Catalog.

### Sources

- distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md

# Citations

1. [distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md](/references/distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws-507af04a.md)
