---
title: Distributed training using DeepSpeed | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-deepspeed
ingestedAt: "2026-06-18T08:08:33.916Z"
---

This page has notebook examples for distributed training using [DeepSpeed](https://github.com/deepspeedai/DeepSpeed) on AI Runtime. DeepSpeed provides advanced memory optimization techniques through its ZeRO (Zero Redundancy Optimizer) stages, enabling efficient training of large models.

## When to use DeepSpeed[​](#when-to-use-deepspeed "Direct link to When to use DeepSpeed")

Use DeepSpeed when:

*   You need advanced memory optimization beyond standard FSDP
*   You want fine-grained control over optimizer state sharding (ZeRO Stage 1, 2, or 3)
*   You need additional features like gradient accumulation fusion or CPU offloading
*   You're working with large language models (1B to 100B+ parameters)

For simpler use cases, consider [DDP](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-ddp). For PyTorch-native large model training, see [FSDP](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-fsdp).

## Examples[​](#examples "Direct link to Examples")
