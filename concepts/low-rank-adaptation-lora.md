---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: af98ee3e7db15fb20431b13320abd52116e3ff6ccdb543bc7a7bdaec00ce4be2
  pageDirectory: concepts
  sources:
    - finetune-llama-32-3b-with-unsloth-databricks-on-aws.md
    - large-language-models-llms-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - low-rank-adaptation-lora
    - LA(
    - LoRA Adapter
  citations:
    - file: large-language-models-llms-databricks-on-aws.md
    - file: finetune-llama-32-3b-with-unsloth-databricks-on-aws.md
title: Low-Rank Adaptation (LoRA)
description: A parameter-efficient fine-tuning technique that adds small, trainable rank-decomposition matrices to attention and feed-forward layers while keeping the base model frozen, reducing memory and compute requirements.
tags:
  - machine-learning
  - fine-tuning
  - adapters
timestamp: "2026-06-19T18:52:40.627Z"
---

# Low-Rank Adaptation (LoRA)

**Low-Rank Adaptation (LoRA)** is a parameter-efficient fine‑tuning (PEFT) technique that reduces the number of trainable parameters in a large language model by injecting small, trainable adapter layers while keeping the original model weights frozen. This approach makes fine‑tuning significantly more memory‑efficient and faster than full fine‑tuning. ^[large-language-models-llms-databricks-on-aws.md]

## How LoRA Works

LoRA adds low‑rank decomposition matrices to specific layers of the pre‑trained model — typically the attention projection layers (query, key, value, output) and feed‑forward layers (gate, up, down projections). Instead of updating the full weight matrix, only these low‑rank adapters are trained, drastically reducing the number of parameters that need to be stored and optimised. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

The key hyperparameter is the **rank** (`r`), which controls the size of the adapter matrices. Typical values are 8, 16, 32, 64, or 128. A smaller rank means fewer trainable parameters and less memory usage, while a larger rank may capture more task‑specific information at the cost of efficiency. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

Additional configuration options include:

- `lora_alpha`: scaling factor for the LoRA update.
- `lora_dropout`: dropout rate applied to the adapter (often set to 0 for efficiency).
- `bias`: whether to train bias parameters (`"none"` is the default).
- `target_parameters` / `target_modules`: which layers receive adapters (e.g., all linear layers, or specific named modules). ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Using LoRA in Fine‑Tuning

In practice, LoRA is applied via a PEFT wrapper such as Hugging Face's `peft` library. The base model is loaded, then a `LoraConfig` is defined, and `get_peft_model()` converts the original model into a PEFT model that contains the LoRA adapters. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

The example configuration for a 120B parameter GPT‑OSS model uses a rank of 32 with LoRA on all linear layers and per‑module rank adjustments for MoE sub‑layers: ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

```python
peft_config = LoraConfig(
    r=32,
    lora_alpha=32,
    target_modules="all-linear",
    rank_pattern={
        "mlp.experts.gate_up_proj": 8,
        "mlp.experts.down_proj": 8
    },
    target_parameters=["mlp.experts.gate_up_proj", "mlp.experts.down_proj"],
    lora_dropout=0.0,
    bias="none",
    task_type="CAUSAL_LM",
)
model = get_peft_model(model, peft_config)
```

When fine‑tuning a smaller model like Llama‑3.2‑3B, the same pattern is followed with a rank of 16 and adapters applied only to the attention and feed‑forward projection layers: ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

```python
model = FastLanguageModel.get_peft_model(
    model,
    r=16,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                    "gate_proj", "up_proj", "down_proj"],
    lora_alpha=16,
    lora_dropout=0,
    bias="none",
    use_gradient_checkpointing="unsloth",
    random_state=3407,
    use_rslora=False,
    loftq_config=None,
)
```

## Merging LoRA Adapters

After training, the LoRA adapter weights can be merged into the base model to produce a single, deployable model. This eliminates the need to keep the adapters as separate files and simplifies serving. The merge operation is typically exposed through a method like `model.merge_and_unload()`. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Advantages

- **Memory efficiency**: Only the adapter weights and their gradients are stored and updated, making it possible to fine‑tune very large models (e.g., 120B parameters) on a single node with limited GPU memory. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]
- **Faster training**: Fewer parameters to update means shorter training times.
- **Parameter retention**: The original base model weights remain frozen, reducing the risk of catastrophic forgetting.
- **Portability**: The small adapter files can be easily shared and swapped for different tasks.

## Related Concepts

- [Parameter‑Efficient Fine‑Tuning (PEFT)](/concepts/parameter-efficient-fine-tuning-peft.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Supervised Fine‑Tuning (SFT)](/concepts/supervised-fine-tuning-sft.md)
- [Unsloth](/concepts/unsloth.md)
- Hugging Face Transformers
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)

## Sources

- large-language-models-llms-databricks-on-aws.md
- finetune-llama-32-3b-with-unsloth-databricks-on-aws.md

# Citations

1. [large-language-models-llms-databricks-on-aws.md](/references/large-language-models-llms-databricks-on-aws-bfc38cd2.md)
2. [finetune-llama-32-3b-with-unsloth-databricks-on-aws.md](/references/finetune-llama-32-3b-with-unsloth-databricks-on-aws-83073ff0.md)
