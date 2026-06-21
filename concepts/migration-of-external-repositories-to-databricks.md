---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 526e93dd0356bd9e43ce2237bda6f8b88f78943341e9f74b19c2dc876e374d41
  pageDirectory: concepts
  sources:
    - distributed-training-with-torchdistributor-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - migration-of-external-repositories-to-databricks
    - MOERTD
  citations:
    - file: distributed-training-with-torchdistributor-databricks-on-aws.md
title: Migration of External Repositories to Databricks
description: Process for importing external distributed training repositories as Databricks Git folders and launching them via TorchDistributor.
tags:
  - migration
  - databricks
  - git
timestamp: "2026-06-19T10:19:45.053Z"
---

# Migration of External Repositories to Databricks

**Migration of External Repositories to Databricks** refers to the process of taking an existing distributed training codebase stored in an external repository (e.g., GitHub, Bitbucket) and adapting it to run on Databricks clusters. This approach leverages [TorchDistributor](/concepts/torchdistributor.md) to launch distributed PyTorch training jobs directly from within a Databricks Notebook, without requiring significant refactoring.

## Steps to Migrate

The migration procedure consists of three main steps: ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

1. **Import the external repository as a [Databricks Git folder](/concepts/databricks-git-folders-for-cicd.md)**. This makes the repository content available within the workspace, preserving its file structure and version history. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

2. **Create a new Databricks Notebook** inside the imported repository folder. This notebook will serve as the launch point for the training job. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

3. **Launch distributed training** by calling `TorchDistributor.run()` with the path to the training script and any command-line arguments the script expects. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Example

The following code demonstrates how to use TorchDistributor to run a training script from an imported repository: ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

```python
from pyspark.ml.torch.distributor import TorchDistributor

train_file = "/path/to/train.py"
args = ["--learning_rate=0.001", "--batch_size=16"]

distributor = TorchDistributor(num_processes=2, local_mode=False, use_gpu=True)
distributor.run(train_file, *args)
```

TorchDistributor initializes the environment and communication channels between workers, then uses the `torch.distributed.run` CLI command under the hood to execute the training job across worker nodes. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Requirements

- Spark 3.4
- Databricks Runtime 13.0 ML or above ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Troubleshooting Common Errors

When migrating external repositories, users may encounter errors related to network communication or GPU peer access. The source material documents the following fixes:

| Error | Resolution |
|-------|------------|
| CUDA: `peer access is not supported between these two devices` (common on AWS G5 GPU instances) | Set `os.environ["NCCL_P2P_DISABLE"] = "1"` in the training code. ^[distributed-training-with-torchdistributor-databricks-on-aws.md] |
| NCCL: `ncclInternalError: Internal check failed.` (multi-node network communication) | Set `os.environ["NCCL_SOCKET_IFNAME"] = "eth0"`. ^[distributed-training-with-torchdistributor-databricks-on-aws.md] |
| Gloo: `RuntimeError: Connection refused` (CPU distributed training) | Set `os.environ["GLOO_SOCKET_IFNAME"] = "eth0"`. ^[distributed-training-with-torchdistributor-databricks-on-aws.md] |

## Best Practices for External Code

If the existing training code uses imports that are only available at the notebook top level, those imports may fail when distributed to executors. To avoid pickling errors, place all necessary `import` statements **inside** the training function that is passed to `TorchDistributor.run()`, as well as inside any other user-defined functions called during training. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Related Concepts

- [TorchDistributor](/concepts/torchdistributor.md) – The PySpark module used to launch distributed PyTorch training.
- [Databricks Git folders](/concepts/databricks-git-folders-for-cicd.md) – The mechanism for importing external repositories into the workspace.
- Distributed Training with PyTorch – General concepts for multi-GPU training.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – The required ML runtime version.
- [PyTorch Distributed Data Parallel](/concepts/distributed-data-parallel-ddp.md) – The underlying parallelism strategy.

## Sources

- distributed-training-with-torchdistributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-torchdistributor-databricks-on-aws.md](/references/distributed-training-with-torchdistributor-databricks-on-aws-8705ab32.md)
