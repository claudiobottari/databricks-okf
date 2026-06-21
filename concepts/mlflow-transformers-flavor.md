---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0a1055d11faf2f6b9706b55d9d012b8b9d2cd8df3b63107e4121538534c47545
  pageDirectory: concepts
  sources:
    - model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md
    - tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-transformers-flavor
    - MTF
    - MLflow Transformers
    - MLflow transformers
    - MLflow Transformers Integration
    - TRANSFORMERS_CACHE
    - Transformer
    - Transformers models
    - Transformers pipeline
    - transformers
  citations:
    - file: tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md
    - file: model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md
title: MLflow Transformers Flavor
description: Logging Hugging Face models to MLflow using the MLflow transformers flavor for model management and versioning
tags:
  - mlflow
  - model-registry
  - hugging-face
timestamp: "2026-06-19T19:43:09.797Z"
---

# MLflow Transformers Flavor

The **MLflow Transformers Flavor** is a built‑in MLflow model flavor that enables logging, packaging, and serving models from the Hugging Face Transformers library. Using `mlflow.transformers.log_model()`, you can save a Hugging Face pipeline along with its configuration, tokenizer, and inference parameters as a reusable MLflow model. This flavor integrates directly with [Databricks Model Serving](/concepts/databricks-model-serving.md) and the [MLflow Model Registry](/concepts/mlflow-model-registry.md). ^[tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md, model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

## Logging a Model with the Transformers Flavor

To log a Transformers model, call `mlflow.transformers.log_model()` within an [MLflow Run](/concepts/mlflow-run.md). The following example records a text‑generation pipeline (`gpt2`) and registers it in the model registry:

```python
with mlflow.start_run():
    model_info = mlflow.transformers.log_model(
        transformers_model=text_generation_pipeline,
        artifact_path="my_sentence_generator",
        inference_config=inference_config,
        registered_model_name='gpt2',
        input_example=input_example,
        signature=signature
    )
```

Required parameters include `transformers_model` (a Hugging Face pipeline or model object), `artifact_path` (the local path for artifacts), and optional arguments such as `inference_config`, `registered_model_name`, `input_example`, and `signature`. ^[tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md]

After logging, the model should be registered in either [Unity Catalog](/concepts/unity-catalog.md) or the workspace MLflow Model Registry for use in serving. ^[tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md]

## Deploying and Querying the Model

Once the model is logged and registered, you can serve it via **Model Serving**:

1. From the Databricks UI, open **Serving** → **Create serving endpoint**.
2. Provide an endpoint name and select the registered model and version.
3. Configure compute size, scale‑out, and whether the endpoint scales to zero.
4. Create the endpoint and wait for it to become ready.

To query the endpoint, use the **Query endpoint** tab in the Serving UI. Insert model input as JSON, for example:

```json
{
  "inputs": ["Hello, I'm a language model,"],
  "params": {"max_new_tokens": 10, "temperature": 1}
}
```

The endpoint accepts standard MLflow serving formats. For programmatic access, you can use the Databricks Serving API with a personal access token. ^[tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md]

## Benefits and Use Cases

- **Simplified packaging**: The flavor handles saving the complete model environment, including tokenizers and custom inference configuration.
- **Alternative to model caching**: Instead of setting the `TRANSFORMERS_CACHE` environment variable in DBFS, you can log the model with the Transformers flavor to make it portable across clusters and sessions. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]
- **Seamless deployment**: Models logged with this flavor are automatically compatible with Databricks Model Serving for both batch and real‑time inference.

## Related Concepts

- [MLflow](/concepts/mlflow.md)
- Hugging Face Transformers
- [Model Serving](/concepts/model-serving.md)
- [MLflow Model Registry](/concepts/mlflow-model-registry.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Pandas UDFs for Model Inference](/concepts/pandas-udfs-for-distributed-model-inference-on-spark.md)

## Sources

- tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md
- model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md

# Citations

1. [tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md](/references/tutorial-deploy-and-query-a-custom-model-databricks-on-aws-16c7ace5.md)
2. [model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md](/references/model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws-b5ae44ca.md)
