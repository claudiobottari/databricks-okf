---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f5e241f1926ce777eda14fbc372cc29fef4510aae4cafab2e9f50fe44cbc5e91
  pageDirectory: concepts
  sources:
    - fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - yaml-based-llm-fine-tuning-configuration
    - YLFC
  citations:
    - file: fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md
title: YAML-based LLM Fine-tuning Configuration
description: A structured YAML configuration pattern used by LLM Foundry to specify model architecture, optimizer, scheduler, FSDP settings, dataset loading, callbacks, and logging parameters for LLM fine-tuning.
tags:
  - configuration
  - fine-tuning
  - yaml
timestamp: "2026-06-19T18:50:43.584Z"
---

# YAML-based LLM Fine-tuning Configuration

**YAML-based LLM Fine-tuning Configuration** refers to the practice of defining all training parameters for large language model (LLM) fine-tuning in a structured YAML file, which is then consumed by a training framework such as [Mosaic LLM Foundry](/concepts/mosaic-llm-foundry.md). This approach separates configuration from code, enabling reproducibility, easier experimentation, and straightforward integration with orchestration tools.

## Overview

In a typical fine-tuning workflow, the YAML configuration specifies the model architecture, pretrained weights, distributed training settings, optimizer and scheduler hyperparameters, data loading details, logging and checkpointing behavior, and callback configurations. The configuration is loaded at runtime and can be dynamically overridden before training begins. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

## YAML Configuration Structure

The following sections describe the major components of a fine-tuning YAML configuration, based on the example from fine-tuning Llama 3.1 8B with Mosaic LLM Foundry on Databricks Serverless GPU. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

### Model Configuration

The `model` section defines the base model and its initialization:

| Parameter | Description |
|-----------|-------------|
| `name` | Model type (e.g., `hf_causal_lm` for Hugging Face causal language models) |
| `pretrained` | Whether to load pretrained weights |
| `pretrained_model_name_or_path` | Hugging Face model identifier (e.g., `meta-llama/Llama-3.1-8B`) |
| `init_device` | Device for initializing model (`mixed` for distributing across GPUs) |
| `use_auth_token` | Whether to use an authentication token for gated models |
| `use_flash_attention_2` | Enable Flash Attention v2 for optimized attention |

The configuration points to a specific Hugging Face model and enables Flash Attention if the corresponding library is installed. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

### Logging (MLflow)

The `loggers` block configures experiment tracking via MLflow:

```yaml
loggers:
  mlflow:
    tracking_uri: databricks
    experiment_name: "mlflow_experiment_name"
    run_name: llama3_8b-finetune
    model_registry_uri: databricks-uc
    model_registry_prefix: main.linyuan
    resume: true
    rename_metrics:
      time/token: time/num_tokens
      lr-DecoupledLionW/group0: learning_rate
    log_system_metrics: true
```

Key parameters include `tracking_uri` (set to `databricks` for Databricks-managed MLflow), `experiment_name`, and `model_registry_uri` (set to `databricks-uc` for Unity Catalog integration). The `rename_metrics` block maps internal metric names to more readable names. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

### Callbacks

Callbacks monitor and control the training process. Common callbacks include:

| Callback | Purpose |
|----------|---------|
| `lr_monitor` | Tracks learning rate during training |
| `run_timeout` | Sets a maximum training duration (in seconds) |
| `scheduled_gc` | Triggers garbage collection at fixed batch intervals |
| `speed_monitor` | Reports training throughput (tokens per second) |
| `memory_monitor` | Logs GPU memory usage |
| `runtime_estimator` | Estimates remaining training time |
| `hf_checkpointer` | Saves Hugging Face compatible checkpoints and registers them to MLflow |

The `hf_checkpointer` callback is particularly important: it specifies where to save checkpoints (`save_folder`), the save interval, precision, and the `mlflow_registered_model_name` for automatic model registration in Unity Catalog. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

### Optimizer and Scheduler

The `optimizer` and `scheduler` sections define the learning algorithm and learning rate schedule:

```yaml
optimizer:
  lr: 5.0e-07
  name: decoupled_lionw
  betas: [0.9, 0.95]
  weight_decay: 0

scheduler:
  name: linear_decay_with_warmup
  alpha_f: 0
  t_warmup: 10ba
```

The optimizer uses the Decoupled LionW algorithm with a learning rate of `5e-7`. The scheduler applies linear decay with 10 batches of warmup, reaching a final multiplier of `alpha_f: 0`. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

