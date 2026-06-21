---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f6bfd6baf2f15d2ec7c739a95de8d2f5118a99077dfa6dad5dfdee50002be413
  pageDirectory: concepts
  sources:
    - deploy-python-code-with-model-serving-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - code-path-parameter-for-shared-modules
    - CPPFSM
  citations:
    - file: deploy-python-code-with-model-serving-databricks-on-aws.md
title: Code Path Parameter for Shared Modules
description: MLflow pyfunc's code_path parameter allows logging shared utility code alongside a model, making it importable from within custom pyfunc classes.
tags:
  - mlflow
  - code-reuse
  - packaging
timestamp: "2026-06-19T15:11:37.286Z"
---

# Code Path Parameter for Shared Modules

The **Code Path Parameter for Shared Modules** is a feature of MLflow's `mlflow.pyfunc.log_model()` that allows authors of custom Python function models to include references to shared code modules. This enables the reuse of organizational code libraries across multiple custom `pyfunc` models without duplicating the code inside each model's logging call. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Overview

When logging a custom model using `mlflow.pyfunc.log_model()`, the `code_path` parameter accepts a list of paths to directories containing Python code. These code references are loaded into the model's Python path and become available for use within the model's `load_context` and `predict` methods. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Usage

The `code_path` parameter is specified when calling `mlflow.pyfunc.log_model()`. The paths provided point to directories containing shared utility code, preprocessing modules, or any other Python code that the custom model depends on. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
mlflow.pyfunc.log_model(CustomModel(), "model", code_path=["preprocessing_utils/"])
```

Code from the `preprocessing_utils` directory then becomes available in the loaded context of the model. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Example

The following custom model demonstrates how to use the `code_path` parameter to import a shared tokenizer module: ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

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

## Model Serving Compatibility

When using `code_path` on a [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) (DBR ML), note that DBR ML ships with `mlflow-skinny` by default rather than the full `mlflow` package. If you specify `pip_requirements` without including the full `mlflow` package, MLflow captures `mlflow-skinny` in the model's `conda.yaml`. [Model Serving](/concepts/model-serving.md) requires the full `mlflow` package (not `mlflow-skinny`) to build the container image. Always specify `mlflow==<version>` in `pip_requirements` when calling `mlflow.pyfunc.log_model()` on a DBR ML runtime: ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
mlflow.pyfunc.log_model(
    name="model",
    python_model=your_model,
    pip_requirements=["mlflow==3.8.1"],  # use mlflow, not mlflow-skinny
    registered_model_name="catalog.schema.model_name",
)
```

## Related Concepts

- [Custom MLflow PyFunc Models](/concepts/custom-mlflow-pythonmodel.md) – The framework for packaging arbitrary Python code as a model.
- [Model Serving](/concepts/model-serving.md) – Serving custom models as endpoints for inference.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – The runtime environment where models are logged.
- [Unity Catalog](/concepts/unity-catalog.md) – Registry for managing models with full lineage and governance.
- [Workspace Registry](/concepts/workspace-model-registry.md) – Alternative model registry for Databricks workspaces.

## Sources

- deploy-python-code-with-model-serving-databricks-on-aws.md

# Citations

1. [deploy-python-code-with-model-serving-databricks-on-aws.md](/references/deploy-python-code-with-model-serving-databricks-on-aws-84536f0c.md)
