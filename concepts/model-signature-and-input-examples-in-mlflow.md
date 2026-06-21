---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7a09508c3aaad1b1f84b0b2f743d108c2fa8b0e7e7fa4c68e82bba0510fa6c39
  pageDirectory: concepts
  sources:
    - custom-models-overview-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-signature-and-input-examples-in-mlflow
    - Input Examples in MLflow and Model Signature
    - MSAIEIM
  citations:
    - file: custom-models-overview-databricks-on-aws.md
title: Model Signature and Input Examples in MLflow
description: Recommended practice of adding signatures (via infer_signature) and input examples when logging models; signatures are required for logging to Unity Catalog.
tags:
  - mlflow
  - model-logging
  - best-practices
timestamp: "2026-06-18T14:58:12.470Z"
---

# Model Signature and Input Examples in MLflow

**Model Signature and Input Examples** are metadata components in MLflow that document the expected interface of a machine learning model. A **model signature** defines the input and output schema (data types and column names), while an **input example** provides a concrete sample of valid input data. Together, they enable robust model validation, seamless deployment, and integration with systems like [Unity Catalog](/concepts/unity-catalog.md). ^[custom-models-overview-databricks-on-aws.md]

## Model Signature

A model signature declares the expected data types for model inputs and outputs. It is inferred automatically from training data using `mlflow.models.signature.infer_signature()` and passed as the `signature` parameter when logging a model. ^[custom-models-overview-databricks-on-aws.md]

### Usage

Signatures are **required** for logging models to the [Unity Catalog](/concepts/unity-catalog.md). They provide:

- **Type safety**: Ensures that inference requests match the expected schema.
- **Automatic validation**: Catches mismatches between training-time and serving-time data at registration or deployment.
- **Documentation**: Makes the model’s contract explicit in the MLflow UI and API.

### Example

```python
from mlflow.models.signature import infer_signature

# training_data and model predictions are used to infer the schema
signature = infer_signature(training_data, model.predict(training_data))
mlflow.sklearn.log_model(model, "model", signature=signature)
```

^[custom-models-overview-databricks-on-aws.md]

## Input Example

An **input example** provides a concrete sample of valid model input, typically a dictionary or a small DataFrame snippet. It is passed as the `input_example` parameter when logging a model. ^[custom-models-overview-databricks-on-aws.md]

### Benefits

- **Documentation**: Makes it easy to understand the expected input format.
- **Testing**: Enables automatic validation of the model’s prediction logic.
- **Debugging**: Helps verify that the model works correctly with representative data.

### Example

```python
input_example = {"feature1": 0.5, "feature2": 3}
mlflow.sklearn.log_model(model, "model", input_example=input_example)
```

^[custom-models-overview-databricks-on-aws.md]

## Best Practices

1. **Add a signature for all models** – Required for Unity Catalog registration; recommended for workspace registry.
2. **Use realistic input examples** – Provide data that mirrors production distributions.
3. **Update signatures when model schema changes** – Retrain or re-log to keep the signature in sync.
4. **Validate before deployment** – Use [Pre-deployment Validation for Model Serving](/concepts/pre-deployment-validation-for-model-serving.md) to catch issues early. ^[custom-models-overview-databricks-on-aws.md]

## Related Concepts

- MLflow Models – The core abstraction for packaging models.
- [MLflow Flavors](/concepts/mlflow-model-flavors.md) – Built-in flavors (sklearn, pytorch, transformers, pyfunc) that integrate with signatures.
- [Unity Catalog](/concepts/unity-catalog.md) – The recommended registry that requires signatures for model registration.
- [Model Serving](/concepts/model-serving.md) – Deployment infrastructure that uses signature metadata.

## Sources

- custom-models-overview-databricks-on-aws.md

# Citations

1. [custom-models-overview-databricks-on-aws.md](/references/custom-models-overview-databricks-on-aws-920e65c5.md)
