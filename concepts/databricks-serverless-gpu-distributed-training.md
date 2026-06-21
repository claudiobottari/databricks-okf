---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 95c98397473e68c97029ae530226817a670188ce7fe5714c127dba3da96dce1d
  pageDirectory: concepts
  sources:
    - distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
    - distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-serverless-gpu-distributed-training
    - DSGDT
  citations:
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
    - file: distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
    - file: distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Databricks Serverless GPU Distributed Training
description: A Databricks compute paradigm that provisions on-demand GPU clusters (e.g., 8xH100) for distributed training using the @distributed decorator, handling data parallelism automatically.
tags:
  - distributed-training
  - databricks
  - serverless-compute
timestamp: "2026-06-19T18:32:54.308Z"
---

# Databricks Serverless GPU Distributed Training

**Databricks Serverless GPU Distributed Training** enables you to run multi-GPU training workloads without managing any underlying infrastructure. By using serverless GPU compute and the `@distributed` decorator from the `serverless_gpu` Python library, you can scale training across 8 H100 GPUs on a single node with minimal configuration. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Overview

Serverless GPU compute is an on-demand compute model that provisions GPU resources automatically when you attach a notebook or run a distributed function. There is no cluster to start, stop, or resize. The compute environment is pre-configured in an **AI Runtime** version (e.g., **AI v5**) that includes all common libraries for distributed deep learning, such as PyTorch, Transformers, TRL, and PyTorch Lightning. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Key Features

### Serverless GPU Compute

- **Zero cluster management** – Compute is attached instantly from the notebook compute selector. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]
- **Choice of accelerators** – For training, the **8xH100** configuration is recommended, providing 8 NVIDIA H100 80GB HBM3 GPUs with 640 GB of total GPU memory. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]
- **Environment isolation** – The **AI v5** environment ships with pre-installed packages for GPU workloads. Additional packages can be installed at runtime. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

### 8xH100 Single-Node Configuration

The 8xH100 configuration is purpose-built for large model training. Each H100 GPU has 81,559 MiB of total memory and a maximum power draw of 700 W. This provides high floating-point operations per second (FLOPS) and high-bandwidth memory (HBM) compared to A10 GPUs. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### AI Runtime Environment (AI v5)

The AI v5 environment includes libraries for distributed training such as `transformers`, `datasets`, `trl`, `peft`, `pytorch-lightning`, and `torchrec`. Some packages (e.g., `torchaudio`, `fbgemm-gpu`, `torchrec`) may need to be installed separately. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Using the `@distributed` Decorator

The `serverless_gpu` library provides a `@distributed` decorator that distributes a Python function across multiple GPUs on a single node. When the decorated function is called with `.distributed()`, the system launches one process per GPU, automatically setting environment variables like `RANK`, `LOCAL_RANK`, and `WORLD_SIZE`. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### Basic Usage

```python
from serverless_gpu import distributed
from serverless_gpu import runtime as rt

@distributed(gpus=8, gpu_type='h100')
def hello_world(name: str) -> list[int]:
    if rt.get_local_rank() == 0:
        print('hello world', name)
    return rt.get_global_rank()

result = hello_world.distributed('SGC')
# result == [0, 1, 2, 3, 4, 5, 6, 7]
```

- `gpus=8` specifies that 8 processes are launched, one per GPU.
- `rt.get_local_rank()` returns the rank of the process within the node.
- `rt.get_global_rank()` returns the rank across all processes. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### Function Definition and Execution

Inside the decorated function, standard PyTorch distributed initialization is handled automatically. You can use `torch.distributed`, PyTorch Lightning `Trainer`, or any other library that respects `RANK` and `WORLD_SIZE`. The function must be called with `.distributed()` to trigger the multi‑GPU launch. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md, distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## Distributed Training Strategies

The `@distributed` decorator works with any parallelism strategy that the underlying libraries support. The following strategies are demonstrated in the provided examples.

### Distributed Data Parallel (DDP)

Both example notebooks use **Distributed Data Parallel (DDP)**. In the PyTorch Lightning example, the `Trainer` is configured with `strategy="ddp"` and `devices=8`. The model is replicated across all 8 GPUs, and each GPU processes a different micro‑batch. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

For non-Lightning workflows, the DDP environment variables are set automatically by the decorator, allowing you to use `torch.nn.parallel.DistributedDataParallel` inside the function. The fine-tuning example for `gpt-oss-20b` uses `SFTTrainer` from the TRL library, which internally handles DDP when `WORLD_SIZE > 1`. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

