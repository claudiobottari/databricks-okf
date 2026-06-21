---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ad4208ddb1e7b05906a567a5f7c05b345a7b7bf020120f9fdaab407110acf62b
  pageDirectory: concepts
  sources:
    - fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-serverless-gpu
    - DSG
    - Databricks Serverless
  citations:
    - file: fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md
title: Databricks Serverless GPU
description: A serverless compute environment on Databricks that provides on-demand GPU resources (e.g., 8×H100) for distributed training workloads without requiring manual cluster management.
tags:
  - databricks
  - gpu-compute
  - cloud-infrastructure
timestamp: "2026-06-19T18:50:18.561Z"
---

Below is the updated wiki page for **Databricks Serverless GPU**, written solely from the provided source material and structured for clarity.

---

# Databricks Serverless GPU

**Databricks Serverless GPU** is a serverless compute option that provides on‑demand GPU resources for running distributed training and inference workloads without requiring users to provision or manage clusters. It supports popular large language model (LLM) training frameworks and integrates seamlessly with Databricks notebooks, MLflow, and Unity Catalog. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

## Connecting to Serverless GPU Compute

To use serverless GPU compute in a notebook:

1. Click the notebook’s compute selector in the top right and select **Serverless GPU**.
2. Open the **Environment** side panel on the right.
3. Set **Accelerator** to **8xH100**.
4. Select the **Standard** base environment and set **Environment version** to **5**, which contains the libraries needed for running distributed training examples.
5. Click **Apply** and then **Confirm**. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

After connecting, the notebook session is backed by eight H100 GPUs on a single node.

## Distributed Training with the `@distributed` Decorator

The `serverless_gpu` Python library provides a `@distributed` decorator that runs a user‑defined function across the connected serverless GPU compute. The decorator accepts parameters such as `gpus` (number of GPUs) and `gpu_type` (e.g., `'H100'`), and handles distributed training orchestration automatically. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

Example usage:

```python
from serverless_gpu import distributed

@distributed(gpus=8, gpu_type='H100')
def run_llm_foundry():
    # training code
    pass
```

The function defined with this decorator executes across all specified GPUs, and its return value (e.g., an [MLflow Run](/concepts/mlflow-run.md) ID) is collected from the main process. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

## Integration with MLflow and Unity Catalog

Serverless GPU compute integrates with [MLflow](/concepts/mlflow.md) for experiment tracking and metric logging, and with [Unity Catalog](/concepts/unity-catalog.md) for storing model checkpoints and registering trained models. In the notebook configuration:

- The MLflow experiment name and model registry URI are set in the YAML configuration or via widgets.
- Training metrics, system metrics (e.g., GPU memory, throughput), and custom callbacks logs are automatically recorded.
- Model checkpoints can be saved to Unity Catalog Volumes, and the final model can be registered in the Unity Catalog registry using a qualified model name (e.g., `catalog.schema.model_name`). ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

The framework’s `hf_checkpointer` callback supports `mlflow_registered_model_name` to automatically register the trained model upon saving. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

## Example: Fine‑tuning Llama 3.1 8B with Mosaic LLM Foundry

The provided tutorial notebook demonstrates fine‑tuning a Llama 3.1 8B model using [Mosaic LLM Foundry](/concepts/mosaic-llm-foundry.md) on Databricks Serverless GPU. Key steps include: ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

1. **Install required libraries**  
   Install `flash-attn` (from a prebuilt wheel to avoid slow compilation), `llm-foundry[gpu]`, `hf_transfer`, and `yamlmagic`. Then restart the Python environment.
   ```python
   %pip install --no-deps "...flash_attn-2.7.4.post1...whl"
   %pip install llm-foundry[gpu]==0.20.0
   %pip install hf_transfer
   %pip install git+https://github.com/josejg/yamlmagic.git
   dbutils.library.restartPython()
   ```

2. **Configure Unity Catalog paths**  
   Use `dbutils.widgets` to set catalog, schema, model name, and volume for storing checkpoints and model registrations.

3. **Define training configuration in YAML**  
   The configuration specifies:
   - Model: `meta-llama/Llama-3.1-8B` with flash attention enabled.
   - FSDP settings: mixed precision `PURE`, sharding strategy `FULL_SHARD`, activation checkpointing enabled.
   - Optimizer: `decoupled_lionw` with learning rate `5.0e-7`.
   - Scheduler: linear decay with warmup.
   - Dataset: `mosaicml/dolly_hhrlhf` (test split).
   - Global train batch size: 32, device train micro‑batch size: 1.
   - MLflow logging, callbacks (lr monitor, speed monitor, memory monitor, Hugging Face checkpointer).
   - Model registered under `{catalog}.{schema}.{model_name}`.

4. **Define and run the distributed training function**  
   The training function is wrapped with `@distributed(gpus=8, gpu_type='H100')`. Inside, it sets the Hugging Face token, enables `hf_transfer` for fast downloads, and calls `llmfoundry.command_utils.train.train()` with the configuration. The function returns the [MLflow Run](/concepts/mlflow-run.md) ID. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

   ```python
   from serverless_gpu import distributed
   from llmfoundry.command_utils.train import train
   from omegaconf import DictConfig

   @distributed(gpus=8, gpu_type='H100')
   def run_llm_foundry():
       import os
       os.environ["HUGGING_FACE_HUB_TOKEN"] = HF_TOKEN
       from huggingface_hub import constants
       constants.HF_HUB_ENABLE_HF_TRANSFER = True
       train(DictConfig(config))
       mlflow_run_id = mlflow.last_active_run().info.run_id if mlflow.last_active_run() else None
       return mlflow_run_id

   mlflow_run_id = run_llm_foundry.distributed()[0]
   ```

5. **Track results**  
   The returned [MLflow Run](/concepts/mlflow-run.md) ID can be used to view metrics and logs in the MLflow UI.

The example uses [FSDP](/concepts/fsdp-fully-sharded-data-parallel.md) (Fully Sharded Data Parallel) to shard model parameters, gradients, and optimizer states across all eight GPUs, enabling fine‑tuning of the 8B‑parameter model on a single serverless node. ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

## Related Concepts

- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – General serverless compute paradigm on Databricks.
- [8xH100 Single‑Node Configuration](/concepts/8xh100-single-node-configuration.md) – Specific accelerator setup of eight H100 GPUs per node.
- [Distributed training](/concepts/workload-yaml-for-distributed-training.md) – Training models across multiple GPUs or nodes.
- [FSDP](/concepts/fsdp-fully-sharded-data-parallel.md) – Fully Sharded Data Parallel for memory‑efficient distributed training.
- [Mosaic LLM Foundry](/concepts/mosaic-llm-foundry.md) – Framework for training and fine‑tuning LLMs.
- Llama 3.1 8B – Popular open‑source large language model used in the example.
- [MLflow](/concepts/mlflow.md) – Experiment tracking and model registry.
- [Unity Catalog](/concepts/unity-catalog.md) – Data governance and model storage.

## Sources

- fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md

# Citations

1. [fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md](/references/fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws-d6760424.md)
