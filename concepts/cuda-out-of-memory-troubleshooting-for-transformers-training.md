---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ac66d1d684952921d08f95ab7253a27d50e8a12fcf35112cce6e5af78e720c5d
  pageDirectory: concepts
  sources:
    - fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cuda-out-of-memory-troubleshooting-for-transformers-training
    - COOMTFTT
  citations:
    - file: fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
title: CUDA Out of Memory Troubleshooting for Transformers Training
description: Common CUDA out-of-memory errors during Hugging Face training and resolution strategies
tags:
  - gpu
  - troubleshooting
  - hugging-face
timestamp: "2026-06-18T12:20:12.734Z"
---

# CUDA Out of Memory Troubleshooting for Transformers Training

**CUDA Out of Memory (OOM) errors** are a common issue when fine-tuning large Hugging Face Transformer models on a single GPU. When training exceeds the available GPU memory, PyTorch raises an `OutOfMemoryError` that halts training. This page provides diagnostic techniques and configuration adjustments to resolve or mitigate OOM errors.

## Error Symptoms

A CUDA OOM error typically appears as:

```
OutOfMemoryError: CUDA out of memory. Tried to allocate 20.00 MiB (GPU 0; 14.76 GiB total capacity; 666.34 MiB already allocated; 17.75 MiB free; 720.00 MiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation. See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF.
```

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Immediate Fixes

### Reduce Batch Size

The most direct remedy is lowering the per-device training batch size. In the Hugging Face `Trainer` API, set `per_device_train_batch_size` in `TrainingArguments` to a smaller value. This reduces the number of samples processed simultaneously, lowering peak GPU memory consumption. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
from transformers import TrainingArguments

training_args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=4,  # Reduce from default (e.g., 8)
    evaluation_strategy="epoch",
)
```

### Use Lower Precision Training

Enable mixed-precision training by setting `fp16=True` in `TrainingArguments`. Half-precision (FP16) uses approximately half the memory of full-precision (FP32), allowing larger models or batch sizes within the same GPU budget. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
training_args = TrainingArguments(
    output_dir="./results",
    fp16=True,  # Enable mixed precision
)
```

### Use Gradient Accumulation

Gradient accumulation simulates a larger batch size without increasing memory usage. Set `gradient_accumulation_steps` in `TrainingArguments` to accumulate gradients over multiple forward/backward passes before performing an optimizer step. For example, with `per_device_train_batch_size=4` and `gradient_accumulation_steps=4`, the effective batch size is 16. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
training_args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,  # Effective batch size = 4 * 4 = 16
)
```

### Use 8-bit Adam Optimizer

The 8-bit Adam optimizer reduces optimizer state memory by storing Adam optimizer states in 8-bit precision instead of 32-bit. This can cut optimizer memory usage by up to 75%. Use the `bitsandbytes` library to enable it. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
import torch
from transformers import TrainingArguments, Trainer
from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained(
    "bert-base-uncased",
    load_in_8bit=True,  # Load model in 8-bit
    device_map="auto",
)
```

## Memory Cleanup

### Clear GPU Memory Before Training

Residual GPU memory allocations from previous operations can reduce available memory at the start of training. Use `numba.cuda` to reset the GPU device before beginning training: ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
from numba import cuda

device = cuda.get_current_device()
device.reset()
```

## Diagnostic Tools

### Run on CPU for Comparison

If a CUDA kernel error occurs alongside the OOM, run the training on CPU to determine whether the error is specific to GPU execution or stems from the model or data pipeline. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
# Force CPU execution for testing
training_args = TrainingArguments(
    output_dir="./results",
    no_cuda=True,
)
```

### Enable Synchronous CUDA Execution

CUDA kernel errors are often reported asynchronously, making stack traces misleading. Set the environment variable `CUDA_LAUNCH_BLOCKING=1` to force synchronous execution and obtain accurate error locations: ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
import os
os.environ["CUDA_LAUNCH_BLOCKING"] = "1"
```

## Systemic Mitigations

### Choose a Smaller Model Variant

If the above adjustments do not resolve the OOM error, consider using a smaller model variant (e.g., `distilbert-base-uncased` instead of `bert-base-uncased`, or `bert-base-uncased` instead of `bert-large-uncased`). Smaller models require less memory for activations and parameters.

### Upgrade to a Multi-GPU Configuration

For workloads that exceed single-GPU capacity, consider scaling to a multi-GPU cluster and using data parallelism or model parallelism strategies. See Distributed Training with Hugging Face and [Multi-GPU Training on Databricks](/concepts/multi-gpu-distributed-training-on-databricks.md).

## Related Concepts

- [Hugging Face Trainer](/concepts/hugging-face-trainer.md) — The training utility handling memory management
- [TrainingArguments](/concepts/trainingarguments-configuration.md) — Configuration class for batch size, precision, and accumulation
- Mixed-Precision Training — Using FP16 to reduce memory footprint
- [Gradient Accumulation](/concepts/gradient-accumulation-fusion.md) — Technique to simulate larger batches with less memory
- 8-bit Optimizers — Memory-efficient optimizer implementations
- GPU Memory Management in PyTorch — Understanding allocation and fragmentation

## Sources

- fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md

# Citations

1. [fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md](/references/fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws-e2c49846.md)