### Memory Optimization (LoRA and MXFP4 Quantization)

For large models (e.g., 20B parameters), the following techniques reduce memory usage enough to fit on 8 H100 GPUs:

- **LoRA (Low-Rank Adaptation)** – Trainable low‑rank adapters are added to the base model, while the original weights remain frozen. This drastically reduces the number of trainable parameters. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]
- **MXFP4 quantization** – The base model is loaded in 4‑bit floating point format using `Mxfp4Config`, which shrinks memory requirements. The LoRA adapters are trained in higher precision. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]
- **Gradient checkpointing** – Enabled via `gradient_checkpointing=True` in the training arguments, trading compute for memory. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]
- **Mixed precision (`bfloat16`)** – The model is loaded with `dtype=torch.bfloat16` to reduce memory footprint without significant accuracy loss. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## Example Workflows

### Fine‑Tuning Large Language Models (gpt‑oss‑20b)

This end‑to‑end notebook fine‑tunes OpenAI’s 20B parameter model on a multilingual thinking dataset. Key steps:

1. Connect the notebook to **8xH100** serverless GPU with the **AI v5** environment.
2. Define a training function decorated with `@distributed(gpus=8, gpu_type="h100")`.
3. Inside the function, load the model with `Mxfp4Config`, apply LoRA, and use `SFTTrainer` for supervised fine‑tuning.
4. Save the trained LoRA adapters to a Unity Catalog volume.
5. Register the merged model in Unity Catalog using MLflow.

Training takes 30–60 minutes. The fine‑tuned model demonstrates multilingual chain‑of‑thought reasoning. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

### Distributed Recommendation Model Training (Two‑Tower with PyTorch Lightning)

This notebook builds a two‑tower recommendation model using **PyTorch Lightning** and **TorchRec**. Key steps:

1. Download the *Learning from Sets* dataset, preprocess, and split.
2. Define a `TwoTowerModel` with `EmbeddingBagCollection` from TorchRec.
3. Wrap the model in a `LitTwoTower` LightningModule with AUROC metrics.
4. Decorate the training function with `@distributed(gpus=8, gpu_type="H100")`.
5. Inside the function, instantiate a Lightning `Trainer` with `strategy="ddp"` and `devices=8`.
6. After training, save the best checkpoint and register the model as an MLflow PyFunc for serving.

The training runs across all 8 GPUs, with logs and checkpoints automatically synced. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Best Practices

- **Select the correct accelerator** – For training, choose **8xH100** rather than A10 GPUs, which are better suited for inference. Use the **Environment** panel in the notebook UI. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md, distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]
- **Install additional packages at the top of the notebook** – Use `%pip install` and `dbutils.library.restartPython()` to ensure all dependencies are available before the distributed function runs. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]
- **Log GPU memory during development** – Use the `log_gpu_memory()` utility to track allocated and reserved memory per GPU rank. This helps identify memory bottlenecks. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]
- **Use Unity Catalog volumes for checkpoint storage** – Save model checkpoints and adapters to locations like `/Volumes/<catalog>/<schema>/<volume>/`. This makes them accessible across sessions. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md, distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]
- **Report metrics to MLflow** – Enable `report_to="mlflow"` in training arguments or use `mlflow.pytorch.autolog()` to capture training metrics automatically. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md, distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Troubleshooting

- **403 PERMISSION_DENIED errors** – If you see `403 Client Error: Forbidden PERMISSION_DENIED: Unable to use fallback policies`, it means the workspace’s default serverless budget policy is disabled. Assign a budget policy to the MLflow experiment using the UI or the tag `mlflow.workload_creation_policy_id`. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]
- **Out‑of‑memory (OOM) errors** – Reduce batch size per device, enable gradient checkpointing, or use a stronger quantization config (e.g., MXFP4). Consider switching to a larger GPU configuration if available. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]
- **Environment mismatches** – Ensure all required libraries are installed in the AI v5 environment. If a library is missing, install it before calling `.distributed()`. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Related Concepts

- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md)
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md)
- [MXFP4 Quantization](/concepts/mxfp4-quantization.md)
- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md)
- TorchRec
- [TRL (Transformer Reinforcement Learning)](/concepts/trl-transformer-reinforcement-learning.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- MLflow Integration

## Sources

- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
- distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
- distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
2. [distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md](/references/distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws-093d5979.md)
3. [distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md](/references/distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws-7ee24e1a.md)
4. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
