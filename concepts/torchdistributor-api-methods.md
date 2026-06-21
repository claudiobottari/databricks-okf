---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6aea1d968d5a13a883787190a3135a6b78d2e08fb5660caa72ff400e6e940a4e
  pageDirectory: concepts
  sources:
    - distributed-training-with-torchdistributor-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - torchdistributor-api-methods
    - TAM
    - TorchDistributor API
  citations:
    - file: distributed-training-with-torchdistributor-databricks-on-aws.md
title: TorchDistributor API Methods
description: The supported API methods for TorchDistributor, enabling launching PyTorch training as Spark jobs with parameters like num_processes, local_mode, and use_gpu
tags:
  - spark
  - pytorch
  - api
  - distributed-training
timestamp: "2026-06-18T15:35:08.751Z"
---

# TorchDistributor API Methods

The **TorchDistributor API Methods** refer to the constructor and runtime methods of the `TorchDistributor` class, an open-source module in PySpark (available from Spark 3.4) that enables distributed training of PyTorch models on Spark clusters. The API initializes the environment and communication channels between workers and uses the CLI command `torch.distributed.run` under the hood. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Requirements

- Spark 3.4
- Databricks Runtime 13.0 ML or above ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Constructor

The `TorchDistributor` constructor accepts the following parameters (shown in code examples in the source documentation):

- `num_processes` – Number of worker processes to launch.
- `local_mode` – Boolean; when `True` training runs on a single node, when `False` it runs across multiple nodes.
- `use_gpu` – Boolean indicating whether to use GPU (sets the NCCL backend) or CPU (sets the Gloo backend). ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

```python
from pyspark.ml.torch.distributor import TorchDistributor

distributor = TorchDistributor(num_processes=2, local_mode=False, use_gpu=True)
```

## `run()` Method

The `run()` method launches distributed training. It supports two calling conventions:

### 1. Running a Python function

```python
distributor.run(train, 1e-3, True)
```

The function `train` must contain all necessary imports (e.g., `import torch`) inside its body to avoid pickling errors, and the `device` should be determined by `int(os.environ["LOCAL_RANK"])` for GPU. The function receives the positional arguments passed to `run()`. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### 2. Running a training script file

```python
train_file = "/path/to/train.py"
args = ["--learning_rate=0.001", "--batch_size=16"]
distributor.run(train_file, *args)
```

The training script is invoked as a subprocess with `torch.distributed.run`. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Troubleshooting Common Errors

### CUDA peer access failure

On G5 GPU instances on AWS, adding `os.environ["NCCL_P2P_DISABLE"] = "1"` resolves the error. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### NCCL internal check failure

For multi‑node training, setting `os.environ["NCCL_SOCKET_IFNAME"] = "eth0"` forces NCCL to use the primary network interface. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Gloo connection refused

When using Gloo for CPU distributed training, set `os.environ["GLOO_SOCKET_IFNAME"] = "eth0"`. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Related Concepts

- [PyTorch Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- Spark Cluster
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- NCCL Communication Library
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)

## Sources

- distributed-training-with-torchdistributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-torchdistributor-databricks-on-aws.md](/references/distributed-training-with-torchdistributor-databricks-on-aws-8705ab32.md)
