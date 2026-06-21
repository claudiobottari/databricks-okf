---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 586c95eb8e040873f5d3f16c34b28432e4ba928a7049c0c2c49902b734ae1615
  pageDirectory: concepts
  sources:
    - deploy-python-code-with-model-serving-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pyfunc-model-preprocessing-and-postprocessing
    - Postprocessing and PyFunc Model Preprocessing
    - PMPAP
    - Model Preprocessing and Postprocessing
  citations:
    - file: deploy-python-code-with-model-serving-databricks-on-aws.md
title: PyFunc Model Preprocessing and Postprocessing
description: Using MLflow pyfunc's predict method to encapsulate preprocessing logic (input formatting) and postprocessing logic (output transformation) within a custom model class.
tags:
  - mlflow
  - model-pipeline
  - python
timestamp: "2026-06-19T18:30:35.273Z"
---

# PyFunc Model Preprocessing and Postprocessing

**PyFunc Model Preprocessing and Postprocessing** refers to the practice of using MLflow’s Python function (`pyfunc`) model format to encapsulate arbitrary data transformation logic that runs before or after the core model’s predictions. This pattern is especially useful when a model’s raw inputs require cleaning or feature engineering, or when its raw outputs must be reformatted for downstream consumption. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Overview

MLflow’s `pyfunc` provides a flexible way to deploy any piece of Python code as a model on [Model Serving](/concepts/model-serving.md) endpoints. By packaging custom preprocessing and postprocessing steps inside a single `pyfunc` model, you ensure that all necessary transformations happen automatically whenever the model is queried. Common use cases include: ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

- Preprocessing inputs before passing them to a model’s predict function (e.g., tokenization, normalization).
- Postprocessing raw model outputs for consumption (e.g., converting logits to probabilities, formatting responses).
- Handling models whose framework is not natively supported by MLflow.
- Implementing per‑request branching logic.
- Deploying fully custom code as a model.

## Key Concepts

### Preprocessing

Preprocessing logic is invoked inside the `predict` method of a custom `pyfunc` model, *before* the core model is called. This can include cleaning, feature extraction, encoding, or any other transformation required to make raw input data compatible with the model’s expected interface. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### Postprocessing

Postprocessing logic runs *after* the core model’s predictions and transforms the raw output into a format suitable for the end user or application. Examples include applying a sigmoid activation, rounding, converting tensor outputs to lists, or structuring a response. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Constructing a Custom PyFunc Model

When building a custom `pyfunc` model, you implement two required methods defined in `mlflow.pyfunc.PythonModel`: ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

- **`load_context(self, context)`:**
  Called once when the model is loaded. Use it to initialize heavy or persistent artifacts (e.g., a pre‑trained model, a tokenizer, a lookup table). This keeps the `predict` method fast. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

- **`predict(self, context, model_input)`:**
  Called for every inference request. This method houses all logic that runs per request, including preprocessing, the core model call, and postprocessing. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

The following example illustrates a custom model that performs both formatting of inputs and postprocessing of outputs: ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
import mlflow

class CustomModel(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        self.model = torch.load(context.artifacts["model-weights"])
        from preprocessing_utils.my_custom_tokenizer import CustomTokenizer
        self.tokenizer = CustomTokenizer(context.artifacts["tokenizer_cache"])

    def format_inputs(self, model_input):
        # Preprocessing logic
        pass

    def format_outputs(self, outputs):
        # Postprocessing logic
        predictions = (torch.sigmoid(outputs)).data.numpy()
        return predictions

    def predict(self, context, model_input):
        model_input = self.format_inputs(model_input)   # preprocessing
        outputs = self.model.predict(model_input)       # core model
        return self.format_outputs(outputs)             # postprocessing
```

## Logging the Model

After defining the custom model, log it with `mlflow.pyfunc.log_model()`. When using Databricks Runtime ML, you must explicitly specify `mlflow` (not `mlflow-skinny`) in `pip_requirements` to ensure [Model Serving](/concepts/model-serving.md) compatibility: ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
mlflow.pyfunc.log_model(
    name="model",
    python_model=CustomModel(),
    pip_requirements=["mlflow==3.8.1"],
    registered_model_name="catalog.schema.model_name",
)
```

The `code_path` parameter allows you to reference shared modules (e.g., `preprocessing_utils/`) that contain reusable helper code. Those modules become available in the model’s context after loading. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Deployment

Once the custom `pyfunc` model is logged and registered (to [Unity Catalog](/concepts/unity-catalog.md) or the Workspace Registry), it can be served by creating a [Model Serving Endpoint](/concepts/model-serving-endpoint.md). The endpoint automatically invokes the `predict` method, which includes the preprocessing and postprocessing logic. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Example Notebook

The source article includes a notebook that demonstrates how to customize model serving output when the raw output of the queried model needs to be post‑processed for consumption. It walks through defining a custom `pyfunc` model, logging it, and deploying it. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Related Concepts

- MLflow PyFunc – The underlying model format used for custom Python code.
- [Model Serving](/concepts/model-serving.md) – The Databricks feature that serves models as REST endpoints.
- [Unity Catalog](/concepts/unity-catalog.md) – Model registry that can store and deploy custom models.
- [Workspace Registry](/concepts/workspace-model-registry.md) – Alternative model registry for serving.
- Custom Python Models – General MLflow guide for arbitrary Python code.

## Sources

- deploy-python-code-with-model-serving-databricks-on-aws.md

# Citations

1. [deploy-python-code-with-model-serving-databricks-on-aws.md](/references/deploy-python-code-with-model-serving-databricks-on-aws-84536f0c.md)
