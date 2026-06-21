---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 479db180ecf59ad90bfa42d6dd9b78b17ca383ccd605d9ad26dfbacc97de53fb
  pageDirectory: concepts
  sources:
    - finetune-llama-32-3b-with-unsloth-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - supervised-fine-tuning-sft-with-sfttrainer
    - SF(WS
  citations:
    - file: finetune-llama-32-3b-with-unsloth-databricks-on-aws.md
title: Supervised Fine-Tuning (SFT) with SFTTrainer
description: Training paradigm using the TRL library's SFTTrainer to fine-tune language models on instruction-following datasets, with configurable hyperparameters and MLflow tracking.
tags:
  - machine-learning
  - fine-tuning
  - training
timestamp: "2026-06-19T10:35:59.008Z"
---

# Supervised Fine-Tuning (SFT) with SFTTrainer

**Supervised Fine-Tuning (SFT) with SFTTrainer** refers to a common approach for adapting a pre-trained large language model (LLM) to a specific task using labeled conversational data. The `SFTTrainer` class from the [trl](https://huggingface.co/docs/trl) library provides a streamlined training loop for supervised fine-tuning, often combined with parameter-efficient methods like LoRA to reduce memory and compute requirements. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Typical Workflow

### 1. Load the Base Model

The model is first loaded using the [Unsloth](/concepts/unsloth.md) library's `FastLanguageModel.from_pretrained()`, which automatically configures data type (e.g., bfloat16 on Ampere GPUs) and sequence length. This step may also use 4-bit quantization to further reduce memory usage. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

```python
from unsloth import FastLanguageModel
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/Llama-3.2-3B-Instruct",
    max_seq_length=2048,
    dtype=None,  # auto-detect
    load_in_4bit=False,
)
```

### 2. Apply LoRA Adapters

LoRA (Low-Rank Adaptation) adapters are added to the attention and feed-forward layers via `FastLanguageModel.get_peft_model()`. This creates a PEFT model where only a small fraction of parameters are trainable. Typical `r` (rank) values are 8, 16, 32, 64, or 128. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

```python
model = FastLanguageModel.get_peft_model(
    model,
    r=16,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                     "gate_proj", "up_proj", "down_proj"],
    lora_alpha=16,
    lora_dropout=0,        # 0 is optimized
    bias="none",
    use_gradient_checkpointing="unsloth",  # saves 30% VRAM
    random_state=3407,
)
```

### 3. Prepare the Dataset

The training dataset (e.g., [FineTome-100k](https://huggingface.co/datasets/mlabonne/FineTome-100k)) is formatted using a chat template. The template is applied with `tokenizer.apply_chat_template()` to convert conversational turns into text sequences. The `standardize_sharegpt` helper normalizes ShareGPT-style data. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

```python
from unsloth.chat_templates import get_chat_template, standardize_sharegpt
tokenizer = get_chat_template(tokenizer, chat_template="llama-3.1")

dataset = load_dataset("mlabonne/FineTome-100k", split="train")
dataset = standardize_sharegpt(dataset)
dataset = dataset.map(formatting_prompts_func, batched=True)
```

### 4. Configure SFTTrainer

The `SFTTrainer` is configured with the model, tokenizer, dataset, and a `TrainingArguments` object. Key hyperparameters include batch size, learning rate, optimizer (`adamw_8bit`), and step count. For short sequences, packing can be enabled for up to 5× speedup. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

```python
from trl import SFTTrainer
from transformers import TrainingArguments, DataCollatorForSeq2Seq

trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=dataset,
    dataset_text_field="text",
    max_seq_length=2048,
    data_collator=DataCollatorForSeq2Seq(tokenizer=tokenizer),
    packing=False,
    args=TrainingArguments(
        per_device_train_batch_size=2,
        gradient_accumulation_steps=4,
        warmup_steps=5,
        max_steps=25,               # or num_train_epochs=1
        learning_rate=2e-4,
        fp16=not is_bfloat16_supported(),
        bf16=is_bfloat16_supported(),
        logging_steps=1,
        optim="adamw_8bit",
        weight_decay=0.01,
        lr_scheduler_type="linear",
        seed=3407,
        output_dir=OUTPUT_DIR,
        report_to="mlflow",
    ),
)
```

### 5. Apply Response-Only Training

To prevent the model from learning to predict user prompts, the `train_on_responses_only` function masks the instruction part of each conversation, so the loss is computed only on assistant responses. The instruction and response markers are provided as string delimiters. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

```python
from unsloth.chat_templates import train_on_responses_only

trainer = train_on_responses_only(
    trainer,
    instruction_part="<|start_header_id|>user<|end_header_id|>\n\n",
    response_part="<|start_header_id|>assistant<|end_header_id|>\n\n",
    num_proc=1,
)
```

### 6. Execute Training

Training is run inside an [MLflow](/concepts/mlflow.md) run to automatically log training metrics (loss, learning rate) and system metrics (GPU utilization, memory). ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

```python
with mlflow.start_run(run_name='finetune-llama-3.2-3b-unsloth',
                      log_system_metrics=True):
    trainer.train()
```

### 7. Merge and Register the Model

After training, the LoRA adapter weights are merged with the base model using `model.merge_and_unload()`. The merged model is logged to MLflow and registered in [Unity Catalog](/concepts/unity-catalog.md) under a three‑level namespace (`catalog.schema.model_name`) with the `llm/v1/chat` task type, making it ready for deployment to [Model Serving](/concepts/model-serving.md) endpoints. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

```python
merged_model = model.merge_and_unload()
model_info = mlflow.transformers.log_model(
    transformers_model={'model': merged_model, 'tokenizer': tokenizer},
    registered_model_name=f"{UC_CATALOG}.{UC_SCHEMA}.{UC_MODEL_NAME}",
    task='llm/v1/chat',
)
```

## Requirements

- **GPU compute** with an A10 accelerator (serverless GPU) is recommended. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]
- **AI v5 runtime** (Databricks) which bundles Unsloth, `trl`, `bitsandbytes`, `xformers`, and `mlflow`. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]
- A **Unity Catalog volume** for saving checkpoints during training. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Related Concepts

- [Unsloth](/concepts/unsloth.md) – Optimized implementations for faster fine-tuning with reduced memory.
- LoRA – Low-Rank Adaptation, the parameter‑efficient technique used.
- PEFT – Parameter‑Efficient Fine‑Tuning, the paradigm that LoRA belongs to.
- [TRL (Transformer Reinforcement Learning)](/concepts/trl-transformer-reinforcement-learning.md) – Library that provides `SFTTrainer`.
- [MLflow](/concepts/mlflow.md) – Experiment tracking and model registry.
- [Unity Catalog](/concepts/unity-catalog.md) – Model storage and governance.
- Chat Template – Formatting conversational data for instruction‑tuned models.
- [Response-Only Training](/concepts/response-only-training.md) – Loss masking to ignore user instructions during fine‑tuning.
- [FineTome-100k](/concepts/finetome-100k-dataset.md) – Example dataset for supervised fine‑tuning.
- [Model Serving](/concepts/model-serving.md) – Deploying the fine‑tuned model for inference.

## Sources

- finetune-llama-32-3b-with-unsloth-databricks-on-aws.md

# Citations

1. [finetune-llama-32-3b-with-unsloth-databricks-on-aws.md](/references/finetune-llama-32-3b-with-unsloth-databricks-on-aws-83073ff0.md)
