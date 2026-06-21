---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 111f90d72133a53ff4050e4933e847c7629aecbf87ebe88de00f9651859b46cf
  pageDirectory: concepts
  sources:
    - distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mxfp4-quantization
    - Quantization
  citations:
    - file: distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
    - file: |-
        distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md>

        ## Benefits

        * **4× memory reduction** for weight tensors: storing 4‑bit instead of 16‑bit cuts the footprint of weights approximately four‑fold.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
    - file: |-
        distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md>

        ## Considerations

        * `dequantize=True` adds a dequantization overhead during each forward pass
    - file: which may slightly reduce training throughput compared to native 4‑bit hardware.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
    - file: |-
        distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md>
        * When using gradient checkpointing
    - file: "`use_cache` must be set to `False` to avoid memory conflicts.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md"
title: MXFP4 Quantization
description: Microscaling 4-bit floating point format that reduces memory requirements during model training and inference by representing weights in a compact 4-bit format with per-group scaling factors.
tags:
  - quantization
  - memory-optimization
  - deep-learning
timestamp: "2026-06-19T18:32:50.869Z"
---

```yaml
---
title: MXFP4 Quantization
summary: Microscaling 4-bit floating point format that reduces memory usage during training and inference of large language models
sources:
  - distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:02:01.358Z"
updatedAt: "2026-06-19T15:14:01.732Z"
tags:
  - machine-learning
  - quantization
  - optimization
aliases:
  - mxfp4-quantization
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 2
```

# MXFP4 Quantization

**MXFP4 (Microscaling 4-bit Floating Point) quantization** is a memory-saving technique that represents model weights and activations in a 4-bit floating‑point format with a shared microscaling exponent per block. It enables fine‑tuning and inference of large language models (LLMs) on GPU‑constrained hardware by reducing the per‑parameter memory footprint approximately 4‑fold compared to standard 16‑bit formats, while preserving more numerical range than traditional 4‑bit integer quantization.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## Overview

MXFP4 is a microscaling floating‑point format defined as part of the Microscaling Formats (MX) standard. In MXFP4, each 4‑bit element shares a block‑level scaling factor (exponent), which increases the effective dynamic range of a low‑precision block. During training or inference, weights stored in MXFP4 can be dequantized on the fly to a higher‑precision format – typically BFloat16 – for the actual matrix‑multiply operations, balancing memory savings with numerical accuracy.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## Usage in Hugging Face Transformers

MXFP4 quantization is supported through the `Mxfp4Config` class in the Hugging Face Transformers library. When loading a compatible `AutoModelForCausalLM` model, users pass `quantization_config=Mxfp4Config()` to the `from_pretrained` call.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

### Dequantization Parameter

The key configuration parameter is `dequantize`:

* **`dequantize=True` (default)**: weights are kept in MXFP4 in GPU memory but are dequantized to BFloat16 before each forward pass. This preserves the memory savings of 4‑bit storage while avoiding the need for custom 4‑bit CUDA kernels for arithmetic; the actual computation still runs in BFloat16.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]
* **`dequantize=False`**: weights remain in MXFP4 format throughout, which may require hardware‑level support for native 4‑bit floating‑point operations on the GPU.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

### Example

The following code snippet, taken from a distributed fine‑tuning notebook, shows how to load the OpenAI gpt-oss-20b model with MXFP4 quantization:^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

```python
from transformers import AutoModelForCausalLM, Mxfp4Config

quantization_config = Mxfp4Config(dequantize=True)
model_kwargs = dict(
    attn_implementation="eager",
    dtype=torch.bfloat16,
    quantization_config=quantization_config,
    use_cache=False,  # Since using gradient checkpointing
)
model = AutoModelForCausalLM.from_pretrained("openai/gpt-oss-20b", **model_kwargs)
```

In this configuration, `use_cache` is set to `False` because [gradient checkpointing](/concepts/activation-checkpointing.md) is used during training – caching intermediate activations would otherwise consume additional memory.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## Integration with Distributed Fine‑Tuning

The primary documented use case is distributed fine‑tuning of the 20B‑parameter [[gpt-oss-20b|OpenAI gpt-oss-20b]] model on 8 H100 GPUs. The Databricks example notebook combines MXFP4 quantization with several complementary techniques:^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

* [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md): the base model is frozen; only small adapter matrices are trained in full precision.
* [Distributed Data Parallelism](/concepts/distributed-data-parallel-ddp.md): training is distributed across 8 H100 GPUs on a single node using the `@distributed` decorator from the `serverless_gpu` library.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]
* [Gradient Checkpointing](/concepts/activation-checkpointing.md): trades compute for memory by recomputing activations during the backward pass.
* Mixed‑precision training: configured via `SFTConfig` / `SFTTrainer` from [TRL](/concepts/trl-transformer-reinforcement-learning.md) (Transformer Reinforcement Learning library).
* GPU memory logging: a `log_gpu_memory` helper reports allocated and reserved GPU memory during training to aid memory debugging.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

This stack allows the 20B model to fit into the combined memory of 8 H100 GPUs with reasonable per‑GPU memory usage.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md>

## Benefits

* **4× memory reduction** for weight tensors: storing 4‑bit instead of 16‑bit cuts the footprint of weights approximately four‑fold.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]
* **Preserved model quality**: the microscaling exponent maintains better dynamic range than purely integer 4‑bit quantization, reducing accuracy loss.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]
* **Seamless integration**: works out of the box with `AutoModelForCausalLM` and common training loops; no custom quantization kernels are needed when `dequantize=True`.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]
* **Compatibility with PEFT**: can be combined with LoRA and [Q-LoRA](/concepts/qlora-quantized-low-rank-adaptation.md) style approaches, where the base model is quantized and only low‑rank adapters are updated in full precision.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md>

## Considerations

* `dequantize=True` adds a dequantization overhead during each forward pass, which may slightly reduce training throughput compared to native 4‑bit hardware.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]
* The format is best suited for **training** and **fine‑tuning** scenarios where memory pressure is the primary bottleneck; for pure inference serving, dedicated 4‑bit inference kernels such as GPTQ or AWQ may offer lower latency.
* Not all model architectures may be fully supported by `Mxfp4Config`; compatibility is expected to grow as the MX standard gains adoption.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md>
* When using gradient checkpointing, `use_cache` must be set to `False` to avoid memory conflicts.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## Related Concepts

* [Quantization](/concepts/mxfp4-quantization.md) – general technique of reducing numerical precision
* [Q-LoRA](/concepts/qlora-quantized-low-rank-adaptation.md) – combining quantization with low‑rank adaptation
* BFloat16 – the dequantization target used alongside MXFP4
* Microscaling Formats (MX) – the OCP standard defining MXFP4 and other formats
* [Gradient Checkpointing](/concepts/activation-checkpointing.md) – technique to trade compute for memory, often used with MXFP4
* LoRA – parameter‑efficient fine‑tuning method
* [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – the GPU configuration used with MXFP4 in the documented example
* [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) – the scale of models that benefit from memory optimization techniques like MXFP4

## Sources

* distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md

# Citations

1. [distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md](/references/distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws-7ee24e1a.md)
2. distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md>

## Benefits

* **4× memory reduction** for weight tensors: storing 4‑bit instead of 16‑bit cuts the footprint of weights approximately four‑fold.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
3. distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md>

## Considerations

* `dequantize=True` adds a dequantization overhead during each forward pass
4. which may slightly reduce training throughput compared to native 4‑bit hardware.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
5. distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md>
* When using gradient checkpointing
6. `use_cache` must be set to `False` to avoid memory conflicts.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
