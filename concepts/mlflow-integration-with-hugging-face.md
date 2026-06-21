---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e61ed8b47e78ac6944e7279f8cbcc407f356e4a09c7cf0ed950059341b74a2fb
  pageDirectory: concepts
  sources:
    - fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-integration-with-hugging-face
    - MIWHF
  citations:
    - file: fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md
title: MLflow Integration with Hugging Face
description: Logging Hugging Face models to MLflow using mlflow.transformers.log_model, including automatic metric logging via MLflowCallback and model artifact management.
tags:
  - mlflow
  - model-registry
  - experiment-tracking
timestamp: "2026-06-19T18:50:03.059Z"
---

# MLflow Integration with Hugging Face

The **MLflow Integration with Hugging Face** enables seamless tracking, logging, and serving of Hugging Face Transformer models within the MLflow ecosystem. On Databricks, this integration is particularly used when fine-tuning Hugging Face models on single or multi‑GPU clusters, allowing practitioners to combine Hugging Face’s training utilities with MLflow’s experiment tracking and model registry capabilities.

## How MLflow Integrates with Hugging Face

MLflow provides a built-in `MLflowCallback` that automatically logs training metrics (e.g., loss, accuracy) during Hugging Face `Trainer` runs. The callback is activated out of the box; you do not need to configure it manually. Metrics are logged for each step or epoch depending on your evaluation strategy. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

However, the trained model itself is **not** automatically logged — you must log it explicitly. The recommended approach is to wrap the training call in an `mlflow.start_run()` context, then call `mlflow.transformers.log_model()` after training completes. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Logging a Fine‑Tuned Model

After training, you can log the model as a Hugging Face pipeline (tokenizer + model) or as a dictionary of components. Use `mlflow.transformers.log_model()` to persist the model to MLflow.

### Logging as a Pipeline

Construct a `transformers.pipeline` from the saved model and tokenizer, then log it:

```python
from transformers import pipeline

with mlflow.start_run() as run:
    trainer.train()
    trainer.save_model(model_output_dir)
    pipe = pipeline(
        "text-classification",
        model=AutoModelForSequenceClassification.from_pretrained(model_output_dir),
        tokenizer=tokenizer,
        batch_size=1
    )
    model_info = mlflow.transformers.log_model(
        transformers_model=pipe,
        artifact_path="classification",
        input_example="Hi there!",
    )
```

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

### Logging Components Directly

If you do not need a pipeline, you can submit the model and tokenizer in a dictionary:

```python
model_info = mlflow.transformers.log_model(
    transformers_model={"model": trainer.model, "tokenizer": tokenizer},
    task="text-classification",
    artifact_path="text_classifier",
    input_example=["MLflow is great!", "MLflow on Databricks is awesome!"],
)
```

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Loading the Model for Inference

Once logged, the model can be loaded as a Spark UDF for batch inference or served via [Model Serving](/concepts/model-serving.md). Use the [MLflow Run](/concepts/mlflow-run.md) URI to reference the logged model:

```python
logged_model = "runs:/{run_id}/{model_artifact_path}".format(
    run_id=run.info.run_id,
    model_artifact_path=model_artifact_path
)
loaded_model_udf = mlflow.pyfunc.spark_udf(spark, model_uri=logged_model, result_type='string')
test = test.select(test.text, test.label, loaded_model_udf(test.text).alias("prediction"))
display(test)
```

^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]

## Best Practices

- **Wrap training in an MLflow run** to capture all auto‑logged metrics together with the model artifact. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]
- **Use `mlflow.transformers.log_model()` with an input example** to provide sample data for the model’s signature and to enable easier debugging. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]
- **Log components as a dictionary** when you want finer control over the artifact or when building a custom pipeline later. ^[fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md]
- **Leverage the MLflow Model Registry** to manage model versions and promote models to staging or production.

## Related Concepts

- [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md)
- [MLflow Model Registry](/concepts/mlflow-model-registry.md)
- Hugging Face Transformers on Databricks
- [Fine-tuning Hugging Face models with Transformers](/concepts/hugging-face-transformers-trainer.md)
- [Model Serving with MLflow](/concepts/model-serving.md)
- Spark UDF for Batch Inference

## Sources

- fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md

# Citations

1. [fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws.md](/references/fine-tune-hugging-face-models-for-a-single-gpu-databricks-on-aws-e2c49846.md)