### Precision and Tokenizer

```yaml
precision: amp_bf16
tokenizer:
  name: meta-llama/Llama-3.1-8B
  kwargs:
    model_max_length: 1024
```

Training uses automatic mixed precision with bfloat16 (`amp_bf16`). The tokenizer is specified by its Hugging Face identifier, and `model_max_length` caps the sequence length to 1024 tokens. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

### FSDP Configuration

The `fsdp_config` block controls [FSDP](/concepts/fsdp-fully-sharded-data-parallel.md) (Fully Sharded Data Parallel) settings for distributed training:

```yaml
fsdp_config:
  verbose: false
  mixed_precision: PURE
  state_dict_type: sharded
  limit_all_gathers: true
  sharding_strategy: FULL_SHARD
  activation_cpu_offload: false
  activation_checkpointing: true
  activation_checkpointing_reentrant: false
```

This configuration uses full sharding (`FULL_SHARD`) with pure mixed precision, activation checkpointing to reduce memory usage, and sharded state dictionaries. `activation_cpu_offload` is disabled to avoid latency overhead. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

### Data Loading

The `train_loader` section defines the fine-tuning dataset:

```yaml
train_loader:
  name: finetuning
  dataset:
    split: test
    hf_name: mosaicml/dolly_hhrlhf
    shuffle: true
    safe_load: true
    max_seq_len: 1024
    packing_ratio: auto
    target_prompts: none
    target_responses: all
    allow_pad_trimming: false
    decoder_only_format: true
  timeout: 0
  drop_last: false
  pin_memory: true
  num_workers: 8
  prefetch_factor: 2
  persistent_workers: true
```

The dataset is loaded from Hugging Face (`mosaicml/dolly_hhrlhf`), using the test split for fine-tuning. Automatic packing (`packing_ratio: auto`) maximizes throughput, and `decoder_only_format: true` indicates the model is a decoder-only architecture (no separate encoder). ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

### Other Global Parameters

| Parameter | Description |
|-----------|-------------|
| `max_seq_len` | Maximum sequence length (1024) |
| `max_duration` | Maximum training duration (e.g., `20ba` for 20 batches) |
| `global_train_batch_size` | Total batch size across all GPUs (32) |
| `device_train_microbatch_size` | Microbatch size per GPU (1) |
| `device_eval_batch_size` | Evaluation batch size per GPU (1) |
| `seed` | Random seed for reproducibility (17) |
| `save_interval` | How often to save checkpoints |
| `eval_interval` | How often to run evaluation |
| `save_overwrite` | Overwrite existing checkpoints |
| `save_num_checkpoints_to_keep` | Number of recent checkpoints to retain |

The `autoresume` flag enables automatic recovery from interruptions. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

## Dynamic Overrides

After loading the YAML configuration (often via a `%%yaml` cell magic), the configuration dictionary can be modified programmatically before training begins. Common overrides include setting the output directory, experiment name, and MLflow registered model name based on environment variables or widget inputs. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

```python
config["loggers"]["mlflow"]["experiment_name"] = MLFLOW_EXPERIMENT_NAME
config["save_folder"] = OUTPUT_DIR
config["callbacks"]["hf_checkpointer"]["save_folder"] = OUTPUT_DIR
config["callbacks"]["hf_checkpointer"]["mlflow_registered_model_name"] = f"{UC_CATALOG}.{UC_SCHEMA}.{UC_MODEL_NAME}"
```

This pattern allows a single YAML template to be reused across different environments and experiments. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

## Related Concepts

- [Mosaic LLM Foundry](/concepts/mosaic-llm-foundry.md) — The training framework that consumes these YAML configurations
- [FSDP](/concepts/fsdp-fully-sharded-data-parallel.md) — The distributed training strategy configured in the `fsdp_config` block
- [MLflow](/concepts/mlflow.md) — Experiment tracking and model registry integration
- [Unity Catalog](/concepts/unity-catalog.md) — Model storage and lineage tracking
- [Serverless GPU](/concepts/serverless-gpu-compute.md) — The compute environment for running distributed fine-tuning
- [Flash Attention](/concepts/flash-attention.md) — Optimized attention mechanism enabled by `use_flash_attention_2`
- [Hugging Face](/concepts/hugging-face-trainer.md) — Source for pretrained models and datasets
- Automatic Mixed Precision — Training with bfloat16 precision

## Sources

- fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md

# Citations

1. [fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md](/references/fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws-d6760424.md)
