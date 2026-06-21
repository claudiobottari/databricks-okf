---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b69b3bac990fc2c985fa9a8d1df1c34900f20344b7edd6e2afa2133f6133bd5a
  pageDirectory: concepts
  sources:
    - distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lora-adapter-merging-and-model-export
    - Model Export and LoRA Adapter Merging
    - LAMAME
  citations:
    - file: distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
title: LoRA Adapter Merging and Model Export
description: Process of merging learned LoRA adapter weights into the base model (merge_and_unload) and exporting both tokenizer and merged model for inference and registration.
tags:
  - machine-learning
  - model-export
  - lora
  - inference
timestamp: "2026-06-18T15:30:39.521Z"
---

# LoRA Adapter Merging and Model Export

**LoRA Adapter Merging and Model Export** is the process of combining a LoRA adapter with its base model into a single set of weights, then packaging the merged model for deployment or registration in a model registry. This step is necessary because a LoRA adapter is a small, separate weight matrix that must be applied on top of the base model; merging them produces a standalone model that can be served without the adapter infrastructure.

## Why Merge LoRA Adapters

When a model is fine-tuned using [PEFT (Parameter-Efficient Fine-Tuning)](/concepts/parameter-efficient-fine-tuning-peft.md) with LoRA, the training output is a set of low-rank adapter weights, not a full model. To use the fine-tuned model for inference or serving, you must load the original base model, load the adapter, and then optionally merge the adapter weights back into the base model. Merging simplifies deployment – the resulting model is a single, self-contained model that does not require the PEFT library or a separate adapter file at inference time.^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Process: Merge and Unload

In the provided example, the procedure is as follows:

1. **Load the base model** with `AutoModelForCausalLM.from_pretrained(MODEL_NAME)`.
2. **Load the tokenizer** with `AutoTokenizer.from_pretrained(MODEL_NAME)`.
3. **Wrap the base model with the trained LoRA adapter** using `PeftModel.from_pretrained(base_model, adapter_dir)`.
4. **Merge and unload** by calling `peft_model.merge_and_unload()`. The method `merge_and_unload` fuses the adapter weights into the base model’s weights and then removes the PEFT wrapper, returning a standalone `merged_model`.^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

```python
base_model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
peft_model = PeftModel.from_pretrained(base_model, adapter_dir)
merged_model = peft_model.merge_and_unload()
```

The adapter directory (`adapter_dir`) is the output path where the LoRA adapters were saved after training (e.g., a Unity Catalog volume).^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Export and Model Registration

After merging, the resulting model and tokenizer are assembled into a components dictionary. This dictionary is then logged to [MLflow](/concepts/mlflow.md) and registered in [Unity Catalog](/concepts/unity-catalog.md) for governance and deployment. The source example uses `mlflow.transformers.log_model()` with the task type `llm/v1/chat`:^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

```python
components = {
    "model": merged_model,
    "tokenizer": tokenizer,
}

with mlflow.start_run(run_id=run_id):
    model_info = mlflow.transformers.log_model(
        transformers_model=components,
        name="model",
        task=task,
        registered_model_name=full_model_name,
        metadata={
            "task": task,
            "pretrained_model_name": MODEL_NAME,
            "databricks_model_family": "Llama3.2",
        },
    )
```

The registered model is versioned and can be deployed to serving endpoints. The MLflow model URI and version are returned for downstream use.

## Benefits of Merging

- **Simplified deployment**: No need to manage separate adapter files or PEFT dependencies in the serving environment.
- **Performance**: Merged weights can be optimized by the inference engine (e.g., through quantization or compilation) more easily than a combination of base + adapter.
- **Portability**: The merged model can be saved to disk and loaded like any other Hugging Face model.

## Related Concepts

- LoRA – The low-rank adaptation technique used for efficient fine-tuning.
- PEFT – The Parameter-Efficient Fine-Tuning library that implements LoRA.
- MLflow Model Registration – Logging and versioning models in MLflow.
- [Unity Catalog](/concepts/unity-catalog.md) – Databricks’ governance catalog for models and data.
- merge_and_unload – The PEFT method that fuses adapter weights.
- [Fine-tuning with Unsloth](/concepts/lora-finetuning-with-unsloth-on-llama-32.md) – The training workflow that produces LoRA adapters.

## Sources

- distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md

# Citations

1. [distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md](/references/distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws-5c6e3457.md)
