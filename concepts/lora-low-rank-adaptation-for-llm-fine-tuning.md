---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d1cd0cb372bae2d38ddd7754785ffbc769cdf8ec1c2ae9e45ec5b4daa7f922d6
  pageDirectory: concepts
  sources:
    - distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lora-low-rank-adaptation-for-llm-fine-tuning
    - L(AFLF
  citations:
    - file: distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
title: LoRA (Low-Rank Adaptation) for LLM fine-tuning
description: Parameter-efficient fine-tuning technique that trains small adapter layers while freezing the base model to reduce compute and memory requirements.
tags:
  - fine-tuning
  - parameter-efficient
  - machine-learning
timestamp: "2026-06-19T10:15:00.993Z"
---

# LoRA (Low-Rank Adaptation) for LLM Fine-Tuning

**LoRA (Low-Rank Adaptation)** is a parameter-efficient fine-tuning method that trains small adapter layers while freezing the base model’s weights. It is particularly useful for fine‑tuning large language models (LLMs) with billions of parameters, such as OpenAI’s gpt‑oss‑20b, because it drastically reduces the number of trainable parameters and the associated memory footprint. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## How LoRA Works

Instead of updating all model parameters during fine‑tuning, LoRA injects low‑rank decomposition matrices into specific layers of the Base model. The original weights remain frozen, and only the small adapter parameters are trained. This makes the fine‑tuning process both computationally and memory efficient. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

The technique was introduced in the paper *LoRA: Low‑Rank Adaptation of Large Language Models* (arXiv:2106.09685). ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## Configuration

A typical LoRA configuration is defined using the `LoraConfig` class from the PEFT library. The example below shows the settings used in a 20B‑parameter fine‑tuning run:

```python
from peft import LoraConfig, get_peft_model

peft_config = LoraConfig(
    r=8,                    # rank of the low-rank matrices
    lora_alpha=16,          # scaling factor
    target_modules="all-linear",  # apply LoRA to all linear layers
    lora_dropout=0.05,      # dropout probability
    bias="none",            # do not train bias parameters
    task_type="CAUSAL_LM",  # task: causal language modeling
)
```

^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

Key parameters:
- **r** – The rank of the low‑rank matrices. A smaller `r` means fewer trainable parameters.
- **lora_alpha** – The scaling factor for the adapter updates.
- **target_modules** – Which layers to adapt. `"all-linear"` applies LoRA to every linear layer.
- **lora_dropout** – Dropout applied to the adapter layers for regularisation.
- **bias** – Whether to train bias terms. `"none"` keeps all biases frozen.

## Training with LoRA

To train a model with LoRA, you first instantiate the base model (e.g., `AutoModelForCausalLM`) and then wrap it with `get_peft_model` using the `LoraConfig`. The resulting PEFT model has most parameters frozen; only the LoRA adapters are updated during training. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

The training can be combined with other memory‑saving techniques such as [MXFP4 Quantization](/concepts/mxfp4-quantization.md) (microscaling 4‑bit floating point) and gradient checkpointing. In the provided example, the fine‑tuning is distributed across 8 H100 GPUs using [Distributed Data Parallel](/concepts/distributed-data-parallel-ddp.md) handled by the `@distributed` decorator from `serverless_gpu`. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

After training, the LoRA adapter weights are saved separately. The checkpoint directory contains the adapter files, which can later be loaded alongside the base model. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## Inference with LoRA

For inference, you have two options:
- **Keep LoRA adapters separate**: Load the base model and then apply the adapter using `PeftModel.from_pretrained()`. This allows you to use the adapter for generation without merging.
- **Merge adapters into the base model**: Call `peft_model.merge_and_unload()` to produce a single model that includes the adapter updates. This merged model can be used in a pipeline without the PEFT wrapper. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

The following example loads a fine‑tuned LoRA adapter, merges it, and then creates a text‑generation pipeline:

```python
from peft import PeftModel

base_model = AutoModelForCausalLM.from_pretrained(HF_MODEL_NAME)
peft_model = PeftModel.from_pretrained(base_model, adapter_dir)
merged_model = peft_model.merge_and_unload()

text_gen_pipe = pipeline(
    task="text-generation",
    model=peft_model,      # or merged_model, depending on preference
    tokenizer=tokenizer,
)
```

^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## Model Registration and Deployment

After fine‑tuning, the model can be logged to [MLflow](/concepts/mlflow.md) and registered in [Unity Catalog](/concepts/unity-catalog.md) for deployment. The notebook wraps the pipeline in `mlflow.transformers.log_model()` and specifies a Unity Catalog path. Once registered, the model is available for serving and inference through Databricks Model Serving. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## Related Concepts

- [Parameter‑efficient fine‑tuning](/concepts/parameter-efficient-fine-tuning-peft.md)
- PEFT library
- [MXFP4 Quantization](/concepts/mxfp4-quantization.md)
- [Distributed training](/concepts/workload-yaml-for-distributed-training.md)
- [MLflow](/concepts/mlflow.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Model Serving](/concepts/model-serving.md)
- [[gpt-oss-20b]]

## Sources

- distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md

# Citations

1. [distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md](/references/distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws-7ee24e1a.md)
