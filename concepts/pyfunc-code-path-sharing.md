---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 78cf668b61a18a97228dcf18ad551dbf3fda7027de4ee0d00553c716307604f9
  pageDirectory: concepts
  sources:
    - deploy-python-code-with-model-serving-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pyfunc-code-path-sharing
    - PCPS
  citations:
    - file: deploy-python-code-with-model-serving-databricks-on-aws.md
title: PyFunc Code Path Sharing
description: Using the code_path parameter in mlflow.pyfunc.log_model to include shared utility modules that can be imported and used inside custom pyfunc model implementations.
tags:
  - mlflow
  - code-organization
  - python
timestamp: "2026-06-19T18:30:58.240Z"
---

# PyFunc Code Path Sharing

**PyFunc Code Path Sharing** is a mechanism in [MLflow](/concepts/mlflow.md) that allows custom Python function (pyfunc) models to reuse shared modules of code from across an organization. By specifying a `code_path` parameter when logging a model, authors can include full code references that are loaded into the Python path and become usable from other custom pyfunc models. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Overview

When constructing a custom [MLflow Python Function Model](/concepts/custom-mlflow-pythonmodel.md), developers often need to use utility code such as custom tokenizers, preprocessing functions, or other shared libraries. PyFunc Code Path Sharing enables this by packaging the referenced code alongside the model artifacts, ensuring that the code is available when the model is loaded for inference. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Usage

To share code paths, use the `code_path` parameter in `mlflow.pyfunc.log_model()`. This parameter accepts a list of paths to Python files or directories containing Python modules. The referenced code is then available in the loaded context of the model. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### Example

```python
mlflow.pyfunc.log_model(
    CustomModel(), 
    "model", 
    code_path=["preprocessing_utils/"]
)
```

Code from the `preprocessing_utils` directory is then available for import in the model's `load_context` method: ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

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

## Benefits

Code path sharing enables several important patterns in model deployment:

- **Reusability**: Common preprocessing, postprocessing, or tokenization logic can be defined once and shared across multiple models. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]
- **Consistency**: Shared code ensures consistent behavior across different models that use the same utility functions. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]
- **Maintainability**: Updates to shared code are reflected across all models that reference it, reducing duplication and maintenance overhead. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Serving Compatibility

After logging a custom pyfunc model with shared code paths, the model can be registered to [Unity Catalog](/concepts/unity-catalog.md) or Workspace Registry and served to a [Model Serving](/concepts/model-serving.md) endpoint. For compatibility with Model Serving, models logged on Databricks Runtime ML must specify `mlflow` (not `mlflow-skinny`) in `pip_requirements`. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Related Concepts

- [MLflow Python Function Model](/concepts/custom-mlflow-pythonmodel.md) — The custom model format that supports code path sharing.
- [Model Serving](/concepts/model-serving.md) — The deployment infrastructure for serving custom pyfunc models.
- [Unity Catalog](/concepts/unity-catalog.md) — Model registry for managing and deploying models.
- [PyFunc Model Logging](/concepts/custom-mlflow-pyfunc-model.md) — The process of packaging custom Python code with MLflow.
- Model Preprocessing and Postprocessing — Common use cases for shared code utilities.

## Sources

- deploy-python-code-with-model-serving-databricks-on-aws.md

# Citations

1. [deploy-python-code-with-model-serving-databricks-on-aws.md](/references/deploy-python-code-with-model-serving-databricks-on-aws-84536f0c.md)
