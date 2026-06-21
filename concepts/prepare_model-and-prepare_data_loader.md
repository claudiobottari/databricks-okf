---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 73e7257552a04add1cd4761d184da473676123b7d5d1d70cc69e5452c89787c3
  pageDirectory: concepts
  sources:
    - distributed-training-with-ray-train-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prepare_model-and-prepare_data_loader
    - prepare_data_loader and prepare_model
    - PAP
    - prepare_data_loader
  citations:
    - file: distributed-training-with-ray-train-databricks-on-aws.md
title: prepare_model and prepare_data_loader
description: Ray Train utility functions that automatically wrap a PyTorch model in DDP (Distributed Data Parallel), move it to the correct device, and inject a DistributedSampler into DataLoaders for sharded training.
tags:
  - pytorch
  - distributed-training
  - ray
timestamp: "2026-06-19T18:37:59.676Z"
---

```yaml
---
title: prepare_model and prepare_data_loader
summary: Two utility functions from `ray.train.torch` that wrap a PyTorch model in Distributed Data Parallel (DDP) and configure a DataLoader with a distributed sampler and automatic GPU transfer for distributed training.
sources:
  - distributed-training-with-ray-train-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:08:11.292Z"
updatedAt: "2026-06-18T08:08:11.292Z"
tags:
  - ray
  - distributed-training
  - pytorch
  - ddp
  - data-loading
aliases:
  - prepare_model
  - prepare_data_loader
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# prepare_model and prepare_data_loader

**`prepare_model`** and **`prepare_data_loader`** are utility functions from the `ray.train.torch` module that simplify converting a standard PyTorch model and data loader for distributed multi‑GPU training. They are typically used inside a [[Ray Train Resource Allocation|Ray Train]] training function to handle Distributed Data Parallel (DDP) wrapping, device placement, and distributed data sampling automatically. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## prepare_model

`prepare_model` moves the model to the current worker’s GPU and wraps it in [[Distributed Data Parallel (DDP)]]. After calling this function, the model is ready for gradient synchronization across workers. ^[distributed-training-with-ray-train-databricks-on-aws.md]

```python
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.bfloat16)
model = prepare_model(model)
```

## prepare_data_loader

`prepare_data_loader` adds a DistributedSampler to the data loader and ensures that batches are automatically moved to the worker’s GPU. This guarantees that each worker processes a unique subset of the data per epoch. ^[distributed-training-with-ray-train-databricks-on-aws.md]

```python
loader = DataLoader(dataset, batch_size=config["batch_size"], shuffle=True, drop_last=True)
loader = prepare_data_loader(loader)
```

## Usage in a Ray Train Training Function

Both functions are called inside the training function that executes on every Ray Train worker (one per GPU). The following pattern is typical: ^[distributed-training-with-ray-train-databricks-on-aws.md]

```python
def train_func(config: dict):
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.bfloat16)
    model.config.use_cache = False
    model = prepare_model(model)              # DDP wrap + device placement

    loader = DataLoader(dataset, batch_size=config["batch_size"], shuffle=True, drop_last=True)
    loader = prepare_data_loader(loader)      # distributed sampler + GPU transfer

    optimizer = torch.optim.AdamW(model.parameters(), lr=config["lr"])
    # training loop...
```

After preparation, the training loop remains unchanged from a single‑GPU script.

## Related Concepts

- [[Ray Train Resource Allocation|Ray Train]] – The distributed training framework that provides these utilities.
- [[Ray Train TorchTrainer|TorchTrainer]] – The Ray Train trainer class that launches workers and coordinates DDP.
- [[Distributed Data Parallel (DDP)]] – The PyTorch backend used for gradient synchronization.
- DistributedSampler – The PyTorch sampler that shards the dataset across workers.
- ScalingConfig – Ray Train configuration for setting the number of workers and GPU usage.
- Multi-Node Training – Scaling these patterns across multiple nodes.

## Sources

- distributed-training-with-ray-train-databricks-on-aws.md
```

# Citations

1. [distributed-training-with-ray-train-databricks-on-aws.md](/references/distributed-training-with-ray-train-databricks-on-aws-05072d36.md)
