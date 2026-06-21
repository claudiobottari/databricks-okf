---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f7da49a14f2b3df71660a3a305015e25a16c0392ed3875d6d5cda3f8b96856e3
  pageDirectory: concepts
  sources:
    - fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-for-model-registration
    - UCFMR
  citations:
    - file: fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md
title: Unity Catalog for Model Registration
description: A Databricks feature that enables registering, versioning, and managing ML models in a unified catalog for deployment and inference
tags:
  - mlops
  - model-management
  - databricks
timestamp: "2026-06-19T18:51:24.581Z"
---

# Unity Catalog for Model Registration

**Unity Catalog for Model Registration** refers to the process of storing, versioning, and managing machine learning models in Databricks using Unity Catalog as the model registry. When fine-tuned or trained models are registered to Unity Catalog, they become accessible for deployment, inference, and governance across the Databricks platform.

## Overview

Model registration in Unity Catalog enables organizations to manage ML models as first-class data assets alongside tables, volumes, and other catalog objects. Registered models benefit from Unity Catalog's centralized governance, lineage tracking, and access control mechanisms. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Registration Workflow

### Prerequisites

Before registering a model to Unity Catalog, you need:
- A Unity Catalog catalog, schema, and optionally a volume for storing checkpoints
- A trained or fine-tuned model (such as a LoRA adapter merged with a base model)
- Sufficient compute resources to load the model checkpoint (H100 GPUs are recommended for large models) ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

### Path Definition

Models are registered using a fully qualified Unity Catalog path in the format `{catalog}.{schema}.{model_name}`. This path identifies the model's location within the Unity Catalog hierarchy. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

```python
full_model_name = f"{catalog}.{schema}.{model_name}"
```

### The Registration Process

The typical registration workflow involves several steps:

1. **Load the trained model**: Load the base model and any adapter weights (such as LoRA adapters).
2. **Merge adapters**: If using parameter-efficient fine-tuning methods like [QLoRA](/concepts/qlora-quantized-low-rank-adaptation.md), merge the adapter weights into the base model and remove the PEFT wrappers.
3. **Create a pipeline**: Wrap the merged model with a tokenizer into a HuggingFace pipeline for inference.
4. **Log to MLflow**: Use MLflow's logging API to register the model under the Unity Catalog path.

^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

### MLflow Registration Example

After fine-tuning with [Axolotl](/concepts/axolotl.md) on serverless GPU compute, a model can be registered using the [MLflow Run](/concepts/mlflow-run.md) ID from the training session:

```python
with mlflow.start_run(run_id=run_id):
    model_info = mlflow.transformers.log_model(
        transformers_model=text_gen_pipe,
        name="model",
        input_example=input_example,
        registered_model_name=full_model_name,
    )
```

This registers the model in Unity Catalog and returns the model URI and version number. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Benefits

Registering models in Unity Catalog provides several advantages:

- **Centralized governance**: Models are subject to Unity Catalog's access controls and auditing.
- **Version management**: Each registration creates a new model version for tracking iterations.
- **Deployment readiness**: Registered models can be deployed to serving endpoints.
- **Lineage tracking**: MLflow automatically tracks the experiment run that produced the model.

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance and metadata layer for Databricks assets
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — The underlying mechanism for model versioning
- [Axolotl](/concepts/axolotl.md) — Framework for LLM fine-tuning that produces models for registration
- [QLoRA](/concepts/qlora-quantized-low-rank-adaptation.md) — Parameter-efficient fine-tuning technique commonly used with model registration
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — Compute infrastructure used for training and model loading
- [Model Deployment](/concepts/model-serving-endpoint-deployment.md) — The downstream step after model registration
- [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md) — Captures run metadata linked to registered models

## Sources

- fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md

# Citations

1. [fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md](/references/fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws-c7178be1.md)
