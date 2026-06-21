---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 87e3bb97270bb6bafed1441db37cb8c80ae59d75b75d608e1a49d481a33c136b
  pageDirectory: concepts
  sources:
    - distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lora-low-rank-adaptation-for-llms
    - L(AFL
  citations:
    - file: distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
title: LoRA (Low-Rank Adaptation) for LLMs
description: A parameter-efficient fine-tuning technique that trains small rank-decomposition matrices on targeted modules (q_proj, k_proj, v_proj, etc.) while keeping the base model frozen, supported by Unsloth.
tags:
  - fine-tuning
  - llm
  - parameter-efficiency
timestamp: "2026-06-18T12:04:01.501Z"
---

# LoRA (Low-Rank Adaptation) for LLMs

**LoRA (Low-Rank Adaptation)** is a parameter-efficient fine-tuning technique that significantly reduces the computational resources required to adapt large language models (LLMs) to specific tasks or domains. Instead of updating all model parameters during fine-tuning, LoRA injects trainable low-rank matrices into specific layers of a pre-trained model, drastically lowering the number of parameters that need to be optimized while preserving model quality.

## How LoRA Works

During standard fine-tuning, all weights in the pre-trained model are updated. LoRA bypasses this by freezing the original model weights and inserting trainable rank decomposition matrices into specific attention layers. For a weight matrix \(W \in \mathbb{R}^{d \times k}\), LoRA approximates the update \(\Delta W\) as a product of two low-rank matrices \(B \in \mathbb{R}^{d \times r}\) and \(A \in \mathbb{R}^{r \times k}\) where \(r\) (the rank) is much smaller than \(\text{min}(d, k)\). The adapted forward pass becomes \(h = Wx + BAx\). ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### Key Parameters

When applying LoRA, practitioners configure several hyperparameters that affect model quality and memory usage: ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

- **\(r\) (rank):** Controls the size of the low-rank matrices. Common values include 8, 16, 32, 64, and 128. Higher ranks increase expressiveness but also increase the number of trainable parameters and memory requirements.
- **Alpha (\( \alpha \)):** A scaling factor that controls the influence of the LoRA update relative to the original model weights. It is used together with the rank to compute the effective learning rate for the LoRA modules.
- **Target modules:** The specific layers where LoRA adapters are injected. A common selection includes the query, key, value, and output projection matrices (`q_proj`, `k_proj`, `v_proj`, `o_proj`) along with the gating and up/down projection layers (`gate_proj`, `up_proj`, `down_proj`).
- **LoRA dropout:** A regularization parameter. Setting dropout to 0 is common and optimized for performance, though any positive value is supported.
- **Bias:** Controls whether bias parameters are trained. Setting bias to "none" is the optimized choice.
- **Rank-stabilized LoRA (rsLoRA):** An extension of standard LoRA that uses a stabilized scaling factor, optionally enabled via `use_rslora`.
- **LoftQ:** A quantization-aware variant of LoRA that can optionally be used for further memory reduction.

## LoRA vs. Full Fine-Tuning

| Aspect | Full Fine-Tuning | LoRA |
|--------|------------------|------|
| Parameters updated | All (billions) | Small fraction (millions) |
| Memory requirement | Very high (multiple GPUs) | Lower (can fit on fewer GPUs) |
| Training speed | Slower | Faster |
| Model quality | Baseline | Near-baseline for most tasks |
| Storage per checkpoint | Full model copy | Small adapter weights (~MBs) |

^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Merging and Deployment

After training, LoRA adapters can be merged into the base model for deployment. The merge operation integrates the low-rank updates directly into the original model weights and removes the PEFT (Parameter-Efficient Fine-Tuning) wrapper, producing a standard model that can be served like any other transformer: ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

```python
from peft import PeftModel
from transformers import AutoModelForCausalLM

# Load base model
base_model = AutoModelForCausalLM.from_pretrained("model-name")

# Apply LoRA adapter
peft_model = PeftModel.from_pretrained(base_model, "path/to/adapter")

# Merge LoRA into base model and unload PEFT wrapper
merged_model = peft_model.merge_and_unload()
```

The merged model can then be logged to a model registry such as [Unity Catalog](/concepts/unity-catalog.md) for governance and deployment. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Distributed Training with LoRA

LoRA is well-suited for distributed training across multiple GPUs. When training on multiple GPUs with LoRA, several considerations apply: ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

- **Device mapping:** Each GPU process must be assigned to a specific device using `torch.cuda.set_device(local_rank)`.
- **Gradient checkpointing:** For distributed data parallel (DDP) training, gradient checkpointing must use `use_reentrant=False` to avoid errors where multiple processes mark a variable as ready.
- **Per-device batch size:** The batch size per GPU is typically small (e.g., 2) with gradient accumulation steps to achieve effective batch sizes.
- **Mixed precision:** Training uses either `fp16` or `bf16` depending on GPU capability. Bfloat16 is supported on Ampere and later architectures.

### Example Configuration for Distributed LoRA

The following shows a typical LoRA configuration used in distributed settings: ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

| Parameter | Typical Value | Purpose |
|-----------|---------------|---------|
| Rank (`r`) | 16 | Balances capacity and efficiency |
| Alpha | 16 | Default scaling factor |
| Target modules | `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj` | Covers all attention and MLP transformations |
| Dropout | 0 | Optimized for performance |
| Bias | "none" | Reduces parameter count |
| Gradient checkpointing | Enabled with non-reentrant | Saves memory during distributed training |

## Training Configuration

During LoRA fine-tuning, the standard training arguments are similar to full fine-tuning but adjusted for the parameter-efficient nature of LoRA: ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

- **Learning rate:** Typically higher than full fine-tuning (e.g., 2e-4 vs 1e-5).
- **Optimizer:** `adamw_8bit` is commonly used for memory efficiency.
- **LR scheduler:** Linear scheduling with warmup steps.
- **Max sequence length:** Determined by model capacity and task requirements.
- **Packing:** Short sequences can optionally be packed together to speed training by up to 5x.

## Best Practices

- **Choose rank appropriately:** Start with rank 16 for most tasks. Increase to 32, 64, or 128 for tasks requiring higher model capacity. Lower ranks (8) are more memory-efficient but may underfit on complex tasks. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]
- **Target multiple modules:** Including both attention and MLP projections generally yields better quality than targeting attention layers alone. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]
- **Use gradient checkpointing:** Essential for training large models on limited GPU memory. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]
- **Monitor with MLflow:** Track training metrics and model artifacts using [MLflow Tracking](/concepts/mlflow-tracking.md) for reproducibility and comparison across experiments. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]
- **Register in a model registry:** After merging, log the complete model to a registry like Unity Catalog for governance, versioning, and deployment. ^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Limitations and Considerations

