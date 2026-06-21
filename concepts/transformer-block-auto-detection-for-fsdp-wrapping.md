---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8dcd170ace72126be44efdd529f73566d967c4f9ba3fc4012ef73e6c00f5bd80
  pageDirectory: concepts
  sources:
    - fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - transformer-block-auto-detection-for-fsdp-wrapping
    - TBAFFW
  citations:
    - file: fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
title: Transformer Block Auto-Detection for FSDP Wrapping
description: A technique for automatically identifying transformer decoder layer class names in a model to configure FSDP's layer wrapping policy for sharding.
tags:
  - distributed-training
  - fsdp
  - transformer
timestamp: "2026-06-19T10:35:28.873Z"
---

# Transformer Block Auto-Detection for FSDP Wrapping

**Transformer Block Auto-Detection for FSDP Wrapping** is a technique that automatically identifies transformer decoder block classes in a model to configure [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) wrapping for distributed training. This approach eliminates the need for manual specification of transformer layer classes when sharding large models across multiple GPUs.

## Overview

FSDP requires knowing which module classes correspond to transformer decoder blocks so that it can wrap them appropriately for parameter sharding and activation checkpointing. The standard approach involves manually specifying a list of class names (e.g., `LlamaDecoderLayer`, `MistralDecoderLayer`) in the FSDP configuration. For novel or custom model architectures, this list may be unknown or require inspection of the model definition.^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Auto-Detection Function

The auto-detection logic inspects the model's modules at runtime to find transformer block classes that match known patterns:^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

```python
def infer_transformer_blocks_for_fsdp(model):
    COMMON = {
        "LlamaDecoderLayer", "MistralDecoderLayer", "MixtralDecoderLayer",
        "Qwen2DecoderLayer", "Gemma2DecoderLayer", "Phi3DecoderLayer",
        "GPTNeoXLayer", "MPTBlock", "BloomBlock", "FalconDecoderLayer",
        "DecoderLayer", "GPTJBlock", "OPTDecoderLayer"
    }
    hits = set()
    for _, m in model.named_modules():
        name = m.__class__.__name__
        if name in COMMON:
            hits.add(name)
    # Fallback: grab anything that *looks* like a decoder block
    if not hits:
        for _, m in model.named_modules():
            name = m.__class__.__name__
            if any(s in name for s in ["Block", "DecoderLayer", "Layer"]) and "Embedding" not in name:
                hits.add(name)
    return sorted(hits)
```

### How It Works

1. **First pass**: Iterates through all modules in the model and checks their class names against a curated set of known transformer decoder layer names from popular architectures (Llama, Mistral, Qwen, Gemma, Phi, GPT-NeoX, MPT, BLOOM, Falcon, GPT-J, OPT).^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

2. **Fallback pass**: If no known classes are found, the function uses a heuristic — matching module names containing keywords like `Block`, `DecoderLayer`, or `Layer`, while excluding `Embedding` modules. This fallback supports custom or newer model architectures that are not in the common list.^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

3. **Error handling**: If both passes yield no results, the function raises a `RuntimeError` instructing the user to print the model and add the block class explicitly.^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Integration with FSDP Configuration

The detected class names are passed to the FSDP configuration via the `fsdp_transformer_layer_cls_to_wrap` field, which controls which layers get individual parameter shards:^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

```python
fsdp_config={
    "version": 2,
    "fsdp_transformer_layer_cls_to_wrap": fsdp_wrap_classes,
    # ...
}
```

## Use Cases

This technique is particularly valuable in the following scenarios:^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

- **Novel architectures**: When training custom transformer models where the decoder layer class name is not known in advance.
- **Automated training pipelines**: When building reusable training functions that must work across multiple model architectures without code changes.
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md): At large parameter scales, FSDP wrapping is essential, and auto-detection simplifies configuration.

## Best Practices

- Verify the detected classes by printing the model structure if training fails or sharding appears incorrect.
- Consider maintaining a local list of known classes for custom architectures to avoid relying on the fallback heuristic.
- When using the fallback pass, be aware that it may match unintended module classes — review the results before critical training runs.

## Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — The distributed training framework that uses this wrapping detection
- Transformer Layer Wrapping — How FSDP partitions transformer layers across GPUs
- LoRA for Distributed Training — Parameter-efficient fine-tuning often combined with FSDP
- [Distributed Training on Databricks](/concepts/distributed-training-on-databricks.md) — Platform context for this technique
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) — Scale where FSDP wrapping becomes critical

## Sources

- fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md

# Citations

1. [fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md](/references/fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws-9fff83fc.md)
