---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bcc442dd268aeb71bcaf3b9a61048cac86b1ff353ce2b0dd9b4928f1720bafa3
  pageDirectory: concepts
  sources:
    - deploy-python-code-with-model-serving-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - pyfunc-preprocessing-and-postprocessing-patterns
    - Postprocessing Patterns and PyFunc Preprocessing
    - PPAPP
  citations:
    - file: deploy-python-code-with-model-serving-databricks-on-aws.md
title: PyFunc Preprocessing and Postprocessing Patterns
description: Custom MLflow pyfunc models can encapsulate preprocessing logic (e.g., tokenization), model inference, and postprocessing (e.g., sigmoid transformation) within the predict function, enabling end-to-end serving.
tags:
  - machine-learning
  - mlflow
  - pattern
timestamp: "2026-06-18T15:27:10.337Z"
---

# PyFunc Preprocessing and Postprocessing Patterns

**PyFunc Preprocessing and Postprocessing Patterns** refer to the common design strategies used when packaging custom Python code as an MLflow `pyfunc` model that requires transforming inputs before inference or transforming raw outputs after inference. These patterns allow practitioners to deploy models that include arbitrary preprocessing, postprocessing, or per-request branching logic — including models whose framework is not natively supported by MLflow. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Overview

When a model cannot accept raw inputs directly (e.g., it expects tokenized text, normalized features, or a specific data structure), or when its raw predictions must be formatted for consumption (e.g., converting logits to probabilities, enriching with metadata), the `pyfunc` interface provides a natural place to encapsulate that logic. The custom `pyfunc` model is logged and then served through [Model Serving](/concepts/model-serving.md), enabling production inference with the same preprocessing and postprocessing pipeline that was used during development. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Required Functions

Every custom `pyfunc` model must implement two functions: ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

- **`load_context(self, context)`** – Runs once when the model is loaded. Used to load expensive artifacts (e.g., model weights, tokenizers) that should not be re-loaded on every inference request.
- **`predict(self, context, model_input)`** – Runs on every inference request. Contains the full pipeline: preprocessing, model inference, and postprocessing.

## Common Patterns

### Preprocessing in `format_inputs`

A common pattern is to define a helper method `format_inputs` in the model class that handles all input transformations. This keeps the `predict` method clean and allows the preprocessing logic to be tested independently. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
def format_inputs(self, model_input):
    # Normalize, tokenize, or reshape inputs
    return transformed_input
```

### Postprocessing in `format_outputs`

Similarly, a `format_outputs` method encapsulates postprocessing logic such as applying a sigmoid to logits, converting confidence scores to labels, or appending metadata. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
def format_outputs(self, outputs):
    predictions = (torch.sigmoid(outputs)).data.numpy()
    return predictions
```

### Full Pipeline in `predict`

Within `predict`, the two helpers are composed to form a clean pipeline:

```python
def predict(self, context, model_input):
    model_input = self.format_inputs(model_input)
    outputs = self.model.predict(model_input)
    return self.format_outputs(outputs)
```

## Reusable Code via `code_path`

Even with a custom `pyfunc` model, it is possible to reference shared modules from your organization by using the `code_path` parameter of `mlflow.pyfunc.log_model()`. This logs additional Python code that becomes importable in the model’s loaded context. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
mlflow.pyfunc.log_model(
    CustomModel(),
    "model",
    code_path=["preprocessing_utils/"]
)
```

Inside the model class, those modules can then be imported:

```python
def load_context(self, context):
    from preprocessing_utils.my_custom_tokenizer import CustomTokenizer
    self.tokenizer = CustomTokenizer(...)
```

This promotes code reuse across multiple models while keeping each model’s custom logic self-contained. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Deployment Considerations

When logging a custom `pyfunc` model on a [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) (which ships `mlflow-skinny` by default), you must explicitly specify `mlflow==<version>` in `pip_requirements`. Model Serving requires the full `mlflow` package (not `mlflow-skinny`) to build the container image. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
pip_requirements=["mlflow==3.8.1"]  # use mlflow, not mlflow-skinny
```

After logging, you can register the model to [Unity Catalog](/concepts/unity-catalog.md) or the workspace registry and serve it to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) for production inference. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Related Concepts

- Custom Python Models – The MLflow format used to log `pyfunc` models.
- MLflow Pyfunc API – The `mlflow.pyfunc` module and its `PythonModel` class.
- [Model Serving](/concepts/model-serving.md) – Production serving of logged models.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The runtime environment used for training and logging.
- Code Path in MLflow Models – Parameter for sharing modules across models.

## Sources

- deploy-python-code-with-model-serving-databricks-on-aws.md

# Citations

1. [deploy-python-code-with-model-serving-databricks-on-aws.md](/references/deploy-python-code-with-model-serving-databricks-on-aws-84536f0c.md)
