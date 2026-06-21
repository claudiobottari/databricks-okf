---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 050d1a2a7c855883c78cb73334ce2d64be5106b637eec59949dbec3159b5e36e
  pageDirectory: concepts
  sources:
    - deep-learning-databricks-on-aws.md
    - pytorch-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - pytorch-on-databricks
    - POD
  citations:
    - file: pytorch-databricks-on-aws.md
      start: 1
      end: 2
    - file: deep-learning-databricks-on-aws.md
      start: 1
      end: 2
title: PyTorch on Databricks
description: Using PyTorch within the Databricks environment for GPU-accelerated tensor computation and building deep learning networks, supporting both single-node and distributed training.
tags:
  - pytorch
  - deep-learning
  - databricks
timestamp: "2026-06-19T18:18:55.231Z"
---

# PyTorch on Databricks

**PyTorch on Databricks** provides a managed environment for building, training, and deploying deep learning models using the [PyTorch](https://pytorch.org/) framework. PyTorch is a Python package that delivers GPU‑accelerated tensor computation and high‑level building blocks for deep learning networks. ^[pytorch-databricks-on-aws.md:1-2]

---

## Availability

### Databricks Runtime ML

[Databricks Runtime for Machine Learning](https://docs.databricks.com/aws/en/machine-learning/) includes PyTorch pre‑installed. You can create a cluster and start using PyTorch immediately without additional package installation. For the specific version of PyTorch included in each Databricks Runtime ML release, see the release notes. ^[pytorch-databricks-on-aws.md:1-2]

### Databricks Runtime (Standard)

If you must use the standard Databricks Runtime instead of Databricks Runtime ML, you can install PyTorch as a [Databricks PyPI library](https://docs.databricks.com/aws/en/libraries/). Databricks recommends using Databricks Runtime ML to avoid manual installation and ensure compatibility. ^[pytorch-databricks-on-aws.md:1-2]

Example installation for PyTorch 1.5.0:

- On GPU clusters: install `torch==1.5.0` and `torchvision==0.6.0`
- On CPU clusters: use the corresponding CPU wheel files from the official PyTorch download repository ^[pytorch-databricks-on-aws.md:1-2]

---

## Single Node and Distributed Training

To test and migrate single‑machine PyTorch workflows, use a [Single Node cluster](https://docs.databricks.com/aws/en/compute/configure#single-node). ^[pytorch-databricks-on-aws.md:1-2]

For distributed training at scale, see [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) for options including Ray, TorchDistributor, and DeepSpeed. Because deep learning models are data and computation-intensive, distributed training can be important for many workloads. ^[deep-learning-databricks-on-aws.md:1-2, pytorch-databricks-on-aws.md:1-2]

---

## Using TorchDistributor

[TorchDistributor](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.torch.distributor.TorchDistributor.html) is the recommended approach for distributed PyTorch training on Databricks. It is available on Databricks Runtime ML 13.0 and above and resolves many common distributed training errors. ^[pytorch-databricks-on-aws.md:1-2]

```python
from pyspark.ml.torch.distributor import TorchDistributor

def train_fn(learning_rate):
    # ... training logic ...

num_processes = 2
distributor = TorchDistributor(num_processes=num_processes, local_mode=True)
distributor.run(train_fn, 1e-3)
```

^[pytorch-databricks-on-aws.md:1-2]

---

## GPU Acceleration

PyTorch provides GPU‑accelerated tensor computation on Databricks clusters with GPU workers. For serverless GPU workloads with AI Runtime, see [AI Runtime](/concepts/ai-runtime.md) for single and multi‑node deep learning. ^[pytorch-databricks-on-aws.md:1-2, deep-learning-databricks-on-aws.md:1-2]

---

## Tracking and Monitoring

Databricks uses [MLflow](/concepts/mlflow.md) to track deep learning training runs and model development. Tracking remains a cornerstone of the MLflow ecosystem and is especially vital for the iterative nature of deep learning. ^[deep-learning-databricks-on-aws.md:1-2]

For an end‑to‑end tutorial notebook using PyTorch and MLflow, see the MLflow 3 deep learning workflow. You can also use [TensorBoard](/concepts/tensorboard-on-databricks.md) for monitoring and debugging PyTorch models. ^[pytorch-databricks-on-aws.md:1-2, deep-learning-databricks-on-aws.md:1-2]

---

## Common Errors and Troubleshooting

### "process 0 terminated with exit code 1"

This error can occur when using notebooks in Databricks. To avoid it, use `torch.multiprocessing.start_processes` with `start_method="fork"` instead of `torch.multiprocessing.spawn`: ^[pytorch-databricks-on-aws.md:1-2]

```python
import torch

def train_fn(rank, learning_rate):
    # required setup, e.g. setup(rank)
    # ... training logic ...

num_processes = 2
torch.multiprocessing.start_processes(
    train_fn, args=(1e-3,), nprocs=num_processes, start_method="fork"
)
```

### "The server socket has failed to bind to port"

This error appears when restarting distributed training after interrupting a cell during training. To fix it, restart the cluster. If the problem persists, check your training function for errors. ^[pytorch-databricks-on-aws.md:1-2]

### CUDA Compatibility with `start_method="fork"`

Using `start_method="fork"` is not CUDA‑compatible. Any `.cuda()` commands called before `torch.multiprocessing.start_processes` may lead to failures. Add a check before starting distributed training: ^[pytorch-databricks-on-aws.md:1-2]

```python
if torch.cuda.is_initialized():
    raise Exception("CUDA was initialized; distributed training will fail.")
```

---

## License

PyTorch is distributed under the [BSD‑style license](https://github.com/pytorch/pytorch/blob/a90c259edad1ea4fa1b8773e3cb37240df680d62/LICENSE) found in the PyTorch GitHub repository. ^[pytorch-databricks-on-aws.md:1-2]

---

## Related Concepts

- [MLflow](/concepts/mlflow.md) — Tracking deep learning experiments
- [TensorBoard](/concepts/tensorboard-on-databricks.md) — Visualizing model training
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Scaling PyTorch across multiple nodes
- [AI Runtime](/concepts/ai-runtime.md) — Serverless GPU for deep learning
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The ML‑optimized runtime that includes PyTorch
- [Deep learning best practices on Databricks](/concepts/deep-learning-best-practices-on-databricks.md) — General guidance for deep learning workflows

## Sources

- pytorch-databricks-on-aws.md
- deep-learning-databricks-on-aws.md

# Citations

1. [pytorch-databricks-on-aws.md:1-2](/references/pytorch-databricks-on-aws-b092c491.md)
2. [deep-learning-databricks-on-aws.md:1-2](/references/deep-learning-databricks-on-aws-50a1d868.md)
