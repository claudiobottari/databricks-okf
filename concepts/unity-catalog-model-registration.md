---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 08d74eadf9f33a0cbc8f5c1af5e79111bc83fbdc951b604e64e8da34f4c1dfba
  pageDirectory: concepts
  sources:
    - distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
    - distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
    - lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md
    - mlflow-3-deep-learning-workflow-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - unity-catalog-model-registration
    - UCMR
    - Model Registration
  citations:
    - file: distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
    - file: distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
    - file: lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md
    - file: mlflow-3-deep-learning-workflow-databricks-on-aws.md
title: Unity Catalog Model Registration
description: The process of registering machine learning models trained with MLflow into Databricks Unity Catalog for centralized governance, versioning, and deployment.
tags:
  - mlops
  - model-registry
  - databricks
timestamp: "2026-06-19T18:32:51.648Z"
---

# Unity Catalog Model Registration

**Unity Catalog Model Registration** is the process of storing a trained machine learning model in Unity Catalog as a registered model, making it discoverable, governable, and deployable across the Databricks platform. Registration is typically performed via the MLflow API by specifying a Unity Catalog three-level namespace (`catalog.schema.model_name`), but can also be done from the MLflow UI after a model has been logged. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md, distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md, lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md, mlflow-3-deep-learning-workflow-databricks-on-aws.md]

## Methods of Registration

### Using the MLflow API

The most common method is to log a model with `mlflow.transformers.log_model()` and specify the `registered_model_name` parameter with a Unity Catalog three-level name. For fine-tuned models that use adapter weights (LoRA), the adapter must be merged into the base model before registration. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md, distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md, lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

The model can be passed as either a Hugging Face pipeline or a dictionary containing `"model"` and `"tokenizer"` keys.

**Using a pipeline** – works for models that can be wrapped in a `text-generation` pipeline:

```python
with mlflow.start_run(run_id=run_id):
    model_info = mlflow.transformers.log_model(
        transformers_model=text_gen_pipe,
        artifact_path="model",
        input_example=input_example,
        registered_model_name=full_model_name,
    )
```
^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

**Using a transformers model dictionary** – preferred for models that are not easily wrapped in a pipeline:

```python
model_info = mlflow.transformers.log_model(
    transformers_model={'model': merged_model, 'tokenizer': tokenizer},
    artifact_path="model",
    task="llm/v1/chat",
    registered_model_name=full_model_name,
)
```
^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

Optionally, the `metadata` parameter can be used to attach custom information such as the source model name, model family, or parameter count:

```python
model_info = mlflow.transformers.log_model(
    transformers_model=transformers_model,
    registered_model_name=full_model_name,
    metadata={
        "task": "llm/v1/chat",
        "pretrained_model_name": MODEL_NAME,
        "databricks_model_family": "QwenForCausalLM",
        "databricks_model_size_parameters": "0.5b_lora",
    },
)
```
^[lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

### Using the MLflow UI

In addition to the API, a model can be registered from the [MLflow Experiments](/concepts/mlflow-experiment.md) UI:

1. Open the experiment’s **Models** tab, which lists all [MLflow LoggedModel](/concepts/mlflow-loggedmodel.md)s from the experiment.
2. Click the name of the model to register, then click **Register model** in the upper-right corner.
3. Select **Unity Catalog** and either choose an existing model name or type a new name.
4. Click **Register**.

^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]

The **Models** tab (within the experiment page) is used for comparing logged models and selecting which version to register, while the model version page in [Catalog Explorer](/concepts/catalog-explorer.md) provides a broader overview for monitoring and approval in deployment workflows. ^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]

## Registration Workflows

### Fine-Tuning with LoRA

When fine-tuning large models, the training function saves LoRA adapters to a Unity Catalog volume. After training completes, the adapter is merged with the base model, loaded into a pipeline or dictionary, and registered to Unity Catalog: ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md, distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md, lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

1. Train the model and save artifacts to `/Volumes/{catalog}/{schema}/{volume}/{model_name}`.
2. Load the base model (`AutoModelForCausalLM.from_pretrained()`) and tokenizer.
3. Load the adapter with `PeftModel.from_pretrained(base_model, adapter_dir)`.
4. Merge and unload the adapter using `merge_and_unload()`.
5. Create a pipeline or a dictionary with the merged model and tokenizer.
6. Log the model with `mlflow.transformers.log_model()` using the Unity Catalog model name. If the training run was tracked by MLflow, pass the `run_id` to the `start_run` context to associate the registered model with the training run.

The same pattern applies regardless of the training library used ([TRL](/concepts/trl-transformer-reinforcement-learning-library.md) or [Liger Kernels](/concepts/liger-kernels.md)). ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md, distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md, lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md]

## Related Concepts

- [MLflow LoggedModel](/concepts/mlflow-loggedmodel.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- LoRA Fine-Tuning
- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md)
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)

## Sources

- distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
- distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
- lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md
- mlflow-3-deep-learning-workflow-databricks-on-aws.md

# Citations

1. [distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md](/references/distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws-7ee24e1a.md)
2. [distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md](/references/distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws-507af04a.md)
3. [lora-fine-tuning-of-qwen2-05b-databricks-on-aws.md](/references/lora-fine-tuning-of-qwen2-05b-databricks-on-aws-e40ade8f.md)
4. [mlflow-3-deep-learning-workflow-databricks-on-aws.md](/references/mlflow-3-deep-learning-workflow-databricks-on-aws-71fc96e5.md)
