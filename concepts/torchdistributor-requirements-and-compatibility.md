---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 824a9c219b60a96438b8b514356f2e3505d77a85abf8cb62c274e016d7331df8
  pageDirectory: concepts
  sources:
    - distributed-training-with-torchdistributor-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - torchdistributor-requirements-and-compatibility
    - Compatibility and TorchDistributor Requirements
    - TRAC
  citations:
    - file: distributed-training-with-torchdistributor-databricks-on-aws.md
title: TorchDistributor Requirements and Compatibility
description: TorchDistributor requires Spark 3.4 and Databricks Runtime 13.0 ML or above for compatibility.
tags:
  - requirements
  - compatibility
  - databricks
timestamp: "2026-06-18T12:09:31.258Z"
---

# TorchDistributor Requirements and Compatibility

**TorchDistributor** is an open-source module in PySpark that enables distributed training of PyTorch models on Spark clusters. It initializes communication channels between workers and uses the CLI command `torch.distributed.run` to run distributed training across worker nodes.^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Requirements

TorchDistributor has the following minimum requirements:^[distributed-training-with-torchdistributor-databricks-on-aws.md]

- **Spark 3.4**
- **Databricks Runtime 13.0 ML** or above

These requirements ensure that the necessary PySpark and environment dependencies are available for distributed execution.

## Compatibility

TorchDistributor is compatible with:

- **PyTorch** and **PyTorch Lightning** — any single-node training code written in these frameworks can be converted for distributed training by wrapping it in a training function passed to `TorchDistributor.run()`.^[distributed-training-with-torchdistributor-databricks-on-aws.md]
- **HuggingFace Trainer API** — TorchDistributor can launch distributed fine-tuning of Hugging Face models.^[distributed-training-with-torchdistributor-databricks-on-aws.md]
- **GPU and CPU clusters** — The `use_gpu` parameter controls whether NCCL (GPU) or Gloo (CPU) backend is used for communication.^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Network and Hardware Considerations

When running on specific hardware or network configurations, environment variable adjustments may be required for successful distributed communication:

| Symptom | Cause | Workaround |
|---------|-------|------------|
| CUDA `peer access is not supported between these two devices` | Common on G5 GPU instances on AWS | Set `NCCL_P2P_DISABLE=1` in the training code.^[distributed-training-with-torchdistributor-databricks-on-aws.md] |
| NCCL `ncclInternalError: Internal check failed` | NCCL cannot use the correct network interface for GPU communication (multi-node) | Set `NCCL_SOCKET_IFNAME=eth0`.^[distributed-training-with-torchdistributor-databricks-on-aws.md] |
| Gloo `RuntimeError: Connection refused` | Gloo backend cannot bind to the correct network interface on CPU clusters | Set `GLOO_SOCKET_IFNAME=eth0`.^[distributed-training-with-torchdistributor-databricks-on-aws.md] |

## Troubleshooting Common Issues

### Pickling / Import Errors

When using TorchDistributor from a notebook, library imports (e.g., `import torch`) that are defined only at the notebook's top level may not be available on worker executors. To avoid this, place all required import statements **both** at the top of the training function passed to `.run()` and inside any other user-defined functions called by the training method.^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Related Concepts

- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- PyTorch Distributed
- Spark ML
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md)
- NCCL and Gloo backends

## Sources

- distributed-training-with-torchdistributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-torchdistributor-databricks-on-aws.md](/references/distributed-training-with-torchdistributor-databricks-on-aws-8705ab32.md)
