---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6141ed820ebc4971b3c6553b47350abd3ce2316fa367f350a4cb2306699a58d1
  pageDirectory: concepts
  sources:
    - distributed-training-with-ray-train-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-train-torchtrainer
    - RTT
    - Ray Train's TorchTrainer
    - TorchTrainer
  citations:
    - file: distributed-training-with-ray-train-databricks-on-aws.md
title: Ray Train TorchTrainer
description: A Ray Train API that launches one worker per GPU, wraps models in DDP, and shards datasets across distributed workers for data-parallel training.
tags:
  - distributed-training
  - ray
  - pytorch
timestamp: "2026-06-19T18:37:59.720Z"
---

```markdown
---
title: Ray Train TorchTrainer
summary: Ray Train's distributed training class for PyTorch that launches one worker per GPU, wraps models in DDP, shards datasets across workers, and aggregates metrics.
sources:
  - distributed-training-with-ray-train-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:19:19.499Z"
updatedAt: "2026-06-19T10:19:19.499Z"
tags:
  - ray
  - pytorch
  - distributed-training
  - deep-learning
aliases:
  - ray-train-torchtrainer
  - RTT
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Ray Train TorchTrainer

**Ray Train TorchTrainer** is a distributed training class from [[Ray Train Resource Allocation|Ray Train]] that automates data‑parallel fine‑tuning of PyTorch models across multiple GPUs. It handles worker management, device placement, wrapping the model in PyTorch’s `DistributedDataParallel` (DDP), distributed dataset sampling, and metric aggregation. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Overview

`TorchTrainer` runs a user‑defined `train_func` on each worker (one per GPU). Ray Train launches the workers, sets up the distributed process group, and provides utility functions such as `prepare_model` and `prepare_data_loader` to reduce boilerplate. The trainer is configured with a `ScalingConfig` that specifies the number of workers and whether to use GPU resources. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Key Components

### `train_func`

A Python function that contains the training loop for a single worker. It receives a `config` dictionary (passed via `train_loop_config`) and typically:

1. Loads the model and tokenizer.
2. Calls `prepare_model` to move the model to the worker's GPU and wrap it in DDP.
3. Loads the dataset and creates a `DataLoader`.
4. Calls `prepare_data_loader` to inject a distributed sampler and move batches to the GPU.
5. Runs the optimization loop, periodically calling `ray.train.report()` to log metrics. ^[distributed-training-with-ray-train-databricks-on-aws.md]

### `prepare_model`

`prepare_model` wraps the model in `torch.nn.parallel.DistributedDataParallel` (DDP) and places it on the correct GPU device for the current worker. This eliminates manual device management. ^[distributed-training-with-ray-train-databricks-on-aws.md]

### `prepare_data_loader`

`prepare_data_loader` adds a `DistributedSampler` to the data loader and ensures batches are moved to the worker's GPU. This distributes the dataset across workers without overlapping data. ^[distributed-training-with-ray-train-databricks-on-aws.md]

### `ScalingConfig`

The `ScalingConfig` defines the resource allocation for the training job. Key parameters include:

- `num_workers`: Number of parallel workers (typically equals the total number of GPUs).
- `use_gpu`: Whether to allocate GPU resources.

In the example, `num_workers` is set to `total_gpus` (discovered from the Ray cluster) and `use_gpu=True`. ^[distributed-training-with-ray-train-databricks-on-aws.md]

### `TorchTrainer`

The `TorchTrainer` constructor takes:
- The `train_func` to execute on each worker.
- `train_loop_config` – a dictionary of hyperparameters passed to `train_func`.
- `scaling_config` – a `ScalingConfig` object.
- Optionally, a `run_config` (e.g., for `storage_path` and experiment name). ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Usage Example

The following example (adapted from a Databricks workload) fine‑tunes a Qwen2.5‑3B model on 8 H100 GPUs using Ray Train's `TorchTrainer`. A workload YAML starts a Ray head with all GPUs, then runs the driver script. ^[distributed-training-with-ray-train-databricks-on-aws.md]

### Workload YAML (`train.yaml`)

```yaml
experiment_name: air-ray-train-distributed
environment:
  version: '4'
  dependencies:
    - ray[default,train]>=2.30
    - transformers>=4.45
    - datasets>=3.0
    - huggingface_hub>=0.34
    - fsspec>=2024.6.1
compute:
  num_accelerators: 8
  accelerator_type: GPU_8xH100
code_source:
  type: snapshot
  snapshot:
    root_path: .
command: |
  cd $CODE_SOURCE_PATH
  RAY_HEAD_PORT=6379
  GPUS_PER_NODE=${LOCAL_WORLD_SIZE:-8}
  if [ "${NODE_RANK:-0}" = "0" ]; then
    ray start --head --port=$RAY_HEAD_PORT --num-gpus="$GPUS_PER_NODE" --dashboard-host=0.0.0.0
    python train_ray.py
    ray stop
  else
    ...
  fi
```

The `command` starts a Ray head on node 0, runs the training script, and stops the cluster. It includes a branch for multi‑node scaling. ^[distributed-training-with-ray-train-databricks-on-aws.md]

### Driver Script (`train_ray.py`)

```python
def train_func(config: dict):
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.bfloat16)
    model.config.use_cache = False
    model = prepare_model(model)              # DDP wrap + device placement
    loader = DataLoader(dataset, batch_size=config["batch_size"], shuffle=True, drop_last=True)
    loader = prepare_data_loader(loader)      # distributed sampler + GPU transfer
    optimizer = torch.optim.AdamW(model.parameters(), lr=config["lr"])
    ...
    ray.train.report({"loss": out.loss.item(), "step": step})

def main():
    ray.init(address="auto")
    total_gpus = int(ray.cluster_resources().get("GPU", 0))
    trainer = TorchTrainer(
        train_func,
        train_loop_config={"lr": 2e-5, "batch_size": 4, "max_steps": 100},
        scaling_config=ScalingConfig(num_workers=total_gpus, use_gpu=True),
    )
    trainer.fit()
```

The script initializes Ray, discovers available GPUs, and creates a `TorchTrainer` that launches one worker per GPU. Metrics are reported via `ray.train.report` and optionally logged to MLflow. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Results and Logging

Metrics reported with `ray.train.report` are aggregated across workers and stored in the Ray Train result object. In the Databricks environment, the AI Runtime injects `MLFLOW_RUN_ID` and configures the tracking URI, so using `mlflow.log_metric` inside `train_func` (on rank 0) integrates with the MLflow experiment named in the YAML. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Related Concepts

- [[Ray Train Resource Allocation|Ray Train]] – The distributed training framework that provides `TorchTrainer`
- [[Distributed Data Parallel (DDP)]] – PyTorch's built‑in data parallelism strategy
- prepare_model – Utility function for DDP wrapping and device placement
- prepare_model and prepare_data_loader|prepare_data_loader – Utility function for distributed sampling and GPU transfer
- ScalingConfig – Configuration for worker resources in Ray Train
- MLflow Integration – Tracking distributed training metrics
- [[AI Runtime CLI]] – Databricks CLI for running Ray Train workloads

## Sources

- distributed-training-with-ray-train-databricks-on-aws.md
```

# Citations

1. [distributed-training-with-ray-train-databricks-on-aws.md](/references/distributed-training-with-ray-train-databricks-on-aws-05072d36.md)
