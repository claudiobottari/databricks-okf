---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 093912e1f5c3588f7a06a54628c083da05274df2745ebdb9ccef2115e39f2f83
  pageDirectory: concepts
  sources:
    - deploy-python-code-with-model-serving-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - preprocessing-and-postprocessing-with-custom-pyfunc
    - Postprocessing with Custom PyFunc and Preprocessing
    - PAPWCP
  citations:
    - file: deploy-python-code-with-model-serving-databricks-on-aws.md
title: Preprocessing and Postprocessing with Custom PyFunc
description: Using custom pyfunc models to add preprocessing (before model inference) and postprocessing (after model inference) logic to model serving pipelines
tags:
  - mlflow
  - model-serving
  - data-pipeline
timestamp: "2026-06-18T12:00:32.949Z"
---

# Preprocessing and Postprocessing with Custom PyFunc

**Preprocessing and Postprocessing with Custom PyFunc** refers to the practice of using MLflow's Python function (`pyfunc`) model format to encapsulate data transformation logic — both before and after model inference — into a single deployable artifact. This approach is particularly valuable when raw inputs require formatting before being passed to a model, or when model outputs need to be transformed for downstream consumption. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Use Cases

The custom PyFunc pattern is appropriate in several scenarios: ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

- Your model requires preprocessing before inputs can be passed to the model's predict function.
- Your model framework is not natively supported by MLflow.
- Your application requires the model's raw outputs to be post-processed for consumption.
- The model itself has per-request branching logic.
- You are looking to deploy fully custom code as a model.

## Constructing a Custom PyFunc Model

MLflow offers a [custom Python models format](/concepts/custom-mlflow-pythonmodel.md) for packaging arbitrary Python code. A custom PyFunc model must implement two required functions: ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### `load_context`

This function handles any one-time initialization that the model needs to operate. Defining expensive operations (such as loading model weights, tokenizers, or other artifacts) here ensures they are loaded only once, minimizing the work performed during every `predict` call and speeding up inference. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### `predict`

This function contains all the logic that runs every time an input request is made. It receives the model input and returns the final output after any preprocessing or postprocessing steps. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### Example

The following example shows a custom PyFunc model that loads a PyTorch model and a custom tokenizer in `load_context`, formats inputs, runs inference, and formats outputs in `predict`: ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
import mlflow
import torch

class CustomModel(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        self.model = torch.load(context.artifacts["model-weights"])
        from preprocessing_utils.my_custom_tokenizer import CustomTokenizer
        self.tokenizer = CustomTokenizer(context.artifacts["tokenizer_cache"])
    
    def format_inputs(self, model_input):
        # insert some code that formats your inputs
        pass
    
    def format_outputs(self, outputs):
        predictions = (torch.sigmoid(outputs)).data.numpy()
        return predictions
    
    def predict(self, context, model_input):
        model_input = self.format_inputs(model_input)
        outputs = self.model.predict(model_input)
        return self.format_outputs(outputs)
```

## Logging the Model

When logging a PyFunc model on a Databricks Runtime ML runtime, it is important to specify `mlflow` (not `mlflow-skinny`) in the `pip_requirements` parameter, because Databricks Runtime ML includes `mlflow-skinny` by default and Model Serving requires the full `mlflow` package to build the container image. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
# DBR ML ships with mlflow-skinny by default, so specify mlflow explicitly
# to ensure Model Serving compatibility.
mlflow.pyfunc.log_model(
    name="model",
    python_model=your_model,
    pip_requirements=["mlflow==3.8.1"],  # use mlflow, not mlflow-skinny
    registered_model_name="catalog.schema.model_name",
)
```

^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Sharing Code Across Models

Even when writing a model with custom code, it is possible to use shared modules from your organization. The `code_path` parameter allows model authors to log full code references that load into the path and are usable from other custom PyFunc models. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

For example, if a model is logged with:

```python
mlflow.pyfunc.log_model(CustomModel(), "model", code_path=["preprocessing_utils/"])
```

Code from the `preprocessing_utils` directory is available in the loaded context of the model. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Validation Before Deployment

Prior to deploying custom code as a model, it is beneficial to verify that the model is capable of being served. MLflow provides `mlflow.models.predict` for [validating models before deployment](/concepts/model-validation-before-deployment.md). ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Serving the Model

After logging a custom PyFunc model, it can be registered to [Unity Catalog](/concepts/unity-catalog.md) or [Workspace Registry](/concepts/workspace-model-registry.md) and served to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md). ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Related Concepts

- MLflow PyFunc — The Python function model flavor in MLflow
- [Model Serving](/concepts/model-serving.md) — The deployment platform for hosting models
- [Custom Python Models Format](/concepts/custom-mlflow-pythonmodel.md) — The MLflow convention for packaging arbitrary Python code
- MLflow Models — The standard format for packaging machine learning models
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer for model registration and discovery

## Sources

- deploy-python-code-with-model-serving-databricks-on-aws.md

# Citations

1. [deploy-python-code-with-model-serving-databricks-on-aws.md](/references/deploy-python-code-with-model-serving-databricks-on-aws-84536f0c.md)
