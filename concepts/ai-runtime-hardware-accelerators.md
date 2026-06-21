---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fa59848d829e2c2e339e481ab24ba8a4c0bc7d789a00dbb3de2f7fc8fd9be073
  pageDirectory: concepts
  sources:
    - ai-runtime-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-hardware-accelerators
    - ARHA
  citations:
    - file: ai-runtime-databricks-on-aws.md
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
title: AI Runtime Hardware Accelerators
description: The GPU hardware options available for AI Runtime on AWS, including A10 and H100 accelerators (single-node, multi-GPU), with region-specific availability and capacity considerations.
tags:
  - databricks
  - infrastructure
  - gpu
  - hardware
timestamp: "2026-06-19T22:03:44.123Z"
---

```markdown
---
title: AI Runtime Hardware Accelerators
summary: Supported GPU accelerators for AI Runtime including A10 and H100 (Beta) on single-node configurations
sources:
  - ai-runtime-databricks-on-aws.md
  - get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:44:09.411Z"
updatedAt: "2026-06-19T17:31:10.010Z"
tags:
  - gpu
  - hardware
  - infrastructure
aliases:
  - ai-runtime-hardware-accelerators
  - ARHA
confidence: 1
provenanceState: extracted
inferredParagraphs: 1
---

# AI Runtime Hardware Accelerators

**AI Runtime Hardware Accelerators** are the GPU-based compute resources provided by [[AI Runtime]], Databricks' serverless compute offering for deep learning workloads. Each accelerator type provisions a single node; the number of GPUs on that node depends on the chosen accelerator type. ^[ai-runtime-databricks-on-aws.md]

## Supported Accelerators

AI Runtime supports two GPU accelerator types: ^[ai-runtime-databricks-on-aws.md]

| Accelerator | Status | Notes |
|-------------|--------|-------|
| A10 | General Availability | Single-node GPU accelerator for deep learning tasks. |
| 1xH100 | Beta | Requires enabling the **AI Runtime Beta Feature** preview in workspace admin settings. See Manage Databricks Previews. |

For large model training workloads that require higher throughput and memory, Databricks also offers an **8xH100** configuration through [[Serverless GPU Compute]]. This provisions eight NVIDIA H100 80GB HBM3 GPUs on a single node, providing 640 GB of total GPU memory, and is selected via the **8xH100** accelerator option in the Environment side panel. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

All accelerators are fully managed and serverless—no cluster configuration, driver selection, or autoscaling policies are required. ^[ai-runtime-databricks-on-aws.md]

## Selecting an Accelerator

To select an accelerator from a Databricks notebook:

1. From the compute selector, choose a connection method that supports AI Runtime.
2. In the **Environment** tab on the right panel, locate the **Accelerator** field.
3. Choose the desired accelerator type (e.g., **A10**, **1xH100**, or **8xH100**).
4. For the 8xH100 configuration, select the **AI v5** environment, which contains all required libraries for running distributed GPU workloads.
5. Click **Apply**.

^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md, ai-runtime-databricks-on-aws.md]

## Recommended Use Cases

Databricks recommends AI Runtime for any custom model training use cases that involve deep learning, large-scale classic workloads, or GPUs. ^[ai-runtime-databricks-on-aws.md]

| Use Case | Recommended Accelerator |
|----------|------------------------|
| LLM fine-tuning (LoRA, QLoRA, full fine-tuning) | A10, 1xH100, or 8xH100 |
| Computer vision (object detection, image classification) | A10 or 1xH100 |
| Deep-learning-based recommender systems | A10 or 1xH100 |
| Reinforcement learning | 1xH100 or 8xH100 |
| Deep-learning-based time series forecasting | A10 or 1xH100 |
| Large model training requiring high throughput and memory | 8xH100 |

H100 GPUs offer larger FLOPS and HBM compared to A10 GPUs. Use the 8xH100 configuration for **training** large models where high throughput and/or large GPU memory is needed. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Region Availability

AI Runtime is available in the following AWS regions: ^[ai-runtime-databricks-on-aws.md]

- `us-west-2`
- `us-west-1`
- `us-east-1`
- `us-east-2`
- `ca-central-1`
- `sa-east-1`

Additional regions may be supported over time. ^[ai-runtime-databricks-on-aws.md]

## Requirements

- A workspace in one of the supported AWS regions listed above. ^[ai-runtime-databricks-on-aws.md]
- The AI Runtime preview must be enabled via workspace admin settings. See Manage Databricks Previews. ^[ai-runtime-databricks-on-aws.md]
- For the 1xH100 accelerator, a workspace admin must enable the **AI Runtime Beta Feature** preview from the **Previews** page. ^[ai-runtime-databricks-on-aws.md]

## Limitations

- AI Runtime only supports A10 and H100 accelerators. ^[ai-runtime-databricks-on-aws.md]
- AI Runtime is **not** supported for [[Compliance Security Profile (Databricks on AWS)|Compliance Security Profile]] workspaces (e.g., HIPAA or PCI). Processing regulated data is not supported. ^[ai-runtime-databricks-on-aws.md]
- Adding dependencies using the **Environments** panel is not supported for AI Runtime scheduled jobs. Install dependencies programmatically using `%pip install` in your notebook instead. ^[ai-runtime-databricks-on-aws.md]
- For scheduled jobs on AI Runtime, auto recovery behavior for incompatible package versions that are associated with your notebook is not supported. ^[ai-runtime-databricks-on-aws.md]
- The maximum runtime for a workload is seven days. For training jobs that exceed this limit, implement checkpointing and restart the job. ^[ai-runtime-databricks-on-aws.md]
- GPU resources are provided on‑demand; capacity may be constrained or unavailable in some regions during periods of high demand. ^[ai-runtime-databricks-on-aws.md]
- AI Runtime may leverage cross‑region GPUs during high demand, which can incur egress costs and may have limited network connectivity. ^[ai-runtime-databricks-on-aws.md]

## Verifying Accelerator Configuration

Use the `nvidia-smi` command to confirm connection to the expected GPUs. For the 8xH100 configuration, each GPU reports as an NVIDIA H100 80GB HBM3 with 81,559 MiB of total memory and a maximum power draw of 700 W. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Distributed Training with Multiple GPUs

AI Runtime supports distributed training across multiple GPUs on the single node your notebook is connected to. Using the `@distributed` decorator from the `serverless_gpu` Python API, you can launch multi-GPU workloads with [[PyTorch DDP on Databricks|PyTorch DDP]], [[Fully Sharded Data Parallel (FSDP)]], or [[DeepSpeed]] with minimal configuration. For details, see Multi-GPU Workload on AI Runtime. ^[ai-runtime-databricks-on-aws.md, get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

```python
from serverless_gpu import distributed
from serverless_gpu import runtime as rt

