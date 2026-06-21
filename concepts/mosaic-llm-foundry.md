---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0d0f46c792cff45c0f1344128479298b9c2c6b86ff3303c58f5e833d773a3989
  pageDirectory: concepts
  sources:
    - fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mosaic-llm-foundry
    - MLF
  citations:
    - file: fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md
title: Mosaic LLM Foundry
description: An open-source framework for training, fine-tuning, evaluating, and deploying large language models with built-in support for distributed training strategies like FSDP.
tags:
  - machine-learning
  - llm-framework
  - fine-tuning
timestamp: "2026-06-19T18:50:52.715Z"
---

# Mosaic LLM Foundry

**Mosaic LLM Foundry** is an open-source codebase, hosted at [GitHub](https://github.com/mosaicml/llm-foundry), for training, fine-tuning, evaluating, and deploying [large language models](/concepts/large-language-models-llms-on-databricks.md) (LLMs). It provides built-in support for distributed training strategies and integrates with experiment tracking and model registry tools such as [MLflow](/concepts/mlflow.md) and [Unity Catalog](/concepts/unity-catalog.md). ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

## Key Features

- **Distributed training**: Uses [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) to distribute model parameters, gradients, and optimizer states across multiple GPUs, enabling training of large models that exceed single-GPU memory. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]
- **Efficient data loading**: Includes built-in data loading pipelines optimized for large-scale fine-tuning, supporting features like packing ratio and parallel data workers. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]
- **Flash Attention**: Supports prebuilt `flash-attn` wheels for optimized attention computation, avoiding slow compilation from source when installing. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]
- **YAML configuration**: Training runs are configured declaratively via YAML files, covering model architecture, optimizer, scheduler, dataset, FSDP settings, callbacks, and logging configuration. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]
- **MLflow integration**: Automatically logs metrics (e.g., tokens per second, learning rate) through MLflow loggers and can register models to the MLflow model registry or [Unity Catalog](/concepts/unity-catalog.md) model registry via the `hf_checkpointer` callback. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]
- **Hugging Face interoperability**: Loads pretrained models and tokenizers from Hugging Face Hub, and can save checkpoints in Hugging Face compatible format using the `hf_checkpointer` callback. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]
- **Built-in callbacks**: Provides callbacks for learning rate monitoring (`lr_monitor`), speed monitoring (`speed_monitor`), memory monitoring (`memory_monitor`), runtime estimation (`runtime_estimator`), garbage collection scheduling (`scheduled_gc`), and timeout handling (`run_timeout`). ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

## Integration with Databricks

On Databricks, Mosaic LLM Foundry runs on serverless GPU compute using the `@distributed` decorator to orchestrate multi-GPU training (e.g., 8× H100 GPUs). ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

### Unity Catalog Integration

Model checkpoints and final models can be stored in Unity Catalog volumes and registered to the Unity Catalog model registry. The YAML configuration specifies the `save_folder` as a Unity Catalog volume path and the `mlflow_registered_model_name` in three-level catalog format (e.g., `catalog.schema.model_name`). ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

### MLflow Experiment Tracking

MLflow experiment tracking is configured via `tracking_uri: databricks`, with options to rename metrics, log system metrics, and set the experiment name. The `hf_checkpointer` callback can log checkpoints to MLflow and register the model to Unity Catalog, returning the [MLflow Run](/concepts/mlflow-run.md) ID for further tracking. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

## Typical Fine-Tuning Workflow

1. **Connect to serverless GPU compute** – Select Serverless GPU compute with an appropriate accelerator (e.g., 8×H100) and environment version (e.g., standard base, version 5). ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]
2. **Install LLM Foundry and dependencies** – Install `flash-attn` (prebuilt wheel first), `llm-foundry[gpu]`, `hf_transfer`, and `yamlmagic`. Restart the Python kernel. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]
3. **Configure Unity Catalog paths** – Set catalog, schema, model name, and volume path for saving checkpoints. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]
4. **Define training configuration** – Write a YAML config specifying the model (e.g., `meta-llama/Llama-3.1-8B`), optimizer (e.g., `decoupled_lionw`), scheduler, dataset (e.g., `mosaicml/dolly_hhrlhf`), FSDP settings, and callbacks. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]
5. **Run distributed training** – Wrap the training function with the `@distributed` decorator (specifying `gpus=8`, `gpu_type='H100'`) and call it. The function calls `llmfoundry.command_utils.train.train()` with the configuration as a `DictConfig`. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]
6. **Monitor and access results** – Training logs metrics to an MLflow experiment, and the final model is saved to Unity Catalog. The [MLflow Run](/concepts/mlflow-run.md) ID is returned for further tracking. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

## Example YAML Configuration Structure

The YAML configuration file controls all aspects of training. Key sections include:

- **model**: Specifies the pretrained model name or path (`pretrained_model_name_or_path`), flash attention usage (`use_flash_attention_2: true`), and device initialization (`init_device`). ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]
- **loggers**: Configures MLflow tracking URI (`databricks`), experiment name, run name, model registry URI (`databricks-uc`), and model registry prefix for Unity Catalog. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]
- **callbacks**: Enables `lr_monitor`, `speed_monitor`, `memory_monitor`, `runtime_estimator`, `hf_checkpointer` (saves Hugging Face checkpoints), and others. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]
- **fsdp_config**: Sets sharding strategy (`FULL_SHARD`), mixed precision (`PURE`), activation checkpointing (`true`), and gradient clipping. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]
- **train_loader**: Defines the dataset (Hugging Face dataset name), tokenization parameters (`max_seq_len`), packing ratio (`auto`), number of workers (`num_workers`), and other data loading settings. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]
- **optimizer**, **scheduler**, **precision**, **max_duration**, **global_train_batch_size**, and other hyperparameters. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

## Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — The distributed training strategy used by LLM Foundry
- [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md) — Models that can be fine-tuned with LLM Foundry
- [MLflow](/concepts/mlflow.md) — Experiment tracking and model registry integration
- [Unity Catalog](/concepts/unity-catalog.md) — Model storage and registry for Databricks workloads
- [Serverless GPU](/concepts/serverless-gpu-compute.md) — The compute environment for running LLM Foundry on Databricks
- [Flash Attention](/concepts/flash-attention.md) — Optimized attention implementation used for faster training
- Hugging Face Hub — Source of pretrained models and tokenizers
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) — Training scale where FSDP is critical
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Multi-GPU and multi-node training patterns
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — Pre-built runtime for ML workloads

## Sources

- fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md

# Citations

1. [fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md](/references/fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws-d6760424.md)