- **Expressiveness:** For tasks requiring significant adaptation, full fine-tuning may still outperform LoRA. The low-rank constraint limits the model's ability to learn entirely new representations.
- **Task complexity:** Very complex or domain-shifted tasks may require higher rank values or alternative PEFT methods.
- **Inference overhead:** When LoRA adapters are not merged, inference requires computing the low-rank updates separately, adding marginal latency. Merging eliminates this overhead.

## Related Concepts

- [Parameter-Efficient Fine-Tuning (PEFT)](/concepts/parameter-efficient-fine-tuning-peft.md) — The broader family of methods that includes LoRA
- [QLoRA](/concepts/qlora-quantized-low-rank-adaptation.md) — A quantized variant of LoRA for further memory reduction
- [Unsloth](/concepts/unsloth.md) — An optimized framework for faster LoRA training
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Scaling training across multiple GPUs
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Experiment tracking for ML workflows
- [Unity Catalog](/concepts/unity-catalog.md) — Model governance and registry
- [Supervised Fine-Tuning (SFT)](/concepts/supervised-fine-tuning-sft.md) — The training paradigm in which LoRA is typically applied
- [Transformer](/concepts/mlflow-transformers-flavor.md) — The architecture in which LoRA adapters are injected

## Sources

- distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md

# Citations

1. [distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md](/references/distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws-5c6e3457.md)
