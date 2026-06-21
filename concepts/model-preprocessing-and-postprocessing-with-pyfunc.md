---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6663ef16f5fa7dfd650852f726a947754f07c1107c5c7009e34cb9a2ab2588a9
  pageDirectory: concepts
  sources:
    - deploy-python-code-with-model-serving-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-preprocessing-and-postprocessing-with-pyfunc
    - Postprocessing with pyfunc and Model Preprocessing
    - MPAPWP
  citations:
    - file: deploy-python-code-with-model-serving-databricks-on-aws.md
title: Model Preprocessing and Postprocessing with pyfunc
description: Pattern of wrapping model inference with custom preprocessing (input formatting) and postprocessing (output transformation) logic within a single MLflow pyfunc model
tags:
  - mlflow
  - model-serving
  - databricks
timestamp: "2026-06-19T10:12:09.677Z"
---

# Model Preprocessing and Postprocessing with pyfunc

**Model Preprocessing and Postprocessing with pyfunc** refers to the practice of using MLflow's Python function (`pyfunc`) format to wrap custom logic that transforms model inputs before inference and model outputs after inference. This approach enables deployment of models that require data transformation, framework support not natively provided by MLflow, or custom per-request branching logic.

## Overview

MLflow's `pyfunc` provides flexibility to deploy any piece of Python code or any Python model as a serving endpoint. This is particularly useful when your model requires preprocessing before inputs can be passed to the model's predict function, or when your application requires the model's raw outputs to be post-processed for consumption. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

Common scenarios for using custom `pyfunc` models include:

- Models that require preprocessing before inputs can be passed to the model's predict function
- Model frameworks not natively supported by MLflow
- Applications requiring post-processing of raw model outputs
- Models with per-request branching logic
- Deploying fully custom code as a model

^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Constructing a Custom MLflow Python Function Model

MLflow offers the ability to log Python code with the custom Python models format. There are two required functions when packaging arbitrary Python code with MLflow: ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### `load_context`

The `load_context` function handles anything that needs to be loaded just one time for the model to operate. This is critical to minimize the number of artifacts loaded during the `predict` function, which speeds up inference. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### `predict`

The `predict` function houses all the logic that is run every time an input request is made. This is where preprocessing, model inference, and postprocessing logic are executed. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Example: Custom PyFunc Model with Preprocessing and Postprocessing

The following example demonstrates a custom model that loads a PyTorch model and tokenizer in `load_context`, formats inputs in a preprocessing step, and applies a sigmoid transformation in a postprocessing step: ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
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

## Using Shared Code Modules

Even when writing a model with custom code, it is possible to use shared modules of code from your organization. With the `code_path` parameter, model authors can log full code references that load into the path and are usable from other custom `pyfunc` models. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

For example, if a model is logged with:

```python
mlflow.pyfunc.log_model(CustomModel(), "model", code_path = ["preprocessing_utils/"])
```

Code from the `preprocessing_utils` directory becomes available in the loaded context of the model, as shown in the example above where `CustomTokenizer` is imported from `preprocessing_utils.my_custom_tokenizer`. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Logging the Model

When logging a `pyfunc` model on Databricks Runtime ML runtimes, it is important to specify `mlflow` (not `mlflow-skinny`) in `pip_requirements`, because Databricks Runtime ML runtimes include `mlflow-skinny` by default rather than the full `mlflow` package. Model Serving requires `mlflow` in `conda.yaml` and cannot build the container image otherwise. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
mlflow.pyfunc.log_model(
    name="model",
    python_model=your_model,
    pip_requirements=["mlflow==3.8.1"],  # use mlflow, not mlflow-skinny
    registered_model_name="catalog.schema.model_name",
)
```

## Serving the Model

After logging a custom `pyfunc` model, you can register it to Unity Catalog or Workspace Registry and serve the model to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md). Prior to deployment, it is beneficial to verify that the model is capable of being served using `mlflow.models.predict` to validate models before deployment. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Related Concepts

- MLflow PyFunc — The underlying MLflow Python function model format
- [Model Serving](/concepts/model-serving.md) — Deploying models to production endpoints
- [Unity Catalog](/concepts/unity-catalog.md) — Registering and managing models
- Custom Python Models — MLflow's custom Python models format
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — Runtime environment considerations for pyfunc models

## Sources

- deploy-python-code-with-model-serving-databricks-on-aws.md

# Citations

1. [deploy-python-code-with-model-serving-databricks-on-aws.md](/references/deploy-python-code-with-model-serving-databricks-on-aws-84536f0c.md)
