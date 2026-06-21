---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c7ce5023f50fdc4cf5621e5649bbf08e1da076051ef52ed8c7c5a0b14bf97377
  pageDirectory: concepts
  sources:
    - fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - llm-foundry-yaml-configuration
    - LFYC
  citations:
    - file: fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md
title: LLM Foundry YAML Configuration
description: A structured YAML-based configuration system for LLM Foundry that defines model architecture, FSDP settings, training hyperparameters, dataset configuration, MLflow logging, callbacks, and checkpointing in a declarative format.
tags:
  - configuration
  - yaml
  - llm-training
timestamp: "2026-06-19T10:36:39.832Z"
---

# LLM Foundry YAML Configuration

**LLM Foundry YAML Configuration** refers to the structured YAML format used by [Mosaic LLM Foundry](https://github.com/mosaicml/llm-foundry) to define the complete configuration for training, fine-tuning, and evaluating large language models. The YAML configuration specifies model architecture, training hyperparameters, distributed training settings, dataset configuration, logging, and checkpointing parameters in a single declarative file. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

## Overview

LLM Foundry uses YAML as its primary configuration format, enabling users to define all aspects of a training run in a human-readable, version-controllable file. The configuration is loaded using the `%%yaml` magic command in Databricks notebooks and passed to the `train()` function via an [OmegaConf](https://omegaconf.readthedocs.io/) `DictConfig` object. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

## Configuration Structure

The YAML configuration is organized into several top-level sections that collectively define the training run:

### Seed and Randomness

The `seed` parameter sets the random seed for reproducibility across all random operations during training. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

```yaml
seed: 17
```

### Model Configuration

The `model` section specifies the model architecture, pretrained weights, and device initialization settings:

- **`name`**: The model type (e.g., `hf_causal_lm` for Hugging Face causal language models)
- **`pretrained`**: Boolean flag to load pretrained weights
- **`init_device`**: Device for model initialization (e.g., `mixed` for mixed device placement)
- **`use_auth_token`**: Whether to use authentication for accessing gated models
- **`use_flash_attention_2`**: Enable Flash Attention 2 for optimized attention computation
- **`pretrained_model_name_or_path`**: The Hugging Face model identifier or local path ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

```yaml
model:
  name: hf_causal_lm
  pretrained: true
  init_device: mixed
  use_auth_token: true
  use_flash_attention_2: true
  pretrained_model_name_or_path: meta-llama/Llama-3.1-8B
```

### Logger Configuration

The `loggers` section configures experiment tracking and metric logging, primarily through [MLflow](https://mlflow.org/):

- **`mlflow.resume`**: Whether to resume a previously logged run
- **`tracking_uri`**: The MLflow tracking server URI (e.g., `databricks` for Databricks-managed MLflow)
- **`rename_metrics`**: A mapping to rename internal metrics to user-friendly names
- **`log_system_metrics`**: Enable logging of system-level metrics (GPU utilization, memory)
- **`experiment_name`**: The MLflow experiment to log runs under
- **`run_name`**: A human-readable name for the run
- **`model_registry_uri`**: The model registry URI (e.g., `databricks-uc` for Unity Catalog)
- **`model_registry_prefix`**: Prefix for model registry paths ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

```yaml
loggers:
  mlflow:
    resume: true
    tracking_uri: databricks
    rename_metrics:
      time/token: time/num_tokens
      lr-DecoupledLionW/group0: learning_rate
    log_system_metrics: true
    experiment_name: "mlflow_experiment_name"
    run_name: llama3_8b-finetune
    model_registry_uri: databricks-uc
```

### Callbacks

The `callbacks` section defines hooks that execute during training for monitoring, optimization, and checkpointing:

- **`lr_monitor`**: Logs learning rate values during training
- **`run_timeout`**: Sets a maximum runtime limit (in seconds) before training is terminated
- **`scheduled_gc`**: Triggers garbage collection at specified batch intervals to manage memory
- **`speed_monitor`**: Tracks training throughput with a sliding window
- **`memory_monitor`**: Logs memory usage statistics
- **`runtime_estimator`**: Estimates remaining training time
- **`hf_checkpointer`**: Saves model checkpoints in Hugging Face format, with options for:
  - **`save_folder`**: Path for storing checkpoints
  - **`save_interval`**: How often to save (e.g., `1ep` for every epoch, `1h` for every hour)
  - **`precision`**: Checkpoint precision (e.g., `bfloat16`)
  - **`overwrite`**: Whether to overwrite existing checkpoints
  - **`mlflow_registered_model_name`**: Unity Catalog model name for registration
  - **`mlflow_logging_config`**: Configuration for model metadata logging, including task type and model metadata ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

```yaml
callbacks:
  lr_monitor: {}
  run_timeout:
    timeout: 7200
  scheduled_gc:
    batch_interval: 1000
  speed_monitor:
    window_size: 10
  memory_monitor: {}
  runtime_estimator: {}
  hf_checkpointer:
    save_folder: "/Volumes/main/sgc/checkpoints/llama3_1-8b-hf"
    save_interval: "1ep"
    precision: "bfloat16"
    overwrite: true
    mlflow_registered_model_name: "main.sgc.llama3_1_8b_full_ft"
    mlflow_logging_config:
      task: "llm/v1/completions"
      metadata:
        pretrained_model_name: "meta-llama/Llama-3.1-8B-Instruct"
```

### Optimizer Configuration

The `optimizer` section defines the optimization algorithm and its hyperparameters:

- **`name`**: Optimizer name (e.g., `decoupled_lionw` for the Decoupled LionW optimizer)
- **`lr`**: Learning rate
- **`betas`**: Adam/Lion beta coefficients
- **`weight_decay`**: Weight decay regularization strength ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

```yaml
optimizer:
  lr: 5.0e-07
  name: decoupled_lionw
  betas:
  - 0.9
  - 0.95
  weight_decay: 0
```

### Precision and Mixed Precision Training

The `precision` parameter controls the numerical precision for training:

- **`amp_bf16`**: Automatic mixed precision with bfloat16, balancing performance and numerical stability ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

```yaml
precision: amp_bf16
```

### Learning Rate Scheduler

The `scheduler` section configures the learning rate schedule:

- **`name`**: Scheduler type (e.g., `linear_decay_with_warmup`)
- **`alpha_f`**: Final learning rate multiplier (final_lr = alpha_f * initial_lr)
- **`t_warmup`**: Number of warmup steps or batches ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

```yaml
scheduler:
  name: linear_decay_with_warmup
  alpha_f: 0
  t_warmup: 10ba
```

### Tokenizer Configuration

The `tokenizer` section specifies the tokenizer to use:

- **`name`**: Hugging Face tokenizer identifier
- **`kwargs.model_max_length`**: Maximum sequence length for tokenization ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

```yaml
tokenizer:
  name: meta-llama/Llama-3.1-8B
  kwargs:
    model_max_length: 1024
```

### Algorithms (Gradient Clipping)

The `algorithms` section configures gradient clipping and other training algorithms:

- **`gradient_clipping.clipping_type`**: Method for clipping (e.g., `norm` for gradient norm scaling)
- **`gradient_clipping.clipping_threshold`**: Maximum gradient norm threshold ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

```yaml
algorithms:
  gradient_clipping:
    clipping_type: norm
    clipping_threshold: 1
```

### Auto-Resume and Logging

- **`autoresume`**: Whether to automatically resume training from the latest checkpoint
- **`log_config`**: Whether to log the full configuration to the experiment tracker ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

```yaml
autoresume: false
log_config: false
```

### FSDP Configuration

The `fsdp_config` section configures [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) for distributed training across multiple GPUs:

- **`verbose`**: Enable verbose logging for FSDP operations
- **`mixed_precision`**: Mixed precision mode (e.g., `PURE` for pure bf16 with FSDP)
- **`state_dict_type`**: How to save/load state dictionaries (e.g., `sharded` for per-rank shards)
- **`limit_all_gathers`**: Synchronize all-gather operations to limit peak memory
- **`sharding_strategy`**: How parameters are sharded (e.g., `FULL_SHARD` for full parameter sharding)
- **`activation_cpu_offload`**: Whether to offload activations to CPU to reduce GPU memory
- **`activation_checkpointing`**: Enable activation checkpointing (gradient checkpointing) to reduce memory
- **`activation_checkpointing_reentrant`**: Whether activation checkpointing uses reentrant mode ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

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

### Sequence Length and Output Paths

- **`max_seq_len`**: Maximum sequence length for training
- **`save_folder`**: Base path for saving training outputs (checkpoints, logs)
- **`dist_timeout`**: Timeout in seconds for distributed training synchronization ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

```yaml
max_seq_len: 1024
save_folder: "output_folder"
dist_timeout: 600
```

### Training Duration

The `max_duration` parameter specifies the total training duration:

- Uses a suffix to indicate units: `ba` for batch steps, `ep` for epochs, `tok` for tokens
- Example: `20ba` means 20 batch steps; `1ep` means 1 epoch ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

```yaml
max_duration: 20ba
```

### Progress Bar and Console Logging

- **`progress_bar`**: Whether to display a progress bar during training
- **`console_log_interval`**: How often to log metrics to console (e.g., `10ba` for every 10 batches) ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

```yaml
progress_bar: false
console_log_interval: 10ba
```

### Data Loader Configuration

The `train_loader` section defines the training data pipeline:

- **`name`**: Dataset type (e.g., `finetuning` for fine-tuning datasets)
- **`dataset`**: Dataset specification:
  - **`split`**: Dataset split to use (e.g., `test` for evaluation)
  - **`hf_name`**: Hugging Face dataset identifier
  - **`shuffle`**: Whether to shuffle the dataset
  - **`safe_load`**: Load dataset with safety checks
  - **`max_seq_len`**: Maximum sequence length for packing
  - **`packing_ratio`**: Dataset packing ratio (`auto` for automatic computation)
  - **`target_prompts`**: Which prompts to include (`none` for decoder-only)
  - **`target_responses`**: Which responses to include (`all` to include all)
  - **`allow_pad_trimming`**: Whether to trim padding tokens
  - **`decoder_only_format`**: Format for decoder-only models
- **`timeout`**: Data loading timeout in seconds
- **`drop_last`**: Drop the last incomplete batch
- **`pin_memory`**: Pin memory for faster GPU transfer
- **`num_workers`**: Number of data loading worker processes
- **`prefetch_factor`**: Number of batches to prefetch per worker
- **`persistent_workers`**: Keep worker processes alive between epochs ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

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

### Evaluation and Save Intervals

- **`eval_interval`**: How often to run evaluation (e.g., `1` for every epoch or `1ba` for every batch)
- **`save_interval`**: How often to save checkpoints (e.g., `1h` for every hour)
- **`save_overwrite`**: Whether to overwrite existing checkpoints
- **`save_weights_only`**: Whether to save only model weights (not optimizer state)
- **`save_num_checkpoints_to_keep`**: Maximum number of checkpoints to retain ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

```yaml
eval_interval: 1
save_interval: 1h
save_overwrite: true
save_weights_only: false
save_num_checkpoints_to_keep: 1
```

### Logging Level

The `python_log_level` parameter controls the verbosity of Python logging output: ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

```yaml
python_log_level: debug
```

### Batch Size Configuration

- **`device_eval_batch_size`**: Batch size per device for evaluation
- **`global_train_batch_size`**: Total batch size across all devices for training
- **`device_train_microbatch_size`**: Microbatch size per device for gradient accumulation (must divide `global_train_batch_size` evenly) ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

```yaml
device_eval_batch_size: 1
global_train_batch_size: 32
device_train_microbatch_size: 1
```

### Console Logging

The `log_to_console` parameter controls whether training metrics are printed to the console during training: ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

```yaml
log_to_console: true
```

## Dynamic Configuration Overrides

YAML configurations can be dynamically modified at runtime using Python. The `%%yaml config` magic command loads the YAML into a Python dictionary, allowing programmatic overrides before passing the configuration to the training function:

```python
config["loggers"]["mlflow"]["experiment_name"] = MLFLOW_EXPERIMENT_NAME
config["save_folder"] = OUTPUT_DIR
config["callbacks"]["hf_checkpointer"]["save_folder"] = OUTPUT_DIR
config["callbacks"]["hf_checkpointer"]["mlflow_registered_model_name"] = f"{UC_CATALOG}.{UC_SCHEMA}.{UC_MODEL_NAME}"
```

This pattern enables parameterization of configuration values through notebook widgets, environment variables, or programmatic logic without

# Citations

1. [fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md](/references/fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws-d6760424.md)
