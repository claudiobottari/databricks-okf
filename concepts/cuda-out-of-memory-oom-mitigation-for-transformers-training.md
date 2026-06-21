---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ffe584f9d36a0f9595e9d10b9367aea72f1e3567de946c2437109d646ad180a8
  pageDirectory: concepts
  sources:
    - fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cuda-out-of-memory-oom-mitigation-for-transformers-training
    - COOM(MFTT
  citations:
    - file: fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
    - file: inferred
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
title: CUDA Out of Memory (OOM) Mitigation for Transformers Training
description: A collection of strategies to resolve CUDA out-of-memory errors during single-GPU training, including reducing batch size, using FP16 precision, gradient accumulation steps, 8-bit Adam optimizer, and GPU memory cleanup.
tags:
  - gpu
  - troubleshooting
  - memory-optimization
  - huggingface
timestamp: "2026-06-19T10:32:48.827Z"
---

# CUDA Out of Memory (OOM) Mitigation for Transformers Training

**CUDA Out of Memory (OOM)** is a common error when training large transformer models on a single GPU. The error typically occurs when the combined memory footprint of model parameters, gradients, optimizer states, activations, and temporary buffers exceeds the GPU’s available VRAM. This page describes mitigation strategies drawn from Databricks documentation for fine-tuning Hugging Face transformers and for training models at scale using sharded data parallelism.

## Common Error Message

A typical OOM error looks like:

```
OutOfMemoryError: CUDA out of memory. Tried to allocate 20.00 MiB (GPU 0; 14.76 GiB total capacity; 666.34 MiB already allocated; 17.75 MiB free; 720.00 MiB reserved in total by PyTorch)
```

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Mitigation Strategies for Single-GPU Training

The following techniques can reduce peak GPU memory usage when training transformers with Hugging Face’s `Trainer` on a single GPU. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### 1. Reduce the Per-Device Batch Size

The batch size directly affects memory consumption for activations. Reducing `per_device_train_batch_size` in `TrainingArguments` lowers the memory required per forward/backward pass. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
from transformers import TrainingArguments
training_args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=4,  # Start low and increase if memory allows
    evaluation_strategy="epoch",
)
```

### 2. Enable Mixed Precision (FP16)

Using `fp16=True` in `TrainingArguments` enables automatic mixed precision training. The majority of computations use 16-bit floats, which halve memory requirements for activations and gradients compared to FP32. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
training_args = TrainingArguments(
    output_dir="./results",
    fp16=True,  # Enables mixed precision
    per_device_train_batch_size=8,
)
```

### 3. Use Gradient Accumulation

Gradient accumulation allows you to simulate a larger effective batch size without increasing per-step memory. Instead of updating weights after every micro-batch, the `Trainer` accumulates gradients over `gradient_accumulation_steps` micro-batches before performing an optimizer step. This is useful when reducing per-device batch size but still needing a large effective batch. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
training_args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=4,
    gradient_accumulation_steps=8,  # Effective batch = 4 * 8 = 32
    fp16=True,
)
```

### 4. Use the 8-Bit Adam Optimizer

The standard Adam optimizer stores two optimizer states per parameter (first and second moments), each in FP32. By replacing Adam with the [8-bit Adam optimizer](https://huggingface.co/docs/transformers/main/en/perf_train_gpu_one#8bit-adam), these states are quantised to 8 bits, reducing optimizer memory by roughly 75%. This is available via the `bitsandbytes` library. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
from transformers import Trainer
from bitsandbytes.optim import AdamW8bit

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    optimizers=(AdamW8bit(model.parameters(), lr=5e-5), None),
)
```

After installing `bitsandbytes`, you can also set `optim="adamw_8bit"` in `TrainingArguments`. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### 5. Clean Up GPU Memory Before Training

Residual GPU memory from previous operations can cause OOM even if the model would otherwise fit. Reset the CUDA device before starting training: ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
from numba import cuda
device = cuda.get_current_device()
device.reset()
```

Alternatively, a more common PyTorch approach is to call `torch.cuda.empty_cache()` before training. ^[inferred]

## Advanced Strategies for Large Models

For transformers with billions of parameters, single‑GPU mitigation strategies alone are insufficient. Models in the **20B to 120B+ parameter range** require distributed training with memory sharding. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### Fully Sharded Data Parallel (FSDP)

[Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) shards model parameters, gradients, and optimizer states across multiple GPUs. This dramatically reduces per‑GPU memory and is the **primary recommended approach** for training models at this scale. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### DeepSpeed

For workloads needing even more advanced memory optimization (e.g., ZeRO stages 2 and 3, offloading to CPU), [DeepSpeed](/concepts/deepspeed.md) provides additional strategies beyond FSDP’s default capabilities. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## Additional Troubleshooting: CUDA Kernel Errors

Another class of CUDA errors during training are kernel crashes, which may produce a generic message like:

```
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
```

To debug these: ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

- Run the same code on CPU to check if the error is reproducible.
- Set the environment variable `CUDA_LAUNCH_BLOCKING=1` to get a synchronous traceback:

```python
import os
os.environ["CUDA_LAUNCH_BLOCKING"] = "1"
```

This forces PyTorch to execute CUDA kernels synchronously, pinpointing the exact line where the error occurs. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Related Concepts

- Memory Management in PyTorch
- Mixed Precision Training
- [Gradient Accumulation](/concepts/gradient-accumulation-fusion.md)
- 8-bit Optimizers
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [DeepSpeed](/concepts/deepspeed.md)
- [Best Practices for Deep Learning on Databricks](/concepts/best-practices-for-deep-learning-on-databricks.md)
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md)

## Sources

- fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md

# Citations

1. [fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md](/references/fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws-e2c49846.md)
2. inferred
3. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
