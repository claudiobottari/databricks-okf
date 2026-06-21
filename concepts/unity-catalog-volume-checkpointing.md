---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 418e046b7535b38295564a2f8a1ffce467ff885c36ca87f2e05491003f4af8a3
  pageDirectory: concepts
  sources:
    - experiment-tracking-and-observability-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-volume-checkpointing
    - UCVC
  citations:
    - file: experiment-tracking-and-observability-databricks-on-aws.md
title: Unity Catalog Volume Checkpointing
description: Save and load model checkpoints asynchronously to Unity Catalog volumes using UCVolumeWriter and UCVolumeReader with Torch Distributed Checkpoint API, optimized with NVMe-backed local staging.
tags:
  - distributed-training
  - checkpointing
  - unity-catalog
timestamp: "2026-06-19T10:26:12.351Z"
---

```markdown
---
title: Unity Catalog Volume Checkpointing
summary: Efficient model checkpointing to Unity Catalog volumes using UCVolumeWriter, UCVolumeReader, and Torch Distributed Checkpoint with asynchronous save support.
sources:
  - experiment-tracking-and-observability-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:14:57.178Z"
updatedAt: "2026-06-18T12:14:57.178Z"
tags:
  - distributed-training
  - checkpointing
  - unity-catalog
  - deep-learning
aliases:
  - unity-catalog-volume-checkpointing
  - UCVC
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

## Unity Catalog Volume Checkpointing

**Unity Catalog Volume Checkpointing** refers to the practice of saving and loading model checkpoints to and from Unity Catalog Volumes during distributed training on [[AI Runtime]]. This approach leverages the governance and lineage capabilities of Unity Catalog while providing a fast, asynchronous I/O path optimized for GPU workloads.^[experiment-tracking-and-observability-databricks-on-aws.md]

### Overview

For distributed training workloads, checkpoints are saved and loaded asynchronously using Unity Catalog volumes. These volumes provide the same access control, auditing, and metadata management as other Unity Catalog objects, enabling teams to treat checkpoints as governed assets. The recommended APIs are `UCVolumeWriter` and `UCVolumeReader` from the `serverless_gpu.data` package, used together with the [[PyTorch Distributed Checkpoint (DCP)|Torch Distributed Checkpoint]] (DCP) API.^[experiment-tracking-and-observability-databricks-on-aws.md]

The storage backends stage all I/O through a fast local temporary directory (`/tmp`, which is NVMe-backed on serverless GPU nodes) and upload to (or download from) the Unity Catalog volume asynchronously. This design is significantly faster than writing checkpoint shards directly to the volume’s FUSE mount. Metadata atomicity is preserved: the writer publishes the `.metadata` file only after all data shards have finished uploading.^[experiment-tracking-and-observability-databricks-on-aws.md]

### Requirements

`UCVolumeWriter`, `UCVolumeReader`, and `UCVolumeDataset` require GPU environment 5 or above (Serverless GPU Python API version 0.5.16 or later).^[experiment-tracking-and-observability-databricks-on-aws.md]

### Usage

#### Basic Checkpoint Save and Load

```python
import torch.distributed.checkpoint as dcp
from serverless_gpu.data import UCVolumeWriter, UCVolumeReader

checkpoint_path = "/Volumes/my_catalog/my_schema/model/checkpoints"

# Save
writer = UCVolumeWriter(checkpoint_path)
dcp.save(state_dict, storage_writer=writer)

# Load
reader = UCVolumeReader(checkpoint_path)
dcp.load(state_dict, storage_reader=reader)
```

^[experiment-tracking-and-observability-databricks-on-aws.md]

#### Asynchronous Save (Background Upload)

To continue training while the checkpoint is being uploaded, use `dcp.async_save` with a `UCVolumeWriter`. Asynchronous saves require a CPU backend on the process group:

```python
torch.distributed.init_process_group(backend="cpu:gloo,cuda:nccl", ...)

writer = UCVolumeWriter(checkpoint_path)
future = dcp.async_save(state_dict, storage_writer=writer)
# ... continue training ...
future.result()  # blocks until upload completes
```

^[experiment-tracking-and-observability-databricks-on-aws.md]

#### Data Pipeline Checkpointing Note

A model checkpoint captures only the model and optimizer state, not the position of the data pipeline within the dataset. When resuming from a checkpoint, you must account for this separately—for example, by restarting from an epoch boundary or by tracking processed samples or shards in your own training state so they can be skipped on resume.^[experiment-tracking-and-observability-databricks-on-aws.md]

### Frequency Recommendations

Checkpoint often enough to limit lost work after an interruption, but not so often that I/O overhead slows training. Databricks recommends aiming for one checkpoint every 30 minutes to an hour, and tuning the interval based on your step time and checkpoint size.^[experiment-tracking-and-observability-databricks-on-aws.md]

### Related Concepts

- [[Unity Catalog]] – The data governance platform providing volumes and access controls.
- Unity Catalog Volumes – The storage objects used for checkpoint files.
- [[AI Runtime]] – The Databricks runtime for GPU-accelerated workloads.
- [[MLflow]] – Experiment tracking and model registry, often used alongside checkpointing.
- [[PyTorch Distributed Checkpoint (DCP)|Torch Distributed Checkpoint]] – The PyTorch API for saving and loading distributed model states.
- [[Workload YAML for Distributed Training|Distributed Training]] – Multi-GPU and multi-node training workflows.
- GPU Environment 5 – The minimum GPU environment version required for `UCVolume*` APIs.
- [[Serverless GPU API]] – The underlying service providing serverless GPU compute.

### Sources

- experiment-tracking-and-observability-databricks-on-aws.md
```

# Citations

1. [experiment-tracking-and-observability-databricks-on-aws.md](/references/experiment-tracking-and-observability-databricks-on-aws-4c27cc68.md)
