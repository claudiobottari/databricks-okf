---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bd679e0d20caac9d4fd41449b8aaf1e4f0a4dd09ce321a0d2e0ec9ee9502f6fd
  pageDirectory: concepts
  sources:
    - fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automodel-and-autotokenizer-for-fine-tuning
    - AutoTokenizer for Fine-tuning and AutoModel
    - AAAFF
  citations:
    - file: fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
title: AutoModel and AutoTokenizer for Fine-tuning
description: Using Hugging Face AutoModelForSequenceClassification and AutoTokenizer to load pre-trained models and tokenize data for fine-tuning tasks.
tags:
  - huggingface
  - nlp
  - tokenization
timestamp: "2026-06-19T18:49:49.945Z"
---

# AutoModel and AutoTokenizer for Fine-tuning

**AutoModel** and **AutoTokenizer** are utility classes from the Hugging Face `transformers` library that automatically instantiate the appropriate model architecture and tokenizer based on a pretrained model name or path. They are essential components for fine-tuning Hugging Face models, enabling users to load and prepare models for downstream tasks without manually specifying the architecture class. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Overview

The Hugging Face `transformers` library provides [Auto Model](https://huggingface.co/docs/transformers/model_doc/auto) classes and the [AutoTokenizer](https://huggingface.co/docs/transformers/v4.26.1/en/autoclass_tutorial#autotokenizer) that enable loading and fine-tuning Transformers models. These tools are available for tasks including text classification, sequence labeling, question answering, and more. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## AutoTokenizer

Tokenization is a critical preprocessing step because Hugging Face Transformers models expect tokenized input rather than raw text. The `AutoTokenizer` class automatically loads the correct tokenizer for a given base model, ensuring compatibility between the tokenization scheme and the model's expected input format. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### Usage

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(base_model)

def tokenize_function(examples):
    return tokenizer(examples["text"], padding=False, truncation=True)

train_test_tokenized = train_test_dataset.map(tokenize_function, batched=True)
```

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### Key Parameters

- `padding=False`: Disables padding during tokenization. Padding is typically handled later by a DataCollator for efficient batching.
- `truncation=True`: Truncates examples that exceed the model's maximum input length.

When using Hugging Face `datasets`, you can apply the tokenizer consistently to both training and testing data using the `.map()` method with `batched=True`. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## AutoModel Classes

AutoModel provides specialized subclasses for different NLP tasks. These classes automatically load the correct architecture based on the pretrained model identifier. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### AutoModelForSequenceClassification

For text classification tasks, use `AutoModelForSequenceClassification`. When creating the model, you must provide the number of classes and label mappings. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained(
    base_model,
    num_labels=len(label2id),
    label2id=label2id,
    id2label=id2label
)
```

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### Available Auto Model Subclasses

The Auto Model classes for NLP include specialized versions for various tasks:
- [AutoModelForSequenceClassification](/concepts/automodelforsequenceclassification.md) — Text classification
- AutoModelForTokenClassification — Named entity recognition and token-level tasks
- AutoModelForQuestionAnswering — Extractive question answering
- AutoModelForCausalLM — Causal language modeling
- AutoModelForMaskedLM — Masked language modeling

## Integration with Trainer

AutoModel and AutoTokenizer integrate directly with the Hugging Face Trainer utility. After loading the model and tokenizer, you configure training parameters and create a Trainer instance: ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
from transformers import TrainingArguments, Trainer, DataCollatorWithPadding

training_args = TrainingArguments(
    output_dir=training_output_dir,
    evaluation_strategy="epoch"
)

data_collator = DataCollatorWithPadding(tokenizer)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_test_dataset["train"],
    eval_dataset=train_test_dataset["test"],
    compute_metrics=compute_metrics,
    data_collator=data_collator,
)
```

## MLflow Integration

After training, models loaded via AutoModel can be logged to [MLflow](/concepts/mlflow.md) for versioning and deployment. The `mlflow.transformers.log_model()` function accepts either a pipeline object or a dictionary containing the model and tokenizer: ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
import mlflow
from transformers import pipeline

with mlflow.start_run() as run:
    trainer.train()
    trainer.save_model(model_output_dir)
    
    pipe = pipeline(
        "text-classification",
        model=AutoModelForSequenceClassification.from_pretrained(model_output_dir),
        batch_size=1,
        tokenizer=tokenizer
    )
    
    model_info = mlflow.transformers.log_model(
        transformers_model=pipe,
        artifact_path="classification",
        input_example="Hi there!",
    )
```

Alternatively, submit components directly: ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
model_info = mlflow.transformers.log_model(
    transformers_model={"model": trainer.model, "tokenizer": tokenizer},
    task="text-classification",
    artifact_path="text_classifier",
    input_example=["MLflow is great!", "MLflow on Databricks is awesome!"],
)
```

## Best Practices

- Always use `AutoTokenizer.from_pretrained()` with the same base model name used for the AutoModel to ensure tokenizer compatibility. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]
- When fine-tuning, set `padding=False` during tokenization and use [DataCollatorWithPadding](/concepts/datacollatorwithpadding.md) for dynamic padding during batching. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]
- Use `truncation=True` to handle variable-length inputs that exceed the model's context window. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Related Concepts

- Hugging Face Transformers
- Tokenization
- Fine-tuning
- Trainer Utility
- Data Collator
- [MLflow Tracking](/concepts/mlflow-tracking.md)

## Sources

- fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md

# Citations

1. [fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md](/references/fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws-e2c49846.md)
