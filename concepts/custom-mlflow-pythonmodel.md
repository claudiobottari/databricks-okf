---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e408fd4b9f1059fb226eb58117e0c61778bd145f27086c1bc61aaba5d46dc713
  pageDirectory: concepts
  sources:
    - deploy-python-code-with-model-serving-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-mlflow-pythonmodel
    - CMP
    - Custom MLflow Python Function Model
    - MLflow PythonModel
    - custom MLflow Python model
    - custom Python model
    - Custom MLflow Python Function Models
    - Custom Python Function Models
    - Custom Python Models (MLflow)
    - Custom Python Models Format
    - MLflow Python Function Model
    - PythonModel
    - custom Python models format
    - custom model
    - custom models
  citations:
    - file: deploy-python-code-with-model-serving-databricks-on-aws.md
title: Custom MLflow PythonModel
description: Pattern for packaging arbitrary Python code as an MLflow model by implementing load_context and predict methods in a class that extends mlflow.pyfunc.PythonModel
tags:
  - mlflow
  - model-serving
  - python
timestamp: "2026-06-18T11:59:32.019Z"
---

# Custom MLflow PythonModel

A **Custom MLflow PythonModel** (also referred to as a custom `pyfunc` model) enables you to package arbitrary Python code and deploy it through [Model Serving](/concepts/model-serving.md). Using MLflow’s Python function (`pyfunc`) format, you can wrap preprocessing, inference, and postprocessing logic into a single deployable artifact. This approach is ideal when your model framework is not natively supported by MLflow, when you need to apply input transformations before prediction, or when you want to post-process raw model outputs for consumption. It also supports per-request branching logic and fully custom code execution. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Why use a custom PythonModel?

The following scenarios benefit from a custom PythonModel:

* Your model requires preprocessing before inputs can be passed to the model’s `predict` function.
* Your model framework is not natively supported by MLflow.
* Your application requires the model’s raw outputs to be post-processed (e.g., converting logits to probabilities).
* The model itself has per-request branching logic.
* You want to deploy fully custom code as a model. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Required functions

Every custom PythonModel must implement two methods:

- **`load_context(self, context)`** – This function runs once when the model is loaded. It is the correct place to initialize heavy artifacts such as model weights, tokenizers, or other dependencies that should not be recreated on every prediction request. Minimising the work done in `predict` speeds up inference.
- **`predict(self, context, model_input)`** – This function contains all logic that runs for every input request. It receives the input data and the context object (populated by `load_context`) and returns the model’s prediction. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### Example skeleton

The following example shows a custom model that loads a PyTorch model and a custom tokenizer:

```python
import mlflow.pyfunc

class CustomModel(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        self.model = torch.load(context.artifacts["model-weights"])
        from preprocessing_utils.my_custom_tokenizer import CustomTokenizer
        self.tokenizer = CustomTokenizer(context.artifacts["tokenizer_cache"])

    def format_inputs(self, model_input):
        # Insert preprocessing logic
        return model_input

    def format_outputs(self, outputs):
        predictions = (torch.sigmoid(outputs)).data.numpy()
        return predictions

    def predict(self, context, model_input):
        model_input = self.format_inputs(model_input)
        outputs = self.model.predict(model_input)
        return self.format_outputs(outputs)
```

## Logging the model

To register your custom PythonModel, use `mlflow.pyfunc.log_model()`. A critical detail when working on [Databricks Runtime ML](/concepts/databricks-runtime-ml.md): those runtime images ship `mlflow-skinny` by default rather than the full `mlflow` package. If you do not explicitly specify `pip_requirements`, MLflow captures `mlflow-skinny` in the model’s `conda.yaml`. Model Serving requires the full `mlflow` package and cannot build the container image otherwise. Therefore, always include `"mlflow==<version>"` in `pip_requirements`:

```python
mlflow.pyfunc.log_model(
    name="model",
    python_model=your_model,
    pip_requirements=["mlflow==3.8.1"],  # use mlflow, not mlflow-skinny
    registered_model_name="catalog.schema.model_name",
)
```

^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### Using shared modules (`code_path`)

Even when writing a custom model, you can reuse shared code from your organisation. The `code_path` parameter lets you log full code references that are added to the Python path when the model is loaded. For example:

```python
mlflow.pyfunc.log_model(CustomModel(), "model", code_path=["preprocessing_utils/"])
```

Then, inside `load_context` or `predict`, you can import modules from `preprocessing_utils` as if they were installed packages. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Serving the model

After the model is logged and registered to [Unity Catalog](/concepts/unity-catalog.md) or the [Workspace Registry](/concepts/workspace-model-registry.md), you can deploy it by creating a Model Serving endpoint. The endpoint will automatically load your custom PythonModel and serve predictions via a REST API. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Notebook example

For a complete walkthrough, see the Databricks notebook *Customize model serving output with MLflow PyFunc* (referenced in the source documentation). That notebook demonstrates how to apply postprocessing to model outputs before serving. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Sources

- deploy-python-code-with-model-serving-databricks-on-aws.md

# Citations

1. [deploy-python-code-with-model-serving-databricks-on-aws.md](/references/deploy-python-code-with-model-serving-databricks-on-aws-84536f0c.md)