@distributed(
    gpus=8,
    gpu_type='h100',
)
def hello_world(name: str) -> list[int]:
    if rt.get_local_rank() == 0:
        print('hello world', name)
    return rt.get_global_rank()

result = hello_world.distributed('Example')
# result == [0, 1, 2, 3, 4, 5, 6, 7]
```

- `gpus=8` specifies that the function runs on 8 processes, one per GPU.
- `rt.get_local_rank()` returns the rank of the GPU within the node.
- `rt.get_global_rank()` returns the global rank across all processes.

## Related Concepts

- [[AI Runtime]] — The serverless compute offering that uses these accelerators.
- [[AI Runtime CLI]] — Command‑line tool for submitting training workloads.
- [[AI Runtime Environments|AI Runtime Environment]] — Managed Python environments available on AI Runtime.
- [[Serverless GPU Compute]] — The compute infrastructure that provisions GPU resources on demand.
- [[8xH100 Single-Node Configuration]] — Detailed documentation on the eight H100 GPU configuration.
- [[A100 GPU Support on Databricks]] — A100 GPU availability for Databricks clusters.
- [[Unity Catalog]] — Governance layer for managing data and ML assets.
- [[Workload YAML for Distributed Training|Distributed Training]] — Multi‑GPU workload support via the `@distributed` decorator.
- [[Multi-GPU distributed training API|Multi-Node Distributed Training]] — Scaling beyond a single node by coordinating across multiple GPU nodes.

## Sources

- ai-runtime-databricks-on-aws.md
- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
```

# Citations

1. [ai-runtime-databricks-on-aws.md](/references/ai-runtime-databricks-on-aws-a734dca1.md)
2. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
