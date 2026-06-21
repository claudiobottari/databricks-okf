---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4756856a1a8fe0ae861118fc1d219f3f700ea3d202312a5230c99d9edc03eadd
  pageDirectory: concepts
  sources:
    - fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - llama-32-1b-fine-tuning-on-databricks
    - L31FOD
  citations:
    - file: fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
title: Llama 3.2 1B Fine-tuning on Databricks
description: A reference workflow for fully fine-tuning the Llama 3.2 1B Instruct model on 8xH100 GPUs using AI Runtime, DeepSpeed, and TRL, with bfloat16 precision and gradient checkpointing.
tags:
  - llama
  - fine-tuning
  - databricks
  - tutorial
timestamp: "2026-06-19T18:50:56.536Z"
---

## Llama 3.2 1B Fine-tuning on Databricks

**Llama 3.2 1B Fine-tuning on Databricks** refers to the process of fully fine-tuning a Meta Llama 3.2 1B Instruct model using supervised fine-tuning (SFT) on the Databricks platform. The recommended approach uses the [Transformers Reinforcement Learning (TRL)](/concepts/trl-transformer-reinforcement-learning.md) library with [DeepSpeed](/concepts/deepspeed.md) ZeRO Stage 3 optimization, running on a single node with 8 H100 GPUs provisioned via [AI Runtime](/concepts/ai-runtime.md) (serverless GPU compute). ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

### Requirements

The notebook requires Databricks AI Runtime with 8 H100 GPUs (no cluster configuration needed), a Unity Catalog [Catalog and Schema](/concepts/catalog-and-schema.md) for storing model checkpoints and registering the trained model, a HuggingFace access token stored in Databricks secrets to download the base model and dataset, and the `deepspeed` Python package, which must be installed separately as the rest of the required libraries are preinstalled in the AI Runtime environment. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

### Connect to Serverless GPU Compute

To connect to serverless GPU compute, select **Serverless GPU** from the notebook's compute selector, then choose **8xH100** as the accelerator and **AI v5** as the environment, which contains the required libraries. Apply the settings. The training function automatically provisions 8 H100 GPUs for distributed training. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

### Configure Unity Catalog and Environment Variables

The notebook sets up Unity Catalog locations for storing model checkpoints and registering the trained model. It uses query parameters to configure a catalog, schema, model name, and volume. The HuggingFace token is retrieved from Databricks secrets, and an [MLflow](/concepts/mlflow.md) experiment is created for tracking training metrics. A Unity Catalog volume is created if it does not already exist. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

### Create DeepSpeed ZeRO Stage 3 Configuration

DeepSpeed ZeRO (Zero Redundancy Optimizer) Stage 3 partitions model parameters, gradients, and optimizer states across all GPUs to reduce memory consumption per GPU. The configuration uses bfloat16 precision (not fp16), no CPU offloading, overlapping gradient communication, and contiguous gradients. All model states are kept on GPUs for maximum performance on H100 hardware. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

### Define Training Parameters

The training configuration uses the Llama 3.2 1B Instruct model and the Capybara dataset from the TRL library. Key hyperparameters include a per-device batch size of 2, 4 gradient accumulation steps leading to an effective batch size of 64, a learning rate of 2e‑4 with a cosine scheduler and warm‑up, and a maximum of 60 training steps (intended for demonstration; increase for full training). Bfloat16 precision and gradient checkpointing are used to optimize memory usage. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

### Define the Distributed Training Function

The `@distributed` decorator from the `serverless_gpu` library provisions 8 H100 GPUs and handles distributed training setup. The decorated function loads the base model and tokenizer from HuggingFace, sets up chat formatting, loads the dataset, initializes a [TRL SFTTrainer](/concepts/trl-sfttrainer.md) with DeepSpeed optimization, trains the model, saves checkpoints to the Unity Catalog volume, logs metrics to MLflow, and returns the training status, final loss, and [MLflow Run](/concepts/mlflow-run.md) ID. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

### Run the Distributed Training Job

The training job is executed by calling `.distributed()` on the decorated function. The process automatically provisions the 8 H100 GPUs, downloads the model and dataset, performs full fine‑tuning, saves checkpoints, and logs metrics. The returned results include the status, final loss, and [MLflow Run](/concepts/mlflow-run.md) ID. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

### Save the Fine‑Tuned Model and Test Inference

After training, the fine‑tuned model can be loaded from the checkpoint directory in the Unity Catalog volume using `AutoModelForCausalLM` and `AutoTokenizer`. Inference is tested with a sample conversational prompt (e.g., “What is machine learning?”) using the model’s `generate` method. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

### Register the Model in Unity Catalog

The fine‑tuned model is logged to MLflow and registered in Unity Catalog. The logging includes the model and tokenizer components, the task type `llm/v1/chat`, an input example with a chat message, and the registered model name. Once registered, the model can be deployed to [Model Serving](/concepts/model-serving.md) endpoints or used for batch inference. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

### Next Steps

After completing fine‑tuning, users can explore the following resources: [AI Runtime](/concepts/ai-runtime.md) documentation, best practices for AI Runtime, troubleshooting guides, multi‑GPU and multi‑node distributed training, training models with MLflow, and deploying models with Model Serving. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

### Sources

- fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md

# Citations

1. [fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md](/references/fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws-4a3f88ec.md)
