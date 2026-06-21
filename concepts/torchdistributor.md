---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3f0f22065725d7b31b2d4b326e7b59c3cc65d696357293b43e392ce493faba46
  pageDirectory: concepts
  sources:
    - distributed-training-databricks-on-aws.md
    - distributed-training-with-torchdistributor-databricks-on-aws.md
    - horovod-databricks-on-aws.md
    - horovodrunner-examples-databricks-on-aws.md
    - horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md
    - multi-gpu-workload-databricks-on-aws.md
    - pytorch-databricks-on-aws.md
    - train-recommender-models-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - torchdistributor
    - Torch Distributed
    - TorchDistributor API
    - torch.distributed.run
    - NCCL Errors with TorchDistributor
    - Spark PyTorch Distributor
  citations:
    - file: distributed-training-databricks-on-aws.md
    - file: distributed-training-with-torchdistributor-databricks-on-aws.md
    - file: horovod-databricks-on-aws.md
    - file: horovodrunner-examples-databricks-on-aws.md
    - file: horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md
    - file: train-recommender-models-databricks-on-aws.md
    - file: pytorch-databricks-on-aws.md
title: TorchDistributor
description: An open-source PySpark module that enables distributed PyTorch training on Spark clusters by initializing environment and communication channels via torch.distributed.run.
tags:
  - pytorch
  - spark
  - distributed-training
timestamp: "2026-06-19T18:34:09.303Z"
---

# TorchDistributor

**TorchDistributor** is an open‑source module in PySpark that enables distributed training of PyTorch models on Apache Spark clusters. It launches PyTorch training jobs as Spark jobs by initialising the environment and communication channels between workers and using the `torch.distributed.run` CLI command to execute training across worker nodes. ^[distributed-training-databricks-on-aws.md, distributed-training-with-torchdistributor-databricks-on-aws.md]

