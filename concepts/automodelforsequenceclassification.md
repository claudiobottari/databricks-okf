---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6756742e7d25b5dbaaab3026438b3d829fc1f02e1a8ec254624b57a4b72b1e61
  pageDirectory: concepts
  sources:
    - fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automodelforsequenceclassification
    - AutoModelForTokenClassification
  citations:
    - file: fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
title: AutoModelForSequenceClassification
description: A Hugging Face Auto Model class that loads a pre-trained transformer model with a classification head for text classification fine-tuning.
tags:
  - huggingface
  - nlp
  - model-loading
timestamp: "2026-06-19T10:32:22.707Z"
---

## AutoModelForSequenceClassification

**AutoModelForSequenceClassification** is a Hugging Face Transformers class used to load a pretrained model for text classification tasks. It is one of the [Auto Model classes for NLP](https://huggingface.co/docs/transformers/v4.26.1/en/model_doc/auto#natural-language-processing) that provide a convenient interface for fine-tuning and inference. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### Overview

The class is designed to simplify the process of adapting a base transformer model for sequence classification, such as sentiment analysis, topic labeling, or any task that assigns a discrete label to a text sequence. It automatically selects the correct model architecture based on the pretrained checkpoint name. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### Usage

To create an instance for fine-tuning, provide the base model identifier along with the number of target labels and optional label mappings: ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained(
    base_model,
    num_labels=len(label2id),
    label2id=label2id,
    id2label=id2label
)
```

- `num_labels` must match the number of classes in your dataset.
- `label2id` and `id2label` are dictionaries that map label names to integer IDs and vice versa, typically prepared during [dataset preparation for fine-tuning](/concepts/data-preparation-for-llm-fine-tuning-with-hugging-face.md).

### Training Integration

`AutoModelForSequenceClassification` is used with the Hugging Face Trainer utility. After constructing the model, you configure a [TrainingArguments](/concepts/trainingarguments-configuration.md) object and create a Trainer instance that handles the training loop, evaluation, and metric computation. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

Once training is complete, the fine-tuned model can be saved and reloaded to build a text classification pipeline: ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

```python
from transformers import pipeline

pipe = pipeline(
    "text-classification",
    model=AutoModelForSequenceClassification.from_pretrained(model_output_dir),
    tokenizer=tokenizer,
    batch_size=1
)
```

This pipeline can then be logged to [MLflow](/concepts/mlflow.md) using `mlflow.transformers.log_model()` for [model governance](/concepts/ai-governance.md) and serving. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### Related Concepts

- Hugging Face Transformers – the library that provides AutoModelForSequenceClassification.
- [AutoTokenizer](/concepts/autotokenizer-for-transformers.md) – used to tokenize input text before feeding it to the model.
- Trainer – the training utility that orchestrates fine-tuning.
- [TrainingArguments](/concepts/trainingarguments-configuration.md) – configuration for training hyperparameters.
- [DataCollatorWithPadding](/concepts/datacollatorwithpadding.md) – collates and pads batches for the model.
- [MLflow Transformers Integration](/concepts/mlflow-transformers-flavor.md) – logs and serves Hugging Face models via MLflow.
- Fine-tuning on a Single GPU – guidance for running such training on Databricks.

### Sources

- fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md

# Citations

1. [fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md](/references/fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws-e2c49846.md)
