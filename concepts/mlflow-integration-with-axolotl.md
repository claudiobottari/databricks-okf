---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 53e41a4e69f87266300f1783f94a43ef02a85cfa585e3537338cbd16154a5a26
  pageDirectory: concepts
  sources:
    - fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-integration-with-axolotl
    - MIWA
    - MLflow Integration with Ray
    - MLflow integration with Ray
  citations:
    - file: fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md
title: MLflow Integration with Axolotl
description: The integration between Axolotl training framework and MLflow for experiment tracking, logging training metrics, and registering models to Unity Catalog
tags:
  - mlops
  - experiment-tracking
  - databricks
timestamp: "2026-06-19T18:51:23.917Z"
---

# MLflow Integration with Axolotl

The **MLflow Integration with Axolotl** enables automatic experiment tracking, metric logging, and model registry management when fine-tuning large language models with the Axolotl framework on Databricks. By setting simple configuration flags, users can log training metrics, parameters, and artifacts to MLflow without manual instrumentation.

## Overview

Axolotl provides built-in support for MLflow through its configuration system. When enabled, Axolotl writes training metrics (loss, learning rate, gradient norms, etc.) to the active [MLflow Run](/concepts/mlflow-run.md). The integration works seamlessly with Databricks’ managed MLflow service, allowing users to track experiments, compare runs, and register models directly to Unity Catalog. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Configuration

To enable MLflow integration in Axolotl, set the following fields in the training configuration dictionary:

| Field                 | Value            | Description                                                                 |
|-----------------------|------------------|-----------------------------------------------------------------------------|
| `use_mlflow`          | `True`           | Enables MLflow logging of metrics and parameters.                          |
| `mlflow_tracking_uri` | `"databricks"`   | Points to the Databricks-hosted MLflow tracking server.                     |
| `mlflow_run_name`     | `<your-run-name>`| Sets the human-readable name for the [MLflow Run](/concepts/mlflow-run.md).                           |
| `hf_mlflow_log_artifacts` | `False`      | Controls whether HuggingFace artifacts are logged (often disabled to reduce clutter). |

Additionally, `wandb_mode` should be set to `"disabled"` if you are not using Weights & Biases, to avoid conflicts. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

Example snippet from an Axolotl configuration:

```python
config = DictDefault(
    ...
    use_mlflow=True,
    mlflow_tracking_uri="databricks",
    mlflow_run_name="olmo3-7b-qlora-axolotl",
    hf_mlflow_log_artifacts=False,
    wandb_mode="disabled",
    ...
)
```

## Training Run Tracking

When training is launched via the `@distributed` decorator (e.g., across 8 H100 GPUs), Axolotl automatically starts an [MLflow Run](/concepts/mlflow-run.md). The training function can retrieve the run ID for later use:

```python
import mlflow

# Inside the distributed training function
model, tokenizer, trainer = train(cfg=cfg, dataset_meta=dataset_meta)
mlflow_run_id = None
if mlflow.last_active_run() is not None:
    mlflow_run_id = mlflow.last_active_run().info.run_id
return mlflow_run_id
```

This run ID can be passed back to the main notebook to associate model registration with the same run. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Model Registration to Unity Catalog

After training completes, the fine-tuned model (including merged LoRA adapter) can be logged and registered to [Unity Catalog](/concepts/unity-catalog.md) using the [MLflow Run](/concepts/mlflow-run.md) ID obtained during training. The example workflow:

1. Load the base model and tokenizer.
2. Load the trained LoRA adapter.
3. Merge and unload the adapter.
4. Create a text-generation pipeline.
5. Call `mlflow.transformers.log_model()` with `registered_model_name` pointing to a Unity Catalog path (e.g., `catalog.schema.model_name`).

The code explicitly starts an [MLflow Run](/concepts/mlflow-run.md) with the previously captured `run_id` to attach the model artifact to the same experiment run:

```python
with mlflow.start_run(run_id=run_id):
    model_info = mlflow.transformers.log_model(
        transformers_model=text_gen_pipe,
        name="model",
        input_example=input_example,
        registered_model_name=full_model_name,
    )
```

This registers the model in [Unity Catalog](/concepts/unity-catalog.md), making it available for deployment and inference through the MLflow Model Registry. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Benefits

- **Automatic metric logging** – No need to manually log loss, learning rate, or other training metrics.
- **Experiment comparison** – MLflow’s UI allows side-by-side comparison of different hyperparameter configurations.
- **Seamless model registry** – The trained adapter can be directly registered to Unity Catalog for production deployment.
- **Single source of truth** – All experiment metadata, metrics, and artifacts are stored in a central MLflow server.

## Related Concepts

- [Axolotl](/concepts/axolotl.md) – Framework for LLM post-training (LoRA, QLoRA).
- [MLflow](/concepts/mlflow.md) – Open-source platform for machine learning lifecycle management.
- [Unity Catalog](/concepts/unity-catalog.md) – Databricks’ unified governance solution for data and AI assets.
- [QLoRA](/concepts/qlora-quantized-low-rank-adaptation.md) – Quantized Low-Rank Adaptation technique used in the example.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – Infrastructure for running distributed training on Databricks.
- [Experiment Tracking](/concepts/mlflow-experiment-tracking.md) – General concept of logging ML experiments.

## Sources

- fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md

# Citations

1. [fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md](/references/fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws-c7178be1.md)
