---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 03dbbe3ff48dee748eda1a1bff3f18f573c3ddb1158be1a876eedb7738e8efe4
  pageDirectory: concepts
  sources:
    - connect-to-ai-runtime-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-checkpointing-for-long-running-ai-runtime-jobs
    - MCFLARJ
  citations:
    - file: connect-to-ai-runtime-databricks-on-aws.md
title: Model Checkpointing for Long-Running AI Runtime Jobs
description: Recommended mechanism using Unity Catalog volumes via UCVolumeWriter/UCVolumeReader for workloads exceeding the 7-day maximum runtime.
tags:
  - databricks
  - checkpointing
  - mlops
timestamp: "2026-06-18T14:43:52.994Z"
---

# Model Checkpointing for Long-Running AI Runtime Jobs

**Model Checkpointing for Long-Running AI Runtime Jobs** refers to the practice of periodically saving model state during extended AI training or inference workloads that may exceed the maximum runtime limits of a single execution environment. This technique allows jobs to resume from a saved checkpoint rather than restarting from scratch, preventing loss of progress.

## Overview

[AI Runtime](/concepts/ai-runtime.md) jobs on Databricks have a maximum runtime of 7 days. For workloads that may exceed this limit, manual checkpointing must be implemented to allow resumption. ^[connect-to-ai-runtime-databricks-on-aws.md]

Checkpointing is especially important for long-running training jobs that require significant compute time to converge, such as fine-tuning large language models or training deep neural networks on large datasets.^[connect-to-ai-runtime-databricks-on-aws.md]

## Recommended Approach

Databricks recommends using [Unity Catalog](/concepts/unity-catalog.md) volumes for storing checkpoints, accessed via the `UCVolumeWriter` and `UCVolumeReader` utilities from the `serverless_gpu.data` module. ^[connect-to-ai-runtime-databricks-on-aws.md]

These utilities provide a reliable, managed storage layer for saving and loading model checkpoints:

```python
from serverless_gpu.data import UCVolumeWriter, UCVolumeReader

# Save checkpoint at regular intervals
UCVolumeWriter.write_checkpoint(
    path="/Volumes/catalog/schema/checkpoints/",
    model_state=model.state_dict(),
    step=current_step
)

# Resume from checkpoint on job restart
model_state = UCVolumeReader.load_checkpoint(
    path="/Volumes/catalog/schema/checkpoints/",
    step=resume_step
)
```

^[connect-to-ai-runtime-databricks-on-aws.md]

## Use Cases

- **Training jobs exceeding 7-day runtime**: Long-running training pipelines that require weeks to converge must implement checkpointing to survive job restarts.^[connect-to-ai-runtime-databricks-on-aws.md]
- **Finetuning large language models**: Models with billions of parameters may require extensive training time that exceeds single-job limits.^[connect-to-ai-runtime-databricks-on-aws.md]
- **Distributed training across multiple GPUs**: Multi-GPU workloads using 8xH100 accelerators benefit from checkpointing to recover from individual GPU failures.^[connect-to-ai-runtime-databricks-on-aws.md]
- **Scheduled jobs with periodic triggers**: Recurring AI Runtime jobs that accumulate training progress over multiple runs.^[connect-to-ai-runtime-databricks-on-aws.md]

## Implementation Considerations

- **Checkpoint frequency**: Balance between saving frequently enough to minimize loss and infrequently enough to avoid storage overhead.
- **Storage location**: Use Unity Catalog volumes rather than local cluster storage to ensure checkpoints survive job termination.
- **Automatic cleanup**: Consider implementing a retention policy to remove old checkpoints and prevent storage accumulation.
- **Versioning**: Include model step number or timestamp in checkpoint filenames for easy identification.

## Related Concepts

- [AI Runtime Environment](/concepts/ai-runtime-environments.md) — The execution environment for serverless GPU jobs
- Unity Catalog Volumes — Managed storage for AI artifacts
- Model Checkpointing — General concept for saving model training progress
- Serverless GPU Scheduling — Configuring and managing AI Runtime jobs
- Long-Running Jobs — Jobs that may exceed maximum execution time limits

## Sources

- connect-to-ai-runtime-databricks-on-aws.md

# Citations

1. [connect-to-ai-runtime-databricks-on-aws.md](/references/connect-to-ai-runtime-databricks-on-aws-edaccc2c.md)
