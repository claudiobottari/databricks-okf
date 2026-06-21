---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8d7b46baae41a6e96eed20953e6f77cb66e26a35b903ad9d14b91498a04db978
  pageDirectory: concepts
  sources:
    - fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - training-configuration-with-hugging-face-trainingarguments
    - TCWHFT
  citations:
    - file: fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
title: Training Configuration with Hugging Face TrainingArguments
description: Setting up TrainingArguments including batch size, precision, evaluation strategy, and gradient accumulation for single-GPU fine-tuning
tags:
  - hugging-face
  - training
  - configuration
timestamp: "2026-06-18T12:20:31.063Z"
---

---
title: Training Configuration with Hugging Face TrainingArguments
summary: How to configure training for Hugging Face models using the `TrainingArguments` class, including key parameters for single-GPU fine-tuning.
sources:
  - fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:13:02.271Z"
updatedAt: "2026-06-18T11:13:02.271Z"
tags:
  - hugging-face
  - training
  - transformers
  - fine-tuning
aliases:
  - training-arguments-huggingface
  - TAHF
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Training Configuration with Hugging Face TrainingArguments

**TrainingArguments** is the class in the Hugging Face `transformers` library that holds all training hyperparameters for the [Hugging Face Trainer](/concepts/hugging-face-trainer.md). It replaces the need to manually pass many arguments when creating a trainer, and it provides a structured way to control output directories, evaluation strategy, batch sizes, precision, and other training settings. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Basic Usage

To create a `TrainingArguments` instance, you must specify at least the `output_dir` argument, which defines where the trained model and checkpoints are saved. Additional parameters control the evaluation strategy, learning rate, and other aspects of the training loop. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
from transformers import TrainingArguments, Trainer

training_args = TrainingArguments(
    output_dir=training_output_dir,
    evaluation_strategy="epoch"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_test_dataset["train"],
    eval_dataset=train_test_dataset["test"],
    compute_metrics=compute_metrics,
    data_collator=data_collator,
)
```

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Key Parameters

### Output and Evaluation

- **`output_dir`** (required): Path to the directory where training outputs (checkpoints, logs) will be saved.
- **`evaluation_strategy`**: Determines when evaluation is performed. Common values include `"no"`, `"steps"`, `"epoch"`, and `"steps"`. Setting `"epoch"` evaluates after every epoch. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### Batch Size and Memory

- **`per_device_train_batch_size`**: Batch size per GPU during training. Lowering this value can help resolve CUDA out of memory errors when training large models on a single GPU.
- **`per_device_eval_batch_size`**: Batch size per GPU for evaluation.
- **`gradient_accumulation_steps`**: Number of steps to accumulate gradients before performing a backward/update pass. Increasing this value effectively increases the total batch size without requiring more GPU memory. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### Precision and Optimization

- **`fp16`**: Set to `True` to enable mixed-precision training (FP16), which reduces memory usage and can speed up training on GPUs that support it. This is recommended when encountering out-of-memory errors.
- **`learning_rate`**: The initial learning rate for the optimizer.
- **`adam_beta1`, `adam_beta2`, `adam_epsilon`**: Parameters for the Adam optimizer.
- **`weight_decay`**: Weight decay to apply (if not `None`). ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### Logging and Saving

- **`logging_dir`**: Directory for TensorBoard logs. Defaults to `runs/`.
- **`logging_steps`**: Log every N steps.
- **`save_strategy`**: When to save checkpoints. Options include `"no"`, `"steps"`, and `"epoch"`.
- **`save_steps`**: Save a checkpoint every N steps.
- **`save_total_limit`**: Maximum number of checkpoints to keep. Older checkpoints are deleted. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Using Data Collators

A [data collator](/concepts/datacollatorwithpadding.md) is used to batch input data during training and evaluation. `TrainingArguments` does not define the collator; it is passed separately to the `Trainer`. The `DataCollatorWithPadding` class provides a good baseline for text classification tasks. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
from transformers import DataCollatorWithPadding

data_collator = DataCollatorWithPadding(tokenizer)
```

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Integration with MLflow

When training within an [MLflow](/concepts/mlflow.md) run, the Hugging Face `Trainer` automatically logs metrics via the `MLflowCallback`. You do not need to configure any special `TrainingArguments` for this; it works out-of-the-box. However, you must log the trained model manually using `mlflow.transformers.log_model()`. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Troubleshooting CUDA Errors

### Out of Memory

Reduce memory usage by adjusting the following `TrainingArguments` parameters:

- **Decrease** `per_device_train_batch_size`.
- **Enable** `fp16=True`.
- **Increase** `gradient_accumulation_steps` to compensate for the smaller batch size.
- **Use** the 8-bit Adam optimizer (not set via `TrainingArguments` alone — requires loading the `bitsandbytes` integration).

These adjustments are the primary levers to resolve CUDA out of memory errors during single-GPU fine-tuning. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### Kernel Errors

If CUDA kernel errors occur, set the environment variable `CUDA_LAUNCH_BLOCKING=1` to get an accurate stack trace. Alternatively, run the code on CPU first to check reproducibility. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Related Concepts

- [Hugging Face Trainer](/concepts/hugging-face-trainer.md) — The class that uses `TrainingArguments` to run the training loop.
- [Fine-tuning Hugging Face Models](/concepts/single-gpu-fine-tuning-with-hugging-face-on-databricks.md) — End-to-end workflow for adapting pretrained models to custom tasks.
- Data Collator — Batching strategy for tokenized inputs.
- [MLflow](/concepts/mlflow.md) — Experiment tracking and model registry used alongside Hugging Face.
- Hugging Face Datasets — Loading and tokenizing data for training.
- Hugging Face Auto Model — Classes that automatically load pretrained model architectures.

## Sources

- fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md

# Citations

1. [fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md](/references/fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws-e2c49846.md)
