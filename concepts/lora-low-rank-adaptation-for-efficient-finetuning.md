---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 30c49e2fe7e6fe7d3f01baa316825180377ca56ef257683e18ecddb997f3fb4c
  pageDirectory: concepts
  sources:
    - distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lora-low-rank-adaptation-for-efficient-finetuning
    - L(AFEF
  citations:
    - file: distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
title: LoRA (Low-Rank Adaptation) for Efficient Finetuning
description: Parameter-efficient fine-tuning technique that adapts pre-trained models by training low-rank matrices targeting specific attention modules (q_proj, k_proj, v_proj, etc.), reducing memory footprint.
tags:
  - machine-learning
  - fine-tuning
  - parameter-efficiency
  - lora
timestamp: "2026-06-18T15:30:18.724Z"
---

---

title: LoRA (Low-Rank Adaptation) for Efficient Fine‑tuning
summary: LoRA (Low-Rank Adaptation) is a parameter‑efficient fine‑tuning technique that trains low‑rank decomposition matrices for selected layers, drastically reducing the number of trainable parameters while preserving model quality.
sources:
  - distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T16:00:00.000Z"
updatedAt: "2026-06-18T16:00:00.000Z"
tags:
  - fine-tuning
  - parameter-efficient
  - lora
  - peft
aliases:
  - lora-low-rank-adaptation-for-efficient-finetuning
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0

---

# LoRA (Low-Rank Adaptation) for Efficient Fine‑tuning

**LoRA (Low-Rank Adaptation)** is a parameter‑efficient fine‑tuning method that reduces the number of trainable parameters by inserting low‑rank decomposition matrices into selected layers of a pre‑trained model. This makes fine‑tuning large models feasible on limited hardware and accelerates training.

## Overview

LoRA works by freezing the original model weights and adding small, trainable rank‑decomposition matrices to certain layers—typically attention projections in transformer models. During fine‑tuning, only these small matrices are updated, which dramatically cuts memory and compute requirements. The notebook on fine‑tuning Llama‑3.2‑3B demonstrates the use of LoRA via the Unsloth library, which provides an optimized implementation. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## LoRA Parameters

When configuring LoRA with PEFT (Parameter‑Efficient Fine‑Tuning), the key hyperparameters are:

| Parameter | Example Value | Description |
|-----------|---------------|-------------|
| `r`       | `16`          | Rank of the low‑rank matrices. Higher values increase expressiveness but also parameter count. |
| `lora_alpha` | `16`       | Scaling factor applied to the LoRA residuals. |
| `lora_dropout` | `0`        | Dropout rate applied to LoRA layers. A value of `0` is often optimal. |
| `bias`       | `"none"`    | Whether to train bias parameters. `"none"` is most efficient. |
| `target_modules` | `["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]` | Attention and feed‑forward projection layers in the transformer. |

^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

The notebook also uses `use_rslora=False` (rank‑stabilized LoRA extension) and `loftq_config=None` (LoFTQ quantization). ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Usage in Unsloth

[Unsloth](/concepts/unsloth.md) provides a `FastLanguageModel` wrapper that integrates seamlessly with LoRA. The typical workflow:

1. Load the base model and tokenizer with `FastLanguageModel.from_pretrained()`.
2. Convert the model to a PEFT model with `FastLanguageModel.get_peft_model()`, specifying the LoRA hyperparameters.
3. Enable gradient checkpointing (with `use_reentrant=False` when using [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)) to further reduce memory.
4. Train with the [SFTTrainer](/concepts/sfttrainer.md) from the `trl` library.

```python
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name=MODEL_NAME,
    max_seq_length=2048,
    dtype=None,
    load_in_4bit=False,
    device_map={'': local_rank},
)
model = FastLanguageModel.get_peft_model(
    model,
    r=16,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                    "gate_proj", "up_proj", "down_proj"],
    lora_alpha=16,
    lora_dropout=0,
    bias="none",
    use_gradient_checkpointing=True,
    random_state=3407,
    use_rslora=False,
    loftq_config=None,
)
```

^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Saving and Merging LoRA Adapters

After training, the LoRA adapter weights (small matrices) are saved separately from the base model. To make inference faster and simpler, the adapter can be merged into the base model:

```python
peft_model = PeftModel.from_pretrained(base_model, adapter_dir)
merged_model = peft_model.merge_and_unload()
```

The merged model contains the original weights updated by the LoRA adjustments. The notebook logs the merged model to [MLflow](/concepts/mlflow.md) and registers it in [Unity Catalog](/concepts/unity-catalog.md). ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Related Concepts

- PEFT – General framework for parameter‑efficient fine‑tuning.
- [SFTTrainer](/concepts/sfttrainer.md) – Supervised fine‑tuning trainer from Hugging Face’s `trl` library.
- [Unsloth](/concepts/unsloth.md) – Optimized training library with LoRA support.
- [Quantization](/concepts/mxfp4-quantization.md) – Used together with LoRA to further reduce memory.
- [Gradient Checkpointing](/concepts/activation-checkpointing.md) – Memory‑saving technique often combined with LoRA.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – Approach for multi‑GPU training with LoRA.
- [MLflow](/concepts/mlflow.md) – Experiment tracking and model registry.

## Sources

- distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md

# Citations

1. [distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md](/references/distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws-5c6e3457.md)
