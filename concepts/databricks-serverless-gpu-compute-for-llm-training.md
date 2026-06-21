---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: af622c3ac7638d0f341e3a63d9cddf79cdafb4d99991b8d718ac9b181181f3c8
  pageDirectory: concepts
  sources:
    - finetune-llama-32-3b-with-unsloth-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-serverless-gpu-compute-for-llm-training
    - DSGCFLT
  citations:
    - file: finetune-llama-32-3b-with-unsloth-databricks-on-aws.md
title: Databricks Serverless GPU Compute for LLM Training
description: Databricks AI Runtime environment providing serverless GPU compute with A10 accelerators, pre-installed with Unsloth and deep learning libraries for fine-tuning large language models.
tags:
  - infrastructure
  - databricks
  - gpu-compute
timestamp: "2026-06-19T10:36:16.862Z"
---

# Databricks Serverless GPU Compute for LLM Training

**Databricks Serverless GPU Compute** is a serverless compute option that provides GPU accelerators for deep learning workloads on Databricks. It is typically used for training and fine-tuning large language models (LLMs), such as Llama 3.2 3B, with frameworks like [Unsloth](/concepts/unsloth.md). Serverless GPU compute does not require managing cluster infrastructure; the user selects accelerator type and base environment at notebook level. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Requirements

To use Databricks Serverless GPU Compute for LLM training, a notebook must be attached to a serverless compute instance with a specific GPU accelerator. The tutorial example requires an **A10 GPU accelerator** (selectable in the environment panel under **Hardware**). ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

The **Base environment** must be set to **AI v5** (available from the environment panel). The AI v5 environment includes pre-installed deep learning libraries such as `unsloth`, `unsloth_zoo`, `bitsandbytes`, `trl`, `xformers`, and `mlflow`, so no additional library installation is needed. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Provisioning

After applying the compute configuration, serverless compute provisioning can take up to eight minutes before the notebook becomes ready to run. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Typical Workflow for LLM Fine-Tuning

A standard workflow on Databricks Serverless GPU Compute includes the following steps, as demonstrated in the [finetune Llama 3.2 3B with Unsloth](/concepts/lora-finetuning-with-unsloth-on-llama-32.md) tutorial:

1. **Configure Unity Catalog and model settings** – Define catalog, schema, model name, and volume paths for saving checkpoints and registering the final model. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]
2. **Load the base model and tokenizer** – Use Unsloth’s `FastLanguageModel.from_pretrained()` to load the model with a chosen maximum sequence length and automatic dtype detection. Support for 4-bit quantization is available to reduce memory. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]
3. **Apply LoRA adapters** – Convert to a PEFT model using `FastLanguageModel.get_peft_model()` with rank‑16 adapters targeting attention and feed‑forward layers, significantly reducing trainable parameters and memory usage. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]
4. **Load and format the dataset** – Load a dataset (e.g., FineTome-100k), apply a chat template, and standardize into ShareGPT format. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]
5. **Configure the trainer** – Set up `SFTTrainer` with hyperparameters (batch size, learning rate, optimizer) and enable MLflow tracking via `report_to = "mlflow"`. Use `train_on_responses_only` to train only on assistant responses. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]
6. **Train** – Run the fine-tuning loop inside an `mlflow.start_run()` to log training metrics, loss, and system metrics (GPU utilization, memory). ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]
7. **Merge LoRA adapters and register** – Merge the trained adapters into the base model, log the model to MLflow, and register it in [Unity Catalog](/concepts/unity-catalog.md) with `task='llm/v1/chat'` for deployment. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Related Concepts

- [Unsloth](/concepts/unsloth.md) – Library providing optimized LoRA implementations for fast fine-tuning.
- LoRA – Parameter-efficient fine-tuning technique used to reduce memory and training time.
- [MLflow](/concepts/mlflow.md) – Experiment tracking and model registry integration.
- [Unity Catalog](/concepts/unity-catalog.md) – Central catalog for model registration and governance.
- [Supervised Fine-Tuning (SFT)](/concepts/supervised-fine-tuning-sft.md) – Training paradigm using labeled instruction‑response pairs.
- Serverless Compute on Databricks – General serverless compute infrastructure.
- A10 GPU – GPU accelerator used in the tutorial.

## Sources

- finetune-llama-32-3b-with-unsloth-databricks-on-aws.md

# Citations

1. [finetune-llama-32-3b-with-unsloth-databricks-on-aws.md](/references/finetune-llama-32-3b-with-unsloth-databricks-on-aws-83073ff0.md)
