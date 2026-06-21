---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5178c93097f23699e0c63029e408c70b6e8ce9d9d6dede744e0e46c423ae8d1b
  pageDirectory: concepts
  sources:
    - distributed-training-with-torchdistributor-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - migration-from-external-repositories-to-databricks
    - MFERTD
  citations:
    - file: distributed-training-with-torchdistributor-databricks-on-aws.md
title: Migration from External Repositories to Databricks
description: Process of importing existing distributed training code from external repos into Databricks Git folders and launching it with TorchDistributor
tags:
  - migration
  - databricks
  - git
timestamp: "2026-06-19T18:39:09.546Z"
---

Here is the wiki page for "Migration from External Repositories to Databricks".

## Migration from External Repositories to Databricks

**Migration from External Repositories to Databricks** describes the process of moving an existing distributed training codebase—typically stored in a remote Git repository—into the Databricks environment and running it as a managed [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) job using [TorchDistributor](/concepts/torchdistributor.md). This workflow is designed for users who already have a working training script written with PyTorch or [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) and want to leverage Databricks for scalable execution.

### Overview

If you maintain an existing distributed training procedure in an external repository (e.g., GitHub, GitLab, or Bitbucket), you can migrate it to Databricks with minimal refactoring. The migration involves three steps: importing the repository as a Git folder, creating a Databricks Notebook inside that repository, and launching the training job via `TorchDistributor`. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Migration Steps

1.  **Import the repository** – Use the [Databricks Repos (Git Folders)](/concepts/databricks-git-folders-for-cicd.md) feature to import the external repository. This makes the source code files (including the training script) available within the Databricks workspace as a Git folder.
2.  **Create a new notebook** – Create a new Databricks Notebook inside the repository folder. This notebook will serve as the entry point for launching distributed training.
3.  **Launch distributed training** – In a single cell of the notebook, instantiate `TorchDistributor` and call its `.run()` method, passing the path to the training script and any command-line arguments.

### Example

The following code snippet demonstrates the minimal migration pattern. After importing the repository and creating a notebook, you add this cell:

```python
from pyspark.ml.torch.distributor import TorchDistributor

train_file = "/path/to/train.py"
args = ["--learning_rate=0.001", "--batch_size=16"]

distributor = TorchDistributor(
    num_processes=2,
    local_mode=False,
    use_gpu=True
)
distributor.run(train_file, *args)
```

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Key Considerations

- **Training script location** – The `train_file` path is relative to the repository inside the Databricks workspace. The script must already be converted to use [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) or a similar distributed paradigm, and it must contain all required import statements (e.g., `import torch`) inside the training function to avoid pickling errors. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]
- **Environment requirements** – The migration requires **Spark 3.4** and **Databricks Runtime 13.0 ML or above**. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]
- **GPU vs. CPU** – The `use_gpu` parameter controls the backend. When `use_gpu=True`, the backend defaults to `"nccl"`; when `False`, the backend uses `"gloo"`. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Common Issues

- **CUDA peer access error** – On AWS G5 GPU instances, add `os.environ["NCCL_P2P_DISABLE"] = "1"` to disable peer-to-peer access between GPUs. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]
- **NCCL internal check failure** – Add `os.environ["NCCL_SOCKET_IFNAME"] = "eth0"` to force NCCL to use the primary network interface. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]
- **Gloo connection refused** – Add `os.environ["GLOO_SOCKET_IFNAME"] = "eth0"` when running distributed training on CPU instances. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Related Concepts

- [TorchDistributor](/concepts/torchdistributor.md) – The primary API for launching distributed training from a notebook.
- [Databricks Repos (Git Folders)](/concepts/databricks-git-folders-for-cicd.md) – The mechanism for importing external repositories.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – The standard PyTorch parallelism strategy used by TorchDistributor.
- NCCL – The NVIDIA Collective Communications Library used for GPU communication.
- Gloo – The CPU-based distributed communication backend.

### Sources

- distributed-training-with-torchdistributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-torchdistributor-databricks-on-aws.md](/references/distributed-training-with-torchdistributor-databricks-on-aws-8705ab32.md)
