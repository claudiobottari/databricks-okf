---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 74b1abe2357d3df4026ba4bd4165ddad2999a22f55cf0656304af7f65991faf4
  pageDirectory: concepts
  sources:
    - fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - activation-checkpointing
    - FSDP Activation Checkpointing
    - CheckpointConfig
    - Gradient Checkpointing
    - Gradient checkpointing
    - gradient checkpointing
  citations:
    - file: fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
title: Activation Checkpointing
description: A memory optimization technique that trades compute for memory by not storing intermediate activations during forward pass and recomputing them during backward pass.
tags:
  - memory-optimization
  - deep-learning
  - training
timestamp: "2026-06-19T10:35:18.961Z"
---

## Activation Checkpointing

**Activation checkpointing** is a memory-saving technique used in distributed training of large deep learning models. During the forward pass, it discards intermediate activations that would normally be stored for the backward pass, then recomputes them on demand when gradients are computed. This trades off a small amount of computation (the recomputation) for a significant reduction in GPU memory usage, enabling the training of models that would otherwise exceed device memory limits. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

### Usage with FSDP

In [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) training, activation checkpointing is often preferred over traditional gradient checkpointing. The FSDP configuration exposes a dedicated boolean flag (`activation_checkpointing`) to enable this behavior. When set to `True`, the FSDP wrapper automatically applies checkpointing to the wrapped layers. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

For example, in an FSDP training script for a 120B parameter model on 8 H100 GPUs, the configuration includes:

```python
fsdp_config={
    "version": 2,
    "fsdp_transformer_layer_cls_to_wrap": fsdp_wrap_classes,
    "reshard_after_forward": True,
    "activation_checkpointing": True,    # use activation ckpt (not gradient)
    "xla": False,
    "limit_all_gathers": True,
}
```

The comment `"use activation ckpt (not gradient)"` indicates that activation checkpointing is used in place of the `gradient_checkpointing` flag in the `SFTConfig` (which is explicitly set to `False`). ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

### Benefits and Tradeoffs

- **Memory savings**: By not storing all intermediate activations, the peak memory per GPU is reduced, which is critical for models with hundreds of billions of parameters.
- **Computation overhead**: The recomputation step adds a minor cost to the backward pass (typically 10–20% more computation).
- **Higher batch sizes**: The memory freed by checkpointing can be used to increase per-device batch size or model size.

### Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Gradient Checkpointing](/concepts/activation-checkpointing.md)
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- Memory Optimization
- [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md)

### Sources

- fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md

# Citations

1. [fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md](/references/fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws-9fff83fc.md)
