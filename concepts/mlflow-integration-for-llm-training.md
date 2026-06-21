---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 97af436a90145e7c5d53a9ebaa1084506102ed2b3b24332c4be25fce4ef7ff68
  pageDirectory: concepts
  sources:
    - fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-integration-for-llm-training
    - MIFLT
  citations:
    - file: fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md
title: MLflow Integration for LLM Training
description: The integration of MLflow experiment tracking with LLM Foundry to log training metrics, system metrics, and model checkpoints, enabling experiment comparison and reproducibility.
tags:
  - mlflow
  - experiment-tracking
  - observability
timestamp: "2026-06-19T18:50:26.998Z"
---

# MLflow Integration for LLM Training

**MLflow Integration for LLM Training** refers to the use of [MLflow](/concepts/mlflow.md) to track experiments, log metrics, and register models during large language model (LLM) training workflows on Databricks. When using [Mosaic LLM Foundry](/concepts/mosaic-llm-foundry.md) with Databricks Serverless GPU, MLflow provides built-in logging, system metric capture, and Unity Catalog model registry integration. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

## MLflow Logger Configuration

In a fine-tuning job (e.g., for Llama 3.1 8B), the training configuration is defined in a YAML block that includes an `mlflow` logger section. The key settings are:

- **`tracking_uri`**: Set to `databricks` to automatically use the workspace’s MLflow tracking server.
- **`experiment_name`**: Specifies the target experiment (e.g., `/Workspace/Shared/llm-foundry-sgc`).
- **`run_name`**: A human-readable name for the run (e.g., `llama3_8b-finetune`).
- **`resume`**: When `true`, allows MLflow to resume a previous run if one exists with the same name.
- **`rename_metrics`**: Maps raw metric names from the training framework to user-friendly names (e.g., `time/token` → `time/num_tokens`, `lr-DecoupledLionW/group0` → `learning_rate`).
- **`log_system_metrics`**: When `true`, captures system-level metrics such as GPU utilization and memory usage during training. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

## Model Registry via Unity Catalog

The MLflow logger configuration can also set the model registry URI to `databricks-uc` and provide a `model_registry_prefix` (e.g., `main.linyuan`) that is prepended to registered model names. This enables automatic registration of trained models in [Unity Catalog](/concepts/unity-catalog.md). ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

## Callbacks and Checkpointing

The Mosaic LLM Foundry training configuration uses a `hf_checkpointer` callback that integrates with MLflow. This callback:

- Saves model checkpoints to a specified folder (e.g., `/Volumes/<catalog>/<schema>/<volume>/<model_name>`).
- Logs the checkpoint to MLflow under a registered model name (e.g., `main.sgc.llama3_1_8b_full_ft`).
- Sets metadata such as `pretrained_model_name` and `task` (e.g., `llm/v1/completions`).
- Supports `mlflow_logging_config` to specify task and metadata for the registered model version. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

## Retrieving the [MLflow Run](/concepts/mlflow-run.md) ID

After training completes, the distributed training function returns the active [MLflow Run](/concepts/mlflow-run.md) ID. This ID can be used to access run artifacts, metrics, and logs in the MLflow UI, as well as to locate the registered model in Unity Catalog. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

## Best Practices

- Set `experiment_name` before launching the training job so all runs are organized under a dedicated experiment.
- Enable `log_system_metrics` to monitor GPU and memory usage for troubleshooting and capacity planning.
- Use `rename_metrics` to map framework‑specific metric names to standard names that are easier to query.
- Specify a `model_registry_uri` of `databricks-uc` to ensure trained models are stored in Unity Catalog for governance and discoverability.
- Use the `hf_checkpointer` callback with a `save_interval` and `mlflow_registered_model_name` to automatically register checkpoints as model versions in Unity Catalog. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizing runs under a named experiment
- [Unity Catalog Model Registry](/concepts/unity-catalog-model-registry.md) — Registering and governing ML models in Unity Catalog
- [Mosaic LLM Foundry](/concepts/mosaic-llm-foundry.md) — The training framework that drives LLM fine-tuning
- [FSDP](/concepts/fsdp-fully-sharded-data-parallel.md) — Distributed training strategy used with MLflow logging
- [Serverless GPU](/concepts/serverless-gpu-compute.md) — The compute environment for running distributed training
- Hugging Face Model Registry — Alternative model source used alongside MLflow

## Sources

- fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md

# Citations

1. [fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md](/references/fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws-d6760424.md)
