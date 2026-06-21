---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4f9c23686c73d09daf1153eafa96011948ff213c6d701954692e6ea1ff40b0e9
  pageDirectory: concepts
  sources:
    - manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-signatures-in-unity-catalog
    - MSIUC
    - Model Signature
    - Model Signatures
  citations:
    - file: manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md
title: Model Signatures in Unity Catalog
description: Required schema definitions for new model versions in Unity Catalog, inferred automatically via autologging or input examples, and needed for input enforcement, AI functions, and model serving.
tags:
  - machine-learning
  - mlflow
  - model-signatures
timestamp: "2026-06-19T19:24:51.101Z"
---

# Model Signatures in Unity Catalog

**Model Signatures** in Unity Catalog define the schema of inputs and outputs expected by an MLflow model version. A model signature specifies the names, types, and structure of the data that a model accepts as input and the data it returns as output. Signatures enable automatic input validation and are required for model versions registered in Unity Catalog. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Overview

All new ML model versions registered in Unity Catalog must have a model signature. Signatures enforce type checking at inference time: if a signature is provided, model inputs are checked when making predictions, and an error is reported if the inputs do not match the expected signature. Without a signature, there is no automatic input enforcement, and models must handle unexpected inputs on their own. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Limitations of Model Versions Without Signatures

Model versions that lack signatures have several limitations on Databricks:

- No automatic input validation — inputs are not checked against a schema at inference time.
- Using a model version with [AI Functions](/concepts/ai-functions.md) requires providing a schema explicitly in the function call.
- Using a model version with [Model Serving](/concepts/model-serving.md) does not auto-generate input examples for the serving endpoint.

^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Creating Models with Signatures

### Using Autologging

[Databricks Autologging](/concepts/databricks-autologging.md) automatically logs models with signatures for many popular ML frameworks, including scikit-learn, TensorFlow, PyTorch, and others. When autologging is enabled, the model signature is captured automatically during training without requiring additional code. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

### Using Input Examples

With MLflow 2.5.0 and above, you can specify an input example in your `mlflow.<flavor>.log_model` call, and the model signature is automatically inferred from the input example. The following example demonstrates this technique: ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

```python
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

with mlflow.start_run():
    X, y = datasets.load_iris(return_X_y=True, as_frame=True)
    clf = RandomForestClassifier(max_depth=7)
    clf.fit(X, y)

    # Take the first row of the training dataset as the model input example.
    input_example = X.iloc0

    # Log the model and register it as a new version in UC.
    mlflow.sklearn.log_model(
        sk_model=clf,
        name="model",
        # The signature is automatically inferred from the input example and its predicted output.
        input_example=input_example,
        # Use three-level name to register model in Unity Catalog.
        registered_model_name="prod.ml_team.iris_model",
    )
```

^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

### Other Frameworks

For a full list of supported ML frameworks that work with autologging and signature inference, refer to the MLflow documentation on supported flavors. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Adding or Updating a Signature for an Existing Model Version

If a model version was registered without a signature, you can add one later. To add or update a model version signature, use the standard [MLflow](/concepts/mlflow.md) approach for defining model signatures. See the MLflow documentation on [model signatures](https://mlflow.org/docs/latest/ml/model/signatures/) for detailed instructions. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — The system for managing model lifecycle in Unity Catalog
- [Databricks Autologging](/concepts/databricks-autologging.md) — Automatic logging of models with signatures
- [AI Functions](/concepts/ai-functions.md) — Feature that requires model signatures for schema inference
- [Model Serving](/concepts/model-serving.md) — Deployment option that benefits from signatures for auto-generated input examples
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that hosts registered models

## Sources

- manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md

# Citations

1. [manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md](/references/manage-model-lifecycle-in-unity-catalog-databricks-on-aws-5d1bac95.md)
