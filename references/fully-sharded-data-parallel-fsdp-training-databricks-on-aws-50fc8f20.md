---
title: Fully Sharded Data Parallel (FSDP) training | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-fsdp
ingestedAt: "2026-06-18T08:08:36.795Z"
---

This page has notebook examples for using [Fully Sharded Data Parallel (FSDP)](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html) training on AI Runtime. FSDP shards model parameters, gradients, and optimizer states across GPUs, enabling training of very large models that don't fit in a single GPU's memory.

## When to use FSDP[​](#when-to-use-fsdp "Direct link to When to use FSDP")

Use FSDP when:

*   Your model is too large to fit in a single GPU's memory
*   You need to train models in the 20B to 120B+ parameter range
*   You want more memory efficiency than DDP provides

For smaller models that fit in single GPU memory, consider [DDP](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-ddp) for simplicity. For advanced memory optimization features, see [DeepSpeed](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-deepspeed).

## Examples[​](#examples "Direct link to Examples")
