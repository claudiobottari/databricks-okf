---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f1325e23925853b4c76bf200a9b152ad5c77e3b199f2e48eb457087e397089cf
  pageDirectory: concepts
  sources:
    - fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - supervised-fine-tuning-sft-of-llms
    - SF(OL
    - Fine-tuning (LLM)
  citations:
    - file: fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
title: Supervised Fine-Tuning (SFT) of LLMs
description: A training approach where a pre-trained language model is further trained on labeled conversational data to improve its performance on specific tasks, using techniques like bfloat16 precision, cosine learning rate scheduling, and gradient accumulation.
tags:
  - machine-learning
  - llm
  - fine-tuning
  - training
timestamp: "2026-06-18T12:21:23.699Z"
---

# Supervised Fine-Tuning (SFT) of LLMs

**Supervised Fine-Tuning (SFT)** is a training method that adapts a pre-trained large language model (LLM) to a specific task or domain by further training it on a labeled dataset of input–output pairs. In the context of LLM alignment, SFT is often the first stage after pre-training, teaching the model to follow instructions and produce desired conversational responses. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Common Tooling and Optimizations

### TRL (Transformers Reinforcement Learning)

TRL is a library that provides tools for training language models with supervised fine-tuning and reinforcement learning. It includes the `SFTTrainer` class, which simplifies loading a base model and tokenizer, formatting data, and running the training loop with support for various optimization techniques.^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

### DeepSpeed ZeRO Stage 3

DeepSpeed ZeRO (Zero Redundancy Optimizer) Stage 3 is a memory optimization technique that partitions model parameters, gradients, and optimizer states across all available GPUs. This reduces memory consumption per GPU and enables training of large models that would not fit into a single GPU’s memory. Key configuration options include bfloat16 precision for faster training and reduced memory usage, overlapping gradient communication with computation, and contiguous gradients.^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

For single‑node multi‑GPU setups, a typical DeepSpeed ZeRO 3 configuration disables CPU offloading to keep all data on GPUs for maximum performance, and sets `overlap_comm: True`, `contiguous_gradients: True`, and `stage3_gather_16bit_weights_on_model_save: True` to enable efficient checkpoint saving.^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Typical SFT Workflow

A common SFT workflow executed on Databricks AI Runtime with 8 H100 GPUs follows these steps:^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

1. **Configure compute and environment** – Select serverless GPU compute (e.g., 8× H100) and set environment variables for a HuggingFace token, Unity Catalog storage paths, and an MLflow experiment.

2. **Install dependencies** – The AI Runtime pre‑installs most required libraries; only `deepspeed` typically needs to be added.

3. **Load tokenizer and base model** – The tokenizer is loaded from the HuggingFace hub, and a padding token is added if missing (usually set to `eos_token`).

4. **Load dataset** – A conversational dataset (e.g., the Capybara dataset from TRL) is loaded from HuggingFace.

5. **Create DeepSpeed configuration** – A JSON config file is written with ZeRO Stage 3 settings.

6. **Define training arguments** – Parameters such as `per_device_train_batch_size`, `gradient_accumulation_steps`, `learning_rate`, `max_steps`, `warmup_steps`, and `lr_scheduler_type` are set. Typical values for demonstration: batch size 2 per device, learning rate 2e-4, cosine scheduler, bf16 enabled, `report_to: "mlflow"`.

7. **Run distributed training** – The training function is decorated with `@distributed(gpus=8, gpu_type='H100')` from the serverless GPU library, which automatically provisions the GPUs and handles distributed setup. Inside the function, an `SFTTrainer` is initialized with the model name, training arguments (including the DeepSpeed config path), tokenizer, and dataset. The trainer calls `.train()` and saves the model.

8. **Log and register the model** – The fine‑tuned model is logged to MLflow and registered in Unity Catalog with the task type `llm/v1/chat`, along with the tokenizer and an input example.

## Best Practices

- **Gradient checkpointing** can be disabled when using DeepSpeed ZeRO 3 on H100 hardware, as the memory savings from partitioning are sufficient.^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]
- **Save checkpoints regularly** and keep the best model based on evaluation loss using `load_best_model_at_end` and `metric_for_best_model`.^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]
- **Use `remove_unused_columns=False`** when the dataset contains columns that are not needed by the model but are still present in the data.^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]
- **Set a limited `max_steps` for demonstration** and increase it for full training on the complete dataset.^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Requirements

- GPU compute (e.g., 8× H100) with AI Runtime support.
- HuggingFace access token stored in secrets.
- Unity Catalog catalog, schema, and volume for storing checkpoints and registering the model.
- Python packages: `transformers`, `datasets`, `trl`, `deepspeed`, and `mlflow`. Most are pre‑installed on AI Runtime.^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Related Concepts

- TRL Library – The Transformers Reinforcement Learning toolkit for SFT and RLHF.
- [DeepSpeed ZeRO](/concepts/deepspeed-zero-stage-3.md) – Memory optimization stages for distributed training.
- [AI Runtime](/concepts/ai-runtime.md) – Databricks‑managed GPU compute for training workloads.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – Experiment tracking and model registration.
- [Unity Catalog](/concepts/unity-catalog.md) – Governance and model storage.

## Sources

- fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md

# Citations

1. [fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md](/references/fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws-4a3f88ec.md)
