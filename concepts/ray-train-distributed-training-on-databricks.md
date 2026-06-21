---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ad0424efd1ac724498403921cd6e5a62e188de98ed9a88a83705aeecf399bd55
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-examples-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-train-distributed-training-on-databricks
    - RTDTOD
  citations:
    - file: ai-runtime-cli-examples-databricks-on-aws.md
      start: 1
      end: 3
    - file: ai-runtime-cli-examples-databricks-on-aws.md
      start: 7
      end: 9
    - file: ai-runtime-cli-examples-databricks-on-aws.md
      start: 7
      end: 8
    - file: ai-runtime-cli-examples-databricks-on-aws.md
      start: 5
      end: 6
    - file: ai-runtime-cli-examples-databricks-on-aws.md
      start: 5
      end: 9
title: Ray Train Distributed Training on Databricks
description: Pattern for distributed data-parallel fine-tuning using Ray Train's TorchTrainer across GPUs on a single node, with one worker per GPU, running on Databricks AI Runtime
tags:
  - ray
  - distributed-training
  - databricks
timestamp: "2026-06-19T22:03:01.088Z"
---

---
title: Ray Train Distributed Training on Databricks
summary: Distributed data-parallel fine-tuning pattern using Ray Train's TorchTrainer across 8 H100 GPUs on a single node, with one worker per GPU, submitted via the air CLI.
sources:
  - ai-runtime-cli-examples-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T13:56:38.793Z"
updatedAt: "2026-06-19T13:56:38.793Z"
tags:
  - distributed-training
  - ray
  - databricks
aliases:
  - ray-train-distributed-training-on-databricks
  - RTDTOD
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Ray Train Distributed Training on Databricks

**Ray Train distributed training on Databricks** refers to the use of the [Ray Train](/concepts/ray-train-resource-allocation.md) library with Databricks [AI Runtime](/concepts/ai-runtime.md) to run distributed deep learning workloads, such as fine-tuning large language models, across GPU clusters. The AI Runtime CLI provides a complete example for launching such workloads using `air run -f train.yaml`. ^[ai-runtime-cli-examples-databricks-on-aws.md:1-3]

## Overview

Databricks supports distributed data-parallel fine-tuning with Ray Train's `TorchTrainer`. This approach leverages the familiar PyTorch training loop while benefiting from Ray's distributed scheduling and fault tolerance. The official example demonstrates a single-node, multi-GPU setup with one worker per GPU. ^[ai-runtime-cli-examples-databricks-on-aws.md:7-9]

## Example Configuration

The AI Runtime CLI example "Distributed training with Ray Train" runs distributed data-parallel fine-tuning across **8 H100 GPUs on a single node** ([8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md)), with one Ray Train worker per GPU. The training code uses `TorchTrainer` from the Ray Train library. ^[ai-runtime-cli-examples-databricks-on-aws.md:7-8]

The workload is submitted via:

```bash
air run -f train.yaml
```

The YAML file, launcher script, and training code for this example are available in the [AI Runtime examples documentation](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/examples/ray-train-distributed). ^[ai-runtime-cli-examples-databricks-on-aws.md:1-3]

### Related AI Runtime CLI Examples

The same page lists other distributed training patterns that can inform the choice of parallelism strategy:

- Multi-node LLM fine-tuning with [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) across 16 H100 GPUs (2 nodes) using `torchrun`. This is suitable for [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) scenarios where memory efficiency is critical. ^[ai-runtime-cli-examples-databricks-on-aws.md:5-6]
- The Ray Train single-node example is presented as an alternative approach for distributed data-parallel fine-tuning. ^[ai-runtime-cli-examples-databricks-on-aws.md:7-9]

## Considerations

The Ray Train example uses Distributed Data Parallel (DDP) as the underlying parallelism strategy. DDP is simpler to implement than FSDP but does not shard model parameters across GPUs. For models that fit within a single GPU's memory (typically models up to 7-13B parameters depending on GPU memory), Ray Train with DDP works well. For larger models that require memory sharding, the multi-node FSDP approach is recommended. ^[ai-runtime-cli-examples-databricks-on-aws.md:5-9]

The single-node configuration ([8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md)) provides 640 GB of total GPU memory across eight H100 80GB GPUs, making it suitable for many medium-to-large model fine-tuning tasks. ^[ai-runtime-cli-examples-databricks-on-aws.md:7-8]

## Related Concepts

- [Ray Train](/concepts/ray-train-resource-allocation.md) – The library for distributed model training on top of Ray.
- [TorchTrainer](/concepts/ray-train-torchtrainer.md) – Ray Train's wrapper for PyTorch training loops.
- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – The `air` command-line tool for submitting workloads on Databricks.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – The hardware configuration used in this example.
- H100 GPU Support on Databricks – Capabilities and configurations of H100 GPUs on the platform.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – A complementary parallelism strategy for multi-node training of larger models.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – The underlying pattern used by Ray Train's TorchTrainer in this example.
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) – The parameter range where FSDP becomes necessary over DDP.

## Sources

- ai-runtime-cli-examples-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-examples-databricks-on-aws.md:1-3](/references/ai-runtime-cli-examples-databricks-on-aws-9e5abf7f.md)
2. [ai-runtime-cli-examples-databricks-on-aws.md:7-9](/references/ai-runtime-cli-examples-databricks-on-aws-9e5abf7f.md)
3. [ai-runtime-cli-examples-databricks-on-aws.md:7-8](/references/ai-runtime-cli-examples-databricks-on-aws-9e5abf7f.md)
4. [ai-runtime-cli-examples-databricks-on-aws.md:5-6](/references/ai-runtime-cli-examples-databricks-on-aws-9e5abf7f.md)
5. [ai-runtime-cli-examples-databricks-on-aws.md:5-9](/references/ai-runtime-cli-examples-databricks-on-aws-9e5abf7f.md)
