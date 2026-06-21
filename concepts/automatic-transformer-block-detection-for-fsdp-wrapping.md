---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 648af4a1e4708773540b097c06475ae611dd06d539a68d1831be785c45692c3c
  pageDirectory: concepts
  sources:
    - fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
  confidence: 0.94
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automatic-transformer-block-detection-for-fsdp-wrapping
    - ATBDFFW
  citations:
    - file: fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
title: Automatic Transformer Block Detection for FSDP Wrapping
description: A technique to programmatically infer which module classes in a model correspond to transformer decoder layers, enabling correct FSDP auto-wrap configuration without hardcoding class names.
tags:
  - distributed-training
  - automation
  - deep-learning
timestamp: "2026-06-19T18:52:21.741Z"
---

# Automatic Transformer Block Detection for FSDP Wrapping

**Automatic Transformer Block Detection for FSDP Wrapping** is a technique used in distributed training with [FSDP (Fully Sharded Data Parallel)](/concepts/fsdp-fully-sharded-data-parallel.md) to automatically identify the transformer decoder/encoder layer classes in a model, so those layers can be wrapped as FSDP units without manual inspection. This approach reduces configuration errors and simplifies the setup of FSDP `auto_wrap` policies, especially when fine‑tuning large models such as OpenAI's GPT‑OSS 120B. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Overview

When training very large models with FSDP, it is common to apply the `auto_wrap` policy so that each transformer block is treated as a separate FSDP unit. This minimizes communication overhead and improves memory efficiency. The `auto_wrap` policy requires specifying a list of transformer block class names via the `fsdp_transformer_layer_cls_to_wrap` configuration key. Manually determining these class names for an unfamiliar model is error‑prone. The automatic detection method solves this by scanning the model's module hierarchy and matching class names against known patterns. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Implementation

The function `infer_transformer_blocks_for_fsdp(model)` performs the detection in two phases:

### 1. Exact match against a known set of block classes

The function maintains a set of common transformer layer class names that appear in popular model architectures:

```
"LlamaDecoderLayer", "MistralDecoderLayer", "MixtralDecoderLayer",
"Qwen2DecoderLayer", "Gemma2DecoderLayer", "Phi3DecoderLayer",
"GPTNeoXLayer", "MPTBlock", "BloomBlock", "FalconDecoderLayer",
"DecoderLayer", "GPTJBlock", "OPTDecoderLayer"
```

It iterates over all named submodules of the model and records any module whose class name appears in this set. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

### 2. Fallback heuristic

If the exact match phase yields no results (for example, when a model uses a custom block naming convention not in the predefined set), the function falls back to a heuristic: it searches for any module whose class name contains the substrings `"Block"`, `"DecoderLayer"`, or `"Layer"` — as long as the name does not contain `"Embedding"`. This heuristic aims to catch most transformer‑like blocks even in unusual architectures. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

The function returns a sorted list of unique class names, which is then passed to the FSDP configuration as `fsdp_transformer_layer_cls_to_wrap`. If no classes are found after both phases, a runtime error is raised. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Usage in a Training Job

In the example notebook for fine‑tuning GPT‑OSS 120B on Databricks Serverless GPU Compute, the detection function is called immediately after the model is prepared for training (with LoRA adapters applied). The resulting list is used in the `SFTConfig`'s `fsdp_config`:

```python
fsdp_wrap_classes = infer_transformer_blocks_for_fsdp(model)
if not fsdp_wrap_classes:
    raise RuntimeError(...)

training_args = SFTConfig(
    ...,
    fsdp="full_shard auto_wrap",
    fsdp_config={
        "version": 2,
        "fsdp_transformer_layer_cls_to_wrap": fsdp_wrap_classes,
        "reshard_after_forward": True,
        "activation_checkpointing": True,
        ...
    },
)
```

This setup enables FSDP2 with full sharding and automatic layer wrapping, which is essential for fitting a 120B‑parameter model on eight H100 GPUs. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Best Practices

- Use the function **after** any model modifications (such as applying LoRA or converting dtypes) so that the module hierarchy is final.
- If the fallback heuristic matches too many modules (e.g., non‑transformer blocks that happen to contain "Layer"), manually verify the detected class list or extend the predefined set.
- When working with a model not covered by the predefined set, add its decoder/encoder layer class name to the `COMMON` set inside the function for deterministic matching. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Related Concepts

- FSDP Custom Auto Wrap Policy — Advanced configuration for layer‑wise FSDP wrapping.
- FSDP Activation Checkpointing — A memory‑saving technique often combined with auto wrap.
- [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md) — Parameter‑efficient fine‑tuning used alongside FSDP.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The Databricks environment where this technique is demonstrated.

## Sources

- fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md

# Citations

1. [fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md](/references/fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws-9fff83fc.md)
