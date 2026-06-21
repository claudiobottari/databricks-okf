---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0b709b920cf416d816aaf62a4129199f4eeacba98b3f36002c904548714d457a
  pageDirectory: concepts
  sources:
    - distributed-training-with-ray-train-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prepare_model-and-prepare_data_loader-in-ray-train
    - prepare_data_loader in Ray Train and prepare_model
    - PAPIRT
  citations:
    - file: distributed-training-with-ray-train-databricks-on-aws.md
title: prepare_model and prepare_data_loader in Ray Train
description: Ray Train utility functions that handle DDP wrapping, GPU device placement, and distributed dataset sampling for PyTorch training workflows.
tags:
  - ray
  - distributed-training
  - pytorch
timestamp: "2026-06-19T10:19:21.090Z"
---

# prepare_model and prepare_data_loader in Ray Train

**`prepare_model` and `prepare_data_loader`** are utility functions from the [Ray Train](/concepts/ray-train-resource-allocation.md) library (`ray.train.torch`) that simplify distributed data-parallel training. `prepare_model` wraps a PyTorch model in `DistributedDataParallel` (DDP) and moves it to the correct GPU device for the current worker. `prepare_data_loader` injects a `DistributedSampler` and configures automatic batch transfer to the GPU. ^[distributed-training-with-ray-train-databricks-on-aws.md]

Together, these two functions eliminate the boilerplate code that developers would otherwise need to write for distributed training: device placement, DDP wrapping, sharding the dataset across workers, and moving batches to the accelerator. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## `prepare_model`

`prepare_model` takes a standard PyTorch model and:

1. Moves the model to the GPU assigned to the current Ray Train worker.
2. Wraps the model in `torch.nn.parallel.DistributedDataParallel` (DDP), enabling gradient synchronization across workers during backpropagation.
3. Returns the prepared model, which can then be used in the training loop without any additional distributed logic. ^[distributed-training-with-ray-train-databricks-on-aws.md]

```python
from ray.train.torch import prepare_model

model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.bfloat16)
model = prepare_model(model)  # DDP wrap + device placement
```

^[distributed-training-with-ray-train-databricks-on-aws.md]

## `prepare_data_loader`

`prepare_data_loader` takes a standard PyTorch `DataLoader` and:

1. Injects a `DistributedSampler` so that each worker processes a distinct subset of the dataset, avoiding redundant computation.
2. Configures automatic batch transfer to the GPU, so individual `.to(device)` calls are no longer needed.
3. Returns the prepared data loader ready for iteration. ^[distributed-training-with-ray-train-databricks-on-aws.md]

```python
from ray.train.torch import prepare_data_loader

loader = DataLoader(dataset, batch_size=config["batch_size"], shuffle=True, drop_last=True)
loader = prepare_data_loader(loader)  # distributed sampler + GPU transfer
```

^[distributed-training-with-ray-train-databricks-on-aws.md]

## Typical Usage Pattern

Both functions are called inside the training function that runs on every worker. The typical sequence is:

1. Load the model.
2. Call `prepare_model` to wrap it in DDP and place it on the correct GPU.
3. Create a standard `DataLoader`.
4. Call `prepare_data_loader` to add a distributed sampler and GPU transfer.
5. Iterate over the prepared loader in the training loop. ^[distributed-training-with-ray-train-databricks-on-aws.md]

```python
def train_func(config: dict):
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.bfloat16)
    model.config.use_cache = False
    model = prepare_model(model)  # DDP wrap + device placement

    loader = DataLoader(dataset, batch_size=config["batch_size"], shuffle=True, drop_last=True)
    loader = prepare_data_loader(loader)  # distributed sampler + GPU transfer

    optimizer = torch.optim.AdamW(model.parameters(), lr=config["lr"])
    ...
    ray.train.report({"loss": out.loss.item(), "step": step})
```

^[distributed-training-with-ray-train-databricks-on-aws.md]

## Relationship to TorchTrainer

`prepare_model` and `prepare_data_loader` are designed to be used with the [TorchTrainer](/concepts/ray-train-torchtrainer.md) class in Ray Train. The `TorchTrainer` launches one worker per GPU according to the `ScalingConfig`, and each worker executes the training function independently. The `prepare_*` functions handle the per-worker distributed setup transparently. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Related Concepts

- [Ray Train](/concepts/ray-train-resource-allocation.md) — The distributed training framework providing these utilities
- [TorchTrainer](/concepts/ray-train-torchtrainer.md) — The Ray Train class that launches distributed PyTorch training
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — The broader practice of training models across multiple GPUs or nodes
- [DistributedDataParallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — The PyTorch parallelism strategy that `prepare_model` configures
- DistributedSampler — The PyTorch sampler that `prepare_data_loader` injects for per-worker data sharding
- [Multi-node LLM fine-tuning with FSDP](/concepts/multi-node-llm-fine-tuning-with-fsdp.md) — An alternative parallelism strategy for distributed training
- ScalingConfig — Ray Train configuration for specifying the number of workers and GPU usage

## Sources

- distributed-training-with-ray-train-databricks-on-aws.md

# Citations

1. [distributed-training-with-ray-train-databricks-on-aws.md](/references/distributed-training-with-ray-train-databricks-on-aws-05072d36.md)
