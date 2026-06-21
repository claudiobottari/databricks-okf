---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e181ff8b3acc0877a62ec4478b941b13f36f85304ab94094299dbf9f0bdaecb4
  pageDirectory: concepts
  sources:
    - distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sfttrainer-with-chat-template-processing
    - SWCTP
  citations:
    - file: distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
title: SFTTrainer with Chat Template Processing
description: The use of TRL's SFTTrainer with Unsloth's chat template utilities (get_chat_template, standardize_sharegpt, train_on_responses_only) for supervised finetuning on conversational datasets like mlabonne/FineTome-100k.
tags:
  - trl
  - training
  - data-processing
timestamp: "2026-06-19T18:33:40.147Z"
---

# SFTTrainer with Chat Template Processing

The **SFTTrainer with Chat Template Processing** technique combines the [SFTTrainer](/concepts/sfttrainer.md) from the TRL library with explicit chat template handling to perform supervised fine-tuning (SFT) of instruction-tuned language models. It is a central pattern in the notebook that demonstrates distributed fine-tuning of Llama-3.2-3B using [Unsloth](/concepts/unsloth.md) on 8 H100 GPUs.

## Overview

In this pattern, a base model is loaded and prepared for parameter-efficient fine-tuning with **LoRA**. The dataset is formatted according to a specific chat template (e.g., `llama-3.1`) so that the model sees conversations in the expected structure. The SFTTrainer then trains on the tokenized text, and a post-processing step masks the user/instruction portion so the model learns only from the assistant responses. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Key Steps

### 1. Load the Model and Tokenizer

The model is loaded with Unsloth’s `FastLanguageModel.from_pretrained`, optionally with 4-bit quantization and a per‑device map. The tokenizer is loaded at the same time.

### 2. Apply a Chat Template

A tokenizer chat template is set using `get_chat_template` from Unsloth’s `chat_templates` module. This configures the tokenizer to use the `llama-3.1` template, which matches the model’s expected conversation format.

```python
from unsloth.chat_templates import get_chat_template

tokenizer = get_chat_template(
    tokenizer,
    chat_template="llama-3.1",
)
```

^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### 3. Format the Dataset

A `formatting_prompts_func` applies the chat template to each conversation in the dataset using `tokenizer.apply_chat_template`. The function returns a `text` field containing the serialized conversation string.

```python
def formatting_prompts_func(examples):
    convos = examples["conversations"]
    texts = [
        tokenizer.apply_chat_template(convo,
                                       tokenize=False,
                                       add_generation_prompt=False)
        for convo in convos
    ]
    return { "text": texts, }
```

The dataset is then standardised with `standardize_sharegpt` and mapped with the formatting function. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### 4. Configure the SFTTrainer

The SFTTrainer is created with the model, tokenizer, formatted dataset, and training arguments. It uses the `dataset_text_field="text"` to know which column contains the pre‑formatted chat‑template text. Other parameters include `max_seq_length`, a `DataCollatorForSeq2Seq`, and `packing=False`.

```python
trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=dataset,
    dataset_text_field="text",
    max_seq_length=max_seq_length,
    data_collator=DataCollatorForSeq2Seq(tokenizer=tokenizer),
    dataset_num_proc=6,
    packing=False,
    args=TrainingArguments(...),
)
```

^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### 5. Mask the Instruction Portion

After constructing the trainer, the helper `train_on_responses_only` from Unsloth’s chat templates is applied. It sets the loss to zero for tokens that belong to the instruction (user) part, so the model learns to predict only the assistant response.

```python
trainer = train_on_responses_only(
    trainer,
    instruction_part="<|start_header_id|>user<|end_header_id|>\n\n",
    response_part="<|start_header_id|>assistant<|end_header_id|>\n\n",
    num_proc=1,
)
```

^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### 6. Train and Save

The trainer is run with `trainer.train()`. On the global rank 0, the model and tokenizer are saved to a Unity Catalog volume. The run is tracked via [MLflow](/concepts/mlflow.md). ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Integration with Distributed Training

The entire training function is decorated with `@distributed(gpus=8, gpu_type='h100')` from the `serverless_gpu` library. This runs the SFTTrainer process on each GPU, with `LOCAL_RANK` used to set the device and `rt.get_global_rank()` to coordinate saving. The chat template processing steps are identical across all ranks. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Advantages of Explicit Chat Template Processing

- **Consistency**: Ensures every training example is formatted identically to the model’s intended chat format.
- **Masking**: The `train_on_responses_only` step prevents the model from wasting capacity on predicting the instruction part, focusing learning on the desired assistant output.
- **Reusability**: The same template and masking logic can be applied to any dataset that follows the ShareGPT conversation schema.

## Related Concepts

- [SFTTrainer](/concepts/sfttrainer.md) – The main training class from TRL used for supervised fine-tuning.
- [Unsloth](/concepts/unsloth.md) – Library providing optimized model loading and chat template utilities.
- Chat Templates – Standardized conversation formats for instruction-tuned models.
- [Supervised Fine-Tuning](/concepts/supervised-fine-tuning-sft.md) – The broader technique of training a pretrained model on labeled instruction data.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – Scaling the training across multiple GPUs using the `@distributed` decorator.
- LoRA – Parameter-efficient fine-tuning method used in the notebook.
- [MLflow](/concepts/mlflow.md) – Used for experiment tracking and model registry.

## Sources

- distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md

# Citations

1. [distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md](/references/distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws-5c6e3457.md)
