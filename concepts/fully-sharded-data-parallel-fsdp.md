---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7481c1bef496487695a4138c534de1264a1e512245864e6f1f04c29576c91639
  pageDirectory: concepts
  sources:
    - distributed-training-using-deepspeed-databricks-on-aws.md
    - fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
    - multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - fully-sharded-data-parallel-fsdp
    - FSDP(
    - Fully Shaded Data Parallel (FSDP)
    - Fully Sharded Data Parallel
    - Fully Sharded Data Parallel (FSDP) training
    - fully_shard
  citations:
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
    - file: fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
    - file: fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md
    - file: distributed-data-parallel-ddp-training-databricks-on-aws.md
title: Fully Sharded Data Parallel (FSDP)
description: A PyTorch-native distributed training strategy for large model training, presented as an alternative to DeepSpeed
tags:
  - machine-learning
  - distributed-training
  - pytorch
timestamp: "2026-06-19T18:37:08.617Z"
---

# Fully Sharded Data Parallel (FSDP)

**Fully Sharded Data Parallel (FSDP)** is a PyTorch distributed training strategy that shards model parameters, gradients, and optimizer states across multiple GPUs. By reducing the per-GPU memory footprint, FSDP enables training of very large models that would not fit into the memory of a single GPU. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## How FSDP Works

FSDP is a data‑parallelism technique that divides model parameters, gradients, and optimizer states among GPUs. During the forward pass, all‑gather operations collect the full parameters for each layer on every GPU; after the backward pass, gradients are reduced and the sharded parameters are updated locally. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md, fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

The sharding strategy is configured via parameters such as `sharding_strategy` (e.g., `FULL_SHARD`), `mixed_precision`, and `activation_checkpointing`. Common configuration options include: ^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

- `mixed_precision: PURE` – Use pure bfloat16 mixed precision.
- `state_dict_type: sharded` – Save sharded state dicts instead of full.
- `limit_all_gathers: true` – Limit the number of simultaneous all‑gather operations.
- `activation_checkpointing: true` – Trade compute for memory by not storing all intermediate activations.
- `activation_cpu_offload: false` – Do not offload activations to CPU.

To apply FSDP, users wrap each transformer block (or other logical module) using an auto‑wrap policy. PyTorch’s `fsdp="full_shard auto_wrap"` argument automatically wraps the model based on the classes specified in `fsdp_config.fsdp_transformer_layer_cls_to_wrap`. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md] A helper function can infer decoder‑layer class names from the model’s structure. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## When to Use FSDP

FSDP is the recommended choice when the model is too large to fit in a single GPU’s memory, especially for models in the 20B to 120B+ parameter range. It offers better memory efficiency than standard [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md), where the full model is replicated on each GPU. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

For smaller models that fit comfortably in a single GPU, [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) is simpler and sufficient. For advanced memory optimization features such as ZeRO offloading, consider [DeepSpeed](/concepts/deepspeed.md) as an alternative. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md, distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Using FSDP on Databricks

Databricks provides examples of FSDP training on serverless GPU compute using both the `@distributed` decorator and YAML configuration with Mosaic LLM Foundry.

### With the `@distributed` Decorator

The following snippet shows the key FSDP configuration for a 120B parameter model using [TRL](/concepts/trl-transformer-reinforcement-learning-library.md)’s `SFTTrainer`:^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

```python
training_args = SFTConfig(
    output_dir=OUTPUT_DIR,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=4,
    bf16=True,
    fsdp="full_shard auto_wrap",
    fsdp_config={
        "version": 2,
        "fsdp_transformer_layer_cls_to_wrap": fsdp_wrap_classes,
        "reshard_after_forward": True,
        "activation_checkpointing": True,
        "xla": False,
        "limit_all_gathers": True,
    },
)
```

The `fsdp_wrap_classes` list is derived from the model’s structure (e.g., `LlamaDecoderLayer`, `MistralDecoderLayer`, etc.). This configuration is combined with LoRA to reduce trainable parameters further. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

### With Mosaic LLM Foundry

The following YAML excerpt shows FSDP configuration for fine-tuning Llama 3.1 8B with LLM Foundry:^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

```yaml
fsdp_config:
  verbose: false
  mixed_precision: PURE
  state_dict_type: sharded
  limit_all_gathers: true
  sharding_strategy: FULL_SHARD
  activation_cpu_offload: false
  activation_checkpointing: true
  activation_checkpointing_reentrant: false
```

In both cases, the training is launched on [Databricks Serverless GPU](/concepts/databricks-serverless-gpu.md) compute using 8× H100 GPUs, and metrics are logged to [MLflow](/concepts/mlflow.md) while checkpoints are saved to [Unity Catalog](/concepts/unity-catalog.md) volumes. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md, fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

## Related Concepts

- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – Simpler data parallelism for models that fit in a single GPU.
- [DeepSpeed](/concepts/deepspeed.md) – Alternative library with ZeRO and offloading.
- LoRA – Parameter‑efficient fine‑tuning that reduces trainable parameters.
- Mixed Precision Training – Using FP16/BF16 to lower memory and accelerate training.
- [Activation Checkpointing](/concepts/activation-checkpointing.md) – Trading compute for memory by recomputing activations.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – Databricks managed GPU environment for distributed training.
- [Mosaic LLM Foundry](/concepts/mosaic-llm-foundry.md) – Framework for training and fine‑tuning LLMs with built‑in FSDP support.
- [TRL](/concepts/trl-transformer-reinforcement-learning-library.md) – Transformers Reinforcement Learning library providing `SFTTrainer`.

## Sources

- distributed-data-parallel-ddp-training-databricks-on-aws.md
- fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md
- fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md

# Citations

1. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
2. [fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md](/references/fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws-9fff83fc.md)
3. [fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md](/references/fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws-d6760424.md)
4. [distributed-data-parallel-ddp-training-databricks-on-aws.md](/references/distributed-data-parallel-ddp-training-databricks-on-aws-7c300c72.md)