Databricks recommends TorchDistributor for distributed deep learning with PyTorch. It is the preferred alternative to the deprecated [Horovod](/concepts/horovod.md) and HorovodRunner packages in Databricks Runtime ML releases after 15.4 LTS ML. ^[horovod-databricks-on-aws.md, horovodrunner-examples-databricks-on-aws.md, horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Overview

TorchDistributor is part of the `pyspark.ml.torch.distributor` package and works with standard [PyTorch Distributed Data Parallel](/concepts/distributed-data-parallel-ddp.md) (DDP) distributed training frameworks. It abstracts the complexity of setting up process groups and synchronising gradients across multiple GPUs or nodes. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

The [DeepSpeed Distributor](/concepts/deepspeed-distributor.md) is built on top of TorchDistributor and adds optimised memory usage, reduced communication overhead, and advanced pipeline parallelism for large models. ^[distributed-training-databricks-on-aws.md]

TorchDistributor is used in production‑scale recommender system training on Databricks, such as two‑tower and DLRM models, where it orchestrates distributed training across multiple GPUs alongside tools like [MLflow](/concepts/mlflow.md), TorchRec, and Mosaic StreamingDataset. ^[train-recommender-models-databricks-on-aws.md]

## Requirements

- Spark 3.4
- Databricks Runtime 13.0 ML or above
- A multi-node cluster or single-node cluster with GPU support (if `use_gpu=True`) ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Usage

### Notebook Workflow

1. **Prepare single‑node code** – Develop and test the training logic with PyTorch, [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md), or the Hugging Face Trainer API.
2. **Convert to standard distributed training** – Adapt the code to use `torch.distributed` primitives (e.g., [DistributedDataParallel](/concepts/distributed-data-parallel-ddp.md)) and wrap everything in a single training function.
3. **Move imports inside the training function** – Place all import statements (e.g., `import torch`) inside the function to avoid pickling errors when distributing across executors. The `device_id` is obtained from `os.environ["LOCAL_RANK"]`.
4. **Launch training** – Instantiate `TorchDistributor` with desired parameters and call `.run(*args)`.

```python
from pyspark.ml.torch.distributor import TorchDistributor

def train(learning_rate, use_gpu):
    import torch
    import torch.distributed as dist
    import torch.nn.parallel.DistributedDataParallel as DDP
    from torch.utils.data import DistributedSampler, DataLoader

    backend = "nccl" if use_gpu else "gloo"
    dist.init_process_group(backend)
    device = int(os.environ["LOCAL_RANK"]) if use_gpu else "cpu"
    model = DDP(createModel(), **kwargs)
    sampler = DistributedSampler(dataset)
    loader = DataLoader(dataset, sampler=sampler)
    output = train(model, loader, learning_rate)
    dist.cleanup()
    return output

distributor = TorchDistributor(num_processes=2, local_mode=False, use_gpu=True)
distributor.run(train, 1e-3, True)
```

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Migrating Training from External Repositories

1. Import the external repository as a [Databricks Git folder](/concepts/databricks-git-folders-for-cicd.md).
2. Create a new notebook inside that repository.
3. Call `TorchDistributor.run()` with the path to the training script and command‑line arguments:

```python
train_file = "/path/to/train.py"
args = ["--learning_rate=0.001", "--batch_size=16"]
distributor = TorchDistributor(num_processes=2, local_mode=False, use_gpu=True)
distributor.run(train_file, *args)
```

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| `process 0 terminated with exit code 1` | Pickling errors from imports not available on executors, or CUDA initialisation conflicts. | Move all imports inside the training function; use `torch.multiprocessing.start_processes` with `start_method='fork'` as a fallback. ^[distributed-training-with-torchdistributor-databricks-on-aws.md, pytorch-databricks-on-aws.md] |
| `CUDA failure: peer access is not supported` | GPU peer‑to‑peer communication unavailable (common on AWS G5 instances). | Set `os.environ["NCCL_P2P_DISABLE"] = "1"` in training code. ^[distributed-training-with-torchdistributor-databricks-on-aws.md] |
| `ncclInternalError: Internal check failed` | NCCL cannot use the default network interface for GPU communication. | Set `os.environ["NCCL_SOCKET_IFNAME"] = "eth0"`. ^[distributed-training-with-torchdistributor-databricks-on-aws.md] |
| `RuntimeError: Connection refused` (Gloo) | Gloo process group fails on CPU instances. | Set `os.environ["GLOO_SOCKET_IFNAME"] = "eth0"`. ^[distributed-training-with-torchdistributor-databricks-on-aws.md] |
| `The server socket has failed to bind to port` | Port conflict after interrupting a training cell. | Restart the cluster. ^[pytorch-databricks-on-aws.md] |

## Example Notebooks

- End‑to‑end distributed training on Databricks
- Distributed fine‑tuning of a Hugging Face model
- Distributed training on a PyTorch file
- Distributed training using PyTorch Lightning
- Two‑tower recommender model training
- DLRM recommender model training

^[distributed-training-with-torchdistributor-databricks-on-aws.md, train-recommender-models-databricks-on-aws.md]

## Related Concepts

- [PyTorch Distributed Data Parallel](/concepts/distributed-data-parallel-ddp.md)
- [DeepSpeed Distributor](/concepts/deepspeed-distributor.md)
- [Horovod](/concepts/horovod.md) (deprecated)
- [Distributed training](/concepts/workload-yaml-for-distributed-training.md)
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md)
- TorchRec
- [MLflow](/concepts/mlflow.md)
- [Single Node cluster](/concepts/single-node-clusters-for-pytorch.md)

## Sources

- distributed-training-databricks-on-aws.md
- distributed-training-with-torchdistributor-databricks-on-aws.md
- horovod-databricks-on-aws.md
- horovodrunner-examples-databricks-on-aws.md
- horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md
- multi-gpu-workload-databricks-on-aws.md
- pytorch-databricks-on-aws.md
- train-recommender-models-databricks-on-aws.md

# Citations

1. [distributed-training-databricks-on-aws.md](/references/distributed-training-databricks-on-aws-826bf389.md)
2. [distributed-training-with-torchdistributor-databricks-on-aws.md](/references/distributed-training-with-torchdistributor-databricks-on-aws-8705ab32.md)
3. [horovod-databricks-on-aws.md](/references/horovod-databricks-on-aws-49662285.md)
4. [horovodrunner-examples-databricks-on-aws.md](/references/horovodrunner-examples-databricks-on-aws-de1151e3.md)
5. [horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md](/references/horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws-513310cf.md)
6. [train-recommender-models-databricks-on-aws.md](/references/train-recommender-models-databricks-on-aws-b4714239.md)
7. [pytorch-databricks-on-aws.md](/references/pytorch-databricks-on-aws-b092c491.md)
