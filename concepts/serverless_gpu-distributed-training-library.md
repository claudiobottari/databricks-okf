---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f25033bd5464a2c83b1423cb6b67ce5e0e037cd01c8afe8eb3d3162df877a9a5
  pageDirectory: concepts
  sources:
    - distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless_gpu-distributed-training-library
    - SDTL
  citations:
    - file: distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
title: serverless_gpu distributed training library
description: A Python library enabling distributed GPU training on Databricks Serverless GPU compute with decorators like @distributed to specify GPU count and type.
tags:
  - machine-learning
  - distributed-training
  - databricks
  - python-library
timestamp: "2026-06-18T15:31:51.606Z"
---

# serverless_gpu Distributed Training Library

The **serverless_gpu** library is a distributed training utility provided in the Databricks environment, designed to simplify launching multi-GPU training jobs from a single notebook cell. It is used in conjunction with frameworks such as [Unsloth](/concepts/unsloth.md) and PyTorch to distribute workloads across multiple GPUs, typically on GPU clusters like 8×H100. The library handles process spawning, rank assignment, and result collection, allowing users to define the training logic in a single function and execute it in parallel. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Usage

### 1. Import the library

```python
from serverless_gpu import distributed
from serverless_gpu import runtime as rt
```

The `distributed` module provides the decorator, and the `runtime` module gives access to distributed runtime utilities such as querying the global rank. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### 2. Decorate the training function

The `@distributed(gpus=<n>, gpu_type='<type>')` decorator is applied to the function that contains the training logic. The decorator arguments specify the number of GPUs and the GPU type (e.g., `'h100'`). Inside the function, the local rank is obtained from the environment variable `LOCAL_RANK` and used to set the CUDA device. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

```python
@distributed(gpus=8, gpu_type='h100')
def run_train():
    import torch
    local_rank = int(os.environ.get("LOCAL_RANK", 0))
    torch.cuda.set_device(local_rank)
    # ... training code ...
    return mlflow_run_id
```

### 3. Execute the distributed training

The decorated function is called using the `.distributed()` method, which launches the training across the specified GPUs. The method returns a list of results from each process. Typically only the result from the rank 0 process (e.g., an [MLflow Run](/concepts/mlflow-run.md) ID) is used. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

```python
run_id = run_train.distributed()[0]
```

### 4. Access runtime utilities

The `rt` object provides functions like `rt.get_global_rank()`, which can be used to conditionally execute code only on the primary process (e.g., saving model artifacts). ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Integration with MLflow and Unity Catalog

The serverless_gpu library works seamlessly with [MLflow Tracking](/concepts/mlflow-tracking.md) and [Unity Catalog](/concepts/unity-catalog.md). In the example notebook, the training function returns an [MLflow Run](/concepts/mlflow-run.md) ID from the rank‑0 process. After training completes, the model is registered in Unity Catalog using `mlflow.transformers.log_model()`, which logs the model artifacts, tokenizer, and metadata under the Unity Catalog model namespace. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Integration with Unsloth

The library is commonly used with [Unsloth](/concepts/unsloth.md) for efficient fine‑tuning of LLMs. The training function imports Unsloth modules (`FastLanguageModel`, `get_chat_template`, etc.) and [TRL](/concepts/trl-transformer-reinforcement-learning.md)’s `SFTTrainer`. The distributed training configuration includes setting `device_map={'': local_rank}` to assign each process its GPU, and enabling non‑reentrant gradient checkpointing to avoid sync errors in DDP. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Requirements

- The environment must have the `serverless_gpu` package installed. This package is available in the Databricks AI Runtime (e.g., AI v5), which also includes [Unsloth](/concepts/unsloth.md) and its dependencies (`unsloth_zoo`, `trl`, `peft`, `bitsandbytes`, `xformers`, `einops`). ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]
- A GPU-accelerated compute cluster with the requested number and type of GPUs (e.g., 8×H100) must be attached. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Related Concepts

- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- [Unsloth](/concepts/unsloth.md)
- [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md)
- [MLflow Tracking](/concepts/mlflow-tracking.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- Databricks AI Runtime for Machine Learning
- [SFTTrainer from TRL](/concepts/sfttrainer-trl.md)

## Sources

- distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md

# Citations

1. [distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md](/references/distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws-5c6e3457.md)
